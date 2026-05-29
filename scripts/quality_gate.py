#!/usr/bin/env python3
"""quality_gate.py — The proof-of-done checker.

The problem this solves: for 5 days, work was reported "done" without being
verified. Stubs reported as renders. Demo content reported as purged when it
wasn't. "PASSED" on frames nobody looked at.

This script is the gate. It runs every check that matters and outputs a single
PASS or FAIL with the actual evidence. The agent must run this and show you the
output before claiming anything is done. It cannot fake a PASS — every check
produces a real artifact (an extracted frame, a grep result, a duration number).

Usage:
  python3 quality_gate.py /path/to/swissgrid-institutions

Exit code 0 = PASS (safe to proceed), 1 = FAIL (do not proceed).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

# Demo strings that must NOT remain in a finished composition
DEMO_STRINGS = [
    "survey findings", "the opportunity", "need motion graphics",
    "percent of you said", "design simplified", "lack editing skills",
    "forty-seven", "losing attention", "3 of 4", "47%", "62%",
]


def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                       shell=isinstance(cmd, str))
    return r.returncode, r.stdout, r.stderr


class Gate:
    def __init__(self, project_dir):
        self.proj = Path(project_dir)
        self.checks = []   # (name, passed, evidence)

    def record(self, name, passed, evidence):
        self.checks.append((name, passed, evidence))

    # ── CHECK 1: project exists and has expected structure ──────────────────
    def check_structure(self):
        if not self.proj.exists():
            return self.record("structure", False, f"project dir not found: {self.proj}")
        idx = self.proj / "index.html"
        comps = self.proj / "compositions"
        ok = idx.exists() and comps.exists()
        ev = f"index.html={'✓' if idx.exists() else '✗'} compositions/={'✓' if comps.exists() else '✗'}"
        self.record("structure", ok, ev)

    # ── CHECK 2: no demo content remains ────────────────────────────────────
    def check_demo_content(self):
        # Search files directly in Python — more reliable than shell grep
        # with complex patterns piped through subprocess.
        files = list(self.proj.rglob("*.html"))
        files = [f for f in files if "node_modules" not in str(f)
                 and "_verify" not in str(f)]
        real_hits = []
        for f in files:
            try:
                lines = f.read_text(errors="ignore").splitlines()
            except Exception:
                continue
            for i, line in enumerate(lines, 1):
                low = line.lower()
                matched = [s for s in DEMO_STRINGS if s in low]
                if not matched:
                    continue
                # Skip if the only match is a GSAP width animation value
                is_gsap_width = bool(re.search(r'width\s*[:=]\s*["\']?\d+%', low))
                has_text_demo = any(s in low for s in
                                    ["losing attention", "motion graphics",
                                     "survey findings", "lack editing",
                                     "the opportunity", "design simplified",
                                     "forty-seven", "3 of 4", "percent of you"])
                if is_gsap_width and not has_text_demo:
                    continue
                real_hits.append(f"{f.name}:{i}: {line.strip()[:60]}")
        ok = len(real_hits) == 0
        if ok:
            ev = "no demo strings in visible content"
        else:
            ev = f"{len(real_hits)} demo strings remain: " + \
                 " || ".join(real_hits[:5])
        self.record("demo_content_purged", ok, ev)

    # ── CHECK 3: lint passes ────────────────────────────────────────────────
    def check_lint(self):
        rc, out, err = run("npx hyperframes lint", cwd=str(self.proj))
        combined = (out + err).lower()
        # count actual errors (warnings are ok)
        error_match = re.search(r"(\d+)\s+error", combined)
        n_errors = int(error_match.group(1)) if error_match else (0 if "0 error" in combined or rc == 0 else -1)
        ok = n_errors == 0
        last_line = (out.strip().splitlines() or ["(no output)"])[-1]
        self.record("lint", ok, f"{n_errors} errors — {last_line[:80]}")

    # ── CHECK 4: composition duration is sane ───────────────────────────────
    def check_duration(self):
        rc, out, err = run("npx hyperframes compositions", cwd=str(self.proj))
        # look for a duration in seconds
        dur_match = re.search(r"(\d+(?:\.\d+)?)\s*s", out)
        dur = float(dur_match.group(1)) if dur_match else 0
        ok = dur >= 3  # anything under 3s is almost certainly a stub/broken
        self.record("duration", ok, f"master composition = {dur}s" +
                    ("" if ok else " — TOO SHORT, likely a stub"))

    # ── CHECK 5: extract proof frames from any rendered MOV ─────────────────
    def check_render_frames(self):
        renders = list(self.proj.glob("**/*.mov")) + list(self.proj.glob("**/out/*.mov"))
        renders = [r for r in renders if "node_modules" not in str(r)]
        if not renders:
            self.record("render_frames", None,
                        "no .mov rendered yet — run render then re-check (not a failure)")
            return
        verify_dir = self.proj / "_verify"
        verify_dir.mkdir(exist_ok=True)
        evidence = []
        all_ok = True
        for mov in renders:
            # get duration
            rc, out, err = run([
                "ffprobe", "-v", "error", "-show_entries", "format=duration",
                "-of", "csv=p=0", str(mov)])
            try:
                d = float(out.strip())
            except ValueError:
                d = 0
            if d <= 0:
                evidence.append(f"{mov.name}: BROKEN (0 duration)")
                all_ok = False
                continue
            # extract 3 frames: start, mid, end
            for label, t in [("start", 0.5), ("mid", d * 0.5), ("end", max(0, d - 0.5))]:
                png = verify_dir / f"{mov.stem}_{label}.png"
                run(["ffmpeg", "-y", "-ss", str(round(t, 2)), "-i", str(mov),
                     "-frames:v", "1", "-q:v", "2", str(png)])
            # check alpha for transparent overlays
            rc, pix, err = run([
                "ffprobe", "-v", "error", "-select_streams", "v:0",
                "-show_entries", "stream=pix_fmt", "-of", "csv=p=0", str(mov)])
            has_alpha = "a" in pix.strip().lower()
            evidence.append(f"{mov.name}: {d:.1f}s, frames→_verify/, "
                            f"alpha={'yes' if has_alpha else 'no'}")
        self.record("render_frames", all_ok, " | ".join(evidence))

    # ── RUN ALL ─────────────────────────────────────────────────────────────
    def run_all(self):
        self.check_structure()
        self.check_demo_content()
        self.check_lint()
        self.check_duration()
        self.check_render_frames()
        return self.report()

    def report(self):
        print("\n" + "═" * 60)
        print(f"QUALITY GATE — {self.proj.name}")
        print("═" * 60)
        hard_fail = False
        for name, passed, evidence in self.checks:
            if passed is True:
                mark = "✓ PASS"
            elif passed is False:
                mark = "✗ FAIL"
                hard_fail = True
            else:
                mark = "– SKIP"
            print(f"  {mark}  {name}")
            print(f"          {evidence}")
        print("═" * 60)

        if hard_fail:
            print("RESULT: ✗ FAILED — DO NOT proceed. Fix the ✗ items above.")
            print("This clip is NOT done. Do not report it as complete.")
            print("═" * 60 + "\n")
            return False
        else:
            print("RESULT: ✓ PASSED — checks clear.")
            print("REQUIRED: a human must still LOOK at the frames in _verify/")
            print("before final approval. Passing structural checks does not")
            print("mean the content is correct — only that it's not broken.")
            print("═" * 60 + "\n")
            return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 quality_gate.py /path/to/project")
        sys.exit(2)
    gate = Gate(sys.argv[1])
    passed = gate.run_all()
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
