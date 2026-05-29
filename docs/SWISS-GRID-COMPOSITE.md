# SWISS-GRID-COMPOSITE.md — Speaker-Inside-Template Workflow
# claudedit / [Your Channel Name]
# Version: 1.0
#
# Goal: Render the speaker INSIDE the Swiss Grid template — grid + panel + text
# all wrapped around the speaker's footage — as ONE finished MOV. Then drop that
# single MOV into Premiere. No overlay stacking.
#
# This is different from everything before it. Previously we rendered transparent
# overlays and stacked them on V2 over A-roll. Now the speaker's footage goes
# INTO HyperFrames and comes out as a complete composited clip.

---

## THE MENTAL MODEL

```
OLD WAY (overlay stacking — looked plain):
  Premiere V1: speaker footage
  Premiere V2: transparent text overlay floating on top
  → looks like "text slapped on a webcam"

NEW WAY (composite — looks like the showcase):
  HyperFrames composition contains:
    - the Swiss Grid background (grid lines, structure)
    - a VIDEO WELL with the speaker playing inside it
    - text graphics animating in beside the speaker
  → renders as ONE MOV where everything is designed together
  → drop that single MOV into Premiere, done
```

---

## CRITICAL RULE — VERIFY THE SPEAKER FIRST

The agent has repeatedly used the WRONG speaker. Before compositing anyone into
the box, the agent MUST confirm who is actually talking in the segment.

### Speaker verification step (MANDATORY, before any compositing):
```bash
# Extract a frame from the MIDDLE of the clip's speaking segment
ffmpeg -y -ss [CLIP_MID_TIMECODE] -i [SOURCE_VIDEO] -frames:v 1 /tmp/who_is_talking.png
```
Then VIEW that frame and identify:
- Is this a single speaker or two-person split?
- WHO is the person actively speaking (mouth moving, framed as primary)?
- For two-person footage: which side is the speaker who says THIS segment's content?

The agent must state: "Segment [X] speaker is [NAME], confirmed from frame at [TC]."
Do NOT proceed to compositing until the speaker is visually confirmed.

If two people are on screen and only one is talking → crop the source to just
the speaker before compositing into the single-speaker box (see Step 4b).

---

## STEP-BY-STEP — SWISS GRID COMPOSITE

### STEP 1 — Initialize Swiss Grid WITH the speaker video

HyperFrames can ingest the source video at init:
```bash
cd [PROJECT-FOLDER]/graphics
npx hyperframes init swissgrid-[slug] --example swiss-grid --video [SPEAKER_CLIP.mp4]
```
This probes the video and wires it in. But the example's default video well may
be small or positioned for the demo. We'll resize it in Step 4.

### STEP 2 — Purge ALL demo content (the 47% / survey findings problem)

```bash
cd swissgrid-[slug]
grep -rni "hyperframes\|survey findings\|the opportunity\|motion graphics\|percent of you\|design simplified\|lack editing\|47%\|forty-seven" .
```
Open EVERY file in compositions/ (intro.html, graphics.html, captions.html) and
replace every demo string with your content. Re-grep until it returns NOTHING.

### STEP 3 — Set up the VIDEO WELL for the speaker

