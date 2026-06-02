# CLIP 8 — AI MULTIPLIER · EDL **v3** (BUILD-READY)

**clip_id:** clip_8 · **dir:** `clip-8-ai-multiplier` · **slug:** `clip-8-ai-multiplier`
**Init template:** kinetic-type (host) · **Source:** `source.mp4` (1920×1080, symlink → clip-2 master).
**src_in = 1677.20 · src_out = 1845.00 · duration = 167.80s · comp = src − 1677.20 · data-media-start = 1677.20**

> Timing note (load-bearing): `clip8-words.txt` is based `table_comp = src − 1675`. This EDL is based `comp = src − 1677.20`.
> **Every comp time below was read off the table and converted: `comp = table_comp − 2.20`.** Verified per beat in the WORD-SYNC AUDIT.

---

## WHY v3 (the round-3 rejections being fixed)

The v2 clips were rejected for: **(a)** view flip-flopping, **(b)** every clip looking like clip-2 (kinetic-heavy), **(c)** jargon errors on screen, **(d)** duplicate words, and — clip-8 specifically — **(e) incoherent content + an opening that "does not make sense."** This v3 fixes all of them:

1. **CONTENT / OPENING COHERENCE (R5) — the headline fix.** v2 opened with a bare data-chart numeral: eyebrow `REQUIRES A TEAM OF` + a dangling cyan `2–3` + sublabel `ANALYSTS`. The QA checklist flags exactly this shape (`REQUIRES A TEAM OF / 2–3`) as the canonical R5 FAIL — the cyan payoff was a dangling number, not a noun phrase, and the three pieces did not parse as one thought. **v3 reworks the open into a coherent kinetic phrase-build that reads top-to-bottom as a complete sentence and whose cyan payoff is a real noun phrase:** `THE WORK I DO TODAY` / `WOULD REQUIRE` / `A TEAM OF 2–3 ANALYSTS` (cyan). Word-synced to the line he actually speaks at the in-point.
2. **VIEW FLIP-FLOP (R1) — the ~11–16s twitch AND the S2→S3→S4 A-B-A.** v2 went **Mode-A(7–12, 5s) → full(12–16, 4s) → Mode-A(16+)** — two sub-8s segments and an A-B-A inside 9s. **v3 groups the two opening kinetics (the coherent open + the "one person" callback) into ONE sustained FULL-FRAME view 0→16s** (clean full-frame video holds between the two builds), then transitions to Mode A **once** at ~16s and holds Mode A to 69s. **The round-3 QA also caught a second A-B-A: S2(ModeA)→S3(full)→S4(ModeA) where S3 was only 10.0s — a ModeA→full→ModeA return inside 12s. v3 EXTENDS S3 (full-frame) to ~12.3s by moving the S3→S4 settle from `toModeA(78.7)` to `toModeA(81.0)`, so Mode-A is GONE 69.0→81.0 (≥12s).** Jasper resumes speaking at comp 79.02 ("Yeah, it is. I think it's a very interesting one on the front end"), so full-frame holds cleanly 79–81. Result: every segment ≥10s, **zero A-B-A inside 12s** (the nearest ModeA↔ModeA gap is now 12.0s). (See VIEW-TIMELINE table.)
3. **TEMPLATE VARIETY (R2) — stop looking like clip-2.** The clip is **not** kinetic-dominated. Of 13 beats, 5 are kinetic and they are interleaved with the clip's two DISTINCT primary devices — a **productivity comparison** (swiss-grid before/after: 2–3 analysts → 1 trader+AI) and an **agent-pipeline flow** (a `flowchart`/decision-tree of talk-to-terminal → routed trade) — plus a front/back split, two liquid-glass cards, and a host-Q. **Max 2 kinetic word-stacks in a row** anywhere.
4. **JARGON (R3) — every on-screen string mapped through `_JARGON.md`:**
   - **graft work → GRUNT WORK** (c8b4). The flagged "graft"/"graft work" Whisper artifact is corrected.
   - **"dime terminal" DROPPED** (c8b7 node 4). `_JARGON.md` marks "dime terminal" UNRESOLVED / avoid-on-screen → the node is just `+ Paradigm` (the spoken institutional-liquidity brand).
   - **"quick law analysis" REWORDED** (c8b11). "law" is an unconfirmed Whisper artifact (not in the glossary) → the card uses only the concrete, confirmed terms from the same sentence (trade types, make/take fees). No "law" on screen.
   - **Paradigm** spelled exactly (the brand list has Paradex; Jasper says "paradigm," the derivatives-liquidity network — kept verbatim, no garble).
5. **DUPLICATE WORDS (R4).** No notable word repeats across two text elements **within one beat**. Audited per beat below. Specifically reconciled the two known collisions: c8b5 eyebrow → `THE PRODUCTIVITY DELTA` (was `NIGHT-AND-DAY vs 5 YEARS AGO`, which duplicated the LEFT header `5 YEARS AGO`), and c8b7 node 1 → `State your thesis` (was `State your market view`, whose "view"/"market" duplicated the sublabel quote `"Here is my view about the market"`). Cross-beat, the word "analysis" still appears in both c8b4 chip1 (`ANALYSIS`) and c8b11 bullet1 (`Market analysis`) — R4 is WITHIN-beat so this is not a hard FAIL, but flagged here for honesty (the earlier v3 claim that "ANALYSIS appears once" was inaccurate; c8b5 carries `ANALYSTS`, not `ANALYSIS`).

---

## IN / OUT (unchanged from v2 — the dialog-matched open is kept)

| field | value | note |
|---|---|---|
| **src_in** | **1677.20** | the exact frame the money line begins: "I can tell you that I think the work which I'm doing today would require a team of two to three people…" (KEPT from v2 — this is the dialog-match the user said to keep) |
| **src_out** | **1845.00** | ends clean on "…I don't think we're that far off…" |
| **duration** | **167.80s** | |
| **comp formula** | **comp = src − 1677.20** | |
| **data-media-start** | **1677.20** | on `<video>` + `<audio>` |
| **data-duration** | **167.8** | master-root + video + audio |

**Opening-frame check (src 1677.20, `/tmp/c8v3_in_1677.png` — extracted + viewed):** hard side-by-side, both speakers visible; **Jasper mid-delivery (mouth open) framed in the right half, burned-in "Jasper De Maere / Wintermute" lower-third visible.** Full-frame kinetic open is valid — NOT "text on black." ✓ (R3 verify-by-frame, opening.)

---

## FRAMING (verified from real source frames — KEPT from v2)

**Source layout (viewed `/tmp/c8v3_in_1677.png`, `/tmp/c8v3_1690.png`, `/tmp/c8v3_hostq_1752.png`):** hard side-by-side. **Nic (host) LEFT half** ("Nic" tag bottom-left). **Jasper (guest, the subject) RIGHT half**, head center ≈ x1380, eyes ≈ 28–32% from top; burned-in **"Jasper De Maere / Wintermute"** lower-third at the bottom of his half (≈ x1000–1250). Host-Q frame (src 1752.5) confirms **Nic speaking left / Jasper listening right** — c8b9 full-frame host-Q is valid (both present).

**Mode-A geometry (clip-2 proven):** `{ left:1229, top:108, width:614, height:864, borderRadius:6px }`; `object-fit:cover` ⇒ cover-scale 0.80 ⇒ no vertical overflow.

