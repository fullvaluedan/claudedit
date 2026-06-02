# CLIP 8 — AI MULTIPLIER · EDL v2 (RE-DESIGN)

**clip_id:** clip_8 · **dir:** `clip-8-ai-multiplier` · **slug:** `clip-8-ai-multiplier`
**Init template:** kinetic-type. **Source:** `source.mp4` (1920×1080, 30fps; symlink to clip-2 master). **data-media-start = 1677.20.**

## WHY v2 (the three failures being fixed)

1. **Opening text did not match the spoken dialog.** v1 opened at src 1675 firing an editorial hook "ONE TRADER / DOING THE WORK OF / 2–3 ANALYSTS" at comp 0.08/0.88/1.60 — but at src 1675 Jasper is actually finishing the *previous* thought ("…fell into the hands of billions of users"). The "two to three" number is not spoken until src 1682–1684. **Fix:** move the in-point forward to **src 1677.20** — the exact frame the money line begins ("I can tell you that I think the work which I'm doing today would require a team of two to three people") — and **word-sync the lead stat so the number "2–3" lands ON the spoken "two…to three" (comp 4.80→6.48)**, not before. No anticipatory text.
2. **Repetitive / formulaic structure.** v1 used the generic `0N / EYEBROW / RULE / two-column` swiss-grid opening (the same chrome every clip used) and then alternated kinetic→swiss-grid→decision-tree mechanically. **Fix:** open on the **STAT-LED lead device** (a count reveal that resolves on the spoken number, then collapses 2–3 → 1), and vary the block vocabulary across the clip (count-stat → kinetic → tag-chips → before/after swiss-grid → flowchart → host-Q → split swiss-grid → bulleted glass → kinetic → liquid-glass risk-metrics). No two adjacent beats share a template, and the opening is NOT the swiss-grid index/eyebrow grid.
3. **Framing.** v1 inherited `object-position: 83%` but never verified it and never addressed the dead ceiling. **Fix:** verified from real source frames (below); keeping **83%** (centers Jasper, keeps his burned-in name visible — 90% truncates it) and adding a **1.08 base scale-up** to remove the dead ceiling above his head.

---

## NEW IN/OUT

| field | value |
|---|---|
| **src_in** | **1677.20** (was 1675.00 — trimmed 2.20s of the prior-thought tail "…fell into the hands of billions of users") |
| **src_out** | **1845.00** (unchanged — ends clean on "I don't think we're that far off…") |
| **duration** | **167.80s** |
| **comp formula** | **comp = src − 1677.20** |
| **data-media-start** | **1677.20** (update index.html `<video>` and `<audio>`; was 1675) |
| **data-duration (master + media)** | **167.8** (was 170) |

Opening frame check (src 1677.20, `/tmp/in_c8_1677.2.png`): Jasper is mid-delivery (mouth open, engaged), framed in the right half. Both speakers visible → full-frame kinetic open is valid (not "text on black").

---

## FRAMING (RULE 3 — verified from actual source frames)

**Source layout (viewed `/tmp/fr_c8_1690.png`, `/tmp/fr_c8_1775.png`):** hard side-by-side. **Nic (host) LEFT half (x 0–960). Jasper (guest, the subject) RIGHT half (x 960–1920),** centered in his own half; head spans ≈ x 1180–1620 (center ≈ x 1400), eyes ≈ 28–32% from top. A burned-in lower-third **"Jasper De Maere / Wintermute"** sits at the bottom of his half (≈ x 1000–1250).

**Mode-A geometry (copied from clip-2):** `{ left:1229, top:108, width:614, height:864, borderRadius:6px }`. `object-fit: cover` ⇒ cover-scale 0.80 ⇒ scaled source 1536×864, zero vertical overflow, 922px horizontal overflow.

**Two Mode-A timestamps extracted and compared (real crops, not math):**
- **src 1690** (Jasper: "And for me, I'm doing research…") — `/tmp/modeA_c8_1690_p83.png` (83%) vs `/tmp/modeA_c8_1690_p90.png` (90%).
- **src 1815** (Jasper: "…potentially short oil") — `/tmp/modeA_c8_1815_p83.png` (83%) vs `/tmp/modeA_c8_1815_p90.png` (90%).

What I saw:
- **83% → source crop x:[957..1725], center x≈1340.** Jasper centered, face fills the frame, **"Jasper De Maere / Wintermute" lower-third fully visible**. Slight dead ceiling above his head.
- **90% → source crop x:[1037..1805], center x≈1410.** Pushes Jasper LEFT, crops into the wall on his right, and **truncates the burned-in name to "…sper De Maere"** — rejected.
- **50% / 62% would center the seam/Nic — WRONG** (confirmed by the seam at x=960).

**Ceiling fix:** Mode A has zero vertical overflow, so a vertical `object-position` bias does nothing. Tested a CSS scale-up instead (`/tmp/modeA_c8_1690_z108.png` = scale 1.08): face larger, eyes at a good height, ceiling reduced, **name still fully visible** (z108_up biased the name off the bottom — rejected).

### CHOSEN: `object-position: 83% center` + Ken-Burns **base scale 1.08** (drifting 1.08 → 1.12 over the clip)

