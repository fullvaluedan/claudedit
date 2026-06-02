# Clip 3 — FINAL BUILD-READY EDL

**Clip:** `clip-3-structured-products`
**Source window:** 700s – 810s | **Duration:** 110s | **comp_t = src_t − 700**
**Theme:** TradFi structured products (autocallables / accelerators) entering crypto via private-banking distribution to UHNW clients; the price ↔ narrative feedback loop and rising take-rates as the next-cycle catalyst.

**Speaker layout:** side-by-side / both-speakers source. Per D1 the opening is FULL-FRAME (both speakers) with the kinetic hook over a left dark-gradient backdrop; video animates to **Mode A** at t=3.0.

**Mode A (binding, per D1):** video framed RIGHT 40%, ~85% scale. Implementation copies `clip-2-altcoin-options/index.html` exactly:
`MODE_A = { left: 1229, top: 108, width: 614, height: 864 }`, `object-position: 83% center`, `border-radius: 6px`; glow `#bg-glow` fades in at +0.3s, `#zone-rule` draws at +0.4s. Full-frame return = `{ left:0, top:0, width:1920, height:1080, borderRadius:"0px" }` (`expo.inOut`, 0.4s) — used for every full-frame kinetic beat.

**Palette / type (D7):** bg `#0a0a0a`; primary text `#F0F0F0`; ONE cyan `#00D4FF` element per beat; cards `rgba(20,26,34,0.92)` solid + 4px cyan accent bar + soft glow + 1px border + `mask-image` feather — **NO backdrop-filter blur, NO grain**. Eyebrow Inter 700 ≥32px `#F0F0F0`; body/bullets Inter ≥600. Any small/label text `#F0F0F0` (never `#888888` under 48px). Date framing: 2026 = "this year".

**Beat count:** 10 (D-table range for clip 3 = 9–10). ✓
**No-outro (D4):** clip ends on a content kinetic (c3b10), not a name card. No intro card, no CTA. ✓
**Hook (D5):** clip 3 hook is STRONG — KEPT as written (D5 replaces hooks for clips 1/5/7 only).

---

## OPENING HOOK — EDITORIAL (D1 / D2: NOT word-synced)

`<!-- EDITORIAL: anticipatory hook, not word-synced. Fires before Jasper reaches the line (he says "autocallables" at comp 21.38). -->`

- **Line 1** "AUTOCALLABLES" — fires comp **t=0.08** — white `#F0F0F0`, Inter 900, 130px
- **Line 2** "IN CRYPTO" — fires comp **t=0.88** — white `#F0F0F0`, 130px
- **Line 3** "NOW." — fires comp **t=1.60** — cyan `#00D4FF`, 130px (single cyan element)
- Whole stack drifts up + fades out at comp **2.8** (`power2.in`).

Source justification: spoken line "...large financial institutions issuing stuff like **autocallables, accelerators**" (autocallables @ comp 21.38). Strongest single-word punch in the window; lands as a confirmation when Jasper reaches it.

---

## BEAT MAP

Legend — every beat lists: comp range · src range · FINAL template · speaker mode · sub-comp file · full content (exact hex) · per-line fire comp_t (verified from `clip3-words.txt`, or `EDITORIAL`).

---

### c3b1 — Opening kinetic hook
- **Comp:** 0.0 – 3.0s   **Src:** 700.0 – 703.0s
- **Template:** kinetic-type (hook)
- **Mode:** full-frame (both speakers)
- **Sub-comp:** `beat-c3b1-hook.html`
- **Content / lines:**
  - "AUTOCALLABLES" — `#F0F0F0` 130px — **comp 0.08** — `EDITORIAL`
  - "IN CRYPTO" — `#F0F0F0` 130px — **comp 0.88** — `EDITORIAL`
  - "NOW." — **cyan `#00D4FF`** 130px — **comp 1.60** — `EDITORIAL`
  - Stack exits (drift up + fade) at comp 2.8.
- **Cyan element:** "NOW." (1).
- `data-start="0.0" data-duration="3.0"`

