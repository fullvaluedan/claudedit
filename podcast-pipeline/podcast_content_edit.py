#!/usr/bin/env python3
"""
podcast_content_edit.py — Content-aware podcast edit analysis using Claude API.

Detects silences, identifies informal/off-topic segments, finds repeats, locates
the intro, and picks the best teaser moments. Outputs content_edit.json for use
with build_content_sequence.py.

Usage:
    python3 podcast_content_edit.py \
        --source /path/to/podcast.mp4 \
        --transcript /path/to/transcript.json \
        [--output /tmp/content_edit.json]
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import anthropic

# ---------------------------------------------------------------------------
# Video / audio utilities
# ---------------------------------------------------------------------------

def get_video_duration(source_path: str) -> float:
    cmd = [
        "ffprobe", "-v", "quiet",
        "-print_format", "json",
        "-show_format",
        source_path,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    data = json.loads(result.stdout)
    return float(data["format"]["duration"])


def detect_silences(
    audio_path: str,
    t_start: float,
    t_end: float,
    min_silence: float,
    threshold_db: float,
) -> list[tuple[float, float]]:
    """Run ffmpeg silencedetect on audio_path between t_start and t_end."""
    duration = t_end - t_start
    if duration <= 0:
        return []

    cmd = [
        "ffmpeg", "-v", "error",
        "-ss", str(t_start),
        "-t", str(duration),
        "-i", str(audio_path),
        "-af", f"silencedetect=noise={threshold_db:.1f}dB:duration={min_silence:.2f}",
        "-f", "null", "-",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        output = result.stderr
    except Exception as exc:
        print(f"  [warn] silencedetect failed: {exc}")
        return []

    silences: list[tuple[float, float]] = []
    last_start: float | None = None

    for line in output.splitlines():
        if "silence_start" in line:
            try:
                raw = float(line.split("silence_start:")[1].strip().split()[0])
                last_start = t_start + raw
            except (IndexError, ValueError):
                pass
        elif "silence_end" in line:
            try:
                parts = line.split("silence_end:")[1].strip().split()
                raw_end = float(parts[0])
                file_end = t_start + raw_end
                if last_start is not None:
                    silences.append((last_start, file_end))
                    last_start = None
            except (IndexError, ValueError):
                pass

    if last_start is not None:
        silences.append((last_start, t_end))

    return silences


# ---------------------------------------------------------------------------
# Transcript utilities
# ---------------------------------------------------------------------------

def load_and_flatten_transcript(path: str) -> tuple[list[dict], list[dict], str]:
    """
    Returns (words, segments, full_text).
    Handles both flat {"words": [...]} and nested {"segments": [{"words": [...]}]}.
    """
    data = json.loads(Path(path).read_text())

    words = []
    segments = []

    if "segments" in data:
        segments = data["segments"]
        for seg in segments:
            for w in seg.get("words", []):
                words.append({
                    "word": w["word"].strip(),
                    "start": float(w["start"]),
                    "end": float(w["end"]),
                })
    elif "words" in data:
        words = [
            {"word": w["word"].strip(), "start": float(w["start"]), "end": float(w["end"])}
            for w in data["words"]
        ]

    full_text = data.get("text", " ".join(w["word"] for w in words))
    return words, segments, full_text


def find_word_gaps(words: list[dict], min_gap: float = 0.5) -> list[tuple[float, float]]:
    """Return gaps between consecutive words longer than min_gap seconds."""
    gaps = []
    for i in range(1, len(words)):
        gap_start = words[i - 1]["end"]
        gap_end = words[i]["start"]
        if gap_end - gap_start >= min_gap:
            gaps.append((gap_start, gap_end))
    return gaps


def format_transcript_for_claude(segments: list[dict], words: list[dict]) -> str:
    """Format transcript as timestamped lines for Claude."""
    lines = []
    if segments:
        for seg in segments:
            t_start = seg["start"]
            t_end = seg["end"]
            text = seg.get("text", "").strip()
            if text:
                m_s = int(t_start // 60)
                s_s = t_start % 60
                m_e = int(t_end // 60)
                s_e = t_end % 60
                lines.append(f"[{m_s:02d}:{s_s:05.2f} - {m_e:02d}:{s_e:05.2f}] {text}")
    else:
        # Fallback: group words into ~10s chunks
        chunk_start = None
        chunk_words = []
        for w in words:
            if chunk_start is None:
                chunk_start = w["start"]
            chunk_words.append(w["word"])
            if w["end"] - chunk_start >= 10.0:
                t_s, t_e = chunk_start, w["end"]
                m_s = int(t_s // 60)
                s_s = t_s % 60
                m_e = int(t_e // 60)
                s_e = t_e % 60
                lines.append(f"[{m_s:02d}:{s_s:05.2f} - {m_e:02d}:{s_e:05.2f}] {' '.join(chunk_words)}")
                chunk_start = None
                chunk_words = []
        if chunk_words and chunk_start is not None:
            t_s, t_e = chunk_start, words[-1]["end"]
            m_s = int(t_s // 60)
            s_s = t_s % 60
            m_e = int(t_e // 60)
            s_e = t_e % 60
            lines.append(f"[{m_s:02d}:{s_s:05.2f} - {m_e:02d}:{s_e:05.2f}] {' '.join(chunk_words)}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Claude analysis
# ---------------------------------------------------------------------------

ANALYSIS_PROMPT = """Analyze this podcast transcript and return a JSON object with exactly these fields:

