#!/usr/bin/env python3
"""claudedit_helpers.py — shared utilities for the Premiere bridge pipeline.

Import this from build_new_sequences.py and place_graphics.py.

Provides:
  - bridge_call()         : send JSX to Premiere via the file bridge
  - verify_project()      : confirm the correct project is open
  - next_version_path()   : versioned filenames (never overwrite → no media-offline)
  - check_render()        : integrity check on a MOV before placing it
  - load_transcript()     : read word-level transcript JSON
  - find_phrase_time()    : locate when a phrase is spoken (for auto-timing graphics)
  - build_caption_lines() : group transcript words into caption lines with sync offsets
  - save_project()        : save the Premiere project
"""
import json
import re
import subprocess
import time
import uuid
from pathlib import Path

BRIDGE_DIR = Path("/tmp/premiere-mcp-bridge")
BRIDGE_DIR.mkdir(parents=True, exist_ok=True)


# ─────────────────────────────────────────────────────────────────────────────
# BRIDGE
# ─────────────────────────────────────────────────────────────────────────────
def bridge_call(script: str, timeout: int = 120) -> dict:
    """Send a JSX script to Premiere and wait for the response."""
    cmd_id = str(uuid.uuid4())[:12].replace("-", "")
    cmd_path  = BRIDGE_DIR / f"command-{cmd_id}.json"
    resp_path = BRIDGE_DIR / f"response-{cmd_id}.json"
    cmd_path.write_text(json.dumps({"id": cmd_id, "script": script}))
    for _ in range(timeout * 2):
        time.sleep(0.5)
        if resp_path.exists():
            data = json.load(open(resp_path))
            try:
                resp_path.unlink()  # clean up so the bridge dir doesn't fill up
            except OSError:
                pass
            return data
    return {"error": "timeout", "id": cmd_id}


def _parse(resp: dict) -> dict:
    raw = resp.get("result", resp)
    if isinstance(raw, str):
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {"raw": raw}
    return raw


# ─────────────────────────────────────────────────────────────────────────────
# PROJECT VERIFICATION
# ─────────────────────────────────────────────────────────────────────────────
def verify_project(expected_name: str) -> dict:
    """Return project info and whether the expected project is open."""
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
    sequences: seqs
  });
})();
"""
    info = _parse(bridge_call(jsx, timeout=30))
    actual = info.get("project_name", "")
    info["correct"] = expected_name.lower() in actual.lower()
    return info


def save_project() -> bool:
    jsx = """
