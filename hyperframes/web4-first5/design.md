# Design System — "Anndy Lian Web4" overlays · LIGHT SWISS GRID

Mood: **editorial, precise, confident — International Typographic Style.** Off-white paper, a visible modular grid, heavy black ink type, one warm accent. Think Vignelli / Müller-Brockmann meets a modern explainer. (This REPLACES the dark charcoal/electric-cyan "cinematic" look, which the user rejected on review.)

Canvas 1920×1080, 24fps, single centered speaker (Anndy Lian). Overlays composite over the source; speaker is never covered on the face.

## Palette
- Paper base:        `#F4F2EC`  (warm off-white)
- **Swiss grid lines: `#E3DFD4`** — hairlines on a 120px module, visible behind content (this is the signature of the look)
- Ink primary:       `#1A1A18`  (near-black headlines/body)
- Ink secondary:     `#6E6B63`  (eyebrows, sublabels)
- **Accent (the ONE): coral `#CC785C`** — index numerals, rules, key words, bars, arrows, the highlighted node. (Swap to a Swiss red on request.)
- Card surface (nodes/cards): `#FFFFFF` with a 1px ink-tint border `rgba(26,26,24,0.12)` + soft shadow.
- No glows (glows are a dark-mode device; on paper use thin rules + subtle shadows). No blur. No grain.

## The grid (do not skip — it's the brand)
- Every full-screen and panel background carries the **120px hairline grid** (`#E3DFD4`) over paper.
- Content aligns to the grid: flush-left, generous left margin (~130px), thin top rules, a running index (`01 /`) in coral.

## Typography
- Headlines/display: **Inter 800–900**, tight tracking (`-0.02em`), large, ink.
- Eyebrows/labels: Inter 600, uppercase, `letter-spacing:0.2em`, secondary ink.
- Numerals: Inter 900, `font-variant-numeric:tabular-nums`. Big stats 200–300px, ink, with a coral underbar.
- One accent idea per beat — a single coral word/number/rule, never two.

## Motion (calm, precise)
- Eases: `expo.out`, `power3.out`, `power2.inOut`, `power2.in` (exits). No bounce/elastic/spin.
- Reveals: clip-path wipe-ups, coral rule draws (scaleX), count-ups, flush-left line stagger. Confident, 0.5–0.9s.
- Over the video each overlay animates IN at its start, OUT before its end.

## Modes
- **Swiss keypoint (bullets/stat windowed):** paper+grid panel left (index, rule, lines reveal on spoken word) + speaker in a right window.
- **Full-screen cutaway (chart/fullflow/hero/compare):** speaker gone — paper+grid fills the frame with the data/diagram/headline.
- **Kinetic:** paper lower-third band over the speaker, ink phrases that STAY, one coral emphasis.
- **Card (glass):** white card + coral accent bar over the speaker (no blur).

## What NOT to do
- No dark/charcoal backgrounds (that was the rejected look). No cyan. No glows or blur or grain. No more than ONE coral accent per beat. No serif. Never cover the speaker's face.
