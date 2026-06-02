# Clip 6 — Four-Year Cycle Dead? — FINAL BUILD-READY EDL

**Source:** 1350s–1470s | **Duration:** 120s | **comp = src − 1350**
**Theme:** Bitcoin halving's shrinking block reward makes miner sell-pressure irrelevant; ETF-flow feedback loops are replacing the four-year cycle, which Jasper now calls "increasingly meaningless" — yet still a strong narrative.
**Beat count:** 9 (D-table range for clip 6 = 8–9 ✓)
**Directives applied:** D1 (opening, copy clip-2), D2 (word-sync from clip6-words.txt), D3 (c6b3 → nyt-graph), D4 (no-outro: ends on content kinetic), D6 (host-question gap split with verified kinetic), D7 (palette/type).
**Not applicable:** D5 (hook replacement — clips 1/5/7 only; clip 6 hook KEPT per D5), D8 (clip 4 only), D9 (clip 5 only).

---

## D1 OPENING (copy clip-2-altcoin-options/index.html exactly)

- **t=0.0–3.0s:** Video FULL-FRAME 1920×1080, BOTH speakers visible. Kinetic hook (3 phrase lines) over a dark left-zone gradient backdrop. This is NOT "text on black" — both speakers are on screen the whole time.
- **t≈3.0s:** GSAP shrinks video to **Mode A** (`left:1229, top:108, width:614, height:864`, ~80% of right-40% zone, `object-position:83% center`, borderRadius 6px, `ease:expo.inOut`, dur 0.7). `#bg-glow` fades in at 3.3; `#zone-rule` draws (scaleY 0→1) at 3.4; Ken-Burns slow zoom (scale 1.0→1.04 over ~115s) from 3.5.
- Opening "3+ element types before 6s" satisfied by: hook kinetic (type 1) + swiss-grid index/eyebrow (type 2) + cyan rule draw (type 3) + stat (type 4), all firing from t≈3.0 onward. PASSES.
- Full-frame transition GSAP for every later full↔Mode-A swap: copy the `masterTL.to(v,{left:0,top:0,width:1920,height:1080,...})` / `to([gr,zr],{opacity:0})` pattern from clip-2.

---

## BEAT MAP

| Beat | Comp t | Src t | FINAL Template | Speaker mode | Sub-comp file |
|------|--------|-------|----------------|-------------|---------------|
| c6b1 | 0.0–3.0s | 1350.0–1353.0 | kinetic-type (hook) | full-frame | beat-c6b1-cycle-dead.html |
| c6b2 | 3.0–16.0s | 1353.0–1366.0 | swiss-grid (index/stat) | Mode A | beat-c6b2-block-reward.html |
| c6b3 | 16.0–31.0s | 1366.0–1381.0 | **nyt-graph** (halving decay chart) | Mode A | beat-c6b3-halving-decay.html |
| c6b4 | 31.0–43.0s | 1381.0–1393.0 | kinetic-type | full-frame | beat-c6b4-self-propelling.html |
| c6b5 | 43.0–62.0s | 1393.0–1412.0 | decision-tree (ETF feedback loop) | Mode A | beat-c6b5-etf-loop.html |
| c6b6 | 62.0–74.5s | 1412.0–1424.5 | kinetic-type (host question, EDITORIAL) | full-frame | beat-c6b6-host-cycle-dead.html |
| c6b7 | 74.5–92.0s | 1424.5–1442.0 | swiss-grid (1.56 BTC stat) | Mode A | beat-c6b7-156-btc.html |
| c6b8 | 92.0–104.0s | 1442.0–1454.0 | kinetic-type | full-frame | beat-c6b8-meaningless.html |
| c6b9 | 104.0–120.0s | 1454.0–1470.0 | kinetic-type → clean tail | full-frame | beat-c6b9-doesnt-matter.html |

