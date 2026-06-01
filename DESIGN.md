# DESIGN.md — Dark Finance / Swiss-Grid Talking Head

This file is the source of truth for all compositions in this project.
The `/hyperframes` skill reads this first before authoring any HTML.

**Date context:** the restream-may18 episode was recorded **June 2026**. When the guest says "this year" he means **2026**, prior period = **2025**. All on-screen date labels use **2026 / 2025** — never 2025 / 2024.

---

## ⚠️ READ THIS FIRST — Opening 6 Seconds Is Mandatory

**The speaker must be visible and framed on the RIGHT from t=0. The LEFT zone must show a SEQUENCE of at least 3 DIFFERENT graphic elements stacking/firing in the first 6 seconds.**

### NON-NEGOTIABLE: Speaker is ALWAYS visible

- The opening is NEVER full-frame text on a black background.
- The speaker is framed on the RIGHT (Mode A or B) starting at t=0 — NOT after the text, not at t=10s, from the very first frame.
- All opening graphics animate in the LEFT 60% zone while the speaker stays visible on the right.
- If a beat shows text on full-frame black with no speaker, it is WRONG and must be rebuilt.

### NON-NEGOTIABLE: Multiple DIFFERENT graphic elements, not one

The first 6 seconds must layer at least 3 DIFFERENT element types in sequence on the left — not one animation. Different ELEMENTS, not one element animating.

Example opening sequence (speaker visible right the entire time):
- `t=0.0s` — Speaker already framed on right. Monospace index "05" + eyebrow label "WINTERMUTE OTC DESK" slams in top-left.
- `t=0.4s` — Cyan horizontal rule draws left-to-right under the eyebrow.
- `t=0.8s` — Large stat "3.5×" counts up / slams in (cyan, the accent element).
- `t=1.6s` — Stat label "MORE ALTCOIN OPTIONS NOTIONAL" slides in from left beside the stat.
- `t=2.4s` — Sublabel "vs. 2025 same period" fades in.
- `t=3.2s` — A second element enters: bottom tag row "YIELD STRATEGIES · LOW DELTA" reveals, OR a kinetic word stack of the spoken phrase begins.
- `t=4.5–6.0s` — Third distinct element: lower-third name card, OR a Liquid Glass Card if a name is dropped, OR a swiss-grid mini-stat.

That is 3+ distinct element TYPES (index/eyebrow, stat block, tag row/word stack) all on the left, speaker visible on the right throughout.

### What counts as "aggressive" (the bar)

PASS: speaker framed right + index + eyebrow + rule + stat + label + sublabel + a second graphic type, all within 6s.
FAIL: one stat counting up on black with no speaker. One kinetic word stack alone. Any full-frame text with no speaker.

If the EDL beat map does not show the speaker present from t=0 AND 3+ different element types before t=6.0s, reject it and redo it.

---

## Hard Rules (Non-Negotiable)

- **No intro cards.** Never generate a guest/host introduction card. Skip or reclassify.
- **No outros.** Never generate an end card, CTA card, or closing screen of any kind.
- **Full-frame cuts only.** Every beat is a full-frame graphic that cuts in over the video in Premiere. No transparent overlays, no lower-thirds, no PiP.
- **ONE cyan element per frame maximum.**
- **Never use `repeat: -1`** — calculate exact repeat count from scene duration.
- **Never use `Math.random()`** — all motion must be deterministic.
- **Always init from a Hyperframes template** using `npx hyperframes init --example <name>`. Never build from blank.
- **Minimum eyebrow weight: Inter 700, #F0F0F0.** Never use muted grey (#888888) for any text smaller than 48px.
- **Minimum font size for any visible label: 32px.**
- **No film grain.** Never add `grain-overlay` / fractal-noise texture overlays. The user rejects them.
- **No `backdrop-filter: blur()` over video.** It renders muddy and was rejected twice. Get the "liquid glass" look from a solid/translucent dark fill + cyan accent bar + glow instead (see Cards & Panels).
- **Overlay z-index.** In `index.html` the video frame `#short_mag_cut_frame` is `z-index: 2`. EVERY overlay beat's `#id` MUST be listed in the `z-index: 3` rule or it renders BEHIND the full-frame video and is invisible. When a NEW beat is added, add its id to that rule. When an overlay "doesn't appear," check this FIRST.

---

## Speaker Framing (Hard Rule)

Every composition must reposition the source video. Never leave the video sitting full-frame behind the graphics unmodified. Use one of these two modes:

### Mode A — Static camera (speaker stays in one position)
- Crop and scale the video to **85% of the RIGHT 40% zone** (x: 1152–1920px) — do NOT fill edge to edge
- Use `object-fit: cover`, `object-position` centered on the speaker's face
- Leave at least **40px clearance from the bottom edge** so any name lower-third is fully visible
- Leave at least **20px clearance from the top edge**
- Entry: `x: 200px → 0, opacity: 0 → 1, expo.out, 0.6s`
- Result: head-and-shoulders speaker with breathing room, name never cut off