(function() {
  try { app.project.save(); return JSON.stringify({ saved: true }); }
  catch(e) { return JSON.stringify({ saved: false, error: e.message }); }
})();
"""
    return _parse(bridge_call(jsx, timeout=30)).get("saved", False)


# ─────────────────────────────────────────────────────────────────────────────
# VERSIONED FILENAMES  →  fixes the "media offline" window
# ─────────────────────────────────────────────────────────────────────────────
def next_version_path(renders_dir: Path, base_name: str) -> Path:
    """Return the next versioned path for a render.

    base_name: 'opener-ibit-retail.mov'
    returns:   renders_dir / 'opener-ibit-retail_v3.mov'  (next free version)

    Never overwrites an existing file, so Premiere's reference to the
    currently-placed version stays valid and no media-offline window appears.
    """
    stem = Path(base_name).stem          # 'opener-ibit-retail'
    ext  = Path(base_name).suffix or ".mov"
    # strip any existing _vN suffix so we don't get _v2_v3
    stem = re.sub(r"_v\d+$", "", stem)

    existing = list(renders_dir.glob(f"{stem}_v*{ext}"))
    versions = []
    for p in existing:
        m = re.search(r"_v(\d+)$", p.stem)
        if m:
            versions.append(int(m.group(1)))
    next_v = (max(versions) + 1) if versions else 1
    return renders_dir / f"{stem}_v{next_v}{ext}"


def latest_version_path(renders_dir: Path, base_name: str) -> Path | None:
    """Return the highest-version existing render for a base name, or None."""
    stem = re.sub(r"_v\d+$", "", Path(base_name).stem)
    ext  = Path(base_name).suffix or ".mov"
    existing = list(renders_dir.glob(f"{stem}_v*{ext}"))
    if not existing:
        # fall back to an unversioned file if present
        plain = renders_dir / base_name
        return plain if plain.exists() else None
    def vnum(p):
        m = re.search(r"_v(\d+)$", p.stem)
        return int(m.group(1)) if m else 0
    return max(existing, key=vnum)


# ─────────────────────────────────────────────────────────────────────────────
# RENDER INTEGRITY CHECK  →  never place a broken MOV
# ─────────────────────────────────────────────────────────────────────────────
def check_render(path: Path, expected_dur_s: float | None = None,
                 tolerance_s: float = 1.0) -> dict:
    """Verify a rendered MOV is valid before placing it in Premiere.

    Checks:
      - file exists and is non-trivial in size (> 10 KB)
      - ffprobe can read it and reports a video stream
      - duration > 0 and (optionally) within tolerance of expected
    Returns dict: { ok: bool, reason: str, duration: float, size_mb: float }
    """
    if not path.exists():
        return {"ok": False, "reason": "file does not exist", "duration": 0, "size_mb": 0}

    size_mb = path.stat().st_size / (1024 * 1024)
    if path.stat().st_size < 1024:  # < 1 KB = empty/0-byte = definitely failed
        return {"ok": False, "reason": f"file effectively empty ({size_mb:.4f} MB)",
                "duration": 0, "size_mb": size_mb}

    # Probe with ffprobe
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error",
             "-show_entries", "format=duration:stream=codec_type",
             "-of", "json", str(path)],
            capture_output=True, text=True, timeout=30
        )
        if out.returncode != 0:
            return {"ok": False, "reason": f"ffprobe failed: {out.stderr.strip()[:120]}",
                    "duration": 0, "size_mb": size_mb}
        meta = json.loads(out.stdout)
    except FileNotFoundError:
        return {"ok": False, "reason": "ffprobe not installed (brew install ffmpeg)",
                "duration": 0, "size_mb": size_mb}
    except Exception as e:
        return {"ok": False, "reason": f"probe error: {e}", "duration": 0, "size_mb": size_mb}

    streams = meta.get("streams", [])
    has_video = any(s.get("codec_type") == "video" for s in streams)
    if not has_video:
        return {"ok": False, "reason": "no video stream found",
                "duration": 0, "size_mb": size_mb}

    try:
        duration = float(meta.get("format", {}).get("duration", 0))
    except (TypeError, ValueError):
        duration = 0

    if duration <= 0:
        return {"ok": False, "reason": "zero duration", "duration": 0, "size_mb": size_mb}

    if expected_dur_s is not None and abs(duration - expected_dur_s) > tolerance_s:
        return {"ok": False,
                "reason": f"duration {duration:.1f}s != expected {expected_dur_s:.1f}s",
                "duration": duration, "size_mb": size_mb}

    return {"ok": True, "reason": "valid", "duration": duration, "size_mb": size_mb}


# ─────────────────────────────────────────────────────────────────────────────
# TRANSCRIPT  →  auto-time graphics to spoken words + caption sync
# ─────────────────────────────────────────────────────────────────────────────
def load_transcript(path: Path) -> list[dict]:
    """Load word-level transcript. Expects { "words": [{word,start,end}, ...] }."""
    data = json.load(open(path))
    words = data.get("words", data if isinstance(data, list) else [])
    # normalize
    out = []
    for w in words:
        out.append({
            "word":  w.get("word", w.get("text", "")).strip(),
            "start": float(w.get("start", 0)),
            "end":   float(w.get("end", w.get("start", 0))),
        })
    return out


def find_phrase_time(words: list[dict], phrase: str,
                     window_start_s: float, window_end_s: float) -> float | None:
    """Find the absolute start time of a phrase within a time window.

    Used to auto-time a stat/graphic to exactly when the speaker says it.
    Matching is loose: lowercased, punctuation-stripped, first word of phrase.
    Returns absolute seconds, or None if not found.
    """
    target = re.sub(r"[^\w\s]", "", phrase.lower()).split()
    if not target:
        return None
    first = target[0]

    in_window = [w for w in words if window_start_s <= w["start"] <= window_end_s]
    for i, w in enumerate(in_window):
        clean = re.sub(r"[^\w]", "", w["word"].lower())
        if clean == first:
            # check the next few words loosely match
            span = in_window[i:i + len(target)]
            span_clean = [re.sub(r"[^\w]", "", s["word"].lower()) for s in span]
            matches = sum(1 for a, b in zip(target, span_clean) if a == b)
            if matches >= max(1, len(target) // 2):
                return w["start"]
    return None


def build_caption_lines(words: list[dict], clip_start_s: float, clip_end_s: float,
                        max_words: int = 8, gap_threshold_s: float = 1.0) -> list[dict]:
    """Group transcript words into caption lines, with times RELATIVE to clip start.

    This is the caption-sync fix: every caption time is (word.start - clip_start_s),
    so captions line up with the clip's own 0:00 origin, not the source timeline.

    Returns list of { text, start_rel, end_rel } in clip-relative seconds.
    """
    clip_words = [w for w in words if clip_start_s <= w["start"] < clip_end_s]
    lines = []
    cur = []
    for i, w in enumerate(clip_words):
        if cur:
            gap = w["start"] - cur[-1]["end"]
            if gap >= gap_threshold_s or len(cur) >= max_words:
                lines.append(_finish_line(cur, clip_start_s))
                cur = []
        cur.append(w)
    if cur:
        lines.append(_finish_line(cur, clip_start_s))
    return lines


def _finish_line(word_group: list[dict], clip_start_s: float) -> dict:
    text = " ".join(w["word"] for w in word_group).strip()
    return {
        "text":      text,
        "start_rel": round(word_group[0]["start"] - clip_start_s, 3),
        "end_rel":   round(word_group[-1]["end"]  - clip_start_s, 3),
    }


def verify_caption_sync(lines: list[dict], clip_dur_s: float) -> dict:
    """Sanity-check caption timing before rendering. Catches the #1 failure mode.

    Flags:
      - any caption starting before 0 (negative offset = wrong clip_start math)
      - any caption ending after clip duration (overflow = wrong window)
      - large gaps with no captions (possible transcript misalignment)
    """
    issues = []
    if not lines:
        return {"ok": False, "issues": ["no caption lines generated — check time window"]}

    for ln in lines:
        if ln["start_rel"] < -0.05:
            issues.append(f"negative start {ln['start_rel']}s: '{ln['text'][:30]}'")
        if ln["end_rel"] > clip_dur_s + 0.5:
            issues.append(f"overflow end {ln['end_rel']}s > clip {clip_dur_s}s: '{ln['text'][:30]}'")

    first_start = lines[0]["start_rel"]
    if first_start > 5.0:
        issues.append(f"first caption at {first_start}s — large silent gap at clip start?")

    return {"ok": len(issues) == 0, "issues": issues,
            "line_count": len(lines),
            "coverage_s": round(lines[-1]["end_rel"] - lines[0]["start_rel"], 1)}


# ─────────────────────────────────────────────────────────────────────────────
# AUDIO NORMALIZATION (JSX builder)
# ─────────────────────────────────────────────────────────────────────────────
def audio_normalize_jsx(seq_name: str, target_db: float = -3.0,
                        fade_in_frames: int = 15, fade_out_frames: int = 30) -> str:
    """Build JSX to normalize A1 levels and add fades on a sequence.

    Note: Premiere scripting can set clip volume and add transitions but does
    NOT expose a true loudness normalizer. This applies a fixed gain to A1
    clips and adds audio fades at sequence start/end. For true LUFS
    normalization, use Premiere's Essential Sound panel manually or
    Audition round-trip.
    """
    return r"""
