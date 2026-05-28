# PROMPT-TEMPLATES.md — HyperFrames Prompt Library
# claudedit / [Your Channel Name]
# Version: 1.0

---

## HOW TO USE THIS FILE

1. Copy the relevant template below
2. Fill in ALL `[BRACKETED]` fields — never leave them blank
3. Attach `DESIGN.md` to the same session
4. Paste into Claude Code or your agent with `/hyperframes`
5. After generation, run QA-CHECKLIST.md before rendering

---

## SCOPE RULE — WHEN TO CALL HYPERFRAMES

HyperFrames is ONLY called for:
- Motion graphic overlays (lower thirds, title cards, stat callouts)
- Subtitle/caption compositions
- Section breaks and intros
- Data visualizations as B-roll

HyperFrames is NEVER called for:
- Cutting or trimming raw footage → use Premiere MCP
- Removing silences → use Premiere MCP
- Repositioning or resizing clips on the timeline → use Premiere MCP
- Color grading raw footage → use Premiere MCP

---

## TEMPLATE INDEX

| # | Name | Template | Duration | Output |
|---|---|---|---|---|
| 1 | Caption Block | swiss-grid | Matches source | captions.html |
| 2 | Stat Callout | swiss-grid | 5–8s | graphics.html |
| 3 | Lower Third | swiss-grid | 4s | overlay |
| 4 | Section Title Card | kinetic-type | 3s | main-graphics.html |
| 5 | Quote Pull | vignelli | 6s | overlays.html |
| 6 | Step Explainer | decision-tree | 10–20s | decision_tree.html |
| 7 | Data Chart | nyt-graph | 8–12s | nyt-chart.html |
| 8 | Intro Hook | play-mode | 3–5s | intro.html |
| 9 | Product Demo Overlay | product-promo | Per scene | scene compositions |
| 10 | Editorial B-roll Card | warm-grain | 5–10s | graphics.html |
| 11 | Blank Custom Graphic | blank | Custom | captions.html |
| 12 | Podcast/Interview Caption | swiss-grid | Matches source | captions.html |

---

## TEMPLATE 1 — Caption Block
**Template:** `swiss-grid` | **Use for:** Any talking-head footage needing subtitles

```
Using /hyperframes with the swiss-grid example, create a caption composition.

DESIGN.md is attached — follow it exactly.

Specs:
- Resolution: 1920×1080, 30fps
- Duration: [X] seconds
- Output: captions.html sub-composition only

Speaker: [SPEAKER NAME]
Caption style: bottom-left, 2 lines max, white text on dark semi-transparent bar

Transcript segment:
[PASTE FULL TRANSCRIPT SEGMENT HERE — include timestamps if available]

Do not invent or paraphrase any text. Captions must exactly match the transcript.
Do not add music. Do not add any graphic elements beyond the caption bar.
```

---

## TEMPLATE 2 — Stat / Data Callout Graphic
**Template:** `swiss-grid` | **Use for:** Single number or metric that supports what speaker is saying

```
Using /hyperframes with the swiss-grid example, create a stat callout B-roll graphic.

DESIGN.md is attached — follow it exactly.

Specs:
- Resolution: 1920×1080, 30fps
- Duration: [5–8] seconds
- This is B-roll — no speaker video in this composition

Content:
- Stat: [NUMBER + UNIT, e.g. "$2.4B" or "73%"]
- Context label: [SHORT LABEL, e.g. "Total Market Cap 2024"]
- Source (optional): [SOURCE NAME, e.g. "Bloomberg, 2024"]

Layout: swiss-grid. Large stat centered, label below in muted text, source as footnote.
Accent color on the number only.

Animation:
- 0s: background fades in (0.3s)
- 0.3s: label slides up (0.4s)
- 0.7s: stat number counts up from 0 (0.8s)
- 1.5s: source fades in (0.3s)
- Hold until [X-0.4]s
- [X-0.4]s: all elements fade out (0.4s)
```

---

## TEMPLATE 3 — Lower Third
**Template:** `swiss-grid` | **Use for:** Speaker introduction, guest name, role title

