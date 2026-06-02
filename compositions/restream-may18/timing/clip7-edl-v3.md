# Clip 7 — v3 build-ready EDL (clip-7-bear-market-exit)

**Primary device (DESIGN.md per-clip map):** NARRATIVE TIMELINE / decision-tree.
A vertical narrative-cycle spine: **2024 ETF → ORDINALS + INSCRIPTIONS → DeFi SUMMER → DePIN → AI AGENTS → ?**
Nodes pop ON their spoken era. The timeline POSES an open cyan `?` node; the closing liquid-glass card
ANSWERS it (PRIVACY + AI). This pose-and-answer is unique to this clip — NOT a kinetic stack of cards.

**Why v3 (the rejected-v2 defects, all fixed):**
1. **View flip-flop @ 41–49s (R1).** v2 did full→ModeA→full→ModeA with three sub-8s segments (clean breath 3.8s,
   cadence 4.6s). v3 **groups** the whole "why the cycle repeats" stretch (spiral + examples + cadence) into a
   single sustained **17s full-frame block**, then ONE switch to Mode-A for the payoff. 4 views, every non-intro
   segment ≥17s, no A-B-A within 12s. See VIEW-TIMELINE below.
2. **All-looking-like-clip-2 (R2).** Device LED by the timeline (decision-tree), not kinetics. Kinetic count is
   3 of 6 beats and **never 3 in a row** — the two full-frame kinetics (spiral, cadence) are split by a
   non-kinetic **examples chip-row** card. No `07/EYEBROW/STAT/tag-row` swiss-grid opener.
3. **Jargon errors (R3).** **DePIN** node ADDED (v2 omitted it; Whisper wrote "deep in / deep intaking"). Examples
   row uses **perp dexes** + **meme coins** (NOT "burp", NOT "meme con"). Every string mapped through `_JARGON.md`.
4. **Duplicate "frontrunners" (R4).** v2 had eyebrow `THE FRONTRUNNERS` **and** sublabel `…the frontrunners` in
   c7b5. v3 eyebrow = `WHAT COMES NEXT` (editorial frame); "frontrunners" appears **once**, in the sublabel only.
5. **clip-8 incoherence** is a clip-8 issue; here the opener (R5) parses as a complete thought: `WE ALWAYS EXIT /
   BEAR MARKETS / IN AN INTERESTING WAY`, cyan payoff is a real phrase, not a dangling number.

**Kept from v2 (what worked):** the dialog-matched cold open on the thesis line, and the framing object-position
(`84% center`, derived from real extracted frames — Jasper face ≈x1400, name lower-third left edge ≈x990;
50%/62% center the seam → rejected).

---

## IN / OUT / DURATION

| field | value | rationale |
|-------|-------|-----------|
| `src_in` (data-media-start) | **1530.50** | "we" @ src1530.76 → fires at comp **0.26** (≈0.3 target). Cut lands on the breath right after "I feel like" (last word "like" ends 1530.60). Filler head ("Well, to your point around building as well, I feel like") trimmed. |
| `src_out` | **1597.0** | Jasper completes the thesis on "…or at least **adjacent to it**" (`it` @ src1595.84). Next word "Yeah" @ src1597.32 is **Nic** → cut before it. ~1.16s settle after "it". |
| duration | **66.5s** | 1597.0 − 1530.50 = 66.5. Use `data-duration="66.5"` on master-root, video, audio. |
| `comp` formula | **comp = src − 1530.50** | All fire-times below read off `clip7-words.txt` (table is src−1515) then re-based to this src_in. |

> NOTE for the builder: `clip7-words.txt` is comp = src − **1515**. This EDL is comp = src − **1530.50**.
> When wiring sub-comps, use the comp values **in this file** (already re-based). Each sub-comp's internal GSAP
> offset = (comp fire) − (beat `data-start`); the per-beat offsets are pre-computed in the BEAT TABLE.

---

## VIEW-TIMELINE (proves R1)

