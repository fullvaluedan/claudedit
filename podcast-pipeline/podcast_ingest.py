#!/usr/bin/env python3.11
"""
podcast_ingest.py — Multi-cam podcast ingest and classification.

Scans a directory of podcast files, auto-classifies them
(reference/mixed, host cam, guest cam, b-roll), and computes
sync offsets between sources.

Usage:
    python3.11 podcast_ingest.py /path/to/episode/ \
        [--output /tmp/ingest.json] \
        [--host-offset 0.0] \
        [--guest-offset 0.0]
"""

import argparse
import json
import math
import os
import subprocess
import sys
import tempfile
from pathlib import Path

# ---------------------------------------------------------------------------
# Filename hint sets for host / guest assignment
# ---------------------------------------------------------------------------
HOST_HINTS = {
    "host", "h1", "cam1", "cam_1", "camera1", "camera_1", "speaker1", "anchor"
}
GUEST_HINTS = {
    "guest", "g1", "cam2", "cam_2", "camera2", "camera_2", "speaker2", "interviewee"
}

# ---------------------------------------------------------------------------
# Supported video / audio extensions
# ---------------------------------------------------------------------------
MEDIA_EXTENSIONS = {
    ".mp4", ".mov", ".mxf", ".mkv", ".avi", ".m4v",
    ".mp3", ".wav", ".aac", ".m4a", ".flac",
}


# ---------------------------------------------------------------------------
# ffprobe helpers
# ---------------------------------------------------------------------------

def get_file_info(path: str) -> dict:
    """Return dict with duration_sec, width, height, audio_channels."""
    cmd = [
        "ffprobe", "-v", "quiet",
        "-print_format", "json",
        "-show_streams",
        "-show_format",
        str(path),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        data = json.loads(result.stdout)
    except Exception as exc:
        print(f"  [warn] ffprobe failed on {path}: {exc}")
        return {"duration_sec": 0.0, "width": 0, "height": 0, "audio_channels": 0}

    duration_sec = float(data.get("format", {}).get("duration", 0))
    width = height = 0
    audio_channels = 0

    for stream in data.get("streams", []):
        codec_type = stream.get("codec_type", "")
        if codec_type == "video" and width == 0:
            width = stream.get("width", 0)
            height = stream.get("height", 0)
        elif codec_type == "audio" and audio_channels == 0:
            audio_channels = stream.get("channels", 0)

    return {
        "duration_sec": duration_sec,
        "width": width,
        "height": height,
        "audio_channels": audio_channels,
    }


# ---------------------------------------------------------------------------
# Speech density
# ---------------------------------------------------------------------------

def compute_speech_density(path: str, duration: float, n_samples: int = 3) -> float:
    """
    Estimate fraction of time that contains speech by sampling n evenly-spaced
    60-second windows and running ffmpeg silencedetect on each.

    Returns float 0.0–1.0 (higher = more speech).
    """
    if duration <= 0:
        return 0.0

    window_sec = 60.0
    total_speech = 0.0
    total_sampled = 0.0

    # Spread sample start points evenly across 10%–90% of file
    for i in range(n_samples):
        frac = 0.10 + (0.80 / max(n_samples - 1, 1)) * i
        start_sec = frac * duration
        # Don't overshoot
        actual_window = min(window_sec, duration - start_sec)
        if actual_window <= 0:
            continue

        cmd = [
            "ffmpeg", "-v", "error",
            "-ss", str(start_sec),
            "-t", str(actual_window),
            "-i", str(path),
            "-af", "silencedetect=noise=-30dB:duration=0.3",
            "-f", "null", "-",
        ]
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=60
            )
            output = result.stderr
        except Exception as exc:
            print(f"  [warn] silencedetect failed on {path} at {start_sec:.1f}s: {exc}")
            total_sampled += actual_window
            continue

        # Parse silence_start / silence_end pairs
        silence_total = 0.0
        last_start = None
        for line in output.splitlines():
            if "silence_start" in line:
                try:
                    last_start = float(line.split("silence_start:")[1].strip().split()[0])
                except (IndexError, ValueError):
                    pass
            elif "silence_end" in line:
                try:
                    parts = line.split("silence_end:")[1].strip().split()
                    end = float(parts[0])
                    # Clamp to window
                    seg_start = max(last_start or 0.0, 0.0)
                    seg_end = min(end, actual_window)
                    if seg_end > seg_start:
                        silence_total += seg_end - seg_start
                    last_start = None
                except (IndexError, ValueError):
                    pass

        speech_in_window = max(actual_window - silence_total, 0.0)
        total_speech += speech_in_window
        total_sampled += actual_window

    if total_sampled <= 0:
        return 0.0

    return total_speech / total_sampled


# ---------------------------------------------------------------------------
# Sync via cross-correlation
# ---------------------------------------------------------------------------

