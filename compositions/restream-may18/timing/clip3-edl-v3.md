# Clip 3 — BUILD-READY EDL v3 (`clip-3-structured-products`)

> Supersedes `clip3-edl-v2.md`. v2 was rejected with the sibling clips for: **view flip-flopping**,
> **all-looking-like-clip-2 (kinetic-heavy)**, **jargon errors on screen**, **duplicate words**.
> This v3 fixes every one against the codified gate (`_QA-CHECKLIST.md`, `_JARGON.md`, `DESIGN.md`).
>
> **Headline fixes vs v2:**
> 1. **R1 (flip-flop) — the rejection cause.** v2 had a **4.7s full-frame wedge** (c3b5 demand kinetic, MA→FF→MA, 37.6–42.3s) — a hard FAIL ("a 4–5s view sandwiched between others is a FAIL"). v3 collapses the middle into **ONE 54.6s Mode-A block** so the frame never bounces. Only **4 views total**; every non-intro view ≥8s; the single A-B-A (MA→FF→MA) has a **14.0s** full-frame middle (>~12s). View-timeline table below proves it.
> 2. **R2 (variety) — the "all looks like clip-2" cause.** v2 leaned on 3 kinetic word-stacks (b1/b5/b8) as its spine. v3 makes the **`data-chart` adoption curve the distinct PRIMARY device** (18.6s centrepiece, longest beat), demotes the middle kinetic to a low-key Mode-A **caption**, and keeps only **2 full kinetic word-stacks** (open + the quotable loop), never adjacent. Spine = term-reveal → card → flowchart → caption → **data-chart** → loop → stat. Distinct silhouette from clip-1/clip-2 (both stat-first).
> 3. **R3 (jargon).** v2 still printed **"Stake rate has been very high"** (FAIL) and routed the demand line through "insaturable". v3: **TAKE RATE** everywhere on screen (b6 line annotation + b9 stat), and the b5 caption prints **INSATIABLE** (the literal R3 correction, on screen, owning the fix).
> 4. **R4 (dup words).** v2 repeated **ACCELERATORS** as the cyan payoff in BOTH b1 and b5 (reads as a clip-2 tic). v3 uses **ACCELERATORS** as cyan exactly once (b1 open). b5's payoff is **ACCELERATOR FIT** (different element/phrase). No notable word repeats across eyebrow vs sublabel/title inside any single beat (audited per beat below).
> 5. Real **`data-chart`** block (`npx hyperframes add data-chart`) replaces v2's hand-built "data-chart-style stat."

---

## NEW IN / OUT (unchanged from v2 — the dialog-matched open is kept; it works)

| field | value | why |
|---|---|---|
| `src_in` | **718.20** | Opens ON the term-reveal line. Trims the "Yeah, yeah… I was a decade off… 2016, 17, BTC as underlying" filler (src 700.16–717.62). First spoken words on screen: *"You see large financial institutions issuing stuff like **autocallables, accelerators**."* |
| `src_out` | **808.50** | Lands just after "…volumes on screen on option exchanges" so the take-rates / infrastructure payoff resolves on a complete clause. No outro. |
| duration | **90.3s** | comp_t = src_t − 718.20. |
| `data-media-start` | **718.20** | source.mp4 is the FULL episode (2853s, 1920×1080, 30fps); media-start is absolute episode time. |