{
  "informal_segments": [
    {"start": <float_seconds>, "end": <float_seconds>, "description": "<brief reason>"}
  ],
  "repeat_segments": [
    {
      "first": {"start": <float>, "end": <float>},
      "repeat": {"start": <float>, "end": <float>},
      "topic": "<what is repeated>"
    }
  ],
  "intro": {"start": <float>, "end": <float>, "confidence": <0.0-1.0>}
}

Rules:
- informal_segments: pre-show chat before the topic starts, post-show wind-down, tangential conversation clearly off-topic for this episode. If none, return [].
- repeat_segments: the same point, story, or statistic made more than once. Keep the BETTER version as "first", the redundant version as "repeat". If none, return [].
- intro: the segment where the host formally introduces the show, episode topic, or guest. Usually near the start. If no formal intro exists, return {"start": 0, "end": 0, "confidence": 0}.

All times must be valid float seconds matching the timestamps shown. Clips must not overlap each other.
Return ONLY valid JSON. No prose, no markdown fences."""


def analyze_with_claude(formatted_transcript: str, duration_sec: float) -> dict:
    """Call Claude API with prompt caching to analyze transcript content."""
    client = anthropic.Anthropic()

    print("  Calling Claude API for content analysis...")
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system="You are a professional podcast editor. Analyze transcripts and identify editorial structure. Return ONLY valid JSON matching the requested schema.",
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": formatted_transcript,
                    "cache_control": {"type": "ephemeral"},
                },
                {
                    "type": "text",
                    "text": ANALYSIS_PROMPT,
                },
            ],
        }],
        extra_headers={"anthropic-beta": "prompt-caching-2024-07-31"},
    )

    usage = response.usage
    cache_created = getattr(usage, "cache_creation_input_tokens", 0)
    cache_read = getattr(usage, "cache_read_input_tokens", 0)
    print(f"  Tokens: {usage.input_tokens} in, {usage.output_tokens} out"
          f" | cache_create={cache_created} cache_read={cache_read}")

    raw = response.content[0].text.strip()
    return raw, {"input": usage.input_tokens, "output": usage.output_tokens,
                 "cache_created": cache_created, "cache_read": cache_read}


def parse_and_validate_claude_response(
    raw: str, duration_sec: float
) -> dict:
    """Parse Claude's JSON response and validate/clamp all timestamps."""
    # Try direct parse, fall back to extracting first {...} block
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        match = re.search(r"\{[\s\S]*\}", raw)
        if not match:
            raise ValueError(f"No JSON found in Claude response:\n{raw[:500]}")
        data = json.loads(match.group())

    def clamp(v: float) -> float:
        return max(0.0, min(float(v), duration_sec))

    def valid_clip(s: float, e: float, min_dur=2.0, max_dur=120.0) -> bool:
        return clamp(e) - clamp(s) >= min_dur and clamp(e) - clamp(s) <= max_dur

    # Validate informal_segments
    informal = []
    for seg in data.get("informal_segments", []):
        s, e = clamp(seg.get("start", 0)), clamp(seg.get("end", 0))
        if e > s:
            informal.append({"start": s, "end": e, "description": seg.get("description", "")})

    # Validate repeat_segments
    repeats = []
    for r in data.get("repeat_segments", []):
        try:
            fs = clamp(r["first"]["start"])
            fe = clamp(r["first"]["end"])
            rs = clamp(r["repeat"]["start"])
            re_ = clamp(r["repeat"]["end"])
            if fe > fs and re_ > rs:
                repeats.append({
                    "first": {"start": fs, "end": fe},
                    "repeat": {"start": rs, "end": re_},
                    "topic": r.get("topic", ""),
                })
        except (KeyError, TypeError):
            pass

    # Validate intro
    intro_raw = data.get("intro", {})
    intro_s = clamp(intro_raw.get("start", 0))
    intro_e = clamp(intro_raw.get("end", 0))
    intro_conf = float(intro_raw.get("confidence", 0))
    if intro_conf < 0.3 or intro_e <= intro_s:
        intro = {"start": 0.0, "end": 0.0, "confidence": 0.0}
    else:
        intro = {"start": intro_s, "end": intro_e, "confidence": intro_conf}

    return {
        "informal_segments": informal,
        "repeat_segments": repeats,
        "intro": intro,
    }