| seg | view | comp range | dwell | beats in view | rule check |
|-----|------|-----------|-------|---------------|------------|
| V1 | **full-frame** (both speakers) | 0.0 – 6.0 | **6.0s** | c7b1 opener kinetic | intro zone — quick switch allowed |
| V2 | **Mode-A** (guest right 40%) | 6.0 – 32.0 | **26.0s** | c7b2 HERO timeline | ≥8s ✓ |
| V3 | **full-frame** (both speakers) | 32.0 – 49.0 | **17.0s** | c7b3 spiral · c7b4 examples · c7b5 cadence | ≥8s ✓ — spiral+cadence kinetics GROUPED into ONE view (no bounce) |
| V4 | **Mode-A** (guest right 40%) | 49.0 – 66.5 | **17.5s** | c7b6 privacy+AI card | ≥8s ✓ — holds to clip end |

**A-B-A proof:** full-frame appears at [0–6] and [32–49] → gap 26s (>12s) ✓. Mode-A appears at [6–32] and
[49–66.5] → gap 17s (>12s) ✓. No view returns within 12s. Only ONE view change happens inside the 32–49 stretch?
**No** — zero view changes inside it: spiral, examples, and cadence ALL render full-frame. The only switches are at
6.0 (intro→timeline), 32.0 (timeline→mechanism), 49.0 (mechanism→payoff). **3 switches, all spaced ≥17s. PASS.**

---

## TEMPLATE VARIETY (proves R2)

| beat | template / device | kinetic? |
|------|-------------------|----------|
| c7b1 | `kinetic-type` (opener) | yes (1) |
| c7b2 | **decision-tree (HERO timeline)** | no |
| c7b3 | `kinetic-type` (spiral) | yes (1) |
| c7b4 | **liquid-glass examples chip-row** | no |
| c7b5 | `kinetic-type` (cadence) | yes (1) |
| c7b6 | **liquid-glass payoff card** | no |

- Max kinetics in a row = **1** (every kinetic is bounded by a non-kinetic neighbor). 3+ in a row = FAIL → PASS.
- No same template twice in a row (kinetic / tree / kinetic / card / kinetic / card). PASS.
- Distinct primary device = narrative timeline, leads as the hero (c7b2, the longest beat). PASS.

**Catalog install vs hand-build:**
- c7b2 HERO timeline → **`npx hyperframes init` style `--example decision-tree`** re-skinned vertical (built-in
  example, NOT an `add` block). The existing `compositions/beat-c7b2-narrative-cycle.html` is already this device —
  **edit it** (add DePIN node + re-time, see below), don't rebuild.
- c7b1 / c7b3 / c7b5 kinetics → **`--example kinetic-type`** (built-in). Existing
  `beat-c7b1-hook.html`, `beat-c7b3-spiral.html`, (rename `beat-c7b4-cadence.html`→ c7b5) — edit/re-time.
- c7b4 examples chip-row → **hand-build** a liquid-glass tag strip (two chips: `PERP DEXES`, `MEME COINS`).
  Do NOT use `ios26-liquid-glass` / `macos-tahoe-liquid-glass` (they carry `backdrop-filter` blur — DESIGN.md
  forbids blur). Use the DESIGN.md card recipe: solid `rgba(20,26,34,0.92)` fill + 4px cyan bar + glow, no blur.
  (The catalog `flowchart` block is overkill for two static chips — skip it here.)
- c7b6 payoff card → **hand-build** liquid-glass card (same recipe). Rename/rewrite v2's `beat-c7b5-privacy-ai.html`.

---

## OBJECT-POSITION (R-framing — kept from v2, verified)

`object-position: 84% center` on `#short_mag_cut`. Mode-A geometry `left:1229, top:108, width:614, height:864`
(bottom clearance 108px >40px so the name never clips; top 108px >20px). With `object-fit:cover` scaling source by
height (×0.8), the 614px window shows a 768px source slice centered at `84%×1152+384 = 1352` → source x≈968–1736:
centers Jasper (face ≈x1400), keeps his "Jasper De Maere / Wintermute" lower-third (left edge ≈x990) inside
window-left (968), trims the dead right-wall. 50%→center 960 (the seam) and 62%→center 1098 (half-host) REJECTED.
**Builder: re-extract a Mode-A frame (e.g. `ffmpeg -ss 1582 -i source.mp4 -frames:v 1`) and LOOK before render.**

