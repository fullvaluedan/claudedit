# QA-CHECKLIST.md — Pre-Render Review Agent
# claudedit / [Your Channel Name]
# Version: 1.0

---

## INSTRUCTIONS FOR THE QA AGENT

You are the QA agent. Your job is to review a HyperFrames composition 
BEFORE it is rendered. You do not render. You do not make changes.
You verify, report, and either APPROVE or BLOCK.

**If ANY item marked [BLOCKING] fails → output "BLOCKED" and list all failures.**
**Do not suggest fixes — list failures only. The author agent fixes and resubmits.**

Items marked [WARN] are flagged but do not block render.
Items marked [INFO] are notes for the human reviewer.

Run this checklist against: the composition HTML file(s) and the brief that was given.

---

## SECTION 1 — IDENTITY (BLOCKING)

- [ ] [BLOCKING] Speaker in composition matches the actual speaker named in the brief
- [ ] [BLOCKING] No unidentified people, stock footage of strangers, or placeholder faces present
- [ ] [BLOCKING] All text content matches what was provided in the brief — nothing invented
- [ ] [BLOCKING] No placeholder text present ("Lorem ipsum", "Title here", "Your name", "Insert text", etc.)

---

## SECTION 2 — DESIGN SYSTEM COMPLIANCE (BLOCKING)

### Colors
- [ ] [BLOCKING] Only palette colors used: `#0A0A0A`, `#161616`, `#2A2A2A`, `#F0F0F0`, `#888888`, accent hex, white `#FFFFFF`
- [ ] [BLOCKING] No blue-to-purple gradients present
- [ ] [BLOCKING] No teal-to-blue gradients present
- [ ] [BLOCKING] No per-scene color invention — all colors traceable to DESIGN.md
- [ ] [BLOCKING] Accent color appears on ONE element max per composition

### Typography
- [ ] [BLOCKING] Only the brand font family used (no fallback decorative fonts rendered)
- [ ] [BLOCKING] No text smaller than 24px at 1080p resolution
- [ ] [BLOCKING] No italic text outside of quoted content
- [ ] [WARN] Headline line length exceeds 3 words (flag for human review)

### Layout
- [ ] [BLOCKING] All elements within 90% safe area (no content outside 96px margins)
- [ ] [BLOCKING] Speaker face not obscured by any text or graphic element
- [ ] [BLOCKING] If speaker + graphics coexist: speaker occupies left 60%, graphics right 40%
- [ ] [WARN] Any element appears free-floating (not aligned to 12-column grid)

---

## SECTION 3 — TEMPLATE USAGE (BLOCKING)

- [ ] [BLOCKING] The correct template was used for the content type (per DESIGN.md Section 6)
- [ ] [BLOCKING] Template is the intended one from the brief — not defaulted to a different one
- [ ] [WARN] `blank` template used when a named template would have been more appropriate

---

## SECTION 4 — ANIMATION COMPLIANCE (BLOCKING)

- [ ] [BLOCKING] No `setTimeout()` calls in any composition file
- [ ] [BLOCKING] No `setInterval()` calls in any composition file  
- [ ] [BLOCKING] No `requestAnimationFrame()` calls in any composition file
- [ ] [BLOCKING] All GSAP timelines are `{ paused: true }` on initialization
- [ ] [BLOCKING] All timelines registered to `window.__timelines`
- [ ] [WARN] More than 3 elements animating in simultaneously (review choreography)
- [ ] [WARN] Any spinning, rotating, or zooming text present

---

## SECTION 5 — TECHNICAL SPECS (BLOCKING)

- [ ] [BLOCKING] `data-width` = 1920 (landscape) or 1080 (portrait)
- [ ] [BLOCKING] `data-height` = 1080 (landscape) or 1920 (portrait)
- [ ] [BLOCKING] `data-fps` = 30
- [ ] [BLOCKING] `data-duration` matches the duration specified in the brief (±0.5s tolerance)
- [ ] [BLOCKING] `data-composition-id` is present on root element
- [ ] [BLOCKING] All asset paths are relative and point to files that exist in the project directory
- [ ] [BLOCKING] No absolute file paths (e.g. `/Users/...` or `C:\...`) in asset references

---

## SECTION 6 — CAPTION QUALITY (if captions present)

- [ ] [BLOCKING] Caption text exactly matches the provided transcript — no paraphrasing
- [ ] [BLOCKING] Max 2 lines per caption display
- [ ] [BLOCKING] Captions positioned bottom-left within safe area
- [ ] [BLOCKING] Caption background: semi-transparent dark bar (no solid white box)
- [ ] [WARN] Any caption line exceeds 8 words

---

## SECTION 7 — CONTENT ACCURACY (BLOCKING)

- [ ] [BLOCKING] All statistics/numbers match exactly what was in the brief
- [ ] [BLOCKING] All data points in charts/graphs match the data provided in the brief
- [ ] [BLOCKING] Source attribution present if data source was provided in brief
- [ ] [WARN] Source attribution missing when data type implies a source should exist

---

## SECTION 8 — AUDIO (BLOCKING)

- [ ] [BLOCKING] No music or audio added unless a file path was explicitly provided in the brief
- [ ] [BLOCKING] No TTS/voiceover generated unless explicitly requested

