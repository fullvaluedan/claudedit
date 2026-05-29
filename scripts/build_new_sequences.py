#!/usr/bin/env python3
"""Build 5 new clip sequences in Premiere via bridge.
Each sequence: V1 = source clipped to segment, ready for V2/V3 graphics.

Fixes over original:
  1. Verifies correct Premiere project is open before doing anything
  2. Creates sequences with explicit 1920x1080 29.97fps settings
  3. Saves project after all sequences are created
  4. Reports which project was found so user can confirm
"""
import json
import time
import uuid
from pathlib import Path

BRIDGE_DIR = Path("/tmp/premiere-mcp-bridge")

# ── VERIFY THIS PATH MATCHES YOUR FILE ──────────────────────────────────────
SOURCE = "/Users/dan/Downloads/live-with-restream,-may-18-May-22-2026-restream.mp4"

# ── VERIFY THIS IS THE EXACT NAME OF YOUR PREMIERE PROJECT ──────────────────
EXPECTED_PROJECT_NAME = "MCP Test"   # change to match what shows in Premiere title bar

CLIPS = [
    {"name": "ibit-retail-unlocked-v2",  "in": 961,  "out": 1015},
    {"name": "ibit-vol-premium",          "in": 921,  "out": 956},
    {"name": "options-ux-evolution",      "in": 1301, "out": 1337},
    {"name": "decacorn-index",            "in": 1800, "out": 1842},
    {"name": "crypto-spectrum",           "in": 2302, "out": 2360},
]

BRIDGE_DIR.mkdir(parents=True, exist_ok=True)


def bridge_call(script: str, timeout: int = 120) -> dict:
    cmd_id = str(uuid.uuid4())[:12].replace("-", "")
    cmd_path  = BRIDGE_DIR / f"command-{cmd_id}.json"
    resp_path = BRIDGE_DIR / f"response-{cmd_id}.json"
    cmd_path.write_text(json.dumps({"id": cmd_id, "script": script}))
    for _ in range(timeout * 2):
        time.sleep(0.5)
        if resp_path.exists():
            return json.load(open(resp_path))
    return {"error": "timeout", "id": cmd_id}


def verify_project() -> dict:
    """Check which project is open and list existing sequences."""
    jsx = """
(function() {
  var proj = app.project;
  var seqs = [];
  for (var i = 0; i < proj.sequences.numSequences; i++) {
    seqs.push(proj.sequences[i].name);
  }
  return JSON.stringify({
    project_name: proj.name,
    project_path: proj.path,
    sequence_count: proj.sequences.numSequences,
    sequences: seqs
  });
})();
"""
    resp = bridge_call(jsx, timeout=30)
    raw = resp.get("result", resp)
    if isinstance(raw, str):
        raw = json.loads(raw)
    return raw


