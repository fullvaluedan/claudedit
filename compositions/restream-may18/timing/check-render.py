#!/usr/bin/env python3
"""
check-render.py — the GATE. Measures the RENDERED output of a clip, not the EDL/plan.
This is the check that was missing: every prior round verified the spec or sampled
convenient frames; nothing measured whether the rendered left-zone is filled at every
second. Run this on every clip before declaring it done. ANY fail = not done.

Usage:  python3 check-render.py <clip-dir>            # uses <clip>-HQ.mp4 or verify.mp4
        python3 check-render.py <clip-dir> --mp4 path

Checks (all mechanical, immune to what the EDL claims):
  1. BLANK-LEFT COVERAGE (the key one): scan the rendered video; in the LEFT 60%
     (the graphics zone), find any run >1.5s where max-luminance < 100 (no bright
     text/graphic AND no host face = truly empty). Full-frame (host present) and
     sparse-but-visible graphics (white text present) both have high YMAX → not flagged.
  2. lint: npx hyperframes lint → 0 errors.
  3. z-index: every overlay beat id is in a z-index:3 rule.
  4. index: no on-screen "0N" clip-number element.
  5. jargon: no garbled Whisper terms on screen (burp / deep in / graft work / stake rate / ...).
"""
import sys, os, re, subprocess, glob

THRESH_YMAX = 100      # below this = no bright content in the zone
MIN_BLANK   = 1.5      # seconds; a dark-left run longer than this fails
LEFT_W      = 1120     # left graphics zone width (of 1920)

def find_mp4(d):
    # prefer the NEWEST render (verify.mp4 during iteration; HQ after final) so the gate
    # never reads a stale file while you're still fixing.
    cands = [p for p in (glob.glob(os.path.join(d,'renders','*-HQ.mp4')) +
             [os.path.join(d,'renders','verify.mp4')]) if os.path.exists(p)]
    return max(cands, key=os.path.getmtime) if cands else None

def blank_left_runs(mp4):
    # sample left-60% max-luminance at 2 fps via signalstats
    cmd = ['ffmpeg','-nostdin','-i',mp4,'-vf',
           f'crop={LEFT_W}:1080:0:0,fps=2,signalstats,metadata=print:file=-','-an','-f','null','-']
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    t=None; series=[]
    for line in out.splitlines():
        m=re.search(r'pts_time:([0-9.]+)', line)
        if m: t=float(m.group(1)); continue
        m=re.search(r'YMAX=([0-9.]+)', line)
        if m and t is not None: series.append((t, float(m.group(1))))
    runs=[]; start=None; last=None
    for t,y in series:
        if y < THRESH_YMAX:
            if start is None: start=t
            last=t
        else:
            if start is not None and (last-start) >= MIN_BLANK: runs.append((start,last))
            start=None
    if start is not None and (last-start) >= MIN_BLANK: runs.append((start,last))
    return runs

def grep_html(d, pattern, flags=re.I):
    hits=[]
    for f in glob.glob(os.path.join(d,'compositions','*.html')):
        for i,ln in enumerate(open(f, errors='ignore'),1):
            if re.search(pattern, ln, flags): hits.append(f"{os.path.basename(f)}:{i}")
    return hits

def zindex_ok(d):
    idx=os.path.join(d,'index.html')
    if not os.path.exists(idx): return False, ['index.html MISSING']
    html=open(idx).read(); slug=r'beat-[a-z0-9-]+'
    hosts=set(re.findall(r'data-composition-src="compositions/('+slug+r')\.html"', html))
    # map host file -> div id
    ids=set()
    for m in re.finditer(r'<div\b[^>]*\bid="('+slug+r')"[^>]*data-composition-src', html): ids.add(m.group(1))
    for m in re.finditer(r'data-composition-src="compositions/'+slug+r'\.html"[^>]*\bid="('+slug+r')"', html): ids.add(m.group(1))
    zids=set()
    for sel in re.findall(r'([^{}]*)\{[^{}]*z-index:\s*3\b', html, re.S):
        zids.update(re.findall(r'#('+slug+r')', sel))
    missing = ids - zids
    return (len(ids)>0 and not missing), (sorted(missing) if missing else [])

def main():
    d=sys.argv[1].rstrip('/')
    mp4=find_mp4(d)
    name=os.path.basename(d); fails=[]
    print(f"=== check-render: {name} ===")
    # 1. blank-left coverage
    if not mp4:
        print("  COVERAGE: no render found (skipped) — render a draft first"); fails.append('no-render')
    else:
        runs=blank_left_runs(mp4)
        if runs:
            print(f"  COVERAGE: FAIL — {len(runs)} blank-left run(s) >{MIN_BLANK}s:")
            for s,e in runs: print(f"      blank left {s:.1f}-{e:.1f}s ({e-s:.1f}s)")
            fails.append('blank-left')
        else: print(f"  COVERAGE: OK (no blank-left >{MIN_BLANK}s) [{os.path.basename(mp4)}]")
    # 2. lint
    try:
        lint=subprocess.run(['npx','hyperframes','lint'], cwd=d, capture_output=True, text=True)
        errs=re.search(r'(\d+)\s+error', lint.stdout+lint.stderr)
        n=int(errs.group(1)) if errs else -1
        print(f"  LINT: {'OK' if n==0 else 'FAIL ('+str(n)+' errors)'}");  (n!=0) and fails.append('lint')
    except Exception as e: print(f"  LINT: skipped ({e})")
    # 3. z-index
    ok,missing=zindex_ok(d); print(f"  Z-INDEX: {'OK' if ok else 'FAIL missing '+str(missing)}"); (not ok) and fails.append('z-index')
    # 4. index counter
    idx=grep_html(d, r'<div[^>]*-idx"[^>]*>\s*[0-9]')
    print(f"  INDEX: {'OK (no 0N)' if not idx else 'FAIL '+str(idx)}"); idx and fails.append('index')
    # 5. jargon
    jar=grep_html(d, r'>[^<]*\b(burp|deep in|deepin|graft work|stake rate|insaturable|meme con)\b[^<]*<')
    print(f"  JARGON: {'OK' if not jar else 'FAIL '+str(jar)}"); jar and fails.append('jargon')
    print(f"  >>> {name}: {'PASS ✓' if not fails else 'FAIL — '+', '.join(fails)}")
    return 1 if fails else 0

if __name__=='__main__': sys.exit(main())
