# DESIGN.md — Video Design System
# claudedit / [Your Channel Name]
# Version: 1.0 — Commit to repo root and attach to every HyperFrames session.

---

## 1. Identity

| Field | Value |
|---|---|
| Speaker | [YOUR NAME] — always the primary subject on screen |
| Channel | [YOUR CHANNEL NAME] |
| Brand voice | Direct, analytical, no filler |
| Primary platform | YouTube (16:9 landscape, 1920×1080, 30fps) |
| Secondary platform | LinkedIn / Twitter clips (same master, recut) |

---

## 2. Color Palette

> These are the ONLY colors permitted. No per-scene invention. No gradients unless listed.

| Role | Hex | Usage |
|---|---|---|
| Background | `#0A0A0A` | All full-bleed backgrounds |
| Surface | `#161616` | Cards, panels, containers |
| Border | `#2A2A2A` | Dividers, grid lines |
| Foreground | `#F0F0F0` | Primary body text |
| Foreground Muted | `#888888` | Labels, secondary text |
| Accent | `#[YOUR ACCENT]` | Data callouts, underlines, highlights — sparingly |
| Accent Muted | `#[YOUR ACCENT at 40% opacity]` | Backgrounds behind accent content only |
| White | `#FFFFFF` | Headlines only |
| Danger/Red | — | Not used unless data requires it |

**Hard rules:**
- No blue-to-purple gradients (AI default — forbidden)
- No drop shadows on text
- No semi-transparent overlays except captions bar (max 70% opacity black)
- Accent appears on ONE element per composition, never more

---

## 3. Typography

| Role | Font | Weight | Size (1080p) | Max line length |
|---|---|---|---|---|
| Display / Headline | [YOUR FONT, e.g. Inter] | 800 (ExtraBold) | 80–120px | 3 words |
| Subheading | Same | 600 (SemiBold) | 48–60px | 6 words |
| Body / Captions | Same | 400 (Regular) | 32–40px | 8 words |
| Data / Numbers | Same | 700 (Bold) | 60–100px | numeric only |
| Labels | Same | 500 (Medium) | 24–28px | 4 words |

**Hard rules:**
- No decorative or serif fonts
- No italic unless quoting
- No all-caps except display headlines
- Letter-spacing on headlines: +0.02em max
- Line height: 1.15 for headlines, 1.5 for body

---

## 4. Layout Grid

- **Format:** 12-column, 8px base unit
- **Canvas:** 1920×1080 (landscape), 1080×1920 (portrait, vignelli only)
- **Margins:** 96px left/right, 80px top/bottom
- **Column gutter:** 24px
- **Safe area:** 90% of frame — nothing outside this zone

### Speaker Video Rules (CRITICAL)
- Speaker video is **always** top-left OR full-bleed — NEVER a corner pip unless explicitly requested
- Speaker face must **never** be obscured by graphics or text
- If speaker and graphics coexist: speaker occupies left 60%, graphics right 40%
- Graphics appear **beside or below** the speaker — never overlapping

---

## 5. Animation Principles

- **Engine:** GSAP timeline only (paused, deterministic) — no `setTimeout`, `setInterval`, `requestAnimationFrame`
- **Entry easing:** `power2.out` for slides, `back.out(1.2)` for elastic (play-mode only)
- **Exit easing:** `power2.in`
- **Standard entry duration:** 0.4s
- **Standard exit duration:** 0.3s
- **Hold time:** minimum 1.5s between entry and exit
- No bouncing unless using play-mode template
- No spinning, rotating, or zooming text

---

## 6. Template Selection Guide

> Always pick the MOST APPROPRIATE template. Default to `swiss-grid` for talking-head content.

| Template | When to use | When NOT to use |
|---|---|---|
| `warm-grain` | Lifestyle, personal story, editorial feel | Data-heavy content, corporate topics |
| `play-mode` | Social hooks, product energy, high-retention short clips | Long-form, serious topics |
| `swiss-grid` | **Default.** Corporate, data, interviews, explainers | Emotional/lifestyle content |
| `kinetic-type` | Section intros, title cards, dramatic quote reveals | Full compositions — use as inserts only |
| `decision-tree` | Step-by-step breakdowns, comparisons, process flows | Anything without a clear branching structure |
| `product-promo` | Demos, feature showcases, SaaS walkthroughs | Personal/talking-head content |
| `nyt-graph` | Charts, data stories, trend lines, stats | Non-quantitative content |
| `vignelli` | Portrait format announcements, quote pulls, bold statements | Landscape format |
| `blank` | Custom agent-generated layouts with no predefined style | Anything where a template fits |

---

## 7. Caption Rules

- Position: bottom-left, 8% from bottom, within left margin
- Max 2 lines at a time
- White text, no stroke
- Background: semi-transparent black bar, 70% opacity, 8px border radius
- Padding: 12px horizontal, 8px vertical
- Always use `captions.html` sub-composition from template
- Font: body weight (400), 36px

---

## 8. What NOT to Do — Anti-Patterns

These are checked by the QA agent before every render. Violations block output.

- ❌ Stock footage or images of people who are not the speaker
- ❌ Invented statistics or text not provided in the brief
- ❌ Placeholder text ("Lorem ipsum", "Title here", "Your text", etc.)
- ❌ Default AI gradients (blue→purple, teal→blue, etc.)
- ❌ Random accent colors — only the palette accent hex
- ❌ Speaker face obscured by any overlay
- ❌ Wall-clock JS animations (setTimeout, rAF — breaks deterministic render)
- ❌ Music unless explicitly requested with a file path
- ❌ Rendering at non-standard resolution/fps without explicit instruction
- ❌ Multiple typefaces in one composition
- ❌ More than 3 animated elements entering simultaneously
- ❌ Text smaller than 24px at 1080p (unreadable on mobile)
