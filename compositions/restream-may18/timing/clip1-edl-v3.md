# Clip 1 — OTC Model / Agency-vs-Principal — EDL **v3** (BUILD-READY)

**clip_id:** `clip_1` · **dir:** `clip-1-otc-model` · **slug:** `clip-1-otc-model`
**Supersedes** `clip1-edl-v2.md`. v2 family (all clips) was rejected for: **view flip-flopping**, **all-looking-like-clip-2 (kinetic-heavy)**, **jargon errors on screen**, **duplicate words**. This is the graded-gate-clean rebuild for Clip 1.

> ## ⚠️ BUILD STATE — EXECUTION REQUIRED (gate must NOT pass until this is done)
> **The as-built files in `clip-1-otc-model/` are still v2.** This EDL prose is correct and gate-clean, but the build has **NOT** been executed. If `clip-1-otc-model/index.html` is rendered as-is it would **catastrophically FAIL R1 (view flip-flop) and R2 (kinetic-heavy)** — the current GSAP has **EIGHT** view transitions (`toModeA 6.0 → toFull 9.3 → toModeA 15.0 → toFull 23.3 → toModeA 30.0 → toFull 70.7 → toModeA 74.7 → toFull 106.5`) with multiple sub-8s A-B-A segments = the exact flip-flop this EDL fixes.
>
> **The build agent MUST execute ALL of the following before the gate can pass** (each maps to the spec below):
> - **(a) GSAP phase map → ONE transition.** Replace the entire v2 phase map with a single `toModeA(30.2)` and Ken Burns `vid scale 1.0→1.03` across comp 30.2–111.3. **DELETE every other** `toFull(...)`/`toModeA(...)` call (all 8 v2 transitions). See the GSAP TIMELINE section.
> - **(b) c1b4 → clean breath.** Delete c1b4's kinetic content; make it a clean full-frame window comp 15.4–30.2 with **no overlay**. The current build still fires `WHAT DOES / AN OTC DESK / ACTUALLY DO` kinetic at comp 23.6 — **remove it**.
> - **(c) Delete `beat-c1b7pre-pricing.html`** and its `<div id="beat-c1b7pre-pricing">` from `index.html` body.
> - **(d) Add `beat-c1b6b-edge.html`** (`data-chart`, 2 bars `MINIMIZE MARKET IMPACT` / `BEST PRICING`@cyan, footnote `#F0F0F0`) and its `<div id="beat-c1b6b-edge" … data-composition-src="compositions/beat-c1b6b-edge.html">`, comp 69.5–76.0.
> - **(e) Rebuild c1b8 as a 3-node flowchart** `WAREHOUSE THE RISK → WORK OFF GRADUALLY → PRICE IMPACT MINIMIZED` (current build is a 4-bar `data-chart`) and place it at comp 100.0–106.5.
> - **(f) Re-time the Mode-A device-beats** to the values in this EDL — `c1b3 data-start 9.4/dur 6.0` (build has 9.6/5.4), `c1b5 33.0/15.5` (build has 33.0/12.0), `c1b6 50.0/10.0` (build has 49.0/12.0), `c1b7 80.5/18.5` (build has 78.0/20.5). Also `c1b9 106.7/dur 4.6` (build has the v2 value).
> - **(g) Update the `z-index:3` rule** to this EDL's 8-id list (see GSAP section): **drop** `#beat-c1b4-host-q` and `#beat-c1b7pre-pricing`; **add** `#beat-c1b6b-edge`.
>
> **Already correct in the as-built `index.html` (verified — do NOT change):** `object-position:85% center`.

> **Lead device (DESIGN.md per-clip map):** **Agency-vs-Principal two-column comparison (swiss-grid)** as the centerpiece, with a **`shimmer-sweep`** on the PRINCIPAL-column reveal. This is the distinct silhouette for clip-1 — it is NOT a stack of kinetic word-stacks.

---

## WHAT v2 GOT WRONG → v3 FIX

