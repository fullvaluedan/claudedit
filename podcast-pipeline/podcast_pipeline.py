#!/usr/bin/env python3
"""
podcast_pipeline.py — End-to-end podcast editing pipeline runner.

Orchestrates all stages for a given podcast episode:
  1. transcribe   — mlx_whisper → transcript JSON
  2. analyze      — content analysis → content_edit.json
  3. build        — Premiere sequence via bridge
  4. qa           — verify sequence is correct
  5. report       — print final summary

Usage:
    python3 podcast_pipeline.py --source /path/to/podcast.mp4
    python3 podcast_pipeline.py --source /path/to/podcast.mp4 --name "Anndy Lian Web4 Ep1"
    python3 podcast_pipeline.py --source /path/to/podcast.mp4 --skip-transcribe --skip-analyze

Flags:
    --source            Path to source MP4/MOV file (required)
    --name              Episode/sequence name (default: filename without extension)
    --work-dir          Working directory for temp files (default: /tmp/podcast-edit)
    --skip-transcribe   Skip stage 1 if transcript already exists
    --skip-analyze      Skip stage 2 if content_edit.json already exists
    --silence-s         Min silence gap to cut (default: 2.0s)
    --snap-window-s     Word-boundary snap window (default: 0.6s)
"""

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Stage runner helpers
# ---------------------------------------------------------------------------

def stage(n: int, total: int, name: str):
    print(f"\n[{n}/{total}] {name}...")


def fail(msg: str):
    print(f"✗ FAILED: {msg}")
    sys.exit(1)


def ok(msg: str = ""):
    print(f"✓ {msg}" if msg else "✓")


def run(cmd: list[str], check=True, capture=False, timeout=600) -> subprocess.CompletedProcess:
    result = subprocess.run(
        cmd, capture_output=capture, text=True, timeout=timeout
    )
    if check and result.returncode != 0:
        err = result.stderr.strip() if capture else ""
        fail(f"Command failed: {' '.join(cmd[:3])}...\n{err}")
    return result


# ---------------------------------------------------------------------------
# Stage 1: Transcribe
# ---------------------------------------------------------------------------

def stage_transcribe(source: Path, work_dir: Path) -> Path:
    transcript = work_dir / f"{source.stem}.json"
    if transcript.exists():
        print(f"  Transcript already exists: {transcript}")
        return transcript

    print(f"  Running mlx_whisper (large-v3-turbo) on {source.name}...")
    try:
        import mlx_whisper
        result = mlx_whisper.transcribe(
            str(source),
            path_or_hf_repo="mlx-community/whisper-large-v3-turbo",
            word_timestamps=True,
        )
        transcript.write_text(json.dumps(result))
        segs = len(result.get("segments", []))
        words = sum(len(s.get("words", [])) for s in result.get("segments", []))
        dur = result["segments"][-1]["end"] if result.get("segments") else 0
        print(f"  Transcribed: {segs} segments, {words} words, {dur/60:.1f} min")
    except ImportError:
        fail("mlx_whisper not installed. Run: pip install mlx-whisper")

    return transcript


# ---------------------------------------------------------------------------
# Stage 2: Analyze — build content_edit.json
# ---------------------------------------------------------------------------