### Mode B — Changing camera angles (multi-cam, cuts, panels, stage footage)
- Scale the entire video down to fit the RIGHT 40% zone as a letterboxed window
- Video window: `width: 768px, height: 432px`, positioned at `x: 1152px, y: 324px`
- Background: `#0A0A0A`
- Entry: `scale: 0.92 → 1, opacity: 0 → 1, expo.out, 0.7s`

**How to choose:** Single consistent speaker → Mode A. Camera cuts, multiple people, stage/panel → Mode B.

This applies to every beat. Exception: full-frame kinetic-type word stack beats with no video.

---

## Opening 6 Seconds (Hard Rule)

Every clip must be aggressive in the first 6 seconds. No slow builds, no empty frames.

1. `t=0.0s` — First graphic fires immediately. No delay.
2. `t=0.0–0.3s` — Kinetic Word Stack or large stat slams in over full-frame video
3. `t=0.3–1.0s` — Video animates to its framed position (Mode A or B) while graphic holds
4. `t=1.0–3.0s` — First graphic completes, second element enters
5. `t=3.0–6.0s` — At least one more graphic beat fires (Liquid Glass Card, swiss-grid, or second kinetic stack)

**First word of the first Kinetic Word Stack must fire at t=0.08s or earlier.**

If the clip's opening words are weak filler, pull the strongest phrase from seconds 5–15 of the transcript and use it as the opening kinetic instead.

---

## Hyperframes Template Mapping

Always initialize compositions from the correct built-in template, then apply DESIGN.md palette and fonts on top.

| Content type | `--example` name | Why |
|---|---|---|
| Stats, data, numbers, comparisons | `swiss-grid` | Clean structured layout for data |
| Strong sentences, phrases, word-for-word impact | `kinetic-type` | Words stack on screen in sync with speaker |
| Pull quotes, hot takes, punchlines | `kinetic-type` | Dramatic typography, full-frame impact |
| Process flows, how-it-works, step chains | `decision-tree` | Animated nodes + arrows |
| Charts, market trends, time-series data | `nyt-graph` | Editorial data visualization |
| Product/feature reveals, named tools | `product-promo` | Multi-scene product showcase |
| Hype moments, milestones, big wins | `play-mode` | Energetic elastic motion |
| Narrative intros, brand/editorial moments | `warm-grain` | Textured, cinematic feel |

**Init command:**
```
npx hyperframes init beat-[N]-[slug] --example [template-name] --video [source.mp4]
```

---

## Kinetic Word Stack — Detailed Spec (UPDATED — phrase build, no dim)

**`--example kinetic-type`**

Use this aggressively. Any time the speaker delivers a strong sentence or memorable phrase, fire a Kinetic Word Stack. This is the highest-engagement template.

**How it works (the requested default — do NOT revert to dimming/black):**
- The sentence builds **line-by-line as PHRASES** (2–4 words per line), e.g. `IN THIS HALF` / `OF THE YEAR` / `WE TRADED`. NOT one word at a time.
- Each line slams in and **STAYS at full opacity**. Do NOT dim previous lines. The full sentence is readable on screen at the end.
- Plays **OVER the full-frame video (both speakers visible)** with a dark gradient backdrop behind the text. The video does NOT cut away. Never on a plain black background.
- Lines stacked `display:flex; flex-direction:column; gap:12px`, vertically centered in the left zone.
- The final / payoff line gets the single cyan accent (`#00D4FF`) — one line only.
- Each line fires in **tight sync (within ~0.03s of the spoken word)** — read the word timestamp from audio.json and fire on it, NOT 0.3–0.4s early.

**Typography:**
- Phrase lines: Inter 900, **~130px**, `#FFFFFF`, all caps, `text-shadow` for contrast over video
- Accent (payoff) line: Inter 900, same size, `#00D4FF` + cyan glow
- All lines stay full opacity — no dimmed/stacked-grey treatment

**GSAP per line:**
- Entry: `fromTo({opacity:0, y:28}, {opacity:1, y:0}, expo.out, 0.28s)` at the spoken-word offset
- Payoff line: add `scale:0.92→1` for emphasis
- No per-line dim. Exit (whole stack): `y:0→-32, opacity:1→0, power2.in, 0.28s` at beat end (handled by the beat boundary)

**When to use:**
- Speaker says something quotable, surprising, or emphatic
- Any sentence with a strong verb or claim
- Topic pivots: the first strong sentence of a new idea
- Host questions are fine as their own stack (right side, over the guest) — but NO "HOST" label, show the question text only

