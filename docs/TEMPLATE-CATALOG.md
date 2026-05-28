# TEMPLATE-CATALOG.md — HyperFrames Template Reference
# claudedit / [Your Channel Name]
# Version: 1.0
# Source: https://hyperframes.mintlify.app/examples

---

## HOW TO USE THIS CATALOG

This file is the agent's reference for selecting and configuring templates.
Before choosing a template, read the "Decision Guide" at the bottom.
Always confirm selection against DESIGN.md Section 6.

Init command for every template:
```
npx hyperframes init [project-name] --example [template-name]
```

---

## TEMPLATE 1 — `warm-grain`

| Field | Value |
|---|---|
| Style | Organic, textured, warm |
| Format | Landscape 1920×1080 |
| Best for | Lifestyle, branding, editorial, personal story |
| Avoid for | Data-heavy content, corporate/technical topics |
| Init | `npx hyperframes init [name] --example warm-grain` |

**File structure:**
```
my-video/
├── meta.json
├── index.html
├── compositions/
│   ├── intro.html       ← opening card with warm aesthetic
│   ├── graphics.html    ← supporting visuals, editorial text
│   └── captions.html    ← subtitles
└── assets/
```

**Visual characteristics:**
- Cream/warm background tones
- Grain texture overlay on all elements
- Soft, slow transitions (no snapping or elasticity)
- Editorial typography — large, considered

**Typical durations:** 5–15 seconds per composition

**Use in claudedit for:**
- Personal story moments in longer videos
- Reflective closing segments
- "Here's what I learned" editorial beats

**Prompt note:** When using warm-grain, specify mood explicitly ("reflective", "optimistic") — the agent uses this to calibrate animation speed and text weight.

---

## TEMPLATE 2 — `play-mode`

| Field | Value |
|---|---|
| Style | Energetic, elastic, playful |
| Format | Landscape 1920×1080 |
| Best for | Social media hooks, product launches, high-retention openers |
| Avoid for | Serious topics, long-form explainers |
| Init | `npx hyperframes init [name] --example play-mode` |

**File structure:**
```
my-video/
├── meta.json
├── index.html
├── compositions/
│   ├── intro.html       ← bold energetic opener
│   ├── stats.html       ← animated stat callouts
│   └── captions.html    ← subtitles
└── assets/
```

**Visual characteristics:**
- Bold, oversized typography that snaps into place
- Elastic easing (`back.out(1.4)`)
- High contrast, energetic motion
- Short hold times (0.5–1s) — content moves fast

**Typical durations:** 3–6 seconds per composition

**Use in claudedit for:**
- 3–5 second social hook clips (YouTube shorts, LinkedIn)
- Product feature highlight reels
- "Before/after" stat moments

**Prompt note:** Only use for clips you intend to export separately for social. Don't use play-mode inside a longer calm video — the energy contrast is jarring.

---

## TEMPLATE 3 — `swiss-grid` ⭐ DEFAULT

| Field | Value |
|---|---|
| Style | Clean, structured, typographic |
| Format | Landscape 1920×1080 |
| Best for | Corporate, data, interviews, explainers, technical content |
| Avoid for | Emotional/lifestyle content, anything needing warmth |
| Init | `npx hyperframes init [name] --example swiss-grid` |

**File structure:**
```
my-video/
├── meta.json
├── index.html
├── compositions/
│   ├── intro.html       ← structured title/intro card
│   ├── graphics.html    ← data callouts, stat panels, supporting text
│   └── captions.html    ← subtitles
└── assets/
```

**Visual characteristics:**
- 12-column grid, strict alignment
- No decorative elements — structure IS the design
- Clean entries: fade + subtle upward slide
- Accent used as a single structural element (line, underline, bar)

**Typical durations:** 4–12 seconds per composition

**Use in claudedit for:**
- All talking-head B-roll graphics (default choice)
- Lower thirds
- Stat callouts supporting what speaker says
- Caption tracks

**Prompt note:** This is the safest template for any corporate or technical topic. When in doubt, use swiss-grid.

---

## TEMPLATE 4 — `kinetic-type`

| Field | Value |
|---|---|
| Style | Dramatic, bold, typographic |
| Format | Landscape 1920×1080 |
| Best for | Section breaks, title cards, dramatic quote reveals, intros |
| Avoid for | Full-length compositions — use as inserts only |
| Init | `npx hyperframes init [name] --example kinetic-type` |

**File structure:**
```
my-video/
├── meta.json
├── index.html
└── compositions/
    └── main-graphics.html   ← single scene, typography-driven
```

**Visual characteristics:**
- Large, dramatic text fills most of the frame
- Word-by-word or character-by-character reveal
- Strong use of negative space
- Fast entry, medium hold, fast exit

**Typical durations:** 2–5 seconds

**Use in claudedit for:**
- "Chapter 2:" section break cards
- Single-stat emphasis moments ("$4.2 Billion.")
- Speaker's most quotable line rendered as title card
- Video intro before speaker appears

**Prompt note:** Keep text SHORT — max 4 words for kinetic-type to work. Long sentences defeat the effect.

---

## TEMPLATE 5 — `decision-tree`

| Field | Value |
|---|---|
| Style | Diagrammatic, systematic, logical |
| Format | Landscape 1920×1080 |
| Best for | Step-by-step processes, comparisons, branching logic, tutorials |
| Avoid for | Anything without clear structure or sequence |
| Init | `npx hyperframes init [name] --example decision-tree` |

**File structure:**
```
my-video/
├── meta.json
├── index.html
└── compositions/
    └── decision_tree.html   ← animated flowchart
```

