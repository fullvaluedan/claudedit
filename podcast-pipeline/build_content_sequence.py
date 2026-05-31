#!/usr/bin/env python3
"""
build_content_sequence.py — Build a Premiere Pro sequence from content_edit.json.

Produces a single-cam edited sequence structured as:
  [Teaser clips 1-3] → [Intro] → [Main content with cuts applied]

All clips come from the same source file. Cross-dissolves are added at every
transition point. Sources must already be imported into the Premiere project.

Usage:
    python3 build_content_sequence.py \
        --edit /tmp/content_edit.json \
        [--sequence-name "Podcast Edit"] \
        [--project "MyProject"] \
        [--dissolve-frames 15] \
        [--batch-size 80]
"""

import argparse
import json
import math
import subprocess
import sys
import time
import os
from pathlib import Path

TICKS = 254016000000  # ticks per second (Premiere internal)


def _jround(x: float) -> int:
    """Round half-up to match ExtendScript Math.round (Python's round() is banker's)."""
    return math.floor(x + 0.5)


def detect_fps(source_path: str, default: float = 30.0) -> float:
    """Detect the source video frame rate via ffprobe (e.g. '24/1' → 24.0).

    CRITICAL: the Premiere sequence inherits the source's frame rate, so all
    timeline tick math must use THIS fps. Snapping to the wrong grid (e.g. 30
    when the source is 24) makes Premiere re-snap clip positions and leaves
    1-frame gaps between clips.
    """
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=r_frame_rate",
             "-of", "default=noprint_wrappers=1:nokey=1", source_path],
            capture_output=True, text=True, timeout=30).stdout.strip()
        num, den = (out.split("/") + ["1"])[:2] if out else ("0", "1")
        fps = float(num) / float(den)
        return fps if fps > 0 else default
    except Exception:
        return default


def _inject_fps(script: str, fps: float) -> str:
    """Substitute FPS_PLACEHOLDER / TPFRAME_PLACEHOLDER for the detected fps."""
    return (script.replace("FPS_PLACEHOLDER", "%g" % fps)
                  .replace("TPFRAME_PLACEHOLDER", str(round(TICKS / fps))))

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from claudedit_helpers import bridge_call, verify_project, save_project

BRIDGE_DIR = "/tmp/premiere-mcp-bridge"

# ---------------------------------------------------------------------------
# Clip list construction
# ---------------------------------------------------------------------------

def build_clip_list(edit: dict) -> list[dict]:
    """Return ordered list of {media_in, media_out, role} for sequence placement.
    Order: teaser clips → brief intro → main content (outro is last main segment).
    """
    clips = []

    # 1. Teaser clips first (top 3 by score, from anywhere in source)
    teasers = sorted(edit.get("teaser_clips", []), key=lambda x: -x.get("score", 0))[:3]
    for t in teasers:
        dur = float(t["end"]) - float(t["start"])
        if dur >= 1.0:
            clips.append({
                "media_in": float(t["start"]),
                "media_out": float(t["end"]),
                "role": "teaser",
            })

    # 2. Intro (brief — typically recorded at end of raw file, moved to front)
    intro = edit.get("intro", {})
    if float(intro.get("end", 0)) > float(intro.get("start", 0)):
        clips.append({
            "media_in": float(intro["start"]),
            "media_out": float(intro["end"]),
            "role": "intro",
        })

    # 3. Main segments in order (outro is naturally the last segment)
    for seg in edit.get("main_segments", []):
        dur = float(seg["end"]) - float(seg["start"])
        if dur >= 0.5:
            clips.append({
                "media_in": float(seg["start"]),
                "media_out": float(seg["end"]),
                "role": "main",
            })

    return clips


# ---------------------------------------------------------------------------
# ExtendScript template
# ---------------------------------------------------------------------------