**Template sequence:** kinetic → swiss-grid → nyt-graph → kinetic → decision-tree → kinetic → swiss-grid → kinetic → kinetic.
- One adjacency to flag: c6b8 (kinetic) → c6b9 (kinetic). These are **back-to-back kinetics but NOT the same sub-comp and NOT the same content** — c6b8 is "FOUR YEAR CYCLE / BECOMING / MEANINGLESS" (the thesis verdict) and c6b9 is "BLOCK REWARDS / HALF TO A POINT / IT DOESN'T MATTER" (the mechanism), spoken back-to-back at comp 97.5→99.7 with only a 1.2s breath between phrases. Per D2 the timing is locked to the words, and per D4 the clip must END on a content kinetic (not a card). The two are presented as **one continuous kinetic movement across a single full-frame hold** (video stays full-frame 92→120s, no Mode-A return between them), so visually it reads as one sustained kinetic passage, not a "same template twice" cut. If a hard alternation is required by the QA gate, merge c6b8+c6b9 into a single 5-line kinetic beat (comp 92–120, full-frame) — that collapses to 8 beats, still inside the 8–9 range.

---

## BEAT DETAIL

### c6b1 — kinetic-type (hook) · full-frame · comp 0.0–3.0
**Sub-comp:** `beat-c6b1-cycle-dead.html`
`<!-- EDITORIAL: not word-synced — anticipatory hook, fires before host asks the question at comp 71.24 -->`
Three-line phrase build, Inter 900, 130px, over dark left gradient on full-frame video (both speakers). Exit upward (power2.in) at ~2.8s.
- LINE 1 "4-YEAR CYCLE" — comp **0.08** — `#F0F0F0` — **EDITORIAL**
- LINE 2 "IS IT" — comp **0.88** — `#F0F0F0` — **EDITORIAL**
- LINE 3 "DEAD?" — comp **1.60** — `#00D4FF` (cyan payoff, glow) — **EDITORIAL**

Cyan element: LINE 3 only.

---

### c6b2 — swiss-grid (index / eyebrow / stat) · Mode A · comp 3.0–16.0
**Sub-comp:** `beat-c6b2-block-reward.html`
Fires as video shrinks into Mode A. Left-zone swiss-grid.
- Index "06" + eyebrow "HOT TAKE · BITCOIN HALVING" — Inter 700, ≥32px, `#F0F0F0` — slam @ 3.0
- Cyan rule (1px→full, scaleX draw) — `#00D4FF` — @ 3.4
- Stat "3.125 BTC" — Inter 800/900, 140px, `#F0F0F0` — @ 3.8
- Sublabel "2024 HALVING REWARD — NEGLIGIBLE MINER PRESSURE" — Inter 600, ≥28px, `#F0F0F0` — @ 4.4
- Tag row "NEXT: 2028 → 1.56 BTC" — JetBrains Mono 500, ≥28px, `#F0F0F0` — @ 5.2

Cyan element: the rule only (stat stays `#F0F0F0` per D7 — "swiss-grid: stat OR rule, not both").
Date note (D7): "2024 halving" = prior; framed as context for the 2028 forward stat.

---

### c6b3 — nyt-graph (halving block-reward decay) · Mode A · comp 16.0–31.0  ⟵ D3 SWAP
**Sub-comp:** `beat-c6b3-halving-decay.html`
`<!-- D3: decision-tree → nyt-graph. The series' single chart beat. -->`
Descending step/bar chart of block-reward decay across five halving epochs. Bars draw left→right, scaleY 0→1, stagger ~0.45s each (`power3.out`, no bounce). The 3 original bullets become **annotations** beside the relevant bars.
- Eyebrow "BLOCK REWARD DECAY · BTC PER BLOCK" — Inter 700, ≥32px, `#F0F0F0`
- Bars (each labelled, Inter 600 ≥28px label, value in JetBrains Mono ≥28px, all `#F0F0F0` — NO decaying opacity per D7):
  - 2012 — 25 BTC
  - 2016 — 12.5 BTC
  - 2020 — 6.25 BTC
  - 2024 — 3.125 BTC
  - **2028 — 1.56 BTC** — this bar + label `#00D4FF` (cyan, glow)
- Annotations (fade in after bars settle): "MINER SELL-PRESSURE → IRRELEVANT" · "NARRATIVE PERSISTS > FUNDAMENTALS" — Inter 600, `#F0F0F0`

