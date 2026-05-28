# HYPERFRAMES-EXECUTION.md — Real Template Execution Protocol
# claudedit / [Your Channel Name]
# Version: 1.0
#
# This file exists because the agent was generating fake graphics —
# text layers in Premiere instead of actual HyperFrames renders.
#
# RULE: Every HyperFrames graphic MUST follow this protocol exactly.
# No shortcuts. No native Premiere text as a substitute.
# If a render didn't produce a .mov file, it didn't happen.

---

## THE FUNDAMENTAL RULE

HyperFrames templates are NOT prompts to generate from scratch.
They are INSTALLED TEMPLATES that you initialize, populate, and render.

The correct mental model:
  WRONG: "Generate a swiss-grid graphic with this content"
  RIGHT: "Initialize swiss-grid template → edit compositions/graphics.html → render → import MOV"

Every template already contains:
  - The grid background (swiss-grid has the actual grid)
  - The layout structure
  - The animation system
  - The typography scale
  - The color variables

Your job is to FILL IN the content, not build the design from scratch.

---

## STEP-BY-STEP EXECUTION — EVERY SINGLE GRAPHIC

### STEP 1 — Initialize the template (NEVER skip this)

```bash
# Navigate to your project graphics folder
cd [PROJECT-FOLDER]/graphics

# Initialize with the CORRECT template example
# This pulls the full template — grid, layout, animations, everything
npx hyperframes init [GRAPHIC-NAME] --example [TEMPLATE-NAME]

# Example:
npx hyperframes init btc-vs-binaries-opener --example kinetic-type
npx hyperframes init msci-stat-card --example swiss-grid
npx hyperframes init investment-steps --example decision-tree
npx hyperframes init revenue-chart --example nyt-graph
```

**Template names — use exactly these:**
- `kinetic-type` — section openers, title cards, bold statements
- `swiss-grid` — stat cards, lower thirds, captions, data overlays
- `decision-tree` — step explainers, process flows
- `nyt-graph` — line charts, bar charts, data stories
- `warm-grain` — editorial, personal story moments
- `play-mode` — social hooks, energetic openers
- `product-promo` — multi-scene product/tool demos
- `vignelli` — portrait quote cards, bold announcements
- `blank` — only when no template fits AND you have a very detailed spec

### STEP 2 — Inspect what was created

```bash
# See the full file structure the template created
ls -la [GRAPHIC-NAME]/

# Expected output for swiss-grid:
# meta.json
# index.html
# compositions/
#   intro.html
#   graphics.html      ← main data/stat compositions
#   captions.html      ← subtitle track
# assets/
```

Open `compositions/graphics.html` in a text editor.
You will see the template's actual HTML — grid lines, layout divs, animation stubs.
This is what you edit. Do NOT replace it. Do NOT start over.

### STEP 3 — PURGE ALL DEMO CONTENT, THEN INSERT YOURS

⚠️ CRITICAL — THIS IS THE STEP THAT KEEPS FAILING ⚠️

The example templates do NOT contain clean placeholders like `[YOUR TEXT]`.
They contain the HyperFrames DEMO'S REAL CONTENT, hardcoded in multiple places:
  - "HYPERFRAMES" / "Hyperframes" / "Design simplified"
  - "THE SURVEY FINDINGS" / "The Opportunity"
  - "47%" / "NEED MOTION GRAPHICS" / "3 OF 4" / "LACK EDITING SKILLS"
  - "Forty-seven percent of you said"

If you only ADD your content without DELETING theirs, BOTH render on top of
each other. That is the "HYPERFRAMES + your text overlapping" bug. (See image 1.)

**The protocol is PURGE, then INSERT — in that order:**

#### 3a. Find every piece of demo text across ALL files
```bash
cd [GRAPHIC-NAME]
# Search every file for the demo's hardcoded strings:
grep -rni "hyperframes\|survey findings\|the opportunity\|motion graphics\|percent of you\|design simplified\|lack editing\|3 of 4\|47%" .
```
This lists every file and line number containing demo content.
You MUST address every single match. Do not skip any.

#### 3b. Open EVERY composition file — not just one
The demo content is spread across multiple scenes and files:
```bash
ls compositions/
# kinetic-type may have: intro.html, scene2.html, scene3.html, main-graphics.html
# swiss-grid may have: intro.html, graphics.html, captions.html
# Open and inspect ALL of them. Demo text hides in scenes you didn't expect.
```

#### 3c. REPLACE demo strings with your content (don't add — replace)
For each match from 3a, replace the demo string in place:
```
"HYPERFRAMES"                → your actual word/title
"THE SURVEY FINDINGS"        → your subtitle (or delete the element)
"The Opportunity."           → your content (or delete)
"47%" / "3 OF 4"             → your real stat
"NEED MOTION GRAPHICS"       → your real label
"LACK EDITING SKILLS"        → your real label
```

