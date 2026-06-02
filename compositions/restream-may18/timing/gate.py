#!/usr/bin/env python3
"""
gate.py — ONE command to run the whole clip gate. This is the repeatable entry point.

  python3 timing/gate.py <clip-dir>            # all STATIC gates (instant, no render) — run before rendering
  python3 timing/gate.py <clip-dir> --render   # also run the post-render pixel gate (after an HQ render)

Static gates (cheapest-catch-first; fix everything here before spending a render):
  lint            npx hyperframes lint            0 errors
  check-edl       blank-left (predict + exit)     no predicted blank-left, no late Mode-A beat
  check-content   empty/hollow box                no container-before-content, no sparse hold
  check-views     view discipline R1              no <6s jitter hold, no A-B-A
  check-selectors GSAP target resolution          every #id/.class animation target exists
  check-text      jargon / index / blur           no garbled term, no 0N index, no blur/grain over video

Render gate (authoritative pixels, after one HQ render):
  check-render    blank-left coverage + lint + z-index + index + jargon on the actual MP4

Exit 0 only if every gate passes. Gates are necessary, NOT sufficient — after green, a human still
eyeballs every Mode-A beat-START + every previously-flagged window (LESSONS: gates can't see wrong/
dark/semantically-off content). See ../LESSONS.md "THE CLIP WORKFLOW".
"""
import sys, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
STATIC = ['check-edl', 'check-content', 'check-views', 'check-selectors', 'check-text']

def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return r.returncode, (r.stdout or '') + (r.stderr or '')

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    do_render = '--render' in sys.argv
    if not args:
        print("usage: python3 timing/gate.py <clip-dir> [--render]"); return 2
    clip = args[0].rstrip('/')
    name = os.path.basename(clip)
    results = []   # (gate, ok, summary_line)

    # lint
    rc, out = run(['npx', 'hyperframes', 'lint'], cwd=clip)
    import re
    m = re.search(r'(\d+)\s+error', out)
    nerr = int(m.group(1)) if m else (0 if rc == 0 else -1)
    results.append(('lint', nerr == 0, f"{nerr} error(s)" if nerr >= 0 else "lint failed to run"))

    # static python gates
    for g in STATIC:
        rc, out = run([sys.executable, os.path.join(HERE, g + '.py'), clip])
        line = next((l for l in out.splitlines() if '>>>' in l), out.strip().splitlines()[-1:] or [''])
        line = line if isinstance(line, str) else (line[0] if line else '')
        results.append((g, rc == 0, line.replace('>>>', '').strip()))

    # render gate (optional)
    if do_render:
        rc, out = run([sys.executable, os.path.join(HERE, 'check-render.py'), clip])
        line = next((l for l in out.splitlines() if '>>>' in l), '')
        results.append(('check-render', rc == 0, line.replace('>>>', '').strip()))

    print(f"\n=== GATE: {name} {'(static + render)' if do_render else '(static only — run with --render after HQ)'} ===")
    allok = True
    for g, ok, summary in results:
        allok = allok and ok
        print(f"  [{'PASS' if ok else 'FAIL'}] {g:14} {summary}")
    print(f"  >>> {name}: {'ALL GREEN ✓ — now human-eyeball beat-starts + flagged windows' if allok else 'FAIL — fix before '+('shipping' if do_render else 'rendering')}")
    return 0 if allok else 1

if __name__ == '__main__':
    sys.exit(main())