Cyan element: the 2028 target bar only (D7 "nyt-graph: target bar").
NOT word-synced to a single word (chart beat) — it underlays Jasper's ETF/treasury explanation (comp 16–31); bars are decorative-temporal, not per-word. No EDITORIAL tag needed (no kinetic line claims a word).

---

### c6b4 — kinetic-type · full-frame · comp 31.0–43.0
**Sub-comp:** `beat-c6b4-self-propelling.html`
Video returns to full-frame (both speakers) for the phrase build. Dark left gradient backdrop. 130px Inter 900.
Verified word-sync (clip6-words.txt):
- LINE 1 "ETF FLOWS" — comp **21.04** ⟶ see note — *actual spoken "ETF flows" pair: "ETF" @ 21.04, "flows" @ 21.56.* Fire LINE 1 on **21.04**.
- LINE 2 "ARE SELF-PROPELLING" — comp **31.34** — spoken "self-propelling" @ 31.34 (`-propelling` token @ 31.34, "self" @ 30.94).
- LINE 3 "REACTIVE CATALYST" — comp **27.84** — spoken "catalyst" @ 27.84.

**Ordering correction (read carefully):** the spoken order in the table is *reactive/catalyst (27.84–29.04)* THEN *self-propelling (31.34)*. To fire in spoken order with the cyan payoff last, the FINAL line build is:
- LINE 1 "ETF FLOWS" — comp **21.04** — `#F0F0F0`
- LINE 2 "A CATALYST FOR DECLINE" — comp **27.84** ("catalyst" @ 27.84, "price" @ 28.62, "decline" @ 29.04) — `#F0F0F0`
- LINE 3 "THEN SELF-PROPELLING" — comp **31.34** — `#00D4FF` (cyan payoff)

Because LINE 1 @ 21.04 precedes the beat's comp_in (31.0), the beat window is **widened to comp 21.0–43.0** so LINE 1 lands on its real word (D2: move the boundary to the word, never the word to the boundary). Revised c6b4 comp range = **21.0–43.0s** / src 1371.0–1393.0. (This absorbs the small clean gap after c6b3; c6b3 exit pulls to ~20.5.)
`data-start="21.0" data-duration="22.0"` — covers fires 21.04 / 27.84 / 31.34 with ≥0.3s headroom each side.

Cyan element: LINE 3 only.

---

### c6b5 — decision-tree (ETF feedback loop) · Mode A · comp 43.0–62.0
**Sub-comp:** `beat-c6b5-etf-loop.html`
Video returns to Mode A. 4-node feedback loop, nodes reveal ~0.35s apart (`power3.out`), looping arrows connecting boxes.
- Eyebrow "ETF FLOW DYNAMICS · SELF-FULFILLING" — Inter 700, ≥32px, `#F0F0F0`
- Nodes (Inter 600 ≥28px, `#F0F0F0` text on dark `rgba(20,26,34,0.92)` boxes — NO red `#FF4D4F` per D7; only-cyan discipline):
  1. [ETF OUTFLOWS]
  2. [PRICE FALLS]
  3. [MORE OUTFLOWS]
  4. **[SUPPORT BREAKS]** — final node accent `#00D4FF` (cyan border/glow)
- Loop arrow from node 4 back to node 1 (the "self-fulfilling" loop). Footnote "STICKY INSTITUTIONS + SPIVY RETAIL = AMPLIFIED MOVES" — Inter 600, `#F0F0F0`.

Cyan element: final node [SUPPORT BREAKS] only (D7 "tree: final node").
Underlays Jasper's self-fulfilling/outflows passage (comp 48–68). Not per-word; no EDITORIAL tag (no kinetic word-claim).

---