#### 3d. DELETE any demo scene you are not using
kinetic-type ships with 6 scenes. If you only want the title card (Scene 1),
you must DELETE or disable scenes 2–6, or set the render duration so it never
reaches them (cap at 1.9s — see STEP 5). Otherwise the later scenes play the
demo's promo content.

#### 3e. Re-grep to confirm ZERO demo content remains
```bash
grep -rni "hyperframes\|survey findings\|the opportunity\|motion graphics\|percent of you\|design simplified\|lack editing" .
# This MUST return NOTHING. If any line shows, you missed one — go back to 3c.
```

**Rules:**
- Do NOT touch: CSS variables, animation timelines, grid structure, layout classes
- ONLY change: text content, numbers, colors from DESIGN.md palette, durations
- The grep in 3e returning empty is the gate. No empty grep = do not render.

**For swiss-grid graphics.html — content to edit:**
```html
<!-- Find these and replace with your content -->
<div class="stat-hero">[YOUR NUMBER HERE]</div>
<div class="stat-label">[YOUR LABEL HERE]</div>
<div class="stat-context">[YOUR CONTEXT LINE HERE]</div>
<div class="source-attribution">[SOURCE, YEAR]</div>
```

**For kinetic-type main-graphics.html — content to edit:**
```html
<!-- Find the word array and replace -->
const words = ["YOUR", "WORDS", "HERE"];
<!-- Find the subtitle and replace -->
<div class="subtitle">[YOUR SUBTITLE]</div>
```

**For decision-tree decision_tree.html — content to edit:**
```html
<!-- Find nodes and replace text only -->
{ id: "start", text: "[YOUR QUESTION]" },
{ id: "yes", text: "[YES OUTCOME]" },
{ id: "no", text: "[NO OUTCOME]" },
```

**For nyt-graph nyt-chart.html — data to edit:**
```javascript
// Find the data array and replace values only
const chartData = [
  { label: "[LABEL]", value: [NUMBER] },
  { label: "[LABEL]", value: [NUMBER] },
];
const chartTitle = "[YOUR CHART TITLE]";
const chartSource = "[SOURCE, YEAR]";
```

### STEP 4 — Apply DESIGN.md colors

After editing content, find the CSS variable block (usually in `index.html` or a `styles.css`):

```css
/* Replace with your DESIGN.md palette */
:root {
  --color-bg: #0A0A0A;
  --color-surface: #161616;
  --color-border: #2A2A2A;
  --color-text-primary: #F0F0F0;
  --color-text-muted: #888888;
  --color-accent: #[YOUR-ACCENT-HEX];
  --color-white: #FFFFFF;
}
```

Do NOT invent new colors. Only these values.

### STEP 5 — Set duration in meta.json

```json
{
  "width": 1920,
  "height": 1080,
  "fps": 30,
  "durationInFrames": [FRAMES],
  "compositionId": "[GRAPHIC-NAME]"
}
```

Duration in frames = seconds × 30
- Stat card (5s) = 150 frames
- Kinetic opener (3s) = 90 frames
- Decision tree (15s) = 450 frames
- Captions = match source duration

### STEP 6 — Preview before rendering

```bash
# Start the HyperFrames dev server to visually verify
npx hyperframes dev [GRAPHIC-NAME]

# Opens in browser at localhost:3000
# CHECK:
# □ Grid/template structure is visible (not blank)
# □ Your content appears correctly
# □ Animation plays smoothly
# □ Colors match DESIGN.md
# □ Text is readable at 1080p scale
# □ No placeholder text remaining
```

DO NOT SKIP THE PREVIEW. This is where you catch problems before a slow render.

### STEP 7 — Run QA-CHECKLIST.md

Before rendering, run every BLOCKING check from QA-CHECKLIST.md.
If anything fails → fix it in the composition files → preview again → re-check.

### STEP 8 — Render

```bash
# Render to MOV (ProRes for overlays, H.264 for full-bleed)
npx hyperframes render [GRAPHIC-NAME] --format mov

# Output location:
# [GRAPHIC-NAME]/out/[GRAPHIC-NAME].mov

# For transparent overlays (lower thirds, captions):
npx hyperframes render [GRAPHIC-NAME] --format mov --transparent

# Confirm render completed:
ls -lh [GRAPHIC-NAME]/out/
# You must see a .mov file with a non-zero file size
# If file is 0 bytes or missing → render failed → do not import
```

### STEP 9 — Import to Premiere

```
"Import [GRAPHIC-NAME]/out/[GRAPHIC-NAME].mov into the GRAPHICS bin"

For FULL-BLEED graphics (kinetic-type, section cards, full stat cards):
  "Place [GRAPHIC-NAME].mov on V1 at [TC_START]"
  "Set V1 clip duration to match MOV duration"
  "Mute or hide original A-roll V1 clip for this duration"
  Note: Full-bleed REPLACES footage — it goes on V1, not V2

For OVERLAY graphics (lower thirds, captions, stat overlays):
  "Place [GRAPHIC-NAME].mov on V2 at [TC_START]"
  "Set blend mode to Normal (transparent renders) or Screen (if no transparency)"

For CAPTION tracks:
  "Place captions.mov on V4 at [TC_START]"
  "Stretch to match corresponding A-roll duration"
```

