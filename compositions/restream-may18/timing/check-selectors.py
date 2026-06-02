#!/usr/bin/env python3
"""
check-selectors.py — STATIC. Every GSAP target selector must resolve to a real element.

The root cause of text floating over the speaker's face (the #br-title bug): an exit tween
targeted `#br-title` but the element was `class="br-title"`, so the tween silently no-op'd and
the title never left. A selector that matches nothing is a silent failure GSAP never reports.

This gate enumerates every animation target in each sub-composition and FAILs if any #id or
.class token doesn't exist in that same file. Instant, no render. Catches the bug at build time.

Usage: python3 check-selectors.py <clip-dir>
"""
import sys, os, re, glob

# .to / .from / .fromTo / .set ( <selector> , ...   where selector is "..." or S + "..."
CALL = re.compile(r'\.(?:to|from|fromTo|set)\(\s*("(?:[^"\\]|\\.)*"|S\s*\+\s*"[^"]*")')

def tokens(selstr):
    """Return the #id / .class tokens referenced by one selector argument (may be a comma list
    and/or descendant chain). Strips the `S + ` scope prefix and quotes."""
    s = selstr.strip()
    s = re.sub(r'^S\s*\+\s*', '', s)        # drop scope var
    s = s.strip('"')
    out = []
    for piece in s.split(','):              # comma list = multiple targets
        for m in re.finditer(r'([#.])([A-Za-z0-9_-]+)', piece):   # each simple selector in the chain
            out.append((m.group(1), m.group(2)))
    return out

def referenced_beats(d):
    """Only check sub-comps actually wired into index.html (skip unused catalog demo files)."""
    idx = os.path.join(d, 'index.html')
    if not os.path.exists(idx): return None
    srcs = re.findall(r'data-composition-src="compositions/([^"]+)"', open(idx, errors='ignore').read())
    return {os.path.join(d, 'compositions', s) for s in srcs}

def main():
    d = sys.argv[1].rstrip('/')
    ref = referenced_beats(d)
    files = sorted(glob.glob(os.path.join(d, 'compositions', '*.html')))
    if ref is not None:
        files = [f for f in files if f in ref]
    fails = []
    for f in files:
        html = open(f, errors='ignore').read()
        # ids/classes from static attrs AND from JS-created elements (createElement + setAttribute/
        # className/classList) and template-literal class="..." — else SVG charts etc. false-positive.
        ids = set(re.findall(r'\bid="([A-Za-z0-9_-]+)"', html))
        ids.update(re.findall(r'\.id\s*=\s*["\']([A-Za-z0-9_-]+)', html))
        ids.update(re.findall(r'setAttribute\(\s*["\']id["\']\s*,\s*["\']([A-Za-z0-9_-]+)', html))
        classes = set()
        for cm in re.findall(r'\bclass="([^"]+)"', html): classes.update(cm.split())
        for cm in re.findall(r'className\s*=\s*["\']([^"\']+)', html): classes.update(cm.split())
        for cm in re.findall(r'classList\.add\(([^)]*)\)', html): classes.update(re.findall(r'["\']([A-Za-z0-9_-]+)', cm))
        for cm in re.findall(r'setAttribute\(\s*["\']class["\']\s*,\s*["\']([^"\']+)', html): classes.update(cm.split())
        for m in CALL.finditer(html):
            for kind, name in tokens(m.group(1)):
                if kind == '#' and name not in ids:
                    fails.append((os.path.basename(f), f'#{name}', 'no element with this id'))
                elif kind == '.' and name not in classes:
                    fails.append((os.path.basename(f), f'.{name}', 'no element with this class'))
    name = os.path.basename(d)
    print(f"=== check-selectors: {name} ===")
    if fails:
        print("  UNRESOLVED GSAP TARGETS (tween silently no-ops -> element never animates/exits):")
        seen = set()
        for fn, sel, why in fails:
            k = (fn, sel)
            if k in seen: continue
            seen.add(k)
            print(f"      {fn}: {sel}  ({why})")
        print(f"  >>> {name}: FAIL (unresolved selector)")
        return 1
    print(f"  >>> {name}: PASS ✓ (every animation target resolves)")
    return 0

if __name__ == '__main__':
    sys.exit(main())