# ---------------------------------------------------------------------------
# Rich content detection (lag, retake, intro, teasers) — used by the pipeline
# ---------------------------------------------------------------------------

DETECTION_PROMPT = """You are editing a single-camera podcast for publication. Above is the full timestamped transcript. Return ONLY a JSON object (no prose, no markdown fences) with this exact shape:

{
  "cuts": [
    {"start": <float_sec>, "end": <float_sec>, "type": "<category>", "confidence": <0.0-1.0>, "reason": "<short>"}
  ],
  "intro": {"start": <float_sec>, "end": <float_sec>, "confidence": <0.0-1.0>},
  "teaser_clips": [
    {"start": <float_sec>, "end": <float_sec>, "quote": "<verbatim words>", "score": <0.0-1.0>, "reason": "<short>"}
  ]
}

CUTS — regions to DELETE. Categories:
- "lag": internet/connection trouble and ALL the talk around it — "we lost you", "how's your internet", "you're lagging", "can you repeat the last 30 seconds", "it cut off", "or restart that". Include the ENTIRE exchange end-to-end, not just one sentence.
- "retake": when a point is interrupted (often by lag) and then RE-EXPLAINED later. Cut the interrupted/incomplete FIRST attempt AND the surrounding banter; KEEP the clean re-done version. Name the duplicated point in the reason.
- "false_start": abandoned sentences or mid-thought restarts ("let me... no, actually...") that lead nowhere.
- "pre_show": chit-chat before the episode topic actually begins (greetings, "how are you", small talk, "haven't posted in a while").
- "post_show": wind-down after the conversation concludes (sign-offs, "that was great", "are we still recording", logistics).
- "tangent": clearly off-topic detours unrelated to the episode subject.

Rules for cuts:
- Times must be valid floats within the transcript's range.
- Boundaries must fall between sentences at natural pauses, FULLY containing the unwanted content (do not leave half of a lag exchange behind).
- Do NOT cut normal back-channeling ("yeah", "right", "exactly") — that is natural conversation.
- Do NOT cut the intro or any teaser_clip you select.
- If unsure whether something is real content, give it LOW confidence (< 0.5).

INTRO — the formal self-introduction of the show/episode/guest. IMPORTANT: it is often recorded AFTER the main conversation, so it may appear near the END of the transcript. If there is no clear intro, return {"start":0,"end":0,"confidence":0}.

TEASER_CLIPS — pick the 3 most compelling, self-contained quotes from the MAIN content (never from pre/post-show) for a cold open. Each must stand alone and hook a viewer; spread them across the episode. "quote" must be verbatim.

Return ONLY the JSON object."""


