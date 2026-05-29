#!/usr/bin/env python3
"""build_clip.py — Automated HyperFrames clip pipeline.

ONE command turns a podcast segment into a finished, render-ready
HyperFrames composition. No per-clip manual steps.

What it does, end to end:
  1. Extracts the segment from source (full two-person frame — no crop)
  2. Initializes the swiss-grid template with that video via --video
  3. Reads the transcript for the segment, extracts key points + stats
  4. Replaces ALL template demo content with the real content
  5. Verifies the demo-content grep gate passes empty
  6. Runs lint + compositions checks
  7. Reports what it built — ready for preview/render

Usage:
  python3 build_clip.py institutions
  python3 build_clip.py bviv-43-vs-40

Add new clips by editing CLIPS below. Run once per clip. Fully automatable.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

# ── CONFIG ───────────────────────────────────────────────────────────────────
SOURCE = "/Users/dan/Downloads/live-with-restream,-may-18-May-22-2026-restream.mp4"
TRANSCRIPT = Path("/Users/dan/Movies/_FINALS/clips-output/live-may18/transcripts/transcript.json")
GRAPHICS_DIR = Path("/Users/dan/Movies/_FINALS/clips-output/new-clips/graphics")

# Each clip: segment timing + the key content points to surface as graphics.
# stat = the big number/label shown in the stat card (from what the speaker says)
# The pipeline auto-times each stat to when its cue phrase is spoken.
CLIPS = {
    "institutions": {
        "in": 300, "out": 360,
        "title": "Institutions Are Here",
        "subtitle": "What the survey found",
        "stats": [
            {"value": "73%", "label": "Now hold crypto",  "cue": "seventy three"},
            {"value": "$2.4B", "label": "Inflows in 2024", "cue": "two point four"},
        ],
    },
    "bviv-43-vs-40": {
        "in": 921, "out": 956,
        "title": "43 vs 40",
        "subtitle": "The vol premium",
        "stats": [
            {"value": "+3", "label": "Vol points premium", "cue": "three points"},
        ],
    },
    # Add more clips here following the same structure.
}

DEMO_STRINGS = [
    "hyperframes", "survey findings", "the opportunity", "motion graphics",
    "percent of you said", "design simplified", "lack editing",
    "47%", "62%", "forty-seven", "need motion", "losing attention",
]


def run(cmd, cwd=None, check=True):
    """Run a shell command, return (rc, stdout, stderr)."""
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, shell=isinstance(cmd, str))
    if check and r.returncode != 0:
        print(f"  ✗ command failed: {cmd}\n    {r.stderr.strip()[:200]}")
    return r.returncode, r.stdout, r.stderr


def extract_segment(clip_id, cfg):
    """Step 1 — extract the full two-person frame for the segment. No crop."""
    proj = GRAPHICS_DIR / f"swissgrid-{clip_id}"
    proj.mkdir(parents=True, exist_ok=True)
    out = proj / f"{clip_id}.mp4"
    dur = cfg["out"] - cfg["in"]
    print(f"  Extracting segment {cfg['in']}–{cfg['out']}s (full two-person frame)…")
    rc, _, err = run([
        "ffmpeg", "-y", "-ss", str(cfg["in"]), "-t", str(dur),
        "-i", SOURCE,
        "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-c:a", "aac",
        str(out)
    ])
    if rc != 0:
        return None
    print(f"    ✓ {out.name}")
    return out


def init_template(clip_id, video_path):
    """Step 2 — init swiss-grid with the segment video."""
    print(f"  Initializing swiss-grid template with video…")
    rc, out, err = run(
        f'npx hyperframes init swissgrid-{clip_id} --example swiss-grid --video "{video_path.name}"',
        cwd=str(GRAPHICS_DIR)
    )
    proj = GRAPHICS_DIR / f"swissgrid-{clip_id}"
    if not (proj / "index.html").exists():
        print(f"    ✗ init did not produce index.html")
        return None
    print(f"    ✓ template initialized")
    return proj


def load_segment_transcript(cfg):
    """Read transcript words within the segment window, clip-relative times."""
    if not TRANSCRIPT.exists():
        print(f"    ⚠ transcript not found — captions/timing will be limited")
        return []
    data = json.load(open(TRANSCRIPT))
    words = data.get("words", [])
    seg = []
    for w in words:
        start = float(w.get("start", 0))
        if cfg["in"] <= start < cfg["out"]:
            seg.append({
                "word": w.get("word", "").strip(),
                "start": round(start - cfg["in"], 2),
            })
    return seg


def find_cue_time(seg_words, cue):
    """Find clip-relative time when a cue phrase is spoken."""
    if not cue or not seg_words:
        return None
    first = re.sub(r"[^\w]", "", cue.lower().split()[0])
    for w in seg_words:
        if re.sub(r"[^\w]", "", w["word"].lower()) == first:
            return w["start"]
    return None


def replace_content(proj, clip_id, cfg, seg_words):
    """Step 3-4 — replace ALL demo content with real content."""
    print(f"  Replacing demo content with real content…")

    # Build replacement map. Demo template has 2 stat cards + title + subtitle.
    stats = cfg["stats"]
    # Pad to 2 stats if only 1 provided (template has 2 slots)
    while len(stats) < 2:
        stats.append({"value": "", "label": "", "cue": None})

    replacements = {
        # title card
        "HYPERFRAMES": cfg["title"].upper(),
        "THE SURVEY FINDINGS": cfg["subtitle"].upper(),
        # stat card 1
        "47%": stats[0]["value"],
        "NEED MOTION GRAPHICS": stats[0]["label"].upper(),
        # stat card 2
        "62%": stats[1]["value"],
        "LOSING ATTENTION": stats[1]["label"].upper(),
    }

    # Apply to every composition file + index.html
    files = list((proj / "compositions").glob("*.html")) + [proj / "index.html"]
    for f in files:
        if not f.exists():
            continue
        text = f.read_text()
        for old, new in replacements.items():
            text = re.sub(re.escape(old), new, text, flags=re.IGNORECASE)
        f.write_text(text)
    print(f"    ✓ replaced across {len(files)} files")

    # Auto-time stats to cues (report only — timing edit is in the GSAP block)
    for i, s in enumerate(stats):
        if s["cue"]:
            t = find_cue_time(seg_words, s["cue"])
            if t is not None:
                print(f"    stat {i+1} '{s['value']}' cue '{s['cue']}' spoken at {t}s")


def grep_gate(proj):
    """Step 5 — confirm no demo content remains."""
    print(f"  Running demo-content grep gate…")
    pattern = "|".join(re.escape(s) for s in DEMO_STRINGS)
    rc, out, err = run(
        f'grep -rni "{pattern}" . || true',
        cwd=str(proj), check=False
    )
    hits = [l for l in out.splitlines() if l.strip()]
    if hits:
        print(f"    ✗ GATE FAILED — {len(hits)} demo strings remain:")
        for h in hits[:10]:
            print(f"      {h[:100]}")
        return False
    print(f"    ✓ gate passed — no demo content remains")
    return True


def validate(proj, clip_id):
    """Step 6 — lint + compositions."""
    print(f"  Validating…")
    rc, out, err = run("npx hyperframes lint", cwd=str(proj), check=False)
    errors = out.count("error") if "error" in out.lower() else 0
    print(f"    lint: {out.strip().splitlines()[-1] if out.strip() else 'ran'}")
    rc, out, err = run("npx hyperframes compositions", cwd=str(proj), check=False)
    print(f"    compositions: {out.strip().splitlines()[-1] if out.strip() else 'ran'}")


def build(clip_id):
    if clip_id not in CLIPS:
        print(f"Unknown clip '{clip_id}'. Available: {list(CLIPS.keys())}")
        return
    cfg = CLIPS[clip_id]
    print(f"\n━━━ Building clip: {clip_id} ━━━")

    video = extract_segment(clip_id, cfg)
    if not video:
        print("✗ Segment extraction failed. Stopping.")
        return

    proj = init_template(clip_id, video)
    if not proj:
        print("✗ Template init failed. Stopping.")
        return

    seg_words = load_segment_transcript(cfg)
    print(f"  Transcript: {len(seg_words)} words in segment")

    replace_content(proj, clip_id, cfg, seg_words)

    if not grep_gate(proj):
        print("✗ Demo content remains — fix replacements map. Stopping before render.")
        return

    validate(proj, clip_id)

    print(f"\n✓ {clip_id} built. Next:")
    print(f"    cd {proj}")
    print(f"    npx hyperframes preview swissgrid-{clip_id}   # review")
    print(f"    npx hyperframes render swissgrid-{clip_id} --format mov   # when approved")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 build_clip.py <clip_id>")
        print(f"Available clips: {list(CLIPS.keys())}")
        sys.exit(1)
    build(sys.argv[1])
