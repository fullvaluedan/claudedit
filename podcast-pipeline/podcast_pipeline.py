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

    # ── 1. Silence cuts (word gaps >= silence_s) ─────────────────────────────
    silence_cuts = []
    for i in range(1, len(words)):
        gap_s = words[i - 1]["end"]
        gap_e = words[i]["start"]
        if gap_e - gap_s >= silence_s:
            silence_cuts.append({"start": gap_s, "end": gap_e, "type": "silence", "reason": ""})
    print(f"  Silence gaps >= {silence_s}s: {len(silence_cuts)}")

    # ── 2. Claude content detection (lag / retake / pre+post-show / intro / teasers) ──
    intro = {"start": 0.0, "end": 0.0, "confidence": 0.0}
    teasers: list[dict] = []
    content_cuts: list[dict] = []
    sys.path.insert(0, str(Path(__file__).parent))
    try:
        import podcast_content_edit as pce
        formatted = pce.format_transcript_for_claude(segs, words)
        raw, _usage = pce.detect_edits_with_claude(formatted)
        det = pce.validate_detection(raw, duration, min_confidence=0.5)
        content_cuts = det["cuts"]
        intro = det["intro"]
        teasers = det["teaser_clips"]
        from collections import Counter
        type_counts = dict(Counter(c["type"] for c in content_cuts))
        print(f"  Claude: {len(content_cuts)} content cuts {type_counts}, "
              f"{len(teasers)} teasers, intro={'yes' if intro['end'] > 0 else 'no'}")
    except Exception as e:
        print(f"  [warn] Claude detection failed ({e}); using silence-only cuts.")

    # ── 3. Snap every cut to word edges (start→word end, end→word start) ──────
    def snap_cut(c: dict) -> dict:
        return {**c,
                "start": snap_to_word_end(c["start"]),
                "end":   snap_to_word_start(c["end"])}

    snapped = [snap_cut(c) for c in (silence_cuts + content_cuts)]
    snapped = [c for c in snapped if c["end"] - c["start"] >= 0.2]

    # ── 4. Snap intro + teasers ──────────────────────────────────────────────
    if intro["end"] > intro["start"]:
        intro = {**intro,
                 "start": snap_to_word_start(intro["start"]),
                 "end":   snap_to_word_end(intro["end"])}
    teasers = [{**t,
                "start": snap_to_word_start(t["start"]),
                "end":   snap_to_word_end(t["end"])}
               for t in teasers]

    # ── 5. Main segments = complement of (cuts ∪ intro) over [0, duration] ────
    # Intro is excluded from the body because it's repositioned to the front.
    cut_ivs = sorted([(c["start"], c["end"]) for c in snapped]
                     + ([(intro["start"], intro["end"])] if intro["end"] > intro["start"] else []))
    merged_ivs: list[list[float]] = []
    for s, e in cut_ivs:
        if merged_ivs and s <= merged_ivs[-1][1] + 0.05:
            merged_ivs[-1][1] = max(merged_ivs[-1][1], e)
        else:
            merged_ivs.append([s, e])

    main_segments = []
    cursor = 0.0
    for s, e in merged_ivs:
        if s > cursor + 0.5:
            main_segments.append({"start": round(cursor, 3), "end": round(s, 3)})
        cursor = e
    if duration - cursor > 0.5:
        main_segments.append({"start": round(cursor, 3), "end": round(duration, 3)})

    # ── 6. Output cut list (deletions only; intro is NOT a deletion) ──────────
    out_cuts = sorted(
        [{"start": c["start"], "end": c["end"],
          "reason": (f"{c.get('type', 'cut')}: {c.get('reason', '')}".rstrip(": ").strip())}
         for c in snapped],
        key=lambda x: x["start"])
    merged_cuts: list[dict] = []
    for c in out_cuts:
        if merged_cuts and c["start"] <= merged_cuts[-1]["end"] + 0.05:
            merged_cuts[-1]["end"] = max(merged_cuts[-1]["end"], c["end"])
        else:
            merged_cuts.append(dict(c))

    edit_dur = sum(s["end"] - s["start"] for s in main_segments)
    print(f"  Main segments: {len(main_segments)}, ~{edit_dur/60:.1f} min of content")

    output = {
        "source": str(source.resolve()),
        "duration_sec": round(duration, 3),
        "teaser_clips": teasers,
        "intro": intro,
        "cuts": merged_cuts,
        "main_segments": main_segments,
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

    # Stage 3: Build + Premiere QA
    stage(3, TOTAL, f"Building Premiere sequence '{name}' + QA")
    print(f"\n  ⚠ Premiere must be open with {source.name} imported into the project bin.")
    success = stage_build_and_qa(content_edit, name, pipeline_dir)
    if not success:
        fail("Build or QA failed — see errors above.")

    # Stage 4: Content QA
    stage(4, TOTAL, "Content QA — verifying edit decisions")
    sys.path.insert(0, str(pipeline_dir))
    from content_qa import run_content_qa
    qa_passed = run_content_qa(transcript, content_edit)
    if not qa_passed:
        fail("Content QA failed — review flagged cuts above before publishing.")

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