### CHOSEN: `object-position: 83% center` + Ken-Burns base **scale 1.08 → 1.12**
- **83%** is the only horizontal position that BOTH centers Jasper AND keeps his burned-in name fully on-screen (90% truncates the name to "…sper De Maere" and adds dead wall; 50/62% center the seam/Nic — all WRONG). KEPT from v2.
- **Scale 1.08→1.12** closes the dead ceiling above his head (Mode A has zero vertical overflow, so a vertical `object-position` bias does nothing — the scale-up is the only ceiling fix). KEPT from v2.
- CSS in `index.html` (already correct in v2 `index.html`; do NOT change to 50/62%):
  ```css
  #short_mag_cut, #short_mag_cut_frame > img.__render_frame__, #short_mag_cut_frame > img.__preview_render_frame__ {
    object-fit: cover; object-position: 83% center;
  }
  ```
  ```js
  masterTL.fromTo(vid, { scale:1.08, transformOrigin:"center center" },
                       { scale:1.12, duration:160, ease:"none" }, 16.0);
  ```

---

## ⭐ VIEW-TIMELINE (proves R1 — no flip-flop, no A-B-A inside 12s)

The source is SIDE-BY-SIDE. Two views: **FULL-FRAME** (both speakers, dark gradient backdrop left for kinetics) and **MODE-A** (Jasper framed right 40%, graphic in left 60%). Consecutive graphic beats are GROUPED into one view so the frame never bounces.

| Segment | View | comp range | **Dwell** | Beats in segment | R1 check |
|---|---|---|---|---|---|
| S1 | **FULL-FRAME** | 0.0 – 16.0 | **16.0s** | c8b1 (open kinetic) · c8b2 (clean) · c8b3 (one-person kinetic) | intro+grouped open; 2 kinetics share the view ✓ |
| S2 | **MODE-A** | 16.0 – 69.0 | **53.0s** | c8b4 (kinetic+chips) · c8b5 (swiss before/after) · c8b6 (clean) · c8b7 (flowchart) | ≥8s ✓ |
| S3 | **FULL-FRAME** | 69.0 – 81.3 | **~12.3s** | c8b8 (kinetic) · c8b9 (host-Q kinetic) | ≥12s ✓; 2 kinetics share the view ✓ |
| S4 | **MODE-A** | 81.3 – 116.5 | **35.2s** | c8b10 (front/back split) · c8b11 (liquid-glass card) | ≥8s ✓ |
| S5 | **FULL-FRAME** | 116.5 – 139.0 | **22.5s** | c8b12 (BLUE WAVE standout kinetic) | ≥8s ✓ |
| S6 | **MODE-A** | 139.0 – 167.8 | **28.8s** | c8b13 (risk card) · c8b14 (clean close) | ≥8s ✓ |

**Proof (R1, no A-B-A inside 12s):** 6 segments. **Minimum dwell = ~12.3s** (S3), every other ≥16s — **none < 8s outside the 0–6s intro.** View sequence is `full → ModeA → full → ModeA → full → ModeA` — a clean alternation. The two distance checks the round-3 gate flagged:
- **full↔full** (S1, S3, S5): nearest pair is S3↔S5 = full gone 81.3→116.5 = **35.2s apart** (≫12s). ✓
- **ModeA↔ModeA** (S2, S4, S6): nearest pair is **S2→S3→S4 — Mode-A leaves at 69.0 (S2→S3 `toModeA` start at the c8b8 boundary) and does NOT return until 81.0 (S3→S4 `toModeA(81.0)`), a gap of exactly 12.0s.** This is the fix vs the round-3 FAIL (old S3 was 69.0–79.0 = 10.0s middle, a ModeA→full→ModeA inside 12s). Now ≥12s. ✓
**The v2 7–16s twitch (ModeA 5s → full 4s → ModeA) is eliminated** by grouping the two opening kinetics into one 16s full-frame view; the round-3 S2→S3→S4 A-B-A is eliminated by extending S3 to ~12.3s. ✓✓

> Boundary GSAP (mirror v2 `toFull`/`toModeA` helpers, retimed): **S1→S2** `toModeA(16.0, 0.6)` (the ONE early settle; Ken-Burns starts here) · **S2→S3** `toFull(68.7, 0.4)` · **S3→S4** `toModeA(81.0, 0.5)` (was 78.7 — pushed so Mode-A is gone ≥12s; full-frame holds through Jasper resuming at comp 79.02) · **S4→S5** `toFull(116.2, 0.4)` · **S5→S6** `toModeA(138.7, 0.5)`. **No transition exists in the 7–16s window** (that was the v2 bug); **no `toModeA` exists in the 69–81s window** (that fixes the round-3 S2→S3→S4 A-B-A).

---

## TEMPLATE VARIETY / DEVICE MAP (proves R2)

**PRIMARY DEVICES (this clip, per DESIGN.md):**
1. **Productivity comparison** — `swiss-grid` two-column before/after: **2–3 ANALYSTS → 1 TRADER + AI** (c8b5). This is the literal payoff of the open and the clip's thesis.
2. **Agent-pipeline flow** — `flowchart` / decision-tree: **state thesis → talk to a terminal → embedded in exchange → routed trade** (c8b7), with the "it knows your profile / the exchange / how to route your trade" kinetic (c8b8) as its verbal climax.

**Template sequence (13 beats — NO two adjacent identical; NOT kinetic-dominated):**

`kinetic(open) → clean → kinetic(one-person) → kinetic+chips → swiss-grid(before/after) → clean → flowchart → kinetic(it-knows) → host-Q kinetic → swiss-grid(front/back) → liquid-glass(bullets) → kinetic(BLUE WAVE) → liquid-glass(risk) → clean`

