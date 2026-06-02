# Clip 3 — BUILD-READY EDL v4 (`clip-3-structured-products`)

> Supersedes `clip3-edl-v3.md`. **v3 was REJECTED** ("Everything has an issue") for two top-priority faults plus four spec defects. This **v4 (rev-2)** keeps every fix that passed and adds **15 verified content/pacing corrections** caught by re-grading the spec against the ground-truth word table AND the on-disk build (which is still v3 — confirming §0 is required).
>
> **The two top-priority faults (still the headline):**
> - **R6 (NO INDEX) — FAIL.** Every beat rendered the internal clip number `03` (a meaningless on-screen artifact). v3 even *mandated* it as the "3rd element" in c3b1. **v4 deletes `03` everywhere** and replaces the opening "3rd element" with a real editorial mark. *(On-disk build STILL has `03` in c3b1 L31, c3b2 L17, c3b3 L21, c3b5 L20, c3b6 L23, c3b9 L20 — 6 instances — §0 unfixed.)*
> - **R7 (VIEW MATCHES CONTENT — no blank-left Mode-A) — FAIL.** v3 wedged a **graphic-OFF "clean breath" (comp 29.0–31.08) INSIDE the Mode-A block** — Jasper cropped right-40% with an EMPTY left half (the clip-8 0:33–0:52 bug). **v4 eliminates the gap** by holding the c3b3 flowchart on screen through the breath. *(On-disk: index.html L96 still declares the breath; c3b3 exits at offset 10.0 = comp 28.5; c3b5 starts at 30.5 — gap present — §0 unfixed.)* **rev-2 fix #1 closes a residual MICRO-gap the v4 spec itself left at the c3b3→c3b5 seam.**
>
> **v4 (rev-1) fixes, KEPT:** Defect 1 (c3b9 footer ticks → two word-synced ticks at comp 83.42 / 84.98; stray 85.56 deleted); Defect 3 (c3b3 node 2 = `Issues a note`, STRUCTURED only in eyebrow — R4); Defect 4 (c3b1 prints `ISSUING`, never non-spoken "are"). **Defect 2 (c3b7 lead-in) is REVISED in rev-2 — see #10/#11: the `THE PRICE` lead-in is DROPPED for a clean full-frame breath, because the lead-in created its own R4 triple-print of "PRICE".**
>
> **rev-2 content/pacing corrections (this round):** #1 c3b3→c3b5 R7 micro-gap (overlap the beats); #2 c3b1 eyebrow forward to comp ~2.2 (real 3-layer open, fixes D1); #3/#4 c3b2 distinct eyebrow (kills the duplicate-eyebrow stuck-frame seam); #5 c3b9 "exactly ONE cyan" gate (✓ glyphs + ↑ arrow neutral); #6 c3b6 annotation anchored to the line peak (was floating below the chart); #7 c3b6 trimmed to kill 2.2s dead-chart tail; #8 c3b5 intermediate line (kills 7.4s single-line hold); #9 c3b5 eyebrow re-label (vary the "demand" framing); #10/#11 c3b7 clean FF breath instead of `THE PRICE` lead-in; #13 honest "hand-built" labeling for c3b3/c3b6; #14 c3b6 carries a quantified anchor; #15 c3b9 deliberate terminal button.
>
> **Carried forward from v3 (verified, KEEP):** dialog-matched term-reveal open; a distinct PRIMARY data device; `object-position: 80% center` framing; `src_out 808.50` ("…option exchanges"); R5-coherent open; no-outro content close; z-index:3 completeness.

---

## TIMING SOURCE OF TRUTH (authoritative — re-derived from audio.json this round)

| field | value | why |
|---|---|---|
| `src_in` | **718.20** | Opens ON "you" (audio.json: `you` start = **718.20** exactly). First spoken words on screen: *"You see large financial institutions issuing stuff like **autocallables, accelerators**."* Trims the "Yeah, yeah… decade off… 2016, 17, BTC as underlying" filler (src 700–717.62). |
| `src_out` | **808.50** | Lands just after "…volumes on screen on option exchanges" (`exchanges,` 808.32→808.88) so the take-rates/infrastructure payoff resolves on a complete clause. No outro. |
| duration | **90.3s** | `comp = src − 718.20`. |
| `data-media-start` | **718.20** | source.mp4 is the FULL episode (2853s, 1920×1080, 30fps); media-start is absolute episode time. |

> **Conversion rule (binding):** `comp = src − 718.20`. Every fire-time below was READ from `clip3-words.txt` (its `src` column is authoritative) and converted, then **re-verified against `.context/episodes/restream-may18/audio.json`** word-by-word. The words.txt "comp = src − 700" column is RELATIVE TO THE TABLE WINDOW (700s), NOT the clip in-point — it is correctly ignored; only the `src` column is used.

**Opening line (verbatim, audio.json):** "You see large financial institutions issuing stuff like **autocallables, accelerators**." — a complete statement (R5): *who* (large institutions) *does what* (issues) *which products* (autocallables, accelerators). Signature terms SPOKEN inside the first ~4.3s → the term-reveal open is honest, not anticipatory.

---

## R6 — NO INDEX (top-priority fix this round)

**The bare clip number `03` (and any beat index) is FORBIDDEN as on-screen text.** It is an internal artifact, meaningless to a viewer. v3 printed `03` in c3b1, c3b2, c3b3, c3b5, c3b6, c3b9 — **ALL DELETED in v4.** Editorial eyebrow labels (e.g. `STRUCTURED PRODUCTS · CRYPTO`) are fine and remain; only the number is removed.

**On-screen index/number scan — every beat must read ZERO:**