**When NOT to use:**
- Casual filler ("you know", "I think", "sort of")
- Transition chatter between topics

**Example — "IN THIS HALF OF THE YEAR WE TRADED…" (3-line phrase build over full-frame video):**
```
spoken "in"     comp 0.88  → fire "IN THIS HALF"  at 0.85  (white, slams in, STAYS)
spoken "of"     comp 1.50  → fire "OF THE YEAR"   at 1.47  (white, slams in, STAYS)
spoken "we"     comp 2.26  → fire "WE TRADED"     at 2.22  (CYAN payoff, slams in, STAYS)
beat end                    → whole 3-line sentence drifts up and out together
```

---

## Cards & Panels over Video

The "liquid glass" / card look the user wants, with the blur removed:

- **Fill, not blur.** Solid translucent dark: `background: rgba(20,26,34,0.90–0.92)`. NO `backdrop-filter`. Add a subtle `1px` border (`rgba(255,255,255,0.07)`) and a soft outer glow (`box-shadow: 0 0 40px rgba(0,212,255,0.10), 0 8px 40px rgba(0,0,0,0.65)`).
- **Cyan accent bar** — 4px, left edge, rounded, `#00D4FF` with a small glow. One per card.
- **Feather the edge into the video.** A left-zone panel must fade out at its right edge into the video, never a hard rectangular cut: `mask-image: linear-gradient(to right, black 82%, transparent 100%)` (+ `-webkit-mask-image`). The backing gradient should also fade to `transparent` by ~92%.
- **No per-card index numbers.** Do not put `01 / 02 / 03` inside decision-tree or comparison cards. Vertically center the card's title + description: `display:flex; flex-direction:column; justify-content:center; min-height:96px`.
- **Comparison = sequential replacement** when the intent is "replace A with B" (e.g. STAKING → COVERED CALLS): slide card A out (`x:-900, opacity:0`) and bring card B into the SAME position (grid-overlap both cards in one cell). Not a permanent side-by-side split unless explicitly comparing.

---

## Color Palette

```css
--bg:           #0A0A0A;   /* near-black background */
--surface:      #141A22;   /* dark blue-grey cards */
--border:       #2A2A2A;   /* subtle grid lines / dividers */
--text:         #F0F0F0;   /* warm white body text */
--text-muted:   #888888;   /* labels, subtitles, eyebrows */
--accent:       #00D4FF;   /* electric cyan — ONE element only per frame */
--accent-bg:    rgba(0, 212, 255, 0.12);
--grid-line:    #181818;   /* 96px repeating grid */
```

---

## Typography

```css
--font: 'Inter', sans-serif;
--font-mono: 'JetBrains Mono', monospace;
/* Weights used: 400 (body), 500 (eyebrow), 600 (labels), 700/800/900 (display) */
```

| Role | Size | Weight | Notes |
|------|------|--------|-------|
| Display / stat | 200px | 900 | tabular-nums, cyan glow on accent element |
| Slam word | 132px | 900 | full-width, one at a time |
| Section title | 64px | 700–800 | — |
| Subtitle | 34px | 500–600 | secondary color |
| Eyebrow | 32px | 700 | uppercase, 0.18em letter-spacing, #F0F0F0 (min 32px — never 24px) |
| Mono label | any | 400 | JetBrains Mono, data tables, epoch rows |

---

## Layout

```
Total canvas: 1920 × 1080px

Left zone  (graphics):  0 – 1152px  (60%), 80px inner margin
Right zone (speaker):   1152 – 1920px (40%)
Vertical divider:       x: 1151px, 1px, color: var(--border)
```

---

## Structural Elements

Every frame uses these consistent marks — apply on top of whatever Hyperframes template is used:

- **Monospace index** — e.g. `01`, `02` — 20px, muted grey, top-left
- **Eyebrow label** — 32px, weight 700, #F0F0F0, uppercase, 0.18em letter-spacing (min 32px)
- **Horizontal rule** — 2px, cyan, extends to right edge of left zone
- **Corner registration marks** — 26px L-brackets, `var(--border)`, all four corners
- **Vertical divider** — 1px at x:1151px
- **Cyan accent bar** — 4px left border, rounded, on cards and bullet lines

---

## Animation Language

Override the template's default eases with these:

| Motion | GSAP | Duration |
|--------|------|----------|
| Panel wipe | `scaleX: 0→1, power3.inOut` | 0.6s |
| Divider draw | `scaleY: 0→1, power4.out` | 0.8s |
| Node pop | `scale: 0→1, back.out(1.5)` | 0.45s |
| Connector draw | `strokeDashoffset, power1.inOut` | 0.55s |
| Payoff / accent | `scale: 0.88→1 + opacity, expo.out` | 0.8s (always last) |
| Key point reveal | `y: 26→0 + opacity, staggered by spoken timing` | 0.55s |
| Slam word entry | `scale pop, expo.out` | 0.3s |
| Slam word exit | `drift up, power2.in` | 0.25s |
| Card slide-in | `x from right, expo.out` | 0.5s |

