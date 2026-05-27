#!/usr/bin/env python3.11
"""
build_podcast_sequence.py — Build a multi-cam podcast sequence in Premiere Pro.

Reads edit_spec.json (from podcast_edit.py) and builds the full sequence via
the Premiere bridge. Sources must already be imported into the Premiere project.

Track layout:
  V2: B-roll (inserts over talking heads at topic-matched moments)
  V1: Main edit — host cam / guest cam / split screen, switching per speaker activity
  A1: Host cam full-duration isolated audio (no cuts, continuous)
  A2: Guest cam full-duration isolated audio (no cuts, sync-offset applied)

Usage:
  python3.11 build_podcast_sequence.py --spec /tmp/edit_spec.json
  python3.11 build_podcast_sequence.py --spec /tmp/edit_spec.json --batch-size 60
"""
import json
import os
import time
import argparse
from pathlib import Path

BRIDGE = "/tmp/premiere-mcp-bridge"

# Core ExtendScript template — DATA_PLACEHOLDER is replaced with JSON edit spec
EXTENDSCRIPT_TEMPLATE = r"""(function() {
  var proj = app.project;
  var TICKS = 254016000000;
  var FPS = 30;
  var TPFRAME = 8467200000;  // ticks per frame at 30fps

  // Build source registry from entire project bin
  var sources = {};
  function findAll(node) {
    if (!node) return;
    if (node.type === 1) { sources[node.name] = node; }
    if (node.children) {
      for (var i = 0; i < node.children.numItems; i++) findAll(node.children[i]);
    }
  }
  findAll(proj.rootItem);

  function getSrc(filePath) {
    if (!filePath) return null;
    var name = filePath.split('/').pop();
    return sources[name] || null;
  }

  // Frame-snap: round seconds to nearest frame boundary
  function secToTicks(sec) {
    return String(Math.round(sec * FPS) * TPFRAME);
  }

  var data = DATA_PLACEHOLDER;
  var slug = data.sequence_name;
  var cuts = data.video_cuts;
  var audioTracks = data.audio_tracks;
  var broll = data.broll || [];

  // Verify all sources exist in the Premiere project
  var needed = [];
  if (data.sources.reference) needed.push(data.sources.reference);
  if (data.sources.host_cam) needed.push(data.sources.host_cam);
  if (data.sources.guest_cam) needed.push(data.sources.guest_cam);
  for (var i = 0; i < (data.sources.broll || []).length; i++) needed.push(data.sources.broll[i]);

  var missing = [];
  for (var i = 0; i < needed.length; i++) {
    var name = needed[i].split('/').pop();
    if (!sources[name]) missing.push(name);
  }
  if (missing.length > 0) {
    return JSON.stringify({
      error: "Missing in Premiere project bin: " + missing.join(", ") +
             ". Import these files into Premiere first, then re-run."
    });
  }

  // Delete existing sequence with same name
  for (var s = proj.sequences.numSequences - 1; s >= 0; s--) {
    if (proj.sequences[s].name === slug) {
      proj.deleteSequence(proj.sequences[s]);
      break;
    }
  }

  var errs = [];

  // ─── V1: Create sequence from first cut ────────────────────────────────────
  var cut0 = cuts[0];
  var src0 = getSrc(cut0.file);
  if (!src0) return JSON.stringify({error: "First cut source not found: " + cut0.file});

  var inT0  = new Time(); inT0.ticks  = secToTicks(cut0.media_in);
  var outT0 = new Time(); outT0.ticks = secToTicks(cut0.media_out);
  src0.setInPoint(inT0.ticks, 4);
  src0.setOutPoint(outT0.ticks, 4);
  var seq = proj.createNewSequenceFromClips(slug, [src0]);
  src0.clearInPoint(4);
  src0.clearOutPoint(4);

  // ─── V1: Append remaining cuts ─────────────────────────────────────────────
  for (var c = 1; c < cuts.length; c++) {
    try {
      var cut = cuts[c];
      var src = getSrc(cut.file);
      if (!src) { errs.push("cut" + c + ": source not found"); continue; }

      var inTc  = new Time(); inTc.ticks  = secToTicks(cut.media_in);
      var outTc = new Time(); outTc.ticks = secToTicks(cut.media_out);
      src.setInPoint(inTc.ticks, 4);
      src.setOutPoint(outTc.ticks, 4);

      var posT = new Time(); posT.ticks = secToTicks(cut.timeline_pos);
      seq.videoTracks[0].overwriteClip(src, posT);

      src.clearInPoint(4);
      src.clearOutPoint(4);
    } catch(e) {
      try {
        var s2 = getSrc(cuts[c].file);
        if (s2) { s2.clearInPoint(4); s2.clearOutPoint(4); }
      } catch(e2) {}
      errs.push("cut" + c + ": " + e.message);
    }
  }

  // ─── A1: Clear auto-placed audio, replace with full-duration host audio ────
  try {
    var at0 = seq.audioTracks[0];
    while (at0.clips.numItems > 0) { at0.clips[0].remove(false, true); }
  } catch(e) { errs.push("a1clear: " + e.message); }

  // ─── A1/A2: Place full-duration isolated audio tracks ─────────────────────
  for (var ai = 0; ai < audioTracks.length; ai++) {
    try {
      var spec = audioTracks[ai];
      var asrc = getSrc(spec.file);
      if (!asrc) { errs.push("audio" + ai + ": source not found"); continue; }

      var aInT  = new Time(); aInT.ticks  = secToTicks(spec.media_in);
      var aOutT = new Time(); aOutT.ticks = secToTicks(spec.media_out);
      asrc.setInPoint(aInT.ticks, 4);
      asrc.setOutPoint(aOutT.ticks, 4);

      var aPosT = new Time(); aPosT.ticks = secToTicks(spec.timeline_pos);
      seq.audioTracks[spec.premiere_track].overwriteClip(asrc, aPosT);

      asrc.clearInPoint(4);
      asrc.clearOutPoint(4);
    } catch(e) {
      errs.push("audio" + ai + ": " + e.message);
    }
  }

  // ─── V2: B-roll ────────────────────────────────────────────────────────────
  for (var bi = 0; bi < broll.length; bi++) {
    try {
      var br    = broll[bi];
      var brsrc = getSrc(br.file);
      if (!brsrc) { errs.push("broll" + bi + ": source not found"); continue; }

      // B-roll starts at its own t=0, plays for duration_sec
      var brInT  = new Time(); brInT.ticks  = secToTicks(0.0);
      var brOutT = new Time(); brOutT.ticks = secToTicks(br.duration_sec);
      brsrc.setInPoint(brInT.ticks, 4);
      brsrc.setOutPoint(brOutT.ticks, 4);

      var brPosT = new Time(); brPosT.ticks = secToTicks(br.timeline_pos);
      seq.videoTracks[1].overwriteClip(brsrc, brPosT);

      brsrc.clearInPoint(4);
      brsrc.clearOutPoint(4);
    } catch(e) {
      errs.push("broll" + bi + ": " + e.message);
    }
  }

  // ─── Return stats ──────────────────────────────────────────────────────────
  var durSec = parseFloat(seq.end) / TICKS;
  return JSON.stringify({
    ok: true,
    sequence: slug,
    dur_sec: Math.round(durSec * 10) / 10,
    v1Clips: seq.videoTracks[0].clips.numItems,
    v2Clips: seq.videoTracks.numTracks > 1 ? seq.videoTracks[1].clips.numItems : -1,
    a1Clips: seq.audioTracks[0].clips.numItems,
    a2Clips: seq.audioTracks.numTracks > 1 ? seq.audioTracks[1].clips.numItems : -1,
    errs: errs.slice(0, 30)
  });
})()"""

