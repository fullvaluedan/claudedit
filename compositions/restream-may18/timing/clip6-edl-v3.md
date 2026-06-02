# Clip 6 — Four-Year Cycle Dead? — v3 BUILD-READY EDL

**Why v3 (what v2 got wrong / what's fixed):**
1. **R1 flip-flop (the headline fix).** v2's view-timeline was `FULL(0–3) → ModeA(3–14.5) → FULL(14.5–24) → ModeA(24–40.5) → FULL(40.5–50.7)` — that is a **Mode-A → full → Mode-A return inside 9.5s**, the exact A-B-A-within-12s defect the checklist flags (clip-7/clip-8 bug). v3 groups the whole middle (answer + both chart devices) into **ONE sustained Mode-A block**, giving `FULL → MODE-A → FULL` with no view ever returning inside 12s.
2. **Device map fully satisfied.** v2 had only the decay chart. v3 adds the **required distinct halving TIMELINE device (2012→2028)** as device #1, the **`nyt-graph` block-reward decay chart** as the hero device #2, and **`caption-neon-glow`** on the closing payoff line. Three distinct catalog-grade devices, none of them another kinetic stack.
3. **Less "clip-2 / kinetic-heavy."** The "self-fulfilling / liquidity cycles" full kinetic stack from v2 is **demoted to a one-line Mode-A annotation** so only ONE kinetic plays before the two chart devices. Kinetic stacks drop from "the whole clip" to 5 short beats, never >2 in a row, and the two chart devices are the visual centerpiece (longest, most-dwelt view).
4. **No cross-beat phrase echo.** v2 used eyebrow "FOUR-YEAR CYCLE" right after the opener said "THE FOUR-YEAR CYCLE." v3 eyebrows are distinct ("THE BULL-CASE / HALVING CADENCE / BLOCK REWARD · BTC ISSUANCE").

**KEPT from v2 (it worked):** the dialog-matched open on the real host question; `object-position: 83% center`; Mode-A geometry `{1229,108,614,864}`; src_in/src_out window; the decay-chart values.

---

## WINDOW (unchanged from v2 — open on a real spoken line)

| | value | note |
|---|---|---|
| **src_in** | **1420.30** | ~0.12s before the host's "Would" (src 1420.42). Trims the trailing "Yeah." (src 1419.74) at the head. |
| **src_out** | **1471.00** | After Jasper's kicker "...still a very strong narrative, I think" (ends src ~1469.4) + ~1.6s clean breath. Cuts BEFORE the host pivot ("Interesting / And lots of crypto insiders…" src 1471.24+). |
| **duration** | **50.70s** | comp = src − 1420.30 |
| **comp basis** | **comp = src − 1420.30** | every fire-time below is read off `clip6-words.txt` (src_t) minus 1420.30; never hand-computed. |

> **clip6-words.txt note:** that table's header (`comp = src − 1350`) is for the OLD 120s window. The src_t column is ground truth; this clip's comp = src_t − 1420.30. Every fire-time below quotes the table's src_t and the subtraction.

**OPENING LINE (R3 dialog-match + R5 coherence):** the clip opens on the HOST question
**"Would you say the four year cycle is dead?"** — a complete, self-contained question spoken in the first 2.02s, word-synced (NOT anticipatory). It is the clip's title line and lands immediately. (DESIGN.md permits a host question as its own word-stack, no "HOST" label.)
- The quote it matches (audio.json 1420.42–1422.52): *"Would you say the four year cycle is dead?"*

---

## VIEW-TIMELINE (proves R1) — the flip-flop killer

| # | segment | view | comp start | comp end | dwell | beats in this view |
|---|---------|------|-----------:|---------:|------:|--------------------|
| 1 | intro host-Q | **FULL-FRAME** (both speakers) | 0.0 | 3.0 | **3.0s** (intro, exempt) | c6b1 |
| 2 | answer + halving devices | **MODE-A** (Jasper right, graphics left) | 3.0 | 40.4 | **37.4s** | c6b2 · c6b3 · c6b4 |
| 3 | closing kinetics + clean tail | **FULL-FRAME** (both speakers) | 40.4 | 50.7 | **10.3s** | c6b5 · c6b6 |

**Transitions:** `FULL → MODE-A → FULL` (exactly two: full→ModeA at 3.0; ModeA→full at 40.4).
**R1 proof:**
- No non-intro segment < 8s (37.4s, 10.3s). PASS.
- Only A-B-A is `FULL→ModeA→FULL`; FULL is left at 3.0 and not re-entered until 40.4 → **gap 37.4s ≫ 12s**. PASS.
- **Consecutive graphic beats grouped:** the three middle beats (answer kinetic + timeline + decay chart) all live in the ONE Mode-A view — the frame does NOT bounce while the halving story tells. The two closing kinetics share the ONE full-frame view. PASS.
- Quick switch only in the intro (full→ModeA at 3.0), and it never loops back. PASS.

**View-timeline one-liner:** `FULL 0–3 → MODE-A 3–40.4 (answer + halving timeline + decay chart, 37.4s sustained) → FULL 40.4–50.7 (closing kinetics + neon-glow payoff + clean tail).`

---

## STRUCTURE / TEMPLATE VARIETY (proves R2)

**Template sequence:** `kinetic(host-Q) → kinetic(answer, Mode-A) → TIMELINE device → nyt-graph CHART (HERO) → kinetic(close) → kinetic+neon-glow(kicker)`

| metric | value | rule | result |
|---|---|---|---|
| distinct PRIMARY device | halving **timeline** + `nyt-graph` **decay chart** (the two longest-dwelt beats, 26.4s combined) lead the clip | R2: distinct device, not kinetic-dominated | PASS — clip 6 is the series' chart/data clip |
| max kinetic word-stacks in a row | **2** (c6b1 full + c6b2 Mode-A), then **two non-kinetic chart devices** break the run; close is 2 (c6b5+c6b6) | R2: ≤2 in a row | PASS |
| kinetic share | 5 short kinetic beats vs 2 chart devices that own the centre + most screen-time | R2: not another clip-2 | PASS |
| init template | chart beats init from `nyt-graph` (NOT `kinetic-type`) | R2: chart content ≠ init kinetic | PASS |

**3+ different element types before t=6.0s (DESIGN.md opening rule):** host-Q kinetic (type 1, full-frame both speakers, fires 0.12) → at t=3.0 video shrinks to **Mode A** + monospace index "06" (type 2) + eyebrow + cyan **rule draw** (type 3) + answer kinetic begins (type 4). Four distinct element types, speaker visible right the whole time, none of them a cookie-cutter stat-grid.

**Catalog blocks — install vs hand-build:**

| beat | device | source | action |
|---|---|---|---|
| c6b3 | halving timeline (horizontal 2012→2028 axis, event ticks) | hand-build (no single catalog block is a labelled halving event-axis; `data-chart` is bar/line, not a time-axis with named ticks) | **HAND-BUILD** — `beat-c6b3-halving-timeline.html` |
| c6b4 | block-reward decay bars | `nyt-graph` example pattern (already realized in the repo's `beat-c6b4-halving-decay.html`) — reuse/retime | **REUSE** existing `beat-c6b4-halving-decay.html` (init lineage `--example nyt-graph`) |
| c6b6 payoff line "NARRATIVE" | premium neon reveal on the single payoff word | **`npx hyperframes add caption-neon-glow`** (component → `compositions/components/caption-neon-glow.html`, ALREADY INSTALLED) | **INSTALL + ADAPT** (see c6b6 detail) |
| (considered, not used) | `caption-kinetic-slam`, `shimmer-sweep`, `data-chart`, `flowchart` | — | considered; the timeline + nyt-graph + neon-glow trio already carries the variety without a second stat-grid or a flow this clip's content doesn't have |

---

## FRAMING (Mode-A — kept verified value from v2)

- **`object-position: 83% center`** — centers Jasper (guest, right half); name lower-third "Jasper De Maere / Wintermute" fully in-frame; seam/Nic excluded. (v2 crop test of 80/83/86 → 83% cleanest.)
- **Mode-A geometry:** `{ left: 1229, top: 108, width: 614, height: 864 }`, `borderRadius: 6px`, entry `expo.inOut` 0.7s. Top clearance 108px, bottom clearance 108px → name never clips. Static camera (head fixed) → **Mode A** (not Mode B).
- Opening full-frame beats (c6b1, c6b5, c6b6) show **both speakers** (text over a dark left-zone gradient, never text on black).
- **VERIFY-BY-FRAME (mandatory before render):** extract and LOOK at frames at the opening (comp 0.5), the full→ModeA switch (comp 3.5), the timeline (comp 18), the decay chart payoff (comp 31.5), the ModeA→full switch (comp 41), and the neon payoff (comp 48.6). Confirm Jasper centered/name in-frame in Mode A; both speakers in full-frame beats.

---

## BEAT MAP

| Beat | comp range | src range | Template / block | View | Sub-comp file |
|------|-----------|-----------|------------------|------|---------------|
| c6b1 | 0.0–3.0 | 1420.30–1423.30 | `kinetic-type` (host question) | FULL-FRAME (both) | `beat-c6b1-host-cycle-dead.html` |
| c6b2 | 3.0–14.0 | 1423.30–1434.30 | Mode-A chrome + `kinetic-type` (answer) | MODE-A | `beat-c6b2-was-dead-it-is.html` |
| **c6b3** | **14.0–25.9** | **1434.30–1446.20** | **Halving TIMELINE (2012→2028) — device #1** | MODE-A | `beat-c6b3-halving-timeline.html` |
| **c6b4** | **25.4–40.4** | **1445.70–1460.70** | **`nyt-graph` block-reward DECAY — HERO device #2** | MODE-A | `beat-c6b4-halving-decay.html` |
| c6b5 | 40.4–46.4 | 1460.70–1466.70 | `kinetic-type` (closing) | FULL-FRAME (both) | `beat-c6b5-doesnt-matter.html` |
| c6b6 | 46.4–50.7 | 1466.70–1471.00 | `kinetic-type` + **`caption-neon-glow`** payoff → clean tail | FULL-FRAME (both) | `beat-c6b6-strong-narrative.html` |

**index.html data-start/data-duration (comp seconds):**
`c6b1 0.0/3.0` · `c6b2 3.0/11.0` · `c6b3 14.0/11.9` · `c6b4 25.4/15.0` · `c6b5 40.4/6.0` · `c6b6 46.4/4.3`

> **c6b3↔c6b4 OVERLAP (required for the seam + cross-dissolve):** c6b3 sub-comp now runs 14.0→**25.9** (data-duration 11.9), so the 2028 cyan tick at comp 25.68 (internal offset 11.68s) renders BEFORE its sub-comp ends (11.9s) — fixing the v3-round failure where the tick fired after the 11.5s clock stopped and the frame lost its only cyan. c6b4 starts at **25.4** (data-start 25.4, data-duration 15.0 → ends 40.4), so the two ranges OVERLAP comp 25.4–25.9 (~0.5s) — this is exactly the window the c6b4 cross-dissolve needs (the 2028 tick lighting at 25.68 sits inside both sub-comps). Before this fix c6b3 (ended 25.5) and c6b4 (started 25.5) abutted with zero overlap, so the described cross-dissolve was impossible.

**z-index:3 rule MUST list every id:** `#beat-c6b1, #beat-c6b2, #beat-c6b3, #beat-c6b4, #beat-c6b5, #beat-c6b6 { z-index: 3; }` (6 ids; no stale c6b7/c6b8). The installed `caption-neon-glow` is wired INSIDE c6b6's sub-comp, so no extra master-level id.

---

## BEAT DETAIL (every kinetic line: on-screen text + transcript words it matches + comp_t)

### c6b1 — `kinetic-type` (HOST QUESTION) · FULL-FRAME · comp 0.0–3.0
**Sub-comp:** `beat-c6b1-host-cycle-dead.html`
`<!-- WORD-SYNCED (not editorial). Cold open IS the spoken host question. No "HOST" label. -->`
Full-frame video, BOTH speakers, dark left-zone gradient backdrop. 3-phrase build, Inter 900 ~94px, each phrase STAYS (no dim). Whole stack exits upward (`power2.in`) at ~2.74 before the Mode-A switch.
- **LINE 1 "WOULD YOU SAY"** — fires **comp 0.12** — matches *"Would"* (src 1420.42; "you" 1420.72, "say" 1420.84) — `#F0F0F0`
- **LINE 2 "THE FOUR-YEAR CYCLE"** — fires **comp 0.94** — matches *"four"* (src 1421.24; "year" 1421.52, "cycle" 1421.70) — `#F0F0F0`
- **LINE 3 "IS DEAD?"** — fires **comp 2.02** — matches *"dead?"* (src 1422.32; "is" 1422.08) — `#00D4FF` (cyan payoff + glow)

Cyan: LINE 3 only. **R5:** the three lines parse as one complete question; payoff is a real phrase ("IS DEAD?"), not a dangling number.
Coherence note: this is a self-contained interrogative — passes R5 ("REQUIRES A TEAM OF / 2–3" type fragments are the failure mode; this is not that).

---

### c6b2 — Mode-A chrome + `kinetic-type` answer · MODE-A · comp 3.0–14.0
**Sub-comp:** `beat-c6b2-was-dead-it-is.html`
At comp 3.0 the master GSAP shrinks video FULL→Mode A (`object-position:83%`); `#bg-glow` fades @3.3; `#zone-rule` draws @3.4. Left-zone chrome + a compact answer kinetic. **NOT a swiss-grid stat block** — no big-number slam, no tag-row.
- Index **"06"** (JetBrains Mono, muted ≥20px) + eyebrow **"THE BULL-CASE"** (Inter 700, ≥32px, `#F0F0F0`) — slam **comp 3.0** `<!-- EDITORIAL chrome: structural label, not a sentence -->`
  - *Eyebrow changed from v2's "FOUR-YEAR CYCLE" → "THE BULL-CASE" so the opener's "THE FOUR-YEAR CYCLE" phrase is NOT echoed in the very next beat (de-repetition).*
- Cyan **rule** draws (scaleX 0→1, `#00D4FF`) **comp 3.4**, then settles to `#2a2a2a` so LINE 2 is the single cyan `<!-- EDITORIAL -->`
- Answer kinetic (2 phrase lines, Inter 900 ~92px, left zone, phrases STAY):
  - **LINE 1 "THOUGHT IT WAS DEAD"** — fires **comp 9.02** — matches *"was"* (src 1429.32) / *"dead,"* (src 1429.54); lead-in "thinking that it was dead" (*thinking* 1428.36) — `#F0F0F0`
  - **LINE 2 "NOW IT IS"** — fires **comp 13.16** — matches *"is."* (src 1433.46) in "the way it's currently playing out… like it is." — `#00D4FF` (cyan payoff)

Cyan: rule draws cyan briefly then → `#2a2a2a`; persistent cyan = LINE 2. One cyan visible at a time. The chrome (3.0–3.4) + Jasper's "I've been going on record multiple times" fills 3.4–9.0 so it isn't dead air.
**R4 (dup words within beat):** eyebrow "THE BULL-CASE" shares no notable word with sublabel/lines "THOUGHT IT WAS DEAD" / "NOW IT IS". PASS.

---

### c6b3 — Halving TIMELINE (2012 → 2028) — DEVICE #1 · MODE-A · comp 14.0–25.9
**Sub-comp:** `beat-c6b3-halving-timeline.html` (HAND-BUILD)
`<!-- DISTINCT DEVICE #1: a horizontal halving-cadence time-axis. NOT a bar chart (that's c6b4), NOT a kinetic stack. Visualizes the four-year halving cadence Jasper is describing while he sets up "the ultimate driver… the Bitcoin halving." Sub-comp data-start="14.0" data-duration="11.9" → clock 14.0→25.9, so the 2028 tick at comp 25.68 (internal offset 11.68s) lights BEFORE the 11.9s clock stops. -->`
A horizontal time-axis across the left zone: baseline rule (x≈80→1060px) with 5 event ticks, each a node + year + a tiny "↓ reward" caption. Ticks pop left→right (`back.out(1.5)`, ~0.4s each) timed to land on the cadence. The **2028 tick** is the single cyan accent (the next/forward halving). The axis stays on-screen and then hands off into the decay chart at c6b4 (the two sub-comps overlap comp 25.4–25.9, so the 2028 tick lighting and the c6b4 chart entry cross-dissolve in the same ~0.5s window).

On-screen text (all Inter/JetBrains Mono, ≥30px, `#F0F0F0` except the one cyan tick):
- Eyebrow **"HALVING CADENCE · EVERY 4 YEARS"** (Inter 700, ≥32px, `#F0F0F0`) — fires **comp 15.22** — matches *"very"* of "very self-fulfilling" (src 1435.52) as the device establishes; the cadence theme is what he's explaining through "liquidity cycles… the ultimate driver" `<!-- EDITORIAL label; device is temporal, not a single word -->`
- Cyan **baseline rule** draws L→R (scaleX 0→1, `#00D4FF` → settles `#2a2a2a`) **comp 15.6**
- Tick markers (node + year, the year in JetBrains Mono ≥30px `#F0F0F0`):
  - **2012** tick pops **comp 17.24** — under *"also"* (src 1437.54)
  - **2016** tick pops **comp 18.18** — under *"liquidity"* (src 1438.48)
  - **2020** tick pops **comp 19.6** (editorial stagger between liquidity-cycles and the "ultimate driver" lead-in — no single word; spaced 0.7s after 2016 to keep the L→R sweep even) `<!-- EDITORIAL stagger -->`
  - **2024** tick pops **comp 21.46** — under *"ultimate"* (src 1441.76) of "the ultimate driver"
  - **2028** tick pops **comp 25.68** — lands on *"Bitcoin"* (src 1445.98) / *"halving,"* (src 1446.34), i.e. exactly as he names the halving — `#00D4FF` (cyan, glow). This tick is the single cyan; it is the "next halving" the whole device points at, and its arrival is the seam into the decay chart. **Internal offset = 25.68 − 14.0 = 11.68s, inside the 11.9s sub-comp duration → the tick renders** (the prior 11.5s duration cut it off at 11.5s, so the only-cyan element never played — that was the §8 hard render fail this revision fixes).

Cyan: the **2028 tick** only (baseline rule settles to `#2a2a2a` once the 2028 tick lights). One cyan.
Date note: 2012/2016/2020/2024/2028 are absolute historical/scheduled halving dates (not relative "this year/last year") → permitted per DESIGN.md date rule.
**R4:** eyebrow "HALVING CADENCE · EVERY 4 YEARS" vs tick years — no shared notable word. PASS. (Note "HALVING" appears here and in c6b4's eyebrow — different beats, allowed; but to be safe c6b4's eyebrow uses "BLOCK REWARD," see below.)

---

### c6b4 — `nyt-graph` BLOCK-REWARD DECAY — HERO (DEVICE #2) · MODE-A · comp 25.4–40.4
**Sub-comp:** `beat-c6b4-halving-decay.html` (REUSE the existing repo file — it already realizes the `nyt-graph` descending-bar pattern; only retime to the offsets below)
`<!-- HERO. nyt-graph descending bars. Bars collapse exactly on "block rewards half… doesn't even matter." Sub-comp data-start="25.4" data-duration="15.0" → enters comp 25.4, overlapping c6b3 (which runs to 25.9) so the 2028 timeline tick lighting at 25.68 cross-dissolves into the chart inside the shared 25.4–25.9 window. -->`
The 2028 tick (c6b3) cross-dissolves into a descending bar chart on a shared baseline: **50 → 25 → 12.5 → 6.25 → 3.125 → 1.56 BTC** (years 2009·2012·2016·2020·2024·2028). `scaleY 0→1` bottom-up, `power3.out` (no bounce). The collapse is the visual of the spoken reward-halving. (The cross-dissolve is real now that c6b3/c6b4 overlap ~0.5s; the chart fades up over comp 25.4–25.9 as the 2028 tick holds, then the timeline hands off.)
- Eyebrow **"BLOCK REWARD · BTC ISSUANCE"** (Inter/JetBrains Mono 700, ≥32px, `#F0F0F0`) — fires **comp 26.04** — matches *"halving,"* (src 1446.34) as the chart enters `<!-- EDITORIAL label; chart is temporal -->`
  - *(Eyebrow says "BLOCK REWARD," not "HALVING," so it shares no notable word with c6b3's "HALVING CADENCE · EVERY 4 YEARS" eyebrow — keeps the two device beats visually distinct. It also no longer repeats "BLOCK" within itself: v3-round had "BLOCK REWARD · BTC PER BLOCK" (R4 internal dup-word); "BTC ISSUANCE" removes the second "BLOCK" so no notable word appears twice in the one label.)*
- Bars draw across **comp 26.0 → 31.8** descending stagger so the collapse aligns to the spoken decay:
  - tall bars (50/25/12.5) settle under "is becoming increasingly" (*becoming* comp 27.22, *increasingly* 27.54)
  - mid bars (6.25/3.125) draw under "block rewards half" (*block* comp 29.36, *rewards* 29.74, *half* 30.20)
  - final **2028 / 1.56** cyan bar draws to a near-invisible sliver on "to a point where it doesn't even matter" (*doesn't* comp 31.32, *matter.* 31.80)
- Supplemental annotation **"INCREASINGLY MEANINGLESS"** (Inter 700, ~40px, left-aligned under the chart, `#F0F0F0`, neutral `#2a2a2a` accent bar) — fires **comp 28.16** — matches *"meaningless"* (src 1448.46) in "the halving is becoming increasingly meaningless." Real spoken line, word-synced (the chart's only sentence-text beyond labels).
- Chart HOLDS comp ~32–40 under Jasper's "the entire dynamic with miners, energy pressure, input cost pressure…" (src 1453.2–1457.6) — a genuine clean-graphic dwell within the Mode-A view; `.b4-inner` exits ~comp 40.0 (offset 14.5) before the full-frame switch.

Cyan: the **2028 / 1.56 bar** only (D7 nyt-graph target bar). The "INCREASINGLY MEANINGLESS" annotation's accent bar is `#2a2a2a` (neutral) so the 2028 bar is the sole cyan; values/years all `#F0F0F0` (no decaying opacity).
Data correctness: current post-2024 reward = 3.125 BTC; next (2028) = 1.5625 ≈ 1.56 BTC. Correct.
**Existing-file retime note:** the repo `beat-c6b4-halving-decay.html` is authored at internal offsets for a comp_in of 24.0 (eyebrow @1.68, bars @2.0–7.1, annot @4.16, exit @16.3). For v3 comp_in **25.4**, set the sub-comp **`data-start="25.4" data-duration="15.0"`** in index.html and shift the internal offsets to: eyebrow **0.64**, bars **0.6 / 1.3 / 2.1 / 3.2 / 4.4 / 5.92** (→ 2028 bar at comp 31.32), annotation **2.76** (→ comp 28.16), `.b4-inner` exit **14.6** (→ comp 40.0). (Offsets = the comp fire-times above minus 25.4. The fire-times themselves are unchanged from v3-round — only the sub-comp start moved 25.5→25.4 to create the c6b3 overlap, so every offset shifts +0.1.)

---

### c6b5 — `kinetic-type` (CLOSING) · FULL-FRAME · comp 40.4–46.4
**Sub-comp:** `beat-c6b5-doesnt-matter.html`
At comp 40.4 master GSAP expands Mode A → FULL-FRAME (both speakers); `#bg-glow`/`#zone-rule` fade @40.2. **Continuous full-frame hold begins here and runs to clip end** (no Mode-A return — R1). The "so what" of the chart. 3 phrase lines, Inter 900 ~118px, STAY.
- **LINE 1 "I DON'T THINK"** — fires **comp 40.84** — matches *"don't"* (src 1461.14; "I" 1460.94, "think" 1461.46) — `#F0F0F0`
- **LINE 2 "IT REALLY MATTERS"** — fires **comp 41.50** — matches *"really"* (src 1461.80) / *"matters"* (src 1462.06) — `#F0F0F0`
- **LINE 3 "IF MINERS SELL OR BUY"** — fires **comp 43.46** — matches *"miners"* (src 1463.76; "selling" 1465.40, "buying." 1465.98) — `#00D4FF` (cyan payoff)

Cyan: LINE 3 only. The Mode-A→full switch (40.4) lands **0.44s before** LINE 1's word (40.84) so the frame is settled when the kinetic fires (D2: boundary moved to the word).
**R4:** no notable word repeats across the three lines / no eyebrow here. PASS.

---

### c6b6 — `kinetic-type` + `caption-neon-glow` payoff (KICKER) → clean tail · FULL-FRAME · comp 46.4–50.7
**Sub-comp:** `beat-c6b6-strong-narrative.html`
`<!-- D4: clip ENDS on a content kinetic + clean speaker tail — NOT a name card/outro. Payoff word uses caption-neon-glow (the clip's premium-reveal device). -->`
The nuance kicker, spoken immediately after c6b5 (one continuous closing movement over the single full-frame hold). Lines 1–2 are standard phrase-build (Inter 900 ~118px, STAY); the **payoff line uses `caption-neon-glow`**.
- **LINE 1 "BUT IT IS STILL"** — fires **comp 46.62** — matches *"But"* (src 1466.92; "it" 1467.44, "is" 1467.64, "still" 1467.94) — `#F0F0F0`
- **LINE 2 "A VERY STRONG"** — fires **comp 48.06** — matches *"very"* (src 1468.36; "strong" 1468.50) — `#F0F0F0`
- **PAYOFF "NARRATIVE"** (`caption-neon-glow`) — fires **comp 48.48** — matches *"narrative,"* (src 1468.78; "I think." 1469.18/1469.38) — `#00D4FF` (neon glow)

**caption-neon-glow wiring + brand adaptation (REQUIRED — the default is off-brand):** the component is installed at `compositions/components/caption-neon-glow.html`. Paste its `#ne-container` markup + neon CSS + GSAP into c6b6 and apply these edits so it obeys the project rules:
1. **Color → brand cyan.** Replace the component's active `#00FFF0` with **`#00D4FF`**. **Delete the pink `#FF0099` keyword branch and the `KEYWORDS` set entirely** (R: one cyan only; pink is banned). All glow uses `#00D4FF`.
2. **No dim-back (phrases STAY rule).** Remove the per-word `tl.to(el, { color:"rgba(...,0.14)", textShadow:"none" }, w.end)` so once "NARRATIVE" lights, it **stays lit** through the beat (matches the project's "phrases build and STAY, no dim" rule; the upstream karaoke dim is for Remotion only).
3. **Single word, positioned in the stack.** WORDS/GROUPS reduced to the one payoff word `{ text:"NARRATIVE", start:0.0 }` (the timeline starts at the beat, so its internal start 0.0 = comp 48.48 via `data-start="48.48"` OR fire it from c6b6's own GSAP at offset 2.08). Move `.ne-group` from `bottom:120px; justify-content:center` to align under LINES 1–2 in the left/centre stack (set `bottom:auto; top:` to match the third line's y, left-justified to the kinetic column).
4. Font: the component ships `Outfit 900`; switch to **Inter 900** to match the other lines (or keep Outfit only for this one hero word — builder's call, but Inter is the safe brand default).

Cyan: the neon "NARRATIVE" only. Lines hold ~1s, then the whole stack drifts up/out ~comp 49.7 leaving a **clean full-frame speaker tail comp ~49.7–50.7** (≈1s). Clip ends on clean speaker video — satisfies D4 (no card to the end).
**R4:** "NARRATIVE" / "A VERY STRONG" / "BUT IT IS STILL" share no notable word. PASS.

---

## VERIFICATION (graded against `_QA-CHECKLIST.md`)

- **§1 R1 view-discipline:** view-timeline `FULL 0–3 → MODE-A 3–40.4 → FULL 40.4–50.7`. No non-intro segment <8s (37.4s, 10.3s). No A-B-A within 12s (FULL not re-entered for 37.4s). Consecutive graphic beats (c6b2/c6b3/c6b4) grouped in ONE Mode-A view. **This is the v2→v3 headline fix.** ✓
- **§2 R2 variety:** distinct primary devices = halving **timeline** (c6b3) + `nyt-graph` **decay chart** (c6b4) — the two longest beats, the centre of the clip; ≤2 kinetic in a row (max 2, broken by the two chart devices); chart beats do not init from kinetic-type; `caption-neon-glow` installed for the payoff. ✓
- **§3 dialog-match:** opens on the real spoken host question (1420.42–1422.52), word-synced 0.12/0.94/2.02; first text by comp 0.12. ✓
- **§4 R5 opening coherence:** "WOULD YOU SAY / THE FOUR-YEAR CYCLE / IS DEAD?" = a complete question; payoff "IS DEAD?" is a real phrase, not a fragment/number. ✓
- **§5 framing:** `object-position: 83% center`, Mode-A `{1229,108,614,864}`; full-frame beats show both speakers; verify-by-frame checklist listed above. ✓
- **§6 R3 jargon:** this window has **no** jargon-table traps (no DePIN/perps/grunt/take-rate/meme-coin/insatiable/spivy in 1420.30–1471.00). On-screen terms = Bitcoin, halving, block reward, BTC, miners, narrative — all plain/correct. Proper noun on the name lower-third "Jasper De Maere / Wintermute" spelled exactly. ✓
- **§7 R4 dup words:** no notable word repeats across two text elements of any single beat, AND no notable word repeats WITHIN a single element. Eyebrows de-duplicated across beats ("THE BULL-CASE" / "HALVING CADENCE · EVERY 4 YEARS" / "BLOCK REWARD · BTC ISSUANCE") and the opener's "FOUR-YEAR CYCLE" is no longer echoed by the next beat's eyebrow. c6b4's eyebrow was "BLOCK REWARD · BTC PER BLOCK" (the word "BLOCK" twice in one label — an internal R4 dup) → now **"BLOCK REWARD · BTC ISSUANCE"**, "BLOCK" appears once, and it still shares no notable word with c6b3's "HALVING CADENCE · EVERY 4 YEARS". ✓
- **§8 hard rules:** z-index:3 lists all 6 ids; exactly one `#00D4FF` per beat (c6b1 L3 / c6b2 L2 / c6b3 2028 tick / c6b4 2028 bar / c6b5 L3 / c6b6 neon "NARRATIVE"). **The c6b3 2028 cyan tick now actually renders:** sub-comp data-duration extended 11.5→**11.9** so the tick at internal offset 11.68s (comp 25.68) plays before the clock stops — previously it fired after the 11.5s clock ended, so the beat lost its only `#00D4FF` element (a hard render fail). c6b4 data-start moved 25.5→**25.4** so c6b3 (now ends 25.9) and c6b4 OVERLAP comp 25.4–25.9, which is what makes the described 2028-tick→decay-chart cross-dissolve actually possible (the prior abutting ranges had zero overlap). No backdrop-filter blur; no grain; eyebrows Inter 700 ≥32px `#F0F0F0`; no `#888888` small text; no intro/outro card; ends on a content beat + clean tail; dates absolute halving years (allowed); phrases STAY (no dim) — and the neon-glow component is explicitly adapted to drop its dim-back. ✓
- **§9 verify-by-frame:** mandated at 6 timestamps above before any "done." ✓

**Build Manifest Row:** `clip_6 | clip-6-four-year-cycle | 1420.30 | 1471.00 | kinetic-type,timeline,nyt-graph,caption-neon-glow | 6 beats | obj-pos 83% | views FULL→MODEA→FULL`
