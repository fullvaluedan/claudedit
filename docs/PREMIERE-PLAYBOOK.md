# PREMIERE-PLAYBOOK.md — Premiere MCP Command Sequences
# claudedit / [Your Channel Name]
# Version: 1.0
#
# Copy-paste MCP command sequences for every repeatable Premiere task.
# The agent uses these verbatim rather than improvising tool calls.
# Content style: Finance / crypto / data-heavy analysis
# Color grade: Subtle — fix exposure and levels, keep natural

---

## SEQUENCE 1 — PROJECT SETUP

Run this at the start of every new project. Never create a sequence manually.

```
1. Create new sequence:
   "Create a new sequence named [PROJECT-NAME]-MASTER
    Settings: 1920x1080, 29.97fps, stereo 48kHz, square pixels
    Video tracks: V1 (A-roll), V2 (overlays), V3 (full-bleed graphics), V4 (text/captions)
    Audio tracks: A1 (speaker primary), A2 (speaker secondary or guest), A3 (music/sfx)"

2. Create project bins:
   "Create bins: FOOTAGE, AUDIO, GRAPHICS, EXPORTS, SELECTS"

3. Import footage:
   "Import all files from [SOURCE FOLDER] into the FOOTAGE bin"

4. Set scratch disk:
   "Set scratch disk path to [PROJECT FOLDER]/scratch"
```

---

## SEQUENCE 2 — SPEAKER DETECTION & TRACK SETUP

Before cutting, identify what's on screen so graphics compose correctly.

```
1. Place main A-roll on V1/A1:
   "Place [MAIN-FOOTAGE-FILE] on V1 starting at 00:00:00"

2. Get sequence info to confirm:
   "Get full sequence info for [SEQUENCE-NAME]"

3. Add source note to sequence marker at 00:00:00:
   "Add marker at 00:00:00 with comment:
    SPEAKER_LAYOUT=[single-center|single-offset-left|single-offset-right|two-person]
    SPEAKER_NAME=[NAME]
    GUEST_NAME=[NAME or none]"
```

The SPEAKER_LAYOUT marker is read by the graphics pipeline to compose
overlays correctly. Always set it before generating any graphics.

---

## SEQUENCE 3 — ROUGH CUT (SILENCE REMOVAL)

Uses transcript gap analysis. Run after transcript is available.

```
Step 1 — Set in/out on full clip:
"Set in point to 00:00:00 and out point to end of clip on V1"

Step 2 — For each silence gap identified in transcript
(gap = no speech for >1.5 seconds):
"Ripple delete from [GAP_START_TC] to [GAP_END_TC] on all tracks"

Step 3 — After all gaps removed, add micro-dissolves:
"Add 3-frame cross-dissolve transition at every cut point on V1"

Step 4 — Verify sequence length:
"Get active sequence info — confirm duration is approximately [EXPECTED_DURATION]"
```

**How to identify silence gaps from transcript:**
Look for lines with no speech between timestamps greater than 1.5 seconds apart.
Example: if [00:01:23] ends speech and [00:01:27] begins speech → gap is 00:01:23–00:01:27 → ripple delete that range.

---

## SEQUENCE 4 — REPEATED PHRASE REMOVAL

Uses transcript diff. Run after silence removal.

```
Method: Compare transcript lines. Flag any phrase that appears 
more than once within a 60-second window.

For each duplicate:
1. Identify the weaker take (more hesitation, less confident delivery)
2. Note its timecode range
3. "Ripple delete from [TC_START] to [TC_END] on all tracks"
4. "Add 3-frame cross-dissolve at cut point"

Keep the cleaner, more confident take. When in doubt, keep the second 
attempt — speakers usually improve on retry.
```

---

## SEQUENCE 5 — AUDIO NORMALIZATION

Run after rough cut is locked.

```
1. Normalize A1 (primary speaker):
   "Set audio level on A1 to -3dB
    Apply Hard Limiter effect to A1 with maximum amplitude -1dB
    Apply Parametric Equalizer to A1:
      - High-pass filter at 80Hz (remove low rumble)
      - Slight boost at 3kHz +1.5dB (presence/clarity)
      - Cut at 200Hz -1dB (muddiness)"

2. Check peaks:
   "Get full clip info for A1 — confirm audio peaks do not exceed -6dB"

3. If guest/second speaker on A2:
   "Match A2 levels to A1 — set A2 to same normalization"

4. Add fade:
   "Add 15-frame audio fade in at sequence start on A1
    Add 30-frame audio fade out at sequence end on A1"
```

---

## SEQUENCE 6 — COLOR GRADE (SUBTLE — NATURAL)

Finance/crypto content. Keep it real — don't stylize. Fix problems only.

```
Apply to every clip on V1:

"Apply Lumetri Color to [CLIP]:
  Basic Correction:
    Exposure: +0.2 (lift slightly — webcam/camera footage tends to run dark)
    Contrast: +8 (add gentle structure without crushing blacks)
    Highlights: -15 (recover any blown highlights)
    Shadows: +10 (open up face shadows slightly)
    Whites: +5
    Blacks: -5
    Saturation: 95 (very slight desaturation — keeps skin tones neutral)

  Color Wheels:
    Midtones: nudge slightly warm (+3 toward amber — counteracts cool webcam color science)

  HSL Secondary: none — do not touch hue/sat curves unless skin tone is clearly wrong

  NO: Curves, Vignette, Grain, LUT — these are all forbidden for this grade style"
```