EXTENDSCRIPT_TEMPLATE = r"""(function() {
  var proj = app.project;
  var FPS = FPS_PLACEHOLDER;
  var TICKS = 254016000000;
  var TPFRAME = TPFRAME_PLACEHOLDER;

  function secToTicks(sec) {
    return String(Math.round(parseFloat(sec) * FPS) * TPFRAME);
  }

  // Walk project bin and build filename → ProjectItem map
  var sources = {};
  function findAll(node) {
    if (!node) return;
    if (node.type === 1) { sources[node.name] = node; }
    if (node.children) {
      for (var i = 0; i < node.children.numItems; i++) findAll(node.children[i]);
    }
  }
  findAll(proj.rootItem);

  var data = DATA_PLACEHOLDER;
  var slug = data.sequenceName;
  var srcPath = data.sourcePath;
  var clips = data.clips;
  var dissolveFrames = data.dissolveFrames;

  // Verify source is in the project bin
  var srcName = srcPath.split('/').pop();
  var srcItem = sources[srcName] || null;
  if (!srcItem) {
    return JSON.stringify({
      error: "Source not found in Premiere project bin: " + srcName +
             ". Import the file into Premiere first (File > Import), then re-run."
    });
  }

  // Delete existing sequence with same name
  for (var s = proj.sequences.numSequences - 1; s >= 0; s--) {
    if (proj.sequences[s].name === slug) {
      proj.deleteSequence(proj.sequences[s]);
      break;
    }
  }

  if (clips.length === 0) {
    return JSON.stringify({error: "No clips to place."});
  }

  var errs = [];

  // ── Create sequence from first clip ────────────────────────────────────────
  var clip0 = clips[0];
  var inT0  = new Time(); inT0.ticks  = secToTicks(clip0.media_in);
  var outT0 = new Time(); outT0.ticks = secToTicks(clip0.media_out);
  srcItem.setInPoint(inT0.ticks, 4);
  srcItem.setOutPoint(outT0.ticks, 4);
  var seq = proj.createNewSequenceFromClips(slug, [srcItem]);
  srcItem.clearInPoint(4);
  srcItem.clearOutPoint(4);

  if (!seq) {
    return JSON.stringify({error: "createNewSequenceFromClips returned null. Check Premiere is open with a project."});
  }

  // cursor tracks current timeline end in ticks (frame-snapped).
  // Advance by the clip's ACTUAL snapped length = round(out*FPS) - round(in*FPS).
  // Using round((out-in)*FPS) instead drifts ±1 frame (round-of-diff ≠ diff-of-rounds),
  // leaving 1-frame gaps/overlaps between clips.
  var cursor = (Math.round(parseFloat(clip0.media_out) * FPS) - Math.round(parseFloat(clip0.media_in) * FPS)) * TPFRAME;

  // ── Append remaining clips ──────────────────────────────────────────────────
  for (var c = 1; c < clips.length; c++) {
    var clip = clips[c];
    var dur = parseFloat(clip.media_out) - parseFloat(clip.media_in);
    if (dur <= 0) continue;
    try {
      var cInT  = new Time(); cInT.ticks  = secToTicks(clip.media_in);
      var cOutT = new Time(); cOutT.ticks = secToTicks(clip.media_out);
      srcItem.setInPoint(cInT.ticks, 4);
      srcItem.setOutPoint(cOutT.ticks, 4);

      var posT = new Time(); posT.ticks = String(cursor);
      seq.videoTracks[0].overwriteClip(srcItem, posT);

      srcItem.clearInPoint(4);
      srcItem.clearOutPoint(4);
      cursor += (Math.round(parseFloat(clip.media_out) * FPS) - Math.round(parseFloat(clip.media_in) * FPS)) * TPFRAME;
    } catch(e) {
      try { srcItem.clearInPoint(4); srcItem.clearOutPoint(4); } catch(e2) {}
      errs.push("clip" + c + "(" + clip.role + "): " + e.message);
    }
  }

  // ── Audio ────────────────────────────────────────────────────────────────
  // No programmatic fades applied. Word-boundary snapping ensures all cuts
  // happen between words in silence — hard cuts in silence are imperceptible.
  //
  // DO NOT add Volume Level keyframes here. Clip-level keyframes at t=0 with
  // value=0 (silence) cause the Audio Clip Mixer to display −∞ and can
  // corrupt the track fader state. AudioTrack.components is not accessible
  // via CEP (causes crash), so track fader cannot be reset programmatically.
  //
  // To add Constant Power crossfades between specific cuts: place playhead
  // at the cut point and press Cmd+Shift+D (Mac) / Ctrl+Shift+D (Win).

  var durSec = parseFloat(seq.end) / TICKS;
  return JSON.stringify({
    ok: true,
    sequence: slug,
    dur_sec: Math.round(durSec * 10) / 10,
    v1Clips: seq.videoTracks[0].clips.numItems,
    a1Clips: seq.audioTracks[0].clips.numItems,
    errs: errs.slice(0, 30)
  });
})()"""

