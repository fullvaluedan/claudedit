#!/usr/bin/env python3
"""
check-text.py — STATIC. Everything that goes ON SCREEN as text/CSS, checked against the rules.
Four sub-checks, all instant, no render:

  R4  DUPLICATE WORDS — the same notable word in two text slots of one beat ("frontrunners" in
      eyebrow AND sublabel = rejected). Each slot must earn distinct words.
  R3  JARGON — reads timing/_JARGON.md (single source of truth, not a frozen regex) and FAILs if
      any "Whisper heard" mis-spelling reaches the screen (burp/deep in/graft work/...).
  R6  INDEX — no on-screen "0N" clip number.
  STYLE — no backdrop-filter blur and no film-grain overlay (rejected look; cards are solid
      translucent fill + one accent bar).

Usage: python3 check-text.py <clip-dir>
"""
import sys, os, re, glob

STOP = set('''THE A AN AND OR BUT OF TO IN ON FOR WITH AS AT BY IS ARE WAS WERE BE IT ITS THIS THAT
THESE THOSE YOU YOUR WE OUR THEY THEM NOT NO YES INTO FROM OVER THAN THEN NOW HERE WHEN WHAT WHY HOW
ALL ANY ONE TWO MORE MOST WILL CAN HAS HAVE HAD WHO WHICH PER VS'''.split())

def jargon_terms(timing_dir):
    """Quoted 'Whisper heard' mis-spellings from col 1 of _JARGON.md (the ones to keep OFF screen)."""
    p = os.path.join(timing_dir, '_JARGON.md')
    terms = []
    if not os.path.exists(p): return terms
    for ln in open(p, errors='ignore'):
        if not ln.strip().startswith('|'): continue
        col1 = ln.split('|')[1] if ln.count('|') >= 2 else ''
        for q in re.findall(r'"([^"]+)"', col1):
            q = q.strip()
            # keep only the ones explicitly to AVOID (skip "leave as" guidance rows handled below)
            if q and not q.lower().startswith('leave as'):
                terms.append(q)
    # rows that say "leave as X / do NOT correct" — the quoted heard term there is INTENTIONAL, drop it
    keep_ok = set()
    for ln in open(p, errors='ignore'):
        if 'leave as' in ln.lower() or 'do not' in ln.lower() or 'intentional' in ln.lower():
            for q in re.findall(r'"([^"]+)"', ln): keep_ok.add(q.strip().lower())
    return [t for t in terms if t.lower() not in keep_ok]

def visible_slots(html):
    """List of (slot_id_or_class, UPPERCASE_text) for elements that carry visible text."""
    slots = []
    for m in re.finditer(r'<(?:div|span|p|h[1-9])\b([^>]*)>([^<]*[A-Za-z][^<]*)</', html):
        attrs, txt = m.group(1), m.group(2)
        idm = re.search(r'\bid="([^"]+)"', attrs); clm = re.search(r'\bclass="([^"]+)"', attrs)
        slot = (idm.group(1) if idm else (clm.group(1).split()[0] if clm else '?'))
        t = re.sub(r'&[a-z]+;', ' ', txt)
        slots.append((slot, t.upper()))
    return slots

def referenced_beats(d):
    idx = os.path.join(d, 'index.html')
    if not os.path.exists(idx): return None
    srcs = re.findall(r'data-composition-src="compositions/([^"]+)"', open(idx, errors='ignore').read())
    return {os.path.join(d, 'compositions', s) for s in srcs}

def main():
    d = sys.argv[1].rstrip('/')
    jterms = jargon_terms(os.path.dirname(os.path.abspath(__file__)))   # _JARGON.md sits beside this script
    ref = referenced_beats(d)
    files = sorted(glob.glob(os.path.join(d, 'compositions', '*.html')))
    if ref is not None: files = [f for f in files if f in ref]   # only beats wired into the clip
    name = os.path.basename(d)
    print(f"=== check-text: {name} ===")
    fails = []     # hard PASS/FAIL: jargon, index, blur (mechanical, no false positives)
    advis = []     # advisory: duplicate words (taste — can't tell topic-word/anaphora from redundancy)
    for f in files:
        b = os.path.basename(f)
        html = open(f, errors='ignore').read()
        slots = visible_slots(html)
        # R4 duplicate notable words — ADVISORY only. Skip anaphora (same word in 3+ slots = device).
        word_slots = {}
        for slot, txt in slots:
            for w in set(re.findall(r'[A-Z][A-Z]{4,}', txt)):
                if w in STOP: continue
                word_slots.setdefault(w, set()).add(slot)
        for w, ss in word_slots.items():
            if len(ss) == 2:   # exactly two slots = possible redundancy worth a human glance
                advis.append((b, f'"{w}" in slots: {", ".join(sorted(ss))}'))
        # R3 jargon mis-spellings on screen (reads _JARGON.md)
        flat = ' '.join(t for _, t in slots)
        for term in jterms:
            if re.search(r'\b' + re.escape(term.upper()) + r'\b', flat):
                fails.append(('R3-jargon', b, f'garbled term on screen: "{term}"'))
        # R6 on-screen index
        if re.search(r'-idx"[^>]*>\s*[0-9]', html):
            fails.append(('R6-index', b, 'on-screen 0N clip index'))
        # STYLE no blur / grain over video
        if re.search(r'backdrop-filter\s*:\s*[^;]*blur', html) or re.search(r'filter\s*:\s*[^;]*blur', html):
            fails.append(('STYLE-blur', b, 'backdrop-filter/blur over video (rejected)'))
        if re.search(r'(grain|film-?noise)\b', html, re.I) and re.search(r'background-image|url\(', html):
            fails.append(('STYLE-grain', b, 'possible film-grain overlay (rejected) — verify'))
    if advis:
        print("  ADVISORY — duplicate notable words (review; not a fail):")
        for b, msg in advis: print(f"      {b}: {msg}")
    if fails:
        print("  FAILS (jargon / index / blur):")
        for kind, b, msg in fails: print(f"      [{kind}] {b}: {msg}")
        print(f"  >>> {name}: FAIL")
        return 1
    print(f"  >>> {name}: PASS ✓ (no garbled jargon, no index, no blur/grain)")
    return 0

if __name__ == '__main__':
    sys.exit(main())