> **Rationale (from the frames I viewed):** 83% is the only horizontal position that BOTH centers Jasper AND keeps his burned-in "Jasper De Maere / Wintermute" name fully on-screen; 90% truncated the name and added empty wall. The 1.08 base scale closes the dead ceiling above his head (which 1.00 left open) without truncating the name or his shoulders. This is clip-2's proven 83% with the brief's requested scale-up for the ceiling.

**CSS to set in `index.html`:**
```css
#short_mag_cut, #short_mag_cut_frame > img.__render_frame__, #short_mag_cut_frame > img.__preview_render_frame__ {
  object-fit: cover;
  object-position: 83% center;   /* centers Jasper; keeps burned-in name on-screen */
}
```
```js
// Ken Burns base scale 1.08 → 1.12 (was 1.0 → 1.04). Removes dead ceiling.
masterTL.fromTo(vid,
  { scale: 1.08, transformOrigin: "center center" },
  { scale: 1.12, duration: 160, ease: "none" },
  3.5
);
```
Mode-A entry tween unchanged: `masterTL.to(v, {left:1229, top:108, width:614, height:864, borderRadius:"6px", duration:0.7, ease:"expo.inOut"}, 3.0)`; `#bg-glow` fade-in @3.3, `#zone-rule` draw @3.4.

---

## STRUCTURE / TEMPLATE VOCABULARY (RULE 2 — varied, not formulaic)

LEAD DEVICE = **the productivity stat: 2–3 analysts → 1 trader.** The clip OPENS on the stat reveal (word-synced to the number), not on the generic swiss-grid index/eyebrow grid.

Template sequence (13 beats, no adjacent repeat, no two siblings alike):

`stat-count → clean → kinetic → kinetic+tag-chips → swiss-grid(before/after) → clean → flowchart → kinetic → host-Q kinetic → swiss-grid(front/back split) → bulleted liquid-glass → kinetic(standout) → liquid-glass(risk metrics) → clean-close`

- **Full-frame beats** (both speakers, dark gradient backdrop on the left): c8b1, c8b3, c8b8, c8b9 (host-Q), c8b12.
- **Mode-A beats:** c8b2 (clean), c8b4, c8b5, c8b6 (clean), c8b7, c8b10, c8b11, c8b13, c8b14 (clean close).
- **Real catalog blocks to install** (vary the look vs hand-built cards): `data-chart` (the count-stat numeral + the risk-metrics bars), `flowchart` (talk-to-terminal pipeline), `shimmer-sweep` (one AI-accent sweep across the stat numeral on c8b1). `npx hyperframes add data-chart flowchart shimmer-sweep`. Kinetic word-stacks use the project's existing kinetic-type pattern. Liquid-glass cards use the DESIGN.md no-blur recipe.

### Opening density (DESIGN.md "3+ element types before 6s", D1)
c8b1 satisfies it WITHOUT the swiss-grid grid: (1) eyebrow "REQUIRES A TEAM OF" slams @3.44 → (2) cyan rule draws under it @3.6 → (3) the big count numeral resolves to "2–3" @4.80→6.48 → (4) subscript label "ANALYSTS" + shimmer-sweep across the numeral @6.5. Speaker framed full-frame (both visible) the whole time; video shrinks to Mode A at the c8b2 boundary (comp 7.0). Three+ distinct element TYPES, none of them the recycled `0N / EYEBROW` chrome.

---

## CYAN DISCIPLINE (D7 — one `#00D4FF` element per beat)
c8b1 numeral "2–3" · c8b3 payoff line · c8b4 payoff line · c8b5 RIGHT column "1 TRADER + AI" value · c8b7 final node · c8b8 payoff line · c8b9 host-Q has NO cyan (white question) · c8b10 RIGHT header "BACK END" rule · c8b11 accent bar · c8b12 payoff line "SHORT OIL" · c8b13 accent bar. Clean beats c8b2/c8b6/c8b14 — none.

---

# BEAT-BY-BEAT EDL

> Every kinetic SENTENCE line lists the **on-screen text**, the **transcript words it matches**, and its **comp_t** (read from clip8-words.txt re-based to src_in 1677.20). Editorial (non-word-synced) lines are marked `EDITORIAL`.

### c8b1 — STAT REVEAL: "2–3 ANALYSTS" (data-chart count numeral) · FULL-FRAME · **LEAD DEVICE**
- **comp:** 0.0 – 7.0s · **src:** 1677.20 – 1684.20
- **template/block:** `data-chart` numeral count + `shimmer-sweep` accent (init kinetic-type host) · **mode:** full-frame (both speakers, left dark-gradient backdrop) · **sub-comp:** `beat-c8b1-stat.html`
- **content & word-sync:**
  - Eyebrow `REQUIRES A TEAM OF` — Inter 700, 34px, `#F0F0F0`, slam-in @ comp **3.44** — matches spoken **"require"** (src 1680.64). *(Eyebrow is a label cueing the number; it lands as he says "would require a team of".)*
  - Cyan horizontal rule draws under eyebrow @ comp **3.6** (`scaleX 0→1`).
  - Big numeral counts/reveals to **`2–3`** — Inter 900, 200px, **cyan `#00D4FF`** + glow — number resolves @ comp **4.80** ("two", src 1682.00) and settles by comp **6.48** ("three", src 1683.68). Count animation runs 3.6→4.80, holds "2–3" 4.80→ then the "3" ticks in at 6.26–6.48 to mirror the verbal "two … to three".
  - Sub-label `ANALYSTS` — Inter 700, 36px, `#F0F0F0` — fades in @ comp **6.70** (matches **"people"**, src 1683.90).
  - `shimmer-sweep` runs once across the numeral @ comp **6.6** (AI premium accent).
  - **on-screen / transcript line:** the eyebrow+numeral together render the spoken claim **"the work which I'm doing today would require a team of two to three people"** — numeral synced to "two"(4.80) / "three"(6.48), label to "people"(6.70). **NOT editorial — the number lands on the spoken number.**