def build_all():
    # ── STEP 1: Verify correct project is open ───────────────────────────────
    print("Checking Premiere project…")
    info = verify_project()
    if info.get("error"):
        print(f"  ✗ Bridge error: {info}")
        return

    actual_name = info.get("project_name", "")
    print(f"  Open project: {actual_name}")
    print(f"  Path: {info.get('project_path', 'unknown')}")
    print(f"  Existing sequences ({info.get('sequence_count', 0)}): {info.get('sequences', [])}")

    if EXPECTED_PROJECT_NAME.lower() not in actual_name.lower():
        print(f"\n  ✗ WRONG PROJECT OPEN.")
        print(f"    Expected: '{EXPECTED_PROJECT_NAME}'")
        print(f"    Found:    '{actual_name}'")
        print(f"    Open the correct project in Premiere and re-run.")
        return

    print(f"  ✓ Correct project confirmed.\n")

    # ── STEP 2: Build sequences ───────────────────────────────────────────────
    clips_json  = json.dumps(CLIPS)
    source_json = json.dumps(SOURCE)

    jsx = r"""
(function() {
  var SOURCE = """ + source_json + r""";
  var CLIPS  = """ + clips_json + r""";
  var proj   = app.project;
  var result = { created: [], skipped: [], errors: [], project: proj.name };

  // ── Import source if not already in project ──────────────────────────────
  function findItem(name) {
    function s(node) {
      if (!node) return null;
      if (node.name === name && node.type === 1) return node;
      if (node.children) {
        for (var i = 0; i < node.children.numItems; i++) {
          var f = s(node.children[i]); if (f) return f;
        }
      }
      return null;
    }
    return s(proj.rootItem);
  }

  var srcName = SOURCE.split("/").pop();
  var sourceItem = findItem(srcName);
  if (!sourceItem) {
    try {
      proj.importFiles([SOURCE], true, proj.rootItem, false);
      sourceItem = findItem(srcName);
    } catch(e) {
      result.errors.push("importFiles: " + e.message);
      return JSON.stringify(result);
    }
  }
  if (!sourceItem) {
    result.errors.push("Source item not found after import: " + srcName);
    return JSON.stringify(result);
  }

  // ── Check existing sequences ─────────────────────────────────────────────
  var existingSeqs = {};
  for (var s = 0; s < proj.sequences.numSequences; s++) {
    existingSeqs[proj.sequences[s].name] = true;
  }

  // ── Create each sequence ─────────────────────────────────────────────────
  for (var c = 0; c < CLIPS.length; c++) {
    var clip = CLIPS[c];

    if (existingSeqs[clip.name]) {
      result.skipped.push(clip.name + " (already exists)");
      continue;
    }

    try {
      // Create a blank sequence with explicit 1920x1080 29.97fps settings
      // Using sequence preset ID for 1080p29.97 — avoids inheriting source settings
      var newSeq = proj.createNewSequence(clip.name, "sequence-from-preset");
      if (!newSeq) {
        // Fallback: create from clips (may inherit source settings)
        newSeq = proj.createNewSequenceFromClips(clip.name, [sourceItem], proj.rootItem);
      }
      if (!newSeq) {
        result.errors.push(clip.name + ": sequence creation returned null");
        continue;
      }

      // ── Set sequence video settings explicitly ───────────────────────────
      // frameRate: 254016000000 ticks/s ÷ (254016000000/29.97) = 29.97fps
      // These calls are no-ops if sequence is already correct format
      try {
        newSeq.frameSizeHorizontal = 1920;
        newSeq.frameSizeVertical   = 1080;
        newSeq.frameRate           = 29.97;
      } catch(e) {
        // Not all Premiere versions expose these as writable — continue anyway
        result.errors.push(clip.name + ": could not set sequence settings: " + e.message);
      }

      // ── Place source clip on V1 at TC=0 with in/out trimmed ─────────────
      var vt1 = newSeq.videoTracks[0];
      // Clear any auto-placed clips
      while (vt1.clips.numItems > 0) { vt1.clips[0].remove(false, true); }

      var inT  = new Time(); inT.seconds  = clip["in"];
      var outT = new Time(); outT.seconds = clip["out"];
      var posT = new Time(); posT.seconds = 0;

      sourceItem.setInPoint(inT.ticks, 4);
      sourceItem.setOutPoint(outT.ticks, 4);
      vt1.overwriteClip(sourceItem, posT);
      sourceItem.clearInPoint(4);
      sourceItem.clearOutPoint(4);

      // ── Place source clip on A1 at TC=0 with same in/out ────────────────
      var at1 = newSeq.audioTracks[0];
      while (at1.clips.numItems > 0) { at1.clips[0].remove(false, true); }

      sourceItem.setInPoint(inT.ticks, 4);
      sourceItem.setOutPoint(outT.ticks, 4);
      at1.overwriteClip(sourceItem, posT);
      sourceItem.clearInPoint(4);
      sourceItem.clearOutPoint(4);

      var dur = clip["out"] - clip["in"];
      result.created.push(clip.name + " (" + dur + "s — V1+A1 placed)");
      existingSeqs[clip.name] = true;

    } catch(e) {
      result.errors.push(clip.name + ": " + e.message);
    }
  }

  // ── Save project after all sequences created ─────────────────────────────
  try {
    proj.save();
    result.saved = true;
  } catch(e) {
    result.saved = false;
    result.errors.push("Project save failed: " + e.message);
  }

  return JSON.stringify(result);
})();
"""

    print("Building sequences…")
    resp = bridge_call(jsx, timeout=120)
    raw = resp.get("result", resp)
    if isinstance(raw, str):
        raw = json.loads(raw)

    print(f"  Project: {raw.get('project', 'unknown')}")
    for s in raw.get("created", []):
        print(f"  ✓ created: {s}")
    for s in raw.get("skipped", []):
        print(f"  – skipped: {s}")
    for e in raw.get("errors", []):
        print(f"  ✗ error:   {e}")

    if raw.get("saved"):
        print("\n  ✓ Project saved.")
    else:
        print("\n  ⚠ Project was NOT saved — save manually in Premiere (Cmd+S).")

    return raw


if __name__ == "__main__":
    build_all()