APPEND_TEMPLATE = r"""(function() {
  var proj = app.project;
  var FPS = 30;
  var TPFRAME = 8467200000;
  function secToTicks(s) { return String(Math.round(s * FPS) * TPFRAME); }

  var sources = {};
  function findAll(n) {
    if (!n) return;
    if (n.type === 1) { sources[n.name] = n; }
    if (n.children) for (var i = 0; i < n.children.numItems; i++) findAll(n.children[i]);
  }
  findAll(proj.rootItem);
  function getSrc(f) { return sources[f.split('/').pop()] || null; }

  var slug = SEQ_NAME_PLACEHOLDER;
  var cuts = CUTS_PLACEHOLDER;

  var seq = null;
  for (var i = 0; i < proj.sequences.numSequences; i++) {
    if (proj.sequences[i].name === slug) { seq = proj.sequences[i]; break; }
  }
  if (!seq) return JSON.stringify({error: "sequence not found: " + slug});

  var errs = [];
  for (var c = 0; c < cuts.length; c++) {
    try {
      var cut = cuts[c];
      var src = getSrc(cut.file);
      if (!src) { errs.push("c" + c + ": not found"); continue; }

      var inT  = new Time(); inT.ticks  = secToTicks(cut.media_in);
      var outT = new Time(); outT.ticks = secToTicks(cut.media_out);
      src.setInPoint(inT.ticks, 4);
      src.setOutPoint(outT.ticks, 4);

      var posT = new Time(); posT.ticks = secToTicks(cut.timeline_pos);
      seq.videoTracks[0].overwriteClip(src, posT);

      src.clearInPoint(4);
      src.clearOutPoint(4);
    } catch(e) {
      errs.push("c" + c + ": " + e.message);
    }
  }

  return JSON.stringify({
    ok: true,
    appended: cuts.length,
    v1Clips: seq.videoTracks[0].clips.numItems,
    errs: errs
  });
})()"""


