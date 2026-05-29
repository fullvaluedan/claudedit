# FRAME-COMPOSITION.md — Speaker-Aware Graphic Zones
# claudedit / [Your Channel Name]
# Version: 1.0
#
# This file tells the agent WHERE to place graphics relative to the speaker.
# Read this before composing any graphic. The wrong zone covers the speaker's face.
# Content style: Finance / crypto / data-heavy — structured, confident layouts.

---

## THE CORE PROBLEM THIS SOLVES

The example graphic failure (TRADFI INDEX COMPANIES bar chart) had:
- Data floating in dead center with massive black borders
- No relationship to where the speaker is or isn't
- No use of the full 1920×1080 canvas
- No visual hierarchy — title, data, and source all same visual weight

Every graphic must be composed for the FULL FRAME, not a safe little box in the middle.

---

## SPEAKER LAYOUT TYPES

Read the `SPEAKER_LAYOUT` marker set in PREMIERE-PLAYBOOK.md Sequence 2.
Then use the matching zone map below.

---

### LAYOUT A — Single Speaker, Center Frame
*Typical: webcam talking head, centered podcast setup*

```
┌─────────────────────────────────────────┐
│                                         │
│          ┌─────────────┐               │
│          │             │               │
│          │   SPEAKER   │               │
│          │   FACE IS   │               │
│          │    HERE     │               │
│          └─────────────┘               │
│                                         │
└─────────────────────────────────────────┘
```

**Overlay graphic zones (appear OVER footage):**
- Safe: Bottom 30% of frame (below chin)
- Safe: Top 10% of frame (above head)
- Danger: Center — never place text or graphics 25–75% vertically

**Full-bleed graphic approach:**
- Replace footage entirely for the graphic duration
- OR split screen: speaker left 50%, graphic right 50%
- NEVER overlay a full-bleed on a center-frame speaker

**Caption zone:** Bottom-left, 8% from bottom, within 96px left margin

---

### LAYOUT B — Single Speaker, Offset Left
*Typical: interview framing, speaker looks right into negative space*

```
┌─────────────────────────────────────────┐
│                                         │
│  ┌──────────┐                          │
│  │          │   ← NEGATIVE SPACE →     │
│  │ SPEAKER  │   USE THIS FOR GRAPHICS  │
│  │  FACE    │                          │
│  └──────────┘                          │
│                                         │
└─────────────────────────────────────────┘
```

**Overlay graphic zones:**
- Primary: Right 45% of frame (columns 7–12 of 12-column grid)
- Safe: Bottom 25% full width
- Danger: Left 40% — speaker is here

**Stat callout position:** Right side, vertically centered, 960px–1824px horizontal
**Lower third position:** Bottom-left (standard) OR bottom-right if speaker is left

**Full-bleed graphic approach:**
- Split screen works naturally — speaker already left, data goes right
- Preferred for data-heavy content: keep speaker in left 45%, data fills right 55%

---

### LAYOUT C — Single Speaker, Offset Right
*Mirror of Layout B — speaker looks left*

```
┌─────────────────────────────────────────┐
│                                         │
│    ← NEGATIVE SPACE →  ┌──────────┐   │
│    USE THIS FOR GRAPHICS│          │   │
│                         │ SPEAKER  │   │
│                         │  FACE    │   │
│                         └──────────┘   │
│                                         │
└─────────────────────────────────────────┘
```

**Overlay graphic zones:**
- Primary: Left 45% of frame (columns 1–5 of 12-column grid)
- Safe: Bottom 25% full width
- Danger: Right 40% — speaker is here

**Stat callout position:** Left side, vertically centered, 96px–864px horizontal

---

### LAYOUT D — Two People on Screen
*Interview, co-host, dual camera*

```
┌─────────────────────────────────────────┐
│                                         │
│  ┌──────────┐         ┌──────────┐    │
│  │          │         │          │    │
│  │ SPEAKER A│         │ SPEAKER B│    │
│  │          │         │          │    │
│  └──────────┘         └──────────┘    │
│                                         │
└─────────────────────────────────────────┘
```

**Overlay graphic zones:**
- Primary: Bottom 25% full width (safe for both speakers)
- Safe: Center top strip (above both heads, top 10%)
- Danger: Middle 60% vertically — both faces are here

**Full-bleed graphic approach:**
- Always replace footage — do not split-screen with two speakers
- Use kinetic-type or swiss-grid full-bleed, cut back to both speakers after

**Lower thirds (two-person):**
- Speaker A: Bottom-left, 8% from bottom
- Speaker B: Bottom-right, 8% from bottom
- Don't show both simultaneously — show each when that speaker is talking

---

## GRAPHIC SIZE RULES — NO MORE TINY BOXES

This is the fix for the TRADFI example. Every graphic must fill its zone confidently.