- **cyan:** the numeral "2–3" only.
- **data-start/data-duration:** start 0.0, duration 7.0 (covers 3.44→6.70 with ≥0.3s headroom; exits upward by ~6.8 as video shrinks at the c8b2 boundary).

### c8b2 — CLEAN VIDEO · Mode A
- **comp:** 7.0 – 12.0s · **src:** 1684.20 – 1689.20
- **template:** clean (no graphic). Video shrinks full-frame → Mode A @ comp 7.0; `#bg-glow`/`#zone-rule` settle. · **mode:** Mode A · **sub-comp:** —
- **content:** none. Jasper elaborates: "two very hard to do, three very hard working people at least to conduct the research." 5s breath.
- **cyan:** none.

### c8b3 — "RESEARCH + TRADING / ONE PERSON" (kinetic word-stack) · FULL-FRAME
- **comp:** 12.0 – 16.0s · **src:** 1689.20 – 1693.20
- **template:** kinetic-type (phrase build, lines STAY, no dim) · **mode:** full-frame · **sub-comp:** `beat-c8b3-one-person.html`
- **content & word-sync (lines build as phrases, all stay):**
  - Line 1 `I'M DOING RESEARCH` — comp **12.76** — white `#F0F0F0` — matches **"for"/"me… I'm doing research"** (src 1689.96 "for", "research" src 1691.26). Fire line on "for me" @ 12.76.
  - Line 2 `AND TRADING` — comp **14.48** — white `#F0F0F0` — matches **"and… I'm trading"** ("and" src 1691.68, "trading" src 1692.14 → comp 14.48/14.94).
  - Line 3 `ONE PERSON.` — comp **15.24** — **cyan `#00D4FF`** payoff — fires on **"So"** (src 1692.44) as the editorial cap of the two literal lines above. `EDITORIAL` (the words "one person" are the design summary of "I'm doing research and I'm trading"; lines 1–2 are verbatim, line 3 is the cyan summary cap). Mark `<!-- EDITORIAL: cyan summary cap; lines 1–2 are verbatim word-synced -->`.
- **cyan:** Line 3 "ONE PERSON."
- **data-start/data-duration:** start 12.0, duration 4.0 (12.76→15.24; exits ~15.8).

### c8b4 — "IT COLLAPSES THE GRAFT WORK" + tag chips (kinetic + tag-chips) · Mode A
- **comp:** 16.0 – 25.0s · **src:** 1693.20 – 1702.20
- **template:** kinetic line + 2 staggered tag-chips (a DISTINCT layout — not swiss-grid, not a card) · **mode:** Mode A · **sub-comp:** `beat-c8b4-collapse.html`
- **content & word-sync:**
  - Kinetic line `IT COLLAPSES THE` / `LONGER-DURATION GRAFT WORK` (2-line, white `#F0F0F0`) — line 1 @ comp **17.46** (matches **"completely collapses"**, "completely" src 1694.66 → 17.46), line 2 @ comp **19.72** (matches **"longer"**, src 1696.92 → 19.72; "graft work" src 1698.32–1698.74).
  - Tag chip 1 `ANALYSIS` — fades/slides in @ comp **23.06** — matches **"analysis"** (src 1700.26).
  - Tag chip 2 `DATA GATHERING` — @ comp **23.88** — matches **"data"** (src 1701.08) / "gathering" (src 1702.14). The two chips are the cyan-bordered pills; ONE of them (DATA GATHERING) carries no cyan fill — keep chips `#F0F0F0` text on `rgba(20,26,34,0.92)`, cyan reserved for nothing here → **make the kinetic line's last word "GRAFT WORK" the cyan accent** instead (one cyan element). Move cyan to "GRAFT WORK".
  - **Revised cyan:** word "GRAFT WORK" in line 2 is **cyan `#00D4FF`**; chips stay `#F0F0F0`.
- **cyan:** "GRAFT WORK" (line 2 accent word).
- **data-start/data-duration:** start 16.0, duration 9.0 (17.46→23.88; exits ~24.8).

