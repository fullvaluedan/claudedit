#!/usr/bin/env python3
"""position_speaker.py — fit the speaker into the Swiss Grid transparent window.

Sets the V1 speaker clip's Motion (Scale, Position) and a Crop effect so the
speaker lands precisely inside the window region of the grid overlay on V2.

Uses JSX through the bridge (not MCP) because:
  - the bridge is already working and tested in your pipeline
  - clip Motion + Crop parameters set most reliably with direct ExtendScript
  - MCP may not expose Crop-effect parameters needed for the two-person split

Window geometry MUST match SWISS-GRID-WINDOW.md (x:1000 y:140 w:824 h:800).
If you change the window in the HTML, change WINDOW here too.

You can still nudge everything live in Premiere afterward — these are starting
values calculated to land the speaker in the window.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import claudedit_helpers as h
import json

# ── CONFIG ───────────────────────────────────────────────────────────────────
EXPECTED_PROJECT_NAME = "MCP Test"
FRAME_W, FRAME_H = 1920, 1080

# Window region — MUST match the clip-path notch in SWISS-GRID-WINDOW.md
WINDOW = {"x": 1000, "y": 140, "w": 824, "h": 800}

# The one test clip
SEQUENCE = "bviv-us-43-vs-40-v1"
SPEAKER_SIDE = "right"   # which half of a two-person source the speaker is on:
                         # "right", "left", or "full" (single-speaker source)


def compute_transform(speaker_side: str) -> dict:
    """Return Premiere Motion + Crop values to fit the speaker into the window.

    Position math: Premiere places the clip such that its anchor point (default =
    clip center at FRAME_W/2, FRAME_H/2) lands at position_x/y in the composition.
    For a cropped half-frame speaker we need to shift position so the speaker's
    half of the clip — not the clip center — aligns with the window.

        position_x = win_cx - (speaker_center_in_clip - clip_center) * scale/100
    """
    win_cx = WINDOW["x"] + WINDOW["w"] / 2   # window center x = 1412
    win_cy = WINDOW["y"] + WINDOW["h"] / 2   # window center y = 540

    if speaker_side == "full":
        src_w, src_h = FRAME_W, FRAME_H
        pre_crop_lr = 0.0
        speaker_center_x = FRAME_W / 2       # clip center = speaker center, no offset
    elif speaker_side == "right":
        src_w, src_h = FRAME_W / 2, FRAME_H
        pre_crop_lr = 50.0                    # crop away left half (Nic)
        speaker_center_x = FRAME_W * 3 / 4   # 1440 = center of right half
    else:  # left
        src_w, src_h = FRAME_W / 2, FRAME_H
        pre_crop_lr = 50.0                    # crop away right half
        speaker_center_x = FRAME_W / 4       # 480 = center of left half

    # Scale to COVER the window (fill fully, keep aspect)
    scale = max(WINDOW["h"] / src_h, WINDOW["w"] / src_w) * 100

    # Correct position: move clip so speaker's content center lands at window center
    clip_center_x = FRAME_W / 2              # 960
    position_x = win_cx - (speaker_center_x - clip_center_x) * (scale / 100)
    position_y = win_cy  # speaker y-center = clip y-center for side-by-side layouts

    # After scaling, crop the overflow so visible area == window
    scaled_w = src_w * scale / 100
    scaled_h = src_h * scale / 100
    crop_lr = max(0, (scaled_w - WINDOW["w"]) / 2) / scaled_w * 100
    crop_tb = max(0, (scaled_h - WINDOW["h"]) / 2) / scaled_h * 100

    return {
        "scale": round(scale, 1),
        "position_x": round(position_x, 1),
        "position_y": round(position_y, 1),
        "crop_left":  round(pre_crop_lr + crop_lr, 1) if speaker_side == "right" else round(crop_lr, 1),
        "crop_right": round(pre_crop_lr + crop_lr, 1) if speaker_side == "left"  else round(crop_lr, 1),
        "crop_top":    round(crop_tb, 1),
        "crop_bottom": round(crop_tb, 1),
        "speaker_side": speaker_side,
    }


def apply_jsx(seq_name: str, t: dict) -> str:
    return r"""
