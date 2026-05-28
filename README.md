# claudedit

AI-assisted video editing tools for Adobe Premiere Pro. Built around a file-based JSON bridge that lets Python scripts (and Claude) drive Premiere programmatically.

---

## What's in here

### `premiere-pro-mcp/`
The bridge layer between the outside world and Premiere Pro. Forked from [`leancoderkavy/premiere-pro-mcp`](https://github.com/leancoderkavy/premiere-pro-mcp), which itself is a community fork of [`ppmcp/premiere-pro-mcp`](https://github.com/ppmcp/premiere-pro-mcp).

The bridge works by polling a directory (`/tmp/premiere-mcp-bridge/`). A Python script drops a `command-{id}.json` file, the Premiere CEP extension picks it up and evaluates the embedded ExtendScript, and writes back a `response-{id}.json`. No WebSockets, no server — just filesystem polling.

### `podcast-pipeline/`
Three-stage pipeline for multi-cam podcast editing:

| Script | What it does |
|--------|-------------|
| `podcast_ingest.py` | Scans a directory of recordings, auto-classifies each file (reference/mixed, host cam, guest cam, b-roll) using audio speech-density analysis and filename hints. Computes sync offsets between all sources via audio cross-correlation — no shared start point required. |
| `podcast_edit.py` | Reads the ingest manifest, detects speech windows per camera using `ffmpeg silencedetect`, applies editorial rules (min cut length, max continuous run, b-roll pacing), and outputs an edit spec. |
| `build_podcast_sequence.py` | Reads the edit spec and builds the full multi-track Premiere sequence via the bridge. Handles batching for large sequences. |

**Output track layout:**
```
V2 ── B-roll clips (auto-inserted over talking heads at topic-matched moments)
V1 ── Main edit: host cam / guest cam / split-screen, switching per speaker activity
A1 ── Host cam isolated audio — full duration, no cuts, continuous
A2 ── Guest cam isolated audio — full duration, sync-offset applied
```

---

## What we can do

- **Auto-classify recordings** — no manual labeling. Speech density analysis identifies the reference (both speakers mixed), host solo, guest solo, and b-roll by audio content alone.
- **Sync multi-cam** — cross-correlation of audio waveforms handles cameras that started at different times.
- **Generate edit decisions** — speaker-switch logic using isolated audio tracks as the signal (no diarization model needed).
- **Drive Premiere fully from Python** — create sequences, import files, place clips on specific tracks at specific timecodes, set in/out points, clear tracks, clone sequences, rename sequences, probe clip counts and durations.
- **Batch bridge calls** — large sequences (30+ clips) get chunked to avoid ExtendScript timeout limits.
- **Frame-snap all timecodes** — every in/out point is rounded to the nearest frame boundary before converting to ticks, eliminating 1-frame gap artifacts.

---

## What we shouldn't do

**Bridge patterns that break:**

| Don't | Do instead | Why |
|-------|-----------|-----|
| `seq.clone()` | `createNewSequenceFromClips` | Clone is unreliable; the sequence ends up detached and rename fails |
| `clip.inPoint = x` | `overwriteClip(item, posT)` | `inPoint` on a timeline clip sets the *media* trim point, not the timeline position |
| Set `seq.end` | Don't — it's read-only | Will silently fail |
| Run concurrent bridge commands | Queue sequentially | The Premiere extension is single-threaded; concurrent writes corrupt responses |
| Send very large ExtendScript in one call | Batch into chunks | ExtendScript has a string-size limit; large batches time out |

**Audio transitions:**
The Premiere ExtendScript API for audio transitions (`setTransition`, `addTransitionAt`) does not work reliably through the bridge. We've probed QE/DOM and executeCommand approaches — none are confirmed working. Audio fade-ins/fade-outs via keyframes work fine as a workaround.

**Don't delete renders before Premiere is done with them:**
Premiere caches media file paths at import time. If a file moves or is deleted after being placed on a timeline, the sequence goes offline. Renders must live at stable paths for the lifetime of the project.

---

## Current struggles

### 1. Renders deleted, Premiere went offline
The 90 ProRes MOV renders (5 clips × 3 aesthetics × ~6 beats each) were deleted from disk after being placed in Premiere, causing all V2 media to go offline. The composition HTML files were intact so we're re-rendering now (~2 renders/minute with 4 parallel workers due to system memory pressure from 20 simultaneous Chrome instances).

**Root cause:** No persistent render output location — renders landed in a path that got cleared. Fix: commit to a stable render directory outside `/tmp/`.

### 2. Render throughput under memory pressure
`npx hyperframes render` spawns 5 Chrome workers per call. With 4 parallel renders (our `ProcessPoolExecutor max_workers=4`), that's 20 Chrome instances simultaneously on a 36 GB machine. Memory fills up, swap kicks in, and render time degrades from ~17s/beat to ~3 min/beat.

**Fix to try:** Drop to `max_workers=2` when re-rendering from scratch, or set `--workers 2` in the hyperframes call to reduce per-render Chrome instances.

### 3. Audio transitions not yet working
Tasks to add `add_audio_transition` and `batch_add_audio_transitions` as bridge MCP tools are still pending. The research phase showed the DOM/QE approach is the most promising path but hasn't been confirmed.

### 4. No stable render pipeline guard
The manifest (`render_manifest_final.json`) checks `file_exists` at generation time and caches the result. Stale `true` values after a delete look like success. Need a pre-flight check in `premiere_build_final.py` that verifies every file before sending a single bridge command.

---

## Setup

### Premiere bridge

1. Install the CEP extension from `premiere-pro-mcp/cep-plugin/` into Premiere Pro.
2. Enable unsigned CEP extensions: `defaults write com.adobe.CSXS.11 PlayerDebugMode 1`
3. Restart Premiere.
4. The extension polls `/tmp/premiere-mcp-bridge/` for `command-*.json` files.

### Podcast pipeline

```bash
# Step 1: ingest + sync
python3.11 podcast-pipeline/podcast_ingest.py /path/to/episode/ \
  --output /tmp/ingest.json

# Step 2: edit decisions
python3.11 podcast-pipeline/podcast_edit.py \
  --ingest /tmp/ingest.json \
  --sequence-name "ep12-edit" \
  --output /tmp/edit_spec.json

# Step 3: build in Premiere (bridge must be running)
python3.11 podcast-pipeline/build_podcast_sequence.py \
  --spec /tmp/edit_spec.json
```

---

## Related repos

- [`fullvaluedan/premiere-pro-mcp`](https://github.com/fullvaluedan/premiere-pro-mcp) — our fork of the bridge (upstream: `leancoderkavy/premiere-pro-mcp`)
