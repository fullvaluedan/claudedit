#!/usr/bin/env python3
"""
check-edl.py — PRE-RENDER static coverage check. Predicts blank-left WITHOUT rendering,
by reading the source: the master view-timeline (when Mode-A is active) vs when each
beat's first visible element actually fires. Catches "graphic fires late -> blank left"
at the EDL/build stage. Fast (no render). Pair with check-render.py (the authoritative
post-render backstop).

Usage: python3 check-edl.py <clip-dir>

Logic: for every MODE_A interval, the left zone is filled only when some mounted beat's
first CONTENT element has fired. A beat is "mounted" data-start..data-start+dur; its first
content time = data-start + (min entrance-tween offset on a non-backdrop element). Any
MODE_A sub-interval with no covering beat = predicted BLANK-LEFT.
"""
import sys, os, re, glob

GAP_FAIL = 1.5          # predicted blank-left longer than this = FAIL
START_TOL = 0.6         # a beat must show content within this of its data-start (R7 frame-at-beat-start)
BACKDROP = re.compile(r'backdrop|glow|grad|-bg\b|bg-|zone|rule|reg', re.I)

def parse_views(html):
    """Return list of (start, end, 'FULL'|'MODE_A') from the master timeline."""
    m = re.search(r'<script>(?!.*cdn).*?window\.__timelines\["master"\]', html, re.S)
    script = html  # search whole file; switches are unique enough
    switches = []
    for mm in re.finditer(r'\btoFull\s*\(\s*([0-9.]+)', script): switches.append((float(mm.group(1)), 'FULL'))
    for mm in re.finditer(r'\btoModeA\s*\(\s*([0-9.]+)', script): switches.append((float(mm.group(1)), 'MODE_A'))
    # raw .to(v,{...},T) form
    for mm in re.finditer(r'\.to\(\s*\w+\s*,\s*\{([^}]*)\}\s*,\s*([0-9.]+)', script):
        obj, t = mm.group(1), float(mm.group(2))
        if 'left:' in obj or 'width:' in obj:
            # const-ref form (left: MODE_A.left / FULL.left) — detect by keyword first
            if re.search(r'\bMODE_A\b', obj): switches.append((t, 'MODE_A')); continue
            if re.search(r'\bFULL\b', obj): switches.append((t, 'FULL')); continue
            w = re.search(r'width:\s*([0-9]+)', obj); l = re.search(r'left:\s*([0-9]+)', obj)
            if (w and w.group(1) in ('1920',)) or (l and l.group(1) == '0'): switches.append((t, 'FULL'))
            elif (w and w.group(1) in ('614','768')) or (l and l.group(1) and int(l.group(1))>1000): switches.append((t, 'MODE_A'))
    switches.sort()
    dur = float(re.search(r'data-duration="([0-9.]+)"', html).group(1))
    segs = []; cur = 'FULL'; start = 0.0
    for t, v in switches:
        if v != cur: segs.append((start, t, cur)); cur = v; start = t
    segs.append((start, dur, cur))
    return segs

def first_content_offset(subpath):
    """Min entrance-tween offset on a non-backdrop element (when the first graphic shows)."""
    if not os.path.exists(subpath): return None
    s = open(subpath, errors='ignore').read()
    best = None
    for mm in re.finditer(r'\.(fromTo|from)\(\s*([^,]+),[^;]*?,\s*([0-9.]+)\s*\)', s):
        sel, off = mm.group(2), float(mm.group(3))
        if BACKDROP.search(sel): continue
        if best is None or off < best: best = off
    # also tl.set(sel,{opacity:1},T) used as a reveal
    for mm in re.finditer(r'\.set\(\s*([^,]+),\s*\{[^}]*opacity:\s*1[^}]*\}\s*,\s*([0-9.]+)\)', s):
        sel, off = mm.group(1), float(mm.group(2))
        if BACKDROP.search(sel): continue
        if best is None or off < best: best = off
    return best

