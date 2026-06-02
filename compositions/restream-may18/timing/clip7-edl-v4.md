# Clip 7 — v4 build-ready EDL (clip-7-bear-market-exit)

**Primary device (DESIGN.md per-clip map):** NARRATIVE TIMELINE (DeFi → Ordinals → DePIN → AI agents).
A vertical narrative-cycle spine: **ETF ANNOUNCEMENTS → ORDINALS + INSCRIPTIONS → DeFi SUMMER → DePIN → AI AGENTS → ?**
Nodes pop ON their spoken era. The timeline POSES an open cyan `?` node; the closing liquid-glass card
ANSWERS it (PRIVACY + AI). This pose-and-answer is unique to this clip — NOT a kinetic stack of cards.

> **⚠️ STATE-OF-TRUTH BANNER (read before anything else).** This EDL is a **prescription of edits NOT YET
> APPLIED**. As of the last file read, the six build files + `index.html` on disk **still contain every v3 defect**
> (`07` indices live, the blank-left seam live, the `2024` date live, the cyan `NEXT` live, the 1.40 glyph time
> live, `data-duration="26.0"` live). The §VERIFICATION section below is therefore a list of **unchecked TODOs
> `[ ]`**, not a record of completed PASSes. **A v3 reject shipped precisely because a prior EDL phrased these as
> past-tense "fixed."** Do NOT mark anything PASS until you have made the edit AND re-verified it by frame. Every
> TODO carries a grep-able QA assertion so the gate does not trust prose.