| # | v2 failure (against the codified rules) | v3 fix |
|---|------------------------------------------|--------|
| 1 | **View flip-flop (R1 FAIL).** v2 bounced FULL→ModeA→FULL→ModeA→FULL: c1b3 full (5.7s), c1b4 host-Q full (6.7s **<8s**), c1b7-pre full (4s **<8s**), c1b9 full (4.3s **<8s**), with FULL recurring at 15.4s and 23.3s — multiple A-B-A within 12s and multiple sub-8s segments. | **Exactly ONE view transition: FULL → MODE-A @ comp 30.2.** Intro FULL holds 0–30.2 (cold open + the two grouped early kinetics + the host-Q breath, all over both speakers). Mode-A holds 30.2–110.8 (the entire OTC explanation). A-B-A is **impossible** with one switch; every segment ≫ 8s. The close kinetic (c1b9) plays IN Mode-A (left zone) rather than re-flipping to full-frame, because a 4.3s full-frame close = sub-8s = R1 FAIL. |
| 2 | **Kinetic-heavy / 3-in-a-row (R2 FAIL).** v2 opened c1b1 → c1b3 → c1b4 = **three kinetic word-stacks in a row** (the "looks like clip-2" defect), and added a 4th kinetic (c1b7-pre) mid-clip. | **Max 2 kinetics in a row.** c1b1 + c1b3 are the only adjacent kinetics (2 — allowed). c1b4 host-Q is **demoted to a clean full-frame breath** (audio carries the pivot) — this breaks the run. c1b7-pre kinetic is **deleted** (it was both the flip-flop offender and a run-extender); its content ("minimize impact / best pricing") is re-expressed as a **non-kinetic `data-chart` mini-beat (c1b6b) inside Mode-A**. Kinetic runs = `[2, 1]`. |
| 3 | **Centerpiece buried.** v2's swiss-grid comparison landed at comp 78s — it did not "lead." | The Agency-vs-Principal comparison is the **structural backbone of the whole Mode-A block** and is the dominant device-beat; every other Mode-A beat (flow-split, edge chart, decay flow, close) **sets it up or pays it off**. It leads the explanation, not the chrome. |
| 4 | **Duplicate words (R4).** v2 c1b7 used eyebrow `AGENCY vs PRINCIPAL` over columns `AGENCY`/`PRINCIPAL` (echo), subs `OTHER OTC DESKS`/`WINTERMUTE OTC` (dup "OTC"), rows repeating "Incentives". c1b6 eyebrow `WINTERMUTE · OTC DESK` over sub with "OTC". | Every on-screen string re-audited; **zero notable-word repeats within any beat** (audit run below). Eyebrow no longer echoes column headers; subs and rows each earn distinct words. |
| 5 | **Jargon.** (Clip-1 had no burp/deep-in errors, but the gate is universal.) | Every string passes `_JARGON.md`: `Wintermute`, `OTC desk`, `take rate`-style terms spelled correctly; no garbled Whisper artifacts on screen. |

**KEPT FROM v2 (what worked):** the dialog-matched cold open (`HALF A DECADE / ANOTHER CAREER / IN AN INDUSTRY` on Jasper's real line), `src_in = 239.10`, and the verified framing `object-position` (live `index.html` uses **85% center** — kept; the v2 doc's "83%" was superseded by the as-built value).

---

## IN / OUT / DURATION

- **src_in = 239.10s** — trim head filler *"So while currently we say like we're full time in crypto,"* and open on *"I think in like **half a decade**…"* (Jasper).
- **src_out = 350.40s** — *"positions"* (the last word of *"helping people enter and exit positions"*, the one-sentence model summary) completes spoken at src 349.90; **src_out is held to 350.40 to capture the natural post-"positions" pause** so the cyan close payoff has room to animate in and hold before the comp ends (see c1b9 fix below). Content close per the no-outro rule — NO end card.
- **duration = 111.30s**
- **comp offset:** `comp_t = src_t − 239.10` (canonical).
- ⚠️ **`clip1-words.txt` is computed at `src − 220`, NOT `src − 239.10`.** Every comp_t in this EDL is RE-derived at `src − 239.10` and was read off the **audio.json word objects** (ground truth), with the source word + `src_t` quoted next to each line so it is auditable. Do not read fire-times from `clip1-words.txt` for this clip without subtracting the 19.10s offset.
- **index.html:** `data-media-start="239.10"` on both `<video>` and `<audio>`; master `data-duration="111.3"`.

---

## FRAMING (verified — RULE 5)

Side-by-side source (1920×1080, 30fps): Nic (host) LEFT half, **Jasper (guest) RIGHT half**, face center ≈ x≈1470 (≈76% across).

- **Mode-A geometry:** `MODE_A = { left:1229, top:108, width:614, height:864 }` (85% of the right-40% zone; bottom clearance 108px > 40px; top 108px > 20px).
- **`object-position: 85% center`** — Jasper horizontally centered in the 614px window; the *"Jasper De Maere / Wintermute"* lower-third stays fully inside the frame. (62% = the v1 seam/host bug; 88%+ clips the name. **As-built `index.html` uses 85%** — keep it; re-confirm by frame extraction at `src 285` and `src 330` before render.)
- **Vertical:** `object-fit:cover` fills the 864px height exactly → vertical object-position has no effect. Add a gentle **Ken Burns 1.0 → 1.03** across the long Mode-A hold to keep it alive and tighten the dead ceiling. NO hard zoom (1.08 clipped "Wintermute").

---

## ★ VIEW-TIMELINE (proves R1) ★

The source is side-by-side. Beats play in **FULL-FRAME** (both speakers, kinetic over a dark left-gradient) or **MODE-A** (Jasper framed right 40%, graphic in left 60%). v3 uses **exactly one transition** so the frame cannot flip-flop.

| Seg | View | comp range | dwell | Beats grouped into this view | R1 verdict |
|----|------|-----------|-------|------------------------------|-----------|
| 1 | **FULL-FRAME** | 0.0 – 30.2 | **30.2s** | c1b1 cold-open kinetic · c1b3 "moving fast" kinetic · c1b4 host-Q (clean) | intro-exempt at the head; ≥8s ✓ |
| 2 | **MODE-A** | 30.2 – 111.3 | **81.1s** | c1b5 flow-split · c1b6 name card · c1b6b edge data-chart · **c1b7 swiss-grid centerpiece + shimmer** · c1b8 decay flow · c1b9 kinetic close | ≥8s ✓ |

