# Clip 6 — Four-Year Cycle Dead? — v2 EDL (RE-DESIGN)

**Why v2:** v1 FAILED review for (1) opening kinetic ("4-YEAR CYCLE / IS IT / DEAD?") was ANTICIPATORY/editorial and did NOT match the spoken dialog at t=0 (the in-point was src 1350, mid-ETF-flow thought; the host doesn't ask the question until v1-comp 71); (2) repetitive/formulaic structure (open stat-grid + two swiss-grids + decision-tree loop + 4 kinetics over 120s); (3) framing. v2 fixes all three: opens ON the real spoken host question, is CHART-LED (the halving decay chart is the hero), and verifies Jasper's framing from source frames.

---

## NEW IN/OUT (RULE 1 — open on a real line)

| | value | note |
|---|---|---|
| **src_in** | **1420.30** | ~0.12s before the host's "Would" (src 1420.42). Trims the trailing "Yeah." (Jasper, src 1419.74) at the head. |
| **src_out** | **1471.00** | After Jasper's kicker "...still a very strong narrative, I think" (ends src ~1469.6) + ~1.4s clean breath. Cuts BEFORE the host's topic pivot ("Interesting / And lots of crypto insiders..." src 1471.24+). |
| **duration** | **50.70s** | (was 120s — the old window's pre-question ETF-flow material 1350–1420 was the source of the formulaic repetition; cut it.) |
| **comp basis** | **comp = src − 1420.30** | every kinetic fire-time below is read off this. |

**Opening line (RULE 1):** the clip opens on the HOST question **"Would you say the four year cycle is dead?"** — a complete, self-contained line spoken in the first 2.02s. The opening kinetic IS that question, word-synced (NOT anticipatory). This is the clip's title line and it lands immediately. (DESIGN.md permits a host question as its own word-stack with no "HOST" label.)

**LEAD DEVICE (RULE 2 — chart-led):** the **halving block-reward decay chart** (`nyt-graph`) is the hero (c6b4, comp 24.0–41.0). Descending bars 50 → 25 → 12.5 → 6.25 → 3.125 → **1.56** BTC (2028 = cyan, near-zero), timed so the bars collapse exactly as Jasper says **"block rewards half to a point where it doesn't even matter."** Everything else in the clip orbits this one chart. NO opening swiss-grid stat-grid; NO duplicate stat beats; NO decision-tree loop. This makes clip 6 visually distinct from its siblings (it is the series' one chart beat).

---

## FRAMING (RULE 3 — verified from source frames)

**Layout (verified):** clean side-by-side. Nic (host) LEFT half (centered), Jasper (guest) RIGHT half (centered). Frame 1920×1080, 30fps. Jasper's face center ≈ x:1400 (≈73% horizontal); eyes ≈ 25% from top; his name lower-third "Jasper De Maere / Wintermute" sits bottom of the right half.

**Frames extracted & viewed** (these are this clip's actual Mode-A source moments):
- `src 1430` (comp 9.7, Jasper answering "...it is") — Jasper centered in right half, name lower-third visible.
- `src 1445` (comp 24.7, "the four year cycle...") — same, stable head position.
- `src 1455` (comp 34.7, chart underlay "entire dynamic with miners") — same; hand gestures enter lower-right but head stays put.
- `src 1463` (comp 42.7, "whether miners are selling") — same.
Command used: `ffmpeg -nostdin -ss <src_t> -i .../clip-6-four-year-cycle/source.mp4 -frames:v 1 /tmp/fr_c6_<t>.png -y` (source.mp4 → full episode, so `-ss src_t` is the correct frame).

**Mode-A crop test** (cover, scaled to 614×864 → visible source width 767.5px, horizontal overflow 1152px). Rendered & viewed object-position 80% / 83% / 86%:
- 80% (source x:922–1690): face leans slightly RIGHT of center.
- **83% (source x:956–1724): face well-centered, both eyes balanced, name lower-third fully in-frame, seam/Nic excluded. CLEANEST.**
- 86% (source x:991–1759): face pushed LEFT of center.

**CHOSEN: `object-position: 83% center`** (matches clip-2's correct value; v1 also had 83% but its OTHER failures masked it). **No vertical bias, no extra scale-up:** there is mild ceiling/wall headroom above Jasper but it is tasteful, and Mode A's `top:108` already gives 108px top clearance + 108px bottom clearance, so the name never clips. A vertical shift would push his chin/name toward the edge for no gain. Static camera (head fixed) → **Mode A** is correct (not Mode B).

**Mode A geometry (copy clip-2):** `{ left: 1229, top: 108, width: 614, height: 864 }`, `borderRadius: 6px`, entry `expo.inOut` 0.7s, glow + zone-rule fade/draw on arrival.

---

## STRUCTURE (RULE 2 — varied, NOT the formulaic open)

Template sequence: **kinetic(host Q) → Mode-A eyebrow+kinetic → kinetic → nyt-graph(HERO) → kinetic → kinetic**.
- The opening is NOT the "0N / EYEBROW / STAT / tag-row" swiss-grid every sibling used. There is **no swiss-grid stat block anywhere** in this clip.
- The 3+-element-types-in-6s rule (DESIGN.md) is met by: host-Q kinetic (type 1, full-frame both speakers, t=0–3) → at t≈3 video → Mode A with monospace index "06" (type 2) + eyebrow "FOUR-YEAR CYCLE" + cyan **rule draw** (type 3) + Jasper's answer **kinetic** building (type 4). Four distinct element types, none of them the cookie-cutter stat-grid.
- Only adjacency: c6b5 (kinetic) → c6b6 (kinetic) — back-to-back spoken phrases ("I don't think it really matters..." → "but it is still a very strong narrative") delivered as ONE continuous closing movement over a single uninterrupted full-frame hold (comp ~41→50.7, no Mode-A return between them). Distinct sub-comps, distinct content, both word-locked. If the QA gate demands hard alternation, merge into one 6-line closing kinetic (collapses 6→5 beats).

---

## BEAT MAP

| Beat | comp range | src range | Template / block | Speaker mode | Sub-comp file |
|------|-----------|-----------|------------------|--------------|---------------|
| c6b1 | 0.0–3.0 | 1420.30–1423.30 | `kinetic-type` (host question) | full-frame (both) | `beat-c6b1-host-cycle-dead.html` |
| c6b2 | 3.0–14.5 | 1423.30–1434.80 | Mode-A eyebrow/index + `kinetic-type` (answer) | Mode A | `beat-c6b2-was-dead-it-is.html` |
| c6b3 | 14.5–24.0 | 1434.80–1444.30 | `kinetic-type` | full-frame (both) | `beat-c6b3-self-fulfilling.html` |
| **c6b4** | **24.0–41.0** | **1444.30–1461.30** | **`nyt-graph` (halving block-reward decay) — HERO** | Mode A | `beat-c6b4-halving-decay.html` |
| c6b5 | 41.0–46.5 | 1461.30–1466.80 | `kinetic-type` | full-frame (both) | `beat-c6b5-doesnt-matter.html` |
| c6b6 | 46.5–50.7 | 1466.80–1471.00 | `kinetic-type` (kicker) → clean tail | full-frame (both) | `beat-c6b6-strong-narrative.html` |

**Catalog blocks considered (RULE 2):** the HERO uses the project's existing `nyt-graph` pattern (descending bar chart, `scaleY` bottom-up draw, cyan target bar) — already proven in v1's `beat-c6b3-halving-decay.html`, reuse it with the timing below. Kinetic beats use the `kinetic-type` phrase-build (line-by-line, phrases STAY, no dim — MEMORY rule). No `caption-kinetic-slam`/`apple-money-count` needed; the chart + word-synced phrase builds carry the variety and avoid a second stat-grid.

---

## BEAT DETAIL (every kinetic line: on-screen text + transcript words it matches + comp_t)

### c6b1 — kinetic-type (HOST QUESTION) · full-frame · comp 0.0–3.0
**Sub-comp:** `beat-c6b1-host-cycle-dead.html`
`<!-- WORD-SYNCED (not editorial). The cold open IS the spoken host question. No "HOST" label per DESIGN.md. -->`
Full-frame video, BOTH speakers visible, dark left-zone gradient backdrop. 3-phrase build, Inter 900 ~118–130px, each phrase STAYS (no dim). Exit upward (`power2.in`) ~2.7s before c6b2.
- LINE 1 **"WOULD YOU SAY"** — fires **comp 0.12** — matches *"Would"* (src 1420.42, "you" 1420.72, "say" 1420.84) — `#F0F0F0`
- LINE 2 **"THE FOUR-YEAR CYCLE"** — fires **comp 0.94** — matches *"four"* (src 1421.24, "year" 1421.52, "cycle" 1421.70) — `#F0F0F0`
- LINE 3 **"IS DEAD?"** — fires **comp 2.02** — matches *"dead?"* (src 1422.32; "is" 1422.08) — `#00D4FF` (cyan payoff + glow)

Cyan element: LINE 3 only.

---

### c6b2 — Mode-A eyebrow/index + kinetic answer · Mode A · comp 3.0–14.5
**Sub-comp:** `beat-c6b2-was-dead-it-is.html`
At comp 3.0 GSAP shrinks video full→Mode A (`object-position:83%`); `#bg-glow` in @3.3, `#zone-rule` draw @3.4. Left-zone chrome + a compact answer kinetic. **NOT a swiss-grid stat block** — no big-number slam, no tag-row.
- Index **"06"** (JetBrains Mono, muted) + eyebrow **"FOUR-YEAR CYCLE"** (Inter 700, ≥32px, `#F0F0F0`) — slam **comp 3.0** (EDITORIAL chrome — structural label, not a sentence) `<!-- EDITORIAL label -->`
- Cyan **rule** draws (scaleX 0→1, `#00D4FF`) — **comp 3.4** (EDITORIAL)
- Kinetic answer (2 phrase lines, Inter 900 ~92px, left zone, phrases STAY):
  - LINE 1 **"THOUGHT IT WAS DEAD"** — fires **comp 9.02** — matches *"was"* (src 1429.32) / *"dead,"* (src 1429.54); lead-in "thinking that it was dead" ("thinking" 1428.36) — `#F0F0F0`
  - LINE 2 **"NOW… IT IS"** — fires **comp 13.16** — matches *"is."* (src 1433.46) in "the way it's currently playing out, like it is." — `#00D4FF` (cyan payoff)

Cyan element: the rule fades when the kinetic LINE 2 cyan arrives, OR (cleaner) keep the rule neutral `#2a2a2a` after its draw and let LINE 2 "IT IS" be the single cyan. **Decision: rule draws cyan briefly then settles to `#2a2a2a`; LINE 2 is the beat's persistent cyan** (one cyan visible at a time).
Window 3.0–14.5 covers fires 9.02 / 13.16 with headroom; the early chrome (3.0–3.4) fills the 3–9 stretch with the eyebrow/rule + Jasper's "I've been going on record multiple times" so it isn't dead air.

---

### c6b3 — kinetic-type · full-frame · comp 14.5–24.0
**Sub-comp:** `beat-c6b3-self-fulfilling.html`
Video full→full-frame (both speakers) for the phrase build. Dark left gradient. 3 phrase lines, Inter 900 ~118px, STAY.
- LINE 1 **"VERY SELF-FULFILLING"** — fires **comp 15.22** — matches *"very"* (src 1435.52) / *"self"* 1435.70 / *"-fulfilling"* 1436.00, in "it's very self-fulfilling" — `#F0F0F0`
- LINE 2 **"IT ALSO COMES DOWN TO"** — fires **comp 17.18** — matches *"also"* (src 1437.54; "It also has to do with" — "has" 1437.98) — `#F0F0F0`
- LINE 3 **"LIQUIDITY CYCLES"** — fires **comp 18.18** — matches *"liquidity"* (src 1438.48) / *"cycles."* 1438.94 — `#00D4FF` (cyan payoff)

Cyan element: LINE 3 only. Lines hold to ~22.5, then exit up before the chart (c6b4 @ 24.0).

---

### c6b4 — nyt-graph (HALVING BLOCK-REWARD DECAY) — HERO · Mode A · comp 24.0–41.0
**Sub-comp:** `beat-c6b4-halving-decay.html`  (reuse v1's `beat-c6b3-halving-decay.html` pattern; rename + retime)
`<!-- LEAD DEVICE. Reuses the nyt-graph descending-bar pattern. Bars timed to collapse on "block rewards half... doesn't even matter." -->`
At comp 24.0 video full→Mode A (83%). Descending bars on a shared baseline, `scaleY 0→1` bottom-up, `power3.out` (no bounce). Add a leading **50 (2008/genesis era)** bar so the halving story reads as a full decay, then 25 → 12.5 → 6.25 → 3.125 → **1.56**. (6 bars; if too tight in the left zone, drop the 50 bar back to the v1 5-bar set 25→1.56 — builder's call, but 6 tells the "halving" story better.)
- Eyebrow **"BLOCK REWARD DECAY · BTC PER BLOCK"** (JetBrains Mono/Inter 700, ≥32px, `#F0F0F0`) — fires **comp 25.68** — matches *"Bitcoin"* (src 1445.98) / *"halving,"* 1446.34 (chart enters as he names the halving) `<!-- eyebrow label times to "Bitcoin halving" -->`
- Bars draw across **comp 26.0 → 31.5**, descending stagger, so the visual collapse aligns to the spoken decay:
  - "is becoming increasingly" (comp 27.22) → tall bars (25/12.5) settling
  - **"meaningless"** (comp 28.16) → supplemental kinetic annotation slams (see below)
  - "block rewards half" (*block* comp 29.36, *rewards* 29.74, *half* 30.20) → mid bars (6.25/3.125) drawing
  - "to a point where it doesn't even matter" (*doesn't* 31.32, *matter.* 31.80) → final **2028 / 1.56** cyan bar draws to a near-invisible sliver
  - Bar values/years all `#F0F0F0` (NO decaying opacity, D7); 2028 bar + value + year = the single cyan (`#00D4FF` + glow).
- Supplemental kinetic annotation **"INCREASINGLY MEANINGLESS"** (Inter 700, ~40px, left-aligned under the chart, `#F0F0F0`, cyan accent bar) — fires **comp 28.16** — matches *"meaningless"* (src 1448.46) in "the halving is becoming increasingly meaningless". This is a real spoken line, word-synced (the chart's only text beyond labels).
- Chart HOLDS comp ~33–40 under Jasper's "entire dynamic with miners, energy pressure, input cost pressure..." (src 1452.7–1458) — a genuine clean-graphic stretch (≤~7s, within D6's 8s cap), exits ~40.5.

Cyan element: the **2028 / 1.56 bar** only (D7 "nyt-graph: target bar"). The annotation uses a cyan *accent bar* but its text is `#F0F0F0`; to stay strictly one-cyan, the annotation's accent bar is `#2a2a2a` if the 2028 bar is on-screen simultaneously — **Decision: annotation accent bar = `#2a2a2a` (neutral); the 2028 chart bar is the sole cyan.**
Date note (D7): 2012/2016/2020/2024/2028 are historical/scheduled halving dates (absolute, not relative "this year/last year") → permitted. Current reward after the 2024 halving = 3.125 BTC; next (2028) = 1.56 BTC. Correct.

---

### c6b5 — kinetic-type · full-frame · comp 41.0–46.5
**Sub-comp:** `beat-c6b5-doesnt-matter.html`
Video Mode A→full-frame (both speakers). The "so what" of the chart. 3 phrase lines, Inter 900 ~118px, STAY. **Continuous full-frame hold begins here and runs to clip end.**
- LINE 1 **"I DON'T THINK"** — fires **comp 40.84** — matches *"don't"* (src 1461.14; "I" 1460.94, "think" 1461.46) — `#F0F0F0`  *(fires 0.16s before nominal comp_in; beat window opens at 40.8 to land on the word — D2: move the boundary to the word.)*
- LINE 2 **"IT REALLY MATTERS"** — fires **comp 41.50** — matches *"really"* (src 1461.80) / *"matters"* 1462.06 — `#F0F0F0`
- LINE 3 **"IF MINERS SELL OR BUY"** — fires **comp 43.46** — matches *"miners"* (src 1463.76; "selling" 1465.40, "buying." 1465.98) — `#00D4FF` (cyan payoff)

Cyan element: LINE 3 only. **Revised window: comp 40.8–46.5** (`data-start="40.8" data-duration="5.7"`) so LINE 1 lands on its word. (c6b4 exit pulls to ~40.4.)

---

### c6b6 — kinetic-type (KICKER) → clean tail · full-frame · comp 46.5–50.7
**Sub-comp:** `beat-c6b6-strong-narrative.html`
`<!-- D4: clip ENDS on a content kinetic + clean speaker tail — NOT a name card / outro. -->`
The nuance kicker, spoken immediately after c6b5 (one continuous closing movement). 3 phrase lines, Inter 900 ~118px, STAY.
- LINE 1 **"BUT IT IS STILL"** — fires **comp 46.62** — matches *"But"* (src 1466.92; "it" 1467.44, "is" 1467.64, "still" 1467.94) — `#F0F0F0`
- LINE 2 **"A VERY STRONG"** — fires **comp 48.06** — matches *"very"* (src 1468.36; "strong" 1468.50) — `#F0F0F0`
- LINE 3 **"NARRATIVE"** — fires **comp 48.48** — matches *"narrative,"* (src 1468.78; "I think." 1469.18/1469.38) — `#00D4FF` (cyan payoff)

Cyan element: LINE 3 only. Lines hold ~1s, then the stack drifts up/out ~49.7 leaving a **clean full-frame speaker tail comp ~49.7–50.7** (≈1s). Clip ends on clean speaker video — satisfies D4 (no card holds to the end).

---

## VERIFICATION

- **RULE 1 (open on a real line):** ✓ in-point moved to src 1420.30; opening kinetic = the host question "Would you say the four year cycle is dead?", word-synced 0.12/0.94/2.02 to the actual spoken words. No anticipatory text.
- **RULE 2 (vary structure):** ✓ no opening swiss-grid stat-grid; no duplicate stats; no decision-tree loop. CHART-LED: `nyt-graph` halving decay is the structural hero (c6b4, 17s), timed to "block rewards half... doesn't even matter." 6 beats over 50.7s (DESIGN.md frequency for a ~50s clip). Only adjacency (c6b5→c6b6) handled as one closing movement.
- **RULE 3 (framing):** ✓ verified from 4 source frames + a 3-way object-position crop test. **`object-position: 83% center`**, Mode A `{1229,108,614,864}`, no vertical bias (top:108 clearance keeps the name in-frame), static camera → Mode A.
- **D7 palette/type:** one `#00D4FF` per beat (c6b1 L3 / c6b2 L2 / c6b3 L3 / c6b4 2028 bar / c6b5 L3 / c6b6 L3); eyebrows Inter 700 ≥32px `#F0F0F0`; no `#888888` small text; no backdrop-filter blur; no grain. ✓
- **D4 no-outro:** ends on c6b6 content kinetic + ~1s clean speaker tail; no name card. ✓
- **Every non-editorial kinetic line has a real comp_t from the transcript** (quoted above per line). EDITORIAL items: only c6b2's structural index/eyebrow/rule chrome (a label + rule, not a sentence). All kinetic SENTENCES are word-synced.
- **z-index:** add `#beat-c6b1 … #beat-c6b6` to the `z-index:3` rule in index.html (only 6 ids now; remove the old c6b7/c6b8 refs).

**Build Manifest Row:** `clip_6 | clip-6-four-year-cycle | 1420.30 | 1471.00 | kinetic-type,nyt-graph | 6 beats | obj-pos 83%`
