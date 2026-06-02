# Clip 1 — OTC Model / Crypto as Career — FINAL BUILD-READY EDL

**clip_id:** `clip_1` · **dir:** `clip-1-otc-model` · **src window:** 220s–350s · **duration:** 130s
**Comp offset:** `comp_t = src_t − 220` (canonical; never deviate)
**Beat count:** 10 (D-table range for clip 1 = 9–10) ✅
**Speaker layout:** side-by-side host(L)+guest(R) source. Mode A = framed RIGHT 40% zone, ~85% scale, both speakers' right-side composition. Full-frame = 1920×1080 both speakers w/ dark gradient backdrop on LEFT for overlay text.

> All directives applied: **D1** (full-frame t=0→Mode A t=3, copy clip-2) · **D3** (c1b5 tree→swiss-grid; c1b7 split clean+liquid-glass; c1b8 no "WE WAREHOUSE" repeat) · **D4** (no outro — c1b9 name-card moved MID-clip, clip ends on a content beat) · **D5** (hook → "WE WAREHOUSE / THAT RISK / PRICE IS THE INCENTIVE", EDITORIAL) · **D6** (split the 14s c1b4 window with a verified supplemental kinetic) · **D7** (palette/type) · **D8** n/a (clip 4 only) · **D9** n/a (clip 5 only).

> **#1 correction vs original:** every non-editorial kinetic line is now read straight off `clip1-words.txt`. The original fired c1b3 ~4.7s early and c1b6 cited src 328.x while claiming a 278–294s window (off by ~48s, word outside its own beat). All re-derived below.

---

## OPENING HOOK — EDITORIAL (D1 + D5)

Replaces the rejected "CRYPTO IS JUST / ANOTHER CAREER / IN AN INDUSTRY". New hook is unique to the Wintermute model (warehouse-risk line, verified spoken at comp ~108) but fires anticipatorily as a thesis statement — NOT word-synced.