- **One-liner:** *FULL-FRAME holds the first 30.2s (cold open + two grouped kinetics + the host-Q breath), then a single switch to MODE-A holds the remaining 81.1s for the entire OTC explanation — one transition, zero flip-flop.*
- **R1 proof:** (a) **No segment < 8s** outside the 0–6s intro — both segments are ≫8s. (b) **No A-B-A within 12s** — with a single transition, no view is ever returned to. (c) **Consecutive graphic beats grouped into one view** — the two early kinetics stay FULL together; all six Mode-A device-beats stay MODE-A together. ✅
- The FULL→MODE-A switch happens once (`expo.inOut`, 0.7s) at comp 30.2, on the natural pivot from "yeah I can't disagree / so for someone who never thought about it…" into Jasper's structured answer. The close kinetic (c1b9) **stays in Mode-A** — flipping back to full-frame for a sub-8s close would be an R1 FAIL, so the kinetic builds in the left zone instead (the QA "≥1 full-frame kinetic over both speakers for >90s clips" requirement is already satisfied by Segment 1).

---

## TEMPLATE VARIETY (proves R2)

Sequence: **kinetic → kinetic → [clean] → flowchart → liquid-glass → data-chart → swiss-grid(centerpiece)+shimmer → flowchart → kinetic.**

- **Max consecutive kinetic word-stacks = 2** (c1b1 + c1b3). c1b4 is clean (not a stack). Runs = `[2, 1]`. ✅ (≤2)
- **Distinct primary device leads:** the Agency-vs-Principal **swiss-grid two-column** is the centerpiece + the only `shimmer-sweep`; the clip is **not** kinetic-dominated (2 kinetic graphic-beats out of 8). ✅
- **No two identical templates adjacent**, except the intentional 2-kinetic opener (R2 explicitly permits ≤2 kinetics in a row). The two flowcharts (c1b5, c1b8) are non-adjacent (separated by card + chart + swiss-grid). ✅
- **8 graphic beats** (c1b1, c1b3, c1b5, c1b6, c1b6b, c1b7, c1b8, c1b9) + 1 clean full-frame window (c1b4) → ≥8 for a >90s clip ✓.

### Catalog blocks — install vs hand-build

Init the master from the swiss-grid example (already done in the as-built dir); then:

| Item | Catalog name | Type | Action | Used by |
|------|-------------|------|--------|---------|
| Comparison grid | `swiss-grid` | **example** | `npx hyperframes init <tmp> --example swiss-grid` → adapt to DESIGN.md, transplant into `beat-c1b7-agency-principal.html` (already exists from v2 — re-skin per new strings) | c1b7 centerpiece |
| Premium reveal | **`shimmer-sweep`** | **component** | `npx hyperframes add shimmer-sweep --dir clip-1-otc-model --no-clipboard` → paste the snippet over the PRINCIPAL column header on its reveal (comp 84.62) | c1b7 |
| Node/branch diagram | `flowchart` | **block** | `npx hyperframes add flowchart --dir clip-1-otc-model --no-clipboard` → wire as sub-comp for the split AND the decay chain | c1b5, c1b8 |
| Bar chart | `data-chart` | **block** | `npx hyperframes add data-chart --dir clip-1-otc-model --no-clipboard` → 2-bar edge panel | c1b6b |
| Kinetic stacks | `kinetic-type` | **example** | already the basis of the v2 sub-comps — reuse `beat-c1b1`, `beat-c1b3`, `beat-c1b9` (re-time/re-string) | c1b1, c1b3, c1b9 |
| Name card | Liquid Glass Card (DESIGN.md "Cards & Panels") | **hand-build** | solid `rgba(20,26,34,0.92)` + 4px cyan bar + glow + mask feather (NO blur, NO grain) — reuse v2 `beat-c1b6-jasper.html` | c1b6 |

> The v2 build already created `beat-c1b1`, `beat-c1b3`, `beat-c1b4`, `beat-c1b5`, `beat-c1b6`, `beat-c1b7pre`, `beat-c1b7`, `beat-c1b8`, `beat-c1b9` sub-comps. v3 **reuses** c1b1/c1b3/c1b5/c1b6/c1b7/c1b8/c1b9 (re-string + re-time per below), **repurposes** c1b4 → clean (delete its kinetic content), **deletes** `beat-c1b7pre-pricing.html`, and **adds** `beat-c1b6b-edge.html` (the data-chart). Update the z-index:3 rule accordingly (see GSAP section).

---

## BEAT MAP

