# Clip 3 — REDESIGN EDL v2 (`clip-3-structured-products`)

> Supersedes `clip3-edl-final.md`. This version fixes the three review failures:
> **(1)** opening kinetic now matches the words ACTUALLY spoken in the first ~0–5s (re-picked in-point);
> **(2)** structure is rebuilt around a TERM-REVEAL lead device (no generic `0N / EYEBROW / STAT / tag-row`
> swiss-grid open that every sibling used); **(3)** framing re-verified from real source frames → `object-position: 80% center`.

---

## NEW IN / OUT (re-picked per RULE 1)

| field | v1 (FAILED) | **v2** | why |
|---|---|---|---|
| `src_in` | 700.00 | **718.20** | Opens ON the term-reveal line. Trims the "Yeah, yeah, yeah… I was a decade off… 2016, 17, BTC as underlying" filler/tangent (src 700.16–717.6). First spoken words on screen are now *"You see large financial institutions issuing stuff like autocallables, accelerators."* |
| `src_out` | 810.00 | **808.50** | Lands just after "…volumes on screen on option exchanges" so the take-rates / infrastructure payoff resolves on a complete clause. No outro. |
| duration | 110.0s | **90.3s** | comp_t = src_t − 718.20. (All comp numbers below are recomputed for this in-point.) |
| `data-media-start` | 700 | **718.20** | source.mp4 is the FULL episode (2853s, 1920×1080, 30fps) → media-start is absolute episode time. |

**Opening line (verbatim, src 718.20–722.44):** "You see large financial institutions issuing stuff like **autocallables, accelerators**."
- word `you` src 718.20 → **comp 0.00**
- word `large` src 718.68 → comp 0.48
- word `autocallables` src 721.38 → comp 3.18
- word `accelerators` src 722.44 → comp 4.24

The clip's signature terms (autocallables / accelerators) are SPOKEN inside the first 4.3s — this is why the term-reveal lead device is honest here, not anticipatory.

---

## FRAMING — verified from real frames (RULE 3)