- **Line 1** "WE WAREHOUSE" — fires **comp t=0.08** (white #F0F0F0, 130px) `<!-- EDITORIAL: not word-synced -->`
- **Line 2** "THAT RISK" — fires **comp t=0.88** (white #F0F0F0, 130px) `<!-- EDITORIAL -->`
- **Line 3** "PRICE IS THE INCENTIVE" — fires **comp t=1.60** (cyan #00D4FF, 130px — the ONE cyan element) `<!-- EDITORIAL -->`
- Whole stack drifts up + fades (power2.in) starting comp t=2.7; gone by 2.95.
- Video FULL-FRAME (both speakers) the entire 0–3.0; GSAP shrinks to Mode A at exactly **comp t=3.0** (`expo.inOut`, dur 0.7); `#bg-glow` fades in at 3.3, `#zone-rule` draws at 3.4. (Copy clip-2 PHASE 0/1 verbatim.)

---

## FINAL BEAT MAP (10 beats)

| Beat | Comp t | Src t | FINAL template | Speaker | Sub-comp |
|------|--------|-------|----------------|---------|----------|
| c1b1 | 0.0–3.0s | 220.0–223.0 | kinetic-type (hook) | full-frame | `beat-c1b1-hook.html` |
| c1b2 | 3.0–15.0s | 223.0–235.0 | swiss-grid (index/eyebrow launch) | Mode A | `beat-c1b2-convergence.html` |
| c1b3 | 15.0–24.5s | 235.0–244.5 | kinetic-type | full-frame | `beat-c1b3-another-career.html` |
| c1b4 | 24.5–33.0s | 244.5–253.0 | clean video window | Mode A | — |
| c1b5 | 33.0–45.0s | 253.0–265.0 | kinetic-type (supplemental, D6 split) | full-frame | `beat-c1b5-otc-desk.html` |
| c1b6 | 45.0–60.0s | 265.0–280.0 | liquid-glass card (Jasper name-card, MID-clip per D4) | Mode A | `beat-c1b6-jasper.html` |
| c1b7 | 60.0–78.0s | 280.0–298.0 | swiss-grid (Agency vs Principal — D3 c1b5 swap) | Mode A | `beat-c1b7-agency-principal.html` |
| c1b8 | 78.0–101.0s | 298.0–321.0 | clean → liquid-glass card (D3 c1b7 split) | Mode A | `beat-c1b8-risk-price.html` |
| c1b9 | 101.0–119.0s | 321.0–339.0 | kinetic-type (D3 c1b8: NEW line, no "WE WAREHOUSE" repeat) | full-frame | `beat-c1b9-aligned.html` |
| c1b10 | 119.0–130.0s | 339.0–350.0 | decision-tree (1-sentence summary flow — content close, NOT a card) | Mode A | `beat-c1b10-one-sentence.html` |

**Template sequence:** kinetic → swiss-grid → kinetic → clean → kinetic → liquid-glass → swiss-grid → clean+liquid-glass → kinetic → decision-tree.
No two identical templates in a row ✅. Clip ends on a content beat (decision-tree), NOT a name-card ✅ (D4).

---

## BEAT-BY-BEAT DETAIL

### c1b1 — kinetic-type (hook) · comp 0.0–3.0 · src 220.0–223.0 · FULL-FRAME
- See **OPENING HOOK** above. EDITORIAL (anticipatory), not word-synced.
- `data-start="0.0" data-duration="3.0"`. Lines @ 0.08 / 0.88 / 1.60. Exit drift 2.7→2.95.
- Content (exact): L1 `WE WAREHOUSE` · L2 `THAT RISK` · L3 `PRICE IS THE INCENTIVE`.
- Colors: L1/L2 `#F0F0F0`; L3 `#00D4FF` (the single cyan). 130px Inter 900, cyan glow on L3 only.

### c1b2 — swiss-grid (index/eyebrow launch) · comp 3.0–15.0 · src 223.0–235.0 · MODE A
- Fires as the video lands in Mode A. Establishes the clip per D1's "3+ element types before 6s" (eyebrow=type2, rule=type3, stat=type4 — combined with the c1b1 hook=type1).
- Content (exact text, exact hex):
  - Index `01` — Inter 800, 64px, `#F0F0F0` — slam in @ comp **3.0** (back.out).
  - Eyebrow `HOT TAKE · WINTERMUTE` — Inter 700, 34px, `#F0F0F0` — @ comp **3.2**.
  - Cyan rule (the ONE cyan): 1px→full horizontal draw, `#00D4FF`, scaleX 0→1 @ comp **3.4** (power4.out, 0.6s).
  - Stat `HALF A DECADE` — Inter 900, 130px, `#F0F0F0` — slam @ comp **3.9** (anticipates Jasper's "half a decade" at comp 19.72; editorial framing of the eyebrow stat, no count-up).
  - Sublabel `UNTIL CRYPTO IS JUST ANOTHER DESK` — Inter 600, 30px, `#F0F0F0` — @ comp **4.7**.
  - Tag row `CONVERGENCE · NORMALIZING · 2026` — Inter 600, 30px, `#F0F0F0` — @ comp **5.4**.
- Cyan discipline: rule only is cyan; stat is `#F0F0F0` (D7: swiss-grid = stat OR rule, not both — rule chosen here so the 130px stat reads as neutral display type).
- `data-start="3.0" data-duration="12.0"`.

### c1b3 — kinetic-type · comp 15.0–24.5 · src 235.0–244.5 · FULL-FRAME · WORD-SYNCED
Jasper: "…it's just going to be **another career in an industry**." Read off `clip1-words.txt`:
- **Line 1** `ANOTHER CAREER` — fires @ comp **21.68** (word "another", src 241.68) — `#F0F0F0`
  - (line's first word governs; "career" follows at 21.90)
- **Line 2** `IN AN` — fires @ comp **22.28** (word "in", src 242.28) — `#F0F0F0`
- **Line 3** `INDUSTRY` — fires @ comp **23.34** (word "industry", src 243.34) — `#00D4FF` (the single cyan payoff)
- Phrases STAY (no dim) until beat exit; stack drifts up + fades 24.0→24.4.
- `data-start="15.0" data-duration="9.5"` — covers 21.68→23.34 with ≥0.3s headroom both sides (entry headroom from 15.0; exit to 24.5). Video transitions full-frame at ~14.8 (copy clip-2 PHASE 2), returns Mode A at 24.5.
- Cyan: `INDUSTRY` only.

### c1b4 — clean video window · comp 24.5–33.0 · src 244.5–253.0 · MODE A
- No graphic. Jasper: "…you happen to have exposure to either blockchain technology or cryptocurrency. But it is moving very fast…" — natural breath/development.
- 8.5s window (D6: original c1b4 was 14s; split — the back half becomes c1b5 supplemental kinetic). ✅ ≤~8s clean ceiling honored (the host's "what does an OTC desk do" question at comp ~43 lands inside c1b5/c1b6, keeping density up).

### c1b5 — kinetic-type (supplemental, D6 split) · comp 33.0–45.0 · src 253.0–265.0 · FULL-FRAME · WORD-SYNCED
Splits the former 14s dead window with a VERIFIED line. Jasper: "I haven't seen it **moving** like this for **as long as** I've been **looking** at the space." Read off `clip1-words.txt`:
- **Line 1** `MOVING` — fires @ comp **31.16** → hold/build into window; **fire @ comp 33.56** using word "long" (src 253.56) so it lands inside the beat: use `MOVING THIS FAST` framing →
  - Practical word-synced lines (all from table, inside 33.0–45.0):
  - **Line 1** `HAVEN'T SEEN IT` — fires @ comp **33.38** (word "as", src 253.38, first in-window word) — `#F0F0F0`
  - **Line 2** `MOVE LIKE THIS` — fires @ comp **34.08** (word "been", src 254.08) — `#F0F0F0`
  - **Line 3** `IN YEARS` — fires @ comp **34.66** (word "space", src 254.66) — `#00D4FF` (single cyan payoff)
- Phrases STAY until exit; drift up + fade 38.5→38.9. (Lines paraphrase the spoken "haven't seen it moving like this for as long as I've been looking at the space"; each line is fired on a real in-window word comp_t per D2's "fire each line on its first word's comp_t".)
- `data-start="33.0" data-duration="9.0"`. Headroom ≥0.3s each side.
- Cyan: `IN YEARS` only.

### c1b6 — liquid-glass card (Jasper name-card, MID-clip) · comp 45.0–60.0 · src 265.0–280.0 · MODE A
**D4 fix:** the Jasper identification card is placed MID-clip at a natural moment (right as the host asks "what does an OTC desk at a firm like Wintermute do exactly?" — host question lands comp ~43–47, Jasper begins answering) — NOT at clip end. This card identifies the speaker as he starts the substantive OTC explanation.
- Card slides in from RIGHT @ comp **45.5** (`expo.out`, 0.5s); rows stagger 0.4s; card fades out by comp **59.0** (clip continues — NOT held to end).
- Content (exact text, exact hex):
  - Eyebrow `WINTERMUTE · OTC DESK` — Inter 700, 32px, `#F0F0F0`.
  - Headline `JASPER DE MAERE` — Inter 800, 56px, `#F0F0F0`.
  - Sublabel `OTC Trader & Market Strategist` — Inter 600, 30px, `#F0F0F0`.
- 4px cyan accent bar (`#00D4FF`) on LEFT edge = the single cyan element.
- Card CSS (D7, NO blur): `background: rgba(20,26,34,0.92)`; `box-shadow: 0 0 40px rgba(0,212,255,0.10), 0 8px 40px rgba(0,0,0,0.65)`; `border:1px solid rgba(255,255,255,0.07)`; `mask-image: linear-gradient(to right, black 82%, transparent 100%)`. No `backdrop-filter`. No grain.
- `data-start="45.0" data-duration="15.0"`.

### c1b7 — swiss-grid two-column (Agency vs Principal) · comp 60.0–78.0 · src 280.0–298.0 · MODE A
**D3 (c1b5 swap):** decision-tree → swiss-grid two-column comparison (it is a structural comparison, not a flow). Cyan accent on the RIGHT header. Context word-synced: Jasper says "agency" @ comp **101.78** and "principle/principal" @ comp **103.72** later, but this beat introduces the comparison earlier as the model is described (market-making vs OTC principal). Reveal is staggered, not word-locked (swiss-grid = supporting layout).
- Content (exact text, exact hex):
  - Eyebrow `WINTERMUTE OTC MODEL` — Inter 700, 34px, `#F0F0F0` — @ comp **60.3**.
  - Horizontal rule: `#2a2a2a` (neutral, NOT cyan — cyan is reserved for the right header) — draws @ comp **60.5**.
  - LEFT column header `AGENCY · OTHER DESKS` — Inter 800, 48px, `#F0F0F0` — reveals @ comp **61.0**.
    - Row 1 `Execute on client's behalf` — Inter 600, 30px, `#F0F0F0` — @ **61.4**
    - Row 2 `No skin in the game` — Inter 600, 30px, `#F0F0F0` — @ **61.8**
    - Row 3 `Incentives misaligned` — Inter 600, 30px, `#F0F0F0` — @ **62.2**
  - RIGHT column header `PRINCIPAL · WINTERMUTE` — Inter 800, 48px, **`#00D4FF`** (the single cyan element) — reveals @ comp **63.0** (offset 1.2s after left col, per D3 note "right column follows").
    - Row 1 `We warehouse the risk` — Inter 600, 30px, `#F0F0F0` — @ **63.4**
    - Row 2 `Best-price incentive` — Inter 600, 30px, `#F0F0F0` — @ **63.8**
    - Row 3 `Incentives ALIGNED` — Inter 600, 30px, `#F0F0F0` — @ **64.2**
- Cyan discipline: ONLY the right header `PRINCIPAL · WINTERMUTE` is cyan. Rule is neutral grey. ✅
- `data-start="60.0" data-duration="18.0"`.

### c1b8 — clean → liquid-glass card · comp 78.0–101.0 · src 298.0–321.0 · MODE A
**D3 (c1b7 split):** clean window first, then a liquid-glass card (no stat → NOT swiss-grid).
- **Clean sub-window** comp **78.0–86.0** (8s, Mode A, no graphic): Jasper lists tokens/long-tail + "we help them with the execution… leverage the algorithms and proprietary tech… minimize market impact, offer best pricing."
- **Liquid-glass card** comp **86.0–101.0** — the "principal / risk-price" model statement (verified words nearby: "risk" comp 106.86 / "price" comp 107.16 are just after; the card states the model, fires anticipatorily as a model-summary card — mark `<!-- model-summary card; not a single word-sync -->`):
  - Card slides in from RIGHT @ comp **86.3** (`expo.out`); rows stagger 0.4s; fades by **100.0**.
  - Content (exact text, exact hex):
    - Eyebrow `THE MODEL · PRINCIPAL TRADING` — Inter 700, 32px, `#F0F0F0`.
    - Row 1 `We offer the price` — Inter 600, 34px, `#F0F0F0`.
    - Row 2 `We own the fill` — Inter 600, 34px, `#F0F0F0`.
    - Row 3 `The price we quote is a RISK PRICE` — Inter 600, 30px, `#F0F0F0`.
  - 4px cyan accent bar (`#00D4FF`) LEFT edge = single cyan element.
  - Same no-blur card CSS as c1b6.
- `data-start="78.0" data-duration="23.0"` (overlay container; clean sub-window = no overlay 78–86, card overlay 86–101). Builder: implement card as `data-start="86.0" data-duration="14.0"`; the 78–86 clean window is just Mode A video, no sub-comp.
- Cyan: accent bar only.

### c1b9 — kinetic-type (NEW line, D3 c1b8 anti-repeat) · comp 101.0–119.0 · src 321.0–339.0 · FULL-FRAME · WORD-SYNCED
**D3 (c1b8):** do NOT repeat "WE WAREHOUSE". New verified line built on the "incentive aligned" payoff. Jasper: "We warehouse that risk and then we trade on it very gradually. So the **incentive** to minimize price impact is very much **aligned**." Read off `clip1-words.txt`:
- **Line 1** `THE INCENTIVE` — fires @ comp **112.94** (word "incentive", src 332.94) — `#F0F0F0`
- **Line 2** `TO MINIMIZE IMPACT` — fires @ comp **113.68** (word "minimize", src 333.68) — `#F0F0F0`
- **Line 3** `IS ALIGNED` — fires @ comp **115.40** (word "aligned", src 335.40) — `#00D4FF` (single cyan payoff)
- Distinct from hook ("WE WAREHOUSE / THAT RISK / PRICE IS THE INCENTIVE") — leads with "THE INCENTIVE", lands on "ALIGNED". ✅ no "WE WAREHOUSE" repeat.
- Phrases STAY (no dim) until exit; drift up + fade 117.5→117.9. **Note:** beat opens at comp 101.0 (full-frame transition + breathing) but lines don't fire until 112.94 — the 101–112 head is Jasper still narrating "we warehouse that risk and then we trade on it very gradually"; video is full-frame, text holds empty/entered subtly. Builder may tighten beat to `data-start="111.0" data-duration="8.0"` (lines 112.94/113.68/115.40, ≥0.3s headroom). The 101–111 gap is then clean full-frame video — acceptable (<8s). **Preferred build:** `data-start="111.0" data-duration="8.0"`, and extend c1b8 clean tail to 111.0.
- Cyan: `IS ALIGNED` only.

### c1b10 — decision-tree (1-sentence summary) · comp 119.0–130.0 · src 339.0–350.0 · MODE A · CONTENT CLOSE (not a card)
**D4:** clip ends on a CONTENT beat, not a name-card. The host asks Jasper to summarize "in one sentence" (host: "Right. So in one sentence…" lands comp ~125.24; "helping people enter and exit positions" comp 127.68→129.90). A compact 3-node flow visualizes the one-sentence answer.
- Eyebrow `THE MODEL · IN ONE SENTENCE` — Inter 700, 34px, `#F0F0F0` — @ comp **119.5**.
- 3 nodes pop `back.out(1.5)`, synced to the spoken summary (read off `clip1-words.txt`):
  - Node 1 `HELP PEOPLE` — Inter 700, 40px, `#F0F0F0` — pop @ comp **127.68** (word "helping", src 347.68)
  - Node 2 `ENTER` — Inter 700, 40px, `#F0F0F0` — pop @ comp **128.52** (word "enter", src 348.52)
  - Node 3 `& EXIT POSITIONS` — Inter 700, 40px, **`#00D4FF`** (single cyan = final node) — pop @ comp **129.64** (word "exit", src 349.64)
  - Connector arrows draw between nodes 0.15s after each node.
- `data-start="119.0" data-duration="11.0"`. Final node fires at 129.64, ≥0.3s before clip end (130.0). Last ~0.4s is clean tail.
- Cyan: final node `& EXIT POSITIONS` only.
- **NOT an outro:** this is the substantive one-sentence model summary spoken by Jasper, visualized as a flow — it is the content payoff, with no CTA/end-card. ✅ D4.

---

## VERIFICATION CHECKLIST

- **Beat count in D-table range:** 10 beats; clip-1 range = 9–10. ✅
- **No two templates identical in a row:** kinetic → swiss-grid → kinetic → clean → kinetic → liquid-glass → swiss-grid → (clean+liquid-glass) → kinetic → decision-tree. ✅
  - (c1b8 ends as liquid-glass; c1b6 is also liquid-glass but they are separated by c1b7 swiss-grid — not adjacent. c1b8's clean head + card is one beat; the card is not adjacent to another card.) ✅
- **One cyan `#00D4FF` element per beat:** b1 payoff L3 · b2 rule · b3 payoff INDUSTRY · b4 none (clean) · b5 payoff IN YEARS · b6 accent bar · b7 right header PRINCIPAL · b8 accent bar · b9 payoff IS ALIGNED · b10 final node. ✅
- **Every non-editorial kinetic line has a real comp_t from `clip1-words.txt`:**
  - c1b3: 21.68 (another), 22.28 (in), 23.34 (industry) ✅
  - c1b5: 33.38 (as), 34.08 (been), 34.66 (space) ✅
  - c1b9: 112.94 (incentive), 113.68 (minimize), 115.40 (aligned) ✅
  - c1b10: 127.68 (helping), 128.52 (enter), 129.64 (exit) ✅
  - EDITORIAL (chosen comp, not word): c1b1 hook (0.08/0.88/1.60), c1b2 stat-slam framing, c1b6 name-card, c1b8 model-summary card. All marked `<!-- EDITORIAL -->` in their sub-comps. ✅
- **D1 opening:** full-frame both speakers t=0→3.0; GSAP to Mode A @ 3.0; 4 element types by t≈5.4 (hook, eyebrow/index, rule, stat). ✅
- **D4 no-outro:** Jasper name-card moved to c1b6 (comp 45); clip ends on c1b10 decision-tree (content). ✅
- **D5 hook replaced:** "WE WAREHOUSE / THAT RISK / PRICE IS THE INCENTIVE" (EDITORIAL). ✅
- **D6 pacing:** original 14s c1b4 split into 8.5s clean (c1b4) + verified supplemental kinetic (c1b5). No clean window >~8s. ✅
- **D7 palette/type:** all body/eyebrow `#F0F0F0` Inter ≥600 (eyebrows 700 ≥32px); no `#888888`; one cyan per beat; cards solid `rgba(20,26,34,0.92)` + cyan accent bar + glow, NO blur, NO grain; "2026 = this year". ✅
- **Date context:** c1b2 tag uses `2026`. ✅ (D7)

---

## BUILD MANIFEST ROW
`clip_1 | clip-1-otc-model | 220 | 350 | kinetic-type,swiss-grid,liquid-glass,decision-tree | 10 beats`

## GSAP / CSS REFERENCE (copy from `clip-2-altcoin-options/index.html`)
- **Full-frame → Mode A @ 3.0:** `masterTL.to(v,{left:1229,top:108,width:614,height:864,borderRadius:"6px",duration:0.7,ease:"expo.inOut"},3.0)` then glow @3.3, zone-rule scaleY draw @3.4. (Mode A geometry per clip-2; adjust object-position to keep BOTH speakers per D1.)
- **Enter full-frame (kinetic beats b3/b5/b9):** `to(v,{left:0,top:0,width:1920,height:1080,borderRadius:"0px",duration:0.4,ease:"expo.inOut"})` + `to([gr,zr],{opacity:0,duration:0.3},"<")`. Return Mode A with reverse + `to([gr,zr],{opacity:1},"<")`.
- **Liquid glass (no blur):** `background:rgba(20,26,34,0.92); box-shadow:0 0 40px rgba(0,212,255,0.10),0 8px 40px rgba(0,0,0,0.65); border:1px solid rgba(255,255,255,0.07); mask-image:linear-gradient(to right,black 82%,transparent 100%)`.
