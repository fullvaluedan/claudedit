#!/usr/bin/env python3
"""
check-content.py — STATIC "empty box" gate. The check the brightness gate could never be.

Prior gates measured whether the left zone is BRIGHT (check-render YMAX) or whether SOME
element fired (check-edl). Both treat a glowing-but-hollow container as "filled": a card
with a lit border + eyebrow pegs luminance, and the container's own entry counted as
"content." So clip-8 c8b13 — card visible at offset 0.70, first metric row at 16.44 —
sat as an EMPTY BOX for ~16s and passed every gate.

This gate reads the SOURCE and separates the SHELL (card / glass / panel / eyebrow / rule /
backdrop / track) from the SUBSTANTIVE CONTENT inside it (rows / bars / values / nodes /
lines / quote / stat / chips). It FAILS any beat where the shell is up but the content
lags by more than LAG_FAIL seconds — i.e. a container that appears emptier than it will be.

Deterministic, no render. Run before building/rendering. Validated: it must flag every
known empty/sparse beat (c8b13, c5b5, c8b7, c3b5, c5b4) and zero after they're fixed.

Usage: python3 check-content.py <clip-dir>
"""
import sys, os, re, glob

BOX_FAIL    = 2.5   # a CONTAINER (card/box) on screen with no content inside this long = empty box
SPARSE_FAIL = 5.0   # only a title/eyebrow (no container) and no content this long = sparse hold

# CONTAINER = a visible bordered/filled shell that looks broken when empty (the literal "box").
CONTAINER = re.compile(r'card|glass|panel|\bbox\b|frame', re.I)
# CHROME = labels / rules / decoration. Not a box, but not content either (an eyebrow alone is sparse).
CHROME = re.compile(r'backdrop|glow|grad|\bbg\b|bg-|-bg|zone|rule|reg\b|eye|title|label|'
                    r'header|hdr|idx|track|crosshalo|axis|grid', re.I)
# anything matching either is SHELL (not substantive content)
SHELL = re.compile(CONTAINER.pattern + '|' + CHROME.pattern, re.I)

def mmss(t):
    return f"{int(t)//60}:{int(t)%60:02d}"

def parse_views(html):
    """List of (start,end,'FULL'|'MODE_A') from the master timeline. Copied from check-edl.py
    so this gate is view-aware: a full-frame beat (both speakers) is NEVER an empty box, and a
    beat's empty window only counts if it overlaps a MODE_A segment."""
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
    m = re.search(r'data-duration="([0-9.]+)"', html)
    dur = float(m.group(1)) if m else 1e9
    segs = []; cur = 'FULL'; start = 0.0
    for t, v in switches:
        if v != cur: segs.append((start, t, cur)); cur = v; start = t
    segs.append((start, dur, cur))
    return segs

def overlaps_modea(segs, a, b):
    """True if [a,b] overlaps any MODE_A segment."""
    for (s, e, v) in segs:
        if v == 'MODE_A' and a < e and b > s:
            return True
    return False

def first_offsets(subpath):
    """Return (shell_in, content_in) — min entrance offset of any SHELL element and of any
    SUBSTANTIVE CONTENT element. None if absent."""
    if not os.path.exists(subpath):
        return None, None
    s = open(subpath, errors='ignore').read()
    box_in = chrome_in = content_in = None
    def note(sel, off):
        nonlocal box_in, chrome_in, content_in
        if CONTAINER.search(sel):
            if box_in is None or off < box_in: box_in = off
        elif CHROME.search(sel):
            if chrome_in is None or off < chrome_in: chrome_in = off
        else:
            if content_in is None or off < content_in: content_in = off
    # .fromTo / .from — always an entrance
    for mm in re.finditer(r'\.(?:fromTo|from)\(\s*([^,]+?),[^;]*?,\s*([0-9.]+)\s*\)', s):
        note(mm.group(1), float(mm.group(2)))
    # .set(sel,{...opacity:1...},T) — reveal
    for mm in re.finditer(r'\.set\(\s*([^,]+?),\s*\{[^}]*opacity:\s*1[^}]*\}\s*,\s*([0-9.]+)\)', s):
        note(mm.group(1), float(mm.group(2)))
    # .to(sel,{obj},T) — counts as an APPEARANCE (element on screen) UNLESS it's an exit
    # (target opacity:0 / clip-path re-hidden). Catches clip-wipe reveals like
    # tl.to("#l1 .clip",{clipPath:"inset(0 0% 0 0)"},0.58) that .fromTo-only parsing missed.
    for mm in re.finditer(r'\.to\(\s*([^,]+?),\s*\{([^}]*)\}\s*,\s*([0-9.]+)\)', s):
        sel, obj, off = mm.group(1), mm.group(2), float(mm.group(3))
        if re.search(r'opacity:\s*0(?!\.)', obj):        # exit fade — not an appearance
            continue
        if re.search(r'inset\(0 100%|inset\(0 0 0 100%', obj):  # re-hide wipe — not an appearance
            continue
        note(sel, off)
    return box_in, chrome_in, content_in