QA_TEMPLATE = r"""(function() {
  var TICKS = 254016000000;
  var TPFRAME = TPFRAME_PLACEHOLDER;
  var slug = QA_SEQ_NAME;
  var expectedClips = QA_EXPECTED_CLIPS;
  var expectedDurSec = QA_EXPECTED_DUR;

  var seq = null;
  for (var i = 0; i < app.project.sequences.numSequences; i++) {
    if (app.project.sequences[i].name === slug) { seq = app.project.sequences[i]; break; }
  }
  if (!seq) return JSON.stringify({pass: false, reason: "Sequence not found: " + slug});

  var v1 = seq.videoTracks[0];
  var a1 = seq.audioTracks[0];
  var v1count = v1.clips.numItems;
  var a1count = a1.clips.numItems;

  if (v1count !== a1count) {
    return JSON.stringify({pass: false, reason: "V1/A1 clip mismatch: V1=" + v1count + " A1=" + a1count});
  }
  if (v1count !== expectedClips) {
    return JSON.stringify({pass: false, reason: "Wrong clip count: got " + v1count + " expected " + expectedClips});
  }
  if (a1.isMuted()) {
    return JSON.stringify({pass: false, reason: "A1 track is muted"});
  }

  // Check for any clips under 0.5s
  var shortClips = [];
  for (var ci = 0; ci < v1.clips.numItems; ci++) {
    var dur = (parseFloat(v1.clips[ci].end.ticks) - parseFloat(v1.clips[ci].start.ticks)) / TICKS;
    if (dur < 0.5) shortClips.push({idx: ci, dur: Math.round(dur * 1000) / 1000});
  }
  if (shortClips.length > 0) {
    return JSON.stringify({pass: false, reason: "Short clips (<0.5s): " + JSON.stringify(shortClips)});
  }

  // First clip must start at or near timeline 0
  var firstStart = parseFloat(v1.clips[0].start.ticks) / TICKS;
  if (firstStart > 0.1) {
    return JSON.stringify({pass: false, reason: "First clip not at timeline 0: " + firstStart + "s"});
  }

  // Duration sanity: within 20% of expected
  var durSec = parseFloat(seq.end) / TICKS;
  if (expectedDurSec > 0 && Math.abs(durSec - expectedDurSec) / expectedDurSec > 0.20) {
    return JSON.stringify({pass: false, reason: "Duration anomaly: got " + Math.round(durSec) + "s expected ~" + Math.round(expectedDurSec) + "s"});
  }

  // Check A1 clips for Volume Level keyframes — if present, warn (they cause −∞ issue)
  var keyframedClips = [];
  for (var ki = 0; ki < a1.clips.numItems; ki++) {
    var ac = a1.clips[ki];
    for (var co = 0; co < ac.components.numItems; co++) {
      if (ac.components[co].displayName === "Volume") {
        for (var po = 0; po < ac.components[co].properties.numItems; po++) {
          if (ac.components[co].properties[po].displayName === "Level") {
            if (ac.components[co].properties[po].isTimeVarying()) {
              keyframedClips.push(ki);
            }
          }
        }
      }
    }
  }

  if (keyframedClips.length > 0) {
    return JSON.stringify({
      pass: false,
      reason: "A1 clips " + keyframedClips.join(",") + " have Volume Level keyframes (causes −∞ audio). " +
              "Delete this sequence and rebuild — the builder no longer sets keyframes."
    });
  }

  // Report transition coverage (audio crossfades smooth the cuts)
  var aTrans = 0, vTrans = 0;
  try { aTrans = a1.transitions.numItems; } catch(e) {}
  try { vTrans = v1.transitions.numItems; } catch(e) {}
  var junctions = v1count - 1;
  var warnings = [];
  if (junctions > 0 && aTrans < junctions) {
    warnings.push("Audio crossfades: " + aTrans + "/" + junctions + " junctions covered");
  }

  // Gap / overlap check on V1. With no video transitions, clips must be exactly
  // contiguous (frame-snapped). A positive gap reveals cursor frame-accounting drift.
  var maxGap = 0, gapAt = -1;
  for (var gi = 0; gi < v1count - 1; gi++) {
    var gapFr = (parseFloat(v1.clips[gi + 1].start.ticks) - parseFloat(v1.clips[gi].end.ticks)) / TPFRAME;
    if (gapFr > maxGap) { maxGap = gapFr; gapAt = gi; }
  }
  if (vTrans === 0 && maxGap >= 0.5) {
    return JSON.stringify({pass: false,
      reason: "Gap of " + Math.round(maxGap) + " frame(s) between V1 clips " + gapAt +
              " and " + (gapAt + 1) + " — cursor frame-accounting drift"});
  }

  return JSON.stringify({
    pass: true,
    sequence: slug,
    maxV1GapFrames: Math.round(maxGap),
    v1Clips: v1count,
    a1Clips: a1count,
    durSec: Math.round(durSec * 10) / 10,
    audioTransitions: aTrans,
    videoTransitions: vTrans,
    junctions: junctions,
    warnings: warnings
  });
})()"""