def stage_analyze(source: Path, transcript: Path, work_dir: Path,
                  silence_s: float, snap_window_s: float) -> Path:
    import bisect

    content_edit = work_dir / "content_edit.json"
    if content_edit.exists():
        print(f"  content_edit.json already exists.")
        return content_edit

    print(f"  Loading transcript and computing edit decisions...")

    d = json.loads(transcript.read_text())
    segs = d.get("segments", [])

    # Flatten words
    words = []
    for seg in segs:
        for w in seg.get("words", []):
            words.append({"start": float(w["start"]), "end": float(w["end"]), "word": w["word"].strip()})
    words.sort(key=lambda x: x["start"])

    if not words:
        fail("No word-level timestamps in transcript.")

    duration = words[-1]["end"]
    word_starts = [w["start"] for w in words]
    word_ends   = [w["end"]   for w in words]

    def snap_to_word_end(t):
        idx = bisect.bisect_right(word_ends, t + snap_window_s) - 1
        if idx >= 0 and word_ends[idx] >= t - snap_window_s:
            return round(word_ends[idx], 3)
        return round(t, 3)

    def snap_to_word_start(t):
        idx = bisect.bisect_left(word_starts, t - snap_window_s)
        if idx < len(word_starts) and word_starts[idx] <= t + snap_window_s:
            return round(word_starts[idx], 3)
        return round(t, 3)

    # Detect word gaps >= silence_s
    silence_cuts = []
    for i in range(1, len(words)):
        gap_s = words[i - 1]["end"]
        gap_e = words[i]["start"]
        if gap_e - gap_s >= silence_s:
            silence_cuts.append({"start": gap_s, "end": gap_e, "reason": "silence"})
    print(f"  Word gaps >= {silence_s}s: {len(silence_cuts)}")

    # Find intro (last 20% of file — search for self-intro patterns)
    last_20pct = duration * 0.80
    import re
    intro_re = re.compile(r"hi (guys|everyone|there)|hello (guys|everyone)|i'?m\s+\w+\s+\w+|welcome to", re.I)
    intro_start = 0.0
    intro_end   = 0.0
    for seg in segs:
        if seg["start"] >= last_20pct and intro_re.search(seg.get("text", "")):
            # Found intro start — read forward up to 90s for CTA or "thank you"
            end_re = re.compile(r"thank you|bye|see you|take a look|subscribe|check it out", re.I)
            intro_start = seg["start"]
            for seg2 in segs:
                if seg2["start"] > intro_start and seg2["start"] <= intro_start + 90:
                    if end_re.search(seg2.get("text", "")):
                        intro_end = seg2["end"]
                        break
            if intro_end == 0.0:
                # No explicit end marker — take 60s window
                intro_end = min(intro_start + 60, duration)
            break

    if intro_start > 0:
        print(f"  Intro detected: {intro_start:.1f}s – {intro_end:.1f}s ({(intro_end-intro_start):.1f}s)")
    else:
        print(f"  No intro detected (search last 20% for 'hi guys', 'I'm [name]')")

    # Structural cuts: pre-show (first 88s heuristic) and post-recording
    # Identify where main content ends: find "catch you next time" or "bye" before intro
    outro_end = intro_start if intro_start > 0 else duration
    outro_re = re.compile(r"catch you|see you next|bye bro|bye everyone|goodbye", re.I)
    main_end = outro_end
    for seg in segs:
        if seg["start"] < outro_end - 60 and outro_re.search(seg.get("text", "")):
            main_end = seg["end"]  # keep searching for latest match before intro

    structural_cuts = [
        {"start": 0.0,      "end": min(90.0, words[0]["start"] + 0.1), "reason": "pre-show"},
        {"start": main_end, "end": duration, "reason": "post-recording"},
    ]
    print(f"  Main content: ~{structural_cuts[0]['end']:.0f}s – {main_end:.0f}s")

    # Snapped lag cuts (empty by default — user adds manually to content_edit.json)
    lag_cuts = []

    # Merge all cuts
    all_raw = [(c["start"], c["end"], c["reason"]) for c in silence_cuts + structural_cuts + lag_cuts]
    all_raw.sort(key=lambda x: x[0])
    merged_cuts = []
    for s, e, r in all_raw:
        if merged_cuts and s <= merged_cuts[-1]["end"] + 0.05:
            merged_cuts[-1]["end"] = max(merged_cuts[-1]["end"], e)
        else:
            merged_cuts.append({"start": s, "end": e, "reason": r})

    # Compute main segments
    main_lo = structural_cuts[0]["end"]
    main_hi = main_end
    main_segments = []
    cursor = 0.0
    for c in merged_cuts:
        if c["start"] > cursor + 0.5:
            main_segments.append({"start": cursor, "end": c["start"]})
        cursor = c["end"]
    if duration - cursor > 0.5:
        main_segments.append({"start": cursor, "end": duration})
    main_segments = [s for s in main_segments
                     if s["end"] - s["start"] >= 0.5
                     and s["end"] > main_lo
                     and s["start"] < main_hi]
    for s in main_segments:
        s["start"] = max(round(s["start"], 3), main_lo)
        s["end"]   = min(round(s["end"],   3), main_hi)
    main_segments = [s for s in main_segments if s["end"] - s["start"] >= 0.5]

    edit_dur = sum(s["end"] - s["start"] for s in main_segments)
    print(f"  Main segments: {len(main_segments)}, ~{edit_dur/60:.1f} min of content")

    output = {
        "source": str(source.resolve()),
        "duration_sec": round(duration, 3),
        "teaser_clips": [],   # populate manually or via LLM analysis
        "intro": {"start": round(intro_start, 3), "end": round(intro_end, 3), "confidence": 0.8 if intro_start > 0 else 0.0},
        "cuts": merged_cuts,
        "main_segments": main_segments,
        "_note": "Add teaser_clips manually, or run with ANTHROPIC_API_KEY to auto-detect.",
    }
    content_edit.write_text(json.dumps(output, indent=2))
    print(f"  Written: {content_edit}")
    return content_edit