# whole-beat exit: a wrapper/multi-element opacity:0 .to(). Single decorative fades (.reg, one line)
# do NOT count, so this never falsely shrinks a beat's covered span. Models blank-left cause #3
# (content fades before the Mode-A window ends — clip-4). check-render remains the pixel authority.
WRAP_EXIT = re.compile(r'inner|zone|words|stack|backdrop|scover|content|wrap', re.I)
def content_exit_offset(subpath):
    if not os.path.exists(subpath): return None
    s = open(subpath, errors='ignore').read()
    best = None
    for mm in re.finditer(r'\.to\(\s*([^,]+?(?:,\s*[^,{]+)*?)\s*,\s*\{([^}]*opacity:\s*0(?!\.)[^}]*)\}\s*,\s*([0-9.]+)\)', s):
        sel, off = mm.group(1), float(mm.group(3))
        if (',' in sel) or WRAP_EXIT.search(sel):     # whole-beat fade only
            if best is None or off < best: best = off
    return best

def main():
    d = sys.argv[1].rstrip('/'); html = open(os.path.join(d,'index.html')).read()
    segs = parse_views(html)
    beats = []  # (start, end, content_time, id, off, exit_t)
    def mk(bid, src, ds, dd):
        off = first_content_offset(os.path.join(d,'compositions',src))
        ct = ds + (off if off is not None else 0)
        ex = content_exit_offset(os.path.join(d,'compositions',src))
        exit_t = ds + ex if (ex is not None and ds + ex > ct) else ds + dd   # only if after content
        beats.append((ds, ds+dd, ct, bid, off, exit_t))
    for mm in re.finditer(r'<div\b[^>]*\bid="(beat-[a-z0-9-]+)"[^>]*data-composition-src="compositions/([^"]+)"[^>]*data-start="([0-9.]+)"[^>]*data-duration="([0-9.]+)"', html, re.S):
        mk(mm.group(1), mm.group(2), float(mm.group(3)), float(mm.group(4)))
    # also handle id-after-src ordering
    for mm in re.finditer(r'<div\b[^>]*data-composition-src="compositions/([^"]+)"[^>]*\bid="(beat-[a-z0-9-]+)"[^>]*data-start="([0-9.]+)"[^>]*data-duration="([0-9.]+)"', html, re.S):
        if any(b[3]==mm.group(2) for b in beats): continue
        mk(mm.group(2), mm.group(1), float(mm.group(3)), float(mm.group(4)))
    # walk every MODE_A segment in 0.25s steps; flag uncovered stretches
    gaps = []; late = []
    t_steps = []
    for (s,e,v) in segs:
        if v != 'MODE_A': continue
        # which beats start inside this seg and fire late?
        for (bs,be,ct,bid,off,xt) in beats:
            if s-0.5 <= bs <= e and off is not None and off > START_TOL:
                late.append((bid, bs, off))
        t = s
        run = None
        while t < e:
            # covered only while content is present: after it fires (ct) and before it exits (xt)
            covered = any(bs <= t <= be and ct <= t <= xt for (bs,be,ct,bid,off,xt) in beats)
            if not covered:
                if run is None: run = t
            else:
                if run is not None and (t-run) >= GAP_FAIL: gaps.append((run, t))
                run = None
            t += 0.25
        if run is not None and (e-run) >= GAP_FAIL: gaps.append((run, e))
    name = os.path.basename(d)
    print(f"=== check-edl (pre-render): {name} ===")
    for (s,e,v) in segs: print(f"   {v:7} {s:6.1f}-{e:6.1f}")
    if late:
        print("  LATE-FIRING beats in Mode-A (frame not at beat-start, R7):")
        for bid,bs,off in late: print(f"      {bid}: first content +{off:.1f}s after start {bs:.1f}")
    if gaps:
        print(f"  PREDICTED BLANK-LEFT (>{GAP_FAIL}s):")
        for s,e in gaps: print(f"      {s:.1f}-{e:.1f}s ({e-s:.1f}s)")
        print(f"  >>> {name}: FAIL (pre-render)")
        return 1
    print(f"  >>> {name}: PASS (pre-render — no predicted blank-left)")
    return 0

if __name__=='__main__': sys.exit(main())