ADD_TRANSITIONS_TEMPLATE = r"""(function() {
  // Add Constant Power audio crossfades + (optionally) Cross Dissolve video
  // transitions at every clip junction, fully via the QE DOM.
  //
  // The QE transition *list* (getAudioTransitionList) is empty via CEP, but
  // getAudioTransitionByName / getVideoTransitionByName return usable objects.
  // Clip-level addTransition(trans, addToStart=false, durStr) adds at the tail.
  // Transitions live in a separate collection from clips, so clip indices do
  // not shift as we add — we can iterate forward safely.
  var proj = app.project;
  var slug = SEQ_NAME_PLACEHOLDER;
  var audioReq = AUDIO_REQ_PLACEHOLDER;   // duration units (~1.25x => timeline frames)
  var videoReq = VIDEO_REQ_PLACEHOLDER;   // 0 = skip video dissolves

  var seq = null;
  for (var i = 0; i < proj.sequences.numSequences; i++) {
    if (proj.sequences[i].name === slug) { seq = proj.sequences[i]; break; }
  }
  if (!seq) return JSON.stringify({error: "Sequence not found: " + slug});

  app.enableQE();
  var qeSeq = qe.project.getActiveSequence();
  if (!qeSeq || String(qeSeq.name) !== slug) {
    return JSON.stringify({error: "Sequence '" + slug + "' is not the active QE sequence (got '" +
      (qeSeq ? qeSeq.name : "none") + "'). Open it in the timeline and re-run."});
  }

  var cp = qe.project.getAudioTransitionByName("Constant Power");
  var xd = (videoReq > 0) ? qe.project.getVideoTransitionByName("Cross Dissolve") : null;
  if (!cp) return JSON.stringify({error: "Constant Power audio transition not found via QE"});

  var errs = [];
  var aAdded = 0, vAdded = 0;

  // Audio crossfades on A1 at each junction (tail of clips 0..N-2)
  var qeA = qeSeq.getAudioTrackAt(0);
  var aClips = seq.audioTracks[0].clips.numItems;
  for (var ai = 0; ai < aClips - 1; ai++) {
    try { qeA.getItemAt(ai).addTransition(cp, false, String(audioReq)); aAdded++; }
    catch(e) { errs.push("a" + ai + ":" + String(e)); }
  }

  // Video cross dissolves on V1 at each junction (optional)
  if (videoReq > 0 && xd) {
    var qeV = qeSeq.getVideoTrackAt(0);
    var vClips = seq.videoTracks[0].clips.numItems;
    for (var vi = 0; vi < vClips - 1; vi++) {
      try { qeV.getItemAt(vi).addTransition(xd, false, String(videoReq)); vAdded++; }
      catch(e) { errs.push("v" + vi + ":" + String(e)); }
    }
  }

  return JSON.stringify({
    ok: true,
    aAdded: aAdded,
    vAdded: vAdded,
    audioTransitions: seq.audioTracks[0].transitions.numItems,
    videoTransitions: seq.videoTracks[0].transitions.numItems,
    errs: errs.slice(0, 20)
  });
})()"""