**Visual characteristics:**
- Nodes appear progressively
- Connecting lines draw in after each node
- Active path uses accent color
- Future/inactive path uses muted border color

**Typical durations:** 10–25 seconds (depends on step count)

**Use in claudedit for:**
- "How X works" explanations
- "Should you do X?" decision frameworks
- Step-by-step setup guides
- Before/during/after process breakdowns

**Prompt note:** Provide the full structure as a list or tree before asking agent to build. The agent cannot infer structure from vague descriptions.

---

## TEMPLATE 6 — `product-promo`

| Field | Value |
|---|---|
| Style | Multi-scene, polished, showcase |
| Format | Landscape 1920×1080 |
| Best for | Product demos, SaaS feature walkthroughs, app showcases |
| Avoid for | Personal/talking-head content |
| Init | `npx hyperframes init [name] --example product-promo` |

**File structure:**
```
my-video/
├── meta.json
├── index.html
├── compositions/
│   ├── scene1-logo-intro.html     ← opening brand moment
│   ├── scene2-4-canvas.html       ← main demo scenes
│   └── scene5-logo-outro.html     ← closing brand moment
└── assets/
    ├── [your-logo].svg
    ├── [feature-graphic].svg
    └── [other-assets].svg
```

**Visual characteristics:**
- Multi-scene structure — each scene is distinct
- SVG asset-heavy — bring your own product graphics
- Smooth scene-to-scene transitions
- Product UI mockups or feature callouts

**Typical durations:** 15–60 seconds total across scenes

**Use in claudedit for:**
- Product launch segments within longer videos
- Tool/software recommendations with visual demo
- "Here's what I used" segments

**Prompt note:** This template requires SVG assets. If you don't have them, either create simple shapes or use swiss-grid with text callouts instead.

---

## TEMPLATE 7 — `nyt-graph`

| Field | Value |
|---|---|
| Style | Editorial data, print-inspired, authoritative |
| Format | Landscape 1920×1080 |
| Best for | Charts, data stories, trend lines, time series, bar charts |
| Avoid for | Non-quantitative content |
| Init | `npx hyperframes init [name] --example nyt-graph` |

**File structure:**
```
my-video/
├── meta.json
├── index.html
└── compositions/
    └── nyt-chart.html    ← single animated chart composition
```

**Visual characteristics:**
- Editorial / newspaper-inspired design
- Serif or clean sans on data labels
- Axes draw in first, then data animates
- Callout annotation on key data point

**Typical durations:** 8–15 seconds

**Use in claudedit for:**
- Market data the speaker references
- Growth charts ("revenue tripled in 3 years")
- Comparison data between two options
- Any time the speaker says a specific number that would benefit from context

**Prompt note:** Provide exact data as a table or list. Agent cannot infer data from vague descriptions like "show it growing." Give real numbers.

---

## TEMPLATE 8 — `vignelli` (Portrait)

| Field | Value |
|---|---|
| Style | Bold, typographic, minimalist |
| Format | Portrait 1080×1920 |
| Best for | Headlines, announcements, quote pulls, social story format |
| Avoid for | Landscape YouTube videos — portrait only |
| Init | `npx hyperframes init [name] --example vignelli` |

**File structure:**
```
my-video/
├── meta.json
├── index.html
├── compositions/
│   ├── overlays.html     ← bold typographic overlays
│   └── captions.html     ← subtitles
└── assets/
```

**Visual characteristics:**
- Bold typography dominates — inspired by Massimo Vignelli
- Red accent color (adapt to your accent in DESIGN.md)
- Extreme typographic scale contrast (huge headline, tiny label)
- Portrait 9:16 aspect ratio

**Typical durations:** 4–10 seconds

**Use in claudedit for:**
- Instagram/TikTok story clips exported from longer content
- Standalone quote graphics for social
- Announcement cards
- Short-form vertical video hooks

**Prompt note:** This is portrait only. Don't use vignelli in a 16:9 timeline — always export as a separate social asset.

---

## TEMPLATE 9 — `blank`

| Field | Value |
|---|---|
| Style | Minimal scaffolding only |
| Format | Any (set in meta.json) |
| Best for | Custom graphics not covered by other templates, full agent control |
| Avoid for | Any scenario where a named template would work |
| Init | `npx hyperframes init [name] --example blank` |

**File structure:**
```
my-video/
├── meta.json
├── index.html
└── compositions/
    └── captions.html    ← minimal scaffolding
```

**Visual characteristics:**
- Empty composition with correct HyperFrames structure
- GSAP timeline wired up, no visual elements
- Agent derives ALL design from DESIGN.md

**Typical durations:** Custom

**Use in claudedit for:**
- Truly custom graphics where no template fits
- Experimental layouts
- When the brief is very specific about layout and no template matches

**Prompt note:** When using blank, be MORE specific in your prompt — not less. The agent has no template guardrails and will fill in defaults. Describe every element explicitly.

---

## DECISION GUIDE — Which Template to Use

```
Is this a subtitle/caption track?
  → swiss-grid (captions.html)

Is this a lower third name tag?
  → swiss-grid (overlay)

Is the speaker explaining a process or steps?
  → decision-tree

Is there a specific number or stat to show?
  → swiss-grid (stat callout) or nyt-graph (if chart)

Is this a section break or title card?
  → kinetic-type

Is this a product or software demo?
  → product-promo

Is this emotional, personal, or lifestyle?
  → warm-grain

Is this for social media in portrait format?
  → vignelli

Is this a bold social hook (3–5s)?
  → play-mode

Does it need a quote pulled out dramatically?
  → vignelli (portrait) or kinetic-type (landscape)

Nothing fits?
  → blank (with very detailed prompt)
```