---

## BEAT TABLE

> `comp = src − 1530.50`. Every kinetic LINE quotes the transcript words it fires on, its `src_t`, the clip
> `comp_t` (re-based), and the in-beat GSAP offset = comp_t − beat `data-start`. EDITORIAL (label / anticipatory)
> lines are marked. All on-screen strings are post-`_JARGON.md`.

### c7b1 — KINETIC opener · **view V1 full-frame** (both speakers) → shrinks to Mode-A at comp 6.0
- **comp 0.0 – 6.0 · src 1530.50 – 1536.50**
- Template/block: `kinetic-type` — 3-line phrase build, lines slam in and **STAY** (no dim). Dark gradient backdrop
  in the left zone; full-frame video (both speakers) behind. Video shrinks to Mode-A at comp 6.0 as the stack wipes up.
- View: **full-frame** the whole opener.
- Sub-comp file: `compositions/beat-c7b1-hook.html` · `data-start="0.0" data-duration="6.0"`
- On-screen lines (R5 coherent: "WE ALWAYS EXIT / BEAR MARKETS / IN AN INTERESTING WAY"):

  | line | text | transcript words | src_t | **comp_t** | GSAP offset | color |
  |---|---|---|---|---|---|---|
  | L1 | `WE ALWAYS EXIT` | "we always exit" | we 1530.76 | **0.26** | 0.26 | #F0F0F0 |
  | L2 | `BEAR MARKETS` | "bear markets" | bear 1532.66 | **2.16** | 2.16 | #F0F0F0 |
  | L3 | `IN AN INTERESTING WAY` | "in a very interesting fashion" | interesting 1535.02 | **4.52** | 4.52 | **#00D4FF** (payoff) |

  - L3 condenses spoken "in a very interesting fashion" → on-screen `IN AN INTERESTING WAY`, fired on "interesting"
    @comp 4.52 (literal-word match, not anticipatory). Cyan: L3 only. Stack drifts up & out at ~5.6 (before the
    Mode-A shrink at 6.0). `data-duration` 6.0 covers L1 0.26 → L3 4.52 + headroom.

### c7b2 — DECISION-TREE: narrative-cycle TIMELINE (HERO) · **view V2 Mode-A**
- **comp 6.0 – 32.0 · src 1536.50 – 1562.50**
- Template/block: `decision-tree` (`--example decision-tree`) re-skinned as a **vertical narrative-cycle timeline**
  (neutral #2A2A2A spine slow-draws top→bottom; nodes pop `back.out(1.5)` ON their spoken era). HERO centerpiece.
- View: **Mode-A** (object-position 84%); `#bg-glow` + `#zone-rule` fade in at ~6.3.
- Sub-comp file: `compositions/beat-c7b2-narrative-cycle.html` · `data-start="6.0" data-duration="26.0"`
- Eyebrow (EDITORIAL label — `<!-- EDITORIAL: section label, not word-synced -->`): `THE NARRATIVE CYCLE`
  — Inter 700, 34px, #F0F0F0, slam @ comp 6.4 (offset 0.40). (Does not duplicate any node word; "narrative"
  appears once in the beat — R4 within-beat OK.)