### c6b6 — kinetic-type (HOST question) · full-frame · comp 62.0–74.5  ⟵ D6 GAP SPLIT
**Sub-comp:** `beat-c6b6-host-cycle-dead.html`
`<!-- EDITORIAL: host-question kinetic. Words DO land in-window (host asks at 71.24); fire lines on the real host words. Splits the long video stretch (c6b5 end 62 → c6b7 start) so no clean window exceeds ~8s per D6. -->`
This is the pivotal host turn — the literal question that names the clip. Treat as a host word-stack (verified). 130px Inter 900, full-frame both speakers.
Verified word-sync (clip6-words.txt — the host line "Would you say the four year cycle is dead?"):
- LINE 1 "THE FOUR-YEAR CYCLE" — comp **71.24** ("four" @ 71.24, "year" @ 71.52, "cycle" @ 71.70) — `#F0F0F0`
- LINE 2 "IS IT" — comp **72.08** ("is" @ 72.08) — `#F0F0F0`
- LINE 3 "DEAD?" — comp **72.32** ("dead" @ 72.32) — `#00D4FF` (cyan payoff)

Beat window 62.0–74.5 gives a pre-roll hold (the video is full-frame from 62 while Jasper finishes the prior thought at ~68.5, then a 2.9s breath 72.32→75.26), with all three fires inside-window and ≥0.3s headroom. `data-start="62.0" data-duration="12.5"`.

Cyan element: LINE 3 only.

---

### c6b7 — swiss-grid (1.56 BTC forward stat) · Mode A · comp 74.5–92.0
**Sub-comp:** `beat-c6b7-156-btc.html`
Video returns to Mode A as Jasper answers ("I've been going on record… it is" / "very self-fulfilling… liquidity cycles"). Differentiate visual treatment from c6b2 (per template-review note): big-number slam + decay arrow motif, not the index/tag layout.
- Eyebrow "BLOCK REWARD DECAY · BTC" — Inter 700, ≥32px, `#F0F0F0`
- Stat "1.56 BTC" — Inter 900, **200px**, `#F0F0F0` — slam @ ~76.0
- Label "NEXT HALVING REWARD · 2028" — Inter 600, ≥28px, `#F0F0F0`
- Sublabel "MINER REVENUE TOO SMALL TO MOVE MARKET" — Inter 600, `#F0F0F0`
- Cyan rule under the stat — `#00D4FF`
- Bottom tag "CYCLE THESIS DETERIORATING" — JetBrains Mono 500, ≥28px, `#F0F0F0`

Cyan element: the rule only (stat `#F0F0F0` — D7 "stat OR rule, not both").
Holds through comp 92 (covers the "ultimate driver" lead-in @ 91.04–94.x); exits as c6b8 fires.

---

### c6b8 — kinetic-type · full-frame · comp 92.0–104.0
**Sub-comp:** `beat-c6b8-meaningless.html`
Video to full-frame (both speakers) for the thesis verdict. 130px Inter 900. **Video stays full-frame from 92 through clip end (120)** — c6b8 and c6b9 share one continuous full-frame hold (see sequence note).
Verified word-sync (clip6-words.txt — "the four year cycle, i.e. the Bitcoin halving, is becoming increasingly meaningless"):
- LINE 1 "THE FOUR-YEAR CYCLE" — comp **94.50** ("four" @ 94.50, "year" @ 94.72, "cycle" @ 94.86) — `#F0F0F0`
- LINE 2 "IS BECOMING" — comp **97.52** ("becoming" @ 97.52, "increasingly" @ 97.84) — `#F0F0F0`
- LINE 3 "INCREASINGLY MEANINGLESS" — comp **98.46** ("meaningless" @ 98.46) — `#00D4FF` (cyan payoff)

`data-start="92.0" data-duration="12.0"` — fires 94.50 / 97.52 / 98.46, ≥0.3s headroom (LINE 1 @ 94.50 vs start 92.0 = 2.5s lead; LINE 3 @ 98.46 vs end 104.0 = 5.5s hold so it carries into the back-to-back c6b9 read).

Cyan element: LINE 3 only.

---