### c3b2 — Swiss-grid launch (index / eyebrow / stat)
- **Comp:** 3.0 – 16.0s   **Src:** 703.0 – 716.0s
- **Template:** swiss-grid
- **Mode:** Mode A (video shrinks to right 40% at t=3.0; glow @3.3, rule @3.4)
- **Sub-comp:** `beat-c3b2-swiss-launch.html`
- **Content (exact text):**
  - Index "03" + eyebrow "STRUCTURED PRODUCTS · CRYPTO" — Inter 700, 34px, `#F0F0F0` — slam in @ comp 3.0
  - Cyan horizontal rule draws left→right @ comp 3.4 — **cyan `#00D4FF`** (this is the beat's single cyan; the stat below is WHITE per D7 "stat OR rule, not both")
  - Stat "UHNW" — Inter 900, 140px, `#F0F0F0` — @ comp 3.8
  - Sublabel "Ultra-high-net-worth clients · via private banking" — Inter 600, 30px, `#F0F0F0` — @ comp 4.6
  - Tag row "TRADFI DISTRIBUTION CHANNEL" — Inter 700, 30px, `#F0F0F0` — @ comp 5.2
- **Cyan element:** the rule (1). Stat is white (rule carries cyan).
- **Opening "3+ element types before 6s" (D1):** kinetic hook (type 1, c3b1) + index/eyebrow (type 2) + rule draw (type 3) + stat (type 4) all before comp 6. ✓
- `data-start="3.0" data-duration="13.0"`

### c3b3 — Kinetic: product names → channel
- **Comp:** 16.0 – 26.0s   **Src:** 716.0 – 726.0s
- **Template:** kinetic-type
- **Mode:** full-frame (both speakers) — video returns full-frame ~15.8, exits ~25.8
- **Sub-comp:** `beat-c3b3-products-kinetic.html`
- **Content / lines (word-synced, verified — all three fires sit inside the 16–26 window):**
  - "AUTOCALLABLES" — `#F0F0F0` 130px — **comp 21.38** (src 721.38 "autocallables")
  - "ACCELERATORS" — `#F0F0F0` 130px — **comp 22.44** (src 722.44 "accelerators")
  - "TO UHNW INDIVIDUALS" — **cyan `#00D4FF`** 130px — **comp 25.70** (src 725.70 "individuals")
  - Stack stays (no dim) through beat end.
- **Cyan element:** "TO UHNW INDIVIDUALS" (1).
- **Payoff choice:** "via private banking" recurs at comp 34.82 (outside this beat); to keep all fires inside 16–26 the payoff uses the verified "individuals" word @ comp 25.70. The "private banking" distribution point is carried by the c3b4 card.
- `data-start="16.0" data-duration="10.0"`

### c3b4 — Liquid-glass card: product taxonomy (D3: builder's call → LIQUID-GLASS, rows stagger)
- **Comp:** 26.0 – 43.0s   **Src:** 726.0 – 743.0s
- **Template:** liquid-glass card  *(D3 c3b4: keep liquid-glass OR swiss-grid — chosen liquid-glass for template variety + name-drop fit; rows MUST stagger)*
- **Mode:** Mode A (card slides in from right; video already Mode A)
- **Sub-comp:** `beat-c3b4-product-card.html`
- **Content (exact text, staggered rows):**
  - Eyebrow "STRUCTURED PRODUCTS IN CRYPTO" — Inter 700, 32px, `#F0F0F0`
  - Row 1 "Autocallables" — Inter 600, 40px, `#F0F0F0` — stagger offset +0.5s
  - Row 2 "Accelerators" — Inter 600, 40px, `#F0F0F0` — offset +1.1s
  - Row 3 "Distributed to UHNW clients via private banking" — Inter 600, 34px, `#F0F0F0` — offset +1.7s
  - 4px **cyan `#00D4FF`** accent bar, left edge (inset, not border-left); `mask-image` right-feather; NO blur.
- **Cyan element:** accent bar (1).
- **Word-sync note:** card is a supporting graphic, not a per-word kinetic; entry timed to land while Jasper is on the UHNW/private-banking content (comp 26–37, e.g. "ultra high net worth individuals" comp 24.5–25.7, "private banking clients" comp 34.8–35.5). Not word-synced lines → entry @ comp 26.3.
- `data-start="26.0" data-duration="17.0"`

### c3b5 — Clean window A (D6 split — first half)
- **Comp:** 43.0 – 50.4s   (**7.4s** ≤ 8s ✓)   **Src:** 743.0 – 750.4s
- **Template:** clean video window (no graphic)
- **Mode:** Mode A
- **Sub-comp:** none (clean)
- **Content:** Jasper on supply/demand + "the product itself needs to make a lot of sense for people." Speaker breathes.
- **Cyan element:** none (clean video).

### c3b6 — Kinetic: supplemental (D6 split — verified bisector)
- **Comp:** 50.4 – 54.5s   **Src:** 750.4 – 754.5s
- **Template:** kinetic-type (supplemental, D6)
- **Mode:** full-frame (both speakers)
- **Sub-comp:** `beat-c3b6-demand-kinetic.html`
- **Content / lines (word-synced, verified — splits the old 18s window):**
  - "DEMAND FOR" — `#F0F0F0` 130px — **comp 50.74** (src 750.74 "demand")
  - "STRUCTURED" — `#F0F0F0` 130px — **comp 51.42** (src 751.42 "structured")
  - "PRODUCTS" — **cyan `#00D4FF`** 130px — **comp 51.78** (src 751.78 "products")
  - Stack stays through beat end (~54.3).
- **Cyan element:** "PRODUCTS" (1).
- **Verified, not invented:** literal spoken phrase "…demand for structured products…" (D6 requires the supplemental be a real line from the table). ✓
- `data-start="50.4" data-duration="4.1"`

### c3b7 — Clean window B (D6 split — second half)
- **Comp:** 54.5 – 61.0s   (**6.5s** ≤ 8s ✓)   **Src:** 754.5 – 761.0s
- **Template:** clean video window (no graphic)
- **Mode:** Mode A (video returns to Mode A ~54.5)
- **Sub-comp:** none (clean)
- **Content:** "where we're seeing a lot of fit, for example, is an accelerator." Sets up the mechanics beat.
- **Cyan element:** none (clean video).

### c3b8 — Decision-tree: how autocallables work
- **Comp:** 61.0 – 76.0s   **Src:** 761.0 – 776.0s
- **Template:** decision-tree (4-step flow)
- **Mode:** Mode A
- **Sub-comp:** `beat-c3b8-autocallable-flow.html`
- **Content (exact node text, pop 0.35s apart, `back.out(1.5)`):**
  - Eyebrow "HOW AUTOCALLABLES WORK" — Inter 700, 32px, `#F0F0F0`
  - Node 1 "High crypto vol" — `#F0F0F0`
  - Node 2 "Bank issues structured note" — `#F0F0F0`
  - Node 3 "UHNW client buys" — `#F0F0F0`
  - Node 4 "Yield if BTC stays range-bound" — **cyan `#00D4FF`** (final node)
  - Connector arrows `#2a2a2a`.
- **Cyan element:** final node (1).
- **Word-sync note:** explanatory flow graphic (not per-word). Anchored to the geographic/fit explanation Jasper gives here (Asia ahead @ comp 67.2–69.1; accelerators "pretty good fit" @ comp 63.5–64.1). Nodes reveal from comp 61.3.
- `data-start="61.0" data-duration="15.0"`

### c3b9 — Kinetic: price ↔ narrative loop (the clip's quotable line)
- **Comp:** 76.0 – 88.0s   **Src:** 776.0 – 788.0s
- **Template:** kinetic-type
- **Mode:** full-frame (both speakers) — video full-frame ~75.8, exits ~87.8
- **Sub-comp:** `beat-c3b9-price-narrative.html`
- **Content / lines (word-synced, verified — corrects the original's comp-76 misfire):**
  - "PRICE" — `#F0F0F0` 130px — **comp 84.44** (src 784.44 "price")
  - "CREATES NARRATIVE" — `#F0F0F0` 130px — **comp 84.78** (src 784.78 "creates" → 785.12 "narrative")
  - "NARRATIVE CREATES PRICE" — **cyan `#00D4FF`** 130px — **comp 86.02** (src 786.02 "price"; phrase "creates price create narrative" @ 785.82–786.58)
  - Stack stays through beat end.
- **Cyan element:** "NARRATIVE CREATES PRICE" (1).
- **Correction:** original fired this at comp 76 (8–11s before the words). Re-synced to the verified comp 84.4–86.6. Beat window 76–88 holds all fires with ≥0.3s headroom. The comp 76–84 lead-in is the loop building (Mode-A→full-frame transition + first stack element entrance held until 84.44).
  - *Builder note:* if a visible 8s pre-roll feels long, pull the full-frame transition to ~83.5 and shorten this beat to comp 83.5–88; c3b8 then extends to 83.5. Either is acceptable; fires stay locked to the verified comp_t.
- `data-start="76.0" data-duration="12.0"`

### c3b10 — [SUPERSEDED DRAFT — DO NOT BUILD] Kinetic take-rates payoff
> ⚠️ This kinetic version is **superseded** by the swiss-grid FINAL below (see "Adjacency fix"). Kept only to show the reasoning. **Build the swiss-grid `c3b10 (REVISED — FINAL)` version.**
- **Comp:** 88.0 – 110.0s   **Src:** 788.0 – 810.0s
- **Template:** ~~kinetic-type~~ (superseded)
- **Mode:** full-frame (both speakers) — stays full-frame through clip end (clean content close, NOT a card; satisfies D4)
- **Sub-comp:** `beat-c3b10-take-rates.html`
- **Content / lines (word-synced, verified — corrects original's comp-99 placement):**
  - "TAKE RATES" — `#F0F0F0` 130px — **comp 95.82** (src 795.82 "take" → 796.06 "rates")
  - "MEANINGFULLY" — `#F0F0F0` 130px — **comp 98.54** (src 798.54 "meaningfully")
  - "HIGHER" — **cyan `#00D4FF`** 130px — **comp 99.04** (src 799.04 "higher")
  - Stack stays; clip ends on this content (last word in table is comp 108.88; final ~1s is clean video tail under the held stack — no end card).
- **Cyan element:** "HIGHER" (1).
- **Correction:** original placed lines at comp 99.1/100.3/101.5; verified comp is 95.82/98.54/99.04 (~3s earlier). Re-synced.
- **D4:** this is a content kinetic, not a name/outro card → compliant.
- `data-start="88.0" data-duration="22.0"`

---

## VERIFICATION

**Beat count:** 10 — within D-table range 9–10 for clip 3. ✓

**No two identical templates in a row:**
kinetic(b1) → swiss-grid(b2) → kinetic(b3) → liquid-glass(b4) → clean(b5) → kinetic(b6) → clean(b7) → decision-tree(b8) → kinetic(b9) → kinetic(b10) …
b9 and b10 are both kinetic and ADJACENT → **conflict**. RESOLUTION applied below.

> **Adjacency fix (binding):** c3b9 (price↔narrative) and c3b10 (take-rates) are both kinetic and back-to-back. Per D3 the swiss-grid→decision-tree swap freed swiss-grid for reuse. Insert the **price→narrative→demand→take-rates cycle as a swiss-grid** between them? No — that re-creates the c3b7/c3b8/c3b9 "swiss-grid sandwiched by kinetics" problem D3 fixed. Instead: **c3b9 stays kinetic; c3b10's template is changed to SWISS-GRID** (the "MARKET MECHANICS / take-rates ↑" content is a stat-style close), making the final run kinetic(b9) → swiss-grid(b10). This also restores a non-kinetic closer surface while remaining a content beat (not an outro card), satisfying D4.

### c3b10 (REVISED — FINAL template = swiss-grid)
- **Comp:** 88.0 – 110.0s   **Src:** 788.0 – 810.0s
- **Template:** **swiss-grid** (stat close)  *(changed from kinetic to break b9↔b10 kinetic adjacency)*
- **Mode:** Mode A (video returns to Mode A ~88.0; held through clip end — content beat, not a card)
- **Sub-comp:** `beat-c3b10-take-rates.html`
- **Content (exact text):**
  - Eyebrow "MARKET MECHANICS · 2026" — Inter 700, 32px, `#F0F0F0`
  - Stat "TAKE RATES ↑" — Inter 900, 160px, `#F0F0F0` — slam in @ **comp 95.82** (sync to "take rates" src 795.82/796.06)
  - Sublabel "Meaningfully higher than before" — Inter 600, 32px, `#F0F0F0` — @ **comp 98.54** (sync "meaningfully" 798.54 / "higher" 799.04)
  - Cyan horizontal rule (draws left→right) @ comp 96.3 — **cyan `#00D4FF`** (single cyan; stat stays white per D7 stat-OR-rule)
  - Footer "Structured products: next-cycle catalyst" — Inter 600, 30px, `#F0F0F0` — @ comp 104.0 (sync "infrastructure is finally here" comp 103.18–104.18)
- **Cyan element:** the rule (1).
- **Word-sync:** stat/ sublabel/ footer entrances pinned to verified comp_t (95.82, 98.54, 104.0). ✓
- `data-start="88.0" data-duration="22.0"`

**FINAL template sequence (no two identical in a row):**
kinetic(b1) → swiss-grid(b2) → kinetic(b3) → liquid-glass(b4) → clean(b5) → kinetic(b6) → clean(b7) → decision-tree(b8) → kinetic(b9) → swiss-grid(b10). ✓

**One cyan `#00D4FF` element per beat:**
b1 "NOW." | b2 rule | b3 "TO UHNW INDIVIDUALS" | b4 accent bar | b5 none(clean) | b6 "PRODUCTS" | b7 none(clean) | b8 final node | b9 "NARRATIVE CREATES PRICE" | b10 rule. ✓ (no beat has two cyan; swiss-grid beats put cyan on the rule and keep the stat white.)

**Every non-editorial kinetic line has a real comp_t from `clip3-words.txt`:**
- c3b3: 21.38 (autocallables), 22.44 (accelerators), 25.70 (individuals) ✓
- c3b6: 50.74 (demand), 51.42 (structured), 51.78 (products) ✓
- c3b9: 84.44 (price), 84.78 (creates), 86.02 (price) ✓
- c3b10 swiss-grid entrances: 95.82 (take rates), 98.54 (meaningfully), 99.04 (higher), 104.0 (infrastructure/finally here) ✓
- Editorial (not word-synced): c3b1 hook lines @ 0.08 / 0.88 / 1.60 only. ✓

**D-directives applied:**
- D1 opening pattern (full-frame t=0 → Mode A t=3, copy clip-2): ✓ (c3b1/c3b2, MODE_A values + GSAP from clip-2).
- D2 word-sync (read off table, ±0.05s): ✓ (all kinetic + swiss-grid entrances re-derived; corrected c3b3 ~5s, c3b9 ~8–11s, c3b10 ~3s vs original).
- D3 swaps for clip 3: c3b4 → liquid-glass (builder's-call, staggered rows) ✓ ; original c3b8 swiss-grid-cycle → **decision-tree** ✓ (now c3b8 = autocallable-flow decision-tree).
- D4 no-outro: clip ends on content swiss-grid c3b10 held to clip end, no name/CTA card. ✓
- D5 hook replacement: N/A for clip 3 (clips 1/5/7 only) — hook KEPT. ✓
- D6 pacing: old 18s clean window (orig c3b5) split into c3b5 (7.4s) + supplemental kinetic c3b6 (verified "DEMAND FOR STRUCTURED PRODUCTS") + c3b7 (6.5s); no clean stretch >8s. ✓
- D7 palette/type: cyan single-per-beat, `#F0F0F0` labels (no `#888888`), solid cards no blur/grain, eyebrow Inter 700 ≥32px, "2026 = this year". ✓
- D8 (clip 4 phrase order): N/A.
- D9 (clip 5 closer): N/A.

**Wrong-window / fabrication checks (from reviews):**
- Original c3b9 cyan line referenced `src ~1192` (belongs to clip 5) → REMOVED; replaced with verified in-window src 786.02. ✓
- No fabricated lines; the c3b6 supplemental is the literal spoken "demand for structured products." ✓

---

## BUILD MANIFEST ROW
`clip_3 | clip-3-structured-products | 700 | 810 | kinetic-type,swiss-grid,liquid-glass,decision-tree | 10 beats`

## SUB-COMP FILE LIST
`beat-c3b1-hook.html`, `beat-c3b2-swiss-launch.html`, `beat-c3b3-products-kinetic.html`, `beat-c3b4-product-card.html`, `beat-c3b6-demand-kinetic.html`, `beat-c3b8-autocallable-flow.html`, `beat-c3b9-price-narrative.html`, `beat-c3b10-take-rates.html` (c3b5, c3b7 are clean windows — no sub-comp).
