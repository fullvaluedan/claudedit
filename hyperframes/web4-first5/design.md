# Design System — "Anndy Lian Web4" overlays · CINEMATIC PREMIUM

Mood: **dramatic, refined, expensive.** Deep charcoal world, a single electric-cyan accent, real depth (soft glows, light sweeps, subtle vignette). Think a high-end tech product film — not flat, not cute, not cream. Bold modern sans, confident weighty motion. (This REPLACES the earlier ivory/"cloud" look, which was rejected.)

Canvas 1920×1080, 24fps. Talking-head body beats sit lower-third over the video on a dark scrim (never over the face, x≈700–1220 y≈150–680). The book intro is a designed split-screen (see below).

## Palette
- Charcoal base:        `#121318`  (overlays/cards), deepening to `#0C0D11` at edges
- Panel surface:        `#191B22` with a 1px hairline border `rgba(255,255,255,0.07)`
- Text primary:         `#EEF1F4`
- Text secondary:       `#969CA6`
- **Accent (the ONE vivid): electric cyan `#1FE3C6`** — for key words, rules, ticks, index numerals, glows, data highlights.
- Accent glow:          cyan at low alpha, e.g. `box-shadow: 0 0 40px rgba(31,227,198,0.35)`, `text-shadow: 0 0 24px rgba(31,227,198,0.5)`
- Over-video scrim:     dark charcoal gradient (so light text reads on the bright talking-head shot)
- Book cover keeps its own colors — never recolor.

## Depth & lighting (this is what makes it "premium" — do not skip)
- Backgrounds are **radial, not flat**: lighter core `#1C1E26` → `#0C0D11` edges, plus a subtle vignette.
- Cards/panels get a soft outer shadow + the hairline border + an optional faint inner top highlight.
- Hero elements get a soft radial cyan glow behind them.
- Use a **light sweep** (a moving linear-gradient highlight) across panels/headlines on entrance.
- Optional very-subtle grain. Keep all of this restrained — depth, not noise.

## Typography
- **Headlines/display: `Inter` 800–900** (black/bold), tight tracking (`-0.02em`), large. `WEB4` is Inter Black (matches the book cover wordmark).
- Labels/eyebrows: `Inter` 600, small-caps, `letter-spacing: 0.18em`, uppercase, secondary color.
- Numerals: `Inter`, `font-variant-numeric: tabular-nums`. Big stats can hit 120–200px with a cyan glow.
- Scale (1080p): hero 120–200px · section 64–88px · key-point headline 52–66px · eyebrow 26–30px · body 28–34px. Never <24px.
- (No serif — that was the old look.)

## Motion (cinematic, weighty)
- Eases: `expo.out`, `power4.out`, `power3.out`, `power2.inOut`, `power2.in` (exits). NO back/elastic/bounce/spin.
- Reveals 0.7–1.1s, confident and slightly slow. Masked **clip-path wipes**, **light sweeps**, accent **glow build-ups**, **count-ups**, subtle scale/parallax for depth. Headlines can reveal letter-grouped or masked.
- Over a continuous video, each overlay animates IN at its start and OUT before its end (entrance `gsap.from`, exit `gsap.to`). Hold values generous.

## Lean on real Hyperframes templates (install via `npx hyperframes add`)
Use and restyle these to the palette above rather than hand-rolling:
- `apple-money-count` / `data-chart` — the "$ trillions" hook and the AI-tier / "$10–30M" stats.
- `caption-kinetic-slam` (and `caption-*`) — the hook lines and pull-quotes.
- `flowchart` — centralized → money/greed → AI.
- `transitions-*` — between beats.
Pack MORE beats in than before (the 5 min felt under-graphic'd).

## Book intro = split-screen (keep it — it tested well)
Charcoal bg. **Left:** the 3D book cover (with cyan glow + light sweep) + `WEB4` (Inter Black) + subtitle + cyan rule + tabular `#1 / #11` stats. **Right:** a **live video panel of Anndy speaking** (the source video, framed in a rounded panel with the hairline border + soft glow). Title text never overlaps the face.

## What NOT to do
- No cream/ivory/white backgrounds. No flat fills (use radial depth + glow). No serif body. More than ONE accent. No bounce/spin. No covering the speaker's face on body beats.