```
Using /hyperframes with the swiss-grid example, create a lower-third overlay.

DESIGN.md is attached — follow it exactly.

Specs:
- Resolution: 1920×1080, 30fps
- Duration: 4 seconds
- Transparent background (no full-bleed bg — overlay only)

Content:
- Line 1 (Name): [FULL NAME]
- Line 2 (Title): [TITLE / ROLE / COMPANY]

Position: bottom-left, 8% from bottom, within left margin (96px from edge)
Style: dark semi-transparent bar behind text, accent color left-edge bar (4px wide)

Animation:
- 0s: slides in from left (0.4s, power2.out)
- 0.4s–3.5s: hold
- 3.5s: slides out left (0.3s, power2.in)
```

---

## TEMPLATE 4 — Section Title Card
**Template:** `kinetic-type` | **Use for:** Section breaks within longer videos

```
Using /hyperframes with the kinetic-type example, create a section title card.

DESIGN.md is attached — follow it exactly.

Specs:
- Resolution: 1920×1080, 30fps
- Duration: 3 seconds
- Full-bleed composition (no speaker video)

Content:
- Section number (optional): [e.g. "02" or leave blank]
- Title: [SECTION TITLE — max 4 words]
- Subtitle (optional): [SHORT DESCRIPTOR — max 6 words]

Animation:
- 0s–0.8s: title words appear one by one, each sliding up (0.15s stagger)
- 0.8s–2.5s: hold
- 2.5s–3s: all elements fade out (0.4s)

Use accent color underline beneath the title. No background pattern.
```

---

## TEMPLATE 5 — Quote Pull
**Template:** `vignelli` | **Use for:** Portrait (9:16) bold quote moments, or landscape quote B-roll

```
Using /hyperframes with the vignelli example, create a quote pull graphic.

DESIGN.md is attached — follow it exactly.

Specs:
- Resolution: [1080×1920 for portrait / 1920×1080 for landscape]
- Duration: 6 seconds
- Full-bleed composition

Content:
- Quote (exact words from speaker, do not paraphrase): "[EXACT QUOTE]"
- Attribution: [SPEAKER NAME]

Layout: large quote text, left-aligned, accent color on opening quotation mark only.
Attribution appears below in muted foreground color.

Animation:
- 0s: quotation mark fades in (0.3s)
- 0.3s: quote text reveals word by word (0.08s stagger)
- end of text + 0.3s: attribution slides up (0.4s)
- Hold 2s
- Fade out all (0.5s)
```

---

## TEMPLATE 6 — Step Explainer / Decision Tree
**Template:** `decision-tree` | **Use for:** Any process, comparison, or branching logic the speaker explains

```
Using /hyperframes with the decision-tree example, create a step explainer graphic.

DESIGN.md is attached — follow it exactly.

Specs:
- Resolution: 1920×1080, 30fps
- Duration: [10–20] seconds depending on step count
- Full-bleed B-roll composition

Content:
[Provide the steps/branches below — label clearly]

Option A — Linear steps:
- Step 1: [TEXT]
- Step 2: [TEXT]
- Step 3: [TEXT]
(add more as needed)

Option B — Decision branch:
- Question: [TEXT]
  - Yes → [OUTCOME]
  - No → [OUTCOME]

Animation: progressive reveal — each node appears 1.2s after the previous.
Connecting lines draw in after node appears (0.4s draw duration).
Completed path uses accent color. Future path uses muted border color.
```

---

## TEMPLATE 7 — Data Chart (NYT Style)
**Template:** `nyt-graph` | **Use for:** Trend lines, bar charts, time series data

```
Using /hyperframes with the nyt-graph example, create a data chart graphic.

DESIGN.md is attached — follow it exactly.

Specs:
- Resolution: 1920×1080, 30fps
- Duration: [8–12] seconds
- Full-bleed B-roll composition

Chart type: [line / bar / area — pick one]
Title: [CHART TITLE]
Source: [DATA SOURCE + YEAR]

Data:
[Paste your data as a simple table or list]
Example:
  2020: 1.2B
  2021: 1.8B
  2022: 2.4B
  2023: 3.1B
  2024: 4.2B

X-axis label: [e.g. "Year"]
Y-axis label: [e.g. "Revenue (USD)"]
Highlight: [which data point to accent, e.g. "2024 — most recent"]

Animation:
- 0s: axes draw in (0.6s)
- 0.6s: data draws left to right (1.5s)
- 2.1s: highlight callout appears (0.3s)
- Hold until [X-0.5]s
- Fade out (0.5s)
```

