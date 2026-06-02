# Clip 4 — Oct 10 Crash (ADL Cascade) — EDL **v4** (BUILD-READY, supersedes clip4-edl-v3.md)

**Source:** `src_in 1030.76 → src_out 1118.98` | **Duration 88.2s** | **Slug:** `clip-4-oct10-crash`
**Comp offset:** `comp_t = src_t − 1030.76` (word-table `clip4-words.txt` uses offset 1010, so `EDL comp = words.txt comp − 20.76`). **See the EDL-comp column added to the inlined table below — read fire-times off the `comp_t` column directly; never compute.**
**Beat count:** 7 (c4b1, c4b2, c4b3, c4b4, c4b5, c4b6, c4b8 — id `c4b7` intentionally skipped to keep the existing index.html z-index slot names).
**Object-position (Mode A):** `83% center` (verified vs extracted frames at src 1044.7 & 1090.9: Jasper centered, seam/host excluded, name-tag kept).
**Primary device (DESIGN per-clip map):** **`flowchart` ADL cascade as the cold open** (c4b2) + **`caption-kinetic-slam`** on the 25× reveal (c4b5).

> v4 is the REJECTION-fix round. The rejected build (1) rendered the internal index "04" on screen (R6) and (2) had a blank-left Mode-A stretch (R7, the clip-8 0:33–0:52 bug). v4 fixes BOTH at the structural level and closes the six prior-round spec findings. **The live `clip-4-oct10-crash/` files are still v3 — every edit below is REQUIRED build work.**
>
> **v4-REV (this revision) adds 7 quality improvements on top of the rejection fixes — all evidence-grounded, none fabricated:** (#1) the c4b2 cascade now BUILDS through the 12.3s setup gap with three new word-synced nodes drawn from spoken legs ("long spot" / "short perp" / "deep ITM"); (#5) the c4b5 25× slam is compressed from 5 slams to 3; (#4) the thin c4b3 REAL/COMPRESSION slam is CUT (beat count → 6, still legal <90s); (#2) node-4 strips the stray `→` glyph; (#3) c4b1 cyan moves to the verb `SHIFTS` only; (#7) the two cards are differentiated (c4b4 = compact stat-stamp, c4b6 = 2-part reveal); (#9) c4b8 L2 plain-language softened; (#10) the table now carries an EDL-comp column so a builder greps the SAME number the EDL cites.

---

## ⚠️ WHAT CHANGED FROM v3 → v4 (the rejection fixes — do ALL of these)

**R6 — NO INDEX ON SCREEN (highest priority, user-flagged "everything has an issue").**
- The live build renders the internal clip number **"04"/"02"/"06"** via index divs **`#c2-idx`** (`beat-c4b2…:35`), **`#c4-idx`** (`beat-c4b4…:27`), and **`#c6-idx`** (`beat-c4b6…:31`) inside the sub-comps — plus the GSAP lines that fade each in (`#c2-idx` line 152, `#c4-idx` line 112, `#c6-idx` line 117) and the CSS blocks that position them (`#c2-idx` line 88, `#c4-idx` line 65, `#c6-idx` line 70). **DELETE every one of these index divs, their CSS, and their GSAP tween lines.** No `04`, `02`, `06`, `4`, `c4`, no beat counter, no monospace index of any kind reaches any frame.
- **Exact live ids (use these in the grep gate — the review caught a stale ref):** `#c2-idx`, `#c4-idx`, `#c6-idx` (every one carries the `-idx` suffix). A grep keyed on bare `#c4`/`#c6` would MISS the real div.
- Eyebrow EDITORIAL labels stay (`ADL CASCADE · LAST OCTOBER`, `HOW LONG IT LASTED`, `WHAT FUELED THE MOVE`). The bare number is the only forbidden thing.
- **Build-time grep gate:** after editing, searching the sub-comps for `c2-idx`, `c4-idx`, `c6-idx`, `>04<`, `>02<`, `>06<`, `>4<`, or a monospace-index class must return ZERO hits. Verify by frame at comp 0.5 / 16 / 52 / 76: NO number in any corner.

**R7 — VIEW MATCHES CONTENT, NO BLANK-LEFT MODE-A (the second rejection cause).**
- v3 hid a blank-left bug: its V2→V3 Mode-A switch fires at **comp 46.0** (`index.html:218–223`, verified live), cropping the speaker right while the LEFT zone sits empty from 46.0 until the c4b4 card appears at ~51.0 (~5s blank-left) — the exact clip-8 defect. v3 also had a ~4.7s blank-left at the TOP of the cascade Mode-A block (shrink at 3.5, but the cascade eyebrow/node-1 did not fire until 8.0).
- **v4 fix — collapse to a bulletproof TWO-block structure** (see View-Timeline): ONE Mode-A block = the flowchart cascade, with a graphic on screen for its ENTIRE duration (eyebrow + zone-rule + node-1 now fire AT the shrink, comp 3.5, anchored to spoken "delta neutral"@3.46); and ONE long full-frame block for everything after the cascade. The two cards (c4b4, c4b6) render as liquid-glass cards over a **full-frame dark-gradient backdrop with BOTH speakers visible** (the treatment DESIGN.md sanctions for full-frame text beats) — NOT as cropped-right Mode-A. There is therefore no second Mode-A block to leave blank, and no breath ever sits inside a Mode-A block. Every Mode-A instant has the flowchart; every breath/card/slam is full-frame.
- **Delete the v3 `46.0` and `58.3` master switches** (`index.html` lines ~218 and ~228) — they are the source of the live blank-left. v4 has exactly two switches: shrink@3.5, expand@34.0.
- Why two blocks instead of v3's five: the only legal way to give a single ~7s card its own Mode-A block is to wedge an 8s Mode-A between two full-frames — which is an A-B-A-within-12s violation (R1). Holding the card in full-frame-backdrop avoids BOTH the blank-left and the A-B-A. Given the "everything has an issue" mandate, v4 chooses the bulletproof structure over view variety.

**Six prior-round spec findings (Agent 3) — all closed in v4:**
1. **c4b3 dialog-match FAIL** — superseded by v4-REV improvement #4: **c4b3 (REAL/COMPRESSION) is now CUT entirely** (thin 2-word abstract slam with no number/stakes; the cascade already shows the compression visually; the c4b4 stat-stamp now carries that stretch). The rejected "40 MINUTES OF / REAL COMPRESSION" firing on "extremely hectic" is moot — the beat is gone.
2. **c4b3 fabricated number + cross-beat numeric conflict** — moot (beat cut). The clip's sole on-screen duration is c4b4's `30–45 MIN`.
3. **c4b2 node false word-cue ("forced selling" never spoken).** → **node renamed to `FEEDBACK LOOP`** (no arrow glyph), cued to the real spoken phrase "feedback loop" (feedback@comp 24.74, loop@comp 25.16). The fabricated "FORCED SELLING →" string AND its `→` glyph are deleted.
4. **c4b6 data-start drift (74.8 vs 75.0).** → **ONE value everywhere: `data-start 75.0 / data-duration 5.0`.** The "slide begins ~75.4" is internal animation timing inside that 75.0 window, NOT a second data-start. No 74.8 variant anywhere in this doc.
5. **Residual top-of-cascade blank-left seam (eyebrow at 8.0, shrink at 3.5).** → **c4b2 `data-start` moved 8.0 → 3.6**; eyebrow + zone-rule + node-1 fire at comp 3.5–3.7 as the shrink lands. Left zone is graphic-occupied from the first Mode-A frame.
6. **Build state was stale (live files = v3).** → BUILD STATE block below lists every required edit; nothing here is "already done."

**Kept from v3 (works):** dialog-matched cold open at in-point `1030.76` ("your delta completely shifts"); `object-position:83% center`; flowchart cascade as centerpiece; `caption-kinetic-slam` for the 25× reveal; the c4b6 leverage-not-spot re-anchor (fires on "leverage."@76.20); the re-derived word table; Ken-Burns + glow/zone-rule choreography.

---

## R7/R1 — VIEW-TIMELINE (every Mode-A names the graphic that fills it; no segment is graphic-less)

Source is a SIDE-BY-SIDE (Nic/host left, Jasper/guest right). Two views: **full-frame** (both speakers, dark gradient backdrop in the left zone for text/cards) and **Mode-A** (guest framed right 40%, graphic in left 60%). v4 uses ONE Mode-A block and ONE full-frame block so the frame never bounces and no Mode-A segment is ever graphic-less.

| # | View | Comp range | Dwell | Graphic that fills it (Mode-A MUST name one) | R7 / R1 check |
|---|------|-----------|-------|-----------------------------------------------|---------------|
| V0 | **full-frame** (intro) | 0.0 → 3.5 | 3.5s | c4b1 cold-open kinetic over both speakers (dark gradient backdrop) | intro (0–6s) exempt; never loops back. NOT blank-left (full-frame). |
| V1 | **Mode-A** | 3.5 → 34.0 | **30.5s** | **c4b2 `flowchart` ADL cascade — eyebrow + cyan zone-rule + node-1 paint AT comp 3.5–3.7 (anchored to spoken "delta neutral"@3.46); the setup legs (LONG SPOT@5.44, SHORT PERP@7.52, PERP DEEP ITM@14.58) then nodes 4–6 fill in on their word cues; whole flowchart holds to ~33.6, clears just before the expand.** Graphic present AND BUILDING every frame 3.6→33.6 — the v4-REV #1 fix turns the old 12.3s frozen gap into continuous node reveals. | NO blank-left instant ✓ (graphic from the first Mode-A frame). NO 12s static stretch ✓. ≥8s ✓. |
| V2 | **full-frame** | 34.0 → 88.2 | **54.2s** | both speakers throughout; sequence: breath → c4b4 `30–45 MIN` stat-stamp on dark-gradient backdrop (51.58) → breath → c4b5 `25×` slam (63.76) → c4b6 `LEVERAGE / NOT SPOT` 2-part card on backdrop (76.20) → c4b8 `WIPED OUT` kinetic closer (81.82) → clip ends on live video. **Subtle slow push-in on Jasper during the c4b5 25× stretch (v4-REV #8) so the 54s block is not static-video-plus-floating-overlays.** | full-frame the entire block; breaths are full-frame (both speakers), NOT cropped. Cards sit over a darkened LEFT zone with both speakers visible = the sanctioned full-frame-text treatment, NOT the blank-left Mode-A bug. ≥8s ✓. |

**Blank-left audit (R7):** the ONLY Mode-A block is V1, and the flowchart occupies its left zone for the entire 3.6→33.6 span (no gap at the top because the eyebrow/rule/node-1 fire at the shrink, not at 8.0; no gap in the middle because the v4-REV #1 setup nodes fire at 5.44/7.52/14.58). Every breath, card, and slam after the cascade is full-frame (both speakers). **No cropped-right speaker with a blank left half exists anywhere. PASS.**

**A-B-A audit (R1):** there is exactly one Mode-A block (V1) and one post-intro full-frame block (V2). Neither view is ever returned to within 12s because neither recurs. V0 intro full-frame → V1 Mode-A → V2 full-frame is a single monotonic progression, never a loop. **No A-B-A. No segment <8s outside the intro. PASS.**

**One-liner:** intro-full(3.5s) → ModeA flowchart cascade(30.5s, graphic BUILDING the whole time) → full-frame everything-else(54.2s: stat-stamp → slam → card → closer). 2 blocks, zero flip-flop, zero blank-left, zero on-screen index.

---

## R2 — Template variety (don't make another clip-2)

`kinetic(open) → flowchart(cascade) → liquid-glass stat-stamp → caption-kinetic-slam → liquid-glass card → kinetic(closer)`

- **Distinct PRIMARY device = `flowchart` ADL cascade as the cold open** (per DESIGN per-clip map). The cascade is the centerpiece; the clip is NOT kinetic-dominated. v4-REV cuts the redundant c4b3 slam so the run is now flowchart → card → slam → card → kinetic = **only one slam in the whole clip after the cascade** (cleaner, less slam-heavy than v4's two-slam plan).
- **≤2 kinetic word-stacks / slams in a row:** every slam/kinetic is separated by a non-kinetic beat. Adjacencies: c4b1(kinetic)→c4b2(flowchart)→c4b4(card)→c4b5(slam)→c4b6(card)→c4b8(kinetic). **No two slams/kinetics ever adjacent. PASS** (stronger than v4, which had c4b3 slam → c4b4 card → c4b5 slam).
- **Catalog blocks to INSTALL (`npx hyperframes add <name>`):**
  - `flowchart` (block) — **c4b2** ADL cascade. Restyle to DESIGN palette (dark nodes, cyan final node, muted connectors). Strip catalog sticky-note/cursor cosmetics. Do NOT re-hand-build (anti-pattern §2).
  - `caption-kinetic-slam` (component) — **c4b5** (25×). Task-mandated for the 25× reveal. *(c4b3 instance removed — beat cut.)*
  - **`data-chart` considered for the 25× and documented (v4-REV #6):** 25× is inherently *comparative* (derivatives vs spot = a 2-bar ratio), which is the textbook `data-chart` case and would add device variety to a slam-leaning clip. **Decision: keep the slam (task-mandated), but the OPTIONAL upgrade — if the builder wants one more distinct device — is a 2-bar `data-chart` ("DERIVATIVES" bar 25× the height of "SPOT") rendered INSIDE the c4b5 full-frame window after the hero number lands.** Not a blocker; the slam alone PASSES. Documented per the checklist's "did I consider a catalog block?" item — this round actively re-opened it rather than flatly rejecting.
  - Duration `data-chart` still rejected: `30–45 MIN` is a single range, not a comparison → the compact stat-stamp reads cleaner.
- **HAND-BUILD (DESIGN "Cards & Panels" recipe):** c4b1 kinetic open, c4b4 stat-stamp, c4b6 2-part card, c4b8 kinetic closer.

---

## R3 — Jargon (every on-screen string mapped through `_JARGON.md`)

Whisper writes **"burp"** for **perps/perp**; **"deep in"** for **DePIN**; the transcript is for TIMING only — never spelling. Every on-screen string in v4-REV, audited:

| Beat | On-screen string | Mapped term? | Verdict |
|------|------------------|--------------|---------|
| c4b1 | `YOUR DELTA` / `COMPLETELY SHIFTS` | none | ✓ |
| c4b2 | `ADL CASCADE · LAST OCTOBER` / `DELTA-NEUTRAL BOOK` / `LONG SPOT` / `SHORT PERP` / `PERP DEEP ITM` / `PERP CLOSED OUT` / `NAKED LONG DELTA` / `FEEDBACK LOOP` / `ALTS −60 / −70 / −80%` | **PERP** (Whisper "burp"@1044.68) → rendered **PERP** ✓ (appears in `SHORT PERP`, `PERP DEEP ITM`, `PERP CLOSED OUT`); `ADL` = auto-deleveraging (correct casing); `ITM` = in-the-money (standard) | ✓ |
| c4b4 | `HOW LONG IT LASTED` / `30–45 MIN` / `of real stress — then everything picked back up` | none | ✓ |
| c4b5 | `25×` / `DERIVATIVES vs SPOT` / `$226K MELT-UP` | none ("derivatives"/"spot" are correct finance terms) | ✓ |
| c4b6 | `WHAT FUELED THE MOVE` / `LEVERAGE` / `NOT SPOT` / `the rally ran on borrowed size` | none ("leverage"/"spot" correct) | ✓ |
| c4b8 | `NEW TO PERPS` / `MAX LEVERAGE ON` / `WIPED OUT` | **PERPS** (Whisper "burp"@1113.08) → rendered **PERPS** ✓ | ✓ |

All four spoken "burp" occurrences (src 1038.90, 1044.68, 1089.74, 1113.08) are perps/perp. Several surface on screen (c4b2 nodes, c4b8 "PERPS") and are spelled correctly; two are audio-only. **No raw "burp", "deep in", "graft", or "stake rate" reaches the render. PASS.** No Wintermute/Paradex/etc. on screen. `ADL`/`DERIVATIVES`/`SPOT`/`DELTA`/`LEVERAGE`/`ITM` casing per `_JARGON.md` "Standard term casing."

---

## R4 — No duplicate notable word across a beat (eyebrow vs sub/title)

| Beat | Elements | Duplicate notable word? |
|------|----------|--------------------------|
| c4b1 | `YOUR DELTA` / `COMPLETELY SHIFTS` | none |
| c4b2 | eyebrow `ADL CASCADE · LAST OCTOBER`; nodes `DELTA-NEUTRAL BOOK` / `LONG SPOT` / `SHORT PERP` / `PERP DEEP ITM` / `PERP CLOSED OUT` / `NAKED LONG DELTA` / `FEEDBACK LOOP` / `ALTS −60/−70/−80%` | "DELTA" (node-1, node-6) and "PERP" (nodes 3/4/5) are sequential **cascade steps** (distinct stages of one chain), not an eyebrow-vs-title echo. The R4 target (same word in eyebrow AND title of one card) does not occur. "FORCED SELLING" removed. ✓ |
| c4b4 | eyebrow `HOW LONG IT LASTED` / headline `30–45 MIN` / sub `of real stress — then everything picked back up` | "real" appears only in the lowercase sub (not in the eyebrow/headline) → no eyebrow-vs-title dup. ✓ |
| c4b5 | slam words `25×` `DERIVATIVES` `vs` `SPOT` then payoff `$226K MELT-UP` | none |
| c4b6 | eyebrow `WHAT FUELED THE MOVE` / headline part-A `LEVERAGE` part-B `NOT SPOT` / sub `the rally ran on borrowed size` | none ("SPOT" only in the headline) |
| c4b8 | `NEW TO PERPS` / `MAX LEVERAGE ON` / `WIPED OUT` | none. *(Note: "LEVERAGE" recurs c4b6 headline → c4b8 L2 — different beats ~5s apart, distinct framing (cause vs consequence); not an in-beat dup. If the builder prefers zero echo, swap c4b8 L2 to `ONE BAD TRADE` — see c4b8 detail.)* |

Cross-beat echoes deliberately controlled: c4b6 sub uses "borrowed size" (not "wiped") so it does not pre-echo c4b8 "WIPED OUT"; "SPOT" recurs across c4b5/c4b6 only as a shared finance term in distinct beats with different framing. **PASS.**

---

## §3 — Dialog-match + open-on-line + text-appears-as-spoken

- **In-point `src_in = 1030.76`** = the word **"your"** in *"your delta completely shifts in your structure."* The "…in the money. But as a result," filler head (src 1029.02–1030.22) is **trimmed**. First audible words at comp 0.0 are the concrete crash-mechanic line — no anticipatory pull.
- **First text by comp 0.08** (c4b1 L1) — under the 1.5s cold-open cap.
- **Every CONTENT beat fires on the line ACTUALLY SPOKEN at its fire time** (the v4 + v4-REV fixes enforce this end-to-end):
  - c4b1 `YOUR DELTA / COMPLETELY SHIFTS` ← "your delta completely shifts" @0.00–0.98 ✓
  - c4b2 node cues are ALL real: node-1 "delta neutral"@3.46, node-2 "long spot"@5.44, node-3 "short the perp"@7.52, node-4 "deeply…in the money"@14.58, node-5 "closed out"@15.88, node-6 "naked long delta"@17.70, node-7 "feedback loop"@24.74, node-8 "60,70,80%"@31.90 ✓ (no fabricated "forced selling")
  - c4b4 `30–45 MIN` ← "half an hour to 45 minutes"; half@51.58, 45@52.24, minutes@52.64 ✓
  - c4b5 `25×`/`DERIVATIVES vs SPOT`/`$226K MELT-UP` ← 25x@63.76 … 226k@71.82 ✓
  - c4b6 `LEVERAGE / NOT SPOT` ← "very heavily supported by leverage"; leverage@76.20 ✓
  - c4b8 `NEW TO PERPS`/`MAX LEVERAGE ON`/`WIPED OUT` ← new@81.82 … wiped@87.16 ✓
- Genuinely editorial labels are marked `EDITORIAL`. All fire-times read off the inlined word table's `comp_t` column, never computed by hand.

## R5 — Opening coherence

c4b1 reads **"YOUR DELTA / COMPLETELY SHIFTS"** — a complete thought; cyan payoff is now the verb **`SHIFTS`** only (v4-REV #3: the consequence-word carries the accent, not the adverb "completely"). **PASS.**

---

## §5 — Speaker framing (Mode A) — kept & verified

- `MODE_A = {left:1229, top:108, width:614, height:864}`, `borderRadius:"6px"`, `object-fit:cover`, `object-position:83% center`.
- 83% lands the tall narrow `cover` window (AR≈0.71, ~40% of source width visible) on **Jasper's face**, catching the right of his name-tag and **excluding the center seam + host** (50%/62% center the seam — the clip-1 mistake).
- Bottom clearance in Mode-A box = 1080−108−864 = **108px** (>40 ✓); top = **108px** (>20 ✓). Name lower-third "Jasper De Maere / Wintermute" fully visible.
- Full-frame beats (V0, V2) show **both speakers** with a left dark gradient backdrop for text/card readability — never text on black. **During c4b5 (25× stretch) the active speaker (Jasper) gets a subtle slow push-in (scale 1.0→~1.03 over the slam window) so V1 reacts to the graphic (v4-REV #8 / "speaker focus + motion" memory item).**
- **Build-time verify-by-frame (mandatory, `_QA-CHECKLIST.md §9`):** after draft render, extract and LOOK at frames at comp **0.5** (open, NO index), **3.7** (Mode-A shrink + cascade eyebrow/node-1 ALREADY painted — confirm NO blank-left), **6** (setup legs LONG SPOT/SHORT PERP painting — confirm cascade is BUILDING, not frozen), **16** (cascade mid, NO index), **34.0** (full-frame breath, both speakers, no crop), **52** (stat-stamp on full-frame backdrop, both speakers, NO index), **63.8** (25× slam + subtle push-in on Jasper), **76.5** (leverage 2-part card on full-frame backdrop, NO index), **82** (closer). Re-tune `object-position` if any frame shows host bleed / dead ceiling. **Confirm at EVERY frame: no "04"/"02"/"06"/index number anywhere.**

---

## Master-timeline framing (update `clip-4-oct10-crash/index.html`)

The existing `index.html` wires the master timeline but at the WRONG switch times (v3 used 33.6/46.0/58.3 producing a blank-left Mode-A) and still renders index numbers. v4 uses ONLY TWO switches:

- **t=0–3.5 full-frame** (both speakers) for c4b1; **shrink to Mode A at t=3.5** (`expo.inOut`, 0.7s, completes ~4.0); `#bg-glow` in at 3.5, `#zone-rule` cyan draw 3.6; Ken-Burns scale 1.0→1.04 across the clip. The c4b1 kinetic exits up ~comp 3.1 (cleared before the shrink).
- **t=34.0 expand to full-frame** for V2 (glow + zone-rule out 33.6) — **stays full-frame through clip end** (breath → c4b4 stat-stamp-on-backdrop → breath → c4b5 slam [with a subtle push-in on Jasper, scale 1.0→~1.03 over ~63.8–72] → c4b6 card-on-backdrop → c4b8 closer). NO return to Mode A (D4 no-outro; clip ends on live full-frame video).
- **DELETE the v3 `46.0` (V2→V3 Mode-A) and `58.3` (V3→V4) switch blocks** at `index.html` lines ~218 and ~228 — these are the live blank-left source. Also delete the `gr`/`zr` opacity tweens at 46.1/46.2.
- Audio: separate `<audio>` `data-volume="1"`, continuous; video `muted`. `data-media-start="1030.76"` on both; `data-duration="88.2"`.

**z-index (DESIGN line 58):** every overlay id `beat-c4b1, beat-c4b2, beat-c4b4, beat-c4b5, beat-c4b6, beat-c4b8` MUST be in the `z-index:3` rule (else it renders behind the video). **v4-REV cuts c4b3 — REMOVE `beat-c4b3` from the z-index:3 rule AND remove its `<iframe>`/include from index.html (delete the `beat-c4b3-hectic-slam.html` file or leave it unwired).** The live rule lists 7 ids; after the cut there are **6** (`beat-c4b1, beat-c4b2, beat-c4b4, beat-c4b5, beat-c4b6, beat-c4b8`) — confirm all 6 stay listed. Note c4b5 file renames to `beat-c4b5-25x-slam.html`, c4b6 to `beat-c4b6-leverage-not-spot.html` — update the `<iframe>`/include `src` in index.html accordingly while keeping the SAME `id`s.

> **BUILD STATE — the live `clip-4-oct10-crash/` files are v3; ALL of the following are REQUIRED edits:**
> 1. **R6 / index removal (every sub-comp):** delete the index divs **`#c2-idx`** (`beat-c4b2…:35`), **`#c4-idx`** (`beat-c4b4…:27`), **`#c6-idx`** (`beat-c4b6…:31`), their CSS (lines 88 / 65 / 70) AND their GSAP tweens (lines 152 / 112 / 117). Grep-gate `c2-idx|c4-idx|c6-idx|>04<|>02<|>06<` clean before render.
> 2. **index.html view switches:** change to **`3.5` (shrink to Mode-A) / `34.0` (expand to full-frame, stays full-frame to end)**. **Remove the v3 `46.0` and `58.3` switches and their `gr`/`zr` tweens** (lines ~218–228 — they created the blank-left Mode-A).
> 3. **c4b2 cascade (REBUILD — v4-REV #1 is the biggest quality change):** move `data-start 8.0 → 3.6`; fire eyebrow + cyan `#zone-rule` + node-1 at comp 3.5–3.7. **Split the old buried sub-text into real word-synced nodes so the cascade BUILDS through the entire setup instead of freezing 3.6→15.9.** New node sequence = **8 nodes** (see c4b2 detail): node-1 `DELTA-NEUTRAL BOOK`@3.6 → node-2 `LONG SPOT`@5.44 → node-3 `SHORT PERP`@7.52 → node-4 `PERP DEEP ITM`@14.58 → node-5 `PERP CLOSED OUT`@15.88 → node-6 `NAKED LONG DELTA`@17.70 → node-7 `FEEDBACK LOOP`@24.74 → node-8 `ALTS −60/−70/−80%`@31.90 (cyan). **Rename the live node-4 title `FORCED SELLING → FEEDBACK LOOP` → `FEEDBACK LOOP` and STRIP the `→` glyph (live `beat-c4b2…:59`).** (Layout: nodes 2+3 and 4 can be a compact stepped group so 8 nodes fit the left zone — or render the setup legs as a 2-up row under node-1; see detail.)
> 4. **c4b3 (CUT — v4-REV #4):** **delete the beat.** Remove `beat-c4b3-hectic-slam.html` from the include/iframe list and from the z-index:3 rule. The clip is 88.2s with 6 beats — legal (<90s ⇒ 6-beat floor). Do NOT re-author it as REAL/COMPRESSION; it is gone.
> 5. **c4b4 (DIFFERENTIATE — v4-REV #7):** render as a **compact number-forward STAT-STAMP** (smaller card, the `30–45 MIN` number dominant, minimal chrome) over a **full-frame dark-gradient backdrop** (both speakers visible), NOT Mode-A. Distinct from c4b6's full card. `data-start 50.8 / data-duration 7.5`.
> 6. **c4b5 (COMPRESS — v4-REV #5):** re-author `beat-c4b5-25x-slam.html` using `caption-kinetic-slam`, **3 hits not 5**: `25×` (hero, held longer) → `DERIVATIVES vs SPOT` (one comparative slam) → `$226K MELT-UP` (cyan payoff). "TIMES MORE" and "THAN SPOT" become the hero's held sub-context, not separate slams. `data-start 58.5 / data-duration 14.3`.
> 7. **c4b6 (2-PART REVEAL — v4-REV #7):** `beat-c4b6-leverage-not-spot.html` (liquid-glass card on full-frame backdrop). Headline reveals in **two parts**: `LEVERAGE` lands first, then `NOT SPOT` snaps in (distinct from c4b4's static headline). **`data-start 75.0 / data-duration 5.0` — this single value everywhere.**

---

## BEAT MAP (v4-REV)

| Beat | Comp range | Src range | Template / block | View | Sub-comp file |
|------|-----------|-----------|------------------|------|---------------|
| c4b1 | 0.0–3.5 | 1030.76–1034.26 | kinetic-type (cold open, hand-built) | full-frame (V0)→ModeA@3.5 | `beat-c4b1-delta-open.html` |
| c4b2 | 3.6–33.6 | 1034.36–1064.36 | **`flowchart` (CENTERPIECE / primary device, 8 building nodes)** | Mode A (V1) | `beat-c4b2-adl-cascade.html` |
| c4b4 | 50.8–58.3 | 1081.56–1089.06 | liquid-glass **stat-stamp** on full-frame backdrop (hand-built) | full-frame (V2) | `beat-c4b4-30-45-min.html` |
| c4b5 | 58.5–72.8 | 1089.26–1103.56 | **`caption-kinetic-slam` (25× reveal, 3 hits)** | full-frame (V2) | `beat-c4b5-25x-slam.html` |
| c4b6 | 75.0–80.0 | 1105.76–1110.76 | liquid-glass **2-part card** on full-frame backdrop (hand-built) | full-frame (V2) | `beat-c4b6-leverage-not-spot.html` |
| c4b8 | 80.6–88.2 | 1111.36–1118.98 | kinetic-type (human closer, hand-built) | full-frame (V2) | `beat-c4b8-wiped-out.html` |

*(c4b3 CUT in v4-REV #4 — the 34.0→50.8 stretch is full-frame BREATH on live video, both speakers. 16.8s of breath after the cascade before the stat-stamp; legal because breath is full-frame, and it lets the cascade payoff land + gives the long V2 block its natural rest. Beat count = 6, ≥6-beat floor for <90s.)*

**Opening "3+ element types before 6s" (DESIGN):** c4b1 L1 kinetic (type 1, comp 0.08) + c4b1 cyan payoff `SHIFTS` (type 2, comp 0.98) + Mode-A video shrink with cyan `#zone-rule` draw + `#bg-glow` (type 3, comp 3.5–3.6) + cascade eyebrow `ADL CASCADE · LAST OCTOBER` + node-1 `DELTA-NEUTRAL BOOK` (type 4, comp 3.5–3.7, anchored to spoken "delta neutral"@3.46) + node-2 `LONG SPOT` building by comp 5.44 (type 5, the cascade is already moving). Speaker visible from t=0. **PASSES**, and the open is the dialog line, NOT formulaic swiss-grid chrome. **NO index number among these elements (R6).**

---

## BEAT DETAIL

### c4b1 — kinetic-type cold open · full-frame → Mode A · `beat-c4b1-delta-open.html`
- **Comp:** 0.0–3.5 · **Src:** 1030.76–1034.26 · `data-start 0.0` / `data-duration 3.5`
- **View:** full-frame (both speakers, dark gradient backdrop LEFT for the kinetic). Master shrinks the video to **Mode A at comp 3.5**; the kinetic exits up ~comp 3.1 (cleared before the shrink).
- **NO INDEX (R6):** no monospace "04"/index element. This open is a clean kinetic — no eyebrow needed.
- **Kinetic lines — phrase build, STAY (no dim), Inter 900 ~130px:**
  - **L1 `YOUR DELTA`** (`#FFFFFF`) — spoken **"your delta"**: your@comp 0.00, delta@comp 0.16 → **fire comp 0.08**.
  - **L2 `COMPLETELY SHIFTS`** — spoken **"completely … shifts"**: completely@comp 0.48, shifts@comp 0.98. **`COMPLETELY` renders WHITE `#FFFFFF`; `SHIFTS` renders CYAN `#00D4FF` + glow (v4-REV #3 — the consequence-verb carries the single cyan accent, not the adverb).** L2 fires at comp 0.48 (whole line on screen by 0.98 when `SHIFTS` turns cyan).
- **Spoken words each line matches:** L1 = "your delta"; L2 = "completely shifts."
- **Cyan element:** the word `SHIFTS` only (the single cyan element for this beat).
- **Exit:** whole stack drifts up `power2.in` ~comp 3.1.

### c4b2 — `flowchart` ADL cascade (CENTERPIECE / PRIMARY DEVICE) · Mode A · `beat-c4b2-adl-cascade.html`
- **Comp:** 3.6–33.6 · **Src:** 1034.36–1064.36 · `data-start 3.6` / `data-duration 30.0`
- **View:** Mode A (video right 40%, ~80% scale; glow + cyan zone-rule come in at the 3.5 shrink). **Graphic fills the left zone for the ENTIRE block AND keeps BUILDING — eyebrow + zone-rule + node-1 paint at comp 3.5–3.7, then a new node lands every few seconds on its spoken cue, killing both the top-of-block blank-left (prior-round #5) AND the 12.3s frozen-node gap (v4-REV #1, the highest-value quality fix).**
- **NO INDEX (R6):** **DELETE the `#c2-idx` div (`beat-c4b2…:35`), its CSS (line 88), and its GSAP tween (line 152).** No "02"/"04" anywhere in this sub-comp. Eyebrow `ADL CASCADE · LAST OCTOBER` is the only top-left label.
- **Install:** `npx hyperframes add flowchart` → restyle to DESIGN palette (node fill `rgba(20,26,34,0.92)`, 1px `rgba(255,255,255,0.08)` border, `#F0F0F0` labels, connectors muted `#6B7480`, final node cyan). Strip the catalog's sticky-note/cursor cosmetics. Do NOT re-hand-build (anti-pattern §2).
- **Lead-device beat — vertical cause→effect flow, building in sync with the spoken cascade. v4-REV #1 turns the old single recap node + 12.3s freeze into 8 WORD-CUED nodes that BUILD through the entire setup the speaker narrates:**
  - Eyebrow **`ADL CASCADE · LAST OCTOBER`** — `#F0F0F0` Inter 700 32px — `EDITORIAL: structural label` — fire comp **3.5** (with the shrink).
  - Node 1 **`DELTA-NEUTRAL BOOK`** — cued to spoken **"delta neutral"** — delta@comp 3.20, neutral@comp 3.46 → reveal **comp 3.6** `#F0F0F0`. *(recap header node, word-anchored.)*
  - Node 2 **`LONG SPOT`** — cued to spoken **"long spot"** — long@comp **5.44**, spot@comp 6.80 → reveal **comp 5.44** `#F0F0F0`. *(v4-REV #1: was buried as node-1 sub-text "long spot · short the perp"; now a real building leg.)*
  - Node 3 **`SHORT PERP`** — cued to spoken **"short … the burp(perp)"** — short@comp **7.52**, burp(perp)@comp 8.14 → reveal **comp 7.52** `#F0F0F0`. *(Whisper "burp"→PERP per _JARGON.md.)*
  - Node 4 **`PERP DEEP ITM`** — cued to spoken **"your burp(perp) is deeply in the money"** — deeply@comp **14.58**, money@comp 15.20 → reveal **comp 14.58** `#F0F0F0`. *(v4-REV #1: was buried as node-2 sub "deep ITM"; now the leg he actually narrates fills the prior dead 8→15s window. ITM = in-the-money per _JARGON.md.)*
  - Node 5 **`PERP CLOSED OUT`** — cued to spoken **"closed out"** — closed@comp **15.88**, out@comp 16.24 → reveal **comp 15.9** `#F0F0F0`.
  - Node 6 **`NAKED LONG DELTA`** — cued to spoken **"naked long delta"** — naked@comp **17.70**, long@comp 18.14, delta@comp 18.52 → reveal **comp 17.7** `#F0F0F0`.
  - Node 7 **`FEEDBACK LOOP`** — cued to spoken **"feedback loop"** — feedback@comp **24.74**, loop@comp 25.16 → reveal **comp 24.7** `#F0F0F0`. *(v4: renamed from the fabricated "FORCED SELLING → FEEDBACK LOOP"; "forced selling" is NEVER spoken — the audio is "…close out that position, creating this very strong feedback loop." **STRIP the `→` glyph too (live `beat-c4b2…:59`); final node text is `FEEDBACK LOOP` only — v4-REV #2.** Prior-round fix #3.)*
  - Node 8 **`ALTS −60 / −70 / −80%`** (cyan final node) — cued to spoken **"60, 70, 80%"** — 60,@comp **31.90**, 70,@comp 32.40, 80%@comp 32.78 → the three numbers tick into the node **comp 31.90 → 32.40 → 32.78**; node finalizes cyan `#00D4FF`.
- **Layout note (8 nodes in the left 60% zone):** to fit 8 nodes, render the three setup legs (LONG SPOT / SHORT PERP / PERP DEEP ITM, nodes 2–4) as **compact secondary nodes** (smaller, e.g. a 2-up `LONG SPOT` + `SHORT PERP` row feeding into `PERP DEEP ITM`) beneath the `DELTA-NEUTRAL BOOK` header, then the chain resumes full-width at node-5 `PERP CLOSED OUT`. Keep node-8 the cyan hero. If 8 full-width nodes overflow, this stepped-group layout is the intended compromise — the GOAL is continuous motion through the setup, not 8 identical boxes.
- **Spoken words each node matches:** n1="delta neutral"; n2="long spot"; n3="short the perp"; n4="deeply…in the money"; n5="closed out"; n6="naked long delta"; n7="feedback loop"; n8="60, 70, 80%".
- **Cyan element:** Node 8 only (final-node convention). Connectors muted `#6B7480`.
- **Anti-static (v4-REV #1 directly fixes R2):** a node pops on its spoken cue roughly every 2–9s across 3.6→33s (3.6 / 5.44 / 7.52 / 14.58 / 15.88 / 17.70 / 24.74 / 31.90), cyan connectors draw `scaleY 0→1` between reveals, the −60/−70/−80% numbers count into node 8. **No frozen stretch longer than ~6.5s (the 8→14.6 gap, now bridged by node-4 at 14.58) — the old 3.6→15.9 12.3s freeze is eliminated.** Continuously building. Whole flowchart holds on screen, then exits ~comp 33.6 (clears as the V2 full-frame expand fires at 34.0).

### c4b4 — liquid-glass STAT-STAMP on full-frame backdrop · full-frame · `beat-c4b4-30-45-min.html`
- **Comp:** 50.8–58.3 · **Src:** 1081.56–1089.06 · `data-start 50.8` / `data-duration 7.5`
- **View:** **full-frame (V2)** — both speakers visible; the stat-stamp sits in the LEFT zone over a dark-gradient backdrop that darkens the host side for readability (the DESIGN-sanctioned full-frame-text treatment). **NOT Mode-A** — keeping it full-frame avoids the v3 blank-left and the A-B-A a short Mode-A card-block would create (R7/R1 fix). After the cascade exits at ~33.6 and the V2 expand at 34.0, comp 34.0→50.8 is full-frame BREATH on live video (both speakers, NO overlay) — the cut of c4b3 lets the cascade payoff land before this stamp.
- **NO INDEX (R6):** **DELETE the `#c4-idx` div (`beat-c4b4…:27`), its CSS (line 65), and its GSAP tween (line 112).** No "04" in this sub-comp.
- **STAT-STAMP treatment (v4-REV #7 — number-forward, distinct from c4b6's full card):** compact, the NUMBER dominates. `rgba(20,26,34,0.92)` fill, **4px cyan `#00D4FF` inset accent bar** (left), soft outer glow (`0 0 40px rgba(0,212,255,0.10), 0 8px 40px rgba(0,0,0,0.65)`), 1px `rgba(255,255,255,0.08)` border, `mask-image:linear-gradient(to right,black 82%,transparent 100%)` feather. **NO `backdrop-filter` blur, NO grain.** Tighter than a full card — the `30–45 MIN` headline is the hero, eyebrow small above, sub small below.
- **Content (exact text + hex):**
  - Eyebrow **`HOW LONG IT LASTED`** — `#F0F0F0` Inter 700 30px — `EDITORIAL: structural label`.
  - Headline **`30–45 MIN`** — `#FFFFFF` Inter 900 ~108px (number-forward; the duration is the point; the clip's SOLE on-screen duration).
  - Sub **`of real stress — then everything picked back up`** — `#B6BEC6` Inter 600 26px.
- **Entry — WORD-CUED:** stamp pops/counts in and lands on spoken **"half an hour to 45 minutes"** — half@comp 51.58, 45@comp 52.24, minutes@comp 52.64. Head begins ~comp 50.9 so the number is settled by comp 51.58. *(Faithful: "half an hour" = 30 min, "45 minutes" → `30–45 MIN`.)* Holds, exits ~comp 57.9.
- **Spoken words this stamp matches:** "half an hour to 45 minutes before everything picked back up."
- **Cyan element:** the 4px accent bar only.

### c4b5 — `caption-kinetic-slam` (25× REVEAL — task-required device, 3 hits) · full-frame · `beat-c4b5-25x-slam.html`
- **Comp:** 58.5–72.8 · **Src:** 1089.26–1103.56 · `data-start 58.5` / `data-duration 14.3`
- **View:** full-frame (V2 — both speakers, dark gradient backdrop). ~3s of breath after the c4b4 stamp precedes the first slam. **V1 push-in (v4-REV #8): the master applies a subtle slow scale 1.0→~1.03 on the (full-frame) video centered on Jasper across ~63.8–72 so the 54s full-frame block is not static-video-plus-floating-overlays.**
- **NO INDEX (R6):** `caption-kinetic-slam`, no eyebrow, **no index** slot rendered.
- **Install:** `npx hyperframes add caption-kinetic-slam` → white slams, single cyan payoff, Inter 900, hero scale for the number. The **only** 25× appearance in the clip.
- **Slam sequence — WORD-SYNCED, COMPRESSED TO 3 HITS (v4-REV #5 — fewer/bigger hits, the hero is no longer buried):**
  - **`25×`** — hero number, Inter 900 ~220px `#FFFFFF` — spoken **"20 or 25x"**: 25x@comp **63.76** → slam **comp 63.76** (scale-pop, `back.out`). **Held LONGER than v4 (it owns ~63.8→66.8 alone) so it lands before the comparison.** A small muted held sub `25× MORE` can sit under the hero (the "times more" idea as context, not a separate slam).
  - **`DERIVATIVES vs SPOT`** (`#FFFFFF`, "vs" muted `#6B7480`) — ONE comparative slam (replaces v4's separate `TIMES MORE` + `DERIVATIVES` + `THAN SPOT`) — cued to spoken **"derivatives … than spots"** — derivatives@comp **66.88**, spots@comp 67.84 → slam **comp 66.88** (enters from right; "vs SPOT" snaps in by 67.84). *(This is the spot the optional `data-chart` 2-bar ratio could replace/augment — v4-REV #6.)*
  - **`$226K MELT-UP`** (cyan `#00D4FF` + glow, payoff) — spoken **"the melt up … 226k"**: melt@comp **69.92**, 226k@comp 71.82 → slam cyan **comp 69.92**, `$226K` emphasized on **comp 71.82**.
- **Spoken words each line matches:** "25×"="20 or 25x"; "DERIVATIVES vs SPOT"="derivatives … than spots"; "$226K MELT-UP"="the melt up… 226k".
- **Cyan element:** `$226K MELT-UP` payoff only (the `25×` hero stays white — D7 "stat OR accent").
- **Anti-static:** hero `25×` scale-pop held → one comparative slam → cyan payoff, across 63.8→71.8, over a subtly pushing-in video. Three clean hits, the hero owns its moment. Exits ~comp 72.4.
- **Date (D7 / §8):** the crash + $226K melt-up are last year's event, but §8 is a HARD RULE — never render the literal year "2025"/"2024". The c4b2 eyebrow uses the relative form `LAST OCTOBER` (today 2026-06-02 → Oct 2025 = last October). No literal year reaches any frame.

### c4b6 — liquid-glass 2-part card (leverage-fueled rally) on full-frame backdrop · full-frame · `beat-c4b6-leverage-not-spot.html`
- **Comp:** 75.0–80.0 · **Src:** 1105.76–1110.76 · **`data-start 75.0` / `data-duration 5.0` (ONE value everywhere — prior-round fix #4; NO 74.8/5.2 variant in this doc).**
- **View:** full-frame (V2 — both speakers; card in the LEFT zone over a dark-gradient backdrop so the host side is darkened while both speakers stay visible). **Breaks the run** between the c4b5 slam and the c4b8 closer (slam → card → kinetic = no 3-in-a-row).
- **NO INDEX (R6):** **DELETE the `#c6-idx` div (`beat-c4b6…:31`), its CSS (line 70), and its GSAP tween (line 117).** No "06"/"04" in this sub-comp.
- **Why this content:** the on-screen claim MUST match the line spoken at fire time (`_QA-CHECKLIST.md §3`). At the fire window the speaker is saying *"the melt-up… was **very heavily supported by leverage**"* (supported@comp 75.48, leverage@comp 76.20). The earlier "perp-side liquidation" idea (liquidation@comp 57.96) is spoken ~16.5s earlier and collides with c4b5 — unusable here. v4 surfaces the leverage point that matches the audio: the rally was driven by borrowed size, not spot demand. Repeats NO number, re-introduces NO swiss-grid chrome.
- **Card (full card, distinct from c4b4's compact stat-stamp — v4-REV #7):** `rgba(20,26,34,0.92)` fill, 4px cyan inset bar, glow, 1px border, mask feather. No blur, no grain.
- **Content (exact text + hex), with a 2-PART HEADLINE REVEAL (v4-REV #7 — not a clone of c4b4's static headline):**
  - Eyebrow **`WHAT FUELED THE MOVE`** — `#F0F0F0` Inter 700 32px — `EDITORIAL: structural label`.
  - Headline part-A **`LEVERAGE`** — `#FFFFFF` Inter 900 72px — lands on the operative word **leverage@comp 76.20**.
  - Headline part-B **`NOT SPOT`** — `#FFFFFF` Inter 900 72px — snaps in ~0.5s after part-A (~comp 76.7), the contrast beat. *(matches spoken "very heavily supported by leverage" — the "not spot" is the editorial contrast the whole card makes.)*
  - Sub **`the rally ran on borrowed size`** — `#B6BEC6` Inter 600 28px.
- **Entry — WORD-CUED:** card slides in from right; part-A `LEVERAGE` settles on leverage@comp 76.20, part-B `NOT SPOT` snaps in ~76.7. Card head begins its slide ~comp 75.4 (internal animation INSIDE the 75.0 data-start window — not a second data-start). Holds, exits ~comp 79.6.
- **Spoken words this card matches:** "very heavily supported by leverage."
- **Cyan element:** the 4px accent bar only.

### c4b8 — kinetic-type human closer · full-frame · `beat-c4b8-wiped-out.html`
- **Comp:** 80.6–88.2 · **Src:** 1111.36–1118.98 · `data-start 80.6` / `data-duration 7.6`
- **View:** full-frame (V2 — both speakers, dark gradient backdrop). Video stays full-frame through clip end — no card, no end screen (D4 no-outro).
- **NO INDEX (R6):** no index element.
- **Kinetic lines — phrase build, STAY (no dim), the human cost. L2 plain-language softened (v4-REV #9 — the closer reads as a human story, not a glossary term):**
  - **L1 `NEW TO PERPS`** (`#FFFFFF`) — spoken **"new to perp"**: new@comp **81.82**, to@comp 82.10, burp(perp)@comp 82.32 → slam **comp 81.82**. *(Whisper "burp"→on-screen "PERPS" per _JARGON.md.)*
  - **L2 `MAX LEVERAGE ON`** (`#FFFFFF`) — spoken **"cross margining enabled"**: cross@comp **83.90**, margining@comp 84.28, enabled@comp 84.80 → slam **comp 83.90**. *(v4-REV #9: the verbatim "cross-margining" is the most jargon-dense string in the clip and it's the SETUP for the emotional payoff; `MAX LEVERAGE ON` is the plain-language meaning of cross-margining-enabled — a viewer reads new-trader → over-leveraged → wiped out as one clean human arc. **Builder option:** if zero "LEVERAGE" cross-beat echo with c4b6 is preferred, use `ONE BAD TRADE` instead — both convey the same setup; `MAX LEVERAGE ON` is the closer paraphrase of the spoken line, `ONE BAD TRADE` is the cleaner-but-looser story beat.)*
  - **L3 `WIPED OUT`** (cyan `#00D4FF` + glow, payoff) — spoken **"absolutely … wiped out"**: wiped@comp **87.16**, out@comp 87.50 → slam cyan **comp 87.16**.
- **Spoken words each line matches:** L1="new to perp[s]"; L2="cross margining enabled" (rendered as plain-language `MAX LEVERAGE ON`); L3="wiped out".
- **Cyan element:** L3 only.
- **Clip end:** L3 lands ~87.5, holds ~0.5s, clip ends at comp 88.2 on **live full-frame video** (no outro, D4). The ending is the human consequence — a different beat-type than the 25× stat.

---

## VERIFICATION GATE (graded against `_QA-CHECKLIST.md` + this round's R6/R7)

- **R6 NO INDEX:** every sub-comp index div (`#c2-idx`, `#c4-idx`, `#c6-idx`) + its CSS + its GSAP tween DELETED; grep-gate (`c2-idx|c4-idx|c6-idx|>04<|>02<|>06<`) + per-frame check confirm no index/clip-number/beat-index anywhere. Eyebrow editorial labels only. **PASS (enforced at build).**
- **R7 NO BLANK-LEFT MODE-A:** one Mode-A block (cascade) with the flowchart filling AND building the left zone for its entire 3.6→33.6 span (eyebrow/rule/node-1 at the shrink; setup nodes at 5.44/7.52/14.58 so no >6.5s freeze); all breaths/cards/slams are full-frame (both speakers); cards sit on a full-frame dark-gradient backdrop, never cropped-right-with-empty-half; the v3 46.0/58.3 Mode-A switches are deleted. **PASS.**
- **§1 R1 view discipline:** 2 view-blocks (Mode-A 30.5s, full-frame 54.2s) + 3.5s intro; every non-intro segment ≥30s; no segment <8s; no A-B-A (neither view recurs). **PASS.**
- **§2 R2 variety:** primary device = `flowchart` cascade cold open; after the cut of c4b3 there is exactly ONE slam (c4b5) and it's never adjacent to another slam/kinetic (flowchart → card → slam → card → kinetic); `caption-kinetic-slam` for the 25× per task; `data-chart` actively re-considered for the 25× and offered as an optional upgrade. The cascade now BUILDS (no frozen device). **PASS (stronger than v4).**
- **§3 dialog-match + text-appears-as-spoken:** opens on the spoken line at in-point 1030.76; first text comp 0.08; ALL fire-times read off the table's `comp_t` column; **every CONTENT beat's claim is the line spoken at its fire time** — c4b2 setup nodes fire on verbatim "long spot"@5.44 / "short the perp"@7.52 / "deeply in the money"@14.58; node-7 on "feedback loop"@24.74 (was fabricated "forced selling"); c4b6 on "leverage"@76.20. The fabricated-number c4b3 is cut. **PASS.**
- **§4 R5 coherence:** "YOUR DELTA / COMPLETELY SHIFTS" is a complete thought; cyan payoff is the verb `SHIFTS`. **PASS.**
- **§5 framing:** `object-position:83% center`, Mode-A clearances 108px/108px, full-frame beats show both speakers, V1 push-in on Jasper during the 25× stretch; verify-by-frame list provided (incl. the no-index, no-blank-left, and cascade-is-building checks). **PASS** (re-verify at build).
- **§6 R3 jargon:** every on-screen string audited; all four "burp"→perps handled (PERP/PERPS on screen; no raw burp); ADL/derivatives/spot/leverage/ITM casing correct. **PASS.**
- **§7 R4 duplicates:** no eyebrow-vs-title duplicate in any beat; the fabricated "FORCED SELLING" + its `→` glyph removed; cross-beat "wiped" pre-echo avoided; the only cross-beat echo (LEVERAGE c4b6→c4b8) is flagged with a zero-echo `ONE BAD TRADE` fallback. **PASS.**
- **§8 hard rules:** all 6 ids in z-index:3 (c4b3 removed); ONE cyan element per beat (listed each beat — c4b1 cyan moved to `SHIFTS`); no backdrop blur / no grain (card recipe = solid fill + accent bar + glow); eyebrows Inter 700 ≥30px `#F0F0F0`, body ≥600, muted = `#B6BEC6` (NO `#888`); no intro/outro (ends on live video); dates use relative form (`LAST OCTOBER`, no literal "2025"/"2024"); phrase kinetics build & STAY (no dim). **PASS.**
- **Beat count = 6.** Clip is 88.2s (<90s), so the 6-beat floor applies and is met; the thin REAL/COMPRESSION slam and the redundant 25× swiss-grid were cut deliberately for R2/pacing.
- **Numeric consistency:** the ONLY on-screen duration is c4b4 `30–45 MIN` (the fabricated "40 MINUTES" never appears — c4b3 is gone). c4b6 `data-start 75.0/5.0` stated identically everywhere (no 74.8 drift).
- **§9 verify-by-frame:** MANDATORY at build — frames at 0.5 / 3.7 / 6 / 16 / 34 / 52 / 63.8 / 76.5 / 82; at EVERY frame confirm (a) no index number, (b) Mode-A only during the cascade with the flowchart present AND building, (c) breaths/cards full-frame both speakers. Do not report done from self-report.

---

## Inlined word table (src_in = 1030.76; `comp_t = src − 1030.76`) — **`comp_t` IS the EDL fire-time; read it directly, never compute.**

**Offset reconciliation (v4-REV #10 — the comp-offset footgun fix):** `clip4-words.txt` on disk uses offset 1010, so its `comp` column = `EDL comp + 20.76`. To eliminate the hand-subtraction risk, the table below carries BOTH columns: **`comp_t` (EDL/this doc, offset 1030.76) AND `wt` (the number in `clip4-words.txt`, offset 1010)**. A builder grepping `clip4-words.txt` for a fire-time must look up the `wt` value, NOT the `comp_t` value — e.g. c4b2 node-4 `PERP DEEP ITM` fires at EDL `comp_t 14.58`, which is `wt 35.34` ("deeply") in the words file. **RECOMMENDED: regenerate `clip4-words.txt` with offset 1030.76 so `wt == comp_t` (Δ=0) and this footgun disappears entirely.** Until then, use the `wt` column to cross-check the words file.

```
comp_t    wt      src_t    word
  0.00   20.76   1030.76  your         <- c4b1 L1
  0.16   20.92   1030.92  delta        <- c4b1 L1
  0.48   21.24   1031.24  completely   <- c4b1 L2 (white)
  0.98   21.74   1031.74  shifts       <- c4b1 L2 (CYAN — v4-REV #3)
  1.46   22.22   1032.22  in
  1.62   22.38   1032.38  your
  1.74   22.50   1032.50  structure
  3.20   23.96   1033.96  delta        <- c4b2 node1 cue "delta neutral" (reveal @3.6, with the shrink)
  3.46   24.22   1034.22  neutral,     <- c4b2 node1 cue
  5.44   26.20   1036.20  long         <- c4b2 NODE2 cue "long spot" (v4-REV #1; reveal @5.44)
  6.80   27.56   1037.56  spot,        <- c4b2 node2 cue
  7.52   28.28   1038.28  short        <- c4b2 NODE3 cue "short the perp" (v4-REV #1; reveal @7.52)
  8.14   28.90   1038.90  burp(perp).  <- c4b2 node3 cue (on-screen "SHORT PERP"); spoken perp #1
 13.92   34.68   1044.68  burp(perp)   <- spoken perp #2 (part of "your perp is deeply ITM")
 14.58   35.34   1045.34  deeply       <- c4b2 NODE4 cue "deeply in the money" (v4-REV #1; reveal @14.58)
 15.20   35.96   1045.96  money.       <- c4b2 node4 cue (on-screen "PERP DEEP ITM")
 15.88   36.64   1046.64  closed       <- c4b2 node5 cue "closed out"
 16.24   37.00   1047.00  out          <- c4b2 node5 cue
 17.70   38.46   1048.46  naked        <- c4b2 node6 cue "naked long delta"
 18.14   38.90   1048.90  long         <- c4b2 node6 cue
 18.52   39.28   1049.28  delta.       <- c4b2 node6 cue
 21.62   42.38   1052.38  close        (spoken "close out that position" — the REAL cascade mechanic; NOT "forced selling")
 22.00   42.76   1052.76  out          (spoken)
 22.38   43.14   1053.14  position,    (spoken; context for node7)
 24.74   45.50   1055.50  feedback     <- c4b2 node7 cue "feedback loop" (renamed; NO "forced selling", NO → glyph)
 25.16   45.92   1055.92  loop         <- c4b2 node7 cue
 31.90   52.66   1062.66  60,          <- c4b2 node8 cue (cyan)
 32.40   53.16   1063.16  70,          <- c4b2 node8 cue (cyan)
 32.78   53.54   1063.54  80%.         <- c4b2 node8 cue (cyan)
 34.52   55.28   1065.28  extremely    (live video, V2 BREATH — NO overlay; c4b3 slam was CUT in v4-REV #4)
 34.98   55.74   1065.74  hectic,      (live video, V2 breath — NO overlay)
 42.28   63.04   1073.04  real         (live video, V2 breath — c4b3 REAL slam CUT; this word is now audio-only)
 43.46   64.22   1074.22  compression  (live video, V2 breath — c4b3 COMPRESSION slam CUT; audio-only)
 50.36   71.12   1081.12  It           (c4b4 data-start ~50.8; stat-stamp head begins)
 51.58   72.34   1082.34  half         <- c4b4 stat cue "half an hour to 45 min" (number settles here)
 52.24   73.00   1083.00  45           <- c4b4 cue
 52.64   73.40   1083.40  minutes      <- c4b4 cue
 57.96   78.72   1088.72  liquidation  (spoken "liquidation on the perp side" — inside c4b5's window; NOT a fire cue)
 58.98   79.74   1089.74  burp(perp)   <- spoken perp #3 (audio-only; collides with c4b5, not on screen)
 60.88   81.64   1091.64  leverage     (first "leverage" mention; context for c4b5/c4b6)
 63.76   84.52   1094.52  25x.         <- c4b5 "25×" hero lands (held longer — v4-REV #5)
 65.68   86.44   1096.44  times        (spoken "25 times more" — now the held hero's sub-context, NOT a separate slam)
 66.88   87.64   1097.64  derivatives  <- c4b5 "DERIVATIVES vs SPOT" (one comparative slam — v4-REV #5)
 67.84   88.60   1098.60  spots,       <- c4b5 "DERIVATIVES vs SPOT" ("vs SPOT" snaps in here)
 69.92   90.68   1100.68  melt         <- c4b5 "$226K MELT-UP" (cyan)
 71.82   92.58   1102.58  226k         <- c4b5 "$226K" (cyan)
 74.18  104.06*  1104.94  heavily      (spoken "very heavily supported by leverage")  [*wt drift in raw file; src is authoritative]
 75.48   96.24   1106.24  supported    (spoken; the c4b6 claim's verb — fire cue is the noun "leverage" below)
 76.20   96.96   1106.96  leverage.    <- c4b6 card cue (part-A "LEVERAGE" lands; part-B "NOT SPOT" snaps in ~76.7)
 81.82  102.58   1112.58  new          <- c4b8 L1 "NEW TO PERPS"
 82.10  102.86   1112.86  to           <- c4b8 L1
 82.32  103.08   1113.08  burp(perp)   <- c4b8 L1 (on-screen "PERPS"); spoken perp #4
 83.90  104.66   1114.66  cross        <- c4b8 L2 (rendered plain-language "MAX LEVERAGE ON" — v4-REV #9)
 84.28  105.04   1115.04  margining    <- c4b8 L2
 84.80  105.56   1115.56  enabled      <- c4b8 L2
 87.16  107.92   1117.92  wiped        <- c4b8 L3 "WIPED OUT" (cyan)
 87.50  108.26   1118.26  out.         <- c4b8 L3 (cyan)
 88.22  108.98   1118.98  So           <- clip end (src_out 1118.98)
```

*(Whisper transcribes perp/perps as "burp" throughout this window — all four occurrences (src 1038.90, 1044.68, 1089.74, 1113.08) are perp/perps. On-screen text uses the correct trading term per `_JARGON.md`; perp #2 (src 1044.68) is the "deeply ITM" leg, perp #3 (src 1089.74) is audio-only. "forced selling" and "40 minutes" do NOT appear anywhere in this table or the clip — both were fabrications removed in v4. The `wt` column = the value in `clip4-words.txt` for cross-checking that file (one raw-file drift noted at "heavily" — `src_t` is authoritative). Cross-offset spot-checks (Δ=20.76): long@1036.20→wt 26.20→EDL 5.44 ✓; deeply@1045.34→wt 35.34→EDL 14.58 ✓; feedback@1055.50→wt 45.50→EDL 24.74 ✓; leverage@1106.96→wt 96.96→EDL 76.20 ✓; wiped@1117.92→wt 107.92→EDL 87.16 ✓.)*
