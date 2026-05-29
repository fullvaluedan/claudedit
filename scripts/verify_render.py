#!/usr/bin/env python3
"""verify_render.py — proof-of-correctness for HyperFrames renders.

The problem this solves:
  The agent kept reporting "PASSED" on renders it never actually looked at.
  An empty demo-content grep proves the demo text is GONE — it does NOT prove
  YOUR content rendered. "HYPERFRAMES" → "c vs 40" stub passes the grep but is
  still broken.

What this does:
  For each rendered MOV, extract a frame at the hold point (mid-composition)
  as a PNG. These PNGs are the proof. A human (or the agent via vision) looks
  at them BEFORE anything is placed in Premiere.

Usage:
  python3 verify_render.py
  → writes _verify/[name]_frame.png for every render
  → prints a checklist of what each frame must show

This does NOT auto-approve. It produces evidence for review.
"""
import subprocess
import sys
from pathlib import Path

RENDERS = Path("/Users/dan/Movies/_FINALS/clips-output/new-clips/renders")
VERIFY_DIR = RENDERS.parent / "_verify"

# What each graphic's frame MUST show. The reviewer checks the PNG against this.
EXPECTED = {
    "opener-b2-institutions":     'Title card: "iBit Options" + "Now Open to Institutions" — large text, NOT a stub',
    "opener-b2-bviv-vix":         'Title card: "BVIV" + "Bitcoin\'s Fear Index" — large text',
    "opener-b2-bviv-43-vs-40":    'Title card: "+3 Vol Pts" + "BVIV-US vs BVIV" — large text, NOT "c vs 40"',
    "opener-b2-perp-predmarket":  'Title card: "Convergence" + "Perps Meets Prediction Markets"',
    "opener-b2-bloomberg-bviv":   'Title card: "100K+" + "Bloomberg Terminal Users"',
    "stat-b2-institutions":       'Stat card with real number + label, structured layout',
    "stat-b2-bviv-vix":           'Stat card with real number + label',
    "stat-b2-bviv-43-40":         'Stat card showing the 43 vs 40 comparison',
    "stat-b2-perp-predmarket":    'Stat card with real data',
    "stat-b2-bloomberg-bviv":     'Stat card: 100K+ Bloomberg users',
}


def extract_frame(mov: Path, out_png: Path, at_seconds: float) -> dict:
    """Pull one frame at the given timestamp."""
    out_png.parent.mkdir(parents=True, exist_ok=True)
    try:
        r = subprocess.run(
            ["ffmpeg", "-y", "-ss", str(at_seconds), "-i", str(mov),
             "-frames:v", "1", "-q:v", "2", str(out_png)],
            capture_output=True, text=True, timeout=60
        )
        if r.returncode != 0 or not out_png.exists():
            return {"ok": False, "reason": r.stderr.strip()[:160]}
        return {"ok": True, "png": str(out_png)}
    except Exception as e:
        return {"ok": False, "reason": str(e)}


def get_duration(mov: Path) -> float:
    try:
        r = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(mov)],
            capture_output=True, text=True, timeout=30
        )
        return float(r.stdout.strip())
    except Exception:
        return 0.0


def main():
    if not RENDERS.exists():
        print(f"✗ Renders folder not found: {RENDERS}")
        sys.exit(1)

    movs = sorted(RENDERS.glob("*.mov"))
    if not movs:
        print(f"✗ No MOV files in {RENDERS}")
        sys.exit(1)

    print(f"Extracting verification frames from {len(movs)} renders\n")
    print(f"Frames will be written to: {VERIFY_DIR}\n")

    results = []
    for mov in movs:
        # match against EXPECTED keys (strip _vN and .mov)
        base = mov.stem
        import re
        base_clean = re.sub(r"_v\d+$", "", base)

        dur = get_duration(mov)
        # sample at 60% through — past entry animation, into the hold
        at = round(dur * 0.6, 2) if dur > 0 else 1.0

        out_png = VERIFY_DIR / f"{base}_frame.png"
        res = extract_frame(mov, out_png, at)

        expected = EXPECTED.get(base_clean, "(no expectation defined — review manually)")
        results.append((base, dur, at, res, expected))

    # Report
    print("─" * 70)
    for base, dur, at, res, expected in results:
        status = "✓" if res["ok"] else "✗"
        print(f"{status} {base}  (dur {dur:.1f}s, frame @ {at}s)")
        print(f"    MUST SHOW: {expected}")
        if res["ok"]:
            print(f"    frame: {res['png']}")
        else:
            print(f"    EXTRACT FAILED: {res['reason']}")
        print()

    print("─" * 70)
    print("NEXT STEP — REVIEW THE FRAMES:")
    print(f"  open {VERIFY_DIR}")
    print()
    print("For each frame, confirm it shows the 'MUST SHOW' content above.")
    print("If any frame is blank, shows a stub (e.g. 'c vs 40'), shows demo")
    print("content, or covers a speaker's face → that render is BROKEN.")
    print("Do NOT place broken renders. Re-render following HYPERFRAMES-EXECUTION.md.")


if __name__ == "__main__":
    main()