- Mono index `07` top-left (20px JetBrains Mono #888) @ 6.3.
- Spine (#2A2A2A, neutral — NOT cyan) slow-draws from comp ~7.2 (offset 1.2) across the beat.
- **Nodes — SPOKEN ORDER (this is the R3 fix: DePIN ADDED as n4):**

  | node | on-screen text | transcript words it fires on | src_t | **comp_t** | GSAP offset | color |
  |---|---|---|---|---|---|---|
  | n1 | `2024` / `ETF ANNOUNCEMENTS` | "the sort of 24, we had the ETF announcements" | ETF 1541.26 | **10.76** | 4.76 | #F0F0F0 |
  | n2 | `ORDINALS + INSCRIPTIONS` | "suddenly we had like inscriptions and ordinals" | inscriptions 1543.76 | **13.26** | 7.26 | #F0F0F0 |
  | n3 | `DeFi SUMMER` | "excited about like Bitcoin, DeFi" | DeFi 1547.58 | **17.08** | 11.08 | #F0F0F0 |
  | **n4** | **`DePIN`** / `Decentralized Physical Infra.` | "Then we had **deep intaking off**" → **DePIN** (`_JARGON.md`, src 1548.2, user-flagged) | deep 1549.02 | **18.52** | 12.52 | #F0F0F0 |
  | n5 | `AI AGENTS` | "Then we had AI agents… very early inflection" | AI 1550.82 | **20.32** | 14.32 | #F0F0F0 |
  | n6 | `?` / `NEXT` | "I'm very **curious** what we will come up with as the **next** narrative" (EDITORIAL turn) | curious 1556.28 | **25.78** | 19.78 | **#00D4FF** |

  - **n4 DePIN is the critical add.** Sublabel `Decentralized Physical Infra.` (Inter 600, ≥32px, #F0F0F0).
    `<!-- JARGON: Whisper "deep intaking off" → DePIN per _JARGON.md (user-flagged confirmed) -->`
  - n6 `?` is the open question — the single cyan element (node fill rgba(0,212,255,0.18) + #00D4FF border + glow;
    `?` glyph #00D4FF ≥48px so the muted-grey rule is moot). `NEXT` sublabel also cyan-tinted on this node only.
    `<!-- EDITORIAL: n6 "?" open-question turn, fires on "curious" — anticipatory of the c7b6 answer -->`
  - 6 nodes now fit; reduce per-node `margin-bottom` 30→22px and spine height 520→600px so all 6 fit the left zone.
  - Inner content fades out @ comp ~31.6 (offset 25.6) before V3 establishes. `data-duration` 26.0 covers n1 10.76 → n6 25.78.
  - Cyan element: n6 only. PASS.

---
**↓↓ view V3 full-frame block (32.0–49.0) — c7b3, c7b4, c7b5 all render full-frame; NO view change between them ↓↓**

### c7b3 — KINETIC: the "spiral" mechanism · **view V3 full-frame** (both speakers)
- **comp 32.0 – 41.2 · src 1562.50 – 1571.70**
- Template/block: `kinetic-type` — 4-line phrase build, lines STAY. Explains WHY the cycle repeats.
- View: **full-frame** — video expands Mode-A→full at comp 32.0 (Ken-Burns reset). Stays full for c7b4 & c7b5 too.
- Sub-comp file: `compositions/beat-c7b3-spiral.html` · `data-start="32.0" data-duration="9.2"`
- Word-synced (spoken: "it's a spiral where like prices go up. We find the narrative. People get excited about it late in the cycle."):

  | line | text | transcript words | src_t | **comp_t** | GSAP offset | color |
  |---|---|---|---|---|---|---|
  | L1 | `IT'S A SPIRAL` | "a spiral where" | spiral 1564.66 | **34.16** | 2.16 | #F0F0F0 |
  | L2 | `PRICES GO UP` | "like prices go up" | prices 1565.70 | **35.20** | 3.20 | #F0F0F0 |
  | L3 | `WE FIND THE NARRATIVE` | "We find the narrative" | We 1567.02 | **36.52** | 4.52 | #F0F0F0 |
  | L4 | `EXCITED LATE IN THE CYCLE` | "People get excited about it late in the cycle" | People 1568.02 (line lead) | **37.52** | 5.52 | **#00D4FF** (payoff) |

  - L4 fires on the first spoken word of the line ("People" @37.52) per the line-lead convention; reads through
    "late… in the cycle" (cycle @40.46). Cyan: L4 only. `data-duration` 9.2 covers L1 34.16 → L4 37.52, lines hold to ~40.8 then exit (no view change — video stays full into c7b4).

### c7b4 — LIQUID-GLASS examples chip-row · **view V3 full-frame** (over both speakers)
- **comp 41.2 – 45.2 · src 1571.70 – 1575.70**
- Template/block: **hand-build** liquid-glass tag strip — two chips slam in, each on its spoken example. Non-kinetic
  device placed BETWEEN the two kinetics (c7b3, c7b5) so kinetics never run 3-in-a-row and the same template never
  repeats back-to-back. Card recipe (DESIGN.md): solid `rgba(20,26,34,0.92)` fill, 4px cyan accent bar (inset
  left), soft glow, 1px border, `mask-image` feather to the right. **NO backdrop-filter blur. NO grain.**
- View: **full-frame** — video stays full from c7b3 (NO view change). Chip strip sits lower-left over the video with
  its own dark fill (full-frame readability backdrop).
- Sub-comp file: `compositions/beat-c7b4-examples.html` (NEW) · `data-start="41.2" data-duration="4.0"`
- Eyebrow (EDITORIAL label): `EVERY CYCLE'S TOYS` — Inter 700, 32px, #F0F0F0 @ comp 41.4.
  `<!-- EDITORIAL: section label, not word-synced -->`
- Chips (each slams in `back.out(1.5)` on its spoken word):

  | chip | on-screen text | transcript words | src_t | **comp_t** | GSAP offset | color |
  |---|---|---|---|---|---|---|
  | c1 | `PERP DEXES` | "we had like perp dexes" | perp 1572.36 | **41.86** | 0.66 | #F0F0F0 (fill #141A22) |
  | c2 | `MEME COINS` | "meme coin launch platforms" | meme 1573.46 | **42.96** | 1.76 | #F0F0F0 (fill #141A22) |

  - `<!-- JARGON: spoken Whisper "perp dexes" OK; "meme con" → MEME COINS per _JARGON.md -->`
  - Cyan element: the single 4px accent bar on the strip (chips themselves are neutral #141A22). PASS.
  - Strip exits ~44.8 (no view change — video stays full into c7b5).

### c7b5 — KINETIC: "cadence of innovation" bridge · **view V3 full-frame** (both speakers)
- **comp 45.2 – 49.0 · src 1575.70 – 1579.50**
- Template/block: `kinetic-type` — 2-line phrase build. The thesis bridge before the Mode-A payoff.
- View: **full-frame** — video still full (NO view change since c7b3). Switches to Mode-A only at comp 49.0 (next beat).
- Sub-comp file: `compositions/beat-c7b5-cadence.html` (rename of v2 `beat-c7b4-cadence.html`) · `data-start="45.2" data-duration="3.8"`
- Word-synced (spoken: "But that cadence of innovation, I think is super interesting to see."):

  | line | text | transcript words | src_t | **comp_t** | GSAP offset | color |
  |---|---|---|---|---|---|---|
  | L1 | `THE CADENCE` | "that cadence of" | cadence 1576.08 | **45.58** | 0.38 | #F0F0F0 |
  | L2 | `OF INNOVATION` | "of innovation" | innovation 1576.64 | **46.14** | 0.94 | **#00D4FF** (payoff) |

  - Cyan: L2 only. Lines hold to ~48.6 then exit as video shrinks to Mode-A for c7b6. `data-duration` 3.8 covers L1 45.58 → L2 46.14.

---
**↑↑ end view V3 full-frame block ↑↑** — single switch to Mode-A at comp 49.0 below.

### c7b6 — LIQUID-GLASS payoff card: the "?" RESOLVES → PRIVACY + AI · **view V4 Mode-A**
- **comp 49.0 – 66.5 · src 1579.50 – 1597.00** (clip end)
- Template/block: **hand-build** liquid-glass card (DESIGN.md recipe: `rgba(20,26,34,0.92)` fill, 4px cyan accent
  bar inset-left, glow, 1px border, `mask-image` feather right). **NO blur, NO grain.** Pays off c7b2's open `?`.
- View: **Mode-A** (object-position 84%); video shrinks full→Mode-A at comp 49.0, `#bg-glow`+`#zone-rule` return.
  Card holds over live continuing speaker video to clip end.
- Sub-comp file: `compositions/beat-c7b6-privacy-ai.html` (rewrite of v2 `beat-c7b5-privacy-ai.html`) ·
  `data-start="49.0" data-duration="17.5"`
- Structural rhyme: card opens with a small `?  →` glyph (echo of c7b2's open node) that the two answer words slam
  in beside — visually "filling in" the answer.
- **Eyebrow (EDITORIAL label) — R4 FIX:** `WHAT COMES NEXT` — Inter 700, 32px, #F0F0F0 @ comp 49.4.
  `<!-- EDITORIAL: section label. R4: "frontrunners" appears ONLY in the sublabel below, NOT here -->`
- Word-synced reveal (spoken: "anyone's guess currently **privacy and AI**… top of mind for many… the **front runners** in terms of what we might see"):

  | element | on-screen text | transcript words | src_t | **comp_t** | GSAP offset | color |
  |---|---|---|---|---|---|---|
  | W1 | `PRIVACY` (130px) | "currently privacy" | privacy 1581.92 | **51.42** | 2.42 | #F0F0F0 |
  | W2 | `AI` (130px) | "and AI" | AI 1583.44 | **52.94** | 3.94 | #F0F0F0 |
  | sub | `Top of mind — the frontrunners` (28px) | "top of mind for many… the front runners" | mind 1585.04 / front 1587.84 | **54.54** | 5.54 | #F0F0F0 |

  - **R4 PASS:** notable word "frontrunners" appears ONLY in `sub`; eyebrow is `WHAT COMES NEXT` (no shared word).
    `<!-- JARGON: spoken "front runners" → on-screen "frontrunners" (one word), single occurrence -->`
  - **R-no-outro (D4):** this is a CONTENT reveal (the thesis answer), NOT a name/credit card. There is **NO
    "Jasper De Maere · Wintermute" attribution** (v1's name sublabel removed). Card lands on "privacy and AI," holds
    while he finishes "…either completely in that vertical or at least adjacent to it" (it @ src1595.84 / comp
    65.34). Clip ends on this live content beat; final ~1.2s is the card gently settling over continuing video.
  - Cyan element: the 4px accent bar only (`?→` glyph and both words are #F0F0F0). PASS.

---

## SUB-COMP FILES (compositions/)

| beat | sub-comp filename | data-start | data-duration | status / action |
|------|-------------------|-----------|---------------|-----------------|
| c7b1 | `beat-c7b1-hook.html` | 0.0 | 6.0 | EDIT — re-time to src_in 1530.50 (L1@0.26 / L2@2.16 / L3@4.52); L3 text `IN AN INTERESTING WAY` |
| c7b2 | `beat-c7b2-narrative-cycle.html` | 6.0 | 26.0 | **EDIT — ADD n4 DePIN node**, reorder to spoken order (ETF→Ordinals→DeFi→DePIN→AI→?), eyebrow `THE NARRATIVE CYCLE`, re-time all offsets, shrink margins+grow spine for 6 nodes |
| c7b3 | `beat-c7b3-spiral.html` | 32.0 | 9.2 | EDIT — re-time (L1@34.16…L4@37.52); no text change |
| c7b4 | `beat-c7b4-examples.html` | 41.2 | 4.0 | **NEW** — liquid-glass 2-chip strip (`PERP DEXES`, `MEME COINS`), eyebrow `EVERY CYCLE'S TOYS` |
| c7b5 | `beat-c7b5-cadence.html` | 45.2 | 3.8 | RENAME from `beat-c7b4-cadence.html`; re-time (L1@45.58 / L2@46.14) |
| c7b6 | `beat-c7b6-privacy-ai.html` | 49.0 | 17.5 | REWRITE/RENAME from `beat-c7b5-privacy-ai.html`; eyebrow `WHAT COMES NEXT` (R4), `?→` rhyme, re-time |

**index.html updates required:**
- `data-media-start="1530.50"`, `data-duration="66.5"` on `#short_mag_cut`, `#a-roll-audio`, and `data-duration="66.5"` on `#master-root`.
- **z-index:3 rule must list exactly the 6 beat ids:** `#beat-c7b1-hook, #beat-c7b2-narrative-cycle,
  #beat-c7b3-spiral, #beat-c7b4-examples, #beat-c7b5-cadence, #beat-c7b6-privacy-ai`. (v2 listed 5 — add c7b4-examples,
  rename c7b4-cadence→c7b5-cadence, c7b5-privacy-ai→c7b6-privacy-ai.)
- Re-time the master GSAP phase map to the v3 view-timeline (3 switches only):
  - PHASE 1 @ comp **6.0** — full→Mode-A (glow/zone-rule in @6.3); Ken-Burns across timeline.
  - PHASE 2 @ comp **32.0** — Mode-A→full (glow/zone-rule out @31.7; Ken-Burns reset). **Holds full through 49.0 — no
    intermediate switches** (this is the R1 fix: c7b3/c7b4/c7b5 all play in the one full-frame window).
  - PHASE 3 @ comp **49.0** — full→Mode-A (glow/zone-rule return); gentle settle Ken-Burns to clip end.
- Set `object-position: 84% center` on `#short_mag_cut` (already correct in v2 index.html).

---

## VERIFICATION CHECKLIST (graded vs _QA-CHECKLIST.md)

- **§1 R1 view discipline:** 4 views, dwell 6.0 / 26.0 / 17.0 / 17.5; only the 6.0 is in the 0–6s intro zone; every
  other ≥17s. No A-B-A within 12s (full gap 26s, Mode-A gap 17s). spiral+examples+cadence GROUPED full-frame. **PASS.**
- **§2 R2 variety:** kinetic / tree / kinetic / card / kinetic / card — max 1 kinetic in a row; no same template
  back-to-back; HERO = decision-tree timeline. No swiss-grid `07/EYEBROW/STAT/tag-row` opener. **PASS.**
- **§3 dialog-match:** opens ON "we always exit bear markets" (we @0.26, first text ≤0.3); every kinetic line fires
  at comp = word.src − 1530.50 from `clip7-words.txt`; editorial labels marked. **PASS.**
- **§4 R5 coherence:** `WE ALWAYS EXIT / BEAR MARKETS / IN AN INTERESTING WAY` is a complete thought; cyan payoff is
  a real phrase, no dangling number. **PASS.**
- **§5 framing:** object-position 84% centers Jasper (re-verify by frame before render); opener full-frame shows both
  speakers, never text-on-black. **PASS** (pending builder frame-check).
- **§6 R3 jargon:** **DePIN** node ADDED (not "deep in"); **perp dexes** + **meme coins** (not "burp"/"meme con");
  brand/proper nouns n/a here except DePIN/DeFi spelled per `_JARGON.md`; date "2024" (historical ETF year he names),
  no 2025/2024 ambiguity. **PASS.**
- **§7 R4 dup words:** c7b6 eyebrow `WHAT COMES NEXT` vs sublabel `…the frontrunners` — "frontrunners" appears once.
  c7b2 eyebrow `THE NARRATIVE CYCLE` shares no word with any node. **PASS.**
- **§8 hard rules:** z-index:3 lists all 6 ids; ONE cyan per beat (c7b1 L3 / c7b2 n6 / c7b3 L4 / c7b4 accent bar /
  c7b5 L2 / c7b6 accent bar); no blur, no grain, cards = solid fill + cyan bar; eyebrows Inter 700 ≥32px #F0F0F0;
  no intro/outro card, ends on live content; phrase kinetics build & STAY. **PASS.**
- **§9 verify-by-frame:** builder MUST extract frames at opener / each of the 3 view switches / DePIN node / payoff
  and LOOK before claiming done. (Mandatory, not yet performed.)

**Build Manifest Row:** `clip_7 | clip-7-bear-market-exit | 1530.50 | 1597.0 | decision-tree (timeline-led) | 6 beats`