**When NOT to grade:**
- Footage is already well-lit and balanced → skip, just apply -15 highlights
- Footage is severely underexposed (>2 stops) → flag for human review, do not auto-grade
- Footage is mixed lighting (outdoor + indoor) → grade each clip individually, not as a batch

---

## SEQUENCE 7 — B-ROLL PLACEMENT

For footage where you have cutaway clips (screen recordings, product demos, environment shots).

```
Track assignment:
  V1 = A-roll (speaker, always)
  V2 = B-roll cutaways (cover speaker with relevant footage)
  V3 = motion graphics overlays
  V4 = captions

Placement rules:
1. "Place [B-ROLL-CLIP] on V2 at [TC_START], duration [DURATION]"
2. "Set V2 clip opacity to 100%" (B-roll fully covers speaker)
3. "Add 8-frame cross-dissolve at V2 in point"
4. "Add 8-frame cross-dissolve at V2 out point"
5. Keep A1 audio from V1 — speaker audio continues under B-roll
6. Never place B-roll over speaker's most important sentence

B-roll timing guide:
  - Minimum B-roll duration: 3 seconds (shorter looks like a glitch)
  - Maximum B-roll duration: 15 seconds (viewer forgets the speaker exists)
  - Sweet spot: 5–10 seconds
```

---

## SEQUENCE 8 — MULTI-SPEAKER / TWO-PERSON SETUP

For interview, co-host, or guest footage.

```
If two speakers are on the same clip (single-camera interview):
  V1/A1 = full clip as-is
  → Graphics compose in right 40% or left 40% (away from active speaker)
  → See FRAME-COMPOSITION.md for speaker-aware graphic zones

If two speakers are on separate clips (two-camera setup):
  V1/A1 = Speaker A (host/primary)
  V2/A2 = Speaker B (guest/secondary), opacity 0 by default
  
  For each speaker turn:
  "Set V1 opacity to [100/0]% at [TC]
   Set V2 opacity to [0/100]% at [TC]"
  Use 3-frame dissolve between speaker switches.

Audio sync (if separate audio tracks):
  "Sync A2 to A1 using audio waveform matching"
```

---

## SEQUENCE 9 — VIDEO FADES

```
Opening fade in:
"Add 24-frame video fade-in (Film Dissolve) at sequence start on V1"

Closing fade to black:
"Add 48-frame video fade-to-black at sequence end on V1"

Section transitions (within video):
"Add 6-frame Film Dissolve between [CLIP_A] and [CLIP_B] on V1"
Do NOT use: Wipe, Slide, Cube Spin, or any 3D transition — finance content only.
```

---

## SEQUENCE 10 — EXPORT PRESET

Run when the edit is final and all graphics are placed.

```
"Export sequence [SEQUENCE-NAME] with settings:
  Format: H.264
  Preset: YouTube 1080p Full HD
  Resolution: 1920x1080
  Frame rate: 29.97
  Video bitrate: VBR 2-pass, Target 20Mbps, Max 25Mbps
  Audio: AAC, 320kbps, 48kHz, Stereo
  Output file: [PROJECT-FOLDER]/EXPORTS/[PROJECT-NAME]-MASTER.mp4"

For social clips (vertical):
"Export sequence [SEQUENCE-NAME] with settings:
  Resolution: 1080x1920
  All other settings same as above
  Output file: [PROJECT-FOLDER]/EXPORTS/[PROJECT-NAME]-VERTICAL.mp4"
```

---

## SEQUENCE 11 — QUALITY CHECK BEFORE EXPORT

Run this before every export. Catch problems before they're permanent.

```
"Get full sequence info — confirm:
  Duration matches expected length (±5 seconds)
  No gaps in V1 track (no black frames)
  No audio spikes above -3dB on A1
  All graphic clips on V2/V3/V4 have correct in/out points"

Visually verify (human step — agent cannot do this):
  □ Speaker is in focus and well-lit throughout
  □ No graphic overlaps the speaker's face
  □ Captions are accurate
  □ Audio levels consistent (no sudden jumps)
  □ Color grade is consistent across all cuts
```

---

## DECISION TREE — WHICH SEQUENCE TO RUN

```
New project with raw footage?
  → Run SEQUENCE 1 (Project Setup)
  → Run SEQUENCE 2 (Speaker Detection)
  → Run SEQUENCE 3 (Silence Removal)
  → Run SEQUENCE 4 (Repeated Phrase Removal)
  → Run SEQUENCE 5 (Audio Normalization)
  → Run SEQUENCE 6 (Color Grade)
  → [Now hand off to DIRECTOR.md for graphics]

Have B-roll files?
  → Run SEQUENCE 7 after rough cut

Two speakers?
  → Run SEQUENCE 8 after import

Ready to export?
  → Run SEQUENCE 11 (Quality Check)
  → Run SEQUENCE 10 (Export)
```