def main():
    d = sys.argv[1].rstrip('/')
    html = open(os.path.join(d, 'index.html')).read()
    name = os.path.basename(d)
    segs = parse_views(html)
    beats = []
    # both id-before-src and src-before-id orderings (match check-edl)
    pats = [r'<div\b[^>]*\bid="(beat-[a-z0-9-]+)"[^>]*data-composition-src="compositions/([^"]+)"[^>]*data-start="([0-9.]+)"[^>]*data-duration="([0-9.]+)"',
            r'<div\b[^>]*data-composition-src="compositions/([^"]+)"[^>]*\bid="(beat-[a-z0-9-]+)"[^>]*data-start="([0-9.]+)"[^>]*data-duration="([0-9.]+)"']
    seen = set()
    for i, pat in enumerate(pats):
        for mm in re.finditer(pat, html, re.S):
            if i == 0: bid, src, ds, dd = mm.group(1), mm.group(2), float(mm.group(3)), float(mm.group(4))
            else:      src, bid, ds, dd = mm.group(1), mm.group(2), float(mm.group(3)), float(mm.group(4))
            if bid in seen: continue
            seen.add(bid)
            box_in, chrome_in, content_in = first_offsets(os.path.join(d, 'compositions', src))
            beats.append((bid, ds, dd, box_in, chrome_in, content_in))
    beats.sort(key=lambda b: b[1])
    print(f"=== check-content (empty-box): {name} ===")
    fails = []
    for bid, ds, dd, box_in, chrome_in, content_in in beats:
        # content_in is None => content not separately animated (chart drawn via JS, or a card
        # whose text rides its own fade). Populated, not empty — skip (human frame-review covers it).
        if content_in is None:
            continue
        # 1) EMPTY CONTAINER (the literal "box"): a card/panel on screen with nothing inside it.
        if box_in is not None and content_in - box_in > BOX_FAIL:
            ef, et = ds + box_in, ds + content_in
            if overlaps_modea(segs, ef, et):
                fails.append(('EMPTY BOX', bid, box_in, content_in, f"{mmss(ef)}-{mmss(et)}"))
                continue
        # 2) SPARSE HOLD: only a title/eyebrow up, no content, for too long (no container case).
        shell_in = min([x for x in (box_in, chrome_in) if x is not None], default=0.0)
        if content_in - shell_in > SPARSE_FAIL:
            ef, et = ds + shell_in, ds + content_in
            if overlaps_modea(segs, ef, et):
                fails.append(('SPARSE', bid, shell_in, content_in, f"{mmss(ef)}-{mmss(et)}"))
    if fails:
        print(f"  FAILS (empty container >{BOX_FAIL}s, or sparse hold >{SPARSE_FAIL}s, during Mode-A):")
        for kind, bid, ref, cin, tc in sorted(fails, key=lambda f: -(f[3]-f[2])):
            print(f"      [{kind:9}] {bid}: shell @+{ref:.2f}s  content @+{cin:.2f}s "
                  f"= {cin-ref:.1f}s empty   [{tc}]")
        print(f"  >>> {name}: FAIL")
        return 1
    print(f"  >>> {name}: PASS ✓ (no empty container, no sparse hold)")
    return 0

if __name__ == '__main__':
    sys.exit(main())