| Beat | comp range | src range | template / block | on-screen text (full) | view | sub-comp file |
|------|-----------|-----------|------------------|----------------------|------|----------------|
| c1b1 | 0.0–6.0 | 239.10–245.10 | **kinetic-type** (cold open, word-synced) | `01` · `WINTERMUTE · OTC` · **HALF A DECADE / ANOTHER CAREER / IN AN INDUSTRY** | FULL-FRAME | `beat-c1b1-half-decade.html` |
| c1b3 | 9.4–15.4 | 248.50–254.50 | **kinetic-type** (word-synced) | `MOMENTUM` · **MOVING / VERY FAST / UNLIKE ANY YEAR PRIOR** | FULL-FRAME | `beat-c1b3-moving-fast.html` |
| c1b4 | 15.4–30.2 | 254.50–269.30 | **clean full-frame** (no overlay) | — (host Q "what does an OTC desk… do exactly?" carried by audio) | FULL-FRAME | — (none) |
| c1b5 | 33.0–48.5 | 272.10–287.60 | **flowchart** (1→2 split block) | `TWO SIDES OF THE BOOK` · root `THE FIRM` · A `MARKET-MAKING` (Maker across exchanges & tokens · provides liquidity) · B `OTC DESK` (Executes specific client transactions) | MODE-A | `beat-c1b5-two-sides.html` |
| c1b6 | 50.0–60.0 | 289.10–299.10 | **liquid-glass card** (name, MID-clip) | `WINTERMUTE` · **JASPER DE MAERE** · OTC Trader & Market Strategist | MODE-A | `beat-c1b6-jasper.html` |
| c1b6b | 69.5–76.0 | 308.60–315.10 | **data-chart** block (2-bar edge) | `EXECUTION EDGE` · bar `MINIMIZE MARKET IMPACT` · bar `BEST PRICING` · note "Algorithms + proprietary tech" | MODE-A | `beat-c1b6b-edge.html` (NEW) |
| **c1b7** | **80.5–99.0** | **319.60–338.10** | **swiss-grid 2-column (CENTERPIECE) + `shimmer-sweep`** | `TWO EXECUTION MODELS` · **AGENCY** \| **PRINCIPAL** (full rows below) | MODE-A | `beat-c1b7-agency-principal.html` |
| c1b8 | 100.0–106.5 | 339.10–345.60 | **flowchart** (3-node decay chain) | `WHY IT ALIGNS` · `WAREHOUSE THE RISK → WORK OFF GRADUALLY → PRICE IMPACT MINIMIZED` | MODE-A | `beat-c1b8-warehouse.html` |
| c1b9 | 106.7–111.3 | 345.80–350.40 | **kinetic-type** (close, word-synced) | `THE MODEL, IN ONE LINE` · **HELP PEOPLE / ENTER / AND EXIT POSITIONS** | MODE-A | `beat-c1b9-enter-exit.html` |

---

## BEAT-BY-BEAT (per kinetic/reveal line: on-screen text → transcript word + src_t → comp_t)

### c1b1 — kinetic-type · COLD OPEN · comp 0.0–6.0 · src 239.10–245.10 · FULL-FRAME · WORD-SYNCED
Opens on Jasper's real, complete line (trimmed to start on "I think"): *"I think in like **half a decade** or so, it's just going to be **another career** **in an industry**."* — a coherent thought (R5). Screen alive from t=0: mono index `01` slams in @ comp 0.0, eyebrow `WINTERMUTE · OTC` fades @ comp 0.15. **No stat-slam / tag-row launch** (the block that made every clip identical — deliberately removed). Kinetic phrases build and STAY (no dim).

| on-screen line | transcript word(s) | src_t | **comp_t (fire)** | color |
|---|---|---|---|---|
| `HALF A DECADE` | "half" (→ "a decade") | 239.72 | **0.62** | #F0F0F0 |
| `ANOTHER CAREER` | "another" (→ "career") | 241.68 | **2.58** | #F0F0F0 |
| `IN AN INDUSTRY` | "industry" | 243.34 | **4.24** | **#00D4FF** (single cyan payoff + glow) |

- Phrase build: `fromTo({opacity:0,y:28},{opacity:1,y:0},expo.out,0.28s)`; payoff adds `scale:0.92→1`. Lines stay full opacity; full sentence readable by comp ~4.5.
- Plays over FULL-FRAME video (both speakers) with a dark left-gradient backdrop for legibility. 130px Inter 900, `text-shadow`.
- Whole stack drifts up + fades (`power2.in`, comp 5.5→5.85) — **but the view does NOT switch yet** (still full-frame for c1b3).
- `data-start="0.0" data-duration="6.0"`. Cyan: `IN AN INDUSTRY` only.
- `<!-- WORD-SYNCED: half@0.62 another@2.58 industry@4.24 (src−239.10, from audio.json) -->`

### c1b3 — kinetic-type · comp 9.4–15.4 · src 248.50–254.50 · FULL-FRAME · WORD-SYNCED
Stays **full-frame** (grouped with c1b1 — no Mode-A flip between them; R1). Jasper: *"But it is **moving** **very fast**. Like I **haven't seen** it moving like this for as long as I've been looking at the space."*
The cyan payoff `UNLIKE ANY YEAR PRIOR` is an editorial compression of "haven't seen it … for as long as I've been looking" — it fires on the real word **"haven't"** and respects the 2026/2025 date rule (no year numerals).