---

## SECTION 9 — HUMAN REVIEW NOTES (INFO)

These items are not auto-checkable. Flag for human to review:

- [ ] [INFO] Does the graphic actually support what the speaker is saying at that timestamp?
- [ ] [INFO] Is the animation timing appropriate for the content (not too fast/slow)?
- [ ] [INFO] Does the visual feel consistent with the previous compositions in this project?
- [ ] [INFO] Would a viewer understand the graphic without additional context?

---

## SIGN-OFF

```
QA Result: [ APPROVED / BLOCKED ]

Blocking failures (if any):
1. [Section X] — [Description of failure]
2. [Section X] — [Description of failure]

Warnings (non-blocking):
1. [Section X] — [Description]

Human review notes:
- [Any INFO items that need attention]

Reviewed: [timestamp]
```

**If APPROVED:** Hand off to render step: `npx hyperframes render`
**If BLOCKED:** Return to author agent with failure list. Do not render.

---

## SECTION 10 — FRAME COMPOSITION (BLOCKING)

*New section — added to catch the "tiny box in sea of black" failure mode.*

- [ ] [BLOCKING] SPEAKER_LAYOUT marker was read from sequence before composing graphic
- [ ] [BLOCKING] Graphic elements are placed in the correct zone for this layout (per FRAME-COMPOSITION.md)
- [ ] [BLOCKING] No graphic element is placed in the DANGER ZONE for this layout
- [ ] [BLOCKING] Speaker's face is not covered by any text, bar, or overlay element
- [ ] [BLOCKING] Graphic fills its zone — no element is smaller than 40% of its available zone width
- [ ] [BLOCKING] Hero stat / number is minimum 96px at 1080p
- [ ] [BLOCKING] All body text and labels are minimum 28px at 1080p
- [ ] [BLOCKING] Caption text is minimum 36px at 1080p
- [ ] [WARN] Source attribution text below 20px (flag but don't block)

---

## SECTION 11 — DATA GRAPHIC INTEGRITY (BLOCKING)

*Applies when graphic contains bars, charts, or numeric comparisons.*

- [ ] [BLOCKING] Bar heights are calculated using the formula from FRAME-COMPOSITION.md — not guessed
- [ ] [BLOCKING] The larger value has a visually larger bar — proportions are accurate
- [ ] [BLOCKING] No pie charts used — bars only for finance comparison content
- [ ] [BLOCKING] No 3D perspective applied to any chart
- [ ] [BLOCKING] No gradient fills on data bars — solid color only
- [ ] [BLOCKING] No drop shadows on chart elements
- [ ] [BLOCKING] Every bar has a readable label directly below it (minimum 28px)
- [ ] [BLOCKING] Data source is attributed in bottom-right corner if provided in brief
- [ ] [WARN] Difference between compared values is not visually obvious at a glance

---

## SECTION 12 — ANIMATION SMOOTHNESS (BLOCKING)

- [ ] [BLOCKING] Numbers count up from 0, not appear instantly
- [ ] [BLOCKING] Bars grow from bottom using power2.out easing — not pop in
- [ ] [BLOCKING] No bounce or elastic easing on any data element
- [ ] [BLOCKING] No spinning or rotating numbers
- [ ] [BLOCKING] Exit is a single simultaneous fade-out — not elements disappearing one by one
- [ ] [BLOCKING] Hold time after full entry is minimum 2.0s (3.0s for multi-bar charts)
- [ ] [WARN] Any animation feels too fast — entry under 0.4s for any element
- [ ] [WARN] Any animation feels too slow — entry over 1.5s for stat/number

---

## SECTION 13 — DEMO CONTENT PURGE (BLOCKING)

*The most important check. Catches the "HYPERFRAMES demo text showing" bug.*

- [ ] [BLOCKING] Ran `grep -rni "hyperframes\|survey findings\|the opportunity\|motion graphics\|percent of you\|design simplified\|lack editing\|3 of 4\|47%"` in the graphic folder
- [ ] [BLOCKING] The grep returned ZERO results — no demo content remains anywhere
- [ ] [BLOCKING] Opened and checked EVERY composition file, not just one
- [ ] [BLOCKING] Every scene either has my content or is deleted/disabled
- [ ] [BLOCKING] Preview (`npx hyperframes dev`) shows ONLY my content — no overlapping text, no demo strings
- [ ] [BLOCKING] No two text layers rendering on top of each other

If the grep returns ANY result → STOP. Do not render. Return to STEP 3c.

---

## SECTION 14 — SPEAKER FACE PROTECTION (BLOCKING)

*Catches stat cards landing on the speaker's face (images 2 & 3).*

- [ ] [BLOCKING] Read SPEAKER_LAYOUT before composing
- [ ] [BLOCKING] For two-person layout: graphic is in the CENTER gap or BOTTOM strip, never over either face
- [ ] [BLOCKING] For single offset: graphic is in the negative-space side, never over the face
- [ ] [BLOCKING] Graphic does not cover eyes, mouth, or any part of the active speaker's face
- [ ] [WARN] Graphic is close to a face edge — review whether it reads cleanly