def _extract_mono_pcm(path: str, start_sec: float, duration_sec: float,
                      sample_rate: int = 4000) -> "list[float] | None":
    """
    Extract a mono PCM segment from path using ffmpeg, return as list of floats.
    Returns None on failure.
    """
    cmd = [
        "ffmpeg", "-v", "error",
        "-ss", str(start_sec),
        "-t", str(duration_sec),
        "-i", str(path),
        "-ac", "1",
        "-ar", str(sample_rate),
        "-f", "f32le",
        "pipe:1",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, timeout=60)
        raw = result.stdout
        import struct
        n = len(raw) // 4
        samples = list(struct.unpack(f"<{n}f", raw[:n * 4]))
        return samples
    except Exception as exc:
        print(f"  [warn] PCM extraction failed on {path}: {exc}")
        return None


def find_sync_offset(reference_path: str, target_path: str,
                     ref_duration: float) -> tuple[float, float]:
    """
    Compute sync offset between reference and target using audio cross-correlation.

    Returns (offset_sec, confidence).
    offset_sec > 0  → target starts that many seconds later than reference
    offset_sec < 0  → target starts that many seconds earlier than reference

    Falls back to (0.0, 0.0) if numpy is unavailable or extraction fails.
    """
    try:
        import numpy as np
    except ImportError:
        print("  [warn] numpy not available — sync offset defaulting to 0.0")
        return 0.0, 0.0

    SAMPLE_RATE = 4000
    WINDOW_SEC = 30.0
    start_sec = ref_duration * 0.10

    print(f"  Extracting {WINDOW_SEC:.0f}s PCM from reference at {start_sec:.1f}s …")
    ref_samples = _extract_mono_pcm(reference_path, start_sec, WINDOW_SEC, SAMPLE_RATE)
    print(f"  Extracting {WINDOW_SEC:.0f}s PCM from target at {start_sec:.1f}s …")
    tgt_samples = _extract_mono_pcm(target_path, start_sec, WINDOW_SEC, SAMPLE_RATE)

    if ref_samples is None or tgt_samples is None:
        return 0.0, 0.0

    ref_arr = np.array(ref_samples, dtype=np.float32)
    tgt_arr = np.array(tgt_samples, dtype=np.float32)

    # Normalise
    for arr in (ref_arr, tgt_arr):
        rms = np.sqrt(np.mean(arr ** 2))
        if rms > 1e-9:
            arr /= rms

    # Full cross-correlation
    corr = np.correlate(ref_arr, tgt_arr, mode="full")
    lags = np.arange(-(len(tgt_arr) - 1), len(ref_arr))

    peak_idx = int(np.argmax(np.abs(corr)))
    peak_val = float(np.abs(corr[peak_idx]))
    mean_val = float(np.mean(np.abs(corr)))

    confidence = peak_val / mean_val if mean_val > 1e-9 else 0.0
    lag_samples = int(lags[peak_idx])
    offset_sec = lag_samples / SAMPLE_RATE

    return offset_sec, confidence


# ---------------------------------------------------------------------------
# Directory classification
# ---------------------------------------------------------------------------

def _name_hint_role(path: str) -> str | None:
    """Return 'host', 'guest', or None based on filename hints."""
    stem = Path(path).stem.lower()
    # Tokenise on underscores, hyphens, spaces, digits
    import re
    tokens = set(re.split(r"[\s\-_]+", stem))
    if tokens & HOST_HINTS:
        return "host"
    if tokens & GUEST_HINTS:
        return "guest"
    return None