APPEND_TEMPLATE = r"""(function() {
  var proj = app.project;
  var FPS = FPS_PLACEHOLDER;
  var TPFRAME = TPFRAME_PLACEHOLDER;
  function secToTicks(s) { return String(Math.round(parseFloat(s) * FPS) * TPFRAME); }

  var sources = {};
  function findAll(n) {
    if (!n) return;
    if (n.type === 1) { sources[n.name] = n; }
    if (n.children) for (var i = 0; i < n.children.numItems; i++) findAll(n.children[i]);
  }
  findAll(proj.rootItem);

  var slug = SEQ_NAME_PLACEHOLDER;
  var srcPath = SRC_PATH_PLACEHOLDER;
  var clips = CLIPS_PLACEHOLDER;
  var startCursor = START_CURSOR_PLACEHOLDER;

  var srcName = srcPath.split('/').pop();
  var srcItem = sources[srcName] || null;
  if (!srcItem) return JSON.stringify({error: "Source not found: " + srcName});

  var seq = null;
  for (var i = 0; i < proj.sequences.numSequences; i++) {
    if (proj.sequences[i].name === slug) { seq = proj.sequences[i]; break; }
  }
  if (!seq) return JSON.stringify({error: "Sequence not found: " + slug});

  var errs = [];
  var cursor = startCursor;

  for (var c = 0; c < clips.length; c++) {
    var clip = clips[c];
    var dur = parseFloat(clip.media_out) - parseFloat(clip.media_in);
    if (dur <= 0) continue;
    try {
      var inT  = new Time(); inT.ticks  = secToTicks(clip.media_in);
      var outT = new Time(); outT.ticks = secToTicks(clip.media_out);
      srcItem.setInPoint(inT.ticks, 4);
      srcItem.setOutPoint(outT.ticks, 4);

      var posT = new Time(); posT.ticks = String(cursor);
      seq.videoTracks[0].overwriteClip(srcItem, posT);

      srcItem.clearInPoint(4);
      srcItem.clearOutPoint(4);
      cursor += (Math.round(parseFloat(clip.media_out) * FPS) - Math.round(parseFloat(clip.media_in) * FPS)) * TPFRAME;
    } catch(e) {
      try { srcItem.clearInPoint(4); srcItem.clearOutPoint(4); } catch(e2) {}
      errs.push("c" + c + ": " + e.message);
    }
  }

  return JSON.stringify({ok: true, appended: clips.length, errs: errs});
})()"""