**Chosen: `object-position: 80% center`** (NOT clip-2's 83%). `MODE_A = { left: 1229, top: 108, width: 614, height: 864 }`, `border-radius: 6px`. No vertical bias / no extra scale-up beyond the standard slow Ken Burns (1.00→1.04). Keep `object-fit: cover`.

**Evidence (frames extracted from `source.mp4` and cover-cropped to the 614×864 Mode-A window):**
- Source is a **side-by-side**: Nic (host) fills the LEFT half (x 0–960), Jasper (guest) fills the RIGHT half (x 960–1920), each centered in their own half. Seam at x=960. Jasper's face center ≈ full-frame **x 1290** (≈67% across), eyes ≈ **y 200/1080 ≈ 19%** from top, name lower-third "Jasper De Maere · Wintermute" bottom-left of his panel. Modest dead ceiling above his head — acceptable, not excessive.
- Cover math for the 614×864 window: source scales to 1536×864 (scale 0.8, height fills exactly → NO vertical crop slack, so vertical `object-position`/bias does nothing without an explicit scale-up). `object-position: X%` slides the 614-wide window: visible source x-range = `[X%·922 , X%·922 + 768] / 0.8`.
  - **76%** → source x **876–1644** — includes the x=960 seam, bleeds a sliver of the host on the left edge. WRONG.
  - **80%** → source x **922–1690** (center x≈1306, ≈ Jasper's face) — viewed crop: **Jasper squarely centered, name fully readable, clears the seam, balanced headroom.** ✓ chosen.
  - **83%** → source x **956–1724** (center x≈1340) — viewed crop: Jasper leans LEFT of center with extra empty wall on the right; name nudged toward the left edge. Acceptable but worse-centered than 80% for THIS guest panel.
- A test with `scale 1.08` + downward vertical bias trimmed ceiling but pinched the name lower-third and added head-room tightness for negligible gain → **rejected**. Plain `80% center` is cleanest.

> Note vs clip-1/clip-2: clip-1 used `50%` (centers the SEAM/host — WRONG). clip-2 used `83%` and is correct *for clip-2's framing*. For clip-3, the viewed frames put Jasper best-centered at **80%**.

Mode-A entry/return mirror clip-2 exactly: full-frame return = `{left:0,top:0,width:1920,height:1080,borderRadius:"0px"}` (`expo.inOut`, 0.4s); on Mode A, `#bg-glow` opacity→1 at +0.3s, `#zone-rule` `scaleY 0→1` at +0.4s (`power4.out`).

---

## STYLE (still binding — D7 / D4)

bg `#0A0A0A`; primary text `#F0F0F0`; **ONE cyan `#00D4FF` element per beat**; cards `rgba(20,26,34,0.92)` solid fill + 4px inset cyan accent bar + soft glow + 1px border + `mask-image` right-feather — **NO `backdrop-filter` blur, NO grain**. Eyebrow Inter 700 ≥32px `#F0F0F0`; body/bullets Inter ≥600; any small/label text `#F0F0F0` (never `#888888` under 48px). Kinetic phrase lines Inter 900, ~130px, white, payoff line cyan; lines slam in and **STAY** (no dim). Date framing: 2026 = "this year". **No intro card, no outro/CTA — clip ends on a content beat (c3b9 stat close held to clip end).**

---

## LEAD DEVICE — TERM-REVEAL-LED (RULE 2)

The clip does **not** open on the `index / eyebrow / big-stat / tag-row` swiss-grid. It opens on a **kinetic term-reveal**: the two product names Jasper says (AUTOCALLABLES, ACCELERATORS) slam in word-synced as he says them, then **pay off into a product glossary card** (each term gets a one-line plain-English definition). The whole clip is organized as: *name the products → define them → show how they reach the buyer → demand → geography → price/narrative loop → take-rates catalyst.* Distinct silhouette from siblings (clip-2 opens stat-first; clip-1 opens stat-first). Real catalog blocks chosen where they fit: kinetic phrase build (`kinetic-type`), `flowchart`/`decision-tree` for the distribution chain, `data-chart`-style stat close.

---

## TEMPLATE SEQUENCE (no two identical in a row; no generic swiss-grid open)

`kinetic term-reveal (b1)` → `liquid-glass glossary (b2)` → `decision-tree distribution (b3)` → `clean (b4)` → `kinetic demand (b5)` → `swiss-grid geography (b6)` → `clean (b7)` → `kinetic price↔narrative (b8)` → `swiss-grid/stat take-rates close (b9)`.

Beat count: **9** (D-table range for clip 3 = 9–10). ✓

---

# BEAT MAP

Every beat: `id` · comp range · src range · template/block · speaker mode · sub-comp file · full content (exact hex) · per kinetic line **on-screen text + matched transcript words + comp_t** (verified from `clip3-words.txt` re-based to src_in 718.20).

---

### c3b1 — Kinetic TERM-REVEAL (opening; word-synced, NOT editorial)
- **Comp:** 0.0 – 6.5s   **Src:** 718.20 – 724.70s
- **Template/block:** `kinetic-type` phrase build (term-reveal variant). Optionally back the two product words with a `caption-kinetic-slam`-style slam; keep DESIGN palette.
- **Mode:** **full-frame** (BOTH speakers visible) over a left dark-gradient backdrop. Video animates to Mode A at the beat's end (see master GSAP, transition at comp ~6.3).
- **Sub-comp:** `beat-c3b1-termreveal.html`
- **On-screen lines (each slams in, STAYS, no dim):**
  - `YOU SEE` — `#F0F0F0` 120px — fires **comp 0.00** — matches **"you"** src 718.20 (`you`/`see` 718.20/718.46)
  - `LARGE INSTITUTIONS` — `#F0F0F0` 120px — fires **comp 0.48** — matches **"large"** src 718.68 (`large financial institutions` 718.68–719.30)
  - `ISSUING` — `#F0F0F0` 120px — fires **comp 1.72** — matches **"issuing"** src 719.92
  - `AUTOCALLABLES` — `#F0F0F0` 130px (term, heavier slam + 0.04em tracking) — fires **comp 3.18** — matches **"autocallables"** src 721.38
  - `ACCELERATORS` — **cyan `#00D4FF`** 130px (payoff term) — fires **comp 4.24** — matches **"accelerators"** src 722.44
  - Whole stack drifts up + fades at **comp 6.3** (`power2.in`) as video begins Mode-A transition.
- **Cyan element:** `ACCELERATORS` (1).
- **Opening "3+ element types before 6s" (D1):** type 1 = kinetic phrase build (this beat); type 2 = glossary card eyebrow/index + rule (c3b2 starts comp 6.5, its eyebrow+rule land by ~7.0 — to fully satisfy "before 6.0s" the build agent should fire c3b2's index/eyebrow/rule as a 3rd element at **comp 5.4–5.9** layered over the still-running term stack, OR slam a small `STRUCTURED PRODUCTS` eyebrow + cyan rule on the left at comp 5.0 within c3b1). See "Opening 6s compliance" note below. **Element types in first 6s = kinetic phrase build + term slam + eyebrow/rule = 3.** ✓
- `data-start="0.0" data-duration="6.5"`

> **Opening-6s compliance (build instruction):** because the in-point now lands directly on speech, the first 6s are dominated by the term-reveal kinetic. To meet DESIGN's "3 DIFFERENT element types before 6.0s" bar WITHOUT a fake stat, add inside `beat-c3b1-termreveal.html`: a monospace index `03` + eyebrow `STRUCTURED PRODUCTS · CRYPTO` (Inter 700, 32px, `#F0F0F0`) slamming in top-left at **comp 5.0**, and a thin neutral `#2a2a2a` rule drawing under it at comp 5.3 (the rule is NOT cyan here — `ACCELERATORS` already owns this beat's single cyan). That yields: (1) kinetic phrase build, (2) heavy term slams, (3) index+eyebrow+rule — three distinct element types, speaker visible full-frame throughout. The eyebrow/index/rule then hand off visually into c3b2.

### c3b2 — Liquid-glass GLOSSARY card (term-reveal payoff: define the two products)
- **Comp:** 6.5 – 19.0s   **Src:** 724.70 – 737.20s
- **Template/block:** liquid-glass card (DESIGN "Cards & Panels", clip-2/c3b4 pattern: solid `rgba(20,26,34,0.92)`, 4px inset cyan accent bar, glow, 1px border, `mask-image` right-feather, NO blur, rows STAGGER). Two glossary rows (term + one-line definition) + a distribution footnote.
- **Mode:** **Mode A** (video transitions full-frame → right-40% at comp ~6.3; card slides in from right). `object-position: 80% center`.
- **Sub-comp:** `beat-c3b2-glossary.html`
- **Content (exact text):**
  - Index `03` (JetBrains Mono 20px `#F0F0F0`) + Eyebrow `STRUCTURED PRODUCTS · CRYPTO` (Inter 700, 32px, `#F0F0F0`) — entry comp ~6.8
  - Card row 1 — title `Autocallables` (Inter 700, 40px, `#F0F0F0`) + def `Auto-redeem note that pays a coupon while BTC stays in a range` (Inter 600, 27px, `#F0F0F0`) — stagger entry **comp 7.6**
  - Card row 2 — title `Accelerators` (Inter 700, 40px, `#F0F0F0`) + def `Leveraged upside to a cap, downside ~1:1` (Inter 600, 27px, `#F0F0F0`) — stagger entry **comp 8.4**
  - Footnote row `Issued by large financial institutions` (Inter 600, 28px, `#F0F0F0`, cyan dot) — stagger entry **comp 9.2**
  - 4px **cyan `#00D4FF`** accent bar (inset, left edge); `mask-image` right-feather; NO blur.
- **Cyan element:** accent bar (1).
- **Word-sync note:** supporting graphic, not per-word. Entry pinned to land while Jasper is still naming/contextualizing the products and the issuers — "issuing stuff like autocallables, accelerators **to their ultra high net worth individuals and to their network**" (src 723.18–726.96, comp ~5.0–8.8) and "validates the fact that they've seen appetites" (comp ~12). The two glossary terms are the literal words just spoken; definitions are editorial (mark `<!-- definitions EDITORIAL: explanatory, not spoken verbatim -->`). Card holds through the "validates appetite / private banking clients" stretch.
- `data-start="6.5" data-duration="12.5"`

### c3b3 — DECISION-TREE: distribution chain (how the product reaches the buyer)
- **Comp:** 19.0 – 31.0s   **Src:** 737.20 – 749.20s
- **Template/block:** `decision-tree` / `flowchart` — 4 nodes, left-to-right with a downstream arrow, `back.out(1.5)` node pops ~0.4s apart; final node cyan. (Distinct from c3b2 card and from any swiss-grid.)
- **Mode:** **Mode A** (video already right-40%). `object-position: 80% center`.
- **Sub-comp:** `beat-c3b3-distribution.html`
- **Content (exact node text):**
  - Eyebrow `THE DISTRIBUTION CHAIN` (Inter 700, 32px, `#F0F0F0`)
  - Node 1 `Large institution` — `#F0F0F0`
  - Node 2 `Issues structured note` — `#F0F0F0`
  - Node 3 `Private-banking desk` — `#F0F0F0`
  - Node 4 `UHNW client buys` — **cyan `#00D4FF`** (final node)
  - Connector arrows `#2a2a2a`.
- **Cyan element:** final node `UHNW client buys` (1).
- **Word-sync anchor (explanatory flow, not per-word; nodes anchored to the spoken supply chain):** "they've seen appetites from a specific subset of like **private banking clients** or **ultra high net worth individuals**" — `private` src 734.82 / `banking` 735.20 / `clients` 735.52 (comp 16.6–17.3, just before this beat) and "we're seeing that exact same thing on our side… supply demand" (src 737.92–742.80, comp 19.7–24.6, inside the beat). Nodes reveal from **comp 19.4** (node1), 19.8, 20.2, 20.6.
- **Variety note:** this replaces the v1 "how autocallables work / yield if range-bound" tree with the *distribution* chain — it carries the private-banking distribution point that v1 had crammed into a card footnote, and it is the natural visual for the words spoken here.
- `data-start="19.0" data-duration="12.0"`

### c3b4 — CLEAN window A
- **Comp:** 31.0 – 38.0s   (**7.0s** ≤ 8s ✓)   **Src:** 749.20 – 756.20s
- **Template:** clean video window (no graphic). **Mode A.**
- **Sub-comp:** none.
- **Content:** Jasper: "It's not like there's this insatiable demand for structured products at the moment, but we're definitely seeing… depending where we're seeing a lot of fit…" Speaker breathes.
- **Cyan element:** none.

### c3b5 — Kinetic: DEMAND (word-synced supplemental)
- **Comp:** 38.0 – 42.5s   **Src:** 756.20 – 760.70s
- **Template/block:** `kinetic-type` phrase build (full-frame). Short 3-line beat.
- **Mode:** **full-frame** (both speakers); video returns full-frame at comp ~37.8, exits to Mode A at ~42.3.
- **Sub-comp:** `beat-c3b5-demand.html`
- **On-screen lines:**
  - `WHERE WE SEE` — `#F0F0F0` 130px — fires **comp 38.46** — matches **"fit"** clause start; use `fit` src 756.66 → comp 38.46 (phrase "where we're seeing a lot of **fit**")
  - `THE BEST FIT` — `#F0F0F0` 130px — fires **comp 39.30** — editorial bridge (mark `<!-- bridge: 'a lot of fit' paraphrase -->`) OR fire on `for`/`example` src 757.00/757.12 (comp 38.80/38.92) — builder's call, keep within beat
  - `ACCELERATORS` — **cyan `#00D4FF`** 130px — fires **comp 39.82** — matches **"accelerator"** src 758.02
  - Stack stays through beat end (~42.3).
- **Cyan element:** `ACCELERATORS` (1).
- **Verified spoken anchor:** "…where we're seeing a lot of **fit**, for example, is an **accelerator**." (`fit` 756.66, `accelerator` 758.02). Real spoken line — not invented. (If a cleaner 3-line build is wanted, the literal "DEMAND FOR / STRUCTURED / PRODUCTS" also exists at `demand` 750.74 comp 32.54 / `structured` 751.42 comp 33.22 / `products` 751.78 comp 33.58 — but that sits in the c3b4 clean window; prefer the accelerator-fit line here to avoid moving the clean window.)
- `data-start="38.0" data-duration="4.5"`

### c3b6 — SWISS-GRID: geography (the ONE swiss-grid — placed mid-clip, distinct content)
- **Comp:** 42.5 – 54.0s   **Src:** 760.70 – 772.20s
- **Template/block:** `swiss-grid` — geographic adoption ranking (NOT the generic open grid; this is a 3-row region comparison). One cyan accent on the rule.
- **Mode:** **Mode A** (video returns right-40% at comp ~42.3). `object-position: 80% center`.
- **Sub-comp:** `beat-c3b6-geography.html`
- **Content (exact text):**
  - Index `03` + Eyebrow `STRUCTURED PRODUCTS · BY REGION` (Inter 700, 32px, `#F0F0F0`) — entry comp ~43.0
  - Cyan horizontal rule draws left→right — **cyan `#00D4FF`** (beat's single cyan) — comp ~43.3
  - Row `ASIA` — `Ahead — high take rate` (Inter 700 label 48px / Inter 600 value 30px, `#F0F0F0`) — entry **comp 49.02** (sync "Asia" src 767.22)
  - Row `EUROPE + US` — `Catching up — rising demand` (Inter 600, 30–40px, `#F0F0F0`) — entry **comp 54.66**? → too late; fire at **comp 55.20** belongs to next region word. To keep both rows inside this beat, fire `EUROPE + US` row at **comp 50.88** (sync "products" tail of "Asia has been ahead on structured **products**" src 769.08) and let the value text update; the literal "Europe and the US" (src 772.86/773.40) lands at the beat tail under the held grid.
  - (Optional) small footnote `Stake rate has been very high` (Inter 600, 28px, `#F0F0F0`) — comp ~46.0 (sync "stake rate… very high" src 769.68–770.66, comp 51.5–52.5).
- **Cyan element:** the rule (1). Region labels stay white (D7 stat-OR-rule → rule carries cyan).
- **Word-sync:** ASIA row pinned to spoken "Asia" (comp 49.02); region content tracks "Asia has been ahead… increasingly in Europe and the US we're also seeing that demand" (src 767.22–777.00, comp 49.0–58.8). Eyebrow/rule are structural (entry ~43.0/43.3, mark structural).
- **Variety note:** the series' single swiss-grid is a *regional ranking*, deliberately unlike clip-2's stat grid and unlike the v1 open grid.
- `data-start="42.5" data-duration="11.5"`

### c3b7 — CLEAN window B
- **Comp:** 54.0 – 60.5s   (**6.5s** ≤ 8s ✓)   **Src:** 772.20 – 778.70s
- **Template:** clean video window (no graphic). **Mode A.**
- **Sub-comp:** none.
- **Content:** "…increasingly in Europe and the US, we're also seeing that demand. So cautiously optimistic." Speaker breathes into the price/narrative pivot.
- **Cyan element:** none.

### c3b8 — Kinetic: PRICE ↔ NARRATIVE loop (the clip's quotable line)
- **Comp:** 60.5 – 71.0s   **Src:** 778.70 – 789.20s
- **Template/block:** `kinetic-type` phrase build (full-frame). The loop line — render the second line as a literal cycle (PRICE→NARRATIVE→PRICE) with a thin cyan loop arrow on the payoff if desired (single cyan).
- **Mode:** **full-frame** (both speakers); video full-frame at comp ~60.3, exits to Mode A at ~70.8.
- **Sub-comp:** `beat-c3b8-price-narrative.html`
- **On-screen lines (word-synced — corrects v1, which fired this ~8s early at comp 76 with a wrong-window cyan ref):**
  - `PRICE` — `#F0F0F0` 130px — fires **comp 66.24** — matches **"price"** src 784.44
  - `CREATES NARRATIVE` — `#F0F0F0` 130px — fires **comp 66.58** — matches **"creates"** src 784.78 → **"narrative"** 785.12
  - `NARRATIVE CREATES PRICE` — **cyan `#00D4FF`** 130px — fires **comp 67.62** — matches **"creates"** src 785.82 → **"price"** 786.02 (spoken "…creates price create narrative", the loop close)
  - Stack stays through beat end.
- **Cyan element:** `NARRATIVE CREATES PRICE` (1).
- **Word-sync note:** Jasper says "I think **price creates narrative, creates price create narrative**" (src 784.44–786.58, comp 66.2–68.4). The beat window 60.5–71.0 holds all three fires with ≥0.3s headroom; the comp 60.5–66.2 lead-in is the full-frame transition + "Obviously, the price, like I think…" (src 780.62–784.26) building to the line. First line held until 66.24 (do not pre-fire).
- `data-start="60.5" data-duration="10.5"`

### c3b9 — STAT close: TAKE RATES (content close, NOT an outro)
- **Comp:** 71.0 – 90.3s   **Src:** 789.20 – 808.50s
- **Template/block:** `data-chart`-style stat / `swiss-grid` stat close — a single rising metric with a short rationale. Held to clip end as a CONTENT beat (no name/CTA card → satisfies D4). Breaks the b8↔b9 kinetic adjacency (b8 kinetic → b9 stat).
- **Mode:** **Mode A** (video returns right-40% at comp ~70.8; held to clip end). `object-position: 80% center`.
- **Sub-comp:** `beat-c3b9-take-rates.html`
- **Content (exact text):**
  - Index `03` + Eyebrow `THE NEXT-CYCLE CATALYST · 2026` (Inter 700, 32px, `#F0F0F0`) — entry comp ~73.0
  - Stat `TAKE RATES ↑` (Inter 900, 160px, `#F0F0F0`) — slam in **comp 77.62** (sync "take" src 795.82 / "rates" 796.06)
  - Cyan horizontal rule draws left→right — **cyan `#00D4FF`** (single cyan) — comp ~78.1
  - Sublabel `Meaningfully higher than before` (Inter 600, 32px, `#F0F0F0`) — entry **comp 80.34** (sync "meaningfully" src 798.54 / "higher" 799.04)
  - Footer `Demand + infrastructure now both here` (Inter 600, 30px, `#F0F0F0`) — entry **comp 84.98** (sync "infrastructure" src 803.18 / "finally here" 803.90–804.18)
  - Late re-tick of the `↑` arrow or footer at **comp 87.4** (sync "volumes on screen" src 805.64) so the ~3s tail isn't static.
- **Cyan element:** the rule (1). Stat stays white (D7 stat-OR-rule).
- **Word-sync:** stat / sublabel / footer entrances pinned to verified comp_t (77.62, 80.34, 84.98). The spoken support: "I could definitely see the **take rates** on structured products being **meaningfully higher** than we had before… the demand is one thing but then also the **infrastructure is finally here**" (src 795.82–804.18, comp 77.6–86.0). Clip ends on this content; final ~1.5s is clean video tail under the held stat — NO end card.
- `data-start="71.0" data-duration="19.3"`

---

## MASTER GSAP TRANSITION PLAN (mode A ↔ full-frame; mirrors clip-2)

| at comp | action |
|---|---|
| 0.0 | full-frame, both speakers (c3b1 term-reveal). No GSAP (CSS default). |
| ~6.3 | full-frame → **Mode A** (`expo.inOut` 0.7s); glow +0.3, rule +0.4. c3b2 glossary slides in. Ken Burns 1.00→1.04 over remaining clip. |
| 6.5–37.6 | Mode A holds across c3b2 (card) → c3b3 (tree) → c3b4 (clean). |
| ~37.8 | Mode A → full-frame for c3b5 demand kinetic (fires 38.46). |
| ~42.3 | full-frame → Mode A for c3b6 geography + c3b7 clean. |
| ~60.3 | Mode A → full-frame for c3b8 price↔narrative kinetic (fires 66.24). |
| ~70.8 | full-frame → Mode A for c3b9 stat close; **held to clip end (90.3)** — content close, no exit. |

`MODE_A = { left: 1229, top: 108, width: 614, height: 864 }`, `object-position: 80% center`, `border-radius: 6px`. Full-frame return = `{left:0,top:0,width:1920,height:1080,borderRadius:"0px"}`.

---

## VERIFICATION

**RULE 1 — open on a real line:** ✓ src_in=718.20; opening kinetic lines fire on `you`(0.00)/`large`(0.48)/`issuing`(1.72)/`autocallables`(3.18)/`accelerators`(4.24) — all the actual spoken words. No anticipatory text pulled from later in the clip.

**Every non-editorial kinetic line has a real comp_t from the transcript (re-based src_in 718.20):**
- c3b1: you 0.00 · large 0.48 · issuing 1.72 · autocallables 3.18 · accelerators 4.24 ✓
- c3b5: fit 38.46 · accelerator 39.82 (bridge line marked editorial) ✓
- c3b8: price 66.24 · creates/narrative 66.58 · creates/price 67.62 ✓
- c3b9 stat entrances: take/rates 77.62 · meaningfully/higher 80.34 · infrastructure/finally-here 84.98 · volumes 87.4 ✓
- EDITORIAL (marked, not word-synced): c3b2 glossary definitions; c3b1 index/eyebrow/rule structural (comp 5.0); c3b6 eyebrow/rule structural (comp 43.0/43.3); c3b9 eyebrow structural (comp 73.0).

**RULE 2 — varied structure:** ✓ TERM-REVEAL lead device; no generic `0N/EYEBROW/STAT/tag-row` open. Template order kinetic→card→tree→clean→kinetic→swiss-grid→clean→kinetic→stat. No two identical templates adjacent. The single swiss-grid is a mid-clip regional ranking, not the open. Distinct silhouette from clip-1/clip-2 (both open stat-first).

**RULE 3 — framing:** ✓ `object-position: 80% center` chosen from viewed cover-crops (Jasper squarely centered, name readable, seam cleared); 83% rejected (leans left), 76% rejected (host bleed), scale-up rejected (clips name). MODE_A geometry copies clip-2.

**One cyan `#00D4FF` per beat:** b1 ACCELERATORS · b2 accent bar · b3 final node · b4 none(clean) · b5 ACCELERATORS · b6 rule · b7 none(clean) · b8 NARRATIVE CREATES PRICE · b9 rule. ✓

**D4 no-outro / no-intro:** ✓ ends on c3b9 stat content held to clip end; no name/CTA/intro card.

**D6 pacing:** longest clean window 7.0s (c3b4) ≤ 8s; c3b7 6.5s. ✓

**D7 palette/type:** cyan single-per-beat; `#F0F0F0` labels (no `#888888` under 48px); solid cards no blur/grain; eyebrow Inter 700 ≥32px; 2026 = "this year". ✓

**Beat count:** 9 (in D-table range 9–10 for clip 3). ✓

---

## SUB-COMP FILE LIST (v2 — rename/rebuild; old c3b* files are superseded)
`beat-c3b1-termreveal.html`, `beat-c3b2-glossary.html`, `beat-c3b3-distribution.html`, `beat-c3b5-demand.html`, `beat-c3b6-geography.html`, `beat-c3b8-price-narrative.html`, `beat-c3b9-take-rates.html` (c3b4, c3b7 are clean windows — no sub-comp).

**index.html changes for build agent:** `data-media-start="718.20"`, `data-duration="90.3"` on `#short_mag_cut` + `#a-roll-audio` + `#master-root`; `object-position: 80% center`; z-index:3 rule must list `#beat-c3b1, #beat-c3b2, #beat-c3b3, #beat-c3b5, #beat-c3b6, #beat-c3b8, #beat-c3b9`.

## BUILD MANIFEST ROW
`clip_3 | clip-3-structured-products | 718.20 | 808.50 | kinetic-type,liquid-glass,decision-tree,swiss-grid,data-chart | 9 beats`
