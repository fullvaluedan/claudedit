# DESIGN.md — Video Design System
# claudedit / Cole Kennelly · Volmex Labs
# Version: 1.0 — Commit to repo root and attach to every HyperFrames session.

---

## 1. Identity

| Field | Value |
|---|---|
| Speaker | Cole Kennelly — always the primary subject on screen |
| Channel | Volmex Labs |
| Brand voice | Direct, analytical, no filler — crypto volatility derivatives |
| Primary platform | YouTube (16:9 landscape, 1920×1080, 30fps) |
| Secondary platform | LinkedIn / Twitter clips (same master, recut) |

---

## 2. Color Palette

> These are the ONLY colors permitted. No per-scene invention. No gradients unless listed.

| Role | Hex | Usage |
|---|---|---|
| Background | `#0A0A0A` | All full-bleed backgrounds |
| Surface | `#141A22` | Cards, panels, containers |
| Border | `#2A2A2A` | Dividers, grid lines |
| Foreground | `#F0F0F0` | Primary body text |
| Foreground Muted | `#888888` | Labels, secondary text |
| Accent | `#00D4FF` | Data callouts, underlines, highlights — sparingly |
| Accent Muted | `rgba(0,212,255,0.15)` | Backgrounds behind accent content only |
| White | `#FFFFFF` | Headlines only |
| Positive | `#16C784` | Up / gain / positive delta |
| Negative | `#FF4D4F` | Down / loss / negative delta |

**Hard rules:**
- No blue-to-purple gradients (AI default — forbidden)
- No drop shadows on text
- No semi-transparent overlays except captions bar (max 70% opacity black)
- Accent appears on ONE element per composition, never more

---

## 3. Typography

| Role | Font | Weight | Size (1080p) | Max line length |
|---|---|---|---|---|
| Display / Headline | Inter Display | 800 (ExtraBold) | 80–120px | 3 words |
| Subheading | Inter | 600 (SemiBold) | 48–60px | 6 words |
| Body / Captions | Inter | 400 (Regular) | 32–40px | 8 words |
| Data / Numbers | Inter | 700 (Bold) | 60–100px | numeric only |
| Labels / Source | JetBrains Mono | 400 | 24–28px | 4 words |

**Google Fonts import:**
```
https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap
```

**Hard rules:**
- No decorative or serif fonts
- No italic unless quoting
- No all-caps except eyebrow labels
- Letter-spacing on headlines: -0.02em
- Letter-spacing on eyebrow labels: +0.18em uppercase
- Line height: 1.1 for headlines, 1.4 for body

---

## 4. Layout Grid

- **Format:** 12-column, 8px base unit
- **Canvas:** 1920×1080 (landscape)
- **Margins:** 96px left/right, 80px top/bottom
- **Column gutter:** 24px
- **Safe area:** 90% of frame — nothing outside this zone

### Speaker Video Rules (CRITICAL)
- Speaker video is **always** top-left OR full-bleed — NEVER a corner pip unless explicitly requested
- Speaker face must **never** be obscured by graphics or text
- If speaker and graphics coexist: speaker occupies left 60%, graphics right 40%
- Graphics appear **beside or below** the speaker — never overlapping

### Standard overlay zones
```
lower-third:   x=96, y=880, w=860, h=120   (bottom-left, 8% from bottom)
stat-callout:  x=1060, y=80, w=760, h=340   (right panel)
eyebrow:       y=80, above hero zone
hero:          x=96, y=280, w=1728, h=520   (full-width center)
```

---

## 5. Animation Principles

- **Engine:** GSAP timeline only (paused, deterministic) — no `setTimeout`, `setInterval`, `requestAnimationFrame`
- **Entry easing:** `power2.out` for slides, `power3.out` for number counters
- **Exit easing:** `power2.in`
- **Standard entry duration:** 0.4s
- **Standard exit duration:** 0.3s
- **Hold time:** minimum 1.5s between entry and exit
- Counter ramp: 1.4s for large numbers
- Stagger on lists: 80ms between items
- No bouncing, spinning, rotating, or zooming text
- No particle bursts, lens flares, 3D extrudes, neon glows

---

## 6. Template Selection Guide

> Always pick the MOST APPROPRIATE template. Default to `swiss-grid` for talking-head content.

| Template | When to use | When NOT to use |
|---|---|---|
| `warm-grain` | Personal story, editorial feel | Data-heavy content, crypto topics |
| `play-mode` | Social hooks, high-retention short clips | Long-form, serious finance topics |
| `swiss-grid` | **Default.** Data, interviews, explainers, lower thirds | Emotional/lifestyle content |
| `kinetic-type` | Section intros, title cards, dramatic quote reveals | Full compositions |
| `decision-tree` | Step-by-step breakdowns, comparisons, process flows | No clear branching structure |
| `product-promo` | Tool demos, protocol walkthroughs | Talking-head content |
| `nyt-graph` | Charts, data stories, trend lines, vol history | Non-quantitative content |
| `vignelli` | Portrait format announcements, quote pulls | Landscape format |
| `blank` | Custom layouts with no predefined style | Anything where a template fits |

---

## 7. Caption Rules

- Position: bottom-left, 8% from bottom, within left margin
- Max 2 lines at a time
- White text, no stroke
- Background: semi-transparent black bar, 70% opacity, 8px border radius
- Padding: 12px horizontal, 8px vertical
- Font: Inter 400, 36px

---

## 8. What NOT to Do — Anti-Patterns

These are checked by the QA agent before every render. Violations block output.

- ❌ Stock footage or images of people who are not Cole Kennelly
- ❌ Invented statistics or text not provided in the brief
- ❌ Placeholder text ("Lorem ipsum", "Title here", "Your text", etc.)
- ❌ Default AI gradients (blue→purple, teal→blue, etc.)
- ❌ Random accent colors — only `#00D4FF`
- ❌ Cole's face obscured by any overlay
- ❌ Wall-clock JS animations (setTimeout, rAF — breaks deterministic render)
- ❌ Music unless explicitly requested with a file path
- ❌ Rendering at non-standard resolution/fps without explicit instruction
- ❌ Multiple typefaces in one composition
- ❌ More than 3 animated elements entering simultaneously
- ❌ Text smaller than 24px at 1080p (unreadable on mobile)
- ❌ Price tickers (distraction, no editorial value)
- ❌ Full-frame overlays that hide Cole (lower-third zone only for overlays)