def classify_directory(directory: str,
                       host_offset: float | None = None,
                       guest_offset: float | None = None) -> dict:
    """
    Scan directory, classify files, compute sync offsets.
    Returns ingest manifest dict.
    """
    directory = str(Path(directory).resolve())
    print(f"\nScanning: {directory}")

    # Collect media files
    media_files = []
    for entry in sorted(Path(directory).iterdir()):
        if entry.is_file() and entry.suffix.lower() in MEDIA_EXTENSIONS:
            media_files.append(str(entry))

    if not media_files:
        print("[error] No media files found.")
        sys.exit(1)

    print(f"Found {len(media_files)} media file(s):")

    # Gather metadata
    file_infos = {}
    for f in media_files:
        info = get_file_info(f)
        file_infos[f] = info
        print(f"  {Path(f).name}  {info['duration_sec']:.1f}s  "
              f"{info['width']}x{info['height']}  ch={info['audio_channels']}")

    durations = [info["duration_sec"] for info in file_infos.values()]
    max_dur = max(durations) if durations else 0.0

    # Long files = within ±10% of max duration
    threshold = max_dur * 0.90
    long_files = [f for f, info in file_infos.items()
                  if info["duration_sec"] >= threshold]
    broll_files = [f for f in media_files if f not in long_files]

    print(f"\nLong files (≥{threshold:.0f}s): {len(long_files)}")
    print(f"B-roll files: {len(broll_files)}")

    # Compute speech density for long files
    print("\nComputing speech densities …")
    densities: dict[str, float] = {}
    for f in long_files:
        dur = file_infos[f]["duration_sec"]
        density = compute_speech_density(f, dur)
        densities[f] = density
        print(f"  {Path(f).name}: {density:.3f}")

    # Highest speech density = reference (mixed / both speakers)
    if not long_files:
        print("[error] No long files found — cannot determine reference.")
        sys.exit(1)

    reference = max(long_files, key=lambda f: densities.get(f, 0.0))
    solo_cams = [f for f in long_files if f != reference]

    print(f"\nReference (mixed):  {Path(reference).name}")

    # Assign host / guest to solo cams
    host_cam: str | None = None
    guest_cam: str | None = None
    unassigned: list[str] = []

    for f in solo_cams:
        role = _name_hint_role(f)
        if role == "host" and host_cam is None:
            host_cam = f
        elif role == "guest" and guest_cam is None:
            guest_cam = f
        else:
            unassigned.append(f)

    # Fill unassigned slots in order
    for f in unassigned:
        if host_cam is None:
            host_cam = f
        elif guest_cam is None:
            guest_cam = f
        else:
            # More than 2 solo cams — treat extras as b-roll
            broll_files.append(f)

    print(f"Host cam:           {Path(host_cam).name if host_cam else 'none'}")
    print(f"Guest cam:          {Path(guest_cam).name if guest_cam else 'none'}")
    if broll_files:
        print(f"B-roll:             {[Path(f).name for f in broll_files]}")

    ref_duration = file_infos[reference]["duration_sec"]

    # Compute sync offsets
    sync = {"host_cam_offset_sec": 0.0, "guest_cam_offset_sec": 0.0}

    CONFIDENCE_THRESHOLD = 2.0

    if host_cam:
        if host_offset is not None:
            print(f"\nUsing manual host offset: {host_offset:.3f}s")
            sync["host_cam_offset_sec"] = host_offset
        else:
            print(f"\nComputing host cam sync offset …")
            offset, conf = find_sync_offset(reference, host_cam, ref_duration)
            print(f"  Host cam offset: {offset:.3f}s  confidence ratio: {conf:.2f}")
            if conf < CONFIDENCE_THRESHOLD:
                print(f"  [warn] Low sync confidence ({conf:.2f} < {CONFIDENCE_THRESHOLD}). "
                      "Consider using --host-offset to set manually.")
            sync["host_cam_offset_sec"] = offset

    if guest_cam:
        if guest_offset is not None:
            print(f"\nUsing manual guest offset: {guest_offset:.3f}s")
            sync["guest_cam_offset_sec"] = guest_offset
        else:
            print(f"\nComputing guest cam sync offset …")
            offset, conf = find_sync_offset(reference, guest_cam, ref_duration)
            print(f"  Guest cam offset: {offset:.3f}s  confidence ratio: {conf:.2f}")
            if conf < CONFIDENCE_THRESHOLD:
                print(f"  [warn] Low sync confidence ({conf:.2f} < {CONFIDENCE_THRESHOLD}). "
                      "Consider using --guest-offset to set manually.")
            sync["guest_cam_offset_sec"] = offset

    manifest = {
        "reference": reference,
        "host_cam": host_cam,
        "guest_cam": guest_cam,
        "broll": broll_files,
        "sync": sync,
        "reference_duration_sec": ref_duration,
    }

    return manifest


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scan a podcast episode directory and produce an ingest manifest."
    )
    parser.add_argument("directory", help="Directory containing episode media files")
    parser.add_argument(
        "--output", default="/tmp/ingest.json",
        help="Path for output ingest.json (default: /tmp/ingest.json)",
    )
    parser.add_argument(
        "--host-offset", type=float, default=None,
        help="Override host cam sync offset in seconds (skips auto-detection)",
    )
    parser.add_argument(
        "--guest-offset", type=float, default=None,
        help="Override guest cam sync offset in seconds (skips auto-detection)",
    )
    args = parser.parse_args()

    if not Path(args.directory).is_dir():
        print(f"[error] Not a directory: {args.directory}")
        sys.exit(1)

    manifest = classify_directory(
        args.directory,
        host_offset=args.host_offset,
        guest_offset=args.guest_offset,
    )

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as fh:
        json.dump(manifest, fh, indent=2)

    print(f"\n{'='*60}")
    print(f"Ingest manifest written to: {output_path}")
    print(f"  Reference:      {Path(manifest['reference']).name}")
    print(f"  Host cam:       {Path(manifest['host_cam']).name if manifest['host_cam'] else 'none'}")
    print(f"  Guest cam:      {Path(manifest['guest_cam']).name if manifest['guest_cam'] else 'none'}")
    print(f"  B-roll files:   {len(manifest['broll'])}")
    print(f"  Host offset:    {manifest['sync']['host_cam_offset_sec']:.3f}s")
    print(f"  Guest offset:   {manifest['sync']['guest_cam_offset_sec']:.3f}s")
    print(f"  Duration:       {manifest['reference_duration_sec']:.1f}s "
          f"({manifest['reference_duration_sec']/60:.1f} min)")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