### c8b5 — BEFORE/AFTER: "NIGHT & DAY vs 5 YEARS AGO" (swiss-grid two-column) · Mode A
- **comp:** 26.0 – 33.0s · **src:** 1703.20 – 1710.20
- **template:** swiss-grid two-column (before/after) — the productivity comparison, anchored to the spoken "five years ago" · **mode:** Mode A · **sub-comp:** `beat-c8b5-before-after.html`
- **content & word-sync:**
  - Eyebrow `NIGHT & DAY vs 5 YEARS AGO` — Inter 700, 34px, `#F0F0F0` — slam @ comp **27.68** — matches **"night"** (src 1704.88; "night and day difference… vs how I used to work five years ago").
  - LEFT column header `5 YEARS AGO` (Inter 700, 48px, `#888888` permitted ≥48px) · value `2–3 ANALYSTS` (`#FF4D4F`).
  - Cyan rule / `→` arrow between columns draws @ comp **28.90** (matches **"difference"**, src 1706.10).
  - RIGHT column header `TODAY` (Inter 700, 48px, `#888888`) · value **`1 TRADER + AI`** (**cyan `#00D4FF`** — the single accent).
  - Footer `same research output` (`#F0F0F0`, 28px) @ comp **30.52** (matches **"five years ago"**, "five" src 1707.72 / "work" src 1707.54).
- **cyan:** RIGHT value "1 TRADER + AI".
- **note (D7 date language):** "5 YEARS AGO" / "TODAY" relative — Jasper literally says "five years ago" (src 1707.72), so the comparison is in-clip and verbatim-anchored. No absolute 2021/2026 labels needed.
- **data-start/data-duration:** start 26.0, duration 7.0 (27.68→30.52; holds to ~32.6, exits as c8b6 clean begins).

### c8b6 — CLEAN VIDEO · Mode A
- **comp:** 33.0 – 45.0s · **src:** 1710.20 – 1722.20
- **template:** clean (no graphic) · **mode:** Mode A · **sub-comp:** —
- **content:** none. Substantive window — Jasper: "in terms of trading with AI… now you can pretty much do any bots or any trading application yourself, basically with AI." 12s; acceptable on a 167.8s clip and it's a genuine breather between the before/after stat and the terminal-flow block.
- **cyan:** none.

### c8b7 — TALK-TO-TERMINAL PIPELINE (flowchart) · Mode A
- **comp:** 45.0 – 69.0s · **src:** 1722.20 – 1746.20
- **template:** `flowchart` (catalog block — animated nodes + SVG connectors; distinct from the kinetic/card vocabulary) · **mode:** Mode A · **sub-comp:** `beat-c8b7-terminal-flow.html`
- **content & word-sync (nodes pop `back.out(1.5)` on the spoken beats):**
  - Eyebrow `REVAMPING THE TRADING EXPERIENCE` — slam @ comp **51.00** — matches **"revamping"** (src 1728.20).
  - Node 1 `[ State your market view ]` — pop @ comp **54.32** — matches **"books"/"charts"→"talk to a terminal"** ("books" src 1731.52 → 54.32; "here is my view about the market" src 1735.70/1736.18).
  - Node 2 `[ Talk to a terminal ]` — pop @ comp **57.04** — matches **"terminal"** (src 1734.24).
  - Node 3 `[ Embedded in exchange ]` — pop @ comp **62.90** — matches **"embedding this into our exchange product"** ("embedding" src 1740.10 → 62.90).
  - Node 4 `[ + Paradigm "dime" terminal ]` — **cyan `#00D4FF`** final node — pop @ comp **65.54** — matches **"paradigm"** (src 1742.74 → 65.54; "as a dime terminal… unified experience" src 1743.72–1745.58).
  - Sublabel `"Here is my view about the market" → unified experience` (`#F0F0F0`, 24px).
- **cyan:** final node "+ Paradigm" only.
- **data-start/data-duration:** start 45.0, duration 24.0 (51.00→65.54; tree holds to ~68.6). This is the clip's flow beat — a long but ACTIVE hold (4 nodes popping across the span, not a static card).

### c8b8 — "IT KNOWS YOUR PROFILE / THE EXCHANGE / HOW TO ROUTE YOUR TRADE" (kinetic) · FULL-FRAME
- **comp:** 69.0 – 74.0s · **src:** 1746.20 – 1751.20
- **template:** kinetic-type (3-line phrase build, lines STAY) · **mode:** full-frame · **sub-comp:** `beat-c8b8-knows.html`
- **content & word-sync (verbatim, tightly synced):**
  - Line 1 `IT KNOWS YOUR PROFILE` — comp **70.40** — matches **"it knows your profile"** ("knows" src 1747.60, "profile" src 1747.90 → 70.40/70.70).
  - Line 2 `IT KNOWS THE EXCHANGE` — comp **71.28** — matches **"it knows the exchange"** (src 1748.48/1748.72).
  - Line 3 `IT KNOWS HOW TO ROUTE YOUR TRADE` — comp **72.94** — **cyan `#00D4FF`** payoff — matches **"it knows how to route your trade"** ("route" src 1750.14 → 72.94, "trade" src 1750.46 → 73.26).
- **cyan:** Line 3 (the "route your trade" payoff).
- **data-start/data-duration:** start 69.0, duration 5.0 (70.40→72.94; exits ~73.8).