### Stat Callout — Full Frame Treatment
```
WRONG (what the example does):
  Small bars centered in a sea of black
  Title is 14px all-caps spacing
  Numbers are medium weight

RIGHT:
  Background: full bleed #0A0A0A (not a floating card)
  Stat number: 120–160px, ExtraBold, fills top 40% of frame
  Context label: 40px below the number
  Comparison bars: full width 1680px, height proportional to data
  Bar labels: 32px, directly below each bar
  Source: 24px, bottom-right corner, muted color
  
  If comparing two values:
    Larger value → accent color, larger bar
    Smaller value → #888888, shorter bar
    Scale to make the difference VISIBLE — 10% difference should look like 10%, not 1px
```

### Bar Chart Sizing Formula
```
Canvas width for data area: 1728px (1920 - 2×96px margins)
Number of bars: N
Bar width: MIN(300px, (1728 - (N-1)×48px) / N)
Gap between bars: 48px
Bar height (max): 480px (top bar at peak value)
Bar height (other): proportional — (value/max_value) × 480px
Minimum bar height: 24px (even tiny values need to be visible)
```

### Text Hierarchy — Finance Content
```
Tier 1 — The Number (what the viewer remembers)
  Size: 96–160px | Weight: 800 | Color: accent OR white
  One per graphic. This is the hero.

Tier 2 — The Context (what the number means)
  Size: 40–52px | Weight: 600 | Color: #F0F0F0
  One or two lines max.

Tier 3 — The Label (what the category is)
  Size: 28–36px | Weight: 400 | Color: #888888
  Under each bar or data point.

Tier 4 — The Source (attribution)
  Size: 20–24px | Weight: 400 | Color: #555555
  Bottom-right corner only. Not centered.

Rule: Every tier must be visually distinct from the others.
If Tier 1 and Tier 2 look similar in size → Tier 1 is too small.
```

---

## ANIMATION RULES — FINANCE CONTENT

Smooth, confident, no gimmicks. Data should feel authoritative, not flashy.

### Entry Animations (what comes in)
```
Numbers / stats:
  Count up from 0 to final value over 0.8s
  Easing: power2.out
  
Bars:
  Grow from bottom (height 0 → final height) over 0.6s
  Easing: power2.out
  Stagger: 0.15s between each bar (left to right)
  
Text labels:
  Fade in 0.2s after their bar reaches full height
  
Comparison accent (larger bar highlight):
  Color transition from #888 → accent over 0.3s, after bar is full height

Background / card:
  Fade in 0.3s, before any data elements
```

### Hold Times
```
After all elements have entered: hold minimum 2.0s
For charts with multiple bars: hold minimum 3.0s
For decision trees: hold 1.5s per node after it appears
```

### Exit Animations
```
Fade out all elements simultaneously over 0.4s
Do NOT exit elements one-by-one — it looks cheap
```

### What NEVER to do in finance graphics
```
❌ Bounce or elastic easing on data
❌ Spinning numbers
❌ Particle effects on charts
❌ Color changes on hover (video, not web)
❌ Drop shadows on bars
❌ 3D perspective on bar charts (distorts data perception)
❌ Pie charts (always use bars for comparison)
❌ Gradients on data bars (solid color only)
```

---

## READABILITY AT PLAYBACK SIZE

Finance content gets watched on phones. Test against this:

```
Minimum readable size at 1080p (also legible on mobile):
  Body text / labels: 28px minimum
  Captions: 36px minimum  
  Data numbers: 72px minimum for secondary, 96px for hero stat
  Source attribution: 20px minimum (can be smaller — it's fine print)

Minimum contrast ratio:
  White text on #0A0A0A background: passes easily ✓
  #888888 text on #0A0A0A: passes AA ✓
  Accent color text on #0A0A0A: VERIFY — must be light enough
    If accent is dark (e.g. dark orange), use lighter tint for text version

Line length:
  Max 8 words per line for body text
  Max 4 words for headline / tier 1 context
  Numbers: single value per line
```

---

## B-ROLL COMPOSITION CHECK

Before placing any B-roll on V2, verify:

```
□ B-roll subject is relevant to what speaker is saying at that moment
□ B-roll does not show competing faces (people who aren't the speaker)
□ B-roll duration is 5–10 seconds (see PREMIERE-PLAYBOOK.md Sequence 7)
□ Speaker audio continues under B-roll (don't cut audio)
□ B-roll color grade roughly matches A-roll (check skin tone / exposure)
□ No motion blur that looks like a recording artifact
□ No watermarks, logos, or third-party branding visible
```

---

## QUICK ZONE REFERENCE

```
LAYOUT          GRAPHIC ZONE                  DANGER ZONE
─────────────────────────────────────────────────────────
Center frame    Bottom 30% or full-bleed      Middle 50% vertically
Offset left     Right 45% or bottom 25%       Left 40%
Offset right    Left 45% or bottom 25%        Right 40%
Two people      Bottom 25% or full-bleed      Middle 60% vertically
```
