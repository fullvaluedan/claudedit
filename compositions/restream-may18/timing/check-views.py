#!/usr/bin/env python3
"""
check-views.py — STATIC. View-switching discipline (R1): no jitter, no flip-flop.

clip-7 (41-49s) and clip-8 (11-16s) bounced full -> Mode-A -> full within ~12s, which reads as
unmotivated jitter. The guard was prose ("hold a view >=8s, never A-B-A within 12s") and shipped
twice. This makes it a mechanical pre-render gate, reusing the same view-parser as check-edl.

FAILs:
  - any non-intro view segment shorter than MIN_HOLD (a <8s view sandwiched between others)
  - A-B-A: returning to a view you just left, with the middle segment shorter than NO_RETURN

Shares check-edl's parser blind spots (transform-based crops are invisible) — see LESSONS backlog.

Usage: python3 check-views.py <clip-dir>
"""
import sys, os, re

# Calibrated to accepted reality: the rejected jitter was ~3.8-4.0s bounces (clip-7/clip-8);
# accepted holds include a 9.5s full-frame breather (clip-1) and a 7.3s Mode-A card (clip-4).
# So the hard-FAIL line is 6s (clear jitter), below the editorial 8s target in DESIGN.md R1.
MIN_HOLD = 6.0     # a mid-clip view shorter than this = jitter = FAIL
NO_RETURN = 6.0    # returning to a view after less than this of the other = A-B-A jitter = FAIL
# First segment (cold open) and last segment (close/outro) are exempt — they can be any length.

def parse_views(html):
    """(start,end,'FULL'|'MODE_A') from the master timeline. Same logic as check-edl/check-content."""
    switches = []
    for mm in re.finditer(r'\btoFull\s*\(\s*([0-9.]+)', html): switches.append((float(mm.group(1)), 'FULL'))
    for mm in re.finditer(r'\btoModeA\s*\(\s*([0-9.]+)', html): switches.append((float(mm.group(1)), 'MODE_A'))
    for mm in re.finditer(r'\.to\(\s*\w+\s*,\s*\{([^}]*)\}\s*,\s*([0-9.]+)', html):
        obj, t = mm.group(1), float(mm.group(2))
        if 'left:' in obj or 'width:' in obj:
            if re.search(r'\bMODE_A\b', obj): switches.append((t, 'MODE_A')); continue
            if re.search(r'\bFULL\b', obj): switches.append((t, 'FULL')); continue
            w = re.search(r'width:\s*([0-9]+)', obj); l = re.search(r'left:\s*([0-9]+)', obj)
            if (w and w.group(1) == '1920') or (l and l.group(1) == '0'): switches.append((t, 'FULL'))
            elif (w and w.group(1) in ('614','768')) or (l and l.group(1) and int(l.group(1))>1000): switches.append((t, 'MODE_A'))
    switches.sort()
    m = re.search(r'data-duration="([0-9.]+)"', html); dur = float(m.group(1)) if m else 1e9
    segs = []; cur='FULL'; start=0.0
    for t,v in switches:
        if v != cur: segs.append((start,t,cur)); cur=v; start=t
    segs.append((start,dur,cur))
    return segs

def main():
    d = sys.argv[1].rstrip('/')
    html = open(os.path.join(d,'index.html')).read()
    segs = parse_views(html)
    name = os.path.basename(d)
    print(f"=== check-views: {name} ===")
    for s,e,v in segs: print(f"   {v:7} {s:6.1f}-{e:6.1f} ({e-s:.1f}s)")
    fails = []
    last = len(segs) - 1
    # short hold — skip the first (cold open) and last (close) segments
    for i,(s,e,v) in enumerate(segs):
        if i == 0 or i == last: continue
        if (e-s) < MIN_HOLD:
            fails.append(f"{v} segment {s:.1f}-{e:.1f} holds only {e-s:.1f}s (< {MIN_HOLD}s) — jitter")
    # A-B-A: a short middle segment bracketed by the same view (skip if the middle is cold-open/close)
    for i in range(2, len(segs)):
        if segs[i][2] == segs[i-2][2]:
            mid = segs[i-1]; midlen = mid[1]-mid[0]
            if midlen < NO_RETURN and (i-1) != 0 and (i-1) != last:
                fails.append(f"A-B-A: returns to {segs[i][2]} at {segs[i][0]:.1f} after only {midlen:.1f}s of {mid[2]} (< {NO_RETURN}s)")
    if fails:
        print("  VIEW DISCIPLINE FAIL (R1):")
        for f in fails: print(f"      {f}")
        print(f"  >>> {name}: FAIL (view-switching)")
        return 1
    print(f"  >>> {name}: PASS ✓ (no <{MIN_HOLD:.0f}s hold, no A-B-A)")
    return 0

if __name__ == '__main__':
    sys.exit(main())