| on-screen line | transcript word(s) | src_t | **comp_t (fire)** | color |
|---|---|---|---|---|
| `MOVING` | "moving" | 249.22 | **10.12** | #F0F0F0 |
| `VERY FAST` | "very" (→ "fast"@10.66) | 249.48 | **10.38** | #F0F0F0 |
| `UNLIKE ANY YEAR PRIOR` | "haven't" (→ "seen"@11.76) | 250.46 | **11.36** | **#00D4FF** payoff |

- `MOVING` / `VERY FAST` build then `UNLIKE ANY YEAR PRIOR` lands; phrases STAY. Stack drifts up + fades comp 14.6→14.95.
- `data-start="9.4" data-duration="6.0"`. Cyan: `UNLIKE ANY YEAR PRIOR` only. 130px Inter 900.
- `<!-- WORD-SYNCED: moving@10.12 very@10.38 haven't@11.36 (src−239.10) -->`
- **`UNLIKE ANY YEAR PRIOR` is a marked EDITORIAL label** (compression of the spoken line), fired on the real word "haven't". If strict literalism is preferred: `HAVEN'T SEEN THIS / IN YEARS` (2-line), still on "haven't"@11.36.

### c1b4 — CLEAN FULL-FRAME · comp 15.4–30.2 · src 254.50–269.30 · NO OVERLAY
**The run-breaker.** No graphic — the host's pivot question carries on audio over both speakers, keeping the frame full and stable so the next kinetic (c1b3) and the upcoming Mode-A explanation are not separated by a flip. Content: Jasper *"…as long as I've been looking at the space."* → Nic *"Yeah, I cannot disagree with that, obviously. So for someone who never thought about it, **what does an OTC desk** at a firm like Wintermute do **exactly**?"* The unanswered question is the natural hinge into the Agency-vs-Principal centerpiece.
- 14.8s of clean full-frame. This is intentional dead-air-free narrative (host question + Jasper's "yeah I can't disagree"). Ken Burns does NOT run here (full-frame).
- **View switch FULL → MODE-A fires at comp 30.2** (`expo.inOut`, 0.7s), landing as Jasper begins his structured answer ("So OTC trading is obviously… bread and butter is market making").

### c1b5 — flowchart (1→2 split) · comp 33.0–48.5 · src 272.10–287.60 · MODE-A · WORD-SYNCED reveals
Catalog **`flowchart`** block, laid out as ONE root node → TWO branches (sets up the Agency/Principal centerpiece). Jasper: *"OTC trading is obviously… bread and butter is **market making**… The **OTC desk** is very much the other side of this. We help people execute specific transactions."*
- Eyebrow `TWO SIDES OF THE BOOK` — Inter 700, 32px, #F0F0F0 — @ comp 33.2.
- Neutral rule `#2a2a2a` draws @ comp 33.4 (cyan reserved for the accent branch).
- Root node `THE FIRM` pops `back.out(1.5)` @ comp 33.8.
- Branch A `MARKET-MAKING` (desc "Maker across exchanges & tokens · provides liquidity"), #F0F0F0 node — reveals on **"market"@36.66**.
- Branch B (accent) `OTC DESK` (desc "Executes specific client transactions"), cyan border+glow — reveals on **"OTC"@46.66** ("The OTC desk is very much the other side"). Connector arrows draw 0.15s after each branch.
- Cyan: ONLY Branch B `OTC DESK` accent border. NO footer line (removed — eyebrow already states the idea; avoids R4 "two/firm" dup).
- `data-start="33.0" data-duration="15.5"`. Mode-A throughout.
- `<!-- WORD-SYNCED reveals: MARKET-MAKING@36.66 (market) · OTC-DESK@46.66 (OTC) (src−239.10) -->`

### c1b6 — liquid-glass card (Jasper name) · comp 50.0–60.0 · src 289.10–299.10 · MODE-A
Speaker-ID card placed **MID-clip** (no-outro rule) as Jasper details execution. DESIGN.md "Cards & Panels": solid `rgba(20,26,34,0.92)`, 4px cyan accent bar, glow, 1px border, `mask-image` feather; **NO blur, NO grain.**
- Card slides in from RIGHT @ comp 50.5 (`expo.out`, 0.5s).
- Eyebrow `WINTERMUTE` — Inter 700, 32px, #F0F0F0.
- Headline `JASPER DE MAERE` — Inter 800, 56px, #F0F0F0.
- Sublabel `OTC Trader & Market Strategist` — Inter 600, 30px, #F0F0F0.
- Card fades out by comp 60.0 (clip continues — not held to end).
- Single cyan = the 4px accent bar. `data-start="50.0" data-duration="10.0"`. (Editorial placement — no word-sync; placed where he's naming the desk's function.)
- **R4:** eyebrow `WINTERMUTE` vs sub `OTC Trader & Market Strategist` — no shared notable word (v2's "OTC"-in-both fixed). ✅

### c1b6b — data-chart (2-bar EDGE panel) · comp 69.5–76.0 · src 308.60–315.10 · MODE-A · WORD-SYNCED · **NEW (replaces v2 c1b7-pre kinetic)**
Catalog **`data-chart`** block — the 8th graphic beat, and the **variety move that removes a kinetic** (v2 expressed this content as a full-frame kinetic that caused the flip-flop). Two short bars in the left zone (Mode-A, no view switch). Jasper: *"…proprietary tech we have to **minimize** market **impact**, offer **best pricing**."*
- Eyebrow `EXECUTION EDGE` — Inter 700, 32px, #F0F0F0 — @ comp 69.7.
- Bar 1 `MINIMIZE MARKET IMPACT` grows on **"minimize"@70.94** — neutral #F0F0F0.
- Bar 2 `BEST PRICING` grows on **"best"@73.32** — **#00D4FF** (single cyan, the payoff bar).
- Footnote `Algorithms + proprietary tech` — JetBrains Mono, 30px, #F0F0F0 (small text <48px MUST be #F0F0F0, never #888888 — checklist line 48 / D7).
- `data-start="69.5" data-duration="6.5"`. Mode-A throughout. Cyan: Bar 2 only.
- `<!-- WORD-SYNCED bars: MINIMIZE-IMPACT@70.94 (minimize) · BEST-PRICING@73.32 (best) (src−239.10) -->`

### c1b7 — swiss-grid TWO-COLUMN (CENTERPIECE) + shimmer-sweep · comp 80.5–99.0 · src 319.60–338.10 · MODE-A · WORD-SYNCED reveals
**★ THE LEAD DEVICE ★.** Two equal columns, headers at equal visual height. LEFT = how rivals execute, RIGHT = Wintermute's model (cyan header = the single cyan; `shimmer-sweep` plays once across the right header on its reveal). Jasper: *"…quite **different** than a lot of other OTC desks where they would execute in **agency**. We do this in… **principal** trading. So the prices we offer is **risk price**. We **warehouse** that risk and then we trade on it very gradually… the incentive to minimize price impact is very much **aligned**."*

- Eyebrow `TWO EXECUTION MODELS` — Inter 700, 34px, #F0F0F0 — @ comp 80.7. *(Eyebrow deliberately does NOT contain "AGENCY"/"PRINCIPAL" — those are the column headers; R4.)*
- Neutral rule `#2a2a2a` (cyan reserved for the right header) — draws @ comp 80.9.
- **LEFT column** header `AGENCY` + sub `RIVAL DESKS` — Inter 800, 48px, #F0F0F0 — reveals on **"agency"@82.68**.
  - Row A1 `Trades on the client behalf` — Inter 600, 30px, #F0F0F0 — @ comp 83.1
  - Row A2 `Holds no position` — @ comp 83.5
  - Row A3 `Incentives can diverge` — @ comp 83.9
- **RIGHT column** header `PRINCIPAL` + sub `WINTERMUTE` — Inter 800, 48px, **#00D4FF** (single cyan) — reveals on **"principal"@84.62**; **`shimmer-sweep` sweeps across this header once** on reveal (premium accent, the only shimmer in the clip).
  - Row P1 `Quotes a RISK PRICE` — Inter 600, 30px, #F0F0F0 — reveals on **"risk"@87.76**
  - Row P2 `Takes the other side` — reveals during the warehouse/gradual stretch on **"warehouse"@88.92** (Jasper: "we warehouse that risk and then we trade on it very gradually" = taking & working the other side)
  - Row P3 `Fully ALIGNED` — reveals on **"aligned"@96.30**
- **Cyan discipline:** ONLY the right header `PRINCIPAL` is cyan (+ its shimmer). Rule neutral; all rows #F0F0F0. ✅
- Headers at equal visual height (both single-line, 48px). Bullet rows use `min-width:0; flex:1` on the text node so wraps align under the first character (QA layout rule).
- `data-start="80.5" data-duration="18.5"`. Mode-A throughout. Exit fade @ comp 98.5.
- **R4 (audited clean):** no notable word repeats across eyebrow/subs/rows (see audit block below).
- `<!-- WORD-SYNCED: AGENCY@82.68 PRINCIPAL@84.62(+shimmer) RISK-PRICE@87.76 OTHER-SIDE@88.92 ALIGNED@96.30 (src−239.10) -->`

### c1b8 — flowchart (3-node decay chain) · comp 100.0–106.5 · src 339.10–345.60 · MODE-A · WORD-SYNCED
Catalog **`flowchart`** as a left-to-right **cause→effect chain** (distinct from c1b5's split and from c1b7's columns — it is the *payoff* of the comparison, showing WHY principal incentives align). Jasper: *"We warehouse that risk and then we trade on it very gradually… a lot of people in the market generally **appreciates** that **alignment** of incentives."*
- Eyebrow `WHY IT ALIGNS` — Inter 700, 32px, #F0F0F0 — @ comp 100.2.
- Node 1 `WAREHOUSE THE RISK` pops @ comp 100.6 — #F0F0F0.
- Connector → Node 2 `WORK OFF GRADUALLY` @ comp 101.4 — #F0F0F0.
- Connector → Node 3 (accent) `PRICE IMPACT MINIMIZED` — **#00D4FF** — reveals on **"appreciates"@103.44** (held; "alignment"@104.70 lands during its glow).
- Cyan: final node only. `data-start="100.0" data-duration="6.5"`. Mode-A.
- `<!-- WORD-SYNCED: final-node@103.44 (appreciates) / alignment@104.70 (src−239.10) -->`

### c1b9 — kinetic-type · CLOSE · comp 106.7–111.3 · src 345.80–350.40 · **MODE-A** · WORD-SYNCED · CONTENT CLOSE
Clip ends on the substantive one-sentence summary — NOT a name/CTA card. Host: "So in one sentence…" Jasper: *"…it's **helping people** **enter** and **exit** **positions** very smoothly."* **Plays in Mode-A** (kinetic builds in the left zone, Jasper framed right) — a full-frame flip here would be a sub-8s segment = R1 FAIL, so the view stays Mode-A through the end.

| on-screen line | transcript word(s) | src_t | **comp_t (fire)** | color |
|---|---|---|---|---|
| `HELP PEOPLE` | "helping" (→ "people"@108.92) | 347.68 | **108.58** | #F0F0F0 |
| `ENTER` | "enter" | 348.52 | **109.42** | #F0F0F0 |
| `AND EXIT POSITIONS` | "exit" (→ "positions"@110.80) | 349.64 | **110.54** | **#00D4FF** payoff |

- Eyebrow `THE MODEL, IN ONE LINE` — Inter 700, 32px, #F0F0F0 — @ comp 106.9 (top-left of the left zone, above the stack).
- Phrase build: `fromTo({opacity:0,y:28},{opacity:1,y:0},expo.out,0.28s)`; the cyan payoff `AND EXIT POSITIONS` adds `scale:0.92→1`. **The payoff fires on "exit"@110.54, finishes its 0.28s entry by comp ~110.82 (as "positions" completes spoken @ src 349.90 = comp 110.80), then HOLDS until the comp ends @ 111.3 — ~0.48s of tail (animate-in 0.28s + ~0.20s hold).** Phrases STAY full-opacity through clip end (no dim, no exit drift). No CTA / end-card.
- `data-start="106.7" data-duration="4.6"` (extended from 4.1 so the close payoff has ~0.5s to build and hold — see IN/OUT and tail-headroom note). Cyan: `AND EXIT POSITIONS` only. Lines ~110px (Mode-A left zone is narrower than full-frame — drop from 130px to ~110px so the phrases fit the 60% zone; still ≥ the 22–28px readable floor by a wide margin).
- `<!-- WORD-SYNCED close: helping@108.58 enter@109.42 exit@110.54 (src−239.10) -->`

---

## GSAP TIMELINE (master) — phase map (ONE view transition)

Geometry `MODE_A={left:1229,top:108,width:614,height:864}`, `object-position:85% center`.

> **BUILD DIRECTIVE (a):** The as-built `index.html` GSAP still has the v2 **8-transition** map (`toModeA 6.0 → toFull 9.3 → toModeA 15.0 → toFull 23.3 → toModeA 30.0 → toFull 70.7 → toModeA 74.7 → toFull 106.5`). **Delete ALL of those calls** and replace the entire phase map with the THREE phases below — the only view call is a single `toModeA(30.2)`. There is **no** `toFull` anywhere after the head, and **no** `toModeA` other than the one at 30.2.

- **PHASE 0 — FULL-FRAME, comp 0.0–30.2.** CSS default full-frame video (both speakers) — **no view call** (full-frame is the default). c1b1 cold open (0–6) → c1b3 kinetic (9.4–15.4) → c1b4 clean host-Q (15.4–30.2, NO overlay — delete its v2 kinetic). Dark left-gradient backdrop fades in under each kinetic stack and out after it; the video stays full-frame the whole phase (no Mode-A between the kinetics — R1 grouping).
- **PHASE 1 — TRANSITION @ comp 30.2.** FULL-FRAME → Mode-A (`expo.inOut`, 0.7s). `#bg-glow` in @ 30.5; `#zone-rule` draws @ 30.6; Ken Burns `vid scale 1.0→1.03` begins and runs across the entire Mode-A hold.
- **PHASE 2 — MODE-A holds, comp 30.9–111.3.** c1b5 (33.0–48.5) → c1b6 (50.0–60.0) → c1b6b (69.5–76.0) → **c1b7 centerpiece (80.5–99.0)** → c1b8 (100.0–106.5) → c1b9 close (106.7–111.3). No view switch — the frame is stable for the entire explanation; variety comes from the device-beats inside it. Ends in Mode-A. Ken Burns 1.0→1.03 runs to comp 111.3.

`#short_mag_cut_frame` video `data-duration="111.3" data-media-start="239.10"`; audio identical. Master `data-duration="111.3"`.

**z-index:3 rule — MUST list every overlay beat id** (else it renders behind the z-index:2 video — the clip-2 v9–v11 bug). For v3, update the rule in `index.html` to:
```css
#beat-c1b1-half-decade,
#beat-c1b3-moving-fast,
#beat-c1b5-two-sides,
#beat-c1b6-jasper,
#beat-c1b6b-edge,
#beat-c1b7-agency-principal,
#beat-c1b8-warehouse,
#beat-c1b9-enter-exit { z-index: 3; }
```
**Removed** from the rule: `#beat-c1b4-host-q` (now clean, no overlay) and `#beat-c1b7pre-pricing` (deleted). **Added:** `#beat-c1b6b-edge`. Also delete the `<div id="beat-c1b4-host-q">` and `<div id="beat-c1b7pre-pricing">` blocks from the body and add a `<div id="beat-c1b6b-edge" … data-composition-src="compositions/beat-c1b6b-edge.html">`.

---

## ON-SCREEN-STRING AUDIT (R3 jargon + R4 duplicates) — machine-checked

**R3 (jargon):** every string scanned against `_JARGON.md` blacklist (`burp`, `deep in`, `graft`, `stake rate`, `meme con`, `insaturable`, `dime terminal`) → **0 hits**. Brand/term spellings exact: `Wintermute`, `OTC desk`. ✅

**R4 (no duplicate notable word within a beat):** per-beat scan (stopwords + ≤2-char words excluded) → **0 dup in every beat**. Specifically fixed vs v2: c1b5 footer removed (was dup "two/firm"); c1b6 eyebrow→`WINTERMUTE` only (was dup "OTC"); c1b7 eyebrow→`TWO EXECUTION MODELS` (no longer echoes `AGENCY`/`PRINCIPAL`), subs→`RIVAL DESKS`/`WINTERMUTE` (was dup "OTC"), rows reworded so no word repeats (`Holds no position` / `Takes the other side` — not both "position"; no row repeats "Incentives"/"risk"). ✅

---

## VERIFICATION CHECKLIST (graded gate — every item)

- **R1 view discipline:** ONE transition (FULL@0–30.2 → MODE-A@30.2–111.3). No segment <8s outside intro; no A-B-A within 12s (impossible with one switch); consecutive graphics grouped per view. View-timeline table included. ✅
- **R2 template variety:** max 2 kinetics in a row (`[2,1]`); distinct lead device = Agency-vs-Principal swiss-grid + the only shimmer-sweep; not kinetic-dominated; catalog blocks named (swiss-grid example, shimmer-sweep/flowchart/data-chart adds); 8 graphic beats; no two identical templates adjacent except the permitted 2-kinetic opener. ✅
- **R3 jargon:** every on-screen string passes `_JARGON.md` (machine-checked, 0 hits). ✅
- **R4 duplicate words:** 0 within-beat notable-word repeats (machine-checked). ✅
- **R5 opening coherence:** `HALF A DECADE / ANOTHER CAREER / IN AN INDUSTRY` is a complete thought; cyan payoff `IN AN INDUSTRY` is a real phrase (not a dangling number). ✅
- **Dialog-match + open-on-line:** src_in=239.10; c1b1 fires on Jasper's actual words half@0.62 / another@2.58 / industry@4.24 (ground truth from audio.json). Index `01` on screen @ t=0; first kinetic word @ 0.62. NO anticipatory hook. ✅
- **Every kinetic/reveal line fires at `comp_t = src_t − 239.10`**, read off audio.json word objects (NOT computed from the src−220 words.txt), quoted per line; one editorial label marked (c1b3 payoff). All fires verified inside their beat windows; the close payoff (c1b9 `AND EXIT POSITIONS`@comp 110.54) now has **≥0.5s tail headroom** (src_out extended to 350.40 → comp end 111.3, so the 0.28s entry animation completes by ~110.82 and holds ~0.48s before the comp ends). ✅
- **Framing:** `object-position:85% center` (as-built), Ken Burns 1.0→1.03, no hard zoom; re-confirm by frame at src 285 & 330 before render. ✅
- **One cyan per beat:** b1 IN AN INDUSTRY · b3 UNLIKE ANY YEAR PRIOR · b5 OTC-DESK node · b6 accent bar · b6b BEST PRICING bar · b7 PRINCIPAL header(+shimmer) · b8 final node · b9 AND EXIT POSITIONS. ✅
- **No outro:** name card mid-clip (c1b6 @ comp 50); clip ends on c1b9 content kinetic. Dates: no numerals, "this year/prior" only. Palette/type: eyebrows Inter 700 ≥32px #F0F0F0; body Inter ≥600; cards solid `rgba(20,26,34,0.92)`+cyan bar+glow, NO blur/grain. ✅
- **VERIFY-BY-FRAME (mandatory, build stage):** after draft render, extract frames at comp 0.6 (open), 12.0 (c1b3 payoff), 30.5 (the single view switch), 47.0 (c1b5 accent node), 55.0 (name card), 73.0 (edge chart), **85.0 (centerpiece w/ shimmer)**, 104.0 (decay node), **110.9 (close payoff held, after the 0.28s entry completes ~110.82)** and LOOK — confirm overlays sit ABOVE video (z-index), Jasper centered+named, cyan-count=1/frame.

## BUILD MANIFEST ROW
`clip_1 | clip-1-otc-model | 239.10 | 350.40 | kinetic-type,flowchart,data-chart,swiss-grid+shimmer-sweep | 8 graphic beats + 1 clean | object-position:85% | 1 view transition`
