comp t=167.8

**Beat c8b13 — clean video, Mode A (2s)**
- Mode A. Comp t=168–170. Clip ends cleanly.

**FINAL BEAT MAP for Clip 8:**

| Beat ID | Comp t | Src t | Template | Speaker mode | Sub-comp |
|---------|--------|-------|----------|-------------|----------|
| c8b1 | 0.0–3.0s | 1675–1678s | kinetic-type (hook) | Mode A | beat-c8b1-hook.html |
| c8b2 | 3.0–5.0s | 1678–1680s | clean video | Mode A | — |
| c8b3 | 5.0–12.0s | 1680–1687s | kinetic-type | full-frame | beat-c8b3-work-team.html |
| c8b4 | 12.0–26.0s | 1687–1701s | swiss-grid | Mode A | beat-c8b4-productivity.html |
| c8b5 | 26.0–44.0s | 1701–1719s | liquid-glass | Mode A | beat-c8b5-jasper-research.html |
| c8b6 | 44.0–56.0s | 1719–1731s | clean video | Mode A | — |
| c8b7 | 56.0–76.0s | 1731–1751s | decision-tree | Mode A | beat-c8b7-pipeline.html |
| c8b8 | 76.0–96.0s | 1751–1771s | kinetic-type (editorial) | full-frame | beat-c8b8-night-day.html |
| c8b9 | 96.0–118.0s | 1771–1793s | swiss-grid | Mode A | beat-c8b9-intent-agents.html |
| c8b10 | 118.0–132.0s | 1793–1807s | decision-tree | Mode A | beat-c8b10-agent-viable.html |
| c8b11 | 132.0–155.0s | 1807–1830s | kinetic-type | full-frame | beat-c8b11-blue-wave.html |
| c8b12 | 155.0–168.0s | 1830–1843s | liquid-glass | Mode A | beat-c8b12-jasper-close.html |
| c8b13 | 168.0–170.0s | 1843–1845s | clean video | Mode A | — |

Template sequence: kinetic → clean → kinetic → swiss-grid → liquid-glass → clean → decision-tree → kinetic → swiss-grid → decision-tree → kinetic → liquid-glass → clean. No consecutive duplicates. PASS.

**Beat c8b11 word-sync (final verified):**
- Line 1: "BLUE WAVE" @ comp 132.70 (src 1807.70, verified)
- Line 2: "STRAIT OF HORMUZ" @ comp 136.44 (src 1811.44, verified)
- Line 3: "SHORT OIL" @ comp 140.68 (src 1815.68, verified)
- Line 3 cyan payoff

**QA pre-check c8:** 13 beats for 170s clip (≥8 required). Full-frame: c8b3, c8b8, c8b11. c8b8 labeled editorial. c8b11 word-sync verified — all three lines correct. Major timing errors from original EDL fully corrected (c8b7 was off by 47s, now correct at comp 132.70). No outro — c8b12 is a name-card, not a CTA. PASS all criteria.

**Build Manifest Row:** `clip_8 | clip-8-ai-multiplier | 1675 | 1845 | kinetic-type | 13 beats`

---

## CROSS-CLIP BUILDER NOTES

**Word-sync computation rule (canonical):** `comp_t = src_t - clip_src_in`. Never deviate. If a word timestamp produces a comp_t that falls outside the beat's comp range, the beat boundary must move to accommodate the word — do not change the comp_t to fit the beat.

**Full-frame transition GSAP (copy from clip-2-altcoin-options/index.html):**
```js
// Enter full-frame
masterTL.to(videoEl, { left:0, top:0, width:1920, height:1080, borderRadius:"0px", duration:0.4, ease:"expo.inOut" });
masterTL.to([gradientRule, zoneRule], { opacity:0, duration:0.3 }, "<");
// Return to Mode A
masterTL.to(videoEl, { left:1152, top:0, width:768, height:1080, duration:0.4, ease:"expo.inOut" });
masterTL.to([gradientRule, zoneRule], { opacity:1, duration:0.3 }, "<");
```

**Liquid glass CSS (no blur):**
```css
background: rgba(20,26,34,0.92);
box-shadow: 0 0 40px rgba(0,212,255,0.10), 0 8px 40px rgba(0,0,0,0.65);
border: 1px solid rgba(255,255,255,0.07);
mask-image: linear-gradient(to right, black 82%, transparent 100%);
-webkit-mask-image: linear-gradient(to right, black 82%, transparent 100%);
/* NO backdrop-filter anywhere */
```

**Cyan discipline:** One `#00D4FF` element per beat. In kinetic beats = final payoff line only. In swiss-grid beats = horizontal rule only (stat in #F0F0F0). In liquid-glass = accent bar only. In decision-tree = final node only. In nyt-graph = final/target bar only. Builder must grep for `#00D4FF` and `color: cyan` in each sub-comp before render.

**Muted grey rule:** `#888888` permitted ONLY on text that is 48px or larger (column headers in swiss-grid at 48px). All other viewer-facing text uses `#F0F0F0`. "???" in clip 7 c7b2 is Inter 700 64px — use `#F0F0F0`.

**Editorial beats (not word-synced):** c1b1 hook, c3b1 hook, c3b10 close, c4b1 hook, c5b1 hook, c6b1 hook, c6b4 ETF flows, c7b1 hook, c7b4 ordinals-ai, c7b7 close, c8b1 hook, c8b8 night-day. These fire as thesis statements or callbacks. Label sub-comp `<!-- EDITORIAL: not word-synced -->` in the HTML comments so QA agents can distinguish from verified word-sync beats.

**Beat 1 (guest intro card) and beat 32 (outro) from edl.json excluded** from all 7 clips per DESIGN.md: "No intro cards. No outros."

---

## MASTER BUILD MANIFEST

| clip_id | dir_name | source_in | source_out | init_template | beat_count |
|---------|----------|-----------|------------|---------------|------------|
| clip_1 | clip-1-otc-model | 220 | 350 | kinetic-type | 10 |
| clip_3 | clip-3-structured-products | 700 | 810 | kinetic-type | 10 |
| clip_4 | clip-4-oct10-crash | 1010 | 1115 | kinetic-type | 8 |
| clip_5 | clip-5-capital-rotation | 1120 | 1300 | kinetic-type | 13 |
| clip_6 | clip-6-four-year-cycle | 1350 | 1470 | kinetic-type | 9 |
| clip_7 | clip-7-bear-market-exit | 1515 | 1600 | kinetic-type | 7 |
| clip_8 | clip-8-ai-multiplier | 1675 | 1845 | kinetic-type | 13 |
| **TOTAL** | | | | | **70 beats** |