def detect_edits_with_claude(formatted_transcript: str) -> tuple[str, dict]:
    """Single Claude call (prompt-cached) returning the raw JSON detection string."""
    client = anthropic.Anthropic()
    print("  Calling Claude for content detection (lag / retake / intro / teasers)...")
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system="You are a meticulous professional podcast editor. You remove connection problems, "
               "re-taken segments, and off-topic chatter while preserving the real conversation. "
               "Return ONLY valid JSON matching the requested schema.",
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": formatted_transcript, "cache_control": {"type": "ephemeral"}},
                {"type": "text", "text": DETECTION_PROMPT},
            ],
        }],
        extra_headers={"anthropic-beta": "prompt-caching-2024-07-31"},
    )
    usage = response.usage
    print(f"  Tokens: {usage.input_tokens} in, {usage.output_tokens} out "
          f"(cache_read={getattr(usage, 'cache_read_input_tokens', 0)})")
    return response.content[0].text.strip(), {
        "input": usage.input_tokens, "output": usage.output_tokens,
        "cache_read": getattr(usage, "cache_read_input_tokens", 0),
    }


def validate_detection(raw: str, duration_sec: float, min_confidence: float = 0.5) -> dict:
    """Parse Claude's detection JSON; clamp times; filter cuts by confidence.
    Returns {cuts, intro, teaser_clips} with unsnapped float times."""
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        match = re.search(r"\{[\s\S]*\}", raw)
        if not match:
            raise ValueError(f"No JSON found in Claude detection response:\n{raw[:500]}")
        data = json.loads(match.group())

    def clamp(v: float) -> float:
        return max(0.0, min(float(v), duration_sec))

    cuts = []
    for c in data.get("cuts", []):
        try:
            s, e = clamp(c["start"]), clamp(c["end"])
            conf = float(c.get("confidence", 0.5))
            if e - s >= 0.3 and conf >= min_confidence:
                cuts.append({
                    "start": s, "end": e,
                    "type": c.get("type", "cut"),
                    "confidence": round(conf, 2),
                    "reason": c.get("reason", ""),
                })
        except (KeyError, TypeError, ValueError):
            pass

    intro_raw = data.get("intro", {}) or {}
    i_s, i_e = clamp(intro_raw.get("start", 0)), clamp(intro_raw.get("end", 0))
    i_conf = float(intro_raw.get("confidence", 0) or 0)
    intro = ({"start": i_s, "end": i_e, "confidence": round(i_conf, 2)}
             if i_conf >= 0.3 and i_e > i_s else {"start": 0.0, "end": 0.0, "confidence": 0.0})

    teasers = []
    for t in data.get("teaser_clips", []):
        try:
            s, e = clamp(t["start"]), clamp(t["end"])
            if e - s >= 1.0:
                teasers.append({
                    "start": s, "end": e,
                    "quote": t.get("quote", ""),
                    "score": round(float(t.get("score", 0.5)), 2),
                    "reason": t.get("reason", ""),
                })
        except (KeyError, TypeError, ValueError):
            pass

    return {"cuts": cuts, "intro": intro, "teaser_clips": teasers}


# ---------------------------------------------------------------------------
# Cut / segment construction
# ---------------------------------------------------------------------------