### c8b9 — HOST QUESTION: "ARE THESE THEMATICS YOU'RE EXPLORING?" (kinetic, no HOST label) · FULL-FRAME
- **comp:** 74.0 – 79.0s · **src:** 1751.20 – 1756.20
- **template:** kinetic-type host-question (left-zone text, no "HOST" label per DESIGN.md) · **mode:** full-frame (Nic speaking LEFT, Jasper listening RIGHT — confirmed `/tmp/hostq_c8.png`) · **sub-comp:** `beat-c8b9-host-q.html`
- **content & word-sync:**
  - Line 1 `ARE THESE THEMATICS` — comp **74.72** — matches **"these thematics"** ("these" src 1751.92, "thematics" src 1752.06 → 74.72/74.86).
  - Line 2 `YOU'RE EXPLORING?` — comp **75.74** — matches **"you guys are exploring these days"** ("exploring" src 1752.94 → 75.74).
- **cyan:** NONE (host question rendered all-white `#F0F0F0`; reserves cyan for the guest's answer beats). This is a deliberate variation — the only beat with no cyan element by design.
- **data-start/data-duration:** start 74.0, duration 5.0 (74.72→75.74; exits ~78.6, just before Jasper answers at 79.02).

### c8b10 — FRONT-END vs BACK-END (swiss-grid two-column split) · Mode A
- **comp:** 79.0 – 102.0s · **src:** 1756.20 – 1779.20
- **template:** swiss-grid two-column — the structural "you guys = front end / us = back end" split · **mode:** Mode A · **sub-comp:** `beat-c8b10-front-back.html`
- **content & word-sync (two columns reveal as he names each side):**
  - Eyebrow `WHERE AI FITS` — Inter 700, 34px, `#F0F0F0` — slam @ comp **80.24** (matches **"I think it's a very interesting one"**, "think" src 1757.44 → 80.24).
  - LEFT column header `FRONT END` (Inter 700, 48px, `#888888`) reveals @ comp **81.72** (matches **"on the front end"**, src 1758.92 → 81.72) · body `Intent · actions of risk` (`#F0F0F0`, 26px) @ comp **82.58** (matches **"intent"**, src 1759.78). Footnote `(you guys)` `#888888` 48px-context — keep ≥32px `#F0F0F0`: render as `YOU GUYS` 32px `#F0F0F0`.
  - RIGHT column header `BACK END` (Inter 700, 48px, `#888888`) reveals @ comp **97.60** (matches **"on the back end"**, "back" src 1774.80 / "end" src 1775.08 → 97.60) · body `Market infrastructure` (`#F0F0F0`, 26px) @ comp **98.46** (matches **"market infrastructure"**, src 1775.66/1775.98). Footnote `US` (Wintermute) `#F0F0F0` 32px @ comp **94.08** (matches **"For us"**, src 1771.28).
  - Cyan vertical rule between the two columns draws @ comp **97.8** — **cyan `#00D4FF`** (the single accent; both column values stay `#F0F0F0`/grey).
- **cyan:** the divider rule between FRONT END / BACK END only.
- **note:** This is the structural payoff of his "for you guys that's front end… for us where we'd explore AI is back end / market infrastructure." Two-column reveal is staggered ~16s apart (front @81.7, back @97.6) so the column literally fills in as he contrasts the two sides — an ACTIVE 23s hold, not a static grid. Replaces v1's generic opening swiss-grid (moved here, late, where it's earned).
- **data-start/data-duration:** start 79.0, duration 23.0 (80.24→98.46; rule @97.8; holds to ~101.6).

### c8b11 — "ANALYSIS IS THE BIGGEST FIT" (bulleted liquid-glass card) · Mode A
- **comp:** 102.0 – 116.0s · **src:** 1779.20 – 1793.20
- **template:** liquid-glass card with 3 staggered bullet rows (DESIGN.md no-blur recipe) — distinct from the swiss-grid before it · **mode:** Mode A · **sub-comp:** `beat-c8b11-analysis-fit.html`
- **content & word-sync (rows stagger ~0.5s; payoff last):**
  - Eyebrow `BACK-END USE CASES` — Inter 700, 34px, `#F0F0F0` — @ comp **100.84** (matches **"can we do quick law analysis"**, "can" src 1778.04 → 100.84).
  - Bullet 1 `Quick "law" analysis` (`#F0F0F0`, 30px, ≥600) @ comp **101.82** (matches **"analysis"**, src 1779.02 → 101.82).
  - Bullet 2 `What trades to do` @ comp **105.66** (matches **"trades"**, src 1782.86 → 105.66).
  - Bullet 3 `Make / take fees` @ comp **108.36** (matches **"make or take fees"**, "make" src 1785.28 / "fees" src 1785.86 → 108.36/108.66).
  - Payoff strip `→ BIGGEST FIT FOR AI` @ comp **115.48** (matches **"biggest"**, src 1792.68 → 115.48; "fits" src 1793.02).
- **cyan:** 4px **cyan `#00D4FF`** left accent bar only.
- **card CSS:** `rgba(20,26,34,0.92)` + 4px cyan bar + soft glow + 1px border + `mask-image` right-feather. **NO `backdrop-filter`. NO grain.**
- **data-start/data-duration:** start 102.0, duration 14.0 (100.84→115.48; bullets staggered across the span; holds to ~115.6).