- **Kinetic word-stacks: 5 of 13** (c8b1, c8b3, c8b8, c8b9, c8b12) — NOT a stack of kinetics.
- **Max consecutive kinetic = 2:** c8b1→c8b3 (split by clean c8b2, same view) then swiss-grid; c8b8→c8b9 then swiss-grid. **Never 3 in a row.** ✓
- **Non-kinetic devices carry the narrative:** swiss-grid ×2, flowchart ×1, liquid-glass ×2, host-Q ×1.
- **Catalog blocks to install** (`npx hyperframes add data-chart flowchart shimmer-sweep`): `flowchart` (c8b7 talk-to-terminal pipeline — the clip's distinct device) · `data-chart` (c8b13 risk-metrics mini-bar row) · `shimmer-sweep` (ONE premium accent sweep across the cyan payoff line `A TEAM OF 2–3 ANALYSTS` on c8b1). **Hand-build:** kinetic word-stacks (project kinetic-type pattern), swiss-grid two-column (c8b5, c8b10), liquid-glass cards (c8b11; DESIGN.md no-blur recipe), tag-chips (c8b4).

**Opening density (DESIGN.md "3+ DIFFERENT element types before 6s"):** c8b1 fires (1) **index `08` + eyebrow `THE AI MULTIPLIER`** @ comp 0.08 → (2) **grey rule** draws @ 0.5 → (3) **kinetic line `THE WORK I DO TODAY`** @ 1.78 → (4) line `WOULD REQUIRE` @ 3.44 → (5) **cyan payoff line `A TEAM OF 2–3 ANALYSTS`** + `shimmer-sweep` @ 4.80→6.48 — four+ distinct element TYPES (index/eyebrow, rule, kinetic phrase build, cyan payoff w/ shimmer) over both speakers, full-frame. First text present by **t=0.08** (QA item 3 — no >1.5s cold-open). The dark left-gradient backdrop holds the text; video stays full-frame the whole intro and settles to Mode A once at 16.0. ✓

---

## CYAN DISCIPLINE (one `#00D4FF` element per beat)
c8b1 payoff line `A TEAM OF 2–3 ANALYSTS` · c8b3 payoff line `ONE PERSON.` · c8b4 accent word `GRUNT WORK` · c8b5 RIGHT value `1 TRADER + AI` · c8b7 final node `+ Paradigm` · c8b8 payoff line `…ROUTE YOUR TRADE` · c8b9 **NONE** (host-Q all-white, by design) · c8b10 divider rule · c8b11 accent bar · c8b12 payoff line `SHORT OIL` · c8b13 accent bar. Clean beats c8b2 / c8b6 / c8b14 — none.

---

# BEAT-BY-BEAT EDL

> Each kinetic SENTENCE line lists the **on-screen text**, the **transcript words it matches**, and its **comp_t** (read off `clip8-words.txt`, converted `comp = table_comp − 2.20`). Editorial lines are marked `EDITORIAL`.

### c8b1 — OPEN: "THE WORK I DO TODAY / WOULD REQUIRE / A TEAM OF 2–3 ANALYSTS" (kinetic phrase-build) · FULL-FRAME · **COHERENT OPEN (R5)**
- **comp:** 0.0 – 7.0s · **src:** 1677.20 – 1684.20
- **template/block:** kinetic-type phrase-build (lines slam in & STAY, no dim) + `shimmer-sweep` once across the cyan payoff line · **view:** FULL-FRAME (both speakers, dark left-gradient backdrop) · **sub-comp:** `beat-c8b1-open.html`
- **content & word-sync (reads top-to-bottom as ONE complete sentence):**
  - **Index + eyebrow (so first text lands by t≤0.3s — QA item 3):** monospace index `08` (JetBrains Mono, **24px, `#F0F0F0`** — NOT `#888888`/20px; per QA item 8 `#888888` is permitted only ≥48px and the 22px readable floor; cyan stays on the payoff line per D7, so the index is recolored to the light index tone rather than enlarged, top-left) + eyebrow `THE AI MULTIPLIER` (Inter 700, 32px, `#F0F0F0`, uppercase, 0.18em) slam in @ comp **0.08** (`EDITORIAL` — structural chrome, not word-synced). A **grey** (`#2A2A2A`, NOT cyan) rule draws under the eyebrow @ comp **0.5** — kept grey so the beat's single cyan element stays the payoff line (D7). This satisfies "first text by ~0.3s"; the kinetic sentence then builds on the spoken words below. `<!-- EDITORIAL: structural index+eyebrow @0.08 so text is present by 0.3s; the 3 sentence lines below are word-synced -->`
  - Line 1 `THE WORK I DO TODAY` — Inter 900, ~120px, white `#F0F0F0` — slam @ comp **1.78** — matches **"the work … today"** ("work" src 1678.98 → 1.78). STAYS.
  - Line 2 `WOULD REQUIRE` — Inter 900, ~120px, white `#F0F0F0` — slam @ comp **3.44** — matches **"would require"** ("require" src 1680.64 → 3.44). STAYS.
  - Line 3 `A TEAM OF 2–3 ANALYSTS` — Inter 900, ~120px, **cyan `#00D4FF`** + glow — slam @ comp **4.80** — matches **"a team of two…to three…people"** ("two" src 1682.00 → 4.80; the `2–3` resolves its "3" as he says "to three" src 1683.68 → 6.48; "people" src 1683.90 → 6.70 confirms the noun). `shimmer-sweep` runs once across THIS line @ comp **6.50** (AI-premium accent). STAYS. *(Editorial note: `ANALYSTS` is a light editorial substitution for the spoken "people" — he says "team of two to three people … to conduct the research"; "ANALYSTS" glosses the research role for coherence. Defensible noun-phrase payoff; not a verbatim word.)*
  - **Coherence (R5):** the three lines parse as the verbatim claim **"the work I do today would require a team of 2–3 [analysts]."** The cyan payoff is a **real noun phrase** (`A TEAM OF 2–3 ANALYSTS`), not a dangling number. He literally describes conducting research = analyst work; the noun lands on his "people"/"conduct the research." Lines 1–2 + the count are verbatim word-synced; `ANALYSTS` is the one light editorial gloss.
- **cyan:** Line 3 `A TEAM OF 2–3 ANALYSTS` (one element).
- **R4:** no word repeats across elements (WORK / REQUIRE / TEAM·ANALYSTS all distinct).
- **data-start / data-duration:** start 0.0, dur 7.0 (covers 1.78→6.70 with ≥0.3s headroom; stack stays full-opacity, drifts up/out by ~6.8 — but video does NOT shrink here; it holds full-frame for c8b2).

### c8b2 — CLEAN VIDEO · FULL-FRAME (grouped with c8b1/c8b3 — R1 fix)
- **comp:** 7.0 – 12.0s · **src:** 1684.20 – 1689.20
- **template:** clean (no graphic). **View stays FULL-FRAME — no transition** (this is the heart of the R1 fix: v2 shrank to Mode A here for 5s then re-expanded, the twitch). · **sub-comp:** —
- **content:** none. Jasper elaborates: "two very hard to do, three very hard working people at least to conduct the research." 5s breath, full-frame, both speakers.
- **cyan:** none.

### c8b3 — "I'M DOING RESEARCH / AND TRADING / ONE PERSON." (kinetic phrase-build) · FULL-FRAME
- **comp:** 12.0 – 16.0s · **src:** 1689.20 – 1693.20
- **template:** kinetic-type phrase-build (lines STAY) · **view:** FULL-FRAME (same view as c8b1/c8b2 — grouped) · **sub-comp:** `beat-c8b3-one-person.html`
- **content & word-sync:**
  - Line 1 `I'M DOING RESEARCH` — white `#F0F0F0` — @ comp **12.76** — matches **"for me … I'm doing research"** ("for" src 1689.96 → 12.76; "research" src 1691.26 → 14.06). Fire on "for me" @ 12.76.
  - Line 2 `AND TRADING` — white `#F0F0F0` — @ comp **14.48** — matches **"and … I'm trading"** ("and" src 1691.68 → 14.48; "trading" src 1692.14 → 14.94).
  - Line 3 `ONE PERSON.` — **cyan `#00D4FF`** payoff — @ comp **15.24** — fires on **"So"** (src 1692.44 → 15.24). `EDITORIAL` — the cyan summary cap of the two verbatim lines above ("research + trading, done by **one person**"). Lines 1–2 are verbatim word-synced; line 3 is the cyan editorial cap. *(Non-blocking note: the view begins shrinking to Mode-A at 16.0, ≤1s after this cyan payoff fires; during build, fire `ONE PERSON.` ~0.3s earlier or hold `toModeA` a hair so the payoff gets ≥1s dwell before the view change.)* `<!-- EDITORIAL: cyan summary cap; lines 1–2 verbatim word-synced -->`
- **cyan:** Line 3 `ONE PERSON.`
- **R4:** RESEARCH / TRADING / PERSON all distinct; no dup with c8b1 (different beat anyway).
- **data-start / data-duration:** start 12.0, dur 4.0 (12.76→15.24; exits ~15.8 as the view transitions to Mode A at 16.0 for c8b4).

### c8b4 — "IT COLLAPSES THE LONGER-DURATION GRUNT WORK" + tag chips (kinetic + chips) · MODE-A
- **comp:** 16.0 – 26.0s · **src:** 1693.20 – 1703.20
- **template:** 2-line kinetic + 2 staggered tag-chips (a DISTINCT layout — not swiss-grid, not a card) · **view:** MODE-A (S2 begins; `toModeA(16.0,0.6)` here — the ONE early settle) · **sub-comp:** `beat-c8b4-collapse.html`
- **content & word-sync:**
  - Kinetic line 1 `IT COLLAPSES THE` — white `#F0F0F0` — @ comp **17.46** — matches **"completely collapses"** ("completely" src 1694.66 → 17.46; "collapses" 1695.20 → 18.00).
  - Kinetic line 2 `LONGER-DURATION GRUNT WORK` — white with the last words **`GRUNT WORK` cyan `#00D4FF`** — @ comp **19.72** — matches **"longer duration grunt work"** ("longer" src 1696.92 → 19.72; the corrected term **GRUNT WORK** sits on src 1698.32–1698.74 → ~21.1). **R3: "graft work" → GRUNT WORK** (the flagged fix).
  - Tag chip 1 `ANALYSIS` — slides in @ comp **23.06** — matches **"analysis"** (src 1700.26 → 23.06).
  - Tag chip 2 `DATA GATHERING` — slides in @ comp **23.88** — matches **"data … gathering"** (src 1701.08 → 23.88). Chips = `#F0F0F0` text on `rgba(20,26,34,0.92)`, 1px border, NO cyan fill (cyan is on `GRUNT WORK`).
- **cyan:** `GRUNT WORK` (line-2 accent words — one element).
- **R4:** COLLAPSES / GRUNT WORK / ANALYSIS / DATA GATHERING all distinct words within the beat. ✓ *(Cross-beat note: chip `ANALYSIS` also echoes c8b11 bullet `Market analysis` — cross-beat, not an R4 within-beat FAIL, but consider varying one during build.)*
- **data-start / data-duration:** start 16.0, dur 10.0 (17.46→23.88; holds to ~25.6, exits as c8b5 enters).

### c8b5 — ⭐ PRODUCTIVITY COMPARISON: "5 YEARS AGO → TODAY" (swiss-grid two-column before/after) · MODE-A · **PRIMARY DEVICE 1**
- **comp:** 26.0 – 33.0s · **src:** 1703.20 – 1710.20
- **template:** swiss-grid two-column before/after — the thesis payoff (2–3 analysts → 1 trader+AI), anchored to his spoken "five years ago" · **view:** MODE-A (grouped with c8b4 — same view) · **sub-comp:** `beat-c8b5-before-after.html`
- **content & word-sync (left col → arrow → right col fills as he contrasts):**
  - **Eyebrow `THE PRODUCTIVITY DELTA`** — Inter 700, 34px, `#F0F0F0` — slam @ comp **27.68** — matches **"night [and day difference]"** (src 1704.88 → 27.68). **(R4 fix — was the old `NIGHT-AND-DAY vs 5 YEARS AGO`, which duplicated the LEFT header `5 YEARS AGO`; this binding eyebrow text removes the dup. On-screen eyebrow = `THE PRODUCTIVITY DELTA`.)**
  - LEFT column: header `5 YEARS AGO` (Inter 700, 48px, `#888888` — permitted ≥48px) · value `2–3 ANALYSTS` (Inter 800, ~64px, `#F0F0F0`).
  - Center `→` arrow / divider draws @ comp **28.90** — matches **"difference"** (src 1706.10 → 28.90).
  - RIGHT column: header `TODAY` (Inter 700, 48px, `#888888`) · value **`1 TRADER + AI`** (Inter 800, ~64px, **cyan `#00D4FF`** — the single accent).
  - Footer `same research output` (Inter 600, 28px, `#F0F0F0`) fades in @ comp **30.52** — matches **"five years ago"** ("five" src 1707.72 → 30.52; "work" 1707.54 → 30.34).
- **cyan:** RIGHT value `1 TRADER + AI`.
- **R4:** eyebrow `THE PRODUCTIVITY DELTA` vs LEFT header `5 YEARS AGO` vs RIGHT header `TODAY` vs values `2–3 ANALYSTS`/`1 TRADER + AI` vs footer `same research output` — **no shared notable word.** ✓ (The earlier eyebrow/`5 YEARS AGO` collision is resolved.)
- **date language:** "5 YEARS AGO"/"TODAY" are relative — he literally says "five years ago" — no absolute 2021/2026 labels (DESIGN.md date rule satisfied).
- **data-start / data-duration:** start 26.0, dur 7.0 (27.68→30.52; holds to ~32.6).

### c8b6 — CLEAN VIDEO · MODE-A
- **comp:** 33.0 – 45.0s · **src:** 1710.20 – 1722.20
- **template:** clean (no graphic) · **view:** MODE-A (grouped — no transition) · **sub-comp:** —
- **content:** none. Jasper: "in terms of trading with AI … now you can pretty much do any bots or any trading application yourself, basically with AI." 12s breather between the comparison and the pipeline (acceptable on a 167.8s clip; it's a genuine topic seam, not dead air).
- **cyan:** none.

### c8b7 — ⭐ AGENT PIPELINE: "TALK TO A TERMINAL" (flowchart / decision-tree) · MODE-A · **PRIMARY DEVICE 2**
- **comp:** 45.0 – 69.0s · **src:** 1722.20 – 1746.20
- **template:** `flowchart` catalog block — animated nodes + SVG connectors (the clip's distinct device; nothing else uses it) · **view:** MODE-A (grouped with c8b4/c8b5/c8b6 — S2 holds) · **sub-comp:** `beat-c8b7-terminal-flow.html`
- **content & word-sync (nodes pop `back.out(1.5)` on the spoken beat; arrows draw between):**
  - Eyebrow `REVAMPING THE TRADING STACK` — slam @ comp **51.00** — matches **"revamping"** (src 1728.20 → 51.00). **(R4 fix — was `REVAMPING THE TRADING EXPERIENCE`, whose "EXPERIENCE" duplicated the sublabel quote `"Here is my view about the market" → a unified experience`. The eyebrow is EDITORIAL chrome → reworded to `STACK` so "experience" lives ONLY in the verbatim sublabel. On-screen eyebrow = `REVAMPING THE TRADING STACK`; no word in {REVAMPING, TRADING, STACK} appears in the sublabel.)**
  - **Node 1 `[ State your thesis ]`** — pop @ comp **54.32** — matches **"instead of … books and charts → here is my view about the market"** ("books" src 1731.52 → 54.32; "view" 1735.70 → 58.50). **(R4 fix — was `State your market view`, whose "view"/"market" duplicated the sublabel quote `"Here is my view about the market"`; renamed so those notable words live in only one element. On-screen Node 1 = `State your thesis`.)**
  - Node 2 `[ Talk to a terminal ]` — pop @ comp **57.04** — matches **"talk to a terminal"** ("terminal" src 1734.24 → 57.04).
  - Node 3 `[ Embedded in the exchange ]` — pop @ comp **62.90** — matches **"embedding this into our exchange product"** ("embedding" src 1740.10 → 62.90).
  - Node 4 `[ + Paradigm ]` — **cyan `#00D4FF`** final node — pop @ comp **65.54** — matches **"into paradigm … a unified experience"** ("paradigm" src 1742.74 → 65.54; "unified" 1745.26 → 68.06). **R3: "dime terminal" DROPPED** — node is `+ Paradigm` only (the spoken brand; "dime terminal" is `_JARGON.md`-unresolved → not on screen).
  - Sublabel `"Here is my view about the market" → a unified experience` (Inter 600, 24px, `#F0F0F0`).
- **cyan:** final node `+ Paradigm`.
- **R4:** Eyebrow `REVAMPING THE TRADING STACK` (REVAMPING·TRADING·STACK) / Node 1 `State your thesis` (THESIS) / Node 2 `Talk to a terminal` (TERMINAL) / Node 3 `Embedded in the exchange` (EXCHANGE) / Node 4 `+ Paradigm` (PARADIGM) / sublabel `"Here is my view about the market" → a unified experience` (VIEW·MARKET·EXPERIENCE) — **all notable words distinct across elements.** The prior "view"/"market" Node1↔sublabel collision is removed AND the eyebrow↔sublabel "experience" collision (eyebrow was `…TRADING EXPERIENCE`) is removed — "experience" now lives in the verbatim sublabel only; the eyebrow carries `STACK`. ✓
- **note:** a LONG but ACTIVE 24s hold — 4 nodes pop across the span (not a static card). This is the clip's flow beat.
- **data-start / data-duration:** start 45.0, dur 24.0 (51.00→65.54; tree holds to ~68.6, exits as view goes full-frame at 68.7).

### c8b8 — "IT KNOWS YOUR PROFILE / IT KNOWS THE EXCHANGE / IT KNOWS HOW TO ROUTE YOUR TRADE" (kinetic) · FULL-FRAME
- **comp:** 69.0 – 74.0s · **src:** 1746.20 – 1751.20
- **template:** kinetic-type 3-line phrase-build (lines STAY) — the verbal climax of the pipeline · **view:** FULL-FRAME (S3 begins; `toFull(68.7,0.4)`) · **sub-comp:** `beat-c8b8-knows.html`
- **content & word-sync (verbatim, tight):**
  - Line 1 `IT KNOWS YOUR PROFILE` — white `#F0F0F0` — @ comp **70.40** — matches **"it knows your profile"** ("knows" src 1747.60 → 70.40; "profile" 1747.90 → 70.70).
  - Line 2 `IT KNOWS THE EXCHANGE` — white `#F0F0F0` — @ comp **71.52** — matches **"it knows the exchange"** ("exchange" src 1748.72 → 71.52).
  - Line 3 `IT KNOWS HOW TO ROUTE YOUR TRADE` — **cyan `#00D4FF`** payoff — @ comp **72.94** — matches **"it knows how to route your trade"** ("route" src 1750.14 → 72.94; "trade" 1750.46 → 73.26).
- **cyan:** Line 3 (the `…ROUTE YOUR TRADE` payoff).
- **R4:** "IT KNOWS" is an intentional anaphora (the spoken structure) — the *distinct* notable words are PROFILE / EXCHANGE / ROUTE YOUR TRADE; this is verbatim parallelism, not a dup-word violation (R4 targets eyebrow-vs-sublabel collisions, not deliberate rhetorical repetition within a single kinetic). ✓
- **data-start / data-duration:** start 69.0, dur 5.0 (70.40→72.94; exits ~73.8).

### c8b9 — HOST QUESTION: "ARE THESE THEMATICS YOU'RE EXPLORING?" (kinetic, no HOST label) · FULL-FRAME
- **comp:** 74.0 – 81.3s · **src:** 1751.20 – 1758.50
- **template:** kinetic-type host-question (left-zone text, NO "HOST" label per DESIGN.md) · **view:** FULL-FRAME (grouped with c8b8 — S3; holds through the gap AND Jasper resuming his answer at comp 79.02 — `toModeA` does NOT fire until 81.0, the R1 A-B-A fix; Nic speaking LEFT, Jasper listening RIGHT at the question — confirmed `/tmp/c8v3_hostq_1752.png`) · **sub-comp:** `beat-c8b9-host-q.html`
- **content & word-sync:**
  - Line 1 `ARE THESE THEMATICS` — white `#F0F0F0` — @ comp **74.72** — matches **"these thematics"** ("these" src 1751.92 → 74.72; "thematics" 1752.06 → 74.86).
  - Line 2 `YOU'RE EXPLORING?` — white `#F0F0F0` — @ comp **75.74** — matches **"you guys are exploring these days"** ("exploring" src 1752.94 → 75.74).
- **cyan:** **NONE by design** (host question all-white; reserves cyan for the guest's answer). The one deliberate no-cyan beat.
- **R4:** THEMATICS / EXPLORING distinct. ✓
- **note (R1):** the host-Q text exits ~76.2 (the question ends on "days?" at comp 76.18; src 1753.38 − 1677.20), opening a ~2.8s gap of silence 76.2→79.0, and the view HOLDS full-frame through Jasper's answer resuming at comp 79.02 ("Yeah, it is. I think it's a very interesting one on the front end"; "Yeah" src 1756.22 − 1677.20). The view settles to Mode-A at 81.0 (`toModeA(81.0,0.5)`), AFTER the answer has begun — so full-frame dwells 69.0→81.3 (~12.3s) and the ModeA↔ModeA gap is ≥12s. *(These are this EDL's comp = src − 1677.20; the earlier "78.4→81.2 / exits ~78.6" figures were TABLE_COMP numbers, src − 1675, in the wrong time base — corrected here.)*
- **data-start / data-duration:** start 74.0, dur 5.0 (74.72→75.74; text exits ~76.2 as the question ends on "days?" comp 76.18; the beat div may stay mounted to 81.3 but renders no text after exit — view holds full-frame).

### c8b10 — FRONT-END vs BACK-END (swiss-grid two-column split) · MODE-A
- **comp:** 81.3 – 102.0s · **src:** 1758.50 – 1779.20
- **template:** swiss-grid two-column — the structural "you guys = front end / us = back end" split (columns fill ~16s apart as he names each side) · **view:** MODE-A (S4 begins; `toModeA(81.0,0.5)` — pushed from 78.7 so Mode-A returns ≥12s after leaving at 69.0, the R1 A-B-A fix; the Mode-A frame is settled by ~81.5) · **sub-comp:** `beat-c8b10-front-back.html`
- **content & word-sync:**
  - LEFT column: header `FRONT END` (Inter 700, 48px, `#888888`) reveals @ comp **81.72** — matches **"on the front end"** ("front" src 1758.92 → 81.72) · body `Intent · expressing risk` (Inter 600, 26px, `#F0F0F0`) @ comp **82.58** — matches **"intent … of risk"** (src 1759.78 → 82.58) · role tag `YOU GUYS` (Inter 600, 32px, `#F0F0F0`).
  - **Eyebrow `WHERE AI FITS`** — Inter 700, 34px, `#F0F0F0` — slam @ comp **81.72** alongside the FRONT-END header reveal (re-anchored from the old comp 80.24 so it lands AFTER the Mode-A settle at 81.0 — the LEFT `FRONT END` header fires at this same 81.72 on "front", src 1758.92). The eyebrow is structural chrome here (`EDITORIAL`), landing as the column header appears.
  - Center divider rule draws @ comp **97.8** — **cyan `#00D4FF`** (the single accent; both column values stay `#F0F0F0`/grey).
  - RIGHT column: role tag `US (Wintermute)` (Inter 600, 32px, `#F0F0F0`) reveals @ comp **94.08** — matches **"For us"** (src 1771.28 → 94.08) · header `BACK END` (Inter 700, 48px, `#888888`) @ comp **97.60** — matches **"on the back end"** ("back" src 1774.80 / "end" 1775.08 → 97.60) · body `Market infrastructure` (Inter 600, 26px, `#F0F0F0`) @ comp **98.46** — matches **"market infrastructure"** (src 1775.66 → 98.46).
- **cyan:** the FRONT/BACK divider rule only.
- **R4:** eyebrow `WHERE AI FITS` vs columns `FRONT END`/`BACK END`/`Intent`/`Market infrastructure`/`YOU GUYS`/`US (Wintermute)` — all distinct (no shared notable word). ✓ (Cross-beat note: c8b11's payoff was reworded to `WHERE IT LANDS FIRST` (dropping "AI" to fix a c8b11 within-beat dup), so this eyebrow's "AI"/"FIT" no longer echoes it cross-beat — the `WHERE ___ ___` cadence is the only residual rhyme, which is fine.)
- **note:** staggered reveal (FRONT @81.7, BACK @97.6) so the column literally fills as he contrasts — an ACTIVE ~20s hold, not a static grid. The Mode-A settle (81.0) lands just before the FRONT reveal (81.72), so the graphic appears into a settled left zone — no empty Mode-A gap.
- **data-start / data-duration:** start 81.3, dur 20.7 (81.72→98.46; rule @97.8; holds to ~101.6).

### c8b11 — BACK-END USE CASES (bulleted liquid-glass card) · MODE-A
- **comp:** 102.0 – 116.5s · **src:** 1779.20 – 1793.70
- **template:** liquid-glass card, 3 staggered bullet rows + payoff strip (DESIGN.md no-blur recipe; distinct from the swiss-grid before it) · **view:** MODE-A (grouped with c8b10 — S4 holds) · **sub-comp:** `beat-c8b11-use-cases.html`
- **content & word-sync (rows stagger; payoff last):**
  - Eyebrow `WHAT AI HANDLES BACK-END` — Inter 700, 34px, `#F0F0F0` — @ comp **100.84** — matches **"can we do … analysis"** ("can" src 1778.04 → 100.84).
  - Bullet 1 `Market analysis` (Inter 600, 30px, `#F0F0F0`) @ comp **101.82** — matches **"analysis"** (src 1779.02 → 101.82). *(R3: the Whisper "quick law analysis" — "law" is an unconfirmed artifact, not in `_JARGON.md` → reworded to the confirmed "analysis"; no "law" on screen.)*
  - Bullet 2 `What trades to do` (Inter 600, 30px) @ comp **105.66** — matches **"what type of trades are there to do"** ("trades" src 1782.86 → 105.66).
  - Bullet 3 `Make / take fees` (Inter 600, 30px) @ comp **108.08** — matches **"make or take fees"** ("make" src 1785.28 → 108.08; "fees" 1785.86 → 108.66).
  - Payoff strip `→ WHERE IT LANDS FIRST` (Inter 700, 32px, `#F0F0F0`) @ comp **115.48** — matches **"the biggest fits"** ("biggest" src 1792.68 → 115.48; "fits" 1793.02 → 115.82). *(R4 fix — the payoff was `WHERE AI LANDS FIRST`, whose "AI" duplicated this beat's eyebrow `WHAT AI HANDLES BACK-END` WITHIN c8b11. Dropped "AI" from the payoff so the eyebrow carries the only "AI" in the beat → `WHERE IT LANDS FIRST`. Still deliberately NOT "biggest fit"/"WHERE AI FITS" — keeps the same meaning AND avoids the cross-beat echo of c8b10's eyebrow "WHERE AI FITS"/"FIT".)*
- **cyan:** 4px **cyan `#00D4FF`** left accent bar only.
- **R4 (within beat):** eyebrow `WHAT AI HANDLES BACK-END`, bullets `Market analysis`/`What trades to do`/`Make / take fees`, payoff `WHERE IT LANDS FIRST` — no shared notable word. ✓ **(R4 fix — the payoff was `WHERE AI LANDS FIRST`; its "AI" duplicated the eyebrow's "AI" WITHIN this beat, an R4 within-beat collision. Dropped "AI" from the payoff (`→ WHERE IT LANDS FIRST`) so "AI" appears in exactly one element — the eyebrow.)** *(Cross-beat note: `Market analysis` echoes c8b4 chip `ANALYSIS` — genuinely cross-beat, stylistically repetitive but not an R4 within-beat FAIL; consider varying during build.)*
- **card CSS:** `rgba(20,26,34,0.92)` + 4px cyan bar + soft glow + 1px border + `mask-image` right-feather. **NO `backdrop-filter`. NO grain.**
- **data-start / data-duration:** start 102.0, dur 14.5 (100.84→115.48; bullets stagger; holds to ~116.1, exits as view goes full-frame at 116.2).

### c8b12 — ⭐ STANDOUT: "BLUE WAVE / STRAIT OF HORMUZ / SHORT OIL" (kinetic phrase-build) · FULL-FRAME
- **comp:** 116.5 – 139.0s · **src:** 1793.70 – 1816.20
- **template:** kinetic-type phrase-build (lines STAY) — the clip's dramatic centerpiece (the vivid agent-reasoning example) · **view:** FULL-FRAME (S5; `toFull(116.2,0.4)`) · **sub-comp:** `beat-c8b12-blue-wave.html`
- **content & word-sync — TWO PHASES (both verbatim):**
  - **Phase A (the setup — fills the ~13s before the example):**
    - Lead `INTENT-BASED TRADING NEEDS:` — Inter 700, 60px, `#F0F0F0` — @ comp **116.92** — matches **"intent based trading"** ("intent" src 1794.12 → 116.92). STAYS through phase A.
    - Mid 1 `INFRASTRUCTURE & HIGH-QUALITY DATA` — Inter 800, ~90px, `#F0F0F0` — @ comp **120.10** — matches **"a lot of infrastructure and high quality data"** ("infrastructure" src 1797.30 → 120.10).
    - Mid 2 `TO LET AGENTS EXPRESS RISK` — Inter 800, ~90px, `#F0F0F0` — @ comp **126.36** — matches **"to be able to allow agents to express risk"** ("agents" src 1802.52 → 125.32; "express" 1803.56 → 126.36).
    - Phase-A lines drift up/out together by ~comp **129** to clear the stage.
  - **Phase B (the example slam — 130px):**
    - Line 1 `BLUE WAVE` — white `#F0F0F0` — @ comp **130.50** — matches **"a blue wave"** ("blue" src 1807.70 → 130.50; "wave" 1807.88 → 130.68).
    - Line 2 `STRAIT OF HORMUZ` — white `#F0F0F0` — @ comp **134.24** — matches **"the Strait of Hormuz"** ("Strait" src 1811.44 → 134.24; "Hormuz" 1812.06 → 134.86).
    - Line 3 `SHORT OIL` — **cyan `#00D4FF`** payoff — @ comp **138.48** — matches **"potentially short oil"** ("short" src 1815.68 → 138.48; "oil" 1816.12 → 138.92).
- **cyan:** Line 3 `SHORT OIL`.
- **R4:** all phase words distinct; no eyebrow/sublabel collision. ✓
- **note:** the beat has two phases so there is never a dead hold — Phase A builds the "needs infrastructure + data → agents express risk" thesis (116.92–129), Phase B slams the BLUE WAVE → HORMUZ → SHORT OIL example (130.5–138.5). All verbatim.
- **VERIFICATION (fixes v1's catastrophic mis-time):** re-derived under src_in 1677.20 — "blue" 1807.70 − 1677.20 = 130.50 ✓; "Strait" 1811.44 − 1677.20 = 134.24 ✓; "short" 1815.68 − 1677.20 = 138.48 ✓.
- **data-start / data-duration:** start 116.5, dur 22.5 (covers 116.92→138.48; phase-A exits ~129; phase-B 130.5→138.5; full stack exits ~138.8).

### c8b13 — RISK METRICS: "BETA · MAX DRAWDOWN" (liquid-glass + data-chart mini-bars) · MODE-A
- **comp:** 139.0 – 165.0s · **src:** 1816.20 – 1842.20
- **template:** liquid-glass card with a small `data-chart` mini-bar row (risk data points) · **view:** MODE-A (S6 begins; `toModeA(138.7,0.5)`) · **sub-comp:** `beat-c8b13-risk-metrics.html`
- **content & word-sync (rows stagger; long clean stretch 139–151 is a video breather while he says "couple of industries you'd go long/short on in the US depending on policy"):**
  - Eyebrow `AGENTS MUST CONTROL RISK` — Inter 700, 34px, `#F0F0F0` — @ comp **151.14** — matches **"an agent also needs to be able to control risk"** ("control" src 1828.34 → 151.14).
  - Data row 1 `BETA` (Inter 600, 30px, `#F0F0F0`) @ comp **155.44** — matches **"beta"** (src 1832.64 → 155.44).
  - Data row 2 `MAX DRAWDOWN` (Inter 600, 30px, `#F0F0F0`) @ comp **157.40** — matches **"max drawdown"** ("max" src 1834.60 → 157.40).
  - Payoff line `…ACROSS THE ENTIRE INVESTABLE UNIVERSE` (Inter 700, 32px, `#F0F0F0`) @ comp **161.98** — matches **"the entire investable universe"** ("entire" src 1839.18 → 161.98; "investable" 1839.54 → 162.34; "universe" 1840.08 → 162.88).
- **cyan:** 4px **cyan `#00D4FF`** left accent bar only.
- **R4:** CONTROL RISK / BETA / MAX DRAWDOWN / INVESTABLE UNIVERSE all distinct. ✓
- **card CSS:** same no-blur liquid-glass recipe as c8b11.
- **D4 (no-outro):** the card is placed on a natural risk-profile beat and **FADES by ~comp 164.6** — it does NOT hold to clip end. The clip closes on clean video (c8b14).
- **note (non-blocking):** Mode-A is held from 139.0 but the card eyebrow does not appear until 151.14 — ~12s of Mode-A with an empty left 60% zone. During build, consider holding full-frame 139→151 and switching to Mode-A at ~151 when the card appears (the S5→S6 `toModeA` would move from 138.7 to ~150.6). Non-blocking; leave the S6 boundary at 138.7 unless the build agent elects the later settle.
- **data-start / data-duration:** start 139.0, dur 26.0 (eyebrow @151.14; rows 155–158; payoff 161.98; fades ~164.6).

### c8b14 — CLEAN VIDEO (close) · MODE-A
- **comp:** 165.0 – 167.8s · **src:** 1842.20 – 1845.00
- **template:** clean (no graphic). Card has faded · **view:** MODE-A (grouped with c8b13 — S6 holds to clip end) · **sub-comp:** —
- **content:** none. Jasper: "I think it makes a lot of sense. I don't think we're that far off…" Clip ends on conversation, NOT a held card (D4 / no-outro). 2.8s clean tail.
- **cyan:** none.

---

## FINAL BEAT MAP

| Beat | comp | src | template / block | view | sub-comp | cyan |
|------|------|-----|------------------|------|----------|------|
| c8b1 | 0.0–7.0 | 1677.20–1684.20 | kinetic phrase-build + shimmer-sweep (**COHERENT OPEN**) | full-frame | beat-c8b1-open.html | line `A TEAM OF 2–3 ANALYSTS` |
| c8b2 | 7.0–12.0 | 1684.20–1689.20 | clean | full-frame | — | — |
| c8b3 | 12.0–16.0 | 1689.20–1693.20 | kinetic phrase-build | full-frame | beat-c8b3-one-person.html | line `ONE PERSON.` |
| c8b4 | 16.0–26.0 | 1693.20–1703.20 | kinetic + tag-chips | Mode-A | beat-c8b4-collapse.html | `GRUNT WORK` |
| c8b5 | 26.0–33.0 | 1703.20–1710.20 | swiss-grid before/after (**DEVICE 1**) | Mode-A | beat-c8b5-before-after.html | `1 TRADER + AI` |
| c8b6 | 33.0–45.0 | 1710.20–1722.20 | clean | Mode-A | — | — |
| c8b7 | 45.0–69.0 | 1722.20–1746.20 | flowchart (**DEVICE 2**) | Mode-A | beat-c8b7-terminal-flow.html | `+ Paradigm` node |
| c8b8 | 69.0–74.0 | 1746.20–1751.20 | kinetic phrase-build | full-frame | beat-c8b8-knows.html | `…ROUTE YOUR TRADE` line |
| c8b9 | 74.0–81.3 | 1751.20–1758.50 | kinetic host-Q (no label) | full-frame | beat-c8b9-host-q.html | NONE (by design) |
| c8b10 | 81.3–102.0 | 1758.50–1779.20 | swiss-grid front/back split | Mode-A | beat-c8b10-front-back.html | divider rule |
| c8b11 | 102.0–116.5 | 1779.20–1793.70 | bulleted liquid-glass | Mode-A | beat-c8b11-use-cases.html | accent bar |
| c8b12 | 116.5–139.0 | 1793.70–1816.20 | kinetic phrase-build (**STANDOUT**) | full-frame | beat-c8b12-blue-wave.html | `SHORT OIL` line |
| c8b13 | 139.0–165.0 | 1816.20–1842.20 | liquid-glass + data-chart (risk) | Mode-A | beat-c8b13-risk-metrics.html | accent bar |
| c8b14 | 165.0–167.8 | 1842.20–1845.00 | clean (close) | Mode-A | — | — |

**13 beats** for a 167.8s clip (≥8 required). **No two adjacent beats identical.** **5 kinetics, max 2 in a row.** **6 view segments, min dwell ~12.3s, no A-B-A inside 12s.**

> Naming change vs v2: c8b1 sub-comp `beat-c8b1-stat.html` → **`beat-c8b1-open.html`** (it is now a kinetic phrase-build, not a stat-numeral). c8b11 `beat-c8b11-analysis-fit.html` → **`beat-c8b11-use-cases.html`** (reworded, de-duped). v2 had 14 beats (c8b2 was a separate Mode-A clean); v3 folds the 7–16s window into ONE full-frame view so c8b2 is a full-frame clean inside S1 — net 13 beats. **Rebuild c8b1, c8b3 (now full-frame), c8b4 (GRUNT WORK), c8b5 (eyebrow → `THE PRODUCTIVITY DELTA`), c8b7 (node1 → `State your thesis`, drop "dime"), c8b11 (reword). c8b8/c8b10/c8b12/c8b13 timings essentially unchanged from v2; c8b9 extended to 81.3 + c8b10 start pushed to 81.3 — content edits + the S3→S4 retime where noted.**

---

## WORD-SYNC AUDIT (every non-editorial kinetic line — verified vs `clip8-words.txt`, converted `comp = table_comp − 2.20`)

| beat·line | on-screen text | transcript words | src | comp (src−1677.20) |
|---|---|---|---|---|
| c8b1 L1 | `THE WORK I DO TODAY` | "the work … today" | 1678.98 | **1.78** |
| c8b1 L2 | `WOULD REQUIRE` | "would require" | 1680.64 | **3.44** |
| c8b1 L3 (cyan) | `A TEAM OF 2–3 ANALYSTS` | "a team of two…to three…people" (ANALYSTS = light editorial gloss of "people") | 1682.00 / 1683.68 / 1683.90 | **4.80 / 6.48 / 6.70** |
| c8b3 L1 | `I'M DOING RESEARCH` | "for me … research" | 1689.96 / 1691.26 | **12.76 / 14.06** |
| c8b3 L2 | `AND TRADING` | "and … trading" | 1691.68 / 1692.14 | **14.48 / 14.94** |
| c8b3 L3 | `ONE PERSON.` | EDITORIAL cyan cap (on "So") | 1692.44 | **15.24** |
| c8b4 L1 | `IT COLLAPSES THE` | "completely collapses" | 1694.66 | **17.46** |
| c8b4 L2 | `LONGER-DURATION GRUNT WORK` | "longer duration grunt work" | 1696.92 / 1698.32 | **19.72 / 21.12** |
| c8b4 chip1 | `ANALYSIS` | "analysis" | 1700.26 | **23.06** |
| c8b4 chip2 | `DATA GATHERING` | "data … gathering" | 1701.08 / 1702.14 | **23.88 / 24.94** |
| c8b5 eyebrow | `THE PRODUCTIVITY DELTA` | "night and day difference" (cue) | 1704.88 | **27.68** |
| c8b5 arrow | (divider) | "difference" | 1706.10 | **28.90** |
| c8b5 footer | `same research output` | "five years ago" | 1707.72 | **30.52** |
| c8b7 eyebrow | `REVAMPING THE TRADING STACK` | "revamping" | 1728.20 | **51.00** |
| c8b7 node1 | `State your thesis` | "books"→"my view about the market" | 1731.52 / 1735.70 | **54.32 / 58.50** |
| c8b7 node2 | `Talk to a terminal` | "terminal" | 1734.24 | **57.04** |
| c8b7 node3 | `Embedded in the exchange` | "embedding … exchange" | 1740.10 | **62.90** |
| c8b7 node4 (cyan) | `+ Paradigm` | "paradigm … unified" | 1742.74 / 1745.26 | **65.54 / 68.06** |
| c8b8 L1 | `IT KNOWS YOUR PROFILE` | "it knows your profile" | 1747.60 / 1747.90 | **70.40 / 70.70** |
| c8b8 L2 | `IT KNOWS THE EXCHANGE` | "it knows the exchange" | 1748.72 | **71.52** |
| c8b8 L3 (cyan) | `…HOW TO ROUTE YOUR TRADE` | "route your trade" | 1750.14 / 1750.46 | **72.94 / 73.26** |
| c8b9 L1 | `ARE THESE THEMATICS` | "these thematics" | 1751.92 / 1752.06 | **74.72 / 74.86** |
| c8b9 L2 | `YOU'RE EXPLORING?` | "you guys are exploring" | 1752.94 | **75.74** |
| c8b10 L-hdr | `FRONT END` | "on the front end" | 1758.92 | **81.72** |
| c8b10 eyebrow | `WHERE AI FITS` | EDITORIAL chrome (lands with FRONT header @ 81.72, post-settle) | 1758.92 | **81.72** |
| c8b10 L-body | `Intent · expressing risk` | "intent … of risk" | 1759.78 | **82.58** |
| c8b10 US tag | `US (Wintermute)` | "For us" | 1771.28 | **94.08** |
| c8b10 R-hdr | `BACK END` | "on the back end" | 1774.80 / 1775.08 | **97.60** |
| c8b10 R-body | `Market infrastructure` | "market infrastructure" | 1775.66 | **98.46** |
| c8b11 eyebrow | `WHAT AI HANDLES BACK-END` | "can we do … analysis" | 1778.04 | **100.84** |
| c8b11 b1 | `Market analysis` | "analysis" | 1779.02 | **101.82** |
| c8b11 b2 | `What trades to do` | "trades" | 1782.86 | **105.66** |
| c8b11 b3 | `Make / take fees` | "make or take fees" | 1785.28 / 1785.86 | **108.08 / 108.66** |
| c8b11 payoff | `→ WHERE IT LANDS FIRST` | "biggest fits" | 1792.68 / 1793.02 | **115.48 / 115.82** |
| c8b12 lead | `INTENT-BASED TRADING NEEDS:` | "intent based trading" | 1794.12 | **116.92** |
| c8b12 mid1 | `INFRASTRUCTURE & HIGH-QUALITY DATA` | "infrastructure … high quality data" | 1797.30 | **120.10** |
| c8b12 mid2 | `TO LET AGENTS EXPRESS RISK` | "agents … express risk" | 1802.52 / 1803.56 | **125.32 / 126.36** |
| c8b12 L1 | `BLUE WAVE` | "a blue wave" | 1807.70 / 1807.88 | **130.50 / 130.68** |
| c8b12 L2 | `STRAIT OF HORMUZ` | "the Strait of Hormuz" | 1811.44 / 1812.06 | **134.24 / 134.86** |
| c8b12 L3 (cyan) | `SHORT OIL` | "potentially short oil" | 1815.68 / 1816.12 | **138.48 / 138.92** |
| c8b13 eyebrow | `AGENTS MUST CONTROL RISK` | "control risk" | 1828.34 | **151.14** |
| c8b13 row1 | `BETA` | "beta" | 1832.64 | **155.44** |
| c8b13 row2 | `MAX DRAWDOWN` | "max drawdown" | 1834.60 | **157.40** |
| c8b13 payoff | `…ENTIRE INVESTABLE UNIVERSE` | "entire investable universe" | 1839.18 / 1840.08 | **161.98 / 162.88** |

**EDITORIAL (not word-synced):** **c8b3 L3 `ONE PERSON.`** (cyan summary cap on "So" — lines 1–2 above it ARE verbatim); the c8b1/c8b7/c8b10 eyebrows (structural chrome); and `ANALYSTS` in c8b1 L3 is a light editorial substitution for the spoken "people." Every other kinetic line lands on its spoken word (the v2→v3 coherence + dialog-match fix). No anticipatory hook anywhere.

---

## JARGON AUDIT (R3 — every on-screen string vs `_JARGON.md`)

| on-screen string | status |
|---|---|
| `GRUNT WORK` (c8b4) | ✅ CORRECTED from Whisper "graft work" (glossary src 1692.4) |
| `+ Paradigm` (c8b7) | ✅ spoken brand kept; **"dime terminal" DROPPED** (glossary: unresolved → avoid on screen) |
| `Market analysis` (c8b11) | ✅ "law" Whisper artifact (not in glossary) reworded out — no "law" on screen |
| `1 TRADER + AI`, `BETA`, `MAX DRAWDOWN`, `Make / take fees`, `Market infrastructure`, `FRONT END`/`BACK END`, `STRAIT OF HORMUZ`, `SHORT OIL`, `BLUE WAVE` | ✅ plain English / standard finance terms, no Whisper garble |
| `Wintermute` (c8b10 US tag) | ✅ exact brand spelling |
| No `burp`/`deep-in`/`graft`/`stake-rate`/`meme con`/`insaturable`/`dime terminal` anywhere | ✅ |

---

## INDEX.HTML CHANGES REQUIRED (vs current v2 `index.html`)

1. **Group the open into one full-frame view (the R1 fix):** **REMOVE** the `toModeA(7.0, 0.7)` + `toFull(11.7, 0.4)` + `toModeA(15.7, 0.5)` cluster (the 7–16s twitch). **REPLACE** with a single `toModeA(16.0, 0.6)` at the c8b4 boundary. Start the Ken-Burns `vid` scale fromTo at **16.0** (not 7.0). The video holds FULL-FRAME 0→16, settles to Mode A once at 16.
2. **c8b2 is now a full-frame clean inside S1** (no overlay, no transition) — its `<!-- c8b2 -->` comment stays; no GSAP at 7.0.
3. **c8b1 sub-comp src** → `compositions/beat-c8b1-open.html` (rebuilt as kinetic phrase-build; corner index `08` is **`#F0F0F0` at ≥22px**, NOT `#888888`/20px). **c8b3 is now FULL-FRAME** (its div is unchanged; it just plays inside S1 — remove any per-c8b3 toFull/toModeA, since the whole 0–16 window is already full-frame). **c8b11 sub-comp src** → `compositions/beat-c8b11-use-cases.html`.
4. **c8b4 data-start/duration** → `data-start="16.0" data-duration="10.0"` (was 16.0/9.0; absorbs the old c8b5 26.0 start gap — c8b5 stays 26.0/7.0). Re-verify c8b4 exits before c8b5 enters.
5. **z-index:3 rule** must list EVERY overlay id (clean beats c8b2/c8b6/c8b14 excluded):
   `#beat-c8b1, #beat-c8b3, #beat-c8b4, #beat-c8b5, #beat-c8b7, #beat-c8b8, #beat-c8b9, #beat-c8b10, #beat-c8b11, #beat-c8b12, #beat-c8b13 { z-index: 3; }` (11 ids — unchanged; just confirm). **CRITICAL: any overlay id missing here renders behind the video.**
6. **Retimed view transitions only** (matching the VIEW-TIMELINE — note the S3→S4 push from 78.7 to 81.0, the R1 A-B-A fix): `toModeA(16.0,0.6)` · `toFull(68.7,0.4)` · **`toModeA(81.0,0.5)`** · `toFull(116.2,0.4)` · `toModeA(138.7,0.5)`. **No transition in 7–16s; no `toModeA` in 69–81s.** Also push c8b10's `data-start` to **81.3** (was 79.0) and re-anchor c8b10's eyebrow `WHERE AI FITS` from comp 80.24 to **81.72** (it now lands with the FRONT-END header, after the Mode-A settle). c8b10 `data-duration` → **20.7** (was 23.0).
7. **object-position stays `83% center`**; Ken-Burns `scale 1.08→1.12` (just move its start to 16.0). `data-media-start=1677.20`, `data-duration=167.8` already correct in v2 — keep.

## BUILD MANIFEST ROW
`clip_8 | clip-8-ai-multiplier | 1677.20 | 1845.00 | kinetic-type,flowchart,swiss-grid,liquid-glass,data-chart,shimmer-sweep | 13 beats`