def merge_intervals(intervals: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Merge overlapping intervals."""
    if not intervals:
        return []
    sorted_ivs = sorted(intervals)
    merged = [sorted_ivs[0]]
    for start, end in sorted_ivs[1:]:
        if start <= merged[-1][1] + 0.05:  # 50ms fudge
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged


def build_cuts(
    silence_gaps: list[tuple[float, float]],
    analysis: dict,
) -> list[dict]:
    """Combine all detected cut regions with reasons."""
    cuts = []

    for s, e in silence_gaps:
        cuts.append({"start": s, "end": e, "reason": "silence"})

    for seg in analysis["informal_segments"]:
        cuts.append({"start": seg["start"], "end": seg["end"], "reason": "informal"})

    for r in analysis["repeat_segments"]:
        cuts.append({
            "start": r["repeat"]["start"],
            "end": r["repeat"]["end"],
            "reason": f"repeat: {r['topic']}",
        })

    # Sort and merge by interval (keep reason of first in merged group)
    cuts.sort(key=lambda x: x["start"])

    merged: list[dict] = []
    for c in cuts:
        if merged and c["start"] <= merged[-1]["end"] + 0.05:
            merged[-1]["end"] = max(merged[-1]["end"], c["end"])
        else:
            merged.append(dict(c))

    return merged


def compute_main_segments(
    cuts: list[dict],
    duration_sec: float,
    intro: dict,
    min_segment: float = 0.5,
) -> list[dict]:
    """
    Compute the complement of cuts over [0, duration_sec], excluding the intro
    segment from the main body (it will be repositioned to the beginning).
    """
    # Add intro as a cut so it doesn't appear in its natural position in main
    all_cut_ivs = [(c["start"], c["end"]) for c in cuts]
    if intro["end"] > intro["start"]:
        all_cut_ivs.append((intro["start"], intro["end"]))

    merged_ivs = merge_intervals(all_cut_ivs)

    segments = []
    cursor = 0.0
    for s, e in merged_ivs:
        if s > cursor + min_segment:
            segments.append({"start": cursor, "end": s})
        cursor = e
    if duration_sec - cursor > min_segment:
        segments.append({"start": cursor, "end": duration_sec})

    return segments


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Content-aware podcast edit analysis via Claude API"
    )
    parser.add_argument("--source", required=True, help="Source video/audio file")
    parser.add_argument("--transcript", required=True, help="Whisper JSON transcript")
    parser.add_argument("--output", default="/tmp/content_edit.json", help="Output path")
    args = parser.parse_args()

    source = args.source
    print(f"Source: {source}")

    # Step 1: Duration
    print("Getting video duration...")
    duration_sec = get_video_duration(source)
    print(f"  Duration: {duration_sec:.1f}s ({duration_sec/60:.1f} min)")

    # Step 2: Silence detection
    print("Detecting silences via ffmpeg...")
    raw_silences = detect_silences(source, 0.0, duration_sec, 2.0, -40.0)
    print(f"  Found {len(raw_silences)} silence windows")

    # Step 3: Load transcript
    print("Loading transcript...")
    words, segments, full_text = load_and_flatten_transcript(args.transcript)
    print(f"  {len(words)} words, {len(segments)} segments")

    # Step 4: Word gap detection + merge with ffmpeg silences
    word_gaps = find_word_gaps(words, min_gap=2.0)
    all_silence_ivs = merge_intervals(raw_silences + word_gaps)
    print(f"  {len(all_silence_ivs)} silence intervals after merge")

    # Step 5: Format transcript for Claude
    formatted = format_transcript_for_claude(segments, words)

    # Step 6: Claude analysis
    try:
        raw_response, cache_stats = analyze_with_claude(formatted, duration_sec)
        analysis = parse_and_validate_claude_response(raw_response, duration_sec)
        print(f"  Found: {len(analysis['informal_segments'])} informal segments, "
              f"{len(analysis['repeat_segments'])} repeats, "
              f"intro={'yes' if analysis['intro']['end'] > 0 else 'no'}")
    except Exception as exc:
        print(f"  [warn] Claude analysis failed: {exc}")
        print("  Falling back to silence-only edit...")
        analysis = {
            "informal_segments": [],
            "repeat_segments": [],
            "intro": {"start": 0.0, "end": 0.0, "confidence": 0.0},
        }
        cache_stats = {}

    # Step 7: Build cut list
    silence_cuts = [{"start": s, "end": e} for s, e in all_silence_ivs]
    all_cuts = build_cuts(all_silence_ivs, analysis)
    print(f"  Total cuts: {len(all_cuts)}")

    # Step 8: Compute main segments
    main_segments = compute_main_segments(all_cuts, duration_sec, analysis["intro"])
    print(f"  Main segments after cuts: {len(main_segments)}")

    # Step 9: Write output
    output = {
        "source": str(Path(source).resolve()),
        "duration_sec": round(duration_sec, 3),
        "teaser_clips": [],  # populated externally from transcript analysis
        "intro": analysis["intro"],
        "cuts": all_cuts,
        "main_segments": main_segments,
        "_debug": {
            "silence_gaps_raw": len(raw_silences),
            "word_gaps": len(word_gaps),
            "informal_segments": analysis["informal_segments"],
            "repeat_segments": analysis["repeat_segments"],
            "cache_stats": cache_stats,
        },
    }

    Path(args.output).write_text(json.dumps(output, indent=2))
    print(f"\n✓ Written to {args.output}")
    print(f"  Intro: {output['intro']['start']:.1f}s – {output['intro']['end']:.1f}s")
    print(f"  Cuts: {len(output['cuts'])}")
    print(f"  Main segments: {len(output['main_segments'])}")
    edit_dur = sum(s["end"] - s["start"] for s in main_segments)
    print(f"  Estimated edit: {edit_dur/60:.1f} min (down from {duration_sec/60:.1f} min)")


if __name__ == "__main__":
    main()