Payoff/accent element always animates last in each scene.

**GSAP hidden-state rule (load-bearing).** Any element that must be invisible before its tween fires needs `opacity: 0` set in **CSS on the animated element itself** — or `immediateRender: true` placed in the `to`-vars (second arg) of `fromTo`, NOT the `from`-vars. `fromTo` inside a paused timeline does not pre-apply the from-state on seek, and a parent's `opacity: 0` blocks all its children even when a child animates to `opacity: 1`. Put the hidden state on the element that animates.

---

## Template Selection Guide (for EDL)

| Content type | Hyperframes template |
|---|---|
| Big stat, number, metric | `swiss-grid` |
| Speaker mentions a tool, product, or name by name | Liquid Glass Card (custom) |
| Strong sentence or memorable phrase | `kinetic-type` (Kinetic Word Stack) |
| Pull quote, hot take, punchline | `kinetic-type` (Kinetic Word Stack) |
| Comparison, side-by-side | `swiss-grid` |
| Process, flow, cause-and-effect chain | `decision-tree` |
| Chart, trend, time-series | `nyt-graph` |
| Topic shift, before/after | `kinetic-type` |
| Hype moment, milestone | `play-mode` |
| Reflective, personal, storytelling moment | `warm-grain` |
| Opinion, reaction, casual aside | Camera only (no graphic) |

**Frequency guide:** In a 90–180s clip, expect:
- 3–5 Kinetic Word Stacks (the most common — fire on every strong sentence)
- 2–4 Liquid Glass Cards (every name-drop)
- 1–2 swiss-grid beats (stats and comparisons)
- 1 decision-tree or nyt-graph if the content supports it
- Clean speaker video between every graphic (minimum 2s gap)


---

## QA Checklist (the QA agent MUST grade against these exact criteria)

Grade every clip against this list. ANY single FAIL = the whole clip fails and must be fixed before render.

**VERIFY BY FRAME (MANDATORY) — do this before claiming any fix works.**
After every render, extract frames at each changed beat and LOOK at them:
```
ffmpeg -ss <seconds> -i renders/<file>.mp4 -frames:v 1 /tmp/f.png   # then Read /tmp/f.png
```
Never report a fix as done without viewing the frame. Never iterate on opacity / visibility / layering / timing by guessing — one frame extraction catches layering bugs (e.g. an overlay hidden behind the video) in a single pass instead of several blind rounds.

**Opening (first 6 seconds):**
- [ ] Speaker is visible and framed on the RIGHT from t=0 (NOT full-frame text on black) — FAIL if speaker first appears after t=1s
- [ ] At least 3 DIFFERENT graphic element types fire on the left before t=6.0s (not one element animating) — FAIL if only one element type
- [ ] First graphic element fires at t=0.3s or earlier

**Speaker framing (every beat with video):**
- [ ] Speaker framed per Mode A (85% scale, 40px bottom clearance) or Mode B — FAIL if name is cut off
- [ ] Video is repositioned/scaled, NOT sitting full-frame unmodified behind graphics

**Graphic depth (whole clip):**
- [ ] Minimum 8 graphic beats for clips over 90s
- [ ] No same template twice in a row
- [ ] Every name-drop has a Liquid Glass Card
- [ ] Every stat has a swiss-grid
- [ ] Every strong sentence has a kinetic word stack

**Hard rules:**
- [ ] No intro cards, no outros
- [ ] One cyan element per frame maximum
- [ ] All eyebrow text Inter 700, min 32px (FAIL if muted grey under 48px)

**Typography and layout (every beat with visible body text):**
- [ ] Body / bullet text minimum font-weight 600 — FAIL if any viewer-facing content is font-weight 400 or 500
- [ ] Bullet items: text wraps UNDER the first character, not under the bullet dot — FAIL if `flex-start` row item has text with no `min-width: 0; flex: 1` causing text to reset to dot level on wrap
- [ ] Column headers at equal visual height across side-by-side columns — FAIL if one column header wraps and pushes bullets out of alignment with the other column

**Full-screen moments:**
- [ ] For clips over 90s: at least ONE full-frame video scene with kinetic text overlay showing both speakers — FAIL if every beat uses only the left-zone/Mode A split
- [ ] Full-screen overlay beats must have a dark gradient backdrop for text readability — FAIL if text appears directly on unmodified bright video with no backdrop

Report format: list each beat with PASS/FAIL per criterion. Do NOT give a numeric score — a clip either passes every criterion or it fails. If anything fails, fix it and re-grade before rendering.