### c8b12 — "BLUE WAVE / STRAIT OF HORMUZ / SHORT OIL" (kinetic word-stack) · FULL-FRAME · **STANDOUT**
- **comp:** 116.5 – 139.0s · **src:** 1793.70 – 1816.20
- **template:** kinetic-type (phrase build, lines STAY) — the clip's dramatic centerpiece (the vivid agent-reasoning example) · **mode:** full-frame · **sub-comp:** `beat-c8b12-blue-wave.html`
- **content & word-sync (all verbatim):**
  - Lead-in line `INTENT-BASED TRADING NEEDS:` — comp **116.92** — matches **"intent based trading"** ("intent" src 1794.12 → 116.92). White `#F0F0F0`, smaller (60px) eyebrow-weight lead.
  - Line 1 `BLUE WAVE` — comp **130.50** — matches **"blue wave"** ("blue" src 1807.70 → 130.50). 130px.
  - Line 2 `STRAIT OF HORMUZ` — comp **134.24** — matches **"the Strait of Hormuz"** ("Strait" src 1811.44 → 134.24). 130px.
  - Line 3 `SHORT OIL` — comp **138.48** — **cyan `#00D4FF`** payoff — matches **"potentially short oil"** ("short" src 1815.68 → 138.48; "oil" src 1816.12). 130px.
- **cyan:** Line 3 "SHORT OIL".
- **note:** Between the lead-in (116.92) and "BLUE WAVE" (130.50) there is a ~13s gap during which Jasper says "you need a lot of infrastructure and high-quality data… to allow agents to express risk. Like, let's say…". Hold the lead-in line on screen (it stays), and bring in a **mid-line** to fill the gap: `+ INFRASTRUCTURE & HIGH-QUALITY DATA` @ comp **120.10** (matches **"infrastructure"**, src 1797.30 → 120.10) and `TO LET AGENTS EXPRESS RISK` @ comp **126.36** (matches **"express"**, src 1803.56 → 126.36) — both white, then they drift up/out by ~129 to clear the stage for the BLUE WAVE / HORMUZ / SHORT OIL slam. So the beat has two phases: (a) 116.92–129 the "needs infrastructure + data → agents express risk" build, (b) 130.50–138.48 the BLUE WAVE example slam. Both phases verbatim word-synced.
- **data-start/data-duration:** start 116.5, duration 22.5 (covers 116.92→138.48; phase-a lines exit ~129, phase-b slams 130.5→138.5, full stack exits ~138.8).
- **VERIFICATION:** corrects v1's catastrophic mis-timing (v1 fired BLUE WAVE at comp 132.70 under the OLD base — now re-derived to **130.50** under src_in 1677.20: "blue" src 1807.70 − 1677.20 = 130.50 ✓; "Strait" 1811.44 − 1677.20 = 134.24 ✓; "short" 1815.68 − 1677.20 = 138.48 ✓).

### c8b13 — RISK METRICS: "BETA · MAX DRAWDOWN" (liquid-glass / data-chart) · Mode A
- **comp:** 139.0 – 165.0s · **src:** 1816.20 – 1842.20
- **template:** liquid-glass card with a small `data-chart` mini-bar row (risk data points) · **mode:** Mode A · **sub-comp:** `beat-c8b13-risk-metrics.html`
- **content & word-sync (rows stagger):**
  - Eyebrow `AGENTS MUST CONTROL RISK` — Inter 700, 34px, `#F0F0F0` — @ comp **151.14** (matches **"an agent also needs to be able to control risk"**, "control" src 1828.34 → 151.14). *(There is a long clean stretch 139–151 — Jasper: "couple of industries you'd go long or short on in the US depending on policy" — left as a video breather; the card fires when he pivots to the risk-control point.)*
  - Data row 1 `BETA` — @ comp **155.44** (matches **"beta"**, src 1832.64 → 155.44).
  - Data row 2 `MAX DRAWDOWN` — @ comp **157.40** (matches **"max drawdown"**, "max" src 1834.60 → 157.40).
  - Payoff line `…across the ENTIRE INVESTABLE UNIVERSE` — @ comp **161.98** (matches **"entire investable universe"**, "entire" src 1839.18 → 161.98). The phrase "entire investable universe" gets weight.
- **cyan:** 4px **cyan `#00D4FF`** left accent bar only.
- **card CSS:** same no-blur liquid-glass recipe as c8b11.
- **D4 note:** This card is placed MID/LATE on a natural risk-profile beat and **EXITS (fades) by ~164.6** — it does NOT hold to the clip end. The clip closes on clean video (c8b14). No outro / no name-card-as-closer.
- **data-start/data-duration:** start 139.0, duration 26.0 (151.14→161.98; eyebrow holds from 151, rows stagger 155–158, payoff 161.98; fades ~164.6).

### c8b14 — CLEAN VIDEO (close) · Mode A
- **comp:** 165.0 – 167.8s · **src:** 1842.20 – 1845.00
- **template:** clean (no graphic) · **mode:** Mode A · **sub-comp:** —
- **content:** none. Card has faded. Jasper: "I think it makes a lot of sense. I don't think we're that far off…" Clip ends on conversation, NOT a held card (D4). 2.8s clean tail.
- **cyan:** none.

---

## FINAL BEAT MAP