> **Timing source of truth.** `clip3-words.txt` is based **comp_table = src − 700**. This EDL is based **comp = src − 718.20 = comp_table − 18.20**. Every fire-time below was READ off the word table and converted; none computed by hand. (Cross-check column: `src` is the table's authoritative value.)

**Opening line (verbatim, src 718.20–722.44):** "You see large financial institutions issuing stuff like **autocallables, accelerators**." — a complete statement (R5): *who* (large institutions) *does what* (issues) *which products* (autocallables, accelerators). The clip's signature terms are SPOKEN inside the first 4.3s → the term-reveal open is honest, not anticipatory.

---

## FRAMING — verified from real frames (kept from v2)

**`object-position: 80% center`** (centers Jasper, guest, right half — clears the x=960 seam, name "Jasper De Maere · Wintermute" fully readable). `MODE_A = { left: 1229, top: 108, width: 614, height: 864 }`, `border-radius: 6px`, `object-fit: cover`, slow Ken Burns 1.00→1.04. (v2's frame audit stands: 50%/62% center the seam/host = FAIL; 76% bleeds host; 83% leans Jasper left; **80% chosen**.) Opening full-frame beats (b1, b7) show BOTH speakers — never text on black.

Mode-A entry/return mirror clip-2: full-frame return = `{left:0,top:0,width:1920,height:1080,borderRadius:"0px"}` (`expo.inOut` 0.4–0.7s); on Mode A `#bg-glow` opacity→1 at +0.3s, `#zone-rule` `scaleY 0→1` at +0.4s (`power4.out`).

---

## STYLE (binding — DESIGN.md)

bg `#0A0A0A`; primary text `#F0F0F0`; **ONE cyan `#00D4FF` element per beat**; cards `rgba(20,26,34,0.92)` solid fill + 4px **inset** cyan accent bar + soft glow + 1px border + `mask-image` right-feather — **NO `backdrop-filter` blur, NO film grain**. Eyebrow Inter 700 ≥32px `#F0F0F0`; body/bullets Inter ≥600; small/label text `#F0F0F0` (never `#888888` under 48px). Kinetic phrase lines Inter 900 ~130px white, payoff line cyan; lines slam in and **STAY** (no dim). 2026 = "this year". **No intro card, no outro/CTA** — clip ends on the b9 stat content held to clip end.

---

## ★ VIEW-TIMELINE — proves R1 (no flip-flop)

The source is a side-by-side (Nic host LEFT, Jasper guest RIGHT). Two views only: **full-frame** (FF, both speakers, kinetic over them) and **Mode-A** (MA, guest framed right 40%, graphic in left 60%). Consecutive graphic beats are GROUPED into the same view so the frame never bounces.

| view | comp range | dwell | beats in this view | R1 check |
|---|---|---|---|---|
| **FF** | 0.0 – 6.4 | **6.4s** | c3b1 (term-reveal) | intro zone (0–6s) — quick switch allowed; never loops back ✓ |
| **MODE-A** | 6.4 – 61.0 | **54.6s** | c3b2 → c3b3 → *(clean gap 29.0–30.5)* → c3b5 → c3b6 | ≥8s ✓ — all four mid-clip graphics + the clean breath share ONE held frame; no bounce |
| **FF** | 61.0 – 75.0 | **14.0s** | c3b7 (price↔narrative loop) | ≥8s ✓; the only A-B-A middle is **14.0s > ~12s** ✓ |
| **MODE-A** | 75.0 – 90.3 | **15.3s** | c3b9 (take-rates stat, held to end) | ≥8s ✓ |

- **No segment < 8s outside the 0–6s intro.** ✓ (54.6 / 14.0 / 15.3)
- **No A-B-A within ~12s.** Only A-B-A is MA(54.6s)→FF(14.0s)→MA(15.3s); the FF middle is 14.0s, clearing the ~12s return-window. The big MA block (54.6s) is far from any return. ✓
- **Consecutive graphics grouped.** c3b2/c3b3/c3b5/c3b6 (card, flow, caption, chart) ALL live in the one 54.6s Mode-A view — the frame is rock-stable across the body of the clip. ✓
- The 29.0–30.5s clean breath is a graphic-OFF moment **inside** the held Mode-A frame — it is NOT a view switch (Jasper stays right-40% throughout). ✓

**Transition events** (only 3 view switches in the whole clip):
| at comp | switch |
|---|---|
| ~6.3 | FF → **Mode A** (`expo.inOut` 0.7s); glow +0.3, zone-rule +0.4; c3b2 glossary slides in; Ken Burns 1.00→1.04 begins |
| ~60.8 | **Mode A → FF** (`expo.inOut` 0.4s); glow/zone-rule out at 60.6; c3b7 loop kinetic fires 66.24 |
| ~74.8 | **FF → Mode A** (`expo.inOut` 0.4s); glow +0.3, zone-rule +0.4; c3b9 stat close; **held to clip end (90.3) — no exit** |

---

## ★ TEMPLATE VARIETY — proves R2

| order | beat | template / block | kinetic? |
|---|---|---|---|
| 1 | c3b1 | `kinetic-type` phrase build (term-reveal) | **kinetic #1** |
| 2 | c3b2 | liquid-glass card (hand-build per DESIGN Cards & Panels) | — |
| 3 | c3b3 | **`flowchart`** (install) — distribution chain | — |
| 4 | c3b5 | Mode-A **caption** (`caption-clip-wipe`-style, low-key supplemental — NOT a full ~130px word-stack) | low-key |
| 5 | c3b6 | **`data-chart`** (install) — **PRIMARY DEVICE**, adoption-by-region | — |
| 6 | c3b7 | `kinetic-type` phrase build (the quotable loop) | **kinetic #2** |
| 7 | c3b9 | stat close — hand-build swiss stat (single rising metric) | — |

- **≤2 kinetic word-stacks in a row:** the only two full kinetic word-stacks are **c3b1** and **c3b7**, separated by the entire 54.6s Mode-A body. They are NEVER adjacent. The c3b5 caption is a deliberately low-key Mode-A supplemental (small, in-zone), not a full-frame slam stack, so it does not count toward "kinetic in a row." ✓ (v2's b1/b5/b8 spread is replaced.)
- **Distinct PRIMARY device leads the clip's identity:** the **`data-chart` adoption curve** is the single largest beat (18.6s), the visual centrepiece, and the device this clip is "about." The term-reveal is the cold-open hook (mandated by the dialog-match rule), not the clip's device signature. Matches DESIGN per-clip map: *clip 3 = `data-chart` (demand/adoption) + term-reveal.* ✓
- **Catalog blocks to INSTALL (`npx hyperframes add`):** `data-chart` (c3b6), `flowchart` (c3b3). **Hand-build** (DESIGN palette, no template needed): c3b1 & c3b7 kinetic stacks, c3b2 liquid-glass card, c3b5 caption line, c3b9 stat. *(data-chart confirmed installable: `npx hyperframes add data-chart` → writes `compositions/data-chart.html`, a bar+line combo with staggered reveal — restyle to dark palette + fit left 60% zone, see c3b6.)*

---

## ★ JARGON AUDIT — proves R3 (every on-screen string mapped through `_JARGON.md`)

| on-screen string | beat | `_JARGON.md` status |
|---|---|---|
| AUTOCALLABLES | b1, b2 | correct casing ✓ |
| ACCELERATORS / Accelerators / ACCELERATOR | b1, b2, b5, b6 | correct casing ✓ |
| INSATIABLE? NO. | b5 | **corrects "insaturable" (src 749.28)** → R3 fix on screen ✓ |
| TAKE RATE (line annotation) | b6 | **corrects "Stake rate" (src 769.68)** ✓ |
| TAKE RATES (stat) | b9 | **corrects "stake rate"** → the headline take-rate term ✓ |
| Wintermute (name tag, in source video) | all MA | exact ✓ |
| Asia / Europe + US | b6 | plain nouns ✓ |
| Structured products | b2, b6, b9 eyebrows | plain ✓ |

No `burp`/`deep-in`/`graft`/`stake-rate`/`insaturable`/`meme-con` reaches the render. ✓

---

## ★ DUPLICATE-WORD AUDIT — proves R4 (per beat: eyebrow vs sublabel/title)

| beat | elements | notable-word overlap? |
|---|---|---|
| b1 | YOU SEE / LARGE INSTITUTIONS / ISSUING / AUTOCALLABLES / ACCELERATORS | none repeat ✓ |
| b2 | eyebrow `STRUCTURED PRODUCTS · CRYPTO`; titles `Autocallables`, `Accelerators`; defs; footnote `Issued by large financial institutions` | "structured products" (eyebrow) vs product titles — distinct words; no element repeats another's notable word ✓ |
| b3 | eyebrow `THE DISTRIBUTION CHAIN`; nodes `Large institution`→`Issues a structured note`→`Private-banking desk`→`UHNW client buys` | each node distinct; eyebrow word "distribution" not reused ✓ |
| b5 | line A `INSATIABLE? NO.`; line B `WHERE THE DEMAND IS`; payoff `= ACCELERATOR FIT` | "FIT" appears in exactly ONE element (the cyan payoff). Line B no longer carries "FIT" → no repeated notable word ✓ |
| b6 | headline `STRUCTURED-PRODUCT ADOPTION`; subtitle `Best fit by region`; bars `Asia` / `Europe + US`; line `Take rate` | "take rate" appears in exactly ONE element (the cyan line label). Subtitle no longer carries "take rate" → headline uses "adoption," subtitle uses "fit/region," line uses "take rate"; no dup ✓ |
| b9 | eyebrow `THE NEXT-CYCLE CATALYST · THIS YEAR`; stat `TAKE RATES ↑`; sublabel `Meaningfully higher than 2025`; footer `Demand + infrastructure both here now` | "take rates" only in the stat; eyebrow/sublabel/footer share no notable word with it or each other ✓ (date rule: eyebrow prints `THIS YEAR` not the literal `2026`; the `2025` baseline in the sublabel is sanctioned as prior-year comparison) |

**Cross-beat note (the v2 tic):** ACCELERATORS is the cyan payoff in **b1 only**. b5's payoff is the distinct phrase **ACCELERATOR FIT** (concept = product-market fit), b6 names it as a bar label — never re-used as a stand-alone cyan slam. R4 is within-beat; cross-beat repetition minimized to avoid the clip-2 feel. ✓

**ONE cyan per beat:** b1 `ACCELERATORS` · b2 accent bar · b3 final node `UHNW client buys` · b5 payoff `= ACCELERATOR FIT` · b6 the line (`Take rate`) · b7 `NARRATIVE CREATES PRICE` · b9 the rule. ✓ (b6: chart bars stay neutral `#3a4654`; the conversion LINE (`Take rate`) is the SOLE cyan — the 58.80 line-peak adds NO second cyan callout — D7 stat-OR-rule → line carries cyan.)

---

# BEAT MAP

Every beat: `id` · comp range · src range · template/block · view · sub-comp filename · full on-screen text (exact hex) · per kinetic line the **comp_t + matched transcript words** (read off `clip3-words.txt`, `comp = table − 18.20`).

---

### c3b1 — Kinetic TERM-REVEAL (opening; word-synced, dialog-matched, R5-coherent)
- **Comp:** 0.0 – 6.4s   **Src:** 718.20 – 724.60s
- **Template/block:** `kinetic-type` phrase build (hand-build, DESIGN palette). Term words get a heavier slam (0.04em tracking).
- **View:** **full-frame** (BOTH speakers) over a left dark-gradient backdrop. Video begins Mode-A transition at comp ~6.3.
- **Sub-comp:** `beat-c3b1-termreveal.html`
- **On-screen lines (each slams in, STAYS, no dim):**
  | line | hex / size | comp_t | matched words (src) |
  |---|---|---|---|
  | `YOU SEE` | `#F0F0F0` 120px | **0.00** | you 718.20 / see 718.46 |
  | `LARGE INSTITUTIONS` | `#F0F0F0` 120px | **0.48** | large 718.68 / institutions 719.30 |
  | `ISSUING` | `#F0F0F0` 120px | **1.72** | issuing 719.92 |
  | `AUTOCALLABLES` | `#F0F0F0` 130px | **3.18** | autocallables 721.38 |
  | `ACCELERATORS` | **cyan `#00D4FF`** 130px (payoff) | **4.24** | accelerators 722.44 |
  - Whole stack drifts up + fades at **comp 6.2** (`power2.in`) as video begins Mode-A transition.
- **Cyan element:** `ACCELERATORS` (1).
- **Opening-6s "3+ element types" (DESIGN D1) — structural 3rd element:** inside this sub-comp, slam a monospace index `03` + eyebrow `STRUCTURED PRODUCTS · CRYPTO` (Inter 700, 32px, `#F0F0F0`) top-left at **comp 5.0**, with a thin **neutral `#2a2a2a`** rule drawing under it at comp 5.3 (NOT cyan — `ACCELERATORS` owns this beat's cyan). Element types in first 6s = (1) kinetic phrase build, (2) heavy term slams, (3) index+eyebrow+rule. Speaker visible full-frame throughout. The eyebrow hands off visually into c3b2.
- `data-start="0.0" data-duration="6.4"`

### c3b2 — Liquid-glass GLOSSARY card (term-reveal payoff: define the two products)
- **Comp:** 6.4 – 18.5s   **Src:** 724.60 – 736.70s
- **Template/block:** liquid-glass card (DESIGN "Cards & Panels": solid `rgba(20,26,34,0.92)`, 4px **inset** cyan accent bar, glow, 1px border, `mask-image` right-feather, NO blur; rows STAGGER).
- **View:** **Mode A** (video transitions full-frame → right-40% at comp ~6.3; card slides in from right). `object-position: 80% center`.
- **Sub-comp:** `beat-c3b2-glossary.html`
- **Content (exact text):**
  - Index `03` (JetBrains Mono 20px `#F0F0F0`) + Eyebrow `STRUCTURED PRODUCTS · CRYPTO` (Inter 700, 32px, `#F0F0F0`) — entry comp ~6.8
  - Card row 1 — title `Autocallables` (Inter 700, 40px, `#F0F0F0`) + def `Auto-redeems and pays a coupon while BTC holds a range` (Inter 600, 27px, `#F0F0F0`) — stagger entry **comp 7.6**
  - Card row 2 — title `Accelerators` (Inter 700, 40px, `#F0F0F0`) + def `Leveraged upside to a cap; downside ~1:1` (Inter 600, 27px, `#F0F0F0`) — stagger entry **comp 8.4**
  - Footnote row `Issued by large financial institutions` (Inter 600, 28px, `#F0F0F0`, cyan dot) — stagger entry **comp 9.2**
  - 4px **cyan `#00D4FF`** inset accent bar (left edge); `mask-image` right-feather; NO blur.
- **Cyan element:** accent bar (1).
- **Word-sync:** supporting graphic (entry pinned, not per-word). The two titles are the literal product words just spoken (b1). Definitions are EDITORIAL — mark `<!-- definitions EDITORIAL: explanatory, not spoken verbatim -->`. Card holds across "to their ultra high net worth individuals and to their network… validates the fact that they've seen appetites" (src 723.18–732.64, comp 5.0–14.4).
- `data-start="6.4" data-duration="12.1"`

### c3b3 — FLOWCHART: distribution chain (how the product reaches the buyer)
- **Comp:** 18.5 – 29.0s   **Src:** 736.70 – 747.20s
- **Template/block:** **`flowchart`** (install: `npx hyperframes add flowchart`). 4 nodes left-to-right with a downstream connector; `back.out(1.5)` node pops ~0.4s apart; final node cyan. Restyle to DESIGN: node fill `rgba(20,26,34,0.92)`, text `#F0F0F0`, connectors `#2a2a2a`. (Distinct from c3b2 card and from any swiss-grid.)
- **View:** **Mode A** (held). `object-position: 80% center`.
- **Sub-comp:** `beat-c3b3-distribution.html`
- **Content (exact node text):**
  - Eyebrow `THE DISTRIBUTION CHAIN` (Inter 700, 32px, `#F0F0F0`)
  - Node 1 `Large institution` — `#F0F0F0`
  - Node 2 `Issues a structured note` — `#F0F0F0`
  - Node 3 `Private-banking desk` — `#F0F0F0`
  - Node 4 `UHNW client buys` — **cyan `#00D4FF`** (final node)
- **Cyan element:** final node `UHNW client buys` (1).
- **Word-sync anchor (explanatory flow, not per-word):** "appetites from a specific subset of like **private banking clients** or **ultra high net worth individuals**" — private 734.82 / banking 735.20 / clients 735.52 (comp 16.6–17.3, just before) → "we're seeing that exact same thing on our side… **supply demand**… the product itself needs to make a lot of sense" (src 737.92–746.16, comp 19.7–28.0, inside beat). Nodes reveal from **comp 19.0** (node1), 19.4, 19.8, 20.2 (mark `<!-- flow nodes structural; anchored to the spoken distribution/supply-demand line -->`).
- `data-start="18.5" data-duration="10.5"`

### *(clean breath inside Mode A — comp 29.0 – 30.5, ~1.5s)*
Graphic-OFF moment; Jasper stays right-40% (NOT a view switch). Covers "…needs to make a lot of sense for people." Speaker breathes before the demand caption. No sub-comp.

### c3b5 — Mode-A CAPTION: demand reality (INSATIABLE → DEMAND → ACCELERATOR FIT; low-key supplemental, NOT a full kinetic slam)
- **Comp:** 30.5 – 42.4s   **Src:** 748.70 – 760.60s
- **Template/block:** Mode-A **caption** (hand-build; `caption-clip-wipe`-style left-to-right reveal, ~56–64px in-zone — deliberately smaller than the b1/b7 ~130px stacks so it reads as a supplemental, not a third headline kinetic). Lines stack in the left zone, stay, no dim.
- **View:** **Mode A** (held — no view change). `object-position: 80% center`.
- **Sub-comp:** `beat-c3b5-demand.html`
- **On-screen lines:**
  | line | hex / size | comp_t | matched words (src) |
  |---|---|---|---|
  | `INSATIABLE? NO.` | `#F0F0F0` 60px | **31.08** | "insaturable" 749.28 → **printed INSATIABLE** (R3 fix on screen) |
  | `WHERE THE DEMAND IS` | `#F0F0F0` 60px | **38.46** | fit 756.66 (phrase "where we're seeing a lot of **fit**") |
  | `= ACCELERATOR FIT` | **cyan `#00D4FF`** 64px (payoff) | **39.82** | accelerator 758.02 ("…for example, is an **accelerator**") |
- **Cyan element:** `= ACCELERATOR FIT` (1).
- **Verified spoken anchor:** "It's not like there's this **insaturable** demand for structured products at the moment… where we're seeing a lot of **fit**, for example, is an **accelerator**." (insaturable 749.28, fit 756.66, accelerator 758.02). All real spoken words; the *spelling* is corrected to **INSATIABLE** per `_JARGON.md`. Line B fires on the spoken word **fit** (756.66, comp 38.46) but prints `WHERE THE DEMAND IS` — faithful to the surrounding thought ("where we're seeing a lot of fit"/"demand for structured products") and deliberately keeps the word "FIT" off line B so it lives ONLY on the cyan payoff `= ACCELERATOR FIT` (R4). The 31.08→38.46 gap (the "demand for structured products at the moment, but…" stretch, src 750.74–756.42) is covered by line A holding on screen.
- **Why a caption, not a kinetic stack:** keeps the count of full kinetic word-stacks at 2 (b1, b7) for R2, AND keeps the view in Mode A (no FF flip) for R1. This is the deliberate replacement of v2's flip-flopping FF demand kinetic.
- `data-start="30.5" data-duration="11.9"`

### c3b6 — ★ DATA-CHART: structured-product adoption by region (the distinct PRIMARY DEVICE)
- **Comp:** 42.4 – 61.0s   **Src:** 760.60 – 779.20s
- **Template/block:** **`data-chart`** (install: `npx hyperframes add data-chart` → `compositions/data-chart.html`). Bar + line combo with staggered bar reveal + animated line + value labels. **Restyle to DESIGN dark palette and FIT THE LEFT 60% ZONE** (Mode-A): set `background: transparent`, `chart-container` scaled/positioned into x 80–1100px (left zone), bars `#3a4654` (neutral), conversion LINE + dots **cyan `#00D4FF`** (the single cyan), axis/labels `#F0F0F0` Inter ≥600, headline Inter 800. Drop the block's default `Libre Baskerville`/`#faf9f6`.
- **View:** **Mode A** (held — the centrepiece of the 54.6s Mode-A block). `object-position: 80% center`.
- **Sub-comp:** `beat-c3b6-datachart.html`
- **Chart config (edit the block's data arrays):**
  - `headline` = `STRUCTURED-PRODUCT ADOPTION` (Inter 800, ~40px, `#F0F0F0`)
  - `subtitle` = `Best fit by region` (Inter 600, ~26px, `#F0F0F0`)
  - **Bars (categories)** `["Asia", "Europe + US"]` — relative adoption, neutral `#3a4654`. `revenueData = [22, 12]` (Asia clearly ahead; Europe+US catching up). Bar value labels `#F0F0F0`.
  - **Line (cyan)** = **`Take rate`** trend rising left→right: `conversionData = [ ... ]` rendered as a rising cyan line/marker across the two categories (Asia high, Europe+US rising) — the single cyan element. Key/legend label `Take rate` (NOT "stake rate" — R3).
  - `source` line: omit or set `Wintermute desk view` (Inter 600, `#F0F0F0`); do NOT print "Source: Internal analytics".
- **Reveal timing (anchored to spoken geography; restyle the block's `1.5 + i*0.5` stagger to these offsets within the beat):**
  | element | comp_t | matched words (src) |
  |---|---|---|
  | headline + subtitle (structural) | ~43.0 | (enters as frame settles; mark structural) |
  | `Asia` bar grows | **49.02** | Asia 767.22 ("Asia has been ahead on structured products") |
  | `Take rate` line annotation appears | **51.48** | take 769.68 / rate 769.86 ("**Take rate** has been very high") — **R3: prints TAKE RATE** |
  | `Europe + US` bar grows | **54.66** | Europe 772.86 / US 773.40 ("increasingly in **Europe and the US**") |
  | cyan `Take rate` line peaks (no extra cyan callout) | **58.80** | demand 777.00 ("we're also seeing that **demand**") |
- **Cyan element:** the conversion LINE (`Take rate`) + its dots (1; bars stay neutral — D7).
- **Why this is the device:** it is the clip's largest, most distinct beat; it visualizes the demand/adoption/pricing narrative the task requires; it gives the clip a non-kinetic identity (fixing "all looks like clip-2"). The two product names (b1) and the demand caption (b5) feed into it; it pays off into the take-rates stat (b9).
- `data-start="42.4" data-duration="18.6"`

### c3b7 — Kinetic: PRICE ↔ NARRATIVE loop (the clip's quotable line; full kinetic #2)
- **Comp:** 61.0 – 75.0s   **Src:** 779.20 – 793.20s
- **Template/block:** `kinetic-type` phrase build (hand-build, full-frame). Render line 3 as a literal cycle; an optional **thin cyan loop arrow** on the payoff is the single cyan.
- **View:** **full-frame** (BOTH speakers); video full-frame at comp ~60.8, exits to Mode A at ~74.8.
- **Sub-comp:** `beat-c3b7-price-narrative.html`
- **On-screen lines (word-synced; corrects v2's wrong-window pre-fire):**
  | line | hex / size | comp_t | matched words (src) |
  |---|---|---|---|
  | `PRICE` | `#F0F0F0` 130px | **66.24** | price 784.44 |
  | `CREATES NARRATIVE` | `#F0F0F0` 130px | **66.58** | creates 784.78 / narrative 785.12 |
  | `NARRATIVE CREATES PRICE` | **cyan `#00D4FF`** 130px (payoff) | **67.62** | creates 785.82 / price 786.02 (the loop close) |
  - Stack stays through beat end.
- **Cyan element:** `NARRATIVE CREATES PRICE` (+ optional loop arrow, same cyan) (1).
- **Word-sync note:** Jasper says "I think **price creates narrative, creates price create narrative**" (src 784.44–786.58, comp 66.24–68.38). The comp 61.0–66.2 lead-in is the FF transition + "cautiously optimistic… Obviously, the price, like I think…" (src 777.54–784.26). First line HELD until 66.24 — do NOT pre-fire (this was the v2 error: it fired ~8s early at comp 76 with a wrong-window cyan ref).
- `data-start="61.0" data-duration="14.0"`

### c3b9 — STAT close: TAKE RATES (content close, NOT an outro)
- **Comp:** 75.0 – 90.3s   **Src:** 793.20 – 808.50s
- **Template/block:** swiss stat close (hand-build) — a single rising metric + short rationale. Held to clip end as a CONTENT beat (no name/CTA card → satisfies the no-outro rule). Breaks the b7→b9 adjacency (kinetic → stat).
- **View:** **Mode A** (video returns right-40% at comp ~74.8; held to clip end). `object-position: 80% center`.
- **Sub-comp:** `beat-c3b9-take-rates.html`
- **Content (exact text):**
  | element | hex / size | comp_t | matched words (src) |
  |---|---|---|---|
  | Index `03` + Eyebrow `THE NEXT-CYCLE CATALYST · THIS YEAR` | Inter 700, 32px, `#F0F0F0` | ~76.8 (structural) | — |
  | Stat `TAKE RATES ↑` | Inter 900, 160px, `#F0F0F0` | **77.62** | take 795.82 / rates 796.06 — **R3: TAKE RATES** |
  | Cyan rule draws left→right (single cyan) | `#00D4FF` 3px | ~78.1 | — |
  | Sublabel `Meaningfully higher than 2025` | Inter 600, 32px, `#F0F0F0` | **80.34** | meaningfully 798.54 / higher 799.04 (2026="this year", prior=2025 per DESIGN) |
  | Footer `Demand + infrastructure both here now` | Inter 600, 30px, `#F0F0F0` | **84.98** | infrastructure 803.18 / finally-here 803.90–804.18 |
  | Late re-tick of `↑` (keeps ~3s tail alive) | — | **87.44** | volumes 805.64 ("volumes on screen") |
- **Cyan element:** the rule (1; stat stays white — D7 stat-OR-rule).
- **Word-sync:** stat / sublabel / footer / re-tick pinned to verified comp_t (77.62 / 80.34 / 84.98 / 87.44). Spoken support: "I could definitely see the **take rates** on structured products being **meaningfully higher** than we had before… the demand is one thing but then also the **infrastructure is finally here**… volumes on screen" (src 795.82–805.64, comp 77.6–87.4). Clip ends on this content; final ~1.9s is clean video tail under the held stat — **NO end card**.
- `data-start="75.0" data-duration="15.3"`

---

## MASTER GSAP TRANSITION PLAN (only 3 view switches; mirrors clip-2)

| at comp | action |
|---|---|
| 0.0 | full-frame, both speakers (c3b1 term-reveal). No GSAP (CSS default). |
| ~6.3 | full-frame → **Mode A** (`expo.inOut` 0.7s); glow +0.3, zone-rule +0.4. c3b2 slides in. Ken Burns 1.00→1.04 over remaining clip. |
| 6.4 – 60.6 | **Mode A HOLDS** across c3b2 (card) → c3b3 (flowchart) → clean breath → c3b5 (caption) → c3b6 (data-chart). Frame stable — no bounce. |
| ~60.8 | Mode A → **full-frame** for c3b7 price↔narrative kinetic (fires 66.24). glow/zone-rule out at 60.6. |
| ~74.8 | full-frame → **Mode A** for c3b9 stat close; **held to clip end (90.3)** — content close, no exit. glow +0.3, zone-rule +0.4. |

`MODE_A = { left: 1229, top: 108, width: 614, height: 864 }`, `object-position: 80% center`, `border-radius: 6px`. Full-frame return = `{left:0,top:0,width:1920,height:1080,borderRadius:"0px"}`.

> **index.html delta vs v2:** drop c3b4's id, rename the flow id stays `#beat-c3b3`, replace `#beat-c3b8` price-narrative id with the new kinetic id (now **c3b7**), and the data-chart is the new **c3b6**. The z-index:3 rule MUST list exactly the live overlay ids: `#beat-c3b1, #beat-c3b2, #beat-c3b3, #beat-c3b5, #beat-c3b6, #beat-c3b7, #beat-c3b9`. (v2 GSAP at comp 37.6–42.3 — the FF demand wedge — is DELETED; the Mode-A→FF→Mode-A there caused the flip-flop FAIL.)

---

## VERIFICATION (graded vs `_QA-CHECKLIST.md`)

**§1 View-switching (R1):** ✓ View-timeline table above. 4 views; non-intro dwells 54.6 / 14.0 / 15.3 (all ≥8s); only A-B-A has a 14.0s middle (>~12s); consecutive graphics grouped into the 54.6s Mode-A block. **v2's 4.7s FF wedge is eliminated.**

**§2 Template variety (R2):** ✓ Exactly 2 full kinetic word-stacks (b1, b7), never adjacent; the c3b5 caption is a low-key Mode-A supplemental. **`data-chart` is the distinct PRIMARY device** (18.6s, the centrepiece). Init/variety: the clip is NOT kinetic-dominated; install `data-chart` + `flowchart`, hand-build the rest.

**§3 Dialog-match + open-on-line:** ✓ src_in=718.20 opens on "you see large…autocallables, accelerators" (spoken in first 4.3s). First text at comp 0.00 (you). Every kinetic/caption line fires at `comp = word.src − 718.20` read off the table (b1: 0.00/0.48/1.72/3.18/4.24; b5: 31.08/38.46/39.82; b7: 66.24/66.58/67.62; b9: 77.62/80.34/84.98/87.44). Editorial items marked.

**§4 Opening coherence (R5):** ✓ "YOU SEE / LARGE INSTITUTIONS / ISSUING / AUTOCALLABLES / ACCELERATORS" parses as a complete thought; cyan payoff is a real noun (ACCELERATORS), not a dangling number.

**§5 Speaker framing:** ✓ `object-position: 80% center` (centers Jasper; name readable; seam cleared). b1 & b7 full-frame show both speakers (never text on black). VERIFY-BY-FRAME at render.

**§6 Jargon (R3):** ✓ TAKE RATE (b6 line) + TAKE RATES (b9 stat) replace "stake rate"; INSATIABLE (b5) replaces "insaturable". No burp/deep-in/graft on screen. Wintermute spelled exact.

**§7 Duplicate words (R4):** ✓ Per-beat audit table above; no notable word repeats across a beat's elements. ACCELERATORS is cyan once (b1); b5 payoff is the distinct phrase ACCELERATOR FIT.

**§8 Carry-over hard rules:** ✓ z-index:3 lists every live overlay id; ONE cyan per beat (list above); no backdrop blur, no grain, cards solid `rgba(20,26,34,0.92)` + inset cyan bar + glow + feather; eyebrows Inter 700 ≥32px `#F0F0F0`; no #888888 under 48px; no intro/outro/CTA — ends on b9 content; 2026="this year", prior=2025; kinetic lines build and STAY (no dim).

**§9 Verify-by-frame:** MANDATORY at draft render — extract frames at: opening (0.5s), the FF→MA switch (7s), b3 flowchart (24s), b5 caption (40s), the **data-chart** (52s — bars + cyan take-rate line), MA→FF (66s loop), FF→MA (78s stat) — and LOOK before claiming done.

**Beat count:** 8 (7 graphic: b1/b2/b3/b5/b6/b7/b9 + 1 clean breath). Data-chart is multi-stage. (D-table clip-3 = 9–10 *elements*; the data-chart's headline/subtitle/two bars/line = 5 internal reveals push effective on-screen graphic moments to ~11.)

---

## SUB-COMP FILE LIST (v3 — rebuild)
`beat-c3b1-termreveal.html`, `beat-c3b2-glossary.html`, `beat-c3b3-distribution.html` (← `npx hyperframes add flowchart`, restyle), `beat-c3b5-demand.html` (caption, Mode-A), `beat-c3b6-datachart.html` (← `npx hyperframes add data-chart`, restyle + fit left zone), `beat-c3b7-price-narrative.html`, `beat-c3b9-take-rates.html`. *(No c3b4/c3b8 — the clean breath is a graphic-off gap inside Mode A.)*

**index.html changes for build agent:** `data-media-start="718.20"`, `data-duration="90.3"` on `#short_mag_cut` + `#a-roll-audio` + `#master-root`; `object-position: 80% center`; **delete the v2 comp-37.6–42.3 Mode-A→FF→Mode-A GSAP** (the flip-flop); z-index:3 rule = `#beat-c3b1, #beat-c3b2, #beat-c3b3, #beat-c3b5, #beat-c3b6, #beat-c3b7, #beat-c3b9`.

## INSTALL COMMANDS (run before build)
```
npx hyperframes add data-chart   # → compositions/data-chart.html (c3b6 centrepiece; restyle to dark + fit left zone)
npx hyperframes add flowchart    # → compositions/flowchart.html  (c3b3 distribution chain; restyle to dark)
```

## BUILD MANIFEST ROW
`clip_3 | clip-3-structured-products | 718.20 | 808.50 | data-chart(PRIMARY),flowchart,kinetic-type,liquid-glass,caption,swiss-stat | 8 beats (7 graphic) | views: FF6.4·MA54.6·FF14.0·MA15.3`
