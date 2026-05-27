# Podcast Pipeline

Multi-cam podcast editing pipeline. Point at a directory of raw recordings and get a Premiere-ready sequence with intelligent camera switching, b-roll placement, and isolated audio tracks.

## What It Does

1. **Auto-classifies** source files (reference/mixed, host cam, guest cam, b-roll) using audio speech-density analysis — no manual labeling required
2. **Auto-syncs** sources via audio cross-correlation — handles recordings that don't share a common start point
3. **Generates AI-driven edit decisions** — cuts to active speaker using isolated audio as the speaker-detection signal (no diarization needed)
4. **Builds the sequence in Premiere** — multi-track layout, continuous isolated audio, b-roll inserts

## Directory Format

Drop your recording files into a single directory:

```
/recordings/ep12/
├── mixed.mp4           ← both speakers, full audio (auto-detected as reference)
├── host_cam.mp4        ← solo host, host audio only
├── guest_cam.mp4       ← solo guest, guest audio only
├── broll_charts.mp4    ← b-roll clip (any name, auto-detected by duration)
└── broll_office.mp4
```

File names don't need to match exactly. The classifier uses speech-density analysis to find the reference, and filename hints (`host`, `guest`, `cam1`, `cam2`) to separate the solo cams. If it can't tell, it asks.

## Premiere Track Layout

```
V2 ──  B-roll clips (insert over talking heads at topic-matched moments)
V1 ──  Main edit (host cam / guest cam / reference, switching per speaker)
A1 ──  Host cam full-duration isolated audio  (continuous, no cuts)
A2 ──  Guest cam full-duration isolated audio (continuous, sync-adjusted)
```

The video cuts while the audio runs uninterrupted from each isolated mic — pristine audio quality regardless of which camera angle is on screen.

## Quick Start

```bash
# Step 1: Classify files + compute sync offsets
python3.11 podcast_ingest.py /recordings/ep12/

# Step 2: Generate edit decisions
python3.11 podcast_edit.py \
  --ingest /recordings/ep12/ingest.json \
  --sequence-name "ep12-edit" \
  --output /tmp/ep12_edit_spec.json

# Step 3: Import source files into Premiere (if not already there)
# File > Import > select all files from /recordings/ep12/

# Step 4: Build the sequence in Premiere
python3.11 build_podcast_sequence.py --spec /tmp/ep12_edit_spec.json
```

## With a Transcript (Better B-Roll Matching)

If you have a transcript JSON (from `vibe-clipper/scripts/transcribe.py`), pass it to `podcast_edit.py` for keyword-matched b-roll placement:

```bash
python3.11 /path/to/vibe-clipper/scripts/transcribe.py \
  /recordings/ep12/mixed.mp4 \
  /recordings/ep12/

python3.11 podcast_edit.py \
  --ingest /recordings/ep12/ingest.json \
  --sequence-name "ep12-edit" \
  --transcript /recordings/ep12/transcripts/transcript.json \
  --output /tmp/ep12_edit_spec.json
```

## Manual Sync Override

If cross-correlation sync is unreliable (low confidence warning), override with known offsets:

```bash
# host_cam starts 1.2s later than mixed; guest_cam starts at same time
python3.11 podcast_ingest.py /recordings/ep12/ --host-offset 1.2 --guest-offset 0.0
```

## Script Reference

### `podcast_ingest.py`
```
usage: podcast_ingest.py [-h] [--output OUTPUT] [--host-offset SECS] [--guest-offset SECS] directory

positional: directory    Directory containing podcast video files

options:
  --output              Output path for ingest.json (default: <directory>/ingest.json)
  --host-offset SECS    Override host cam sync offset (skip cross-correlation)
  --guest-offset SECS   Override guest cam sync offset (skip cross-correlation)
```

### `podcast_edit.py`
```
usage: podcast_edit.py [-h] --ingest INGEST [--sequence-name NAME] [--output OUTPUT]
                       [--transcript JSON] [--silence-threshold SECS]
                       [--min-cut SECS] [--max-run SECS]

required:
  --ingest              Path to ingest.json

options:
  --sequence-name       Premiere sequence name (default: podcast-edit)
  --output              Output path for edit_spec.json (default: /tmp/edit_spec.json)
  --transcript          transcript.json for keyword-based b-roll placement
  --silence-threshold   Min silence to detect speaker inactivity (default: 0.5s)
  --min-cut             Min cut duration before merging with neighbor (default: 2.0s)
  --max-run             Max single-angle run before inserting split-screen (default: 90s)
```

### `build_podcast_sequence.py`
```
usage: build_podcast_sequence.py [-h] --spec EDIT_SPEC [--batch-size N]

required:
  --spec                Path to edit_spec.json

options:
  --batch-size          Max cuts per bridge call (default: 80; lower if CEP crashes)
```

## Dependencies

- Python 3.11
- ffmpeg (for silence detection and sync)
- ffprobe (for file metadata)
- numpy (optional, for cross-correlation sync — `pip3.11 install numpy`)
- Groq API key in `~/.zshrc` (for b-roll transcript matching, via transcribe.py)
- Premiere Pro open with bridge CEP panel active (`/tmp/premiere-mcp-bridge/`)

## After Building in Premiere

1. **Scrub the sequence** — camera cuts are AI-generated, some will be wrong
2. **Audio mixer** — open Window > Audio Track Mixer, set levels for A1 (host) and A2 (guest)
3. **Fix bad cuts** — roll edits, swap angles where needed
4. **B-roll** — review V2 inserts, trim or reposition as needed
5. **Export** — the sequence is fully editable, export when done
