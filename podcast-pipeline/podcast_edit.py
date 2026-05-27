#!/usr/bin/env python3.11
"""
podcast_edit.py — Generate Premiere-ready edit decisions from an ingest manifest.

Reads ingest.json produced by podcast_ingest.py, detects speech windows for
each solo cam, applies editorial rules, and outputs edit_spec.json.

Usage:
    python3.11 podcast_edit.py \
        --ingest /tmp/ingest.json \
        --sequence-name "ep1-edit" \
        [--output /tmp/edit_spec.json] \
        [--transcript /tmp/transcript.json] \
        [--silence-threshold 0.5] \
        [--min-cut 2.0] \
        [--max-run 90.0]
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Silence / speech detection
# ---------------------------------------------------------------------------

def detect_silences(
    audio_path: str,
    t_start: float,
    t_end: float,
    min_silence: float,
    threshold_db: float,
) -> list[tuple[float, float]]:
    """
    Run ffmpeg silencedetect on audio_path between t_start and t_end.
    Returns list of (silence_start, silence_end) in file-time seconds.
    """
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
        print(f"  [warn] silencedetect failed on {audio_path} [{t_start:.1f}–{t_end:.1f}]: {exc}")
        return []

    silences: list[tuple[float, float]] = []
    last_start: float | None = None

    for line in output.splitlines():
        if "silence_start" in line:
            try:
                raw = float(line.split("silence_start:")[1].strip().split()[0])
                # Offset back into file-absolute time
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

    # If ffmpeg ended in the middle of a silence window, close it
    if last_start is not None:
        silences.append((last_start, t_end))

    return silences


def detect_speech_windows(
    file_path: str,
    total_duration: float,
    offset_sec: float,
    silence_threshold: float,
    chunk_size: float = 600.0,
) -> list[tuple[float, float]]:
    """
    Return list of (start, end) speech windows in REFERENCE timeline seconds,
    accounting for offset_sec.

    Processes file in chunk_size-second chunks to avoid memory issues.
    """
    print(f"  Detecting speech in {Path(file_path).name} "
          f"({total_duration/60:.1f} min, offset={offset_sec:+.3f}s) …")

    # Collect all silences across chunks
    all_silences: list[tuple[float, float]] = []
    pos = 0.0
    chunk_num = 0
    total_chunks = math.ceil(total_duration / chunk_size)

    while pos < total_duration:
        end = min(pos + chunk_size, total_duration)
        chunk_num += 1
        print(f"    chunk {chunk_num}/{total_chunks}  [{pos/60:.1f}–{end/60:.1f} min] …",
              end="\r", flush=True)
        chunk_silences = detect_silences(
            file_path, pos, end,
            min_silence=silence_threshold,
            threshold_db=-30,
        )
        all_silences.extend(chunk_silences)
        pos = end

    print()  # newline after \r progress

    # Merge adjacent silence segments (within 0.1s)
    merged_silences: list[tuple[float, float]] = []
    for seg in sorted(all_silences):
        if merged_silences and seg[0] <= merged_silences[-1][1] + 0.1:
            merged_silences[-1] = (merged_silences[-1][0], max(merged_silences[-1][1], seg[1]))
        else:
            merged_silences.append(list(seg))  # type: ignore[arg-type]

    # Invert silences to get speech windows (in file time)
    speech_file: list[tuple[float, float]] = []
    prev_end = 0.0
    for s_start, s_end in merged_silences:
        if s_start > prev_end + 0.01:
            speech_file.append((prev_end, s_start))
        prev_end = s_end
    if prev_end < total_duration - 0.01:
        speech_file.append((prev_end, total_duration))

    # Convert to reference timeline using offset
    # offset_sec = solo_cam_time - reference_time
    # → reference_time = solo_cam_time - offset_sec
    speech_ref = [
        (max(0.0, s - offset_sec), max(0.0, e - offset_sec))
        for s, e in speech_file
    ]
    speech_ref = [(s, e) for s, e in speech_ref if e > s]

    print(f"    Found {len(speech_ref)} speech window(s)")
    return speech_ref


# ---------------------------------------------------------------------------
# Edit decision generation
# ---------------------------------------------------------------------------

def generate_video_cuts(
    host_windows: list[tuple[float, float]],
    guest_windows: list[tuple[float, float]],
    total_dur: float,
    min_cut: float = 2.0,
    max_run: float = 90.0,
    hold: float = 0.5,
) -> list[dict]:
    """
    Generate raw video cut list from speech windows.

    Rules:
    - source "host_cam" when only host is speaking
    - source "guest_cam" when only guest is speaking
    - source "reference" (split-screen) when both or neither speaking
    - Transition hold: don't cut until speaker active for `hold` seconds
    - Min cut: merge cuts shorter than `min_cut` with neighbor
    - Max run: insert 2s split-screen air shot when single angle exceeds `max_run`

    Returns list of dicts: {source, start, end}
    """
    RESOLUTION = 0.05  # seconds per tick

    def is_active(windows: list[tuple[float, float]], t: float) -> bool:
        for s, e in windows:
            if s <= t < e:
                return True
        return False

    print("  Building frame-by-frame source map …")
    cuts: list[dict] = []
    current_source: str | None = None
    current_start = 0.0
    run_start = 0.0  # start of current single-angle run

    t = 0.0
    while t < total_dur:
        host_on = is_active(host_windows, t)
        guest_on = is_active(guest_windows, t)

        if host_on and not guest_on:
            desired = "host_cam"
        elif guest_on and not host_on:
            desired = "guest_cam"
        else:
            desired = "reference"  # both, neither → split-screen

        # Apply transition hold: wait for speaker to be continuously active
        if desired != current_source and desired in ("host_cam", "guest_cam"):
            # Check if desired speaker has been active for `hold` seconds
            hold_start = t
            hold_ok = True
            check = t
            while check < t + hold:
                if not is_active(
                    host_windows if desired == "host_cam" else guest_windows, check
                ):
                    hold_ok = False
                    break
                check += RESOLUTION
            if not hold_ok:
                desired = current_source if current_source else "reference"

        if desired != current_source:
            if current_source is not None:
                seg_dur = t - current_start
                if seg_dur > 0:
                    cuts.append({
                        "source": current_source,
                        "start": current_start,
                        "end": t,
                    })
            current_source = desired
            current_start = t
            run_start = t

        # Max-run check
        if current_source in ("host_cam", "guest_cam"):
            run_dur = t - run_start
            if run_dur >= max_run:
                # Flush current segment, insert 2s split-screen air shot
                cuts.append({
                    "source": current_source,
                    "start": current_start,
                    "end": t,
                })
                air_end = min(t + 2.0, total_dur)
                cuts.append({
                    "source": "reference",
                    "start": t,
                    "end": air_end,
                })
                current_source = current_source  # resume same angle
                current_start = air_end
                run_start = air_end
                t = air_end
                continue

        t += RESOLUTION

    # Flush final segment
    if current_source is not None and current_start < total_dur:
        cuts.append({
            "source": current_source,
            "start": current_start,
            "end": total_dur,
        })

    # Merge cuts shorter than min_cut into their neighbor
    print(f"  Raw cuts before merge: {len(cuts)}")
    merged: list[dict] = []
    for cut in cuts:
        dur = cut["end"] - cut["start"]
        if merged and dur < min_cut:
            # Extend previous cut to absorb this one
            merged[-1]["end"] = cut["end"]
        else:
            merged.append(dict(cut))

    # Fix any gaps / overlaps from the merge pass
    for i in range(1, len(merged)):
        merged[i]["start"] = merged[i - 1]["end"]

    print(f"  Cuts after min-cut merge: {len(merged)}")
    return merged


# ---------------------------------------------------------------------------
# Convert raw cuts to Premiere-ready spec
# ---------------------------------------------------------------------------

def build_cuts_for_premiere(cuts: list[dict], ingest: dict) -> tuple[list[dict], float]:
    """
    Convert raw cut list (timeline start/end) to Premiere-ready cut dicts with:
    - file path
    - media_in / media_out (accounting for sync offset)
    - timeline_pos / duration

    Returns (video_cuts, actual_duration).
    """
    host_offset = ingest["sync"]["host_cam_offset_sec"]
    guest_offset = ingest["sync"]["guest_cam_offset_sec"]
    ref_dur = ingest["reference_duration_sec"]

    source_files = {
        "reference": ingest["reference"],
        "host_cam": ingest.get("host_cam"),
        "guest_cam": ingest.get("guest_cam"),
    }

    video_cuts = []
    timeline_pos = 0.0

    for cut in cuts:
        source = cut["source"]
        tl_start = cut["start"]
        tl_end = cut["end"]
        duration = tl_end - tl_start

        if duration <= 0:
            continue

        file_path = source_files.get(source)
        if not file_path:
            # Fall back to reference if cam not present
            source = "reference"
            file_path = ingest["reference"]

        # Convert timeline position to media position
        if source == "host_cam":
            offset = host_offset
        elif source == "guest_cam":
            offset = guest_offset
        else:
            offset = 0.0

        media_in = tl_start + offset
        media_out = tl_end + offset

        # Clamp to file bounds (rough guard)
        media_in = max(0.0, media_in)
        media_out = max(media_in + duration, media_out)

        video_cuts.append({
            "source": source,
            "file": file_path,
            "media_in": round(media_in, 4),
            "media_out": round(media_out, 4),
            "timeline_pos": round(timeline_pos, 4),
            "duration": round(duration, 4),
        })
        timeline_pos += duration

    return video_cuts, timeline_pos


# ---------------------------------------------------------------------------
# B-roll placement
# ---------------------------------------------------------------------------

def _keywords_from_filename(path: str) -> list[str]:
    """Extract lowercase tokens from a filename as keyword candidates."""
    import re
    stem = Path(path).stem.lower()
    tokens = re.split(r"[\s\-_]+", stem)
    # Remove common filler tokens
    stopwords = {"broll", "broll", "b", "roll", "clip", "footage", "shot",
                 "01", "02", "03", "04", "05"}
    return [t for t in tokens if t and t not in stopwords and not t.isdigit()]


def plan_broll(
    broll_files: list[str],
    transcript_words: list[dict],
    total_dur: float,
) -> list[dict]:
    """
    Plan b-roll placements.

    For each b-roll file:
    1. Extract keyword hints from filename.
    2. Search transcript_words for first mention of any keyword.
       transcript_words is a list of {word, start, end} dicts.
    3. Fallback: evenly-spaced insertion every ~120s.

    Returns list of {file, timeline_pos, duration_sec}.
    """
    if not broll_files:
        return []

    placements = []
    keyword_hits: dict[str, float] = {}  # file → timeline_pos

    # Build keyword → earliest timestamp map from transcript
    if transcript_words:
        word_map: dict[str, float] = {}
        for entry in transcript_words:
            w = entry.get("word", "").lower().strip(".,!?\"'")
            if w and w not in word_map:
                word_map[w] = float(entry.get("start", 0.0))
    else:
        word_map = {}

    for f in broll_files:
        keywords = _keywords_from_filename(f)
        best_time: float | None = None
        for kw in keywords:
            if kw in word_map:
                t = word_map[kw]
                if best_time is None or t < best_time:
                    best_time = t
        if best_time is not None:
            keyword_hits[f] = best_time

    # Determine duration for each b-roll file (prefer short clips, cap at 30s)
    def _broll_duration(f: str) -> float:
        cmd = [
            "ffprobe", "-v", "quiet",
            "-print_format", "json",
            "-show_format", str(f),
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            data = json.loads(result.stdout)
            d = float(data.get("format", {}).get("duration", 10.0))
            return min(d, 30.0)
        except Exception:
            return 10.0

    # Assign placements
    placed_times: list[float] = []
    for f in broll_files:
        if f in keyword_hits:
            pos = keyword_hits[f]
        else:
            # Evenly spaced fallback among files without keyword hits
            idx = broll_files.index(f)
            spacing = total_dur / (len(broll_files) + 1)
            pos = spacing * (idx + 1)

        # Avoid collisions (nudge if within 5s of already-placed)
        pos = _avoid_collision(pos, placed_times, gap=5.0, total_dur=total_dur)
        placed_times.append(pos)

        dur = _broll_duration(f)
        placements.append({
            "file": f,
            "timeline_pos": round(pos, 4),
            "duration_sec": round(dur, 4),
        })

    placements.sort(key=lambda x: x["timeline_pos"])
    return placements


def _avoid_collision(pos: float, placed: list[float], gap: float, total_dur: float) -> float:
    """Nudge pos forward until it is `gap` seconds away from all placed times."""
    MAX_ITER = 200
    for _ in range(MAX_ITER):
        collision = any(abs(pos - p) < gap for p in placed)
        if not collision:
            return min(pos, total_dur - gap)
        pos += gap
        if pos > total_dur:
            pos = max(0.0, total_dur - gap)
            break
    return pos


# ---------------------------------------------------------------------------
# Audio tracks
# ---------------------------------------------------------------------------

def build_audio_tracks(ingest: dict) -> list[dict]:
    """
    Build full-duration isolated audio tracks for Premiere.
    A1 = host_cam, A2 = guest_cam.
    """
    host_offset = ingest["sync"]["host_cam_offset_sec"]
    guest_offset = ingest["sync"]["guest_cam_offset_sec"]
    ref_dur = ingest["reference_duration_sec"]

    tracks = []

    if ingest.get("host_cam"):
        tracks.append({
            "source": "host_cam",
            "file": ingest["host_cam"],
            "premiere_track": 0,
            "media_in": round(host_offset, 4),
            "media_out": round(host_offset + ref_dur, 4),
            "timeline_pos": 0.0,
        })

    if ingest.get("guest_cam"):
        tracks.append({
            "source": "guest_cam",
            "file": ingest["guest_cam"],
            "premiere_track": 1,
            "media_in": round(guest_offset, 4),
            "media_out": round(guest_offset + ref_dur, 4),
            "timeline_pos": 0.0,
        })

    return tracks


# ---------------------------------------------------------------------------
# Summary stats
# ---------------------------------------------------------------------------

def print_summary(video_cuts: list[dict], broll: list[dict], total_dur: float) -> None:
    source_time: dict[str, float] = {}
    source_count: dict[str, int] = {}
    max_single_run: dict[str, float] = {}
    current_run: dict[str, float] = {}
    run_source: str | None = None

    for cut in video_cuts:
        src = cut["source"]
        dur = cut["duration"]
        source_time[src] = source_time.get(src, 0.0) + dur
        source_count[src] = source_count.get(src, 0) + 1

        if src != run_source:
            run_source = src
            current_run[src] = dur
        else:
            current_run[src] = current_run.get(src, 0.0) + dur

        if current_run.get(src, 0.0) > max_single_run.get(src, 0.0):
            max_single_run[src] = current_run[src]

    print(f"\n{'='*60}")
    print(f"EDIT SUMMARY")
    print(f"{'='*60}")
    print(f"Total duration:   {total_dur:.1f}s ({total_dur/60:.1f} min)")
    print(f"Total cuts:       {len(video_cuts)}")
    print()
    print(f"{'Source':<15} {'Cuts':>6} {'Duration':>10} {'% of show':>10} {'Max run':>10}")
    print(f"{'-'*55}")
    for src in sorted(source_count.keys()):
        pct = 100.0 * source_time.get(src, 0.0) / total_dur if total_dur > 0 else 0.0
        print(f"{src:<15} {source_count[src]:>6} "
              f"{source_time.get(src,0.0):>9.1f}s "
              f"{pct:>9.1f}% "
              f"{max_single_run.get(src,0.0):>9.1f}s")
    print()
    print(f"B-roll placements: {len(broll)}")
    for b in broll:
        print(f"  @{b['timeline_pos']/60:.2f}min  {Path(b['file']).name}  ({b['duration_sec']:.1f}s)")
    print(f"{'='*60}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

# Need math for ceiling in detect_speech_windows
import math


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Premiere-ready edit decisions from an ingest manifest."
    )
    parser.add_argument(
        "--ingest", required=True,
        help="Path to ingest.json from podcast_ingest.py",
    )
    parser.add_argument(
        "--sequence-name", required=True, dest="sequence_name",
        help="Name for the Premiere sequence",
    )
    parser.add_argument(
        "--output", default="/tmp/edit_spec.json",
        help="Path for output edit_spec.json (default: /tmp/edit_spec.json)",
    )
    parser.add_argument(
        "--transcript", default=None,
        help="Path to transcript.json with word-level timestamps [{word, start, end}, …]",
    )
    parser.add_argument(
        "--silence-threshold", type=float, default=0.5, dest="silence_threshold",
        help="Min silence duration in seconds (default: 0.5)",
    )
    parser.add_argument(
        "--min-cut", type=float, default=2.0, dest="min_cut",
        help="Minimum cut duration in seconds (default: 2.0)",
    )
    parser.add_argument(
        "--max-run", type=float, default=90.0, dest="max_run",
        help="Maximum single-angle run in seconds before inserting air shot (default: 90.0)",
    )
    args = parser.parse_args()

    # Load ingest manifest
    with open(args.ingest) as fh:
        ingest: dict = json.load(fh)

    print(f"Loaded ingest manifest: {args.ingest}")
    print(f"  Reference:  {Path(ingest['reference']).name}")
    print(f"  Host cam:   {Path(ingest['host_cam']).name if ingest.get('host_cam') else 'none'}")
    print(f"  Guest cam:  {Path(ingest['guest_cam']).name if ingest.get('guest_cam') else 'none'}")
    print(f"  B-roll:     {len(ingest.get('broll', []))} file(s)")
    print(f"  Duration:   {ingest['reference_duration_sec']:.1f}s")

    ref_dur = ingest["reference_duration_sec"]
    host_offset = ingest["sync"]["host_cam_offset_sec"]
    guest_offset = ingest["sync"]["guest_cam_offset_sec"]

    # Load transcript if provided
    transcript_words: list[dict] = []
    if args.transcript:
        try:
            with open(args.transcript) as fh:
                transcript_words = json.load(fh)
            print(f"Loaded transcript: {len(transcript_words)} word(s)")
        except Exception as exc:
            print(f"  [warn] Could not load transcript: {exc}")

    # Detect speech windows for each solo cam
    print("\nDetecting speech windows …")
    host_windows: list[tuple[float, float]] = []
    guest_windows: list[tuple[float, float]] = []

    if ingest.get("host_cam"):
        host_windows = detect_speech_windows(
            ingest["host_cam"],
            total_duration=ref_dur + abs(host_offset),  # file duration approx
            offset_sec=host_offset,
            silence_threshold=args.silence_threshold,
            chunk_size=600.0,
        )

    if ingest.get("guest_cam"):
        guest_windows = detect_speech_windows(
            ingest["guest_cam"],
            total_duration=ref_dur + abs(guest_offset),
            offset_sec=guest_offset,
            silence_threshold=args.silence_threshold,
            chunk_size=600.0,
        )

    # Generate raw cuts
    print("\nGenerating video cut list …")
    raw_cuts = generate_video_cuts(
        host_windows=host_windows,
        guest_windows=guest_windows,
        total_dur=ref_dur,
        min_cut=args.min_cut,
        max_run=args.max_run,
        hold=0.5,
    )

    # Build Premiere-ready cut list
    video_cuts, actual_dur = build_cuts_for_premiere(raw_cuts, ingest)

    # Audio tracks
    audio_tracks = build_audio_tracks(ingest)

    # B-roll planning
    print("\nPlanning b-roll placements …")
    broll_placements = plan_broll(
        broll_files=ingest.get("broll", []),
        transcript_words=transcript_words,
        total_dur=actual_dur,
    )

    # Assemble edit spec
    edit_spec = {
        "sequence_name": args.sequence_name,
        "total_duration_sec": round(actual_dur, 4),
        "sources": {
            "reference": ingest["reference"],
            "host_cam": ingest.get("host_cam"),
            "guest_cam": ingest.get("guest_cam"),
            "broll": ingest.get("broll", []),
        },
        "sync": ingest["sync"],
        "video_cuts": video_cuts,
        "audio_tracks": audio_tracks,
        "broll": broll_placements,
        "cut_count": len(video_cuts),
    }

    # Write output
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as fh:
        json.dump(edit_spec, fh, indent=2)

    print(f"\nEdit spec written to: {output_path}")

    # Print summary
    print_summary(video_cuts, broll_placements, actual_dur)


if __name__ == "__main__":
    main()