# ---------------------------------------------------------------------------
# Stage 3+4: Build + QA (delegates to build_content_sequence.py)
# ---------------------------------------------------------------------------

def stage_build_and_qa(content_edit: Path, sequence_name: str, pipeline_dir: Path) -> bool:
    builder = pipeline_dir / "build_content_sequence.py"
    cmd = [
        sys.executable, str(builder),
        "--edit", str(content_edit),
        "--sequence-name", sequence_name,
    ]
    print(f"  Running build_content_sequence.py...")
    result = subprocess.run(cmd, text=True, timeout=600)
    return result.returncode == 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Podcast editing pipeline runner")
    parser.add_argument("--source",           required=True,  help="Source MP4/MOV file")
    parser.add_argument("--name",             default="",     help="Episode/sequence name")
    parser.add_argument("--work-dir",         default="/tmp/podcast-edit", help="Working directory")
    parser.add_argument("--skip-transcribe",  action="store_true")
    parser.add_argument("--skip-analyze",     action="store_true")
    parser.add_argument("--silence-s",        type=float, default=2.0)
    parser.add_argument("--snap-window-s",    type=float, default=0.6)
    args = parser.parse_args()

    source = Path(args.source).resolve()
    if not source.exists():
        fail(f"Source file not found: {source}")

    name = args.name or source.stem.replace("-", " ").replace("_", " ").title()
    work_dir = Path(args.work_dir)
    work_dir.mkdir(parents=True, exist_ok=True)

    pipeline_dir = Path(__file__).parent
    TOTAL = 4  # transcribe, analyze, build+qa, report

    # Save run config for reproducibility
    config = {
        "source": str(source),
        "name": name,
        "work_dir": str(work_dir),
        "silence_threshold_s": args.silence_s,
        "word_snap_window_s": args.snap_window_s,
        "skip_transcribe": args.skip_transcribe,
        "skip_analyze": args.skip_analyze,
    }
    (work_dir / "run_config.json").write_text(json.dumps(config, indent=2))

    print(f"\n{'='*60}")
    print(f"  Podcast Pipeline: {name}")
    print(f"  Source: {source.name}")
    print(f"  Work dir: {work_dir}")
    print(f"{'='*60}")

    # Stage 1: Transcribe
    if not args.skip_transcribe:
        stage(1, TOTAL, "Transcribing audio")
        transcript = stage_transcribe(source, work_dir)
    else:
        transcript = work_dir / f"{source.stem}.json"
        if not transcript.exists():
            fail(f"--skip-transcribe set but transcript not found: {transcript}")
        stage(1, TOTAL, "Transcribing audio")
        print(f"  Skipped — using existing: {transcript}")

    # Stage 2: Analyze
    if not args.skip_analyze:
        stage(2, TOTAL, "Analyzing transcript for edit decisions")
        content_edit = stage_analyze(source, transcript, work_dir, args.silence_s, args.snap_window_s)
    else:
        content_edit = work_dir / "content_edit.json"
        if not content_edit.exists():
            fail(f"--skip-analyze set but content_edit.json not found: {content_edit}")
        stage(2, TOTAL, "Analyzing transcript for edit decisions")
        print(f"  Skipped — using existing: {content_edit}")

    # Stage 3+4: Build + QA
    stage(3, TOTAL, f"Building Premiere sequence '{name}' + QA")
    print(f"\n  ⚠ Premiere must be open with {source.name} imported into the project bin.")
    success = stage_build_and_qa(content_edit, name, pipeline_dir)
    if not success:
        fail("Build or QA failed — see errors above.")

    # Stage 4: Report
    stage(4, TOTAL, "Pipeline complete")
    edit_data = json.loads(content_edit.read_text())
    clips_kept = len(edit_data.get("main_segments", []))
    cuts_made  = len(edit_data.get("cuts", []))
    orig_dur   = edit_data.get("duration_sec", 0)
    edit_dur   = sum(s["end"] - s["start"] for s in edit_data.get("main_segments", []))

    print(f"""
  Summary:
    Original:     {orig_dur/60:.1f} min
    Cuts made:    {cuts_made}
    Segments:     {clips_kept}
    Est. edit:    {edit_dur/60:.1f} min
    Run config:   {work_dir}/run_config.json
    Transcript:   {transcript}
    Edit spec:    {content_edit}

  To reproduce: python3 podcast_pipeline.py --source {source} --name "{name}" --skip-transcribe --skip-analyze
""")


if __name__ == "__main__":
    main()