---

## TEMPLATE 8 — Intro Hook
**Template:** `play-mode` | **Use for:** Short energetic opener, 3–5s clip for social

```
Using /hyperframes with the play-mode example, create an intro hook graphic.

DESIGN.md is attached — follow it exactly.

Specs:
- Resolution: 1920×1080, 30fps
- Duration: [3–5] seconds
- Full-bleed composition

Content:
- Hook text (the payoff statement): [1 LINE, MAX 5 WORDS]
- Sub-text (optional): [1 LINE, MAX 6 WORDS]

Energy: elastic, bold. Use back.out(1.4) easing on entries.
Text should feel like it snaps into place, not floats.
No music. No sound effects.
Duration of hold after entry: [1–2]s before exit.
```

---

## TEMPLATE 9 — Product Demo Overlay
**Template:** `product-promo` | **Use for:** Screen recordings, SaaS demos, feature callouts

```
Using /hyperframes with the product-promo example, create a multi-scene product overlay.

DESIGN.md is attached — follow it exactly.

Specs:
- Resolution: 1920×1080, 30fps
- Total duration: [X] seconds across [N] scenes

Scenes:
Scene 1 — [DURATION]s: [DESCRIPTION OF WHAT'S ON SCREEN AND WHAT TO HIGHLIGHT]
Scene 2 — [DURATION]s: [DESCRIPTION]
Scene 3 — [DURATION]s: [DESCRIPTION]
(add more as needed)

For each scene, provide:
- Feature being highlighted: [TEXT]
- Callout label (if any): [TEXT]
- Arrow/pointer needed: [yes/no, and where it points]

Assets: [list any SVG or PNG files to include, or write "none"]
```

---

## TEMPLATE 10 — Editorial B-roll Card
**Template:** `warm-grain` | **Use for:** Lifestyle context, personal story moments, editorial feel

```
Using /hyperframes with the warm-grain example, create an editorial B-roll composition.

DESIGN.md is attached — follow it exactly.

Specs:
- Resolution: 1920×1080, 30fps
- Duration: [5–10] seconds

Content:
- Main text: [1–2 lines, editorial tone]
- Supporting detail (optional): [SHORT LINE]
- Mood: [e.g. "reflective", "optimistic", "serious"]

Style: warm-grain aesthetic. Cream/warm tones from palette.
Grain texture overlay. Smooth, slow transitions.
No hard cuts within the composition.
```

---

## TEMPLATE 11 — Blank Custom Graphic
**Template:** `blank` | **Use for:** Any graphic not covered by the above templates

```
Using /hyperframes with the blank example, create a custom graphic.

DESIGN.md is attached — follow it exactly. The agent must derive all design 
decisions from DESIGN.md — no defaults, no inventions.

Specs:
- Resolution: 1920×1080, 30fps
- Duration: [X] seconds

Description of what this graphic needs to do:
[DESCRIBE IN PLAIN LANGUAGE — be specific about content, layout, and timing]

Elements needed:
- [LIST EACH ELEMENT: type, content, position, animation]

Important constraints:
- [ANY SPECIFIC RULES FOR THIS GRAPHIC]
```

---

## TEMPLATE 12 — Podcast / Interview Captions (Long Form)
**Template:** `swiss-grid` | **Use for:** Full transcript captioning for podcast-style content

```
Using /hyperframes with the swiss-grid example, create a full caption track 
for a podcast/interview segment.

DESIGN.md is attached — follow it exactly.

Specs:
- Resolution: 1920×1080, 30fps
- Duration: matches source video segment
- Output: captions.html only — no other graphic elements

Speakers:
[If single speaker]: Speaker: [NAME]
[If multiple speakers]: 
  Speaker A: [NAME] — label color: white
  Speaker B: [NAME] — label color: accent

Caption format: 
- Speaker label appears at start of each new speaker turn
- Max 2 lines per caption
- Bottom-left position, within safe area
- Captions clear on speaker change or natural pause >1.5s

Transcript with timestamps:
[PASTE FULL TIMESTAMPED TRANSCRIPT HERE]
Format: [00:00:00] TEXT
```
