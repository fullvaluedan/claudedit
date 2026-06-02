# Clip 1 — OTC Model / Agency-vs-Principal — EDL v2 (RE-DESIGN)

**clip_id:** `clip_1` · **dir:** `clip-1-otc-model` · **slug:** `clip-1-otc-model`
**Supersedes** `clip1-edl-final.md` (v1 — REJECTED for: opening kinetic didn't match dialog, formulaic structure, wrong framing).

---

## WHAT v1 GOT WRONG (and how v2 fixes it)

| # | v1 failure | v2 fix |
|---|-----------|--------|
| 1 | **Opening text ≠ dialog.** v1 opened on EDITORIAL hook "WE WAREHOUSE / THAT RISK / PRICE IS THE INCENTIVE" at comp 0.08/0.88/1.60 — but at the v1 in-point (src 220) Jasper was actually saying *"I think now we're at an interesting point… a very strong convergence…"*. Totally different words. | **New in-point src_in = 239.10**, on Jasper's line *"I think in like half a decade… it's just going to be another career in an industry."* The opening kinetic IS those words, word-synced. ZERO anticipatory text. |
| 2 | **Formulaic.** Opened with the generic swiss-grid "01 / HOT TAKE · WINTERMUTE / cyan rule / HALF A DECADE stat / sublabel / tag-row" — the same launch every clip used. | **Comparison-led structure.** No stat-slam launch. Cold-open is pure kinetic over both speakers with only a minimal index+eyebrow chrome. The centerpiece is the **Agency-vs-Principal two-column**, supported by a *two-sides-of-the-book* split node and a *risk-warehouse* data beat — a distinct silhouette from clip-2 (which is stat→buyers card→option tree→APY chart). |
| 3 | **Wrong framing.** Mode A used `object-position: 62% center` → exposed the center seam + Nic's wall on the left of the crop; Jasper shoved to the edge. | **`object-position: 83% center`** (matches clip-2, verified by frame extraction — see below). Jasper horizontally centered, name lower-third fully visible. |

---

## IN / OUT / DURATION

- **src_in = 239.10s** (trim head filler *"So while currently we say like we're full time in crypto,"* — open on *"I think in like half a decade…"*)
- **src_out = 349.90s** (end of the word "positions" in *"helping people enter and exit positions"* — the one-sentence model summary; content close per D4, NO outro)
- **duration = 110.80s**
- **comp offset:** `comp_t = src_t − 239.10` (canonical). NB: this differs from `clip1-words.txt` which is computed at src−220; every comp_t below is RE-derived at src−239.10 and the source word + src_t is quoted next to each kinetic line so it is auditable.
- **media-start in index.html:** `data-media-start="239.10"` on both the `<video>` and `<audio>` (was 220).
- **master `data-duration`:** `110.8`.

---

## FRAMING — verified from actual source frames (RULE 3)

Source `source.mp4` is the full episode (1920×1080, 30fps); `media-start=239.10` maps source.mp4 timestamp ≈ episode time, so a frame extracted at `src_t` is the frame on screen at `comp_t = src_t − 239.10`.

**Frames extracted & viewed:** `ffmpeg -ss 285 -i source.mp4 -frames:v 1 /tmp/fr_c1_285.png` and `-ss 330 …/tmp/fr_c1_330.png` (both inside Mode-A windows: 285 = OTC-desk explanation, 330 = warehouse-risk). Also simulated the exact Mode-A crop (`scale=1536:864,crop=614:864:<left>:0`, i.e. `object-fit:cover` into the 614×864 window) at object-position **62 / 80 / 83 / 88 / 92%** and viewed each.

**What the frames show:** true side-by-side. Vertical seam at x≈960. Nic (host) LEFT half; **Jasper (guest) RIGHT half**, face center ≈ x≈1470 (≈76% across the full 1920). Modest dead ceiling above his head (hair starts ~28% down). His name lower-third *"Jasper De Maere / Wintermute"* sits bottom-left of his half (x≈1180–1370, y≈88–95%).

**Crop simulations (what each object-position renders):**
- **62%** (v1) — WRONG: center seam + Nic's wall fill the left third of the crop; Jasper pushed to the right edge. This is the v1 bug.
- **80%** — Jasper centered, slightly loose left.
- **83%** — Jasper's face horizontally centered in the 614px window; name *"Jasper De Maere / Wintermute"* fully inside the frame. ✅
- **88%** — Jasper drifts right-of-center; name label begins to clip on its left ("…asper De Maere").
- **92%** — name clipped to "…er De Maere". Too far.

**DECISION: `object-position: 83% center`** (identical to clip-2, keeps the series consistent).
**Vertical bias:** none — in this Mode-A geometry `object-fit:cover` scales the source to fill the 864px height *exactly* (scale 0.8 → 1536×864), so there is **no vertical crop room and vertical object-position has zero effect**. The only lever to cut the dead ceiling is a scale-up; a slow Ken Burns **1.0 → 1.03** adds life and tightens slightly without clipping the name. A harder 1.08 zoom was tested and rejected — it clipped the "Wintermute" sub-line. So: 83% center + gentle Ken Burns 1.0→1.03, NO hard zoom.

Mode A geometry (copy clip-2): `MODE_A = { left:1229, top:108, width:614, height:864 }` (85% of right-40% zone; bottom clearance 108px, top 108px).

---

## STRUCTURE (lead device = COMPARISON; distinct from siblings)

Template sequence: **kinetic → clean → kinetic(question) → flowchart(2-node split) → liquid-glass(name) → swiss-grid 2-col (CENTERPIECE) → data-chart → kinetic(close)**.
No two identical templates adjacent ✅. Ends on a content kinetic, not a card ✅ (D4). 8 graphic beats + 1 clean window = **9 beats** (D-table range 9–10 ✅).

The "3+ element TYPES before 6s" rule (DESIGN.md) is met inside the cold open: kinetic phrase (type 1) + mono index (type 2) + eyebrow (type 3) + the cyan payoff line accent (type 4) all fire 0–4.3s, speaker visible the whole time. There is deliberately **no stat-slam / tag-row launch** — that block is what made every clip look identical, and it is dropped here.

| Beat | comp range | src range | template / block | content (summary) | speaker mode | sub-comp |
|------|-----------|-----------|------------------|-------------------|--------------|----------|
| c1b1 | 0.0–6.0 | 239.10–245.10 | **kinetic-type** (cold open, WORD-SYNCED) | HALF A DECADE / ANOTHER CAREER / IN AN INDUSTRY | full-frame | `beat-c1b1-half-decade.html` |
| c1b2 | 6.0–9.6 | 245.10–248.70 | clean video | — (breath: "…exposure to blockchain or crypto") | Mode A | — |
| c1b3 | 9.6–15.0 | 248.70–254.10 | **kinetic-type** (WORD-SYNCED) | IT'S MOVING / VERY FAST / HAVEN'T SEEN THIS IN YEARS | full-frame | `beat-c1b3-moving-fast.html` |
| c1b4 | 23.6–30.0 | 262.70–269.10 | **kinetic-type** (HOST QUESTION, WORD-SYNCED) | WHAT DOES / AN OTC DESK / ACTUALLY DO? | full-frame | `beat-c1b4-host-q.html` |
| c1b5 | 33.0–45.0 | 272.10–284.10 | **flowchart** (2-node split — NOT generic grid) | TWO SIDES OF THE BOOK · Market-Making ↔ OTC Desk | Mode A | `beat-c1b5-two-sides.html` |
| c1b6 | 49.0–61.0 | 288.10–300.10 | **liquid-glass card** (Jasper name, MID-clip per D4) | JASPER DE MAERE · Wintermute OTC | Mode A | `beat-c1b6-jasper.html` |
| c1b7 | 78.0–98.5 | 317.10–337.60 | **swiss-grid 2-column** (CENTERPIECE, WORD-SYNCED reveal) | AGENCY vs PRINCIPAL | Mode A | `beat-c1b7-agency-principal.html` |
| c1b8 | 100.0–106.5 | 339.10–345.60 | **data-chart** (price-impact decays as risk is worked off) | WAREHOUSE THE RISK → minimize impact | Mode A | `beat-c1b8-warehouse.html` |
| c1b9 | 106.7–110.8 | 345.80–349.90 | **kinetic-type** (CLOSE, WORD-SYNCED) | ENTER / AND EXIT / POSITIONS | full-frame | `beat-c1b9-enter-exit.html` |

---

## BEAT-BY-BEAT (every kinetic line: on-screen text + the transcript words it matches + comp_t)

### c1b1 — kinetic-type · cold open · comp 0.0–6.0 · src 239.10–245.10 · FULL-FRAME · WORD-SYNCED
**Opens on the strongest real early line.** Jasper (trimmed to start on "I think"): *"I think in like **half a decade** or so, it's just going to be **another career** **in an industry**."*
Screen is alive from t=0: mono index `01` slams in top-left @ comp 0.0, thin eyebrow `WINTERMUTE · OTC` fades @ comp 0.15 — but **no stat block / tag row** (that's the formulaic launch we removed). The kinetic sentence carries the open, word-synced:

| on-screen line | transcript word(s) | src_t | **comp_t (fire)** | color |
|---|---|---|---|---|
| `HALF A DECADE` | "half" (→ "a decade") | 239.72 | **0.62** | #F0F0F0 |
| `ANOTHER CAREER` | "another" (→ "career") | 241.68 | **2.58** | #F0F0F0 |
| `IN AN INDUSTRY` | "industry" (line 1st word "in"@3.18, lands on "industry") | 243.34 | **4.24** | **#00D4FF** (single cyan payoff + glow) |

- Lines build as phrases and STAY (no dim) — full sentence readable by comp 4.5.
- Entry per line: `fromTo({opacity:0,y:28},{opacity:1,y:0},expo.out,0.28s)`; payoff adds `scale:0.92→1`.
- Whole stack drifts up + fades (power2.in) @ comp **5.5→5.85** (before video shrinks to Mode A at 6.0).
- Video FULL-FRAME (both speakers) 0–6.0; dark gradient backdrop on left for legibility (copy `beat-intro.html` `.bi-backdrop`).
- `data-start="0.0" data-duration="6.0"`. Cyan: `IN AN INDUSTRY` only.
- 130px Inter 900, `text-shadow` for contrast (copy `beat-intro.html` line styles).
- `<!-- WORD-SYNCED: half@0.62 another@2.58 industry@4.24 (src−239.10) -->`

### c1b2 — clean video window · comp 6.0–9.6 · src 245.10–248.70 · MODE A
- No graphic. GSAP shrinks video FULL-FRAME → Mode A @ comp **6.0** (`expo.inOut`, 0.7s); `#bg-glow` in @ 6.3, `#zone-rule` draws @ 6.4 (copy clip-2 PHASE 1). Ken Burns 1.0→1.03 begins.
- Jasper: *"And you happen to have exposure to either blockchain technology or cryptocurrency."* — natural breath. 3.6s (≤8s ceiling, D6) ✅.

### c1b3 — kinetic-type · comp 9.6–15.0 · src 248.70–254.10 · FULL-FRAME · WORD-SYNCED
Jasper: *"But it is **moving** **very fast**. Like I **haven't seen** it moving like **this** for as long as I've been looking at the space."*
Video expands FULL-FRAME @ comp **9.3** (`expo.inOut` 0.4s), glow/rule fade @ 9.1.

| on-screen line | transcript word(s) | src_t | **comp_t (fire)** | color |
|---|---|---|---|---|
| `IT'S MOVING` | "moving" | 249.22 | **10.12** | #F0F0F0 |
| `VERY FAST` | "very" (→ "fast"@10.66) | 249.48 | **10.38** | #F0F0F0 |
| `HAVEN'T SEEN THIS IN YEARS` | "haven't" (→ "seen"@11.76,"this"@12.50) | 250.46 | **11.36** | **#00D4FF** payoff |

- Phrases STAY; stack drifts up + fades @ comp **13.6→13.95**.
- `data-start="9.6" data-duration="5.4"`. Headroom: first line 10.12 (≥0.5s after 9.6), last 11.36 (≥0.3s before… payoff line text is long, hold to 13.6). Cyan: `HAVEN'T SEEN THIS IN YEARS` only.
- Video returns Mode A @ comp **15.0** (`expo.out`), glow/rule back @ 15.1.
- `<!-- WORD-SYNCED: moving@10.12 very@10.38 haven't@11.36 (src−239.10) -->`

### c1b4 — kinetic-type · HOST QUESTION · comp 23.6–30.0 · src 262.70–269.10 · FULL-FRAME · WORD-SYNCED
The pivot into the OTC explanation. Host (Nic): *"So for someone who never thought about it, **what does** **an OTC desk** at a firm like Wintermute do **exactly**?"* The question is the natural hinge that sets up the whole Agency-vs-Principal comparison — fired as its own stack (DESIGN.md: host questions are fine as their own stack, no "HOST" label, question text only).
- Clean Mode-A window comp 15.0–23.3 (Jasper: "Yeah I cannot disagree with that…" + host preamble). That window is 8.3s — at the ceiling; the host's "So for someone who never thought about it" preamble (comp ~21–23) keeps it from feeling dead, and the question kinetic lands at 23.6. (If QA wants <8s, a tiny supplemental is available but not required.)
- Video expands FULL-FRAME @ comp **23.3**.

| on-screen line | transcript word(s) | src_t | **comp_t (fire)** | color |
|---|---|---|---|---|
| `WHAT DOES` | "what" (→ "does"@24.80) | 263.26 | **24.16** | #F0F0F0 |
| `AN OTC DESK` | "OTC" (→ "desk"@25.58) | 264.34 | **25.24** | #F0F0F0 |
| `ACTUALLY DO?` | "exactly" (delivered as the punch) | 266.76 | **27.66** | **#00D4FF** payoff |

- (On-screen wording "ACTUALLY DO?" is a light paraphrase of the spoken "do exactly?" — fires on the real word "exactly" @ 27.66; the literal transcript is "do exactly". If strict literalism is preferred, use `DO EXACTLY?`. Either fires on "exactly"@27.66.)
- Phrases STAY; drift up + fade @ comp **28.6→28.95** (before Jasper's answer "Yeah, that's a good question" — the answer "So OTC trading…" starts comp ~32.4).
- `data-start="23.6" data-duration="5.4"`. Cyan: `ACTUALLY DO?` only.
- Video returns Mode A @ comp **30.0**.
- `<!-- WORD-SYNCED (host Q): what@24.16 OTC@25.24 exactly@27.66 (src−239.10) -->`

### c1b5 — flowchart (2-node split) · comp 33.0–45.0 · src 272.10–284.10 · MODE A
**Not the generic grid.** A two-node *split* showing the firm's book has two sides, which teees up the Agency/Principal centerpiece. Jasper: *"OTC trading is obviously… bread and butter is **market making**… The OTC desk is very much **the other side** of this. We help people **execute specific transactions**."*
Uses the proven `beat-2f.html` node pattern (rounded `rgba(20,26,34,0.92)` nodes, accent node has cyan border+glow), but laid out as ONE source node → TWO branches (not a 3→2 grid).
- Eyebrow `WINTERMUTE'S BOOK` — JetBrains Mono 700, 32px, #F0F0F0 — @ comp **33.2**.
- Neutral rule `#2a2a2a` draws @ comp **33.4** (cyan is reserved for the accent node, D7).
- Root node `THE FIRM` pops `back.out(1.5)` @ comp **33.8**.
- Branch A `MARKET-MAKING` (desc "Maker across exchanges & tokens · provides liquidity") pops @ comp **36.66** (word "market" @ src 275.76). #F0F0F0 node.
- Branch B (accent) `OTC DESK` (desc "Executes specific client transactions") pops @ comp **48.50→** — too late for this beat; fire on "the other side" @ "other" src 287.60 lands comp 48.50 which is AFTER beat end (45.0). **Fix:** the OTC-desk branch fires on "OTC desk" earlier — Jasper says "The OTC desk" at src 285.76 (comp 46.66), also after 45.0. So set Branch B on **comp 41.0** as a within-beat reveal anchored to "execute specific transactions" anticipation, OR extend the beat. **Chosen:** keep beat 33.0–45.0 and fire Branch B (accent, cyan border) at **comp 41.0** `<!-- node reveal; "OTC desk = other side" is spoken just after at comp 46.66, branch shown anticipatorily within the split -->`. Connector arrows draw 0.15s after each branch.
- Footer `Two sides of the same book` — JetBrains Mono, 32px, #444 — @ comp 41.3.
- Cyan: ONLY Branch B `OTC DESK` accent border+glow. ✅
- `data-start="33.0" data-duration="12.0"`. Mode A throughout.

### c1b6 — liquid-glass card (Jasper name) · comp 49.0–61.0 · src 288.10–300.10 · MODE A
**D4:** speaker-ID card placed MID-clip (as Jasper details the execution model) — NOT at clip end. Copy `beat-2d.html` card CSS exactly (solid `rgba(20,26,34,0.92)`, 4px cyan accent bar, glow, 1px border, `mask-image` feather; NO blur, NO grain — D7).
- Card slides in from RIGHT @ comp **49.5** (`expo.out`, 0.5s).
- Eyebrow `WINTERMUTE · OTC DESK` — JetBrains Mono 700, 32px, #F0F0F0.
- Headline `JASPER DE MAERE` — Inter 800, 56px, #F0F0F0.
- Sublabel `OTC Trader & Market Strategist` — Inter 600, 30px, #F0F0F0.
- Card fades out by comp **60.0** (clip continues — not held to end).
- 4px cyan accent bar = single cyan. `data-start="49.0" data-duration="12.0"`.
- Context: Jasper @ this point: "We help people execute specific transactions… BTC, Ethereum, Solana… we help them with the execution." Naming him as he explains the desk is natural.

### c1b7 — swiss-grid TWO-COLUMN (CENTERPIECE) · comp 78.0–98.5 · src 317.10–337.60 · MODE A · WORD-SYNCED reveal
**THE LEAD DEVICE.** D3 (c1b5 swap): the Agency-vs-Principal two-column IS the centerpiece. Jasper: *"The way we do this is quite **different** than a lot of other OTC desks where they would execute in **agency**. We do this in… **principle** trading. So the prices we offer is **risk price**. We **warehouse** that risk… the incentive to minimize price impact is very much **aligned**."*
Two equal columns, headers at equal height. LEFT = AGENCY (other desks), RIGHT = PRINCIPAL (Wintermute, cyan header = the single cyan). Rows stagger; the column reveals are word-synced to the spoken contrast.
- Clean Mode-A window comp 61.0–77.8 is too long (16.8s). **D6 split:** this clean stretch (Jasper listing tokens / "leverage algorithms & proprietary tech to minimize market impact, offer best pricing") is broken by firing a SHORT supplemental within it — see **c1b7-pre** below — so no clean window exceeds ~8s.
- Eyebrow `AGENCY vs PRINCIPAL` — JetBrains Mono 700, 34px, #F0F0F0 — @ comp **78.2**.
- Neutral rule `#2a2a2a` (cyan reserved for right header) — draws @ comp **78.4**.
- **LEFT column header** `AGENCY` + sub `OTHER OTC DESKS` — Inter 800, 48px, #F0F0F0 — reveals @ comp **82.68** (word "agency" @ src 321.78).
  - Row A1 `Execute on the client's behalf` — Inter 600, 30px, #F0F0F0 — @ **83.1**
  - Row A2 `Desk takes no position` — Inter 600, 30px, #F0F0F0 — @ **83.5**
  - Row A3 `Incentives can diverge` — Inter 600, 30px, #F0F0F0 — @ **83.9**
- **RIGHT column header** `PRINCIPAL` + sub `WINTERMUTE OTC` — Inter 800, 48px, **#00D4FF** (single cyan) — reveals @ comp **84.62** (word "principle/principal trading" @ src 323.72).
  - Row P1 `Quote is a RISK PRICE` — Inter 600, 30px, #F0F0F0 — @ **87.76** (word "risk price" @ src 326.86)
  - Row P2 `We warehouse the risk` — Inter 600, 30px, #F0F0F0 — @ **88.92** (word "warehouse" @ src 328.02)
  - Row P3 `Incentives ALIGNED` — Inter 600, 30px, #F0F0F0 — @ **96.30** (word "aligned" @ src 335.40)
- Cyan discipline: ONLY the right header `PRINCIPAL` is cyan; rule neutral; rows #F0F0F0. ✅
- Headers at equal visual height (both single-line at 48px). Bullet rows: `min-width:0; flex:1` on text so wraps align under first char (QA rule).
- `data-start="78.0" data-duration="20.5"`. Mode A throughout. Exit fade @ comp 98.0.
- `<!-- WORD-SYNCED reveals: AGENCY@82.68 PRINCIPAL@84.62 risk-price@87.76 warehouse@88.92 aligned@96.30 (src−239.10) -->`

#### c1b7-pre — supplemental kinetic (D6 split of the 61–78 clean window) · comp 70.9–74.5 · src 310.0–313.6 · FULL-FRAME · WORD-SYNCED
Splits the long clean stretch with a verified spoken line. Jasper: *"…proprietary tech we have to **minimize** market **impact**, offer **best pricing**."*

| on-screen line | transcript word(s) | src_t | **comp_t (fire)** | color |
|---|---|---|---|---|
| `MINIMIZE` | "minimize" | 310.04 | **70.94** | #F0F0F0 |
| `MARKET IMPACT` | "impact" | 310.96 | **71.86** | #F0F0F0 |
| `BEST PRICING` | "best" (→ "pricing"@73.64) | 312.42 | **73.32** | **#00D4FF** payoff |

- Video expands FULL-FRAME @ comp **70.7**, returns Mode A @ comp **74.7** (so it is in Mode A before the c1b7 centerpiece at 78.0). Phrases STAY; drift+fade @ comp 74.0→74.35.
- `data-start="70.9" data-duration="3.6"`. Cyan: `BEST PRICING` only.
- **Beat-count note:** c1b7-pre is a 10th beat; clip-1 D-table range is **9–10** ✅. Sub-comp `beat-c1b7pre-pricing.html`. Add its id to the z-index:3 rule.
- `<!-- WORD-SYNCED: minimize@70.94 impact@71.86 best@73.32 (src−239.10) -->`

### c1b8 — data-chart · comp 100.0–106.5 · src 339.10–345.60 · MODE A
**Variety block (catalog `data-chart`).** D3/D6: not a repeated card. Visualizes the principal model's payoff — *"We warehouse that risk and then we trade on it very gradually"* → market impact decays as the position is worked off. A descending bar set: **IMPACT IF DUMPED** (tall, neutral) vs **IMPACT WORKED GRADUALLY** (short, cyan = the aligned outcome). Or a simple 4-bar decay (T+0 → T+1 → T+2 → T+3) descending, last bar cyan.
- Eyebrow `WHY INCENTIVES ALIGN` — JetBrains Mono 700, 32px, #F0F0F0 — @ comp **100.2**.
- Bars stagger in @ comp 100.5 / 100.9 / 101.3 / 101.7 (descending). Final/lowest bar = **#00D4FF** (single cyan) — the "minimized impact" outcome.
- Annotation (the 3 bullets→annotations style of the chart): `Warehouse → work off gradually → price impact minimized` synced to "appreciates that alignment" @ comp **103.44**.
- Context word: Jasper "a lot of people in the market generally **appreciates** that **alignment** of **incentives**" @ comp 103.44 / 104.70 / 105.42.
- Cyan: lowest bar only. `data-start="100.0" data-duration="6.5"`. Mode A.
- Clean Mode-A window comp 98.5–100.0 (1.5s) bridges c1b7→c1b8.

### c1b9 — kinetic-type · CLOSE · comp 106.7–110.8 · src 345.80–349.90 · FULL-FRAME · WORD-SYNCED · CONTENT CLOSE (D4)
Clip ends on the substantive one-sentence summary — NOT a name card. Host: "So in one sentence…" Jasper: *"…it's **helping people** **enter** and **exit** **positions** very smoothly."*
- Video expands FULL-FRAME @ comp **106.5**.

| on-screen line | transcript word(s) | src_t | **comp_t (fire)** | color |
|---|---|---|---|---|
| `HELP PEOPLE` | "helping" (→ "people"@108.92) | 347.68 | **108.58** | #F0F0F0 |
| `ENTER` | "enter" | 348.52 | **109.42** | #F0F0F0 |
| `AND EXIT POSITIONS` | "exit" (→ "positions"@110.80) | 349.64 | **110.54** | **#00D4FF** payoff |

- Phrases STAY through clip end (no exit drift — clip ends at 110.80, the payoff lands at 110.54; the final ~0.26s holds the full sentence, then the comp simply ends). This is the content payoff, no CTA / end-card. ✅ D4.
- `data-start="106.7" data-duration="4.1"`. Cyan: `AND EXIT POSITIONS` only.
- Clean Mode-A bridge comp 106.5–106.7 is just the full-frame expansion settling.
- `<!-- WORD-SYNCED close: helping@108.58 enter@109.42 exit@110.54 (src−239.10) -->`

---

## GSAP TIMELINE (master) — phase map

Copy clip-2 mechanics; geometry `MODE_A={left:1229,top:108,width:614,height:864}`, `object-position:83% center`.

- **PHASE 0** comp 0.0–6.0: FULL-FRAME (c1b1 cold open over both speakers). CSS default full-frame.
- **PHASE 1** comp 6.0: FULL-FRAME → Mode A (`expo.inOut` 0.7s); glow @6.3; zone-rule draw @6.4; Ken Burns `vid scale 1.0→1.03` start.
- **PHASE 2** comp 9.3: → FULL-FRAME for c1b3 (glow/rule fade 9.1; `vid` scale reset to 1.0). **PHASE 3** comp 15.0: → Mode A; glow/rule back; Ken Burns resumes.
- **PHASE 4** comp 23.3: → FULL-FRAME for c1b4 host-Q. **PHASE 5** comp 30.0: → Mode A.
- **PHASE 6** comp 33.0–61.0: Mode A holds (c1b5 flowchart + c1b6 card). Ken Burns 1.0→1.03 across the hold.
- **PHASE 7** comp 70.7: → FULL-FRAME for c1b7-pre. **PHASE 8** comp 74.7: → Mode A (before centerpiece).
- **PHASE 9** comp 78.0–106.5: Mode A holds (c1b7 centerpiece + c1b8 data-chart). Ken Burns.
- **PHASE 10** comp 106.5: → FULL-FRAME for c1b9 close (holds to clip end 110.8).

`#short_mag_cut_frame` video `data-duration="110.8" data-media-start="239.10"`; audio same. Master `data-duration="110.8"`.
**z-index:3 rule MUST list all beat ids:** `#beat-c1b1-half-decade, #beat-c1b3-moving-fast, #beat-c1b4-host-q, #beat-c1b5-two-sides, #beat-c1b6-jasper, #beat-c1b7pre-pricing, #beat-c1b7-agency-principal, #beat-c1b8-warehouse, #beat-c1b9-enter-exit` (DESIGN.md line 58 — else overlays render behind the z-index:2 video).

---

## VERIFICATION CHECKLIST

- **RULE 1 — opens on a real spoken line, word-synced:** src_in=239.10; c1b1 fires HALF A DECADE@0.62 / ANOTHER CAREER@2.58 / IN AN INDUSTRY@4.24, all on Jasper's actual words ("half/another/industry"). NO anticipatory text. ✅
- **RULE 2 — varied structure:** no swiss-grid stat-slam launch; cold-open is pure kinetic + minimal chrome. Centerpiece = Agency-vs-Principal 2-col. Supporting blocks: 2-node flowchart split + data-chart decay. Distinct silhouette vs clip-2. ✅
- **RULE 3 — framing verified from frames:** `object-position:83% center` (62% was the v1 bug — exposed seam/host). Verified at src 285 & 330 + 5 simulated crops viewed. Ken Burns 1.0→1.03, no hard zoom (clips name). ✅
- **Every non-editorial kinetic line has a real comp_t (src−239.10), quoted above.** NO editorial hook anywhere. ✅
- **No two templates adjacent identical:** kinetic→clean→kinetic→kinetic(Q)… c1b3 and c1b4 are both kinetic but separated by the clean 15.0–23.3 window (c1b4 opens at 23.6). flowchart→card→[c1b7-pre kinetic]→swiss-grid→data-chart→kinetic. ✅
- **One cyan per beat:** b1 IN AN INDUSTRY · b3 HAVEN'T SEEN THIS IN YEARS · b4 ACTUALLY DO? · b5 OTC-DESK accent node · b6 accent bar · b7-pre BEST PRICING · b7 PRINCIPAL header · b8 lowest bar · b9 AND EXIT POSITIONS. ✅
- **D4 no-outro:** Jasper card mid-clip (c1b6 @ comp 49); clip ends on c1b9 content kinetic. ✅
- **D7 palette/type:** all eyebrows JetBrains Mono 700 ≥32px #F0F0F0; body Inter ≥600; cards solid rgba(20,26,34,0.92)+cyan bar+glow, NO blur, NO grain; date context 2026. ✅
- **Beat count:** 9 core + c1b7-pre = 10 (range 9–10). ✅

## BUILD MANIFEST ROW
`clip_1 | clip-1-otc-model | 239.10 | 349.90 | kinetic-type,flowchart,liquid-glass,swiss-grid,data-chart | 10 beats | object-position:83%`
