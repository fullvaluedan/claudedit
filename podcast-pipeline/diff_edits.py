#!/usr/bin/env python3
"""
diff_edits.py — Compare the original Whisper transcript against a re-transcription
of the edited export to learn what the editor actually kept/cut.

Usage:
    python3 diff_edits.py \
        --original  /tmp/podcast-edit/anndy-lian-web4-podcast.json \
        --edited    .context/episodes/anndy-lian-web4/transcript.edited.json \
        [--out      .context/episodes/anndy-lian-web4/edit-diff.json]

Outputs:
    - A JSON diff of kept / removed / reordered spans
    - A human-readable report to stdout
    - Candidate rules for exclusion_rules.yaml (low-value patterns found in cuts)
"""

import json
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def fmt(sec: float) -> str:
    m, s = divmod(int(sec), 60)
    return f"{m:02d}:{s:02d}"


def flatten_words(transcript: dict) -> list[dict]:
    words = []
    for seg in transcript.get("segments", []):
        for w in seg.get("words", []):
            words.append({
                "start": float(w["start"]),
                "end":   float(w["end"]),
                "word":  w["word"].strip(),
            })
    words.sort(key=lambda x: x["start"])
    return words


def flatten_text_by_segments(transcript: dict) -> list[dict]:
    segs = []
    for s in transcript.get("segments", []):
        text = s.get("text", "").strip()
        if text:
            segs.append({"start": float(s["start"]), "end": float(s["end"]), "text": text})
    return segs


LAG_RE = re.compile(
    r"\b(lagging|you.?re breaking up|we lost you|lost you there|"
    r"can.?t hear|your internet|internet went down|internet is down|"
    r"you dropped|you froze|cutting out|how.?s your (internet|connection)|"
    r"repeat the last|it cut off|restart that)\b",
    re.I,
)

TANGENT_RE = re.compile(
    r"\b(every week|once a week|weekly session|weekly series|"
    r"find a few friends|same intellectual|wavelength|couldn.?t find|"
    r"come to X more|spot on|deal flow|hong kong friend|lovely lady|"
    r"people in the building|service provider|full monopoly|"
    r"watching podcast|one.person compan|my X algorithm|vibe cod)\b",
    re.I,
)

RETAKE_RE = re.compile(
    r"\b(repeat the last|can you repeat|it cut off|restart that|"
    r"start over|do it again|one more time)\b",
    re.I,
)


def classify_removed(text: str) -> str:
    if LAG_RE.search(text):
        return "lag"
    if RETAKE_RE.search(text):
        return "retake"
    if TANGENT_RE.search(text):
        return "tangent"
    # Short filler / cross-talk
    words = [w for w in text.split() if re.match(r"\w", w)]
    if len(words) <= 6:
        return "filler/silence"
    return "content"   # real content removed — flag for review


# ---------------------------------------------------------------------------
# Core diff logic
# ---------------------------------------------------------------------------

def diff_transcripts(orig_path: str, edited_path: str) -> dict:
    orig   = json.loads(Path(orig_path).read_text())
    edited = json.loads(Path(edited_path).read_text())

    orig_segs   = flatten_text_by_segments(orig)
    edited_segs = flatten_text_by_segments(edited)

    orig_dur   = orig_segs[-1]["end"]   if orig_segs   else 0
    edited_dur = edited_segs[-1]["end"] if edited_segs else 0

    # Build a lookup of orig-source text windows matched against edited text
    # Strategy: sliding 8-word fingerprint match (robust to Whisper variation)
    def fingerprint(text: str, n: int = 8) -> list[str]:
        words = re.findall(r"\w+", text.lower())
        return [" ".join(words[i:i+n]) for i in range(len(words)-n+1)]

    edited_text_full = " ".join(s["text"] for s in edited_segs).lower()

    # Walk original segments; for each, check if its fingerprint appears in edited
    cuts = []          # removed segments
    kept = []          # kept segments
    candidate_rules = []

    for seg in orig_segs:
        prints = fingerprint(seg["text"])
        if not prints:
            continue
        found = any(p in edited_text_full for p in prints[:3])
        if found:
            kept.append(seg)
        else:
            cat = classify_removed(seg["text"])
            cuts.append({**seg, "category": cat})

    # Merge adjacent cut segments into spans
    merged_cuts = []
    for c in cuts:
        if merged_cuts and c["start"] - merged_cuts[-1]["end"] < 2.0:
            merged_cuts[-1]["end"] = c["end"]
            merged_cuts[-1]["text"] += " " + c["text"]
            # keep most severe category
            cats = {"content": 3, "retake": 2, "lag": 1, "tangent": 1, "filler/silence": 0}
            merged_cuts[-1]["category"] = max(
                [merged_cuts[-1]["category"], c["category"]],
                key=lambda x: cats.get(x, 0)
            )
        else:
            merged_cuts.append({**c})

    for cut in merged_cuts:
        cut["category"] = classify_removed(cut["text"])
        cut["duration"] = round(cut["end"] - cut["start"], 1)
        if cut["category"] in ("tangent", "content"):
            preview = cut["text"][:120]
            candidate_rules.append({
                "time": fmt(cut["start"]),
                "duration_s": cut["duration"],
                "category": cut["category"],
                "preview": preview,
                "suggested_pattern": re.findall(r"\b\w{5,}\b", cut["text"])[:6],
            })

    total_cut = sum(c["duration"] for c in merged_cuts)
    categories = {}
    for c in merged_cuts:
        categories[c["category"]] = categories.get(c["category"], 0) + 1

    return {
        "orig_duration_min":   round(orig_dur / 60, 1),
        "edited_duration_min": round(edited_dur / 60, 1),
        "total_cut_min":       round(total_cut / 60, 1),
        "cut_count":           len(merged_cuts),
        "cut_categories":      categories,
        "cuts":                merged_cuts,
        "candidate_exclusion_rules": candidate_rules,
    }


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def print_report(diff: dict):
    print()
    print("=" * 68)
    print("  EDIT DIFF REPORT")
    print("=" * 68)
    print(f"\nOriginal:  {diff['orig_duration_min']:.1f} min")
    print(f"Edited:    {diff['edited_duration_min']:.1f} min")
    print(f"Cut:       {diff['total_cut_min']:.1f} min  ({diff['cut_count']} spans)")
    print(f"By type:   {diff['cut_categories']}")

    print(f"\nCUT SPANS ({diff['cut_count']}):")
    for c in diff["cuts"]:
        flag = "  ✗ REAL CONTENT — review" if c["category"] == "content" else ""
        print(f"  [{fmt(c['start'])}–{fmt(c['end'])}] {c['category']:14s} "
              f"({c['duration']:.0f}s){flag}")
        print(f"     \"{c['text'][:90]}\"")

    if diff["candidate_exclusion_rules"]:
        print(f"\nCANDIDATE EXCLUSION RULES (add to exclusion_rules.yaml):")
        for r in diff["candidate_exclusion_rules"]:
            print(f"  [{r['time']}] {r['category']} ({r['duration_s']:.0f}s): "
                  f"\"{r['preview'][:70]}\"")
            print(f"    patterns: {r['suggested_pattern']}")

    print("=" * 68)
    print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--original", required=True)
    p.add_argument("--edited",   required=True)
    p.add_argument("--out",      default=".context/episodes/anndy-lian-web4/edit-diff.json")
    args = p.parse_args()

    print(f"Diffing transcripts...")
    diff = diff_transcripts(args.original, args.edited)
    print_report(diff)

    Path(args.out).write_text(json.dumps(diff, indent=2))
    print(f"Saved diff to {args.out}")


if __name__ == "__main__":
    main()