# ---------------------------------------------------------------------------
# Bridge helpers
# ---------------------------------------------------------------------------

def send_bridge(script: str, timeout_sec: int = 300) -> dict:
    """Send ExtendScript via filesystem bridge and wait for response."""
    cmd_id = f"content-seq-{int(time.time())}"
    cmd_file = os.path.join(BRIDGE_DIR, f"command-{cmd_id}.json")
    resp_file = os.path.join(BRIDGE_DIR, f"response-{cmd_id}.json")

    os.makedirs(BRIDGE_DIR, exist_ok=True)
    with open(cmd_file, "w") as f:
        json.dump({"id": cmd_id, "script": script}, f)

    for _ in range(timeout_sec // 2):
        time.sleep(2)
        if os.path.exists(resp_file):
            with open(resp_file) as f:
                data = json.load(f)
            try:
                os.remove(resp_file)
            except OSError:
                pass
            return data

    return {"success": False, "error": "Bridge timeout — is Premiere open and the MCP bridge running?"}


def parse_result(resp: dict) -> dict:
    """Extract the inner result dict from bridge response."""
    raw = resp.get("result", resp)
    if isinstance(raw, str):
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {"raw": raw, "error": "could not parse bridge response"}
    return raw


# ---------------------------------------------------------------------------
# Sequence builder
# ---------------------------------------------------------------------------

def run_qa(sequence_name: str, expected_clips: int, expected_dur_sec: float, fps: float) -> dict:
    """Run post-build QA checks via bridge. Returns {pass, reason?, warnings?}."""
    script = _inject_fps(QA_TEMPLATE, fps)
    script = (script
              .replace("QA_SEQ_NAME", json.dumps(sequence_name))
              .replace("QA_EXPECTED_CLIPS", str(expected_clips))
              .replace("QA_EXPECTED_DUR", str(round(expected_dur_sec, 1))))
    resp = send_bridge(script, timeout_sec=30)
    result = parse_result(resp)
    if resp.get("success") is False:
        return {"pass": False, "reason": resp.get("error", "Bridge error during QA")}
    return result


def ticks_for_clips(clips: list[dict], fps: float) -> int:
    """Total ticks for a list of clips, using each clip's frame-snapped length
    (round(out*fps) - round(in*fps)) so the batch cursor never drifts a frame."""
    tpframe = round(TICKS / fps)
    total = 0
    for c in clips:
        total += (_jround(float(c["media_out"]) * fps) - _jround(float(c["media_in"]) * fps)) * tpframe
    return total


def add_transitions(sequence_name: str, audio_frames: int, video_frames: int) -> dict:
    """Add Constant Power audio crossfades + Cross Dissolve video transitions at
    every clip junction via the QE DOM. Returns {ok, aAdded, vAdded, ...} or {error}.
    """
    script = (ADD_TRANSITIONS_TEMPLATE
              .replace("SEQ_NAME_PLACEHOLDER", json.dumps(sequence_name))
              .replace("AUDIO_REQ_PLACEHOLDER", str(int(audio_frames)))
              .replace("VIDEO_REQ_PLACEHOLDER", str(int(video_frames))))
    resp = send_bridge(script, timeout_sec=120)
    return parse_result(resp)


def build_sequence(edit: dict, sequence_name: str, fps: float, dissolve_frames: int, batch_size: int) -> dict:
    source_path = edit["source"]
    clips = build_clip_list(edit)

    if not clips:
        return {"error": "No clips to place — check content_edit.json"}

    print(f"  Clips to place: {len(clips)} "
          f"({sum(1 for c in clips if c['role']=='teaser')} teaser, "
          f"{sum(1 for c in clips if c['role']=='intro')} intro, "
          f"{sum(1 for c in clips if c['role']=='main')} main)")

    if len(clips) <= batch_size:
        payload = {
            "sequenceName": sequence_name,
            "sourcePath": source_path,
            "clips": clips,
            "dissolveFrames": dissolve_frames,
        }
        script = _inject_fps(EXTENDSCRIPT_TEMPLATE, fps).replace("DATA_PLACEHOLDER", json.dumps(payload))
        print(f"  Sending {len(clips)} clips in one bridge call...")
        resp = send_bridge(script, timeout_sec=300)
        return parse_result(resp)

    # Batch mode: first call creates sequence + first N clips, subsequent calls append
    print(f"  Large clip list ({len(clips)}) — batching in groups of {batch_size}...")

    first_payload = {
        "sequenceName": sequence_name,
        "sourcePath": source_path,
        "clips": clips[:batch_size],
        "dissolveFrames": dissolve_frames,
    }
    script = _inject_fps(EXTENDSCRIPT_TEMPLATE, fps).replace("DATA_PLACEHOLDER", json.dumps(first_payload))
    print(f"  Batch 1: clips 0–{batch_size - 1}...")
    result = parse_result(send_bridge(script, timeout_sec=300))
    if result.get("error"):
        return result

    cursor = ticks_for_clips(clips[:batch_size], fps)

    for start in range(batch_size, len(clips), batch_size):
        batch = clips[start:start + batch_size]
        end_idx = min(start + batch_size, len(clips))
        print(f"  Batch {start // batch_size + 1}: clips {start}–{end_idx - 1}...")
        script = (_inject_fps(APPEND_TEMPLATE, fps)
                  .replace("SEQ_NAME_PLACEHOLDER", json.dumps(sequence_name))
                  .replace("SRC_PATH_PLACEHOLDER", json.dumps(source_path))
                  .replace("CLIPS_PLACEHOLDER", json.dumps(batch))
                  .replace("START_CURSOR_PLACEHOLDER", str(cursor)))
        result = parse_result(send_bridge(script, timeout_sec=300))
        if result.get("error"):
            print(f"  WARNING: Batch failed: {result}")
            break
        cursor += ticks_for_clips(batch, fps)

    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Build a content-edited Premiere sequence from content_edit.json"
    )
    parser.add_argument("--edit", required=True, help="Path to content_edit.json")
    parser.add_argument("--sequence-name", default="Podcast Edit", help="Premiere sequence name")
    parser.add_argument("--project", help="Expected Premiere project name (for verification)")
    parser.add_argument("--dissolve-frames", type=int, default=15,
                        help="(legacy, unused) Cross-dissolve length in frames")
    parser.add_argument("--audio-crossfade-frames", type=int, default=4,
                        help="Constant Power audio crossfade length at each cut (4 frames ≈ 0.17s at 24fps). 0 disables.")
    parser.add_argument("--video-dissolve-frames", type=int, default=0,
                        help="Cross Dissolve video transition length at each cut. Default 0 = OFF "
                             "(hard cuts on video; audio still crossfades). Set >0 to enable.")
    parser.add_argument("--batch-size", type=int, default=80,
                        help="Max clips per bridge call (default 80)")
    parser.add_argument("--fps", type=float, default=0.0,
                        help="Override source frame rate. Default 0 = auto-detect via ffprobe.")
    args = parser.parse_args()

    with open(args.edit) as f:
        edit = json.load(f)

    source = edit.get("source", "")
    duration = edit.get("duration_sec", 0)
    fps = args.fps if args.fps > 0 else detect_fps(source)
    print(f"Source: {Path(source).name}")
    print(f"Original duration: {duration:.1f}s ({duration/60:.1f} min)")
    print(f"Frame rate: {fps:g} fps  (timeline tick grid = {round(TICKS/fps)} ticks/frame)")
    print(f"Sequence name: '{args.sequence_name}'")
    print()
    print("  ⚠ The source file must be imported into the Premiere project bin before running.")
    print()

    if args.project:
        info = verify_project(args.project)
        if not info.get("correct"):
            print(f"  WARNING: Expected project '{args.project}', "
                  f"found '{info.get('project_name')}'. Proceeding anyway.")

    result = build_sequence(edit, args.sequence_name, fps, args.dissolve_frames, args.batch_size)

    if result.get("error"):
        print(f"\n✗ BUILD FAILED: {result['error']}")
        sys.exit(1)

    build_errs = result.get("errs", [])
    if build_errs:
        print(f"\n  Build warnings ({len(build_errs)}):")
        for e in build_errs:
            print(f"    - {e}")

    # Add transitions (audio crossfades + optional video dissolves) at every junction
    if args.audio_crossfade_frames > 0 or args.video_dissolve_frames > 0:
        print("\nAdding transitions at clip junctions...")
        tr = add_transitions(args.sequence_name,
                             args.audio_crossfade_frames,
                             args.video_dissolve_frames)
        if tr.get("error"):
            print(f"  ⚠ Transitions not added: {tr['error']}")
            print(f"    (Sequence still built; cuts are hard cuts in silence.)")
        else:
            print(f"  ✓ Audio crossfades: {tr.get('aAdded', 0)} added "
                  f"({tr.get('audioTransitions', 0)} on A1)")
            if args.video_dissolve_frames > 0:
                print(f"  ✓ Video dissolves:  {tr.get('vAdded', 0)} added "
                      f"({tr.get('videoTransitions', 0)} on V1)")
            for e in tr.get("errs", []):
                print(f"    - {e}")

    # QA gate — runs before declaring success
    clips = build_clip_list(edit)
    expected_dur = sum(c["media_out"] - c["media_in"] for c in clips)
    print("\nRunning QA checks...")
    qa = run_qa(args.sequence_name, len(clips), expected_dur, fps)

    if not qa.get("pass"):
        print(f"✗ QA FAILED: {qa.get('reason', 'unknown')}")
        print(f"  The sequence was built but has issues. Check Premiere and re-run.")
        sys.exit(1)

    print(f"✓ QA PASSED")
    for w in qa.get("warnings", []):
        print(f"  ⚠ {w}")

    dur_sec = qa.get("durSec", result.get("dur_sec", 0))
    print(f"\n✓ Sequence built: '{args.sequence_name}'")
    print(f"  Duration:  {dur_sec:.1f}s ({dur_sec/60:.1f} min)  ←  trimmed from {duration/60:.1f} min")
    print(f"  V1 clips:  {qa.get('v1Clips', result.get('v1Clips'))}")
    print(f"  A1 clips:  {qa.get('a1Clips', result.get('a1Clips'))}")
    if "audioTransitions" in qa:
        print(f"  Crossfades: {qa.get('audioTransitions', 0)} audio / "
              f"{qa.get('videoTransitions', 0)} video  (at {qa.get('junctions', 0)} junctions)")

    teasers = [c for c in clips if c["role"] == "teaser"]
    intro   = [c for c in clips if c["role"] == "intro"]
    teaser_dur = sum(c["media_out"] - c["media_in"] for c in teasers)
    intro_dur  = sum(c["media_out"] - c["media_in"] for c in intro)

    print(f"""
Sequence structure:
  [00:00 – {teaser_dur/60:.1f}min] Teaser cold open ({len(teasers)} clips)
  [{teaser_dur/60:.1f}min – {(teaser_dur+intro_dur)/60:.1f}min] Show intro
  [{(teaser_dur+intro_dur)/60:.1f}min – end] Main content

Next steps in Premiere:
  1. Open sequence '{args.sequence_name}'
  2. Check Audio Clip Mixer — A1 fader should be at 0 dB
  3. Scrub edit points — audio crossfades applied; video is hard cuts (no dissolves)
  4. Add music, color, and export
""")


if __name__ == "__main__":
    main()