The Swiss Grid template's black box is the video well. Per HyperFrames docs, the
correct pattern is a wrapper div with the video filling it (never animate the
video element's dimensions directly — animate the wrapper).

In index.html or the relevant composition, the speaker video well should be:
```html
<!-- The video well — speaker fills this box -->
<div id="speaker-well" class="clip"
     style="position:absolute; top:140px; left:960px;
            width:864px; height:800px; overflow:hidden;
            border-radius:8px; background:#000;">
  <video id="speaker-video"
         data-start="0"
         data-media-start="[CLIP_IN_SECONDS]"
         data-has-audio="true"
         data-volume="1"
         src="[SPEAKER_CLIP.mp4]"
         style="width:100%; height:100%; object-fit:cover;"></video>
</div>
```

Key attributes (from HyperFrames data-attribute spec):
- `data-media-start` = the IN point in the source video (trims to your segment)
- `object-fit:cover` = speaker fills the box cleanly, no letterboxing
- wrapper has the position/size; video fills 100% — NEVER animate video dims directly

### STEP 4 — Position the grid + speaker layout

For SINGLE SPEAKER FILLS THE BOX (your chosen layout):
```
Frame: 1920×1080
  - Swiss grid background: full frame, behind everything
  - Speaker well: right side, ~864px wide (columns 7–12), full height with margins
  - Text graphics zone: left side, ~768px wide (columns 1–6)
  - Grid lines visible throughout
```

#### STEP 4b — If source is two-person, crop to the single speaker first
```bash
# Crop source to just the speaking half before compositing
# Left speaker:  crop=960:1080:0:0
# Right speaker: crop=960:1080:960:0
ffmpeg -y -ss [CLIP_IN] -t [CLIP_DUR] -i [SOURCE] \
  -vf "crop=960:1080:[X]:0,scale=864:800" \
  -c:v prores_ks -profile:v 3 [SPEAKER_CLIP_CROPPED.mov]
```
Use the cropped clip as the video well source. This puts ONLY the confirmed
speaker in the box — no second person bleeding in.

### STEP 5 — Animate text graphics in the LEFT zone

Text must be relevant to what the speaker is saying. Pull from transcript.
Each text element is a timed clip beside the speaker:
```html
<div id="stat-headline" class="clip"
     data-start="2" data-duration="6" data-track-index="1"
     style="position:absolute; top:380px; left:96px; width:768px;
            font-size:130px; font-weight:800; color:var(--accent);">
  43 vs 40
</div>
<div id="stat-label" class="clip"
     data-start="2.3" data-duration="5.7" data-track-index="1"
     style="position:absolute; top:540px; left:96px; width:768px;
            font-size:42px; color:var(--text-muted);">
  Regulated Clearing Premium
</div>
```
GSAP animates these in (fade + slide). Time them to when the speaker says it
(use transcript word timings).

### STEP 6 — Extend the timeline to the full clip length

⚠️ The #1 documented bug: composition duration = GSAP timeline duration.
If your last animation ends at 8s but the clip is 54s, it cuts off at 8s.

At the end of the GSAP timeline, extend it to the full clip duration:
```javascript
// clip is 54s → extend timeline so the speaker plays the whole way
tl.set({}, {}, 54);
```

### STEP 7 — Validate BEFORE rendering (HyperFrames' own tools)

```bash
npx hyperframes lint
# Must pass clean. Common flags: missing class="clip", missing muted attribute.

npx hyperframes compositions
# Check the resolved duration MATCHES your clip length (e.g. 54s, not 8s).

npx hyperframes dev swissgrid-[slug]
# Preview in browser. CONFIRM:
#   □ Grid visible
#   □ Speaker playing inside the box (correct speaker!)
#   □ Text animating in beside them, readable
#   □ No demo content (no 47%, no "survey findings")
#   □ Speaker plays the full duration, doesn't freeze at 8s
```

### STEP 8 — Render the full composite

```bash
# This is NOT transparent — it's the full finished frame
npx hyperframes render swissgrid-[slug] --format mov
# Output: swissgrid-[slug]/out/swissgrid-[slug].mov
# Save versioned: swissgrid-[slug]_v1.mov
```

### STEP 9 — Verify the render visually (proof, not assumption)

```bash
python3 verify_render.py
# Open the extracted frames. Confirm:
#   - Correct speaker in the box
#   - Grid + text present
#   - Real content, no stub, no demo
```

### STEP 10 — Drop into Premiere

This single MOV IS the finished clip. It goes on V1 (it's the whole frame now,
not an overlay):
```
"Import swissgrid-[slug]_v1.mov"
"Place on V1 at [TC] — this replaces the raw A-roll for this segment"
```
No V2 overlay needed — the graphics are already baked into this clip.

---

## QUALITY GATES — ALL MUST PASS BEFORE PLACING

```
□ Speaker verified visually (correct person in the box)
□ npx hyperframes lint passes clean
□ npx hyperframes compositions shows FULL clip duration (not 8s stub)
□ Browser preview shows grid + speaker + text, no demo content
□ verify_render.py frame shows the finished composite
□ Speaker plays the entire clip (check a frame near the end, not just the middle)
```

If ANY gate fails → do not place. Fix and re-verify.

---

## WHAT MAKES THIS LOOK LIKE THE SHOWCASE (vs the plain overlays)

1. The speaker is INSIDE the design, framed by the grid — not floating under text
2. The grid lines and panel structure fill the whole frame
3. Text sits in its own zone beside the speaker, not on top of their face
4. Everything animates together as one composition
5. The accent color, grid, and typography are the template's — coherent, not slapped on