(function() {
  var SEQ = """ + json.dumps(seq_name) + r""";
  var T   = """ + json.dumps(t) + r""";
  var proj = app.project;
  var result = { seq: SEQ, applied: false, errors: [] };

  var seq = null;
  for (var s=0;s<proj.sequences.numSequences;s++)
    if (proj.sequences[s].name === SEQ) { seq = proj.sequences[s]; break; }
  if (!seq) { result.errors.push("seq not found"); return JSON.stringify(result); }

  // V1 first clip = speaker
  var vt1 = seq.videoTracks[0];
  if (vt1.clips.numItems === 0) { result.errors.push("no V1 clip"); return JSON.stringify(result); }
  var clip = vt1.clips[0];

  // ── Motion: Scale + Position ──────────────────────────────────────────────
  function setMotion(clip, scaleVal, posX, posY) {
    var comps = clip.components;
    for (var i=0;i<comps.numItems;i++) {
      var c = comps[i];
      if (c.displayName === "Motion" || c.matchName === "AE.ADBE Motion") {
        for (var p=0;p<c.properties.numItems;p++) {
          var prop = c.properties[p];
          if (prop.displayName === "Scale") {
            prop.setValue(scaleVal, true);
          }
          if (prop.displayName === "Position") {
            // Position expects normalized [x/frameW, y/frameH]
            prop.setValue([posX/""" + str(FRAME_W) + r""", posY/""" + str(FRAME_H) + r"""], true);
          }
        }
        return true;
      }
    }
    return false;
  }

  // ── Crop effect (add if missing, then set params) ──────────────────────────
  function setCrop(clip, l, r, tp, b) {
    var comps = clip.components;
    var crop = null;
    for (var i=0;i<comps.numItems;i++) {
      if (comps[i].displayName === "Crop" || comps[i].matchName === "AE.ADBE Crop") { crop = comps[i]; break; }
    }
    if (!crop) {
      // Try to add the Crop effect via QE DOM
      try {
        app.enableQE();
        var qeSeq = qe.project.getActiveSequence();
        var qeTrack = qeSeq.getVideoTrackAt(0);
        var qeClip = qeTrack.getItemAt(0);
        qeClip.addVideoEffect(qe.project.getVideoEffectByName("Crop"));
        // re-find
        for (var j=0;j<clip.components.numItems;j++)
          if (clip.components[j].displayName === "Crop") { crop = clip.components[j]; break; }
      } catch(e) { result.errors.push("addCrop: " + e.message); }
    }
    if (!crop) return false;
    for (var p=0;p<crop.properties.numItems;p++) {
      var prop = crop.properties[p];
      if (prop.displayName === "Left")   prop.setValue(l, true);
      if (prop.displayName === "Right")  prop.setValue(r, true);
      if (prop.displayName === "Top")    prop.setValue(tp, true);
      if (prop.displayName === "Bottom") prop.setValue(b, true);
    }
    return true;
  }

  try {
    var m = setMotion(clip, T.scale, T.position_x, T.position_y);
    if (!m) result.errors.push("Motion component not found");
    var cr = setCrop(clip, T.crop_left, T.crop_right, T.crop_top, T.crop_bottom);
    if (!cr) result.errors.push("Crop effect could not be set");
    result.applied = m;
    proj.save();
  } catch(e) { result.errors.push(e.message); }

  return JSON.stringify(result);
})();
"""


def main():
    print("Checking project…")
    info = h.verify_project(EXPECTED_PROJECT_NAME)
    if not info.get("correct"):
        print(f"  ✗ Wrong/closed project: {info.get('project_name')}"); return
    print(f"  ✓ {info.get('project_name')}\n")

    t = compute_transform(SPEAKER_SIDE)
    print(f"Computed transform for '{SPEAKER_SIDE}' speaker → window "
          f"{WINDOW['w']}×{WINDOW['h']} @ ({WINDOW['x']},{WINDOW['y']}):")
    print(f"  Scale:    {t['scale']}%")
    print(f"  Position: ({t['position_x']}, {t['position_y']})  [clip center]")
    print(f"  Crop:     L {t['crop_left']}%  R {t['crop_right']}%  "
          f"T {t['crop_top']}%  B {t['crop_bottom']}%\n")

    print("Applying to V1 speaker clip via JSX bridge…")
    resp = h._parse(h.bridge_call(apply_jsx(SEQUENCE, t), timeout=60))
    if resp.get("applied"):
        print("  ✓ Motion + Crop applied, project saved.")
    else:
        print("  ⚠ Not fully applied.")
    for e in resp.get("errors", []):
        print(f"    - {e}")
    print("\nScrub the sequence — speaker should sit inside the window.")
    print("Nudge Scale/Position live in Premiere if it needs fine-tuning.")


if __name__ == "__main__":
    main()