---

## WHAT PREMIERE HANDLES NATIVELY — DON'T USE HYPERFRAMES FOR THESE

Build these directly in Premiere. Faster, easier to adjust.

```
✅ BUILD IN PREMIERE:
  - Simple lower thirds (name + title, static or simple slide-in)
    → Use Essential Graphics panel, not HyperFrames
  - Basic text callouts (one line of text overlay)
    → Use Legacy Title or Essential Graphics
  - Audio waveform visualization
    → Premiere's built-in audio meters
  - Speed ramps / slow motion
    → Time remapping on clip
  - Simple color overlays / bars
    → Adjustment layers with color fills
  - Split screen (two speakers side by side)
    → Crop effect on two V1/V2 clips
  - Picture-in-picture
    → Scale + position on V2 clip

🎬 USE HYPERFRAMES FOR:
  - Animated stat cards with count-up numbers
  - Full swiss-grid compositions with grid background
  - Kinetic-type word-by-word reveals
  - Decision tree / flowchart animations
  - NYT-style animated data charts
  - Warm-grain editorial full-bleed moments
  - Play-mode social hook openers
  - Vignelli portrait quote cards
  - Any animation that requires GSAP timeline control
```

---

## GRAPHIC LIBRARY — REUSE BEFORE REBUILDING

Once a graphic is rendered, save it to the library. Never re-render the same graphic type.

```
[PROJECT-ROOT]/
  graphic-library/
    lower-thirds/
      [speaker-name]-lower-third.mov    ← render once, reuse every video
    openers/
      kinetic-opener-v1.mov
      kinetic-opener-v2.mov
    captions/
      [project-name]-captions.mov
    stat-cards/
      [stat-name]-card.mov
    section-breaks/
      section-break-01.mov
      section-break-02.mov
```

Before generating any new graphic, check the library first.
If a similar graphic exists → reuse or duplicate and edit content only.
Re-rendering is expensive. Build the library as you go.

---

## TROUBLESHOOTING

**Render produces blank/black video:**
→ GSAP timeline not paused on init. Check `{ paused: true }` on all timelines.
→ CSS variables not resolving. Check `:root` block is in scope.

**Template looks nothing like the example:**
→ You edited the wrong file, or replaced template HTML with custom code.
→ Re-initialize: `npx hyperframes init [NAME] --example [TEMPLATE] --force`

**Colors look wrong:**
→ CSS variable override not applied. Make sure `:root` block is in `index.html` not a composition file.

**Text is too small:**
→ You used the template's default font sizes. Finance content needs larger type.
→ Find `.stat-hero` or `.headline` class and override: `font-size: 120px !important`

**Animation doesn't play:**
→ `requestAnimationFrame` or `setTimeout` used instead of GSAP. Replace with GSAP timeline.
→ Check QA-CHECKLIST Section 4 for forbidden animation methods.

**MOV file is 0 bytes:**
→ Render crashed silently. Check terminal output for errors.
→ Common cause: missing asset file referenced in composition.

---

## QUICK REFERENCE — COMMAND SEQUENCE PER GRAPHIC TYPE

### Kinetic-type opener (3s, full-bleed, V1)
```bash
npx hyperframes init [NAME]-opener --example kinetic-type
# Edit: words array, subtitle text, CSS color vars
npx hyperframes dev [NAME]-opener          # preview
npx hyperframes render [NAME]-opener --format mov
# Import → place on V1 → mute A-roll beneath
```

### Swiss-grid stat card (6s, full-bleed or overlay, V1 or V2)
```bash
npx hyperframes init [NAME]-stat --example swiss-grid
# Edit: stat number, label, context, source, CSS color vars
# In meta.json: durationInFrames: 180
npx hyperframes dev [NAME]-stat            # preview
npx hyperframes render [NAME]-stat --format mov
# Import → place on V1 (full-bleed) or V2 (overlay)
```

### Captions (full segment duration, V4)
```bash
npx hyperframes init [PROJECT]-captions --example swiss-grid
# Edit: captions.html only — paste timestamped transcript
# In meta.json: durationInFrames = segment length × 30
npx hyperframes render [PROJECT]-captions --format mov --transparent
# Import → place on V4 → stretch to match A-roll
```

### Decision tree (15–20s, full-bleed, V1)
```bash
npx hyperframes init [NAME]-steps --example decision-tree
# Edit: node text content only
# In meta.json: durationInFrames: 450–600
npx hyperframes dev [NAME]-steps           # preview
npx hyperframes render [NAME]-steps --format mov
# Import → place on V1
```

### Lower third (4s, transparent overlay, V2)
```bash
npx hyperframes init [SPEAKER]-lower-third --example swiss-grid
# Use captions.html sub-composition only
# Edit: name, title text
# Render transparent
npx hyperframes render [SPEAKER]-lower-third --format mov --transparent
# Import → place on V2 → save to graphic-library/lower-thirds/
```
