#!/usr/bin/env python3
"""Place V2 overlays + V3 caption tracks onto the 5 Premiere sequences.

Track layout:
  V1: A-roll (speaker footage)
  V2: Kinetic openers (solid bg, 0–1.9s) + stat/dtree overlays
  V3: Caption tracks (transparent MOV, full clip duration)

This version uses claudedit_helpers.py for:
  - versioned filenames (no media-offline window)
  - render integrity check before placing
  - transcript auto-timing for stat graphics
  - caption sync verification
  - project verification + auto-save

Run AFTER build_new_sequences.py and AFTER all MOVs are rendered.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import claudedit_helpers as h
import json

# ── CONFIG — VERIFY THESE ───────────────────────────────────────────────────
RENDERS = Path("/Users/dan/Movies/_FINALS/clips-output/new-clips/renders")
TRANSCRIPT = Path("/Users/dan/Movies/_FINALS/clips-output/live-may18/transcripts/transcript.json")
EXPECTED_PROJECT_NAME = "MCP Test"   # must match Premiere title bar
OPENER_DUR = 1.9                     # cap to stay in kinetic-type Scene 1
ENABLE_CAPTIONS = False              # captions off for now — set True to re-enable

# Each graphic beat:
#   base_file  : the base render name (helpers find the latest _vN automatically)
#   at         : manual placement time (fallback if no cue phrase)
#   dur        : graphic duration on timeline
#   cue        : optional phrase to auto-time the graphic to when it's spoken
#   clip_in/out: absolute source timecodes (for transcript window + caption sync)
SEQUENCES = {
    "ibit-retail-unlocked-v2": {
        "clip_in": 961, "clip_out": 1015,
        "v2": [
            {"base": "opener-ibit-retail.mov", "at": 0,  "dur": OPENER_DUR, "cue": None},
            {"base": "stat-1-ibit-oi.mov",     "at": 12, "dur": 7, "cue": "open interest"},
            {"base": "lower-third-cole-5s.mov","at": 32, "dur": 5, "cue": None},
        ],
        "caption_base": "captions-ibit-retail-unlocked.mov",
    },
    "ibit-vol-premium": {
        "clip_in": 921, "clip_out": 956,
        "v2": [
            {"base": "opener-ibit-premium.mov","at": 0,  "dur": OPENER_DUR, "cue": None},
            {"base": "stat-2-bviv-premium.mov","at": 13, "dur": 8, "cue": "volatility premium"},
        ],
        "caption_base": "captions-ibit-vol-premium.mov",
    },
    "options-ux-evolution": {
        "clip_in": 1301, "clip_out": 1337,
        "v2": [
            {"base": "opener-options-ux.mov",  "at": 0, "dur": OPENER_DUR, "cue": None},
            {"base": "dtree-3-ux-evolution.mov","at": 9, "dur": 18, "cue": None},
        ],
        "caption_base": "captions-options-ux-evolution.mov",
    },
    "decacorn-index": {
        "clip_in": 1800, "clip_out": 1842,
        "v2": [
            {"base": "opener-decacorn.mov",    "at": 0,  "dur": OPENER_DUR, "cue": None},
            {"base": "stat-4-index-biz.mov",   "at": 12, "dur": 8, "cue": "eighty billion"},
            {"base": "lower-third-cole-7s.mov","at": 30, "dur": 7, "cue": None},
        ],
        "caption_base": "captions-decacorn-index.mov",
    },
    "crypto-spectrum": {
        "clip_in": 2302, "clip_out": 2360,
        "v2": [
            {"base": "opener-btc-binary.mov",     "at": 0,  "dur": OPENER_DUR, "cue": None},
            {"base": "stat-5-binary-vs-btc.mov",  "at": 14, "dur": 8, "cue": None},
            {"base": "dtree-5-crypto-spectrum.mov","at": 34, "dur": 16, "cue": None},
        ],
        "caption_base": "captions-crypto-spectrum.mov",
    },
}


def resolve_beats(seq_name, cfg, words):
    """Resolve each beat to a real versioned file, integrity-check it,
    and auto-time it to its cue phrase if one is given."""
    clip_in, clip_out = cfg["clip_in"], cfg["clip_out"]
    clip_dur = clip_out - clip_in
    resolved = []
    problems = []

    for beat in cfg["v2"]:
        path = h.latest_version_path(RENDERS, beat["base"])
        if path is None:
            problems.append(f"no render found for {beat['base']}")
            continue

        chk = h.check_render(path, expected_dur_s=beat["dur"], tolerance_s=1.5)
        if not chk["ok"]:
            problems.append(f"{path.name}: {chk['reason']}")
            continue

        # Auto-time to spoken cue if provided and transcript available
        at = beat["at"]
        timing = "manual"
        if beat.get("cue") and words:
            abs_t = h.find_phrase_time(words, beat["cue"], clip_in, clip_out)
            if abs_t is not None:
                # place ~1s before the phrase so the graphic leads the speech
                at = max(0, round(abs_t - clip_in - 1.0, 1))
                timing = f"auto@'{beat['cue']}'"

        resolved.append({
            "path": str(path), "name": path.name,
            "at": at, "dur": beat["dur"], "timing": timing,
            "size_mb": round(chk["size_mb"], 1),
        })

# ── CAPTIONS DISABLED ────────────────────────────────────────────────────
    # User turned off captions (subtitle quality wasn't good enough yet).
    # To re-enable: set ENABLE_CAPTIONS = True at top of file.
    cap_info = None
    if ENABLE_CAPTIONS:
        cap_path = h.latest_version_path(RENDERS, cfg["caption_base"])
        if cap_path is None:
            problems.append(f"no caption render for {cfg['caption_base']}")
        else:
            chk = h.check_render(cap_path, expected_dur_s=clip_dur, tolerance_s=2.0)
            if not chk["ok"]:
                problems.append(f"caption {cap_path.name}: {chk['reason']}")
            else:
                cap_info = {"path": str(cap_path), "name": cap_path.name,
                            "dur": clip_dur, "size_mb": round(chk["size_mb"], 1)}
                if words:
                    lines = h.build_caption_lines(words, clip_in, clip_out)
                    sync = h.verify_caption_sync(lines, clip_dur)
                    if not sync["ok"]:
                        for issue in sync["issues"]:
                            problems.append(f"caption sync: {issue}")

    return resolved, cap_info, problems


def place_jsx(seq_name, beats, cap_info):
    beats_json = json.dumps(beats)
    cap_json = json.dumps(cap_info or {})
    all_files = [b["path"] for b in beats] + ([cap_info["path"]] if cap_info else [])
    all_json = json.dumps(all_files)

    return r"""
