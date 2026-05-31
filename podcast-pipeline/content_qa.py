#!/usr/bin/env python3
"""
content_qa.py — Content quality gate for podcast edits (transcript-only, no render).

The sequence builder's structural QA proves the Premiere sequence matches the
cut list. This stage proves the cut list itself is RIGHT by re-deriving the
edited transcript in final timeline order and having Claude re-read it:

  1. Re-derive the edited transcript (teasers → intro → main), marking every
     cut junction with its source timecode.
  2. Claude reviews it for: leftover lag/retake banter, points made twice
     (an interrupted take left in beside its re-done version), abrupt joins,
     dangling thoughts. Returns issues with source timecodes.
  3. Deterministic pre-checks (regex lag scan of kept words, duration
     accounting) run as cheap guards.
  4. FAIL the gate on any high-severity content issue.

Usage:
  python3 content_qa.py --transcript ep.json --edit content_edit.json
  python3 content_qa.py --transcript ep.json --edit content_edit.json --skip-claude

Importable:
  from content_qa import run_content_qa
  passed = run_content_qa(transcript_path, content_edit_path)
"""

import json
import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Patterns (deterministic pre-check)
# ---------------------------------------------------------------------------

LAG_RE = re.compile(
    r"\b("
    r"lagging|"
    r"you.?re breaking up|you.?re frozen|you broke up|"
    r"we lost you|lost you there|can.?t hear you|can.?t hear me|"
    r"your internet|internet went down|internet is down|internet is not|"
    r"you dropped|you froze|cutting out|cutting in and out|"
    r"repeat the last|it cut off|restart that|"
    r"how.?s your (internet|connection|signal)"
    r")\b",
    re.I,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def fmt_time(sec: float) -> str:
    m, s = divmod(int(sec), 60)
    h, m = divmod(m, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def flatten_words(transcript: dict) -> list[dict]:
    words = []
    for seg in transcript.get("segments", []):
        for w in seg.get("words", []):
            words.append({"start": float(w["start"]), "end": float(w["end"]),
                          "word": w["word"].strip()})
    words.sort(key=lambda x: x["start"])
    return words


def words_in_range(words: list[dict], start: float, end: float, slop: float = 0.1) -> list[dict]:
    return [w for w in words if w["start"] >= start - slop and w["end"] <= end + slop]


def segments_text_in_range(segments: list[dict], start: float, end: float) -> str:
    """Concatenate segment text whose midpoint falls within [start, end]."""
    out = []
    for seg in segments:
        mid = (float(seg.get("start", 0)) + float(seg.get("end", 0))) / 2
        if start - 0.1 <= mid <= end + 0.1:
            t = seg.get("text", "").strip()
            if t:
                out.append(t)
    return " ".join(out)


# ---------------------------------------------------------------------------
# Pre-check 1: lag/retake phrases in kept segments
# ---------------------------------------------------------------------------

def find_lag_in_kept(words: list[dict], main_segs: list[dict]) -> list[dict]:
    """Sliding 8-word window over each kept segment (windows never cross cuts)."""
    hits = []
    WIN = 8
    last_hit = -999.0
    for ms in main_segs:
        seg_words = words_in_range(words, float(ms["start"]), float(ms["end"]))
        for i, w in enumerate(seg_words):
            window_text = " ".join(x["word"] for x in seg_words[i:i + WIN])
            if LAG_RE.search(window_text) and w["start"] - last_hit > 15.0:
                hits.append({"at": w["start"], "text": window_text})
                last_hit = w["start"]
    return hits


# ---------------------------------------------------------------------------
# Re-derive the edited transcript in final timeline order
# ---------------------------------------------------------------------------

def ordered_clips(content_edit: dict) -> list[dict]:
    """Clips in final timeline order: teasers (top 3 by score) → intro → main."""
    clips = []
    teasers = sorted(content_edit.get("teaser_clips", []),
                     key=lambda x: -x.get("score", 0))[:3]
    for t in teasers:
        if float(t["end"]) - float(t["start"]) >= 1.0:
            clips.append({"role": "teaser", "start": float(t["start"]), "end": float(t["end"])})
    intro = content_edit.get("intro", {})
    if float(intro.get("end", 0)) > float(intro.get("start", 0)):
        clips.append({"role": "intro", "start": float(intro["start"]), "end": float(intro["end"])})
    for seg in content_edit.get("main_segments", []):
        if float(seg["end"]) - float(seg["start"]) >= 0.5:
            clips.append({"role": "main", "start": float(seg["start"]), "end": float(seg["end"])})
    return clips


def build_ordered_edit(content_edit: dict, segments: list[dict]) -> str:
    """Edited transcript in timeline order, with cut junctions marked by source TC."""
    clips = ordered_clips(content_edit)
    parts = []
    prev_end = None
    for c in clips:
        if prev_end is not None:
            parts.append(f"\n⟨cut {fmt_time(prev_end)} → {fmt_time(c['start'])}⟩")
        text = segments_text_in_range(segments, c["start"], c["end"])
        parts.append(f"[{c['role']} {fmt_time(c['start'])}-{fmt_time(c['end'])}] {text}")
        prev_end = c["end"]
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Claude review of the edited transcript
# ---------------------------------------------------------------------------

REVIEW_PROMPT = """Below is a podcast edited for publication, shown in FINAL timeline order. Each kept segment is labeled with its role (teaser/intro/main) and source timecode. Points where content was removed are marked ⟨cut MM:SS → MM:SS⟩ — these are hard cuts joining two kept parts.

Confirm the edit makes sense and flag anything an editor MUST fix before publishing. Return ONLY a JSON object:

{
  "summary": "<2-3 sentences: what this edited episode covers>",
  "issues": [
    {
      "timecode": "<MM:SS source time of the problem>",
      "type": "lag_leftover | retake_duplicate | abrupt_join | dangling_thought | other",
      "severity": "high | low",
      "quote": "<exact words involved>",
      "explanation": "<why it's a problem>"
    }
  ]
}

HIGH severity (must fix):
- lag_leftover: leftover internet/connection/retake banter — "we lost you", "how's your internet", "can you repeat the last 30 seconds", "it cut off", "or restart that", "you're lagging".
- retake_duplicate: the same point made twice because an interrupted take was left in beside its re-done version.
- abrupt_join: a ⟨cut⟩ that joins mid-thought, leaving a broken or nonsensical sentence.

LOW severity (review, won't block):
- dangling_thought: a question or idea introduced but never resolved.
- other: minor awkwardness.

If the edit is clean, return "issues": []. Quote exact words. Return ONLY the JSON."""


def review_edit_with_claude(edited_text: str) -> dict:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return {"error": "ANTHROPIC_API_KEY not set"}
    try:
        import anthropic
    except ImportError:
        return {"error": "anthropic SDK not installed"}

    client = anthropic.Anthropic()
    truncated = len(edited_text) > 120_000
    body = edited_text[:120_000] if truncated else edited_text
    try:
        msg = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=2000,
            system="You are a meticulous podcast editor doing a final content pass before publishing.",
            messages=[{"role": "user", "content": f"{REVIEW_PROMPT}\n\n--- EDITED TRANSCRIPT ---\n{body}"}],
        )
        raw = msg.content[0].text.strip()
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            m = re.search(r"\{[\s\S]*\}", raw)
            data = json.loads(m.group()) if m else {"summary": raw, "issues": []}
        data["tokens"] = msg.usage.input_tokens + msg.usage.output_tokens
        return data
    except Exception as e:
        return {"error": str(e)}


# ---------------------------------------------------------------------------
# QA runner
# ---------------------------------------------------------------------------

def run_content_qa(transcript_path, content_edit_path, skip_claude: bool = False) -> bool:
    transcript   = json.loads(Path(transcript_path).read_text())
    content_edit = json.loads(Path(content_edit_path).read_text())
    words        = flatten_words(transcript)
    segments     = transcript.get("segments", [])

    cuts      = content_edit.get("cuts", [])
    main_segs = content_edit.get("main_segments", [])
    teasers   = content_edit.get("teaser_clips", [])
    intro     = content_edit.get("intro", {})
    duration  = float(content_edit.get("duration_sec", 0))

    total_cut  = sum(float(c["end"]) - float(c["start"]) for c in cuts)
    total_kept = sum(float(s["end"]) - float(s["start"]) for s in main_segs)

    fail_reasons: list[str] = []

    print("\n" + "=" * 64)
    print("  CONTENT QA REPORT")
    print("=" * 64)
    print(f"\nSource:   {Path(content_edit.get('source', '?')).name}")
    print(f"Duration: {duration/60:.1f} min → {total_kept/60:.1f} min edit  ({total_cut/60:.1f} min cut)")

    # ── Cut summary (what each cut removed) ──────────────────────────────────
    print(f"\nCUTS ({len(cuts)}):")
    for c in cuts:
        wic = words_in_range(words, float(c["start"]), float(c["end"]))
        preview = " ".join(w["word"] for w in wic)[:70] if wic else "(no words / silence)"
        print(f"  · [{fmt_time(float(c['start']))}–{fmt_time(float(c['end']))}] "
              f"{c.get('reason', 'cut')[:34]:34s} \"{preview}\"")

    # ── Pre-check 1: lag/retake phrases left in kept content ─────────────────
    print(f"\nPRE-CHECK — lag/retake phrases in kept content:")
    lag_hits = find_lag_in_kept(words, main_segs)
    if not lag_hits:
        print("  ✓ none")
    else:
        for h in lag_hits:
            print(f"  ✗ [{fmt_time(h['at'])}] \"{h['text']}\"")
        fail_reasons.append(f"{len(lag_hits)} lag/retake phrase(s) survive in kept content")

    # ── Pre-check 2: duration accounting ─────────────────────────────────────
    accounted = total_cut + total_kept
    dur_diff = abs(accounted - duration)
    print(f"\nPRE-CHECK — duration accounting:")
    print(f"  {'✓' if dur_diff < 5 else '✗'} cuts + kept = {accounted/60:.1f} min "
          f"(source {duration/60:.1f} min, diff {dur_diff:.1f}s)")
    if dur_diff >= 60.0:
        fail_reasons.append(f"duration mismatch: {dur_diff:.0f}s unaccounted")

    # ── Teasers + intro sanity ───────────────────────────────────────────────
    print(f"\nTEASERS ({len(teasers)}):")
    for t in teasers:
        tw = words_in_range(words, float(t["start"]), float(t["end"]))
        print(f"  · [{fmt_time(float(t['start']))}] \"{(' '.join(w['word'] for w in tw))[:70]}\"")
    if not teasers:
        print("  ⚠ none selected")
    iv = float(intro.get("end", 0)) > float(intro.get("start", 0))
    print(f"INTRO: " + (f"[{fmt_time(float(intro['start']))}–{fmt_time(float(intro['end']))}]"
                        if iv else "⚠ none"))

    # ── Authoritative check: Claude reviews the edited transcript ────────────
    if not skip_claude:
        print(f"\nCLAUDE REVIEW (edited transcript in timeline order):")
        edited = build_ordered_edit(content_edit, segments)
        result = review_edit_with_claude(edited)
        if result.get("error"):
            print(f"  ⚠ Claude unavailable: {result['error']} — content not LLM-verified.")
        else:
            print(f"\n  SUMMARY: {result.get('summary', '(none)')}\n")
            issues = result.get("issues", [])
            if not issues:
                print("  ✓ No content issues flagged.")
            else:
                highs = [i for i in issues if i.get("severity") == "high"]
                for i in issues:
                    mark = "✗" if i.get("severity") == "high" else "⚠"
                    print(f"  {mark} [{i.get('timecode','?')}] {i.get('type','?')}: "
                          f"{i.get('explanation','')}")
                    if i.get("quote"):
                        print(f"       \"{i['quote'][:120]}\"")
                if highs:
                    fail_reasons.append(f"{len(highs)} high-severity content issue(s) flagged by Claude")
            if result.get("tokens"):
                print(f"\n  [{result['tokens']:,} tokens]")

    # ── Result ───────────────────────────────────────────────────────────────
    print("\n" + "=" * 64)
    if not fail_reasons:
        print("  RESULT: PASS")
    else:
        print("  RESULT: FAIL")
        for r in fail_reasons:
            print(f"    ✗ {r}")
    print("=" * 64 + "\n")
    return not fail_reasons


def main():
    import argparse
    p = argparse.ArgumentParser(description="Content QA gate for podcast edits")
    p.add_argument("--transcript", required=True)
    p.add_argument("--edit", required=True)
    p.add_argument("--skip-claude", action="store_true")
    args = p.parse_args()
    sys.exit(0 if run_content_qa(args.transcript, args.edit, skip_claude=args.skip_claude) else 1)


if __name__ == "__main__":
    main()