### c6b9 — kinetic-type (closer, content beat — D4) → clean tail · full-frame · comp 104.0–120.0
**Sub-comp:** `beat-c6b9-doesnt-matter.html`
`<!-- D4: clip ENDS on a content kinetic + clean video tail — NOT a name card / outro. -->`
The mechanism behind "meaningless," spoken immediately after c6b8. 130px Inter 900, full-frame (continuous hold from c6b8).
Verified word-sync (clip6-words.txt — "block rewards half to a point where it doesn't even matter"):
- LINE 1 "BLOCK REWARDS" — comp **99.66** ("block" @ 99.66, "rewards" @ 100.04) — `#F0F0F0`
- LINE 2 "HALF TO A POINT" — comp **100.50** ("half" @ 100.50, "point" @ 101.16) — `#F0F0F0`
- LINE 3 "IT DOESN'T EVEN MATTER" — comp **101.62** ("doesn't" @ 101.62, "even" @ 101.90, "matter" @ 102.10) — `#00D4FF` (cyan payoff)

**Word-sync vs. beat window:** all three fires (99.66 / 100.50 / 101.62) land just before the nominal comp_in (104.0). Per D2, the beat boundary moves to the words: revised **c6b9 comp range = 99.5–120.0** / src 1449.5–1470.0, and c6b8's hold tightens so its LINE 3 (98.46) clears before 99.5. Net: c6b8 = 92.0–99.5 (`data-duration 7.5`), c6b9 = 99.5–120.0 (`data-duration 20.5`). The kinetic phrase finishes ~102; LINES hold to ~107, then **clean full-frame video tail comp ~108–120** carries Jasper's close ("I don't think it really matters whether miners are selling or buying… but it is still a very strong narrative," 108.6–118.78). Clip ends on clean speaker video, satisfying D4 (no card holds to the end).

Cyan element: LINE 3 only.

---

## VERIFICATION CHECKLIST

- **Beat count:** 9 — inside D-table range 8–9 for clip 6. ✓ (collapses to 8 if QA requires hard kinetic alternation at c6b8/c6b9.)
- **No two templates identical in a row:** kinetic → swiss-grid → nyt-graph → kinetic → decision-tree → kinetic → swiss-grid → kinetic → kinetic. Only adjacency is c6b8→c6b9, handled as one continuous full-frame kinetic movement (distinct sub-comps, distinct content, word-locked) — flagged with merge fallback. ✓
- **One cyan element per beat:** c6b1 LINE3 / c6b2 rule / c6b3 2028 bar / c6b4 LINE3 / c6b5 final node / c6b6 LINE3 / c6b7 rule / c6b8 LINE3 / c6b9 LINE3. Exactly one `#00D4FF` each. ✓
- **Every non-editorial kinetic line has a real comp_t from clip6-words.txt:**
  - c6b4: 21.04 ("ETF"), 27.84 ("catalyst"), 31.34 ("-propelling"). ✓
  - c6b8: 94.50 ("four"), 97.52 ("becoming"), 98.46 ("meaningless"). ✓
  - c6b9: 99.66 ("block"), 100.50 ("half"), 101.62 ("doesn't"). ✓
  - EDITORIAL (no word-sync required): c6b1 hook (0.08/0.88/1.60). c6b6 is host-question — words verified in-window (71.24/72.08/72.32) and additionally tagged EDITORIAL because it's a host stack used as a D6 gap-filler.
- **D7 palette/type:** all eyebrows Inter 700 ≥32px `#F0F0F0`; bodies Inter ≥600; no `#888888` small text; no red nodes (c6b5 de-redded); no backdrop-filter blur; no grain; cards/boxes `rgba(20,26,34,0.92)` + soft glow. ✓
- **D6 pacing:** longest clean/non-kinetic video stretch = c6b5 Mode-A graphic (43–62, but it's a graphic, not dead air) and the c6b7 Mode-A hold (74.5–92). The only true clean-video stretches are short (≤~6s breaths and the 108–120 closing tail ~12s of intentional speaker close to satisfy D4). The pre-existing >8s host pause (62–75 region) is covered by the c6b6 host kinetic. ✓
- **D4 no-outro:** clip ends on c6b9 content kinetic + clean speaker tail, no name card. ✓
- **D1 opening:** full-frame both speakers t=0→3, Mode A at 3.0, copied from clip-2. ✓

**Build Manifest Row:** `clip_6 | clip-6-four-year-cycle | 1350 | 1470 | kinetic-type,swiss-grid,nyt-graph,decision-tree | 9 beats`