| Beat | comp | src | template / block | speaker mode | sub-comp | cyan |
|------|------|-----|------------------|--------------|----------|------|
| c8b1 | 0.0–7.0 | 1677.20–1684.20 | data-chart count + shimmer-sweep (LEAD STAT) | full-frame | beat-c8b1-stat.html | numeral "2–3" |
| c8b2 | 7.0–12.0 | 1684.20–1689.20 | clean | Mode A | — | — |
| c8b3 | 12.0–16.0 | 1689.20–1693.20 | kinetic word-stack | full-frame | beat-c8b3-one-person.html | "ONE PERSON." |
| c8b4 | 16.0–25.0 | 1693.20–1702.20 | kinetic + tag-chips | Mode A | beat-c8b4-collapse.html | "GRAFT WORK" |
| c8b5 | 26.0–33.0 | 1703.20–1710.20 | swiss-grid before/after | Mode A | beat-c8b5-before-after.html | "1 TRADER + AI" |
| c8b6 | 33.0–45.0 | 1710.20–1722.20 | clean | Mode A | — | — |
| c8b7 | 45.0–69.0 | 1722.20–1746.20 | flowchart | Mode A | beat-c8b7-terminal-flow.html | "+ Paradigm" node |
| c8b8 | 69.0–74.0 | 1746.20–1751.20 | kinetic word-stack | full-frame | beat-c8b8-knows.html | "ROUTE YOUR TRADE" line |
| c8b9 | 74.0–79.0 | 1751.20–1756.20 | kinetic host-Q (no label) | full-frame | beat-c8b9-host-q.html | NONE (by design) |
| c8b10 | 79.0–102.0 | 1756.20–1779.20 | swiss-grid front/back split | Mode A | beat-c8b10-front-back.html | divider rule |
| c8b11 | 102.0–116.0 | 1779.20–1793.20 | bulleted liquid-glass | Mode A | beat-c8b11-analysis-fit.html | accent bar |
| c8b12 | 116.5–139.0 | 1793.70–1816.20 | kinetic word-stack (STANDOUT) | full-frame | beat-c8b12-blue-wave.html | "SHORT OIL" line |
| c8b13 | 139.0–165.0 | 1816.20–1842.20 | liquid-glass + data-chart (risk) | Mode A | beat-c8b13-risk-metrics.html | accent bar |
| c8b14 | 165.0–167.8 | 1842.20–1845.00 | clean (close) | Mode A | — | — |

Template sequence: stat-count → clean → kinetic → kinetic/tag → swiss-grid → clean → flowchart → kinetic → host-Q → swiss-grid → liquid-glass → kinetic → liquid-glass → clean. **No two adjacent beats identical.** 14 beats for a 167.8s clip (≥8 required).

---

## WORD-SYNC AUDIT (every non-editorial kinetic line — verified against clip8-words.txt, re-based to src_in 1677.20)