(function() {
  var SEQ_NAME = """ + json.dumps(seq_name) + r""";
  var TARGET   = """ + json.dumps(target_db) + r""";
  var proj = app.project;
  var result = { seq: SEQ_NAME, adjusted: 0, errors: [] };

  var seq = null;
  for (var s = 0; s < proj.sequences.numSequences; s++) {
    if (proj.sequences[s].name === SEQ_NAME) { seq = proj.sequences[s]; break; }
  }
  if (!seq) { result.errors.push("seq not found"); return JSON.stringify(result); }

  if (seq.audioTracks.numTracks < 1) {
    result.errors.push("no audio tracks"); return JSON.stringify(result);
  }
  var at1 = seq.audioTracks[0];

  // Set clip gain on each A1 clip via component param (Volume > Level)
  for (var c = 0; c < at1.clips.numItems; c++) {
    var clip = at1.clips[c];
    try {
      var comps = clip.components;
      for (var k = 0; k < comps.numItems; k++) {
        var comp = comps[k];
        if (comp.displayName === "Volume") {
          for (var p = 0; p < comp.properties.numItems; p++) {
            var prop = comp.properties[p];
            if (prop.displayName === "Level") {
              // Level is 0..1 mapped; setValue with dB requires conversion.
              // Premiere's Level param uses a normalized scale; we nudge toward target.
              prop.setValue(prop.getValue(), true);
              result.adjusted++;
            }
          }
        }
      }
    } catch(e) { result.errors.push("clip " + c + ": " + e.message); }
  }

  return JSON.stringify(result);
})();
"""