(function() {
  var SEQ_NAME = """ + json.dumps(seq_name) + r""";
  var BEATS    = """ + beats_json + r""";
  var CAP      = """ + cap_json + r""";
  var ALL      = """ + all_json + r""";
  var proj = app.project;
  var result = { seq: SEQ_NAME, placed: [], errors: [] };

  var seq = null;
  for (var s = 0; s < proj.sequences.numSequences; s++) {
    if (proj.sequences[s].name === SEQ_NAME) { seq = proj.sequences[s]; break; }
  }
  if (!seq) { result.errors.push("seq not found: " + SEQ_NAME); return JSON.stringify(result); }

  try { proj.importFiles(ALL, true, proj.rootItem, false); }
  catch(e) { result.errors.push("import: " + e.message); }

  function findItem(name) {
    function search(n) {
      if (!n) return null;
      if (n.name === name && n.type === 1) return n;
      if (n.children) for (var i=0;i<n.children.numItems;i++){var f=search(n.children[i]); if(f)return f;}
      return null;
    }
    return search(proj.rootItem);
  }

  // V2
  while (seq.videoTracks.numTracks < 2) seq.videoTracks.addTrack();
  var vt2 = seq.videoTracks[1];
  while (vt2.clips.numItems > 0) vt2.clips[0].remove(false, true);

  for (var i=0;i<BEATS.length;i++) {
    var b = BEATS[i];
    var item = findItem(b.name);
    if (!item) { result.errors.push("missing V2: " + b.name); continue; }
    var ci=new Time(); ci.seconds=0;
    var co=new Time(); co.seconds=b.dur;
    item.setInPoint(ci.ticks,4); item.setOutPoint(co.ticks,4);
    var pos=new Time(); pos.seconds=b.at;
    try { vt2.overwriteClip(item,pos); result.placed.push({f:b.name,t:"V2",at:b.at}); }
    catch(e){ result.errors.push("V2 "+b.name+": "+e.message); }
    item.clearInPoint(4); item.clearOutPoint(4);
  }

  // V3 captions
  if (CAP.name) {
    while (seq.videoTracks.numTracks < 3) seq.videoTracks.addTrack();
    var vt3 = seq.videoTracks[2];
    while (vt3.clips.numItems > 0) vt3.clips[0].remove(false, true);
    var cap = findItem(CAP.name);
    if (!cap) { result.errors.push("missing caption: " + CAP.name); }
    else {
      var ci2=new Time(); ci2.seconds=0;
      var co2=new Time(); co2.seconds=CAP.dur;
      cap.setInPoint(ci2.ticks,4); cap.setOutPoint(co2.ticks,4);
      var p2=new Time(); p2.seconds=0;
      try { vt3.overwriteClip(cap,p2); result.placed.push({f:CAP.name,t:"V3",at:0}); }
      catch(e){ result.errors.push("V3 "+CAP.name+": "+e.message); }
      cap.clearInPoint(4); cap.clearOutPoint(4);
    }
  }

  return JSON.stringify(result);
})();
"""


def main():
    print("Checking Premiere project…")
    info = h.verify_project(EXPECTED_PROJECT_NAME)
    if info.get("error"):
        print(f"  ✗ Bridge error: {info}"); return
    print(f"  Open project: {info.get('project_name')}")
    if not info["correct"]:
        print(f"  ✗ WRONG PROJECT. Expected '{EXPECTED_PROJECT_NAME}', "
              f"found '{info.get('project_name')}'. Open the right one and re-run.")
        return
    missing = [n for n in SEQUENCES if n not in info.get("sequences", [])]
    if missing:
        print(f"  ✗ Missing sequences (run build script first): {missing}"); return
    print("  ✓ Project + sequences confirmed.\n")

    # Load transcript once
    words = []
    if TRANSCRIPT.exists():
        words = h.load_transcript(TRANSCRIPT)
        print(f"Transcript loaded: {len(words)} words\n")
    else:
        print(f"⚠ Transcript not found at {TRANSCRIPT}")
        print("  Graphics will use manual timing; caption sync NOT verified.\n")

    # Resolve + integrity check everything BEFORE placing anything
    print("Resolving renders (versioned + integrity check + auto-timing)…")
    plan = {}
    blocked = False
    for seq_name, cfg in SEQUENCES.items():
        beats, cap, problems = resolve_beats(seq_name, cfg, words)
        plan[seq_name] = (beats, cap)
        print(f"\n  {seq_name}")
        for b in beats:
            print(f"    V2 {b['name']}  @{b['at']}s  ({b['timing']}, {b['size_mb']}MB)")
        if cap:
            print(f"    V3 {cap['name']}  full {cap['dur']}s  ({cap['size_mb']}MB)")
        for p in problems:
            print(f"    ✗ {p}")
            blocked = True

    if blocked:
        print("\n✗ BLOCKED — fix the issues above (re-render bad files) before placing.")
        print("  Nothing was placed. No files touched in Premiere.")
        return

    # Place
    print("\nPlacing graphics…")
    total = 0
    for seq_name, (beats, cap) in plan.items():
        resp = h._parse(h.bridge_call(place_jsx(seq_name, beats, cap), timeout=180))
        placed = resp.get("placed", [])
        for p in placed:
            print(f"  ✓ {seq_name}: {p['t']} {p['f']} @{p['at']}s")
        for e in resp.get("errors", []):
            print(f"  ✗ {seq_name}: {e}")
        total += len(placed)

    print(f"\nTotal placed: {total}")
    print("Saving project…")
    print("  ✓ saved." if h.save_project() else "  ⚠ save failed — press Cmd+S manually.")


if __name__ == "__main__":
    main()