def send_bridge(script, timeout_sec=300):
    """Send ExtendScript to the Premiere bridge and wait for response."""
    cmd_id = f"podcast-{int(time.time())}"
    cmd_file = os.path.join(BRIDGE, f"command-{cmd_id}.json")
    resp_file = os.path.join(BRIDGE, f"response-{cmd_id}.json")

    with open(cmd_file, "w") as f:
        json.dump({"id": cmd_id, "script": script}, f)

    for _ in range(timeout_sec // 2):
        time.sleep(2)
        if os.path.exists(resp_file):
            with open(resp_file) as f:
                return json.load(f)

    return {"success": False, "error": "Bridge timeout — Premiere may be busy or not open."}


def build_sequence(spec, batch_size=80):
    """Build the sequence, batching cuts if the list is large."""
    cuts = spec["video_cuts"]

    if len(cuts) <= batch_size:
        # All cuts fit in a single bridge call
        print(f"  Sending {len(cuts)} cuts in one bridge call...")
        script = EXTENDSCRIPT_TEMPLATE.replace("DATA_PLACEHOLDER", json.dumps(spec))
        return send_bridge(script)

    # Split into batches to avoid CEP script size limits
    print(f"  Large cut list ({len(cuts)} cuts) — batching in groups of {batch_size}...")

    # First batch: create sequence + audio + broll + first N cuts
    first_spec = dict(spec)
    first_spec["video_cuts"] = cuts[:batch_size]
    print(f"  Batch 1: cuts 0–{batch_size - 1} + audio + b-roll...")
    script = EXTENDSCRIPT_TEMPLATE.replace("DATA_PLACEHOLDER", json.dumps(first_spec))
    result = send_bridge(script)

    if not result.get("success") or result.get("result", {}).get("error"):
        return result

    # Remaining batches: append cuts only
    for start in range(batch_size, len(cuts), batch_size):
        batch = cuts[start:start + batch_size]
        end_idx = min(start + batch_size, len(cuts))
        print(f"  Batch {start // batch_size + 1}: cuts {start}–{end_idx - 1}...")
        script = APPEND_TEMPLATE \
            .replace("SEQ_NAME_PLACEHOLDER", json.dumps(spec["sequence_name"])) \
            .replace("CUTS_PLACEHOLDER", json.dumps(batch))
        result = send_bridge(script)
        if not result.get("success"):
            print(f"  WARNING: Batch failed: {result}")
            break

    return result


def print_result(data, spec):
    """Print a human-friendly summary of the build result."""
    if data.get("error"):
        print(f"\n✗ BUILD FAILED: {data['error']}")
        return

    print(f"\n✓ Sequence built: '{data.get('sequence')}'")
    print(f"  Duration:  {data.get('dur_sec')}s ({data.get('dur_sec', 0) / 60:.1f} min)")
    print(f"  V1 clips:  {data.get('v1Clips')}  (video cuts — expected {spec['cut_count']})")
    print(f"  V2 clips:  {data.get('v2Clips')}  (b-roll)")
    print(f"  A1 clips:  {data.get('a1Clips')}  (host isolated audio)")
    print(f"  A2 clips:  {data.get('a2Clips')}  (guest isolated audio)")

    errs = data.get("errs", [])
    if errs:
        print(f"\n  ⚠ Warnings ({len(errs)}):")
        for e in errs:
            print(f"    - {e}")

    print(f"""
Next steps in Premiere:
  1. Open sequence '{data.get('sequence')}'
  2. Scrub through to review camera cuts and b-roll
  3. Set audio levels: open Audio Track Mixer, balance A1 (host) and A2 (guest)
  4. Adjust any cuts that feel off — the AI first pass is a starting point
""")


def main():
    parser = argparse.ArgumentParser(
        description="Build a multi-cam podcast sequence in Premiere Pro from an edit spec"
    )
    parser.add_argument("--spec", required=True, help="Path to edit_spec.json from podcast_edit.py")
    parser.add_argument(
        "--batch-size", type=int, default=80,
        help="Max video cuts per bridge call (default 80; lower if CEP crashes)"
    )
    args = parser.parse_args()

    with open(args.spec) as f:
        spec = json.load(f)

    print(f"Building Premiere sequence: '{spec['sequence_name']}'")
    print(f"  {spec['cut_count']} video cuts, {spec['total_duration_sec']:.1f}s total")
    print(f"  {len(spec.get('broll', []))} b-roll placements")
    src = spec["sources"]
    names = [Path(v).name for k, v in src.items()
             if isinstance(v, str) and v and k != "broll"]
    broll_names = [Path(b).name for b in (src.get("broll") or [])]
    print(f"  Sources: {', '.join(names)}")
    if broll_names:
        print(f"  B-roll:  {', '.join(broll_names)}")
    print()
    print("  ⚠ All source files must be imported into the Premiere project bin first.")
    print()

    result = build_sequence(spec, args.batch_size)

    # Unpack result
    if result.get("success"):
        data = result.get("result", {})
    else:
        data = {"error": result.get("error", str(result))}

    print_result(data, spec)


if __name__ == "__main__":
    main()