> **v4 scope note:** this revision targets the two rejection causes (R6 on-screen index; R7 blank-left Mode-A), the
> seven Agent-3 contradictions, **and nine Agent-2 quality findings** (opener font size, cyan-on-payoff sync, the
> HERO→spiral lull, the chip-strip/host-face collision, the `?`-match-cut, the <90s graphic-density carve-out, the
> worst-frame extract point, and promoting the grouped-V3 win so a future pass doesn't re-split it). It otherwise
> **keeps the verified-correct v3 build decisions.** It does NOT merge beats, drop the DePIN node label set, add
> looping pulses, or add an underline sweep — those would re-introduce the very ≤1-cyan and consistency problems
> Agent-3 flagged.

---

## WHY v4 — the v3 build was REJECTED (two headline defects) + seven Agent-3 contradictions + nine Agent-2 quality findings

**REJECTION CAUSE 1 — R6 INDEX ON SCREEN.** The v3 build renders the literal clip number `07` top-left in TWO
beats: `beat-c7b2-narrative-cycle.html` **line 34** (`<div id="b2-idx">07</div>`) and `beat-c7b6-privacy-ai.html`
**line 35** (`<div id="b6-idx">07</div>`). The v3 EDL even *specified* it. **R6 forbids any internal clip number /
beat index as on-screen text.** v4 DELETES both `#b2-idx` and `#b6-idx` (node + CSS + GSAP tween). c7b1/c7b3/c7b4/
c7b5 carry no index — confirmed clean on disk. The eyebrow editorial labels stay. **STATUS: NOT YET DONE on disk.**

**REJECTION CAUSE 2 — R7 blank-left Mode-A at the V2→V3 seam.** In v3 (still on disk): c7b2's inner content fades
out at offset **25.6** (`beat-c7b2` line 226 → comp 31.6) but `index.html` PHASE-2 only **starts** expanding the
video to full at comp **32.0** (`index.html` line 186, duration 0.4). So the true sequence is: content clears
~32.05, video begins expanding 32.0 and is not full until ~32.4 → a cropped Mode-A frame with an emptying/empty
left zone exists **~31.9–32.4 (~0.5s)** — the clip-8 0:33–0:52 blank-left bug. **v4 makes the fade and the
video-expansion both START at offset/comp 31.70**, the expand running 0.3s so it is **complete by 32.0** — i.e. the
expand `to {left:0…}` STARTS no later than the c7b2 fade START, and the frame is full before the old 32.0 boundary.
The graphic is on screen for the entire Mode-A dwell, and the instant it leaves the frame is already opening to
full. No graphic-less cropped frame exists. **HARD RULE for the builder:** *the video-expand `to {left:0…}` must
fire at or before the c7b2 inner-fade `to {opacity:0}` (both 31.70), and complete (0.3s) by 32.0.* **STATUS: NOT YET
DONE** — `index.html` still reads 32.0 / dur 0.4; `beat-c7b2` still reads fade 25.6.

**The seven Agent-3 contradictions — all PRESCRIBED below (none yet applied):**
1. c7b6 ONE-CYAN: glyph + words stay `#F0F0F0`; the **accent bar is the sole cyan**; NO underline sweep is added.
   *(This one is already correct on disk — glyph+words are `#f0f0f0`, no `.b6-uline`. KEEP; do not regress.)*
2. c7b4 eyebrow: ONE string everywhere = **`EVERY CYCLE'S TOYS`**. *(Already correct on disk. KEEP.)*
3. c7b6 `?→` glyph fires at **offset 1.44 (comp 50.44)** in every reference. *(Disk still reads `1.40` line 148 → CHANGE.)*
4. V2→V3 seam: fade + expansion both at **comp 31.70** (REJECTION CAUSE 2). *(NOT yet applied — see above.)*
5. c7b2 n1: **drops the literal "2024"** → renders `ETF ANNOUNCEMENTS` alone. *(Disk still has `.b2-yr` line 45 → DELETE.)*
6. c7b1 opener: explicit note that **R7 (full-frame kinetic opener, both speakers) supersedes** DESIGN.md's older
   "speaker-right + 3 element types in 6s" mandate (DESIGN.md lines 10–42; QA lines 348–351). *(EDL note only.)*
7. c7b2 n6: **`NEXT` sublabel → `#F0F0F0`**; only the `?` glyph + node dot carry cyan. *(Disk still `#00d4ff` lines 183–186 → CHANGE.)*

**The nine Agent-2 quality findings — incorporated this revision:**
- **A2-1 Banner + unchecked-TODO checklist** (above + §VERIFICATION): the single most important fix — the EDL no
  longer reports unapplied edits as PASS.
- **A2-2 c7b1 opener font 108px → ~130px** (§c7b1): the hook currently reads SMALLER than the c7b6 payoff (130px) —
  inverted hierarchy. Bump to 130px (DESIGN.md line 189 kinetic spec). *(Disk reads `font-size: 108px` line 56.)*
- **A2-3 c7b1 second element TYPE** (§c7b1): add ONE cheap R7-legal full-frame element so the opener isn't a thin
  lone word-stack — a small white eyebrow `THE EXIT PATTERN` at t≈0.10 above the stack. Keeps ≤1 cyan (L3 stays the
  only cyan); narrows the DESIGN.md "3 element types" gap instead of only declaring it superseded.
- **A2-4 c7b3 L4 cyan-on-payoff sync** (§c7b3): split L4 so the cyan lands on the literal payoff word. Fire
  `EXCITED` white on "excited" (**comp 37.84**) and reveal `LATE IN THE CYCLE` cyan on "late" (**comp 38.82**) —
  instead of firing the whole cyan line on "People" (37.52), 2.9s before "cycle" (40.46) is spoken.
- **A2-5 HERO→spiral lull** (§c7b2 / §VIEW-TIMELINE): the ~comp 26–34 stretch (n6 done → spiral starts) is the one
  felt lull. Extend the c7b2 `?` node hold and give it a subtle downward drift at ~31 so the pose visually *leans*
  into the spiral cut (motivates the seam; stays R7-legal).
- **A2-6 chip-strip vs host face** (§c7b4): source is SIDE-BY-SIDE (Nic/host LEFT, Jasper/guest RIGHT — QA line 6).
  c7b4's strip is lower-LEFT (`bottom:0`, backdrop 560px tall) over the full-frame two-shot — i.e. directly over the
  host. Raise the strip baseline so the backdrop top edge clears both chins; VERIFY by frame at comp 42.
- **A2-7 `?` match-cut** (§c7b6): make the c7b2→c7b6 `?` rhyme land harder — enter the c7b6 `?` at the same
  size/screen position the c7b2 `?` exited so it reads as a match-cut across the V3 block, then `→ PRIVACY/AI`
  resolves it.
- **A2-8 <90s density carve-out** (§VERIFICATION §3a): state explicitly that the clip is 66.5s (<90s), so DESIGN.md
  line 358 "min 8 graphic beats for clips over 90s" is N/A and 6 beats is correct density (prevents a false-FAIL).
- **A2-9 worst-frame extract point** (§VERIFICATION §9): the blank-left risk frame opens *between* 31.6 and 32.0, so
  add comp **32.2** to the extract set (sample 31.8 / 32.0 / 32.2 / 32.4) — extracting at 31.6/32.0 alone can miss it.

**Kept from v3 (what worked — DO NOT undo):** dialog-matched cold open on the thesis line; framing object-position
`84% center` (Jasper face ≈x1400, name lower-third left edge ≈x990; 50%/62% center the seam → rejected); the
timeline-led HERO device; the 4-view structure; the DePIN R3 node add + `Decentralized Physical Infra.` sublabel
(the one node a 1080p viewer cannot decode from the acronym alone); **and the grouped-V3 block (spiral+examples+
cadence in ONE 17.3s full-frame view, no bounce)** — this is the single strongest structural decision and it
directly fixes the v3 "41–49s A-B-A" reject (QA §1 / DESIGN R1). **A future pass must NOT "add variety" by
re-splitting V3 — that re-breaks R1.** (See §VIEW-TIMELINE "kept win.")

---

## IN / OUT / DURATION (unchanged from v3 — verified correct)

| field | value | rationale |
|-------|-------|-----------|
| `src_in` (data-media-start) | **1530.50** | "we" @ src1530.76 → fires comp **0.26** (≈0.3 target). Cut lands on the breath after "I feel like" ("like" ends 1530.60). Filler head ("Well, to your point around building as well, I feel like") trimmed. **LOCKED.** |
| `src_out` | **1597.0** | Jasper completes the thesis on "…or at least **adjacent to it**" (`it` @ src1595.84). Next word "Yeah" @ src1597.32 is **Nic (host)** → cut before it. ~1.16s settle after "it". |
| duration | **66.5s** | 1597.0 − 1530.50 = 66.5. `data-duration="66.5"` on `#master-root`, `#short_mag_cut`, `#a-roll-audio`. |
| `comp` formula | **comp = src − 1530.50** | All fire-times below read off `clip7-words.txt` (table is comp = src − 1515) then re-based (subtract 15.50 from the table's comp). |

> Builder note: `clip7-words.txt` is comp = src − **1515**. This EDL is comp = src − **1530.50**.
> Use the comp values **in this file** (already re-based: `EDL_comp = table_comp − 15.50`). Each sub-comp GSAP offset
> = (comp fire) − (beat `data-start`). All fire-times below were re-verified word-by-word against `clip7-words.txt`.

---

## VIEW-TIMELINE (proves R1 + R7 — EVERY Mode-A segment names the graphic that fills it; none is graphic-less)

| seg | view | comp range | dwell | beat(s) in view | graphic that fills the LEFT zone for the ENTIRE segment | R1/R7 check |
|-----|------|-----------|-------|------------------|----------------------------------------------------------|-------------|
| **V1** | **full-frame** (both speakers) | 0.00 – 6.00 | **6.0s** | c7b1 opener kinetic | n/a — full-frame kinetic phrase-stack OVER both speakers (dark left gradient backdrop) + a small white eyebrow `THE EXIT PATTERN` (the A2-3 2nd element type). View = full-frame because content is a **kinetic over video**, not a left-zone card. R7 blank-left cannot apply to a full-frame view. | intro zone — quick switch allowed |
| **V2** | **Mode-A** (guest right 40%) | 6.00 – 31.70 | **25.7s** | c7b2 HERO narrative-cycle timeline | **c7b2 timeline left zone** — eyebrow `THE NARRATIVE CYCLE` (in @6.40, as the shrink completes) + neutral spine drawing (7.20) + 6 nodes popping (10.76…25.78). The n6 `?` then **holds and gently drifts down ~comp 31** (A2-5) so the pose leans into the spiral cut. A graphic occupies the left zone continuously from 6.40 to the 31.70 fade. **No graphic-less instant.** | ≥8s ✓ · graphic fills whole dwell ✓ |
| **V3** | **full-frame** (both speakers) | 31.70 – 49.00 | **17.3s** | c7b3 spiral · c7b4 examples · c7b5 cadence | n/a — all three are full-frame graphics OVER both speakers (two kinetic stacks + a lower-left chip strip). Continuous text on screen 34.16→48.6; the two ~0.6s inter-beat gaps are full-frame talking (R7-legal: full-frame = both speakers, never a cropped blank-left). **GROUPED — no view change inside this stretch (the kept R1 win).** | ≥8s ✓ · grouped, no bounce ✓ |
| **V4** | **Mode-A** (guest right 40%) | 49.00 – 66.50 | **17.5s** | c7b6 privacy+AI payoff card | **c7b6 card left zone** — eyebrow `WHAT COMES NEXT` (in @49.40) + liquid-glass card frame + accent bar (in @49.60) + match-cut `?→` glyph (50.44, A2-7) + `PRIVACY`/`AI` (51.42 / 52.94) + sublabel (54.54). Card holds, NEVER exits → graphic fills the left zone from 49.40 to clip end. **No graphic-less instant.** | ≥8s ✓ · graphic fills whole dwell to clip end ✓ |

**KEPT R1 WIN (A2-13 — do not regress):** the v3 reject had an A-B-A inside 41–49s. v4 groups spiral + examples +
cadence into the **single 17.3s full-frame V3 block with ZERO view changes between them.** This is the strongest
structural decision in the clip. A future reviewer must NOT "add variety" by re-splitting V3 into separate views —
that re-introduces the exact reject. The non-kinetic chip strip (c7b4) between the two kinetics is what keeps R2
(template variety) satisfied WITHOUT a view bounce.

**R7 blank-left audit (the rejection-cause fix):**
- V2 ENTRY: video shrinks full→Mode-A starting comp 6.0; the eyebrow + bg-glow fire @ **6.30–6.40** as the 0.7s
  shrink completes — the left-zone graphic is co-incident with Mode-A establishing. The 6.0–6.40 window is the entry
  ramp (video in motion, not a settled cropped blank frame), not a breath. PASS.
- V2 EXIT (the v3 bug): the inner-content fade AND the video full-expansion **both start comp 31.70** (fade 0.45s,
  expand 0.3s done by 32.0). The graphic is present until 31.70; from 31.70 the frame is already opening to full,
  full by 32.0 — i.e. the expand completes BEFORE the old 32.0 boundary. There is **no instant of a settled Mode-A
  crop with an empty left zone.** PASS. (v3 split these fade-31.6 / expand-32.0→32.4 → ~0.5s blank-left → REJECTED.)
- V4: card never exits → left zone occupied to clip end. PASS.
- Every full-frame segment (V1, V3) shows BOTH speakers; no full-frame moment is ever a cropped blank-left. PASS.

**A-B-A / dwell proof (R1):** full-frame at [0–6] and [31.7–49] → gap **25.7s** (>12s) ✓. Mode-A at [6–31.7] and
[49–66.5] → gap **17.3s** (>12s) ✓. No view returns within 12s. Switches at 6.0, 31.70, 49.0 only — **3 switches,
all spaced ≥17s.** Zero view changes inside the 31.7–49 stretch (spiral, examples, cadence ALL full-frame). **PASS.**

**Breath classification (R7):** there is **no intentional clean/breath beat sitting inside a Mode-A block.** Breaths,
where they fall, are inside the full-frame V1/V3 blocks (both speakers visible). The only near-graphic-less instants
are the sub-0.3s view-transition seams, handled above by co-incident graphic entry / coincident fade+expand.

---

## TEMPLATE VARIETY (proves R2)

| beat | template / device | kinetic? |
|------|-------------------|----------|
| c7b1 | `kinetic-type` (opener) | yes (1) |
| c7b2 | **decision-tree (HERO narrative timeline)** | no |
| c7b3 | `kinetic-type` (spiral) | yes (1) |
| c7b4 | **liquid-glass examples chip-row** | no |
| c7b5 | `kinetic-type` (cadence) | yes (1) |
| c7b6 | **liquid-glass payoff card** | no |

- Sequence: kinetic / tree / kinetic / card / kinetic / card. Max kinetics in a row = **1** (every kinetic bounded by
  a non-kinetic neighbor). 3+ in a row = FAIL → **PASS**.
- No same template twice in a row. **PASS**.
- Distinct primary device = narrative timeline, leads as the HERO (c7b2, the longest beat at 25.7s). No swiss-grid
  `07/EYEBROW/STAT/tag-row` opener exists. **PASS**.

**Catalog install vs hand-build:**
- c7b2 HERO timeline → `--example decision-tree` re-skinned vertical (built-in example). EDIT the existing
  `compositions/beat-c7b2-narrative-cycle.html` (remove `#b2-idx`, white-out n6 NEXT, drop n1 "2024", re-time fade,
  add the n6 hold-drift).
- c7b1 / c7b3 / c7b5 kinetics → `--example kinetic-type` (built-in). EDIT c7b1 (font 130px + 2nd-element eyebrow) and
  c7b3 (L4 split). c7b5 is correct — keep.
- c7b4 examples chip-row → hand-built liquid-glass tag strip (two chips `PERP DEXES`, `MEME COINS`). DESIGN.md card
  recipe (solid `rgba(20,26,34,0.92)` fill + 4px cyan bar + glow, **no blur, no grain**). Do NOT use
  `ios26-liquid-glass` / `macos-tahoe-liquid-glass` (they carry `backdrop-filter` blur). EDIT only the strip
  baseline (A2-6 face-clear).
- c7b6 payoff card → hand-built liquid-glass card (same recipe). Remove `#b6-idx`; keep glyph + words white; fix glyph
  fire-time; add the match-cut entry.

---

## OBJECT-POSITION (R-framing — KEPT from v3, verified by frame)

`object-position: 84% center` on `#short_mag_cut`. Mode-A geometry `left:1229, top:108, width:614, height:864`
(bottom clearance 108px >40px so the name never clips; top 108px >20px). With `object-fit:cover` scaling source by
height (×0.8), the 614px window shows a 768px source slice centered at `84%×1152+384 = 1352` → source x≈968–1736:
centers Jasper (face ≈x1400), keeps his "Jasper De Maere / Wintermute" lower-third (left edge ≈x990) inside
window-left (968), trims the dead right-wall. 50%→center 960 (the seam) and 62%→center 1098 (half-host) REJECTED.
**Builder: re-extract a Mode-A frame (`ffmpeg -ss 1582 -i source.mp4 -frames:v 1`) and LOOK before re-render.**

---

## BEAT TABLE

> `comp = src − 1530.50`. Every kinetic LINE quotes the transcript words it fires on, its `src_t`, the clip
> `comp_t` (re-based), and the in-beat GSAP offset = comp_t − beat `data-start`. EDITORIAL (label / anticipatory)
> lines are marked. All on-screen strings are post-`_JARGON.md`. **NO beat renders a clip number / index (R6).**

### c7b1 — KINETIC opener · **view V1 full-frame** (both speakers) → shrinks to Mode-A at comp 6.0
- **comp 0.0 – 6.0 · src 1530.50 – 1536.50**
- Template/block: `kinetic-type` — 3-line phrase build, lines slam in and **STAY** (no dim). Dark gradient backdrop
  in the left zone; full-frame video (both speakers) behind. Video shrinks to Mode-A at comp 6.0 as the stack wipes up.
- View: **full-frame** the whole opener. **NO index on screen.**
- Sub-comp file: `compositions/beat-c7b1-hook.html` · `data-start="0.0" data-duration="6.0"`
- **A2-2 FONT FIX — phrase lines `font-size: 108px` → `font-size: 130px`** (build line 56). DESIGN.md line 189
  mandates ~130px for kinetic phrase lines; at 108 the hook reads SMALLER than the c7b6 payoff words (130px) =
  inverted hierarchy on the most important 6 seconds. "WE ALWAYS EXIT" (14 chars) fits the 960px usable width
  (zone 1040px − 80px padding) at 130px Inter 900. *(c7b3 stays 92px — it is a 4-line stack; only the opener is the
  inverted-hierarchy problem.)*
- **A2-3 SECOND ELEMENT TYPE — add a small white eyebrow `THE EXIT PATTERN`** above the stack, slam @ offset **0.10**
  (Inter 700, 32px, `#F0F0F0`, letter-spacing 0.2em, the same `text-shadow` as the lines). This gives the opener a
  2nd distinct element TYPE (eyebrow + word-stack) so it is not a thin lone 3-line stack with a 1.9s gap to L2, and
  narrows the DESIGN.md "3 element types in 6s" expectation while staying full-frame and R7-legal.
  `<!-- EDITORIAL: opener eyebrow, white, NOT cyan (L3 remains the sole cyan); not word-synced -->`
- On-screen lines (R5 coherent: "WE ALWAYS EXIT / BEAR MARKETS / IN AN INTERESTING WAY"):

  | line | text | spoken words it fires on | src_t | **comp_t** | GSAP offset | color |
  |---|---|---|---|---|---|---|
  | eyebrow | `THE EXIT PATTERN` | (EDITORIAL label) | — | **0.10** | 0.10 | #F0F0F0 |
  | L1 | `WE ALWAYS EXIT` | "we always exit" | we 1530.76 | **0.26** | 0.26 | #F0F0F0 |
  | L2 | `BEAR MARKETS` | "bear markets" | bear 1532.66 | **2.16** | 2.16 | #F0F0F0 |
  | L3 | `IN AN INTERESTING WAY` | "in a very interesting fashion" | interesting 1535.02 | **4.52** | 4.52 | **#00D4FF** (payoff) |

  - L3 condenses spoken "in a very interesting fashion" → on-screen `IN AN INTERESTING WAY`, fired on "interesting"
    @comp 4.52 (literal-word match, not anticipatory). **Cyan: L3 ONLY** (the new eyebrow is white — ≤1 cyan holds).
    Stack + eyebrow drift up & out at ~5.6 (before the Mode-A shrink at 6.0). `data-duration` 6.0 covers eyebrow 0.10
    → L3 4.52 + headroom.
  - **R7/DESIGN.md reconciliation (Agent-3 fix #6):** this opener is a FULL-FRAME kinetic over BOTH speakers (per
    R1/R7 view-discipline: kinetic → full-frame). **R7 intentionally SUPERSEDES DESIGN.md's older "speaker framed
    RIGHT from t=0 + ≥3 different element TYPES before t=6" mandate (DESIGN.md lines 10–42, QA lines 348–351) for
    this opener.** The added eyebrow (A2-3) gives a 2nd element type and narrows the gap, but the gate must NOT
    FAIL this opener on QA lines 349–350 for being full-frame / for showing both speakers: a full-frame kinetic
    opener is the correct, R7-compliant choice, and dialog-match §3 (first text by ~0.3s) is met at 0.10.

### c7b2 — DECISION-TREE: narrative-cycle TIMELINE (HERO) · **view V2 Mode-A** · **NO "07" INDEX (R6 fix)**
- **comp 6.0 – 31.7 · src 1536.50 – 1562.20**
- Template/block: `decision-tree` (`--example decision-tree`) re-skinned as a **vertical narrative-cycle timeline**
  (neutral #2A2A2A spine slow-draws top→bottom; nodes pop `back.out(1.5)` ON their spoken era). HERO centerpiece.
- View: **Mode-A** (object-position 84%); `#bg-glow` + `#zone-rule` fade in at **6.30** (as the 0.7s shrink completes
  — graphic co-incident with Mode-A; see R7 audit). **NO index on screen.**
- Sub-comp file: `compositions/beat-c7b2-narrative-cycle.html` · `data-start="6.0" data-duration="25.7"`
- **R6 FIX — DELETE the index:** remove the `<div id="b2-idx">07</div>` node (**build line 34**), its `#b2-idx` CSS
  block (**build lines 112–116**), and its GSAP tween (**build line 197**). The eyebrow becomes the topmost
  left-zone element. *(Also drop the now-orphaned `tl.fromTo("#b2-idx", …)` line.)*
- Eyebrow (EDITORIAL label — `<!-- EDITORIAL: section label, not word-synced -->`): `THE NARRATIVE CYCLE`
  — Inter 700, 34px, #F0F0F0, slam @ comp 6.40 (offset 0.40). (Shares no notable word with any node — R4 within-beat OK.)
- Spine (#2A2A2A, neutral — NOT cyan) slow-draws from comp ~7.2 (offset 1.2) across the beat.
- **Nodes — SPOKEN ORDER (DePIN present as n4 per R3; n1 carries NO on-screen date per Agent-3 fix #5):**

  | node | on-screen text | spoken words it fires on | src_t | **comp_t** | GSAP offset | color |
  |---|---|---|---|---|---|---|
  | n1 | `ETF ANNOUNCEMENTS` | "the sort of 24, we had the **ETF** announcements" | ETF 1541.26 | **10.76** | 4.76 | #F0F0F0 |
  | n2 | `ORDINALS + INSCRIPTIONS` | "suddenly we had like **inscriptions** and ordinals" | inscriptions 1543.76 | **13.26** | 7.26 | #F0F0F0 |
  | n3 | `DeFi SUMMER` | "excited about like Bitcoin, **DeFi**" | DeFi 1547.58 | **17.08** | 11.08 | #F0F0F0 |
  | **n4** | **`DePIN`** / `Decentralized Physical Infra.` | "Then we had **deep intaking off**" → **DePIN** (`_JARGON.md`, user-flagged) | deep 1549.02 | **18.52** | 12.52 | #F0F0F0 |
  | n5 | `AI AGENTS` | "Then we had **AI** agents… very early inflection" | AI 1550.82 | **20.32** | 14.32 | #F0F0F0 |
  | n6 | `?` / `NEXT` | "I'm very **curious** what we will come up with as the next narrative" (EDITORIAL turn) | curious 1556.28 | **25.78** | 19.78 | **cyan node** (see below) |

  - **n1 — NO on-screen date (Agent-3 fix #5):** renders `ETF ANNOUNCEMENTS` ALONE. The literal `2024` is DROPPED
    (DESIGN.md line 6 + QA §8 ban on-screen "2024"/"2025" date labels; this also matches n2/n3/n5 which carry no
    date, resolving the lone-date inconsistency). **DELETE the `.b2-yr` `2024` element** (**build line 45**). *(The
    `.b2-yr` CSS block at build lines 149–152 becomes orphaned — remove or leave; no other node uses it.)*
    `<!-- DATE: per DESIGN.md/QA, no on-screen year; he names "24" by ear, but the node label is event-only -->`
  - **n4 DePIN is the critical R3 add.** Sublabel `Decentralized Physical Infra.` (Inter 600, ≥32px, #F0F0F0) KEPT —
    the only node a 1080p viewer cannot decode from the acronym alone.
    `<!-- JARGON: Whisper "deep intaking off" → DePIN per _JARGON.md (user-flagged confirmed) -->`
  - **n6 cyan discipline (Agent-3 fix #7) — n6 is ONE cyan accent unit:** the open `?` glyph (#00D4FF, 64px so the
    muted-grey rule is moot) + the node dot (cyan fill rgba(0,212,255,0.18) + #00D4FF border + glow). The **`NEXT`
    sublabel renders `#F0F0F0`** — change the build CSS `.b2-label-open` `color: #00d4ff` → `#f0f0f0` and drop its
    cyan `text-shadow` (**build lines 183–186**). Per the §8 carve-out "tree: final node = the one cyan element,"
    the `?`+dot read as a single cyan accent; the white `NEXT` makes n6 unambiguously one cyan unit.
    `<!-- EDITORIAL: n6 "?" open-question turn, fires on "curious" — anticipatory of the c7b6 answer -->`
  - **A2-5 + A2-7 — the n6 `?` is the bridge into the spiral AND the match-cut anchor for c7b6.** After n6 pops
    (offset 19.78 / comp 25.78), hold it, then give it a **subtle downward drift @ ~comp 31** (e.g.
    `tl.to("#b2-n6", {y: 18, duration: 0.6, ease: "power1.in"}, 24.5)`) so the open question visually leans toward
    the spiral cut — this softens the ~comp 26–34 lull (the one felt dead spot, where he finishes "…what we will
    come up with as the next narrative… it's a spiral"). Note for c7b6: the `?` glyph here is **64px**; record its
    on-screen position so c7b6's `?→` can enter at a matched size/position (A2-7 match-cut).
  - 6 nodes fit the left zone: per-node `margin-bottom` 22px, spine height 600px (already set in build).
  - **Inner-content fade + master video-expansion BOTH start comp 31.70 (offset 25.70)** (REJECTION CAUSE 2 fix —
    no blank-left seam). Move the build fade from offset **25.6 → 25.70** (build line 226). The inner fade is 0.45s;
    the master video-expand (in index.html) is 0.3s and completes by 32.0. `data-duration` **25.7** covers n1 10.76 →
    n6 25.78 → fade 31.70.
  - **`data-duration` 26.0 → 25.7** in TWO places: the sub-comp root `<div data-composition-id …>` (**build line 22**)
    AND the index `#beat-c7b2-narrative-cycle` div (**index.html line 99**). Until both read 25.7 the beat is still
    authored to the old 32.0 (blank-left) boundary.
  - Cyan element: n6 only (one cyan unit). PASS.

---
**↓↓ view V3 full-frame block (31.7–49.0) — c7b3, c7b4, c7b5 all render full-frame; NO view change between them ↓↓**

### c7b3 — KINETIC: the "spiral" mechanism · **view V3 full-frame** (both speakers)
- **comp 32.0 – 41.2 · src 1562.50 – 1571.70** (`data-start="32.0"`; the master video-expand STARTS 31.70 and
  completes by 32.0, so the frame is already full when this beat's text begins at 34.16 — well clear)
- Template/block: `kinetic-type` — 4-line phrase build, lines STAY. Explains WHY the cycle repeats.
- View: **full-frame** — video expansion completes by 32.0 (started 31.70); Ken-Burns reset. Stays full for c7b4 & c7b5 too.
- Sub-comp file: `compositions/beat-c7b3-spiral.html` · `data-start="32.0" data-duration="9.2"`
- Word-synced (spoken: "it's a spiral where like prices go up. We find the narrative. People get excited about it late in the cycle."):

  | line | text | spoken words it fires on | src_t | **comp_t** | GSAP offset | color |
  |---|---|---|---|---|---|---|
  | L1 | `IT'S A SPIRAL` | "a spiral where" | spiral 1564.66 | **34.16** | 2.16 | #F0F0F0 |
  | L2 | `PRICES GO UP` | "like prices go up" | prices 1565.70 | **35.20** | 3.20 | #F0F0F0 |
  | L3 | `WE FIND THE NARRATIVE` | "We find the narrative" | We 1567.02 | **36.52** | 4.52 | #F0F0F0 |
  | L4a | `EXCITED` | "**excited** about it" | excited 1568.34 | **37.84** | 5.84 | #F0F0F0 |
  | L4b | `LATE IN THE CYCLE` | "**late** in the cycle" | late 1569.32 | **38.82** | 6.82 | **#00D4FF** (payoff) |

  - **A2-4 cyan-on-payoff fix (REPLACES the v3 single-line L4).** v3 fired the whole cyan line `EXCITED LATE IN THE
    CYCLE` on "People" (comp 37.52) — 2.9s before "cycle" (comp 40.46) is spoken, so the cyan payoff pre-empted the
    audio. v4 splits it: `EXCITED` (white) lands on the spoken word **"excited" @ comp 37.84**, and `LATE IN THE
    CYCLE` (cyan) lands on **"late" @ comp 38.82** — the cyan now hits the literal payoff, tightly word-synced. Both
    render on the same stack line position (L4a then L4b appears beneath, or L4 reveals in two slams — builder's
    choice, but the cyan must be the "LATE IN THE CYCLE" run). **Cyan: the `LATE IN THE CYCLE` run ONLY.**
    `<!-- A2-4: split former single L4; cyan now on the spoken payoff "late...cycle", not anticipatory on "People" -->`
  - *(Fire-time provenance: table "excited" 53.34 → 53.34−15.50 = 37.84; "late" 54.32 → 38.82; "cycle" 55.96 →
    40.46. All from `clip7-words.txt`.)*
  - `data-duration` 9.2 covers L1 34.16 → L4b 38.82, lines hold to ~40.8 then exit (no view change — video stays
    full into c7b4).

### c7b4 — LIQUID-GLASS examples chip-row · **view V3 full-frame** (over both speakers)
- **comp 41.2 – 45.2 · src 1571.70 – 1575.70**
- Template/block: **hand-build** liquid-glass tag strip — two chips slam in, each on its spoken example. Non-kinetic
  device placed BETWEEN the two kinetics (c7b3, c7b5) so kinetics never run 3-in-a-row and the same template never
  repeats back-to-back. **Lower-left strip over the full-frame video (both faces visible)** — a supplemental overlay,
  NOT a left-zone card, so the view stays full-frame (R7-correct: no crop, no blank half). Card recipe (DESIGN.md):
  solid `rgba(20,26,34,0.92)` fill, 4px cyan accent bar (inset left), soft glow, 1px border, `mask-image` feather to
  the right, own dark readability backdrop. **NO backdrop-filter blur. NO grain.**
- View: **full-frame** — video stays full from c7b3 (NO view change). **NO index on screen.**
- Sub-comp file: `compositions/beat-c7b4-examples.html` · `data-start="41.2" data-duration="4.0"`
- **A2-6 FACE-CLEAR FIX — raise the strip so it doesn't cover the HOST.** Source is SIDE-BY-SIDE (Nic/host LEFT,
  Jasper/guest RIGHT — QA line 6); a full-frame two-shot puts Nic's face in the left half, exactly where this strip
  sits. Current build: `#b4-backdrop` `bottom:0 height:560px` (line 47), `.b4-zone` `bottom:0 height:420px` with
  `padding: 0 80px 96px 80px` (line 61) — the backdrop top edge reaches ~y520, mid-frame, over Nic's chin/mouth.
  **Raise the strip baseline** (e.g. `.b4-zone` → `bottom: 96px`, and/or shrink `#b4-backdrop` `height: 420px` and
  push its `bottom` up) so the strip + its backdrop's top edge clear both speakers' chins. **VERIFY by frame at
  comp 42** (§9): the strip must not cross either mouth; if it does, raise further. *(Chips are 52px — readable;
  font is fine. This is purely a vertical-position safety fix per the "supplemental overlays only / lower-third
  y≥740" memory note.)*
- Eyebrow (EDITORIAL label): **`EVERY CYCLE'S TOYS`** — Inter 700, 32px, #F0F0F0 @ comp 41.4 (offset 0.20).
  `<!-- EDITORIAL: section label, not word-synced. ONE string everywhere: EVERY CYCLE'S TOYS (Agent-3 fix #2) -->`
- Chips (each slams in `back.out(1.5)` on its spoken word):

  | chip | on-screen text | spoken words it fires on | src_t | **comp_t** | GSAP offset | color |
  |---|---|---|---|---|---|---|
  | c1 | `PERP DEXES` | "we had like perp dexes" | perp 1572.36 | **41.86** | 0.66 | #F0F0F0 (fill #141A22) |
  | c2 | `MEME COINS` | "meme coin launch platforms" | meme 1573.46 | **42.96** | 1.76 | #F0F0F0 (fill #141A22) |

  - `<!-- JARGON: spoken Whisper "perp dexes" OK; "meme con" → MEME COINS per _JARGON.md -->`
  - **R4 check** for eyebrow `EVERY CYCLE'S TOYS` vs chips `PERP DEXES` / `MEME COINS`: no shared notable word
    ("cycle"/"toys" ≠ "perp"/"dexes"/"meme"/"coins"). PASS.
  - Cyan element: the single 4px accent bar on the strip (chips themselves are neutral #141A22). PASS.
  - Strip exits ~44.8 (no view change — video stays full into c7b5).

### c7b5 — KINETIC: "cadence of innovation" bridge · **view V3 full-frame** (both speakers)
- **comp 45.2 – 49.0 · src 1575.70 – 1579.50**
- Template/block: `kinetic-type` — 2-line phrase build. The thesis bridge before the Mode-A payoff.
- View: **full-frame** — video still full (NO view change since c7b3). Switches to Mode-A only at comp 49.0 (next beat).
- Sub-comp file: `compositions/beat-c7b5-cadence.html` · `data-start="45.2" data-duration="3.8"` · **KEEP as-is**
  (already 124px lines, L1@45.58 / L2@46.14, L2 cyan, no index).
- Word-synced (spoken: "But that cadence of innovation, I think is super interesting to see."):

  | line | text | spoken words it fires on | src_t | **comp_t** | GSAP offset | color |
  |---|---|---|---|---|---|---|
  | L1 | `THE CADENCE` | "that cadence of" | cadence 1576.08 | **45.58** | 0.38 | #F0F0F0 |
  | L2 | `OF INNOVATION` | "of innovation" | innovation 1576.64 | **46.14** | 0.94 | **#00D4FF** (payoff) |

  - Cyan: L2 only. Lines hold to ~48.6 then exit as video shrinks to Mode-A for c7b6. `data-duration` 3.8 covers L1 45.58 → L2 46.14.

---
**↑↑ end view V3 full-frame block ↑↑** — single switch to Mode-A at comp 49.0 below.

### c7b6 — LIQUID-GLASS payoff card: the "?" RESOLVES → PRIVACY + AI · **view V4 Mode-A** · **NO "07" INDEX (R6 fix)**
- **comp 49.0 – 66.5 · src 1579.50 – 1597.00** (clip end)
- Template/block: **hand-build** liquid-glass card (DESIGN.md recipe: `rgba(20,26,34,0.92)` fill, 4px cyan accent
  bar inset-left, glow, 1px border, `mask-image` feather right). **NO blur, NO grain.** Pays off c7b2's open `?`.
- View: **Mode-A** (object-position 84%); video shrinks full→Mode-A at comp 49.0, `#bg-glow`+`#zone-rule` return @49.3.
  Card holds over live continuing speaker video to clip end (never exits → left zone occupied to 66.5). **NO index.**
- Sub-comp file: `compositions/beat-c7b6-privacy-ai.html` · `data-start="49.0" data-duration="17.5"`
- **R6 FIX — DELETE the index:** remove the `<div id="b6-idx">07</div>` node (**build line 35**), its `#b6-idx` CSS
  block (**build lines 86–90**), and its GSAP tween (**build line 143**). The eyebrow becomes the topmost left-zone
  element. *(Also drop the orphaned `tl.fromTo("#b6-idx", …)` line.)*
- **A2-7 MATCH-CUT — the `?→` rhyme lands harder.** c7b2's open node ends on a 64px cyan `?`; this card's `?→` glyph
  should **enter at the same size/screen position that c7b2's `?` occupied** (a match-cut feel across the 17s V3
  block), then the `→ PRIVACY / AI` resolves it. The glyph here is currently 72px `#F0F0F0` (build line 116) — keep
  it white (one-cyan), but tune its entry so it reads as the SAME `?` returning (e.g. fade/scale from the c7b2
  position rather than a generic x-slide). Pure polish; do not let it add a 2nd cyan.
- Eyebrow (EDITORIAL label): `WHAT COMES NEXT` — Inter 700, 32px, #F0F0F0 @ comp 49.4 (offset 0.40).
  `<!-- EDITORIAL: section label. R4: "frontrunners" appears ONLY in the sublabel below, NOT here -->`
- Word-synced reveal (spoken: "anyone's guess currently **privacy and AI**… top of mind for many… the **front runners** in terms of what we might see"):

  | element | on-screen text | spoken words it fires on | src_t | **comp_t** | GSAP offset | color |
  |---|---|---|---|---|---|---|
  | glyph | `?  →` (72px) | (EDITORIAL rhyme; fires on "guess" — the "anyone's guess" turn into the answer) | guess 1580.94 | **50.44** | **1.44** | #F0F0F0 |
  | W1 | `PRIVACY` (130px) | "currently privacy" | privacy 1581.92 | **51.42** | 2.42 | #F0F0F0 |
  | W2 | `AI` (130px) | "and AI" | AI 1583.44 | **52.94** | 3.94 | #F0F0F0 |
  | sub | `Top of mind — the frontrunners` (28px) | "top of mind for many… the front runners" | mind 1585.04 / front 1587.84 | **54.54** | 5.54 | #F0F0F0 |

  - **`?→` glyph fire-time (Agent-3 fix #3):** offset **1.44 (comp 50.44)** everywhere — fired on "guess" @
    src1580.94 → comp 50.44 → offset 50.44 − 49.0 = 1.44. **Build script line 148 currently uses `1.40` → CHANGE to
    `1.44`.**
  - **ONE-CYAN (Agent-3 fix #1 — the headline fail):** the **4px accent bar is the SOLE cyan element.** The `?→`
    glyph and BOTH answer words are `#F0F0F0`. **There is NO underline sweep.** At no instant of c7b6 is >1 cyan
    element visible. The current build file ALREADY renders glyph + words `#f0f0f0` with the bar as sole cyan and
    has no `.b6-uline` — **keep it; do not regress.**
  - **R4 PASS:** notable word "frontrunners" appears ONLY in `sub`; eyebrow is `WHAT COMES NEXT` (no shared word).
    `<!-- JARGON: spoken "front runners" → on-screen "frontrunners" (one word), single occurrence -->`
  - **R-no-outro (D4):** this is a CONTENT reveal (the thesis answer), NOT a name/credit card. **NO "Jasper De Maere
    · Wintermute" attribution in the overlay** (the name in the FRAME is the source video's own caption, not a
    generated card). Card lands on "privacy and AI," holds while he finishes "…either completely in that vertical or
    at least adjacent to it" (it @ src1595.84 / comp 65.34). Clip ends on this live content beat; final ~1.2s is the
    card gently settling over continuing video — not a frozen end screen.
  - Cyan element: the 4px accent bar only. PASS.

---

## AGENT-3 FIXES (the seven prior-round contradictions — each resolved; STATUS = on-disk reality)

| # | issue | v4 resolution | where in build | on-disk status |
|---|-------|---------------|----------------|----------------|
| 1 | c7b6 THREE cyan (bar + `?→` glyph + underline) | `?→` glyph + words `#F0F0F0`; **NO underline sweep**; bar = sole cyan. ≤1 cyan always. | `beat-c7b6` (`#b6-q` + `.b6-word` already `#f0f0f0`; no `.b6-uline`) | **already correct — KEEP** |
| 2 | c7b4 eyebrow `EXAMPLES` vs `EVERY CYCLE'S TOYS` | ONE string: **`EVERY CYCLE'S TOYS`** everywhere. | `beat-c7b4` `#b4-eye` | **already correct — KEEP** |
| 3 | c7b6 `?→` glyph time 1.40 vs 1.44 | **offset 1.44 (comp 50.44)** — on "guess" @ src1580.94. | `beat-c7b6` line 148 `1.40` → `1.44` | **NOT DONE — disk reads 1.40** |
| 4 | V2→V3 seam blank-left (fade 31.6 vs expand 32.0) | fade + expand **both start comp 31.70**; expand 0.3s done by 32.0. | `beat-c7b2` fade `25.6`→`25.70` (line 226); `index.html` PHASE-2 expand start `32.0`→`31.70` + dur `0.4`→`0.3` (lines 183–186) | **NOT DONE — disk: fade 25.6, expand 32.0** |
| 5 | c7b2 n1 literal "2024" vs date ban | **DROP the year**; render `ETF ANNOUNCEMENTS` alone. | `beat-c7b2` DELETE `.b2-yr` node (line 45) | **NOT DONE — disk has `.b2-yr` "2024"** |
| 6 | c7b1 opener vs DESIGN.md "speaker-right + 3 types" | note: **R7 SUPERSEDES**; + A2-3 adds a 2nd element type (eyebrow). Gate must not FAIL on QA lines 349–350. | EDL note + `beat-c7b1` add eyebrow | EDL note + new eyebrow (A2-3) |
| 7 | c7b2 n6 multiple cyan (dot + `?` + cyan `NEXT`) | **`NEXT` → `#F0F0F0`**; only `?` glyph + dot cyan. | `beat-c7b2` `.b2-label-open` `#00d4ff`→`#f0f0f0`, drop cyan text-shadow (lines 183–186) | **NOT DONE — disk: `NEXT` is `#00d4ff`** |

---

## SUB-COMP FILES (compositions/) — v4 actions

| beat | sub-comp filename | data-start | data-duration | v4 action |
|------|-------------------|-----------|---------------|-----------|
| c7b1 | `beat-c7b1-hook.html` | 0.0 | 6.0 | **EDIT** — (A2-2) phrase lines `font-size: 108px` → **130px** (line 56); (A2-3) ADD white eyebrow `THE EXIT PATTERN` @ offset 0.10 (Inter 700, 32px, #F0F0F0). KEEP L1@0.26 / L2@2.16 / L3@4.52 (L3 cyan), no index, ≤1 cyan (eyebrow white). |
| c7b2 | `beat-c7b2-narrative-cycle.html` | 6.0 | **25.7** | **EDIT** — (a) R6: DELETE `#b2-idx` "07" node (L34) + CSS (L112–116) + tween (L197); (b) fix #5: DELETE n1 `.b2-yr` "2024" node (L45); (c) fix #7: `.b2-label-open` (NEXT) `#00d4ff`→`#f0f0f0`, drop its cyan text-shadow (L183–186); (d) fix #4: move inner-fade offset 25.6 → **25.70** (L226); (e) `data-duration` 26.0 → **25.7** (L22); (f) A2-5: add n6 hold + downward drift @ ~offset 24.5–25. Keep the DePIN sublabel, n6 `?`+dot cyan, all node fire-times. |
| c7b3 | `beat-c7b3-spiral.html` | 32.0 | 9.2 | **EDIT** — (A2-4) split L4: `EXCITED` (white) on "excited" offset **5.84** (comp 37.84); `LATE IN THE CYCLE` (cyan) on "late" offset **6.82** (comp 38.82). Replaces the v3 single cyan line on "People" (5.52). KEEP L1@2.16 / L2@3.20 / L3@4.52, no index. |
| c7b4 | `beat-c7b4-examples.html` | 41.2 | 4.0 | **EDIT** — (A2-6) raise the strip baseline so the strip + backdrop clear the HOST's face on the full-frame two-shot (`.b4-zone bottom:0`→`96px`; shrink/raise `#b4-backdrop`). VERIFY by frame at comp 42. KEEP eyebrow `EVERY CYCLE'S TOYS`, chips `PERP DEXES`/`MEME COINS`, accent-bar sole cyan, no index. |
| c7b5 | `beat-c7b5-cadence.html` | 45.2 | 3.8 | **KEEP** — already correct (L1@45.58 / L2@46.14, L2 cyan, 124px, no index). |
| c7b6 | `beat-c7b6-privacy-ai.html` | 49.0 | 17.5 | **EDIT** — (a) R6: DELETE `#b6-idx` "07" node (L35) + CSS (L86–90) + tween (L143); (b) fix #3: `#b6-q` GSAP offset 1.40 → **1.44** (L148); (c) A2-7: tune the `?→` entry as a match-cut from c7b2's `?` size/position. Glyph/words already `#f0f0f0`, accent bar sole cyan, no underline — **confirm, no other cyan change (fix #1)**. |

**`index.html` — v4 actions:**
- **No change to media/duration:** `data-media-start="1530.50"`, `data-duration="66.5"` on `#short_mag_cut`,
  `#a-roll-audio`; `data-duration="66.5"` on `#master-root`. (All correct on disk.)
- **z-index:3 rule** lists exactly the **6** beat ids (already correct — KEEP): `#beat-c7b1-hook,
  #beat-c7b2-narrative-cycle, #beat-c7b3-spiral, #beat-c7b4-examples, #beat-c7b5-cadence, #beat-c7b6-privacy-ai`.
- **c7b2 `data-duration` 26.0 → 25.7** on the `#beat-c7b2-narrative-cycle` div (**index.html line 99**) — the SECOND
  of the two locations (the first is the sub-comp root, line 22). BOTH must read 25.7.
- **Master GSAP phase map — KEEP the 3-switch structure; ONE change at PHASE 2 (the R7 seam fix, fix #4):**
  - PHASE 1 @ comp **6.0** — full→Mode-A (0.7s shrink; glow/zone-rule in @6.3); Ken-Burns across timeline. KEEP.
  - PHASE 2 — **move the Mode-A→full video expansion EARLIER to coincide with the c7b2 fade:** glow/zone-rule out
    **@31.70** (already 31.7 on disk — KEEP); **change the video `to {left:0, top:0, width:1920, height:1080}` start
    from 32.0 → 31.70 AND its duration from 0.4 → 0.3** (**index.html lines 183–186**) so it completes by 32.0;
    Ken-Burns reset @31.70 (already 31.7 — KEEP). (v3 had glow-out @31.7 but the video-expand at 32.0/0.4 → the
    blank-left seam.) Holds full through 49.0 — NO intermediate switches (c7b3/c7b4/c7b5 all in the one full-frame
    window).
  - PHASE 3 @ comp **49.0** — full→Mode-A (0.7s shrink; glow/zone-rule return @49.3); gentle settle to clip end. KEEP.
- `object-position: 84% center` on `#short_mag_cut`. **KEEP (verified).**

---

## VERIFICATION CHECKLIST (graded vs `_QA-CHECKLIST.md` + DESIGN.md R6/R7)

> **These are UNCHECKED TODOs, not PASSes.** On-disk reality at last read is noted per item. The builder makes the
> edit, runs the grep assertion, THEN extracts the frame, THEN may tick the box. A v3 reject shipped because these
> were prematurely marked PASS — do not repeat that.

- **§1 R6 — NO index on screen:**
  `[ ]` c7b2: DELETE `#b2-idx` "07" node (L34) + CSS (L112–116) + tween (L197). **NOT YET DONE.**
  `[ ]` c7b6: DELETE `#b6-idx` "07" node (L35) + CSS (L86–90) + tween (L143). **NOT YET DONE.**
  **QA gate:** `grep -rn '>07<\|"07"\|b2-idx\|b6-idx' compositions/` must return ZERO hits. Eyebrows are editorial
  labels (allowed); only the bare number/index id is the FAIL.

- **§1 R7 — view matches content / NO blank-left Mode-A:**
  `[ ]` Move c7b2 inner-fade 25.6 → 25.70 (L226). **NOT YET DONE — disk reads 25.6.**
  `[ ]` Move `index.html` video-expand start 32.0 → 31.70 AND dur 0.4 → 0.3 (L183–186). **NOT YET DONE — disk: 32.0 / 0.4.**
  When done: every Mode-A segment (V2, V4) has a left-zone graphic for its ENTIRE duration — V2 = eyebrow @6.40 +
  spine + nodes (6.40→31.70 fade, n6 drift-bridge); V4 = card eyebrow @49.40 + shell @49.60 + glyph/words/sub, never
  exits. The V2→V3 blank-left seam is eliminated (fade + expand both @31.70, expand done by 32.0). Clean/kinetic
  beats (V1, V3) are full-frame with both speakers. **QA gate:** in `index.html` the video-expand `to{left:0…}`
  position must be ≤ the c7b2 fade start (both 31.70); confirm by frame at comp 31.8/32.0/32.2/32.4 (§9).

- **§1 R1 view discipline:** 4 views, dwell 6.0 / 25.7 / 17.3 / 17.5; only the 6.0 is intro-zone; others ≥17s. No
  A-B-A within 12s (full gap 25.7s, Mode-A gap 17.3s). spiral+examples+cadence GROUPED full-frame (the KEPT win —
  do not re-split). 3 switches, ≥17s apart. **PASS by design** (structure unchanged from v3's correct grouping).

- **§3a graphic density (A2-8):** clip = **66.5s (<90s)** → DESIGN.md line 358 "minimum 8 graphic beats for clips
  over 90s" is **N/A**. **6 beats is the correct density.** (Stated explicitly so a QA agent does not false-FAIL the
  6-beat count against the >90s rule.)

- **§2 R2 variety:** kinetic / tree / kinetic / card / kinetic / card — max 1 kinetic in a row; no same template
  back-to-back; HERO = narrative timeline (longest beat). No swiss-grid index/stat opener. **PASS by design.**

- **§3 dialog-match + word-sync:**
  `[ ]` c7b1 font 108 → 130 (L56) — A2-2. **NOT YET DONE.**
  `[ ]` c7b1 add eyebrow `THE EXIT PATTERN` @0.10 — A2-3. **NOT YET DONE.**
  `[ ]` c7b3 split L4: EXCITED @37.84 (white) / LATE IN THE CYCLE @38.82 (cyan) — A2-4. **NOT YET DONE — disk fires the cyan line on "People" @37.52.**
  `[ ]` c7b6 glyph 1.40 → 1.44 — fix #3. **NOT YET DONE.**
  Opens ON "we always exit bear markets" (we @ comp 0.26, first text ≤0.3, eyebrow @0.10); every kinetic line fires
  at comp = word.src − 1530.50 from `clip7-words.txt`; editorial labels marked. **QA gate:** re-verify each fire-time
  against the word table (`EDL_comp = table_comp − 15.50`): glyph "guess" 65.94→50.44; "excited" 53.34→37.84; "late"
  54.32→38.82.

- **§4 R5 coherence:** `WE ALWAYS EXIT / BEAR MARKETS / IN AN INTERESTING WAY` is a complete thought; cyan payoff is
  a real phrase, no dangling number. **PASS by design.**

- **§5 framing:**
  `[ ]` A2-6: raise c7b4 strip so it clears the HOST's face on the full-frame two-shot. **NOT YET DONE.**
  object-position 84% centers Jasper (re-verify by frame before render); opener + V3 full-frame beats show BOTH
  speakers, never text-on-black. **QA gate:** frame at comp 42 must show the c7b4 strip NOT crossing either
  speaker's mouth; frame at comp 20 (Mode-A) must show Jasper centered, name tag visible, no host bleed.

- **§6 R3 jargon:** **DePIN** node present (not "deep in"); **perp dexes** + **meme coins** (not "burp"/"meme con");
  DePIN/DeFi spelled per `_JARGON.md`; **no on-screen date at all** once the n1 "2024" is dropped.
  `[ ]` DELETE n1 `.b2-yr` "2024" (L45) — fix #5. **NOT YET DONE.** **QA gate:** `grep -rn '2024\|2025' compositions/`
  must return ZERO hits in rendered text.

- **§7 R4 dup words:** c7b6 eyebrow `WHAT COMES NEXT` vs sublabel `…the frontrunners` — "frontrunners" once.
  c7b4 eyebrow `EVERY CYCLE'S TOYS` vs chips `PERP DEXES`/`MEME COINS` — no shared word. c7b2 eyebrow `THE NARRATIVE
  CYCLE` shares no word with any node; c7b1 new eyebrow `THE EXIT PATTERN` shares no word with the lines. **PASS by design.**

- **§8 hard rules — ONE CYAN per beat (re-verify after edits):**
  `[ ]` c7b2 n6: white-out `NEXT` (L183–186) so n6 = one cyan unit (`?`+dot). **NOT YET DONE.**
  **QA gate:** `grep -c '#00d4ff\|#00D4FF' beat-c7b2-narrative-cycle.html` — after the fix the cyan hits are ONLY
  the n6 unit: `.b2-dot-open` bg + border + box-shadow, and `.b2-q` color + text-shadow (the `#bg-glow`/`#zone-rule`
  are in index.html, not this file). `.b2-label-open` must read `#f0f0f0`. Per beat: c7b1 L3 / c7b2 n6 one-unit
  [`?`+dot; NEXT white] / c7b3 LATE-IN-THE-CYCLE run / c7b4 accent bar / c7b5 L2 / **c7b6 accent bar ONLY [glyph+words
  white, no underline]**. No blur, no grain; cards = solid fill + cyan bar + glow + mask feather; eyebrows Inter 700
  ≥32px #F0F0F0; muted text #B6BEC6 (no #888); no on-screen 2025/2024 date; no intro/outro/CTA card; ends on live
  content; phrase kinetics build & STAY (no dim).

- **§9 verify-by-frame (MANDATORY after re-render — LOOK, don't self-report):** extract frames at:
  - opener (comp 3 — **confirm 130px lines + eyebrow `THE EXIT PATTERN`**, both speakers, no index),
  - V1→V2 seam (comp 6.4 — timeline eyebrow present, no blank crop),
  - DePIN node (comp 20 — Jasper centered Mode-A, name visible),
  - **V2→V3 seam — sample comp 31.8, 32.0, 32.2, 32.4 (A2-9: the blank-left risk opens BETWEEN 31.7 and 32.0; 32.2
    is the worst frame). CONFIRM NO blank-left cropped frame; fade + expand coincide @31.70, expand done by 32.0**,
  - spiral (comp 38.8 — **confirm `LATE IN THE CYCLE` is the cyan run, fired on "late"**),
  - chips (comp 42 — **confirm the strip clears BOTH speakers' faces, A2-6**),
  - cadence (comp 46),
  - V3→V4 seam (comp 49.3 — card shell + eyebrow present, NOT a blank left zone),
  - n6 (comp 28 — **confirm ONLY `?`+dot cyan, NEXT white**),
  - c7b6 payoff (comp 53 — **confirm ONLY the accent bar cyan; glyph + words white; no underline; `?→` match-cut**),
  - end (comp 66).
  **Confirm NO "07" anywhere** (`grep` + frame). LOOK before claiming done.

**Build Manifest Row:** `clip_7 | clip-7-bear-market-exit | 1530.50 | 1597.0 | narrative-timeline (decision-tree HERO) | 6 beats`