| beat·line | on-screen text | transcript words | src | comp (src−1677.20) |
|---|---|---|---|---|
| c8b1 numeral | `2–3` | "two" … "three" | 1682.00 / 1683.68 | **4.80 / 6.48** |
| c8b1 label | `ANALYSTS` | "people" | 1683.90 | **6.70** |
| c8b3 L1 | `I'M DOING RESEARCH` | "for me… research" | 1689.96 / 1691.26 | **12.76** |
| c8b3 L2 | `AND TRADING` | "and… trading" | 1691.68 / 1692.14 | **14.48 / 14.94** |
| c8b3 L3 | `ONE PERSON.` | (EDITORIAL cyan cap on "So" 1692.44) | 1692.44 | **15.24** |
| c8b4 L1 | `IT COLLAPSES THE` | "completely collapses" | 1694.66 | **17.46** |
| c8b4 L2 | `LONGER-DURATION GRAFT WORK` | "longer… graft work" | 1696.92 / 1698.32 | **19.72** |
| c8b4 chip1 | `ANALYSIS` | "analysis" | 1700.26 | **23.06** |
| c8b4 chip2 | `DATA GATHERING` | "data… gathering" | 1701.08 / 1702.14 | **23.88** |
| c8b5 eyebrow | `NIGHT & DAY vs 5 YEARS AGO` | "night and day difference" | 1704.88 | **27.68** |
| c8b5 footer | `same research output` | "five years ago" | 1707.72 | **30.52** |
| c8b7 eyebrow | `REVAMPING THE TRADING EXPERIENCE` | "revamping" | 1728.20 | **51.00** |
| c8b7 node1 | `State your market view` | "books"→"my view about the market" | 1731.52 / 1735.70 | **54.32** |
| c8b7 node2 | `Talk to a terminal` | "terminal" | 1734.24 | **57.04** |
| c8b7 node3 | `Embedded in exchange` | "embedding… exchange" | 1740.10 | **62.90** |
| c8b7 node4 | `+ Paradigm "dime" terminal` | "paradigm" | 1742.74 | **65.54** |
| c8b8 L1 | `IT KNOWS YOUR PROFILE` | "it knows your profile" | 1747.60 / 1747.90 | **70.40 / 70.70** |
| c8b8 L2 | `IT KNOWS THE EXCHANGE` | "it knows the exchange" | 1748.48 / 1748.72 | **71.28** |
| c8b8 L3 | `…HOW TO ROUTE YOUR TRADE` | "route your trade" | 1750.14 / 1750.46 | **72.94 / 73.26** |
| c8b9 L1 | `ARE THESE THEMATICS` | "these thematics" | 1751.92 / 1752.06 | **74.72 / 74.86** |
| c8b9 L2 | `YOU'RE EXPLORING?` | "you guys are exploring" | 1752.94 | **75.74** |
| c8b10 eyebrow | `WHERE AI FITS` | "very interesting one" | 1757.44 | **80.24** |
| c8b10 L-hdr | `FRONT END` | "on the front end" | 1758.92 | **81.72** |
| c8b10 L-body | `Intent · actions of risk` | "intent" | 1759.78 | **82.58** |
| c8b10 US note | `US` | "For us" | 1771.28 | **94.08** |
| c8b10 R-hdr | `BACK END` | "on the back end" | 1774.80 / 1775.08 | **97.60** |
| c8b10 R-body | `Market infrastructure` | "market infrastructure" | 1775.66 / 1775.98 | **98.46** |
| c8b11 eyebrow | `BACK-END USE CASES` | "can we do quick law analysis" | 1778.04 | **100.84** |
| c8b11 b1 | `Quick "law" analysis` | "analysis" | 1779.02 | **101.82** |
| c8b11 b2 | `What trades to do` | "trades" | 1782.86 | **105.66** |
| c8b11 b3 | `Make / take fees` | "make or take fees" | 1785.28 / 1785.86 | **108.36 / 108.66** |
| c8b11 payoff | `→ BIGGEST FIT FOR AI` | "biggest… fits" | 1792.68 / 1793.02 | **115.48** |
| c8b12 lead | `INTENT-BASED TRADING NEEDS:` | "intent based trading" | 1794.12 | **116.92** |
| c8b12 mid1 | `+ INFRASTRUCTURE & HIGH-QUALITY DATA` | "infrastructure" | 1797.30 | **120.10** |
| c8b12 mid2 | `TO LET AGENTS EXPRESS RISK` | "agents… express risk" | 1802.52 / 1803.56 | **125.32 / 126.36** |
| c8b12 L1 | `BLUE WAVE` | "blue wave" | 1807.70 | **130.50** |
| c8b12 L2 | `STRAIT OF HORMUZ` | "the Strait of Hormuz" | 1811.44 | **134.24** |
| c8b12 L3 | `SHORT OIL` | "potentially short oil" | 1815.68 / 1816.12 | **138.48** |
| c8b13 eyebrow | `AGENTS MUST CONTROL RISK` | "control risk" | 1828.34 | **151.14** |
| c8b13 row1 | `BETA` | "beta" | 1832.64 | **155.44** |
| c8b13 row2 | `MAX DRAWDOWN` | "max drawdown" | 1834.60 | **157.40** |
| c8b13 payoff | `ENTIRE INVESTABLE UNIVERSE` | "entire investable universe" | 1839.18 | **161.98** |

**EDITORIAL (not word-synced) lines:** c8b3 L3 "ONE PERSON." (cyan summary cap on "So" 1692.44 — lines 1–2 above it ARE verbatim). Everything else above is verbatim word-synced. **No anticipatory hook** — the opening stat numeral lands on the spoken number.

---

## INDEX.HTML CHANGES REQUIRED (vs current v1 index.html)

1. **`data-media-start`** on `<video id="short_mag_cut">` and `<audio id="a-roll-audio">`: `1675` → **`1677.20`**.
2. **`data-duration`** on master-root, video, and audio: `170` → **`167.8`**.
3. **Ken-Burns base scale** in the `vid` fromTo: `1.0 → 1.04` becomes **`1.08 → 1.12`** (ceiling fix), duration `115` → `160`.
4. **Beat list** rebuilt to the 14 beats above (new sub-comp ids/srcs/durations). Update the **z-index:3 rule** to list every new overlay id: `#beat-c8b1, #beat-c8b3, #beat-c8b4, #beat-c8b5, #beat-c8b7, #beat-c8b8, #beat-c8b9, #beat-c8b10, #beat-c8b11, #beat-c8b12, #beat-c8b13` (clean beats c8b2/c8b6/c8b14 have no overlay). **CRITICAL: any overlay id missing from this rule renders behind the video.**
5. **Full-frame ⇄ Mode A GSAP** transitions at the new boundaries: shrink→Mode A @7.0; expand→full @ ~11.7 (for c8b3); shrink @ ~15.7 (c8b4); the c8b8/c8b9 full-frame block expands @ ~68.7 and returns to Mode A @ ~78.7; the c8b12 full-frame expands @ ~116.2 and returns to Mode A @ ~138.7. Mirror the `toFull(t,dur)` / `toModeA(t,dur)` + `[gr,zr]` opacity pattern already in v1 index.html, just at the new times.
6. **object-position stays `83% center`** (already correct in v1 CSS — do not change to 50/62%).

## BUILD MANIFEST ROW
`clip_8 | clip-8-ai-multiplier | 1677.20 | 1845.00 | kinetic-type,data-chart,flowchart,swiss-grid,liquid-glass,shimmer-sweep | 14 beats`