| beat | on-disk build (v3, line) | v4 |
|---|---|---|
| c3b1 | `03` mono index (L31) as the "3rd element" | **REMOVED.** 3rd element is now a neutral `#2a2a2a` rule + the eyebrow (no number), brought forward to comp ~2.2 (#2). |
| c3b2 | `03` mono index (L17) | **REMOVED.** New distinct eyebrow `WHAT THEY'RE SELLING` (#4). |
| c3b3 | `03` mono index (L21) | **REMOVED.** Eyebrow `THE DISTRIBUTION CHAIN` only. |
| c3b5 | `03` mono index (L20) | **REMOVED.** (caption has no chrome index). |
| c3b6 | `03` mono index (L23) | **REMOVED.** Eyebrow `STRUCTURED PRODUCTS · BY REGION` + headline `STRUCTURED-PRODUCT ADOPTION`. |
| c3b9 | `03` mono index (L20) | **REMOVED.** Eyebrow `THE NEXT-CYCLE CATALYST · THIS YEAR` only. |

**BUILD-AGENT MANDATE (R6):** delete the `id="bN-idx"` element AND its `.bN-idx` CSS AND its GSAP `tl.fromTo("#bN-idx", …)` tween from every sub-comp (`beat-c3b1`, `-c3b2`, `-c3b3`, `-c3b5`, `-c3b6`, `-c3b9`). Grep-gate after edit: `grep -RnE ">0?3<|class=\"b[0-9]-idx" compositions/` must return **nothing**. (Numbers that are DATA — chart axis ticks/value labels, "2025" baseline, percentages — are fine; only the clip-number chrome is banned.)

---

## ★ VIEW-TIMELINE — proves R1 (no flip-flop) AND R7 (view matches content; no blank-left Mode-A)

Source is a side-by-side (Nic host LEFT, Jasper guest RIGHT). Two views: **FULL-FRAME** (FF, both speakers, kinetic over them) and **MODE-A** (MA, guest framed right-40%, graphic in left-60%). **Every Mode-A segment names the graphic that fills it — no segment is graphic-less.**

| view | comp range | dwell | what fills it (Mode-A: graphic on screen the ENTIRE time) | R1/R7 check |
|---|---|---|---|---|
| **FF** | 0.0 – 6.4 | **6.4s** | c3b1 term-reveal kinetic over BOTH speakers | intro zone (0–6s): quick switch allowed; never loops back ✓ |
| **MODE-A** | 6.4 – 61.0 | **54.6s** | **continuous graphic, zero gaps:** c3b2 card (6.4–18.5) → **c3b3 flowchart held & OVERLAPPED into c3b5 (18.5–~31.4)** → c3b5 caption (31.0–42.4) → c3b6 data-chart (42.4–61.0) | ≥8s ✓; **R7 ✓ — a graphic is on screen at EVERY instant** (v3's 29.0–31.08 blank-left is GONE; rev-2 #1 overlaps the c3b3→c3b5 seam so neither the flowchart-fade nor the caption-wipe leaves the left zone near-empty) |
| **FF** | 61.0 – 75.0 | **14.0s** | c3b7: **clean both-speaker breath 61.0–66.0**, then price↔narrative loop kinetic 66.2–74.6 over BOTH speakers | ≥8s ✓; the only A-B-A middle is **14.0s > ~12s** ✓; the 61–66 breath is FULL-FRAME (both speakers), R7-safe |
| **MODE-A** | 75.0 – 90.3 | **15.3s** | c3b9 take-rates stat card (held to clip end) | ≥8s ✓; graphic present throughout ✓ |

- **No segment < 8s outside the 0–6s intro.** ✓ (54.6 / 14.0 / 15.3)
- **No A-B-A within ~12s.** ✓ The only A-B-A is MA(54.6s)→FF(14.0s)→MA(15.3s); the FF middle is 14.0s, clearing the ~12s window.
- **R7 — NO blank-left Mode-A.** ✓ NO graphic-off moment inside any Mode-A block. v3's "clean breath" (29.0–31.08) is eliminated by holding the c3b3 flowchart through it AND overlapping it with the c3b5 caption entry (#1). The only graphic-off video is FULL-FRAME (both speakers): the 0–6s lead before c3b1 text, the FF transitions, and the deliberate **c3b7 61–66 clean breath** (both speakers, R7-safe).
- **Consecutive graphics grouped.** c3b2/c3b3/c3b5/c3b6 ALL live in the one 54.6s Mode-A view — frame rock-stable across the body. ✓

**Transition events (only 3 view switches in the whole clip):**
| at comp | switch |
|---|---|
| ~6.3 | FF → **Mode A** (`expo.inOut` 0.7s); glow +0.3, zone-rule +0.4; c3b2 card slides in; Ken Burns 1.00→1.04 begins |
| ~60.8 | **Mode A → FF** (`expo.inOut` 0.4s); glow/zone-rule out at 60.6; **clean both-speaker breath 61–66**, then c3b7 loop kinetic 66.2+ |
| ~74.8 | **FF → Mode A** (`expo.inOut` 0.4s); glow +0.3, zone-rule +0.4; c3b9 stat close; **held to clip end (90.3) — no exit** |

---

## FRAMING — verified from real frames (kept from v3)

**`object-position: 80% center`** (centers Jasper, guest, right half — clears the x=960 seam; name "Jasper De Maere · Wintermute" fully readable). `MODE_A = { left: 1229, top: 108, width: 614, height: 864 }`, `border-radius: 6px`, `object-fit: cover`, slow Ken Burns 1.00→1.04. (50%/62% center the seam/host = FAIL; 76% bleeds host; 83% leans Jasper left; **80% chosen**.) FF beats (b1, b7) show BOTH speakers — never text on black. Full-frame return = `{left:0,top:0,width:1920,height:1080,borderRadius:"0px"}`. On Mode A: `#bg-glow` opacity→1 at +0.3s, `#zone-rule` `scaleY 0→1` at +0.4s (`power4.out`).

---

## STYLE (binding — DESIGN.md)

bg `#0A0A0A`; primary text `#F0F0F0`; muted secondary `#B6BEC6` (**never `#888888`**); **ONE cyan `#00D4FF` element per beat**; cards `rgba(20,26,34,0.92)` solid fill + 4px **inset** cyan accent bar + soft glow + 1px border + `mask-image` right-feather — **NO `backdrop-filter` blur, NO film grain**. Eyebrow Inter 700 ≥32px `#F0F0F0`; body/bullets Inter ≥600. Kinetic phrase lines Inter 900 ~130px white, payoff line cyan; lines slam in and **STAY** (no dim). 2026 = "this year", 2025 = prior. **No intro card, no outro/CTA** — ends on b9 content held to clip end. **No on-screen clip number (R6).**

---

## ★ TEMPLATE VARIETY — proves R2

| order | beat | template / block | kinetic? |
|---|---|---|---|
| 1 | c3b1 | `kinetic-type` phrase build (term-reveal) | **kinetic #1** |
| 2 | c3b2 | liquid-glass card (hand-build, DESIGN Cards & Panels) | — |
| 3 | c3b3 | **flowchart-style** node flow (hand-built dark — see #13) — distribution chain (held & overlapped) | — |
| 4 | c3b5 | Mode-A **caption** (low-key supplemental, ~56–64px — NOT a full ~130px slam) | low-key |
| 5 | c3b6 | **data-chart-style SVG** (hand-built to fit Mode-A left zone — see #13) — **PRIMARY DEVICE**, adoption by region | — |
| 6 | c3b7 | clean FF breath → `kinetic-type` phrase build (the quotable loop) | **kinetic #2** |
| 7 | c3b9 | stat close — hand-build swiss stat (single rising metric) | — |

- **≤2 kinetic word-stacks in a row:** the only two full kinetic stacks are **c3b1** and **c3b7**, separated by the entire 54.6s Mode-A body — NEVER adjacent. The c3b5 caption is a deliberately low-key Mode-A supplemental (small, in-zone), not a full-frame slam, so it does not count toward "kinetic in a row." ✓
- **Distinct PRIMARY device:** the **data-chart adoption curve** is the single largest beat (~17.2s after the #7 trim) and the visual centrepiece — matches DESIGN per-clip map (*clip 3 = `data-chart` (demand/adoption) + term-reveal*). ✓
- **#13 — "Did I consider a catalog block?" (R2) answered honestly:** BOTH "install" beats are **hand-built**, by deliberate choice: the catalog `flowchart` block is a multi-branch DECISION-TREE with a cursor/emoji click-sim (wrong shape for a linear 4-node distribution chain), and the catalog `data-chart` block ships `Libre Baskerville`/`#faf9f6` and a full-width layout (wrong palette + doesn't fit the Mode-A left 60% zone). Both were considered and rejected for FIT, and re-implemented as distinct equivalents (connector-drawn node flow; dark SVG bar+line). **The QA gate must NOT fail these for not matching the catalog block's markup** — they satisfy R2 (distinct device, not another kinetic) on substance.

---

## ★ JARGON AUDIT — proves R3 (every on-screen string mapped through `_JARGON.md`)

| on-screen string | beat | `_JARGON.md` status |
|---|---|---|
| AUTOCALLABLES | b1, b2 | correct casing ✓ |
| ACCELERATORS / Accelerators / ACCELERATOR | b1, b2, b5, b6 | correct casing ✓ |
| INSATIABLE? NO. | b5 | **corrects "insaturable" (src 749.28)** → R3 fix on screen ✓ |
| TAKE RATE (line annotation + value labels) | b6 | **corrects "Stake rate" (src 769.68)** ✓ |
| TAKE RATES (stat) | b9 | **corrects "stake rate"** → headline take-rate term ✓ |
| Wintermute (name tag, in source video; "Wintermute desk view" source line) | all MA | exact ✓ |
| Asia / Europe + US | b6 | plain nouns ✓ |
| Structured products / STRUCTURED-PRODUCT | b2, b6, b9 | plain ✓ |

No `burp`/`deep-in`/`graft`/`stake-rate`/`insaturable`/`meme-con` reaches the render. ✓

---

## ★ DUPLICATE-WORD AUDIT — proves R4 (per beat: eyebrow vs sublabel/title/nodes)

| beat | elements | notable-word overlap? |
|---|---|---|
| b1 | YOU SEE / LARGE INSTITUTIONS / ISSUING / AUTOCALLABLES / ACCELERATORS / eyebrow `STRUCTURED PRODUCTS · CRYPTO` | none repeat ✓ ("are" NOT printed — only spoken words, in order) |
| b2 | eyebrow **`WHAT THEY'RE SELLING`** (#4 — was `STRUCTURED PRODUCTS · CRYPTO`); titles `Autocallables`, `Accelerators`; defs; footnote `Issued by large financial institutions` | distinct words; no element repeats another's notable word ✓; **and no longer duplicates the b1 eyebrow across the seam (#3/#4)** |
| b3 | eyebrow `THE DISTRIBUTION CHAIN`; nodes `Large institution`→**`Issues a note`**→`Private-banking desk`→`UHNW client buys` | **node 2 = `Issues a note` (NOT "Issues a structured note")** so the notable word STRUCTURED lives ONLY in the eyebrow → R4 ✓ |
| b5 | eyebrow **`THE REAL APPETITE`** (#9 — was `DEMAND REALITY`); line A `INSATIABLE? NO.`; mid line `NOT FOR EVERYTHING` (#8); line B `WHERE THE DEMAND IS`; payoff `= ACCELERATOR FIT` | "FIT"/"ACCELERATOR" in exactly ONE element (cyan payoff); eyebrow no longer keys off "demand" (#9); "DEMAND" appears only in line B ✓ |
| b6 | eyebrow `STRUCTURED PRODUCTS · BY REGION`; headline `STRUCTURED-PRODUCT ADOPTION`; subtitle `Best fit by region`; bars `Asia` / `Europe + US`; line `Take rate` + value labels | "take rate" in ONE element (cyan line+labels); headline="adoption", subtitle="fit/region" → no dup ✓ |
| b7 | `PRICE` / `CREATES NARRATIVE` / payoff `NARRATIVE CREATES PRICE` (**NO `THE PRICE` lead-in — dropped, #10**) | "PRICE"/"NARRATIVE" recur ACROSS the loop lines **by design** (the loop IS the device: price→narrative→price; the cyan payoff is the closing inversion). Dropping the lead-in removes the 3rd redundant print of "PRICE" the v4-rev1 lead-in introduced. ✓ |
| b9 | eyebrow `THE NEXT-CYCLE CATALYST · THIS YEAR`; stat `TAKE RATES ↑`; sublabel `Meaningfully higher than 2025`; footer ticks `DEMAND ✓` / `INFRASTRUCTURE ✓`; terminal line `VOLUMES ON-CHAIN NOW` (#15) | "take rates" only in the stat; eyebrow/sublabel/footer/terminal share no notable word ✓ (eyebrow prints `THIS YEAR` not literal `2026`; `2025` baseline sanctioned as prior-year) |

**ONE cyan per beat:** b1 `ACCELERATORS` · b2 accent bar · b3 final node `UHNW client buys` · b5 payoff `= ACCELERATOR FIT` · b6 the `Take rate` line + dots + its value labels (all cyan, one element type) · b7 `NARRATIVE CREATES PRICE` (+ loop arrow, same cyan) · b9 the rule (stat WHITE, ✓ marks + `↑` arrow + terminal line all neutral `#B6BEC6`/`#F0F0F0` — D7 stat-OR-rule). ✓ **See #5 — c3b9 needs a "exactly ONE cyan" frame gate.**

---

# BEAT MAP

Every beat: `id` · comp range · src range · template/block · view · sub-comp filename · full on-screen text (exact hex) · per kinetic line the **comp_t + matched transcript words** (read off `clip3-words.txt`/audio.json, `comp = src − 718.20`).

---

### c3b1 — Kinetic TERM-REVEAL (opening; word-synced, dialog-matched, R5-coherent)
- **Comp:** 0.0 – 6.4s   **Src:** 718.20 – 724.60s
- **Template/block:** `kinetic-type` phrase build (hand-build, DESIGN palette). Term words get a heavier slam (0.04em tracking).
- **View:** **FULL-FRAME** (BOTH speakers) over a left dark-gradient backdrop. Video begins Mode-A transition at comp ~6.3.
- **Sub-comp:** `beat-c3b1-termreveal.html`
- **On-screen lines (each slams in, STAYS, no dim):**
  | line | hex / size | comp_t | matched words (src) |
  |---|---|---|---|
  | `YOU SEE` | `#F0F0F0` 120px | **0.00** | you 718.20 / see 718.46 |
  | `LARGE INSTITUTIONS` | `#F0F0F0` 120px | **0.48** | large 718.68 / institutions 719.30 |
  | `ISSUING` | `#F0F0F0` 120px | **1.72** | issuing 719.92 — **(Defect-4 fix: prints `ISSUING` only; "are" is NOT spoken, NOT printed)** |
  | `AUTOCALLABLES` | `#F0F0F0` 130px | **3.18** | autocallables 721.38 |
  | `ACCELERATORS` | **cyan `#00D4FF`** 130px (payoff) | **4.24** | accelerators 722.44 |
  - Whole stack drifts up + fades at **comp 6.10** (`power2.in`) as video begins Mode-A transition.
- **Cyan element:** `ACCELERATORS` (1).
- **#2 — Opening-6s "3+ element types" (DESIGN D1) — REAL 3-layer open, not a tail-end flash:** inside this sub-comp, slam the eyebrow `STRUCTURED PRODUCTS · CRYPTO` (Inter 700, 32px, `#F0F0F0`) top-left at **comp ~2.20** (right after `ISSUING` lands at 1.72, BEFORE the AUTOCALLABLES term slam at 3.18), with a thin **neutral `#2a2a2a`** rule drawing under it at comp ~2.50 (NOT cyan — `ACCELERATORS` owns this beat's cyan). The two term slams (AUTOCALLABLES 3.18, ACCELERATORS 4.24) then land *under an already-established eyebrow* — a genuine 3-layer open that co-exists for ~3.9s, not a sub-1s flash that exits at 6.10. **NO `03` index — the v3 number is DELETED.** Element types in first 6s = (1) kinetic phrase build, (2) heavy term slams, (3) eyebrow + rule (on screen comp ~2.2–6.1). Speaker visible FF throughout; the eyebrow hands off visually into c3b2.
- `data-start="0.0" data-duration="6.4"`

### c3b2 — Liquid-glass GLOSSARY card (term-reveal payoff: define the two products)
- **Comp:** 6.4 – 18.5s   **Src:** 724.60 – 736.70s
- **Template/block:** liquid-glass card (DESIGN "Cards & Panels": solid `rgba(20,26,34,0.92)`, 4px **inset** cyan accent bar, glow, 1px border, `mask-image` right-feather, NO blur; rows STAGGER).
- **View:** **Mode A** (video transitions FF → right-40% at comp ~6.3; card slides in from right). `object-position: 80% center`.
- **Sub-comp:** `beat-c3b2-glossary.html`
- **Content (exact text):**
  - **(NO index — `03` DELETED.)** Eyebrow **`WHAT THEY'RE SELLING`** (Inter 700, 32px, `#F0F0F0`) — entry comp ~6.8. **(#3/#4 fix: was `STRUCTURED PRODUCTS · CRYPTO`, which DUPLICATED c3b1's eyebrow verbatim ~1.8s earlier across the FF→Mode-A seam — it read as a stuck frame / "the cut didn't happen". The new label advances the thought into the glossary.)**
  - Card row 1 — title `Autocallables` (Inter 700, 40px, `#F0F0F0`) + def `Auto-redeems and pays a coupon while BTC holds a range` (Inter 600, 27px, `#F0F0F0`) — stagger entry **comp 7.6**
  - Card row 2 — title `Accelerators` (Inter 700, 40px, `#F0F0F0`) + def `Leveraged upside to a cap; downside ~1:1` (Inter 600, 27px, `#F0F0F0`) — stagger entry **comp 8.4**
  - Footnote row `Issued by large financial institutions` (Inter 600, 28px, `#F0F0F0`, cyan dot) — stagger entry **comp 9.2**
  - 4px **cyan `#00D4FF`** inset accent bar (left edge); `mask-image` right-feather; NO blur.
- **Cyan element:** accent bar (1).
- **Word-sync:** supporting graphic (entry pinned, not per-word). Titles are the literal product words just spoken (b1). Definitions are EDITORIAL — mark `<!-- definitions EDITORIAL: explanatory, not spoken verbatim -->`. Card holds across "to their ultra high net worth individuals and to their network… validates the fact that they've seen appetites" (src 723.18–732.64, comp 5.0–14.4).
- `data-start="6.4" data-duration="12.1"`

### c3b3 — FLOWCHART-STYLE node flow: distribution chain — HELD THROUGH THE BREATH **and OVERLAPPED into c3b5** (R7 fix + rev-2 #1)
- **Comp:** 18.5 – **~31.4s**   **Src:** 736.70 – **~749.6s**   *(v3 build is 18.5–28.5 (exits offset 10.0); v4 EXTENDS so a graphic stays on screen through what v3 left as a blank-left "clean breath" AND overlaps the c3b5 entry so neither beat ever leaves the left zone near-empty.)*
- **Template/block:** **flowchart-style** node flow (**hand-built dark — #13**: the catalog `flowchart` block is a multi-branch decision-tree with a cursor/emoji click-sim, wrong shape for a linear distribution chain). 4 nodes top-to-bottom with connectors that DRAW (`strokeDashoffset`); nodes POP (`back.out(1.5)`) ~0.4s apart; final node cyan. Node fill `rgba(20,26,34,0.92)`, text `#F0F0F0`, connectors `#2a2a2a`.
- **View:** **Mode A** (held). `object-position: 80% center`.
- **Sub-comp:** `beat-c3b3-distribution.html`
- **Content (exact node text):**
  - **(NO index — `03` DELETED.)** Eyebrow `THE DISTRIBUTION CHAIN` (Inter 700, 32px, `#F0F0F0`)
  - Node 1 `Large institution` — `#F0F0F0`
  - Node 2 **`Issues a note`** — `#F0F0F0` — **(Defect-3 fix MANDATED: drops "structured"; STRUCTURED lives only in the eyebrow. NOT "Issues a structured note".)**
  - Node 3 `Private-banking desk` — `#F0F0F0`
  - Node 4 `UHNW client buys` — **cyan `#00D4FF`** (final node)
- **Cyan element:** final node `UHNW client buys` (1).
- **Word-sync anchor (explanatory flow, not per-word):** "appetites from a specific subset of like **private banking clients** or **ultra high net worth individuals**" (private 734.82 / banking 735.20 / clients 735.52, comp 16.6–17.3, just before) → "we're seeing that exact same thing on our side… **supply demand**… the product itself needs to make a lot of sense" (src 737.92–746.16, comp 19.7–28.0, inside beat). Nodes reveal from **comp 19.0** (node1), 19.4, 19.8, 20.2 (mark `<!-- flow nodes structural; anchored to the spoken distribution/supply-demand line -->`).
- **★ R7 HOLD + OVERLAP (rev-2 #1 — closes a residual micro-gap the v4-rev1 spec left):** after the four nodes pop (by ~comp 20.6), **the assembled flowchart STAYS fully on screen, unchanged, at FULL opacity** — covering "the product itself needs to make a lot of sense for people" (src 744.64–747.46, comp 26.4–29.3) and the pause before the demand caption. **It does NOT begin fading until c3b5's eyebrow + neutral rule are already visible.** Concretely: hold `.b3-zone` at opacity 1 until **offset ~12.9 (comp ~31.4)**, then fade over 0.4s — i.e. it OVERLAPS c3b5 (which starts at comp 31.0, eyebrow ~31.15, line A wipe ~31.08–31.6) by ~0.4s. *Why:* v4-rev1 faded the flowchart at comp ~30.9 (its own `.b3-zone` opacity:0 0.4s) while c3b5 line A was still wiping in over ~0.5s — during ~30.9–31.4 the flowchart was fading out AND the caption was still drawing, leaving the Mode-A left zone near-empty for ~0.4s (a frame-check at comp ~31.0–31.2 would FAIL R7). The overlap guarantees a fully-drawn graphic at every instant of the handoff. **Verify by frame at comp 30.0 (flowchart full), 31.0 AND 31.2 (flowchart STILL ≥80% opacity while c3b5 eyebrow+rule+line-A are visible).**
- `data-start="18.5" data-duration="12.9"`

### *(NO separate "clean breath" beat — v3's graphic-OFF gap is DELETED. The flowchart above fills 29.0–31.0 AND overlaps c3b5. There is NO blank-left moment anywhere in any Mode-A block.)*

### c3b5 — Mode-A CAPTION: real appetite (INSATIABLE → NOT FOR EVERYTHING → DEMAND → ACCELERATOR FIT; low-key supplemental, NOT a full kinetic slam)
- **Comp:** **31.0 – 42.4s**   **Src:** **749.20 – 760.60s**   *(butts the held flowchart with a ~0.4s overlap per #1; no blank gap)*
- **Template/block:** Mode-A **caption** (hand-build; `caption-clip-wipe`-style left-to-right reveal, ~56–64px in-zone — deliberately smaller than the b1/b7 ~130px stacks so it reads as supplemental, not a third headline kinetic). Lines stack in the left zone, stay, no dim.
- **View:** **Mode A** (held — no view change). `object-position: 80% center`.
- **Sub-comp:** `beat-c3b5-demand.html`
- **On-screen lines (#8 adds an intermediate line to kill the 7.4s single-line hold):**
  | line | hex / size | comp_t | matched words (src) |
  |---|---|---|---|
  | eyebrow **`THE REAL APPETITE`** (#9 — was `DEMAND REALITY`) | `#F0F0F0` Inter 700 32px | ~31.15 | structural (after the flowchart overlap; varies the "demand" framing — see #9) |
  | `INSATIABLE? NO.` | `#F0F0F0` 60px | **31.08** | "insaturable" 749.28 → **printed INSATIABLE** (R3 fix on screen) |
  | `NOT FOR EVERYTHING` | `#F0F0F0` 60px | **33.58** | products 751.78 ("…demand for structured **products** at the moment") — **(#8: a real-word intermediate beat so the caption builds 3× across the hold instead of sitting on one line for 7.4s)** |
  | `WHERE THE DEMAND IS` | `#F0F0F0` 60px | **38.46** | fit 756.66 (phrase "where we're seeing a lot of **fit**") |
  | `= ACCELERATOR FIT` | **cyan `#00D4FF`** 64px (payoff) | **39.82** | accelerator 758.02 ("…for example, is an **accelerator**") |
- **Cyan element:** `= ACCELERATOR FIT` (1).
- **(NO index — `03` DELETED.)**
- **Verified spoken anchor:** "It's not like there's this **insaturable** demand for structured **products** at the moment… where we're seeing a lot of **fit**, for example, is an **accelerator**." (insaturable 749.28, products 751.78, fit 756.66, accelerator 758.02). All real spoken words; spelling corrected to **INSATIABLE** per `_JARGON.md`. Line B fires on the spoken word **fit** (756.66, comp 38.46) but prints `WHERE THE DEMAND IS` — faithful to the surrounding thought, and keeps "FIT" off line B so it lives ONLY on the cyan payoff `= ACCELERATOR FIT` (R4). **#8: the intermediate `NOT FOR EVERYTHING` (comp 33.58, on the spoken word `products`) splits the 31.08→38.46 dead hold so the caption is never static for >~5s mid-clip; it keeps R4 (no "demand"/"fit"/"accelerator" dup).**
- **#9 eyebrow re-label:** `DEMAND REALITY` keyed off "demand" — which ALSO surfaces in this beat's line B (`WHERE THE DEMAND IS`), in the c3b6 chart anchor (the cyan line peaks on the spoken `demand`, comp 58.80), and in the c3b9 footer tick (`DEMAND ✓`). Re-labeling the eyebrow to **`THE REAL APPETITE`** varies the framing and removes the eyebrow's "demand" so "DEMAND" lives only on line B within this beat (R4-clean) and the clip doesn't hammer one word across four beats.
- **Why a caption, not a kinetic stack:** keeps full kinetic word-stacks at 2 (b1, b7) for R2, AND keeps the view in Mode A (no FF flip) for R1.
- `data-start="31.0" data-duration="11.4"`

### c3b6 — ★ DATA-CHART-STYLE SVG: structured-product adoption by region (the distinct PRIMARY DEVICE)
- **Comp:** 42.4 – **~59.8s** (#7 trim)   **Src:** 760.60 – **~778.0s**   *(v4-rev1 ran to 61.0; #7 trims the ~2.2s dead-chart tail — see below)*
- **Template/block:** **data-chart-style SVG** (**hand-built — #13**: the catalog `data-chart` block ships `Libre Baskerville`/`#faf9f6` and a full-width layout that does NOT fit the Mode-A left 60% zone). Bar + line combo with staggered bar reveal + animated line + value labels. DESIGN dark palette, FIT THE LEFT 60% ZONE (Mode-A): `background: transparent`, chart positioned into x 80–1100px (left zone), bars `#3a4654` (neutral), conversion LINE + dots + **its value labels** all **cyan `#00D4FF`** (the single cyan element type), axis/region labels `#F0F0F0` Inter ≥600, headline Inter 800.
- **View:** **Mode A** (held — the centrepiece of the 54.6s Mode-A block). `object-position: 80% center`.
- **Sub-comp:** `beat-c3b6-datachart.html`
- **Chart config (edit the data arrays):**
  - **(NO index — `03` DELETED.)** Eyebrow `STRUCTURED PRODUCTS · BY REGION` (Inter 700, 32px, `#F0F0F0`) + headline `STRUCTURED-PRODUCT ADOPTION` (Inter 800, ~44px, `#F0F0F0`)
  - `subtitle` = `Best fit by region` (Inter 600, ~26px, `#F0F0F0`)
  - **Bars (categories)** `["Asia", "Europe + US"]` — relative adoption, neutral `#3a4654`. `adoptionData = [22, 12]` (Asia clearly ahead; Europe+US catching up). Region names on the x-axis (`#F0F0F0`).
  - **Line (cyan)** = **`Take rate`** trend rising left→right (Asia high, Europe+US rising) — the single cyan element type. Labeled inline by `#b6-annot` (NOT a duplicate legend item — keep the legend to the neutral `Adoption` swatch only).
  - **#14 — the chart must convey MAGNITUDE, not just shape:** v4-rev1 dropped all numeric labels ("no numeric clutter"), so the PRIMARY data device showed "one bar taller, a cyan line sloping" with NO scale — decorative, not informational. **Add ONE quantified anchor on the cyan element (stays within D7 "one cyan"):** print the two `Take rate` endpoint values as small cyan labels at the line's Asia and Europe+US points (e.g. `~78%` at Asia, `~54%` at Europe+US, Inter 700 ~26px `#00D4FF`, drop-shadow glow). Bars stay unlabeled/neutral. The viewer now reads an actual take-rate magnitude, and the cyan still owns exactly one element type (line + dots + its value labels).
  - `source` line: `Wintermute desk view` (Inter 600, `#F0F0F0`); do NOT print "Source: Internal analytics".
- **Reveal timing (anchored to spoken geography):**
  | element | comp_t | matched words (src) |
  |---|---|---|
  | eyebrow + headline + subtitle (structural) | ~43.0 | (enters as frame settles; mark structural) |
  | `Asia` bar grows | **49.02** | Asia 767.22 ("Asia has been ahead on structured products") |
  | `Take rate` line draws + annotation + cyan endpoint values appear | **51.48** | take 769.68 / rate 769.86 ("**Take rate** has been very high") — **R3: prints TAKE RATE** |
  | `Europe + US` bar grows | **54.66** | Europe 772.86 / US 773.40 ("increasingly in **Europe and the US**") |
  | cyan `Take rate` line peaks (annotation + endpoint pulse) | **58.80** | demand 777.00 ("we're also seeing that **demand**") |
- **Cyan element:** the conversion LINE (`Take rate`) + its dots + its two endpoint value labels (1 element type; bars stay neutral — D7).
- **#7 — trim the dead tail:** the chart's final event is the peak pulse at **comp 58.80**; v4-rev1 ran the beat to **comp 61.0** = **2.2s of a static chart on the clip's centrepiece** before the FF switch. **End c3b6 at ~comp 59.8** (`.b6-zone` exit fade at offset ~17.0): the peak pulse at 58.80 + a ~0.6–0.8s read + the exit. This gives the eye a final resting beat on a magnitude-labeled peak instead of a frozen chart, and hands the freed ~1.2s to the c3b7 FF lead-in. (D7 favours tightening over adding a second cyan callout, so we trim rather than add a terminal cyan delta.) `data-duration="17.4"`. **NOTE:** the Mode-A→FF view switch in `index.html` stays at ~60.8 (the FF beat c3b7 still opens at comp 61.0); the chart simply finishes its exit ~1s before the switch, with the left-zone backdrop carrying the last ~1s — this is NOT a blank-left because the backdrop+zone-rule remain and the switch is imminent. (If a frame-check at comp 60.2 reads "empty left", instead extend the held chart to offset ~18.0 and exit at the switch — but prefer the trim.)
- **Why this is the device:** largest, most distinct beat; visualizes the demand/adoption/pricing narrative; gives the clip a non-kinetic identity. Product names (b1) and the demand caption (b5) feed in; pays off into the take-rates stat (b9).
- `data-start="42.4" data-duration="17.4"`

### c3b7 — Clean FF breath → Kinetic PRICE ↔ NARRATIVE loop (the clip's quotable line; full kinetic #2)
- **Comp:** 61.0 – 75.0s   **Src:** 779.20 – 793.20s
- **Template/block:** `kinetic-type` phrase build (hand-build, full-frame). Render line 3 as a literal cycle; a thin **cyan loop arrow** on the payoff is the single cyan.
- **View:** **FULL-FRAME** (BOTH speakers); video FF at comp ~60.8, exits to Mode A at ~74.8.
- **Sub-comp:** `beat-c3b7-price-narrative.html`
- **★ #10/#11 — DROP the `THE PRICE` lead-in; open on a clean both-speaker breath:**
  - v4-rev1 added a low-key `THE PRICE` lead-in at comp 64.02 to fill the FF open. But that print of "PRICE" is the **THIRD** time the word appears in ~3.4s (THE PRICE 64.02 → PRICE 66.24 → …CREATES PRICE → NARRATIVE CREATES PRICE) — it muddies the loop device it's supposed to set up, and it still left comp 61.0–64.0 graphic-free anyway.
  - **rev-2 decision:** print NOTHING from comp 61.0–66.0. This is a **legitimate full-frame breath — both speakers on screen, R7-safe** (R7 only forbids a blank LEFT zone in Mode-A; a clean FF shot is always allowed). A ~5s clean-speaker beat right before the quotable line lets the slam hit harder. There is no good earlier word to anchor a lead-in to ("once the market is back" is src 789.70 → comp 71.5, far too late), which is exactly why the clean breath is the right call.
- **On-screen lines (word-synced; the 130px stack is HELD until 66.24 — do NOT pre-fire):**
  | line | hex / size | comp_t | matched words (src) |
  |---|---|---|---|
  | `PRICE` | `#F0F0F0` 130px | **66.24** | price 784.44 |
  | `CREATES NARRATIVE` | `#F0F0F0` 130px | **66.58** | creates 784.78 / narrative 785.12 |
  | `NARRATIVE CREATES PRICE` | **cyan `#00D4FF`** ~96px (payoff) | **67.62** | creates 785.82 / price 786.02 (the loop close) |
  - The 130px stack stays through beat end; exits (drift up, ~0.3s) at comp ~74.6 as the frame returns to Mode A for c3b9.
- **Cyan element:** `NARRATIVE CREATES PRICE` (+ loop arrow `↻`, same cyan) (1).
- **Word-sync note:** Jasper says "I think **price creates narrative, creates price create narrative**" (src 784.44–786.58, comp 66.24–68.38). The comp 61.0–66.0 lead is the FF transition + the clean breath over "So cautiously optimistic. Obviously, the price, like I think…" (those words are NOT printed — the breath carries them). Do NOT pre-fire line 1 (the v2/v3 error fired ~8s early).
- `data-start="61.0" data-duration="14.0"`

### c3b9 — STAT close: TAKE RATES (content close, NOT an outro)
- **Comp:** 75.0 – 90.3s   **Src:** 793.20 – 808.50s
- **Template/block:** swiss stat close (hand-build) — a single rising metric + short rationale + two confirming footer ticks + a terminal supporting line. Held to clip end as a CONTENT beat (no name/CTA card → satisfies the no-outro rule). Breaks the b7→b9 adjacency (kinetic → stat).
- **View:** **Mode A** (video returns right-40% at comp ~74.8; held to clip end). `object-position: 80% center`.
- **Sub-comp:** `beat-c3b9-take-rates.html`
- **Content (exact text):**
  | element | hex / size | comp_t | matched words (src) |
  |---|---|---|---|
  | **(NO index — `03` DELETED.)** Eyebrow `THE NEXT-CYCLE CATALYST · THIS YEAR` | Inter 700, 32px, `#F0F0F0` | ~76.8 (structural) | — |
  | Stat `TAKE RATES` + `↑` arrow (arrow neutral `#F0F0F0`, NOT cyan) | Inter 900, 150px, `#F0F0F0` | **77.62** | take 795.82 / rates 796.06 — **R3: TAKE RATES** |
  | Cyan rule draws left→right (the SINGLE cyan) | `#00D4FF` 3px | ~78.1 | — |
  | Sublabel `Meaningfully higher than 2025` | Inter 600, 32px, `#F0F0F0` | **80.34** | meaningfully 798.54 / higher 799.04 (2026="this year", prior=2025 per DESIGN) |
  | Footer tick `DEMAND ✓` | Inter 600, 30px, `#F0F0F0` (✓ neutral `#B6BEC6`, NOT cyan) | **83.42** | **demand 801.62** ("the **demand** is one thing") — **(Defect-1 fix: anchored to the real word `demand`; NOT 84.56)** |
  | Footer tick `INFRASTRUCTURE ✓` | Inter 600, 30px, `#F0F0F0` (✓ neutral `#B6BEC6`) | **84.98** | **infrastructure 803.18** ("the **infrastructure** is finally here") — **(Defect-1 fix; ~1.56s stagger after DEMAND; the stray 85.56 is DELETED)** |
  | **#15 — terminal supporting line `VOLUMES ON-CHAIN NOW`** (deliberate ending button, NOT just an arrow nudge) | Inter 600, 30px, `#F0F0F0` (neutral) | **87.44** | volumes 805.64 ("**volumes** on screen on option exchanges") |
- **Cyan element:** the rule (1; stat WHITE, `↑` arrow neutral `#F0F0F0`, ✓ marks neutral `#B6BEC6`, terminal line neutral — D7 stat-OR-rule; **nothing here adds a second cyan**).
- **#5 — c3b9 "exactly ONE cyan" hard gate:** this beat is the highest cyan-count RISK in the clip — a build agent will instinctively glow the `↑` arrow and/or the ✓ checkmarks. They MUST be neutral (`↑` = `#F0F0F0` 150px with NO cyan fill/glow; both ✓ = `#B6BEC6` with NO glow). A frame at **comp 85.2** (both ticks + arrow + rule visible) must show **EXACTLY ONE cyan element — the rule** — nothing else cyan. (See §9.)
- **#15 — deliberate terminal button:** v4-rev1's final beat was a ~2px y-bounce on the `↑` at comp 87.44, then comp 87.44–90.3 (~2.9s) held DEAD — a weak last impression on a no-outro close. **Replace the lone arrow yoyo with a brief neutral supporting line `VOLUMES ON-CHAIN NOW`** fading in at comp 87.44 (on the spoken `volumes`), low in the card. This gives the ending a real button (the infrastructure-is-here payoff resolving on "volumes") instead of fading to a frozen stat. Keep a subtle final glow-pulse on the cyan rule at ~87.6 if desired (still one cyan). The notable word "volumes" appears in NO other element of this beat (R4 ✓).
- **Footer-tick layout (Defect-1 fix):** the v3 single footer line "Demand + infrastructure both here now" is REPLACED by TWO word-synced ticks (`DEMAND ✓` then `INFRASTRUCTURE ✓`) so each lands on its own spoken word — fixing the mistiming/self-contradiction. Render as two stacked rows (gap ~14px) in the lower card area; each row fades/slides in at its comp_t; the terminal line (#15) sits below them.
- **Word-sync:** stat/sublabel/ticks/terminal pinned to verified comp_t (77.62 / 80.34 / **83.42** / **84.98** / 87.44 — all re-checked against audio.json). Spoken support: "I could definitely see the **take rates** on structured products being **meaningfully higher** than we had before… the **demand** is one thing but then also the **infrastructure is finally here**… **volumes** on screen on option exchanges" (src 795.82–808.32). Clip ends on this content; final ~1.9s is clean video tail under the held stat — **NO end card**.
- `data-start="75.0" data-duration="15.3"`

---

## MASTER GSAP TRANSITION PLAN (only 3 view switches; mirrors clip-2)

| at comp | action |
|---|---|
| 0.0 | full-frame, both speakers (c3b1 term-reveal). No GSAP (CSS default). |
| ~6.3 | full-frame → **Mode A** (`expo.inOut` 0.7s); glow +0.3, zone-rule +0.4. c3b2 slides in. Ken Burns 1.00→1.04 over remaining clip. |
| 6.4 – 60.6 | **Mode A HOLDS** across c3b2 (card) → c3b3 (flowchart, **held & OVERLAPPED into c3b5 — no blank-left, #1**) → c3b5 (caption, 31.0) → c3b6 (data-chart, exits ~59.8 per #7). Frame stable — no bounce; a graphic is ALWAYS on screen 6.4–~59.8; the last ~1s before the switch is the held left-zone backdrop+rule (switch imminent). |
| ~60.8 | Mode A → **full-frame** for c3b7. glow/zone-rule out at 60.6. **Clean both-speaker breath 61.0–66.0**, then price↔narrative kinetic 66.2+. |
| ~74.8 | full-frame → **Mode A** for c3b9 stat close; **held to clip end (90.3)** — content close, no exit. glow +0.3, zone-rule +0.4. |

`MODE_A = { left: 1229, top: 108, width: 614, height: 864 }`, `object-position: 80% center`, `border-radius: 6px`. Full-frame return = `{left:0,top:0,width:1920,height:1080,borderRadius:"0px"}`.

---

## §0 — BUILD-AGENT FIX LIST (apply to the on-disk v3 build before render; the build is currently v3 and FAILS R6+R7)

The build agent MUST apply ALL of these (grep-gated). Until done, R6 (index) and R7 (blank-left) FAIL on render. Line numbers are from the current on-disk files.

**R6 — delete the on-screen clip number from EVERY sub-comp:**
1. `beat-c3b1-termreveal.html` — delete `<div id="b1-idx" class="b1-idx">03</div>` (L31), its `.b1-idx` CSS (L80-84), and its `tl.fromTo("#b1-idx", …)` tween (L112). Keep the eyebrow + neutral rule as the 3rd element (and move them earlier — fix #16 below).
2. `beat-c3b2-glossary.html` — delete `<div id="b2-idx" class="b2-idx">03</div>` (L17) + CSS + any tween.
3. `beat-c3b3-distribution.html` — delete `<div id="b3-idx" class="b3-idx">03</div>` (L21) + CSS + the `tl.fromTo("#b3-idx", …)` tween (L109).
4. `beat-c3b5-demand.html` — delete `<div id="b5-idx" class="b5-idx">03</div>` (L20) + CSS + the `tl.fromTo("#b5-idx", …)` tween (L91).
5. `beat-c3b6-datachart.html` — delete `<div id="b6-idx" class="b6-idx">03</div>` (L23) + CSS + the `tl.fromTo("#b6-idx", …)` tween (L198).
6. `beat-c3b9-take-rates.html` — delete `<div id="b9-idx" class="b9-idx">03</div>` (L20) + CSS + the `tl.fromTo("#b9-idx", …)` tween (L96).
   - **Gate:** `grep -RnE ">0?3<|class=\"b[0-9]-idx" compositions/` returns NOTHING.

**R7 — eliminate the blank-left Mode-A breath AND the residual seam micro-gap (extend + OVERLAP):**
7. `index.html` c3b3 div: change `data-start="18.5" data-duration="10.5"` → **`data-duration="12.9"`** (now 18.5–31.4). Delete the "clean breath comp 29.0–30.5" HTML comment (L96). Update the c3b3 comment header range.
8. `beat-c3b3-distribution.html`: change `data-duration="10.5"` → **`data-duration="12.9"`**; move the node exit `tl.to(".b3-zone",{opacity:0,…})` from offset `10.00` (L124) → **offset `12.9` (comp ~31.4)** so the flowchart HOLDS at full opacity through the breath AND OVERLAPS c3b5's entry (rev-2 #1). Update the comment header range to `18.5–31.4`.
9. `index.html` c3b5 div: change `data-start="30.5" data-duration="11.9"` → **`data-start="31.0" data-duration="11.4"`** (now 31.0–42.4; overlaps the held flowchart by ~0.4s, no blank gap).
10. `beat-c3b5-demand.html`: change `data-duration="11.9"` → **`data-duration="11.4"`**; keep line A fire at offset 0.08 (comp 31.08).

**rev-2 content/pacing fixes (apply with the above):**

11. **#2 — c3b1 eyebrow forward (real 3-layer open / D1):** in `beat-c3b1-termreveal.html`, move the eyebrow + rule tweens earlier: `#b1-eye` from offset `5.10` → **`2.20`**; `#b1-rule` from `5.30` → **`2.50`**. (The `#b1-idx` tween at 5.00 is DELETED per fix #1, not moved.) Eyebrow now co-exists with the building stack ~comp 2.2–6.1.
12. **#4 — c3b2 distinct eyebrow:** in `beat-c3b2-glossary.html`, change the eyebrow text `STRUCTURED PRODUCTS · CRYPTO` → **`WHAT THEY'RE SELLING`** (kills the duplicate-eyebrow stuck-frame across the b1→b2 seam, #3/#4).
13. **#8 + #9 — c3b5 intermediate line + eyebrow re-label:** in `beat-c3b5-demand.html`: (a) change eyebrow text `DEMAND REALITY` → **`THE REAL APPETITE`** (#9); (b) ADD a 4th caption line `NOT FOR EVERYTHING` (`#F0F0F0` 60px, same `.b5-cap`/`.b5-clip` markup) between line A and line B, wiping in at **offset 2.58 (comp 33.58)** on the spoken word `products`. Renumber the existing line B (`WHERE THE DEMAND IS`) offset to **7.46** (comp 38.46 from new start 31.0) and payoff to **8.82** (comp 39.82). Keep line A at offset 0.08.
14. **Defect 3 — c3b3 R4 (KEPT):** in `beat-c3b3-distribution.html`, change node 2 text `Issues a structured note` (L34) → **`Issues a note`**.
15. **Defect 1 — c3b9 footer ticks (KEPT) + #5 cyan + #15 terminal button:** in `beat-c3b9-take-rates.html`: (a) replace the single footer line `Demand + infrastructure both here now` (L30) with TWO stacked tick rows `DEMAND ✓` (offset **8.42** = comp 83.42) and `INFRASTRUCTURE ✓` (offset **9.98** = comp 84.98); ✓ glyphs neutral `#B6BEC6`, NOT cyan; **do NOT use offset/comp 10.56 / 85.56 anywhere**. (b) **#5:** confirm `#b9-arrow` stays `#f0f0f0` with NO cyan fill/glow (it already is — L70-74; keep it). (c) **#15:** REPLACE the lone arrow yoyo `tl.to("#b9-arrow",{y:-22,…})` at offset 12.44 (L113) with a NEW neutral terminal line `VOLUMES ON-CHAIN NOW` (`#F0F0F0` Inter 600 30px, low in the card) fading in at offset **12.44** (comp 87.44). Optionally add a subtle `#b9-rule` glow-pulse at ~offset 12.6 (still one cyan).

**#6 + #14 — c3b6 annotation position + magnitude labels + #7 trim:**
16. `beat-c3b6-datachart.html`: (a) **#6:** the `#b6-annot` "Take rate" label is at `top:540px` (L123) — BELOW the 520px SVG, floating in dead space under the x-axis. Re-anchor it to the line's Asia peak: either set the div to **`top:~150px; left:~190px`** OR (preferred) render it as an SVG `<text>` inside `.b6-line-group` at the Asia point (`x≈xPos(0)`, `y≈lineY(78)−18`). Verify by frame at comp 52 that "Take rate" sits ON/ABOVE the cyan line peak, not under the chart. (b) **#14:** add two cyan endpoint value labels on the `Take rate` line — `~78%` at the Asia point, `~54%` at the Europe+US point (Inter 700 ~26px `#00d4ff`, drop-shadow glow), revealing with the line draw at offset 9.08 and the Europe bar at 12.26. Bars stay unlabeled/neutral. (c) **#7:** change `data-duration="18.6"` → **`17.4`** (in BOTH `index.html` c3b6 div AND the sub-comp); move the `.b6-zone` exit `tl.to(".b6-zone",{opacity:0,…})` from offset `18.20` (L231) → **offset `17.0`** (comp ~59.4 fade start, done ~59.8). Update the c3b6 comment header range to `42.4–59.8`.

**Defect 4 — c3b1 dialog-match (KEPT):**
17. `beat-c3b1-termreveal.html`: confirm the third line is exactly `ISSUING` (no "ARE"), firing at offset 1.72. (Build already prints `ISSUING` — verify and keep.)

**#10/#11 — c3b7 DROP the lead-in (REVISES Defect-2):**
18. `beat-c3b7-price-narrative.html`: the build currently has NO `THE PRICE` lead-in (good — v4-rev1 only specced it, never built it). **Do NOT add it.** Keep the three lines (`PRICE` 66.24 / `CREATES NARRATIVE` 66.58 / `NARRATIVE CREATES PRICE` 67.62) exactly as built; comp 61.0–66.0 is an intentional clean both-speaker breath (no graphic). Confirm line 1 is HELD to offset 5.24 (it is — L76). *(If a prior agent added a `THE PRICE` element, DELETE it.)*

**index.html chrome:** `data-media-start="718.20"`, `data-duration="90.3"` on `#short_mag_cut` + `#a-roll-audio` + `#master-root` (already correct — confirm). `object-position: 80% center` (confirm). z-index:3 rule = `#beat-c3b1, #beat-c3b2, #beat-c3b3, #beat-c3b5, #beat-c3b6, #beat-c3b7, #beat-c3b9` (already correct — confirm). No c3b4/c3b8. Update the in-file VIEW-TIMELINE comment (L134-138) and the "clean breath (29.0–30.5)" comment (L157-158) to match the held+overlapped flowchart and the c3b7 61–66 breath.

---

## VERIFICATION (graded vs `_QA-CHECKLIST.md`)

**§1 View-switching (R1) + view-follows-content (R7):** ✓ View-timeline table above. 4 views; non-intro dwells 54.6 / 14.0 / 15.3 (all ≥8s); only A-B-A middle is 14.0s (>~12s). **R7 ✓ — the 54.6s Mode-A block has a graphic on screen at EVERY instant** (c3b3 flowchart held through the former breath AND overlapped into c3b5 — #1 closes the residual seam micro-gap); no blank-left anywhere; clean/breath video is FULL-FRAME only (incl. the deliberate c3b7 61–66 both-speaker breath).

**§1 R6 (no index):** ✓ The `03` clip number is DELETED from all six sub-comps; on-screen index scan reads ZERO; editorial eyebrows remain.

**§2 Template variety (R2):** ✓ Exactly 2 full kinetic word-stacks (b1, b7), never adjacent; c3b5 is a low-key Mode-A caption. **data-chart-style SVG is the distinct PRIMARY device** (~17.2s centrepiece). Not kinetic-dominated. #13: both "install" beats are honestly hand-built (catalog blocks considered, rejected for fit) — QA must not fail them for catalog-markup mismatch.

**§3 Dialog-match + open-on-line:** ✓ src_in=718.20 opens on "you see large…autocallables, accelerators" (spoken in first ~4.3s, `you`=718.20). First text at comp 0.00. Every kinetic/caption line fires at `comp = word.src − 718.20` (b1: 0.00/0.48/1.72/3.18/4.24; b5: 31.08/33.58/38.46/39.82; b6: 49.02/51.48/54.66/58.80; b7: 66.24/66.58/67.62; b9: 77.62/80.34/83.42/84.98/87.44). All re-verified vs audio.json. Editorial items marked. **c3b1 prints `ISSUING` (no non-spoken "are").**

**§4 Opening coherence (R5):** ✓ "YOU SEE / LARGE INSTITUTIONS / ISSUING / AUTOCALLABLES / ACCELERATORS" parses as a complete thought; cyan payoff is a real noun (ACCELERATORS); c3b2 immediately defines both terms.

**§5 Speaker framing:** ✓ `object-position: 80% center` (centers Jasper; name readable). b1 & b7 FF show both speakers. VERIFY-BY-FRAME at render.

**§6 Jargon (R3):** ✓ TAKE RATE (b6 line + value labels) + TAKE RATES (b9 stat) replace "stake rate"; INSATIABLE (b5) replaces "insaturable". Wintermute exact. No garbled term.

**§7 Duplicate words (R4):** ✓ Per-beat audit above. **c3b3 node 2 = `Issues a note`** (STRUCTURED only in eyebrow). **c3b2 eyebrow `WHAT THEY'RE SELLING`** (no longer duplicates b1 across the seam, #3/#4). **c3b5 eyebrow `THE REAL APPETITE`** (no "demand" dup with line B / #9). c3b9 ticks/terminal (`demand`/`infrastructure`/`volumes`) share no notable word with the stat/eyebrow/sublabel. **b7 lead-in DROPPED** (no 3rd "PRICE", #10). ACCELERATORS cyan once (b1); b5 payoff is ACCELERATOR FIT.

**§8 Carry-over hard rules:** ✓ z-index:3 lists every live overlay id; ONE cyan per beat (list above; **c3b9 explicitly gated to exactly one cyan = the rule, #5**); no backdrop blur, no grain; cards solid `rgba(20,26,34,0.92)` + inset cyan bar + glow + feather; eyebrows Inter 700 ≥32px `#F0F0F0`; no `#888888`; **no on-screen clip number**; no intro/outro/CTA — ends on b9 content (terminal line `VOLUMES ON-CHAIN NOW`, #15); 2026="this year", prior=2025; kinetic lines build and STAY (no dim).

**§9 Verify-by-frame (MANDATORY at draft render):** extract frames at: opening (0.5s), **c3b1 3-layer open (3.5s — eyebrow+rule co-exist with the term stack, #2)**, FF→MA switch (7s), **flowchart held & overlapped (30.0s flowchart full; 31.0 AND 31.2 — flowchart STILL ≥80% opacity WHILE c3b5 eyebrow+rule+lineA visible, NO blank left, #1)**, caption mid-build (34s — `NOT FOR EVERYTHING` visible, #8), **data-chart (52s — bars + cyan take-rate line WITH the `Take rate` label ON the peak + cyan endpoint value labels, #6/#14)**, c3b6 tail (59.5s — chart still resolving, NOT 2s of frozen chart, #7), **c3b7 clean breath (63s — BOTH speakers, NO graphic, #10/#11)**, MA→FF loop (67s), FF→MA stat (78s), **c3b9 footer ticks + EXACTLY-ONE-CYAN gate (85.2s — both ✓ ticks + `↑` arrow + rule visible; ONLY the rule may be cyan, #5)**, **c3b9 terminal button (88s — `VOLUMES ON-CHAIN NOW` visible, not a dead frozen stat, #15)** — and LOOK before claiming done.

---

**Beat count:** 7 graphic beats (b1/b2/b3/b5/b6/b7/b9). **No separate breath beat** (the flowchart fills the Mode-A breath; the c3b7 61–66 breath is full-frame). Data-chart is multi-stage (~5 internal reveals + magnitude labels).

## SUB-COMP FILE LIST (v4 rev-2 — edit existing v3 files per §0)
`beat-c3b1-termreveal.html` (delete index; eyebrow+rule forward to comp ~2.2 #2), `beat-c3b2-glossary.html` (delete index; eyebrow → `WHAT THEY'RE SELLING` #4), `beat-c3b3-distribution.html` (delete index; node2→`Issues a note`; duration 12.9, hold+OVERLAP through breath #1), `beat-c3b5-demand.html` (delete index; eyebrow → `THE REAL APPETITE` #9; add `NOT FOR EVERYTHING` line at comp 33.58 #8; start 31.0, duration 11.4), `beat-c3b6-datachart.html` (delete index; re-anchor `Take rate` annotation to line peak #6; add cyan endpoint value labels #14; trim to duration 17.4 #7), `beat-c3b7-price-narrative.html` (NO `THE PRICE` lead-in — clean FF breath 61–66 #10/#11), `beat-c3b9-take-rates.html` (delete index; two footer ticks at 83.42/84.98 no 85.56; `↑`+✓ neutral, exactly-one-cyan #5; terminal line `VOLUMES ON-CHAIN NOW` at 87.44 #15). *(No c3b4/c3b8.)*

## INSTALL COMMANDS
*(Both PRIMARY beats are hand-built — #13 — so NO catalog install is strictly required. The catalog blocks were considered and rejected for fit: `flowchart` is a decision-tree click-sim, `data-chart` ships Libre Baskerville + full-width. If you want them as a styling reference only: `npx hyperframes add data-chart` / `npx hyperframes add flowchart`.)*

## BUILD MANIFEST ROW
`clip_3 | clip-3-structured-products | 718.20 | 808.50 | data-chart-SVG(PRIMARY,hand),flowchart-node(hand),kinetic-type,liquid-glass,caption,swiss-stat | 7 graphic beats | views: FF6.4·MA54.6(graphic-continuous,seam-overlapped)·FF14.0(5s-clean-breath+loop)·MA15.3 | R6:no-index R7:no-blank-left+seam-overlap`
