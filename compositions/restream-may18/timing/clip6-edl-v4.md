# Clip 6 — Four-Year Cycle Dead? — v4 BUILD-READY EDL

**Status:** v3 build was REJECTED. The user saw two on-screen defects ("everything has an issue"): the internal "06" index rendered on screen, and a cropped-right speaker with a blank left half. v4 fixes both by **re-architecting the view-timeline so the view always equals the content** — kinetics play full-frame (both speakers), graphics play Mode-A, and the Mode-A block contains ONLY left-zone graphics. This makes blank-left structurally impossible instead of papering over it with overlaps. All four Agent-3 spec defects are resolved.

> **⚠ BUILD-STATE / RENDER-HYGIENE WARNING (read first).** The on-disk files are STILL v3 and the existing HQ render is the rejected build:
> - `clip-6-four-year-cycle/index.html` (09:08) shrinks to Mode-A at **comp 3.0** and puts the answer kinetic in Mode-A (c6b2 `data-start="3.0"`); `beat-c6b2` (09:08) still renders `#b2-idx` "06" + Mode-A chrome; `beat-c6b3` (09:43) still has the reward-ladder captions and fires the 2028 tick at offset 9.4. `beat-c6b4`/`c6b5` (09:10) use v3 offsets.
> - `renders/clip-6-four-year-cycle-HQ.mp4` is dated **09:58 — i.e. it was rendered from the v3 build above** (it predates none of the v4 edits because the v4 edits do not exist on disk yet). **It is the rejected v3 render. DELETE it before the next build** (`rm clip-6-four-year-cycle/renders/clip-6-four-year-cycle-HQ.mp4`) so it is not mistaken for the v4 render; per QA §10, only re-create HQ AFTER the v4 build passes §VBF.
> - **This EDL is the SPEC, not the current files.** Apply every row of the §CHANGE SUMMARY work-order, then render a draft and run §VBF. Do NOT render the c6b3→c6b4 seam check (VBF #5 / §8 ledger) against the current files — that ledger is only true AFTER the c6b3 retime ships (see §8 note).

> **🔒 CANONICAL VIEW-SWITCH PAIR (state once; every other number must match these — fixes the prior 14.0/40.4 ambiguity).**
> - **FULL → Mode-A SHRINK at comp `14.7`** (0.5s `expo.inOut`). `#bg-glow` fades in @14.7; `#zone-rule` draws @14.9.
> - **Mode-A → FULL EXPAND at comp `40.2`** (0.4s `expo.inOut`). `#bg-glow`/`#zone-rule` fade @40.0.
> - Dependent instants locked to this pair: c6b2 stack exit **14.4** (< shrink-complete 15.2); c6b3 axis baseline in **14.9**, axis fade-out **26.1**; c6b4 `.b4-inner` exit **40.2** (coincident with expand). **There is no 14.0, 14.95, or 40.4 anywhere in v4 — if you see one, it is a leftover v3 number; use 14.7 / 40.2.**

---

## WHY v4 (every fix, mapped to the rule)

### TOP-PRIORITY (user-flagged this round)

1. **R6 — NO INDEX ON SCREEN (the headline rejection).** The on-disk v3 `beat-c6b2-was-dead-it-is.html` literally renders `<div id="b2-idx">06</div>` (line 28) and animates it in (GSAP line 100). That bare "06" is the internal clip number — meaningless to a viewer, forbidden by R6. **v4 deletes the index entirely** from c6b2 (markup + CSS + GSAP). No beat renders any clip number or beat index. Editorial eyebrows ("HALVING CADENCE · EVERY 4 YEARS", "BLOCK REWARD · BTC ISSUANCE") stay — those are real labels; the years on the chart/timeline (2009–2028) are real data labels, not indices.

2. **R7 — NO BLANK-LEFT MODE-A (the structural rejection) — fixed at the root, not patched.** v3 forced the *answer kinetic* into Mode-A and padded it with chrome, then let `.b2-inner` fade (comp ~13.6) before c6b3's first graphic appeared (comp 15.22) → a ~1.6s cropped-speaker-with-empty-left gap (the exact clip-8 0:33–0:52 bug). **Root cause: a kinetic word-stack was placed in Mode-A.** Per R7/DESIGN.md, a kinetic = both speakers = FULL-FRAME; only a left-zone graphic = Mode-A. **v4 re-classifies every beat by content and groups them so the view matches at every instant:**
   - **Kinetics → FULL-FRAME** (c6b1 host-Q, c6b2 answer, c6b5 close, c6b6 kicker). Both speakers.
   - **Left-zone graphics → MODE-A** (c6b3 halving timeline, c6b4 decay chart). A real graphic fills the left zone for the ENTIRE Mode-A block.
   - **The answer ("THOUGHT IT WAS DEAD / NOW IT IS") moves OUT of Mode-A into the full-frame opening block** alongside the host question (it is the natural Q→A exchange, both speakers). The Mode-A block then contains **only the two chart devices**, both of which occupy the left zone continuously → **there is no graphic-less instant inside Mode-A, so blank-left cannot occur.**

   This is fundamentally more robust than v3's "add overlaps + filler" approach: instead of trying to keep a kinetic's left zone painted, the kinetic simply isn't in Mode-A at all.

### AGENT-3 SPEC DEFECTS (all four resolved)

3. **#1 R8 one-cyan-at-the-seam.** In v4 the answer (c6b2) is full-frame and **fully exits before Mode-A begins** (its cyan "NOW IT IS" is gone by comp 14.4, ~11s before the next cyan). The remaining seam is c6b3→c6b4 (comp 26.0–26.4): the c6b3 baseline is drawn **neutral `#2a2a2a`** (the only cyan on the timeline is the 2028 tick), and every c6b4 element entering during the cross-dissolve (eyebrow, rule, first bars) is **neutral** — c6b4's only cyan (the 1.56 bar) does not light until comp 31.32. So the cross-dissolve carries **exactly one** cyan (c6b3's fading 2028 tick). Full frame-by-frame ledger in §8.

4. **#2 c6b4 verify targeted the wrong zone.** v3's verify said confirm the chart "clears the lower-third name tag (Jasper / Wintermute)." That tag is burned into the SOURCE video in the **right** zone (x:1229–1843); every c6b4 graphic is in the **left** zone (`.b4-zone` width 1152px) — non-overlapping halves that cannot collide. **v4 rewrites the c6b4 verify to the REAL risk: left-zone VERTICAL fit** (eyebrow + rule + 400px chart + annotation must not overflow 1080 or overlap the bars). **And c6b4 carries NO 3-item list** — just the chart + one annotation — so there is no list-vs-chart or list-vs-frame overflow to begin with. (The on-disk c6b4 layout already fits; the verify just confirms it.)

5. **#3 device distinctness (timeline = chart preview).** v3's c6b3 captions were the **reward ladder** `↓ 25 / ↓ 12.5 / ↓ 6.25 / ↓ 3.125 / ↓ 1.56` — the identical values c6b4 plots, making the timeline a horizontal preview of the chart (R2 fail). **v4 changes c6b3 captions to CADENCE/ERA labels** (`CYCLE 1 / CYCLE 2 / CYCLE 3 / CYCLE 4 / NEXT`). The **timeline now tells the WHEN story** (a halving every 4 years; four cycles done, one ahead) and the **chart tells the HOW-MUCH story** (the reward decaying 50→1.56). Disjoint data dimensions → two genuinely distinct devices. (The clip's whole subject is "the four-year cycle," so CYCLE 1–4 is exactly on-theme — each halving opens a market cycle.) **v4-revision reinforces this VISUALLY too:** the 2028 node is now a hollow cyan RING reached by a DASHED baseline extension (#5 below) so "four done, one ahead" reads at a glance — the timeline looks nothing like the chart's filled descending bars.

6. **#4 c6b3 internal "HALVING" dup (R4).** v3 had eyebrow "HALVING CADENCE…" + 2028 caption "↓ NEXT HALVING" = "HALVING" twice in one beat. **v4's 2028 caption is "↓ NEXT"** (no second "HALVING"). The spec BODY and the build note agree (no contradiction). R4-clean.

7. **#5 ≤2 kinetics in a row (borderline, held).** Opening run = **2** (c6b1 + c6b2, both full-frame), broken by the two chart devices; close = **2** (c6b5 + c6b6). Passes with zero margin. **BUILD-AGENT NOTE: do NOT add a kinetic line to c6b2 or the close** — any added kinetic beat fails R2. (v4 deliberately does NOT add the "ON RECORD MULTIPLE TIMES" line a prior draft proposed — that would not break R2 since c6b2 is still one kinetic beat, but the answer is kept tight at 2 phrases; see c6b2.)

8. **#6 word-table citation.** Fixed: **"block" = src 1449.66** (clip6-words.txt line 263); "rewards" = src 1450.04. Both fire-times below cite the correct src.

### KEPT from v3 (verified, still correct)
- src window `1420.30 → 1471.00` (opens on the real host question; cuts before the host pivot "Interesting" at src 1471.24).
- `object-position: 83% center`; Mode-A geometry `{1229, 108, 614, 864}`.
- The decay-chart values (50/25/12.5/6.25/3.125/1.56 over 2009/2012/2016/2020/2024/2028) and `caption-neon-glow` (already adapted on-disk) on the closing payoff.
- Every fire-time below is read off `clip6-words.txt` as `comp = src − 1420.30`, verified to the centisecond against `.context/episodes/restream-may18/audio.json`.

---

## WINDOW (unchanged)

| | value | note |
|---|---|---|
| **src_in** | **1420.30** | ~0.12s before the host's "Would" (src 1420.42). Trims the trailing "Yeah." (src 1419.74) at the head. |
| **src_out** | **1471.00** | After Jasper's kicker "…still a very strong narrative, I think." (ends src ~1469.60) + ~1.4s clean breath ("Yeah." at 1470.38). Cuts BEFORE the host pivot ("Interesting" src 1471.24). |
| **duration** | **50.70s** | comp = src − 1420.30 |
| **comp basis** | **comp = src − 1420.30** | every fire-time below = the `clip6-words.txt` src_t minus 1420.30; never hand-computed. Verified against `audio.json` (exact match across 1419.74–1471.24). |

> **clip6-words.txt header note:** the table's header reads `comp = src − 1350` (the OLD 120s window). The **src_t column is ground truth**; this clip's comp = src_t − 1420.30. Each fire-time below quotes the src_t and the subtraction.

**OPENING LINE (R3 dialog-match + R5 coherence):** opens on the HOST question **"Would you say the four year cycle is dead?"** — a complete, self-contained question spoken in the first 2.02s, word-synced (NOT anticipatory). It is the clip's title line. (DESIGN.md permits a host question as its own full-frame word-stack, no "HOST" label.)
- Matches audio.json 1420.42–1422.52: *"Would you say the four year cycle is dead?"*

---

## VIEW-TIMELINE (proves R1 + R7) — THE FIX

| # | segment | view | comp start | comp end | dwell | beats | LEFT-ZONE GRAPHIC (Mode-A only — none may be graphic-less) |
|---|---------|------|-----------:|---------:|------:|-------|---|
| 1 | host-Q + answer | **FULL-FRAME** (both speakers) | 0.0 | 14.7 | **14.7s** | c6b1 · c6b2 | — (kinetics over full-frame video; no left-zone crop by design, so R7 N/A) |
| 2 | halving timeline → decay chart | **MODE-A** (Jasper right, graphic left) | 14.7 | 40.2 | **25.5s** | c6b3 · c6b4 | **c6b3 halving-cadence TIME-AXIS (appears comp 14.9 → 26.4) → c6b4 block-reward DECAY CHART (26.0 → 40.2).** A graphic fills the left zone the ENTIRE 25.5s; the two overlap comp 26.0–26.4 (cross-dissolve) so there is no instant without a graphic. |
| 3 | closing kinetics + clean tail | **FULL-FRAME** (both speakers) | 40.2 | 50.7 | **10.5s** | c6b5 · c6b6 | — (kinetics over full-frame, then ~1s clean speaker tail; R7 N/A) |

**Transitions:** exactly TWO — FULL→MODE-A at comp 14.7 (shrink), MODE-A→FULL at comp 40.2 (expand).

**R7 BLANK-LEFT PROOF (the headline fix):** the Mode-A block (14.7–40.2) contains **only the two chart graphics**, never a kinetic or a breath. A graphic is on screen the entire time:

| moment | what fills the left zone | blank-left? |
|---|---|---|
| FULL→Mode-A shrink (14.7→15.2) | **c6b3 axis baseline appears at comp 14.9** (offset 0.2) — i.e. while the video is still shrinking; the left zone has the axis structure before the crop completes | **NONE** |
| c6b3 hold (15.2→26.0) | c6b3 timeline (eyebrow + axis + era ticks) | NONE |
| c6b3 → c6b4 seam (26.0→26.4) | c6b4 chart enters at 26.0 while c6b3 holds to 26.4 → **0.4s overlap** = the cross-dissolve | **NONE** |
| c6b4 hold (26.4→40.2) | c6b4 decay chart | NONE |
| Mode-A→FULL expand (40.2) | c6b4 `.b4-inner` exits at comp 40.2 **coincident with the expand** → the left clears at the instant both speakers fill the frame | **NONE** |

Every kinetic/breath beat (c6b1, c6b2, c6b5, c6b6) is **full-frame** (both speakers). There is **no cropped speaker with a blank left half anywhere in the clip.** This is the v3→v4 structural fix.

**R1 PROOF:**
- 3 segments, dwell 14.7s / 25.5s / 10.5s — none < 8s. PASS.
- Only A-B-A pattern is `FULL→MODE-A→FULL`; FULL is left at 14.7 and not re-entered until 40.2 → gap 25.5s ≫ 12s. No A-B-A within 12s. PASS.
- Consecutive graphic beats (c6b3 + c6b4) grouped in the ONE Mode-A view; consecutive kinetics grouped in the full-frame blocks → the frame does not bounce. PASS.

**One-liner:** `FULL 0–14.7 (host-Q + answer, both speakers) → MODE-A 14.7–40.2 (halving timeline 14.9–26.4 → decay chart 26.0–40.2, graphic the entire time, zero blank-left) → FULL 40.2–50.7 (closing kinetics + neon payoff + clean tail).`

---

## STRUCTURE / TEMPLATE VARIETY (proves R2)

**Template sequence:** `kinetic(host-Q) → kinetic(answer) → TIMELINE device → nyt-graph CHART (HERO) → kinetic(close) → kinetic+neon-glow(kicker)`

| metric | value | rule | result |
|---|---|---|---|
| distinct PRIMARY device | halving **timeline** (c6b3, cadence/WHEN) + `nyt-graph` **decay chart** (c6b4, reward/HOW-MUCH) — the two longest-dwelt beats (~25s combined), the visual centre | R2: distinct device, not kinetic-dominated | PASS — clip 6 is the series' chart/data clip |
| timeline vs chart distinctness | timeline captions = **cadence/era** (`CYCLE 1…4 / NEXT`); chart bars = **reward values** (`50→1.56`). **Disjoint data series.** | R2: two devices must not carry the same data | PASS (v3's reward-ladder timeline is fixed) |
| max kinetics in a row | **2** (c6b1 + c6b2), then the two chart devices; close = **2** (c6b5 + c6b6) | R2: ≤2 in a row | PASS (zero margin — do not add a kinetic) |
| init template | chart beats init from `nyt-graph` (NOT `kinetic-type`) | R2: chart content ≠ init kinetic | PASS |

**DESIGN.md opening rule (full-frame kinetic variant):** a full-frame kinetic open satisfies the "aggressive open" via the **multi-phrase build with cyan payoff** — c6b1 fires phrase 1 at comp 0.12, phrase 2 at 0.94, cyan payoff at 2.02 (3 staged text elements over both-speaker video, first text at comp 0.12). This is the correct pattern for a clip whose first content is a spoken Q&A: R7 keeps kinetics full-frame, so there is no Mode-A left zone to stack "3 element types" into during the open. (The "3 left-zone element types in 6s" form of the rule applies to Mode-A opens; a full-frame kinetic open uses the phrase-build + payoff instead.)

**Catalog blocks — install vs hand-build:**

| beat | device | source | action |
|---|---|---|---|
| c6b3 | halving timeline (horizontal cadence axis 2012→2028, era ticks) | hand-build (no single catalog block is a labelled halving event-axis; `data-chart` is bar/line, not a named-tick time-axis) | **HAND-BUILD** — `beat-c6b3-halving-timeline.html` (edit the on-disk file per c6b3 detail) |
| c6b4 | block-reward decay bars | `nyt-graph` descending-bar pattern (already realized on-disk in `beat-c6b4-halving-decay.html`) | **REUSE/RETIME** the on-disk file to the v4 offsets below |
| c6b6 payoff "NARRATIVE" | premium neon reveal on the single payoff word | `caption-neon-glow` (installed at `compositions/components/caption-neon-glow.html`; already adapted on-disk in `beat-c6b6`) | **KEEP** the adapted on-disk neon (brand cyan, no dim-back) |
| (considered, not used) | `caption-kinetic-slam`, `shimmer-sweep`, `data-chart`, `flowchart` | — | the timeline + nyt-graph + neon-glow trio already carries the variety without a second stat-grid |

---

## FRAMING (Mode-A — verified value kept from v3)

- **`object-position: 83% center`** — centers Jasper (guest, right half); name lower-third "Jasper De Maere / Wintermute" fully in-frame; seam/Nic excluded. (Crop test 80/83/86 → 83% cleanest.)
- **Mode-A geometry:** `{ left: 1229, top: 108, width: 614, height: 864 }`, `borderRadius: 6px`, entry shrink `expo.inOut` 0.5s. Top clearance 108px, bottom clearance 108px → name never clips. Static camera (head fixed) → **Mode A** (not Mode B).
- **Entry shrink at comp 14.7** (0.5s); the c6b3 axis baseline is already drawing (comp 14.9) so the crop never opens onto an empty half.
- **Exit expansion at comp 40.2** (0.4s); c6b4 `.b4-inner` exits on the same instant so the left clears as both speakers fill the frame.
- Full-frame beats (c6b1, c6b2, c6b5, c6b6) show **both speakers** (text over a dark left-zone gradient, never text on black).
- **VERIFY-BY-FRAME (mandatory before render):** see §VBF.

---

## BEAT MAP

| Beat | comp range | src range | Template / block | View | Sub-comp file |
|------|-----------|-----------|------------------|------|---------------|
| c6b1 | 0.0–8.5 | 1420.30–1428.80 | `kinetic-type` (host question) | FULL-FRAME (both) | `beat-c6b1-host-cycle-dead.html` |
| c6b2 | 8.5–15.2 | 1428.80–1435.50 | `kinetic-type` (answer) | **FULL-FRAME (both)** | `beat-c6b2-was-dead-it-is.html` |
| **c6b3** | **14.7–26.4** | **1435.00–1446.70** | **Halving TIMELINE (cadence/era) — device #1** | MODE-A | `beat-c6b3-halving-timeline.html` |
| **c6b4** | **26.0–40.3** | **1446.30–1460.60** | **`nyt-graph` block-reward DECAY — HERO device #2** | MODE-A | `beat-c6b4-halving-decay.html` |
| c6b5 | 40.2–46.4 | 1460.50–1466.70 | `kinetic-type` (closing) | FULL-FRAME (both) | `beat-c6b5-doesnt-matter.html` |
| c6b6 | 46.4–50.7 | 1466.70–1471.00 | `kinetic-type` + `caption-neon-glow` payoff → clean tail | FULL-FRAME (both) | `beat-c6b6-strong-narrative.html` |

**index.html `data-start` / `data-duration` (comp seconds):**
`c6b1 0.0 / 8.5` · `c6b2 8.5 / 6.7` · `c6b3 14.7 / 11.7` · `c6b4 26.0 / 14.3` · `c6b5 40.2 / 6.2` · `c6b6 46.4 / 4.3`

**Track assignment & the only two overlaps:**
- **c6b2 (full-frame answer) ends comp 15.2; c6b3 (Mode-A timeline) starts comp 14.7** → 0.5s overlap. Intentional: during 14.7–15.2 the video is shrinking full→Mode-A, c6b2's answer phrases are already drifting up/out (exit at offset 5.6 = comp 14.1, gone by 14.4), and c6b3's axis is establishing. Put **c6b3 on `data-track-index="4"`** (c6b2 on track 3). No two text stacks fight: c6b2's text is gone by 14.4; c6b3's first text (eyebrow) fires at 15.22.
- **c6b3 ends comp 26.4; c6b4 starts comp 26.0** → 0.4s cross-dissolve. Put **c6b4 on `data-track-index="3"`** (c6b3 on track 4). Both render over the z-index:2 video via the z-index:3 rule.

> **c6b3 2028-tick render check:** c6b3 `data-duration="11.7"` → clock 14.7→26.4. The 2028 cyan tick fires at comp 25.68 = **internal offset 10.98s < 11.7s → it renders** (holds ~0.7s, then the axis cross-dissolves out into c6b4). No cut-off.

**z-index:3 rule MUST list every id (6 ids, no stale c6b7/c6b8):**
`#beat-c6b1, #beat-c6b2, #beat-c6b3, #beat-c6b4, #beat-c6b5, #beat-c6b6 { z-index: 3; }`
The adapted `caption-neon-glow` lives INSIDE c6b6's sub-comp → no extra master-level id.

---

## BEAT DETAIL (every kinetic line: on-screen text + the transcript words it matches + comp_t + internal offset)

### c6b1 — `kinetic-type` (HOST QUESTION) · FULL-FRAME · comp 0.0–8.5
**Sub-comp:** `beat-c6b1-host-cycle-dead.html` — **NO CONTENT CHANGE; one TIMING change** (extend the on-disk exit so the question breathes). In index.html its `data-duration` changes 3.0→**8.5**; in the sub-comp, move the on-disk stack-exit tween from offset **2.74 → 7.8** (the on-disk file fires the exit at 2.74, which kills the question <1s after the cyan word — too fast for the clip's entire hook).
`<!-- WORD-SYNCED. Cold open IS the spoken host question. No "HOST" label, NO index number. -->`
Full-frame video, BOTH speakers, dark left-zone gradient backdrop. 3-phrase build, Inter 900 ~94px, each phrase STAYS (no dim).
**STRONGER HOOK (#10):** the rejection-bait payoff **"IS DEAD?" lights at comp 2.02 and now HOLDS lit ~5.8s solo** (the whole stack stays put — no exit at 2.74) while Jasper opens his answer ("I've been going on record multiple times…" begins src 1425.26 = comp 4.96). The question lands and lingers as the answer starts, instead of vanishing in under a second. Only then does the stack drift up/out at comp 7.8, bridging into c6b2. This is free with the 8.5s duration and makes the title question hit materially harder.
- **LINE 1 "WOULD YOU SAY"** — fires **comp 0.12** (offset 0.12) — matches *"Would"* (src 1420.42; "you" 1420.72, "say" 1420.84) — `#F0F0F0`
- **LINE 2 "THE FOUR-YEAR CYCLE"** — fires **comp 0.94** (offset 0.94) — matches *"four"* (src 1421.24; "year" 1421.52, "cycle" 1421.70) — `#F0F0F0`
- **LINE 3 "IS DEAD?"** — fires **comp 2.02** (offset 2.02) — matches *"dead?"* (src 1422.32; "is" 1422.08) — `#00D4FF` (cyan payoff + glow). **HOLDS lit through comp ~7.8** (the micro-pause + answer-open beat).
- **EXIT** — whole stack drifts up/out at offset **7.8** (comp 7.8) `power2.in` 0.3s → gone by comp 8.1, bridging into c6b2.

Cyan: LINE 3 only (lit comp 2.02–~7.8). **R5:** the three lines parse as one complete question; payoff "IS DEAD?" is a real phrase, not a number/fragment. PASS. **R6:** no index. PASS.

---

### c6b2 — `kinetic-type` (ANSWER) · FULL-FRAME (both speakers) · comp 8.5–15.2
**Sub-comp:** `beat-c6b2-was-dead-it-is.html` — **REWRITE REQUIRED** (the R6 + R7 fix beat).
`<!-- WORD-SYNCED answer kinetic, FULL-FRAME (both speakers). This beat MOVED OUT of Mode-A (it is a kinetic, not a left-zone graphic). NO index "06", NO eyebrow chrome, NO corner marks, NO rule. Same full-frame kinetic treatment as c6b1/c6b5/c6b6: dark left-zone gradient backdrop + a phrase build that STAYS. -->`

**DELETE from the on-disk file (R6 + R7 fixes):**
- `<div id="b2-idx">06</div>` + its CSS rule + its GSAP tween (the rendered "06" — R6 violation; this is the only place "06" appears in the clip),
- `<div id="b2-eye">THE BULL-CASE</div>` + its CSS/GSAP,
- `<div id="b2-rule">` cyan rule + its CSS/GSAP,
- the four `.b2-reg` corner marks + their CSS/GSAP.
(None belong on a full-frame kinetic — they were Mode-A chrome.)

**BUILD as a full-frame kinetic** (mirror c6b1's structure): a `.b2-backdrop` left-zone dark gradient + a `.b2-words` phrase stack, Inter 900 ~88px, phrases STAY:
- **LINE 1 "THOUGHT IT WAS DEAD"** — fires **comp 9.02** (offset 0.52) — matches *"was"* (src 1429.32) / *"dead,"* (src 1429.54); lead-in "thinking that it was dead" (*thinking* 1428.36) — `#F0F0F0`
- **LINE 2 "NOW IT IS"** — fires **comp 13.16** (offset 4.66) — matches *"is."* (src 1433.46) in "the way it's currently playing out… like it is." — `#00D4FF` (cyan payoff)
- **EXIT** — whole stack drifts up/out at offset **5.6** (comp 14.1) `power2.in` 0.3s → fully gone by comp 14.4, BEFORE the FULL→Mode-A shrink completes (15.2). This guarantees the answer kinetic is off-screen when the video crops, and its cyan ("NOW IT IS") is gone ~11s before c6b3's cyan tick (comp 25.68).

Cyan: LINE 2 only. Between the host-Q exit (comp 8.1) and "THOUGHT IT WAS DEAD" (comp 9.02) is a ~0.9s full-frame breath (both speakers, Jasper mid-sentence) — correct under R7 (a breath is full-frame, never cropped).
**R2 note:** c6b2 stays a tight **2-phrase** answer. Do NOT add a third kinetic line (keeps the answer clean; the kinetic-in-a-row count is governed by beats, not lines, but the tighter the better for pacing into the charts).
**R4:** no eyebrow now; "THOUGHT IT WAS DEAD" / "NOW IT IS" share no notable word with each other or with c6b1. PASS. **R6:** index removed. PASS. **R7:** this beat is full-frame (a kinetic), so there is no left-zone crop to leave blank. PASS.

---

### c6b3 — Halving TIMELINE (cadence/era) — DEVICE #1 · MODE-A · comp 14.7–26.4
**Sub-comp:** `beat-c6b3-halving-timeline.html` — **EDIT REQUIRED** (caption-content fix #3 + dup fix #4 + retime).
`<!-- DISTINCT DEVICE #1: a horizontal halving-CADENCE time-axis (the WHEN story). NOT a bar chart (that's c6b4 — the HOW-MUCH story), NOT a kinetic stack. Captions are CADENCE/ERA labels, NOT reward values, so the timeline is NOT a preview of c6b4's chart. data-start="14.7" data-duration="11.7" → clock 14.7→26.4; the 2028 cyan tick at comp 25.68 (offset 10.98) lights before the 11.7s clock stops. -->`

A horizontal time-axis across the left zone: a **baseline rule** (scaleX draw L→R, x≈40→1032 within the 1152 left zone) with **5 era ticks**, each a node + year + a small **cadence caption** (NOT a reward value). Ticks pop left→right (`back.out(1.5)`, ~0.4s each) on the cadence. The **2028 tick is the SINGLE cyan accent** (the next/forward halving). The axis appears at comp 14.9 (offset 0.2 — while the video is still shrinking) so the left zone is never cropped-and-empty, and it hands off into c6b4 over the comp 26.0–26.4 cross-dissolve.

**STRONGER GRAPHIC — make "NEXT" read as forward/unknown, not just another node (#5, cheap CSS, no new elements, still one cyan):** right now all five ticks are visually identical filled dots and 2028 is differentiated by colour alone, so "four done, one ahead" doesn't read at a glance. v4 makes the past↔future split structural:
   - **Baseline rule is drawn in TWO segments.** The **2012→2024 span is SOLID neutral `#2a2a2a`** (the four completed cycles). The **2024→2028 span is a DASHED neutral `#2a2a2a` extension** (`border-top: 3px dashed #2a2a2a` on the rule's tail, or a sibling `.b3-base-future` pseudo/element with `background:none; border-top:3px dashed #2a2a2a` covering x≈724→952) — visually "the path continues into the unknown next cycle." Both segments are NEUTRAL (the rule never carries cyan; only the 2028 node does — preserves the §8 one-cyan ledger).
   - **The four PAST nodes (2012–2024) stay SOLID filled dots** (`background:#3a4452`). **The 2028 node becomes a HOLLOW/RING node** — `background: transparent; border: 3px solid #00d4ff` (cyan ring, transparent centre) instead of a solid cyan fill — reading as "open / not-yet-happened." Keep its cyan glow (`box-shadow` as on-disk). The cyan ring + dashed approach segment make 2028 unmistakably "the one still ahead," earning the accent without a second colour or a new caption.
   - This is pure CSS on existing nodes/baseline — do NOT add tick elements, a 6th node, or a 2009 node.

**On-screen text (Inter / JetBrains Mono, ≥30px, `#F0F0F0` except the one cyan tick):**
- Eyebrow **"HALVING CADENCE · EVERY 4 YEARS"** (Inter 700, ≥32px, `#F0F0F0`) — fires **comp 15.22** (offset 0.52) — matches *"very"* of "very self-fulfilling" (src 1435.52) as the device establishes during "it also has to do with liquidity cycles" `<!-- EDITORIAL label; device is temporal, not a single word -->`
- **Baseline rule** draws L→R (`scaleX 0→1`), **`#2a2a2a` NEUTRAL** (NOT cyan), in TWO segments per #5: **SOLID 2012→2024** + **DASHED 2024→2028** (the future extension) — appears **comp 14.9** (offset 0.2), draw completes ~15.5. (Neutral so the ONLY cyan on this device is the 2028 ring node — see §8.)
- Era ticks (node + year in JetBrains Mono ≥36px `#F0F0F0`; **cadence caption** in JetBrains Mono ≥30px below). Past nodes (2012–2024) = SOLID filled dots; the 2028 node = HOLLOW cyan RING (per #5):
  - **2012 · "CYCLE 1"** — pops **comp 17.24** (offset 2.54) — under *"also"* (src 1437.54) of "it also has to do with…"
  - **2016 · "CYCLE 2"** — pops **comp 18.18** (offset 3.48) — under *"liquidity"* (src 1438.48)
  - **2020 · "CYCLE 3"** — pops **comp 19.6** (offset 4.9) — EDITORIAL stagger (even L→R sweep between "liquidity cycles" and "the ultimate driver"; ~1.4s after 2016) `<!-- EDITORIAL stagger -->`
  - **2024 · "CYCLE 4"** — pops **comp 21.46** (offset 6.76) — under *"ultimate"* (src 1441.76) of "the ultimate driver"
  - **2028 · "↓ NEXT"** — HOLLOW CYAN RING node (per #5) — pops **comp 25.68** (offset 10.98) — lands on *"Bitcoin"* (src 1445.98) / *"halving,"* (src 1446.34), exactly as he names the halving — **`#00D4FF`** (cyan ring + glow). The single cyan: the "next halving" the whole device points at, and the seam into the decay chart. (The dashed 2024→2028 baseline extension is already on-screen as a neutral path before this; the ring is the only cyan.)

**Caption-content change (fixes #3 + #4):** the on-disk file currently has captions `↓ 25 BTC / ↓ 12.5 / ↓ 6.25 / ↓ 3.125 / ↓ 1.56` (the reward ladder — duplicates c6b4's data). **Replace with** `CYCLE 1 / CYCLE 2 / CYCLE 3 / CYCLE 4 / ↓ NEXT`. The 2028 caption is **"↓ NEXT"** (NOT "↓ NEXT HALVING") so "HALVING" appears once in the beat (eyebrow only) — R4-clean. Keep the 5 ticks/years as-is (2012/2016/2020/2024/2028); do NOT add a 2009 tick (a 2009 "↓ 50" tick would re-introduce the reward-ladder/chart-axis duplication — the timeline is a CADENCE device, not a reward axis).

**Retime (on-disk currently fires 2028 at offset 9.4; v4 fires per cadence):** set tick offsets **2.54 / 3.48 / 4.9 / 6.76 / 10.98** (2012/2016/2020/2024/2028), eyebrow **0.52**, baseline (solid + dashed segments) **0.2** (the dashed future-segment may draw with the solid, or fade in ~0.1s after — either reads). Add an axis cross-dissolve-out at offset **11.4** (comp 26.1, `opacity→0` 0.3s) so the whole device clears as c6b4 establishes (nothing lingers past the seam). The on-disk file has **NO exit tween** — without this fade the timeline would hard-cut instead of cross-dissolving into c6b4; add it.
**#5 CSS swap on-disk:** the on-disk 2028 node `.b3-node-accent` is a SOLID cyan fill (`background:#00d4ff`); change it to `background: transparent; border: 3px solid #00d4ff` (hollow ring) and keep the `box-shadow` glow. Split the on-disk single `.b3-base` (solid `#2a2a2a`, x 0→992) so the 2024→2028 portion (x≈724→952) renders dashed (`border-top:3px dashed #2a2a2a; background:none; height:0`) while 0→724 stays the solid 3px fill.

Cyan: the **2028 ring node** only (both baseline segments are neutral). One cyan.
Date note: 2012/2016/2020/2024/2028 are absolute historical/scheduled halving years (not relative "this year/last year") → permitted per DESIGN.md date rule.
**R4:** eyebrow "HALVING CADENCE · EVERY 4 YEARS" vs captions "CYCLE 1…4 / ↓ NEXT" vs years — no shared notable word ("HALVING" appears once). PASS.
**R2 distinctness:** captions are cadence/era (CYCLE count) — a different data dimension from c6b4's reward values → distinct devices, not a preview. PASS.
**R6:** the years 2012–2028 are real data labels on a time-axis, not a clip index. PASS. **R7:** graphic present 14.9→26.4 (overlapping c6b4) → no blank-left. PASS.

---

### c6b4 — `nyt-graph` BLOCK-REWARD DECAY — HERO (DEVICE #2) · MODE-A · comp 26.0–40.3
**Sub-comp:** `beat-c6b4-halving-decay.html` — **REUSE the on-disk file; RETIME + two targeted CLARITY edits** (values/colours already correct; the layout gets breathing room, the last bar collapses as motion, and a second neutral annotation fills the 32–40 hold; NO new DEVICE, NO 3-item list, NO new cyan).
`<!-- HERO. nyt-graph descending bars (the HOW-MUCH story). 6 bars on a shared baseline: 50 → 25 → 12.5 → 6.25 → 3.125 → 1.56 BTC over 2009·2012·2016·2020·2024·2028. scaleY 0→1 bottom-up, power3.out (no bounce). The 2028 / 1.56 bar = the single cyan (lights LAST, comp 31.32). All entering elements (eyebrow, rule, bars 50/25/12.5) are NEUTRAL so the c6b3→c6b4 cross-dissolve (comp 26.0–26.4) carries exactly one cyan (c6b3's fading 2028 tick). data-start="26.0" data-duration="14.3". -->`

**CLARITY/PACING (#7 — the decay must read as a MOTION, not three static stubs).** On-disk the chart is 6 cols × 116px + 5 gaps × 34px ≈ 866px inside the 992px inner zone (edge-to-edge, no breathing room), and bars 6.25/3.125/1.56 are 76/48/28px — nearly indistinguishable, so the "collapsing toward zero" point lands on the value labels, not the visual. v4 keeps all 6 bars (the 50→25 first halving is the most dramatic part of the collapse — do NOT drop the 2009/50 bar) and makes the decay cinematic two ways:
   - **Breathing room:** widen the chart gap and right-pad so it is not edge-to-edge — set `.b4-chart` `gap: 48px` (was 34px) and add right padding so the 6 cols sit comfortably inside the 992px inner zone (≈ 6×116 + 5×48 = 936px; keep ~28–40px right margin). Do NOT widen bars or the zone.
   - **CHOSEN motion (option b — last bar collapses):** the **2028 / 1.56 bar enters TALLER and `scaleY`-collapses DOWN to the 28px sliver** on "doesn't even matter," so the decay is an action, not a pre-drawn stub. Concretely: give `#b4-b6` a taller rendered height (~120px) and animate `scaleY: 1 → 0.23` (ending at the ~28px visual) over ~0.5s `expo.out` landing at comp 31.32 (offset 5.32) — i.e. it *drops* on "doesn't even matter" while every prior bar drew bottom-up. Keep it the single cyan. (Alternative option a — re-plot 2012→2028 for wider bars — is explicitly NOT chosen because it removes the 50→25 drama and is a layout reflow; the build agent must NOT silently substitute it.)

The 2028 timeline tick (c6b3) cross-dissolves into a descending bar chart on a shared baseline. The collapse is the visual of the spoken reward-halving.
- Eyebrow **"BLOCK REWARD · BTC ISSUANCE"** (JetBrains Mono 700, ≥32px, `#F0F0F0`) — fires **comp 26.04** (offset 0.04) — matches *"halving,"* (src 1446.34) as the chart enters `<!-- EDITORIAL label -->` *(says "BLOCK REWARD," not "HALVING," so shares no notable word with c6b3's eyebrow; "BTC ISSUANCE" avoids repeating "BLOCK" within the label → R4-clean.)*
- Rule draws (neutral `#2a2a2a`) — offset 0.20 (comp 26.2).
- Bars draw bottom-up, descending stagger, aligned to the spoken decay:
  - **2009 / 50** — offset 0.0 (comp 26.0) — chart enters on "halving"
  - **2012 / 25** — offset 0.70 (comp 26.70)
  - **2016 / 12.5** — offset 1.50 (comp 27.50) — under "becoming increasingly" (*becoming* comp 27.22, *increasingly* 27.54)
  - **2020 / 6.25** — offset 2.60 (comp 28.60)
  - **2024 / 3.125** — offset 3.80 (comp 29.80) — under "block rewards half" (**block src 1449.66 → comp 29.36**, *rewards* 1450.04 → comp 29.74, *half* 1450.50 → comp 30.20)
  - **2028 / 1.56** — offset 5.32 (comp **31.32**) — draws to a near-invisible sliver on "to a point where it doesn't even matter" (*doesn't* comp 31.32, *matter.* 31.80) — **`#00D4FF`** (the single cyan)
- Supplemental annotation **"INCREASINGLY MEANINGLESS"** (Inter 700, ~40px, left-aligned under the chart, `#F0F0F0`, **neutral `#2a2a2a` accent bar**) — fires **comp 28.16** (offset 2.16) — matches *"meaningless"* (src 1448.46) in "the halving is becoming increasingly meaningless." Real spoken line, word-synced. **This is NOT a 3-item list** — it is one short caption (see §VBF #6 for the corrected vertical-fit check).
- **Second supplemental annotation (#11 — keeps the long Mode-A hold from going visually dead) "MINERS · ENERGY · INPUT COST"** (JetBrains Mono 500, ~28px, neutral `#B6BEC6`, **NO accent bar, NO cyan**, sits as a small caption beneath/right of "INCREASINGLY MEANINGLESS" — does NOT overlap the bars) — slow `opacity 0→1` + small `y` reveal **comp 34.20** (offset 8.20, ~0.6s `power2.out`) — matches Jasper literally listing *"miners,"* (src 1454.48) → *"energy"* (src 1455.34) → *"input cost"* (src 1456.72/1457.06) in "the entire dynamic with miners, with energy pressure and input cost pressure." This is a low-key second neutral annotation (NOT a new device, NOT a list build, NOT cyan) that gives the 32–40 dwell one quiet motion tied to a spoken phrase. **R2/R8 safe:** same device (chart annotation), zero cyan, neutral muted colour. **R4 safe:** "MINERS / ENERGY / INPUT COST" shares no notable word with the eyebrow, the other annotation, or the year/value labels.
- Chart **HOLDS comp ~32–40** under Jasper's "the entire dynamic with miners, energy pressure, input cost pressure…" (src 1453.2–1457.6) — a genuine clean-graphic dwell within the Mode-A view (the chart is the visual; he narrates the consequence). The #11 second annotation reveals at comp 34.20 so the dwell has one quiet motion. `.b4-inner` exits at offset **14.2** (comp **40.2**), coincident with the Mode-A→FULL expand → no blank-left tail. (The master also Ken-Burns the *video* across the Mode-A view — that motion is on the speaker, not the graphic; #11 gives the graphic itself a beat of life.)

Cyan: the **2028 / 1.56 bar** only (lights at comp 31.32). The annotation's accent bar is `#2a2a2a` (neutral); values/years all `#F0F0F0` (no decaying opacity).
Data correctness: post-2024 reward = 3.125 BTC; next (2028) = 1.5625 ≈ 1.56 BTC. Correct.
**Retime note (on-disk → v4):** the on-disk file is authored at offsets for data-start 25.4 (eyebrow 0.64, bars 0.6/1.3/2.1/3.2/4.4/5.92, annot 2.76, exit 14.6). For v4 **data-start 26.0**, set offsets to **eyebrow 0.04, rule 0.20, bars 0.0/0.70/1.50/2.60/3.80/5.32, annotation-1 ("INCREASINGLY MEANINGLESS") 2.16, annotation-2 ("MINERS · ENERGY · INPUT COST") 8.20, `.b4-inner` exit 14.2** (→ 2028 bar comp 31.32, annot-1 comp 28.16, annot-2 comp 34.20, exit comp 40.2). Set index.html `data-start="26.0" data-duration="14.3"`.
**The ONLY additions/edits permitted in c6b4 (everything else stays):** (1) widen `.b4-chart` gap 34→48px + right pad (#7 breathing room); (2) make `#b4-b6` enter taller and `scaleY`-collapse to the 28px sliver at comp 31.32 (#7 motion); (3) add the ONE neutral `MINERS · ENERGY · INPUT COST` caption at comp 34.20 (#11). Do NOT add a third device, a stat grid, a 3-item bulleted list, a 2009 timeline echo, or any second cyan.
**R6:** the years 2009–2028 are data labels, not a clip index. PASS. **R7:** graphic present 26.0→40.2 (exit coincident with the expand) → no blank-left at entry or tail. PASS.

---

### c6b5 — `kinetic-type` (CLOSING) · FULL-FRAME · comp 40.2–46.4
**Sub-comp:** `beat-c6b5-doesnt-matter.html` — **NO CONTENT CHANGE** (on-disk file correct; only index.html `data-start` 40.4→40.2, `data-duration` 6.0→6.2; internal offsets shift +0.2).
At comp 40.2 the master GSAP expands Mode-A → FULL-FRAME (both speakers); `#bg-glow`/`#zone-rule` fade @40.0; c6b4 `.b4-inner` exits on the same instant → the left clears as the frame fills (no blank-left tail). **Continuous full-frame hold begins here and runs to clip end** (no Mode-A return — R1). The "so what" of the chart. 3 phrase lines, Inter 900 ~90px, STAY.
- **LINE 1 "I DON'T THINK"** — fires **comp 40.84** (offset 0.64) — matches *"don't"* (src 1461.14; "I" 1460.94, "think" 1461.46) — `#F0F0F0`
- **LINE 2 "IT REALLY MATTERS"** — fires **comp 41.50** (offset 1.30) — matches *"really"* (src 1461.80) / *"matters"* (src 1462.06) — `#F0F0F0`
- **LINE 3 "IF MINERS SELL OR BUY"** — fires **comp 43.46** (offset 3.26) — matches *"miners"* (src 1463.76; "selling" 1465.40, "buying." 1465.98) — `#00D4FF` (cyan payoff)
- **EXIT** — stack drifts up/out at offset **5.6** (comp 45.8) into c6b6.

Cyan: LINE 3 only. The Mode-A→FULL expand (40.2) lands **0.64s before** LINE 1's word (40.84) so the frame is settled when the kinetic fires.
**R4:** no notable word repeats across the three lines; no eyebrow. PASS. **R6:** no index. PASS.

---

### c6b6 — `kinetic-type` + `caption-neon-glow` payoff (KICKER) → clean tail · FULL-FRAME · comp 46.4–50.7
**Sub-comp:** `beat-c6b6-strong-narrative.html` — **NO CHANGE NEEDED** (on-disk file is already correct: adapted neon = brand cyan `#00D4FF`, pink/KEYWORDS branch deleted, no dim-back, Inter 900, positioned in the stack; the dim word starts at `rgba(0,212,255,0.16)` and ignites at offset 2.10).
`<!-- D4: clip ENDS on a content kinetic + clean speaker tail — NOT a name card/outro. Payoff word uses the adapted caption-neon-glow (the clip's premium-reveal device). No index. -->`
The nuance kicker, spoken immediately after c6b5 (one continuous closing movement over the single full-frame hold). Lines 1–2 standard phrase-build (Inter 900 ~100px, STAY); the **payoff line uses the adapted `caption-neon-glow`**.
- **LINE 1 "BUT IT IS STILL"** — fires **comp 46.62** (offset 0.22) — matches *"But"* (src 1466.92; "it" 1467.44, "is" 1467.64, "still" 1467.94) — `#F0F0F0`
- **LINE 2 "A VERY STRONG"** — fires **comp 48.06** (offset 1.66) — matches *"very"* (src 1468.36; "strong" 1468.50) — `#F0F0F0`
- **PAYOFF "NARRATIVE"** (`caption-neon-glow`, adapted) — fires **comp 48.48** (offset 2.08) — matches *"narrative,"* (src 1468.78; "I think." 1469.18/1469.38) — `#00D4FF` (neon glow), ignites and **STAYS lit** (no dim-back).
- **EXIT** — stack drifts up/out at offset **3.3** (comp 49.7), leaving a **clean full-frame speaker tail comp ~49.7–50.7** (~1s). Clip ends on clean speaker video (D4: no card to the end).

**caption-neon-glow (already adapted on-disk — verify these hold, do not regress):** brand cyan `#00D4FF` (component's `#00FFF0` replaced; pink `#FF0099` + KEYWORDS branch deleted), no per-word dim-back (the upstream karaoke dim is Remotion-only — removed), single payoff word positioned in the left/centre stack under LINES 1–2, Inter 900. The dim pre-ignite word is `rgba(0,212,255,0.16)` and the ignite tween at offset 2.10 locks it lit.
Cyan: the neon "NARRATIVE" only.
**R4:** "NARRATIVE" / "A VERY STRONG" / "BUT IT IS STILL" share no notable word. PASS. **R6:** no index. PASS.

---

## §8 — ONE-CYAN-PER-FRAME LEDGER (R8 — verified frame-by-frame, not just per-beat)

Scanned for any instant where two fully-lit cyan elements coexist (the v3 seam defect). Result: **never — AFTER the c6b3 retime ships.**

> **⚠ R8 seam is only clean after #4's c6b3 retime (#12).** This ledger assumes c6b3's 2028 ring fires at comp 25.68 and **fades out by ~26.1** (axis cross-dissolve at offset 11.4). **On the current on-disk files the seam is RISKY:** c6b3 fires its 2028 cyan at comp 23.4 and has NO exit tween, so at the c6b4 entry (26.0) the c6b3 cyan is still fully lit (not fading) — two cyan could momentarily coexist. Do NOT render/grade the seam (this ledger / VBF #5) against the current files. The seam check is valid ONLY after c6b3 is retimed (2028 ring → 25.68) AND given its axis fade-out (→ ~26.1).

| comp window | cyan element(s) on screen | count | note |
|---|---|---|---|
| 0.0–2.02 | (none yet) | 0 | OK |
| 2.02–~8.1 | c6b1 "IS DEAD?" | 1 | host-Q payoff — now **holds lit comp 2.02→~7.8** (stronger-hook #10), exits ~8.1 |
| ~8.1–13.16 | (none) | 0 | OK — host-Q exited, answer payoff not yet |
| 13.16–~14.4 | c6b2 "NOW IT IS" | 1 | answer payoff (full-frame); **exits by 14.4** |
| 14.4–25.68 | (none) | 0 | OK — both c6b3 baseline segments (solid 2012→2024 + dashed 2024→2028) are **neutral**; ticks 2012–2024 (CYCLE 1–4) are neutral solid dots |
| 25.68–~26.4 | c6b3 **2028 RING node** ("↓ NEXT") | 1 | the device's single cyan (hollow cyan ring, #5); **fading out by 26.1–26.4** |
| 26.0–26.4 (the c6b3→c6b4 seam) | c6b3 2028 ring (fading) — c6b4 entering elements (eyebrow, rule, bars 50/25/12.5) are **all neutral** | **1** | **the v3 seam defect is gone:** c6b4's only cyan (the 1.56 bar) does NOT light until comp 31.32 |
| 26.4–31.32 | (none) | 0 | OK — chart bars 50→3.125 are neutral; one-cyan-MAX permits zero |
| 31.32–~40.2 | c6b4 **2028 / 1.56 bar** | 1 | chart's single cyan (collapses-down per #7); the #11 "MINERS · ENERGY · INPUT COST" annotation reveals at comp 34.20 in **neutral `#B6BEC6` (no cyan)** → count stays 1 |
| 40.2–43.46 | (none) | 0 | OK |
| 43.46–~45.8 | c6b5 "IF MINERS SELL OR BUY" | 1 | close payoff; exits 45.8 |
| 45.8–48.48 | (none) | 0 | OK |
| 48.48–~49.7 | c6b6 neon "NARRATIVE" | 1 | kicker payoff; exits 49.7 |
| 49.7–50.7 | (none) | 0 | clean tail |

**Max simultaneous cyan = 1 at every instant.** Both formerly-risky seams are clean: c6b2→c6b3 (answer cyan fully exits at 14.4, ~11s before the next cyan, because the answer is now full-frame and ends before Mode-A begins) and c6b3→c6b4 (c6b4 enters neutral; its cyan bar waits until 31.32). PASS.

---

## §VBF — VERIFY-BY-FRAME (MANDATORY before any "done")

After the draft render, extract a frame at each and LOOK (`ffmpeg -ss <sec> -i renders/<file>.mp4 -frames:v 1 /tmp/f.png` → Read /tmp/f.png):

1. **comp 0.5** — opening: full-frame, BOTH speakers visible, "WOULD YOU SAY" on screen, **NO "06" or any number anywhere.** (R6 check.)
2. **comp 9.5** — c6b2 answer: still FULL-FRAME (both speakers), "THOUGHT IT WAS DEAD" on screen, **NO index, NO eyebrow chrome, NO corner marks.** (R6 + R7 — confirms the answer is full-frame, not cropped.)
2.5. **comp 5.0 — THE v3-REGRESSION CATCHER (#13, check this one FIRST).** Mid-c6b1-hold, pre-answer. Confirm the screen shows **BOTH speakers FULL-FRAME**, the title question still up (and "IS DEAD?" still lit), and **NO Mode-A crop, NO "06", NO corner marks, NO eyebrow chrome.** Rationale: the single most likely build error is retiming the beats but forgetting to MOVE the comp-3.0 shrink — which would leave the old Mode-A crop live at comp 5.0. If this frame is cropped-right or shows "06", the v3 state was not fully removed — STOP and fix index.html (shrink must be at 14.7, not 3.0) and c6b2 (no chrome) before continuing.
3. **comp 14.7** — the FULL→Mode-A switch (CANONICAL shrink instant): the c6b3 axis baseline must ALREADY be drawing in the left zone as the video crops. **There must be NO frame where the speaker is cropped-right with an empty left half.** (R7 blank-left check — the headline fix. Also sample comp 15.0 mid-shrink.)
4. **comp 18.5** — c6b3 timeline mid-build: Jasper centered/name in-frame (Mode-A, object-position 83%); axis + era ticks (CYCLE 1 / CYCLE 2…) on the left; **captions are CADENCE labels, NOT reward values**; **the four past nodes are SOLID dots and the 2024→2028 baseline tail is DASHED** (#5 — confirm the future-segment renders dashed, not solid). (R2 distinctness + framing + #5.)
5. **comp 26.2** — the c6b3→c6b4 cross-dissolve: confirm **exactly ONE cyan** on screen (c6b3's fading 2028 "↓ NEXT" **hollow ring** node); c6b4's entering eyebrow/rule/first bars are neutral. (R8 seam check. **Do NOT run this against the current on-disk files** — only valid after the c6b3 retime ships; on disk the 2028 cyan fires at comp 23.4 and is fully lit here, not fading.)
6. **comp 31.5** — c6b4 decay payoff: the 2028/1.56 bar lit cyan and visibly **collapsed-down to the sliver** (#7 motion — sample comp 31.0→31.6 to see it drop); "INCREASINGLY MEANINGLESS" annotation present; **left-zone VERTICAL FIT — eyebrow + rule + 400px chart + BOTH annotations (incl. the new #11 caption when it appears at 34.20) all within the 1080 frame, neither annotation overlaps the bars, chart is NOT edge-to-edge (gap widened to 48px), nothing overflows the bottom edge.** (Fix #2 + #7 + #11: the REAL c6b4 risk is left-zone vertical/horizontal fit — NOT a right-zone name-tag collision. Adding annot-2 grows the stack ~50px; the zone is vertically centered so it still fits, but CONFIRM by frame. No 3-item list.)
6.5. **comp 35.0 — the long-hold check (#11).** Mid 32–40 dwell: confirm the **"MINERS · ENERGY · INPUT COST" neutral caption has revealed** beneath/right of the chart in muted `#B6BEC6` (NO cyan, NOT overlapping the bars), so the Mode-A dwell is not visually dead. Confirm it adds **no second cyan** (the only cyan here is still the 1.56 bar).
7. **comp 40.2** — the Mode-A→FULL switch (CANONICAL expand instant): confirm full-frame (both speakers), no blank-left tail, chart fully cleared. (R7 + R1. Also sample comp 40.5.)
8. **comp 48.6** — c6b6 neon payoff: "NARRATIVE" lit in brand cyan `#00D4FF` (NOT pink, NOT teal `#00FFF0`); both speakers full-frame. Also glance at **comp 48.3** to confirm no dim-cyan ghost word renders before its ignite tween (caption-neon-glow hidden-state).
9. **comp 50.3** — clean tail: both speakers, no card/outro, no lingering text. (D4.)

---

## VERIFICATION (graded against `_QA-CHECKLIST.md`)

- **§1 R7 NO blank-left Mode-A (the headline v4 fix):** the Mode-A block (14.7–40.2) contains ONLY the two chart graphics; a graphic fills the left zone its ENTIRE duration (axis appears comp 14.9 during the shrink; chart exits comp 40.2 coincident with the expand; the two charts overlap 26.0–26.4). The **answer kinetic moved to full-frame**, so there is no kinetic-in-Mode-A to leave a blank left. No cropped-speaker-with-empty-left frame exists. The occupancy table proves it. ✓
- **§1 R6 NO index/clip-number on screen:** the rendered "06" (`b2-idx`) is **deleted from c6b2**; no beat renders any internal clip/beat number. Years (2009–2028) are data labels; eyebrows are editorial labels (permitted). ✓
- **§1 R1 view-discipline:** `FULL 0–14.7 → MODE-A 14.7–40.2 → FULL 40.2–50.7`. Dwell 14.7/25.5/10.5 (none <8s). No A-B-A within 12s (FULL not re-entered for 25.5s). Consecutive graphics (c6b3/c6b4) grouped in ONE Mode-A view; consecutive kinetics grouped in the full-frame blocks. ✓
- **§2 R2 variety:** distinct primary devices = halving **timeline** (cadence/WHEN, captions CYCLE 1…4/NEXT) + `nyt-graph` **decay chart** (reward/HOW-MUCH, bars 50→1.56) — **disjoint data series** (v3's reward-ladder-timeline preview is fixed); ≤2 kinetic in a row (max 2 each end, broken by the two chart devices); chart beats init from `nyt-graph`; neon-glow for the payoff. ✓
- **§3 dialog-match:** opens on the real spoken host question (1420.42–1422.52), word-synced 0.12/0.94/2.02; first text comp 0.12. ✓
- **§4 R5 opening coherence:** "WOULD YOU SAY / THE FOUR-YEAR CYCLE / IS DEAD?" = a complete question; payoff "IS DEAD?" is a real phrase. ✓
- **§5 framing:** `object-position: 83% center`, Mode-A `{1229,108,614,864}`; full-frame beats show both speakers; verify-by-frame mandated in §VBF (incl. the R6/R7/R8 and corrected c6b4 vertical-fit checks). ✓
- **§6 R3 jargon:** window 1420.30–1471.00 has **no** jargon-table traps (no DePIN/perps/grunt/take-rate/meme-coin/insatiable; "spivvy" at src 1394.06 is OUTSIDE the window). On-screen terms = Bitcoin, halving, block reward, BTC, miners, narrative, CYCLE — all plain/correct. Name lower-third "Jasper De Maere / Wintermute" spelled exactly. ✓
- **§7 R4 dup words:** no notable word repeats across two elements of any beat, nor within an element. c6b3 internal "HALVING" dup fixed (2028 caption "↓ NEXT"). Eyebrows distinct across beats ("HALVING CADENCE · EVERY 4 YEARS" / "BLOCK REWARD · BTC ISSUANCE"); opener's "FOUR-YEAR CYCLE" not echoed (c6b2 has no eyebrow now). ✓
- **§8 hard rules:** z-index:3 lists all 6 ids; **exactly one `#00D4FF` per FRAME** (full ledger in §8 — clean AFTER the c6b3 retime; c6b3's single cyan is the 2028 hollow RING node, c6b3→c6b4 carries one cyan because c6b4 enters neutral; the #5 dashed baseline segment and the #11 "MINERS · ENERGY · INPUT COST" caption are both NEUTRAL). No backdrop-filter blur; no grain; eyebrows Inter 700 ≥32px `#F0F0F0`; muted text `#B6BEC6` (no `#888888`); no intro/outro card; ends on a content beat + clean tail; halving years absolute (allowed); phrases STAY (no dim); neon-glow adapted (brand cyan, no dim-back). ✓
- **§9 verify-by-frame:** mandated at 11 timestamps in §VBF (incl. #2.5 the v3-regression catcher at comp 5.0 and #6.5 the long-hold check at comp 35.0), covering R6 (no "06"), R7 (no blank-left at the 14.7 shrink), R8 (one cyan at the 26.2 seam — only valid after the c6b3 retime), the #5 hollow-ring/dashed read, the #7 collapsing-bar + breathing-room, and the corrected c6b4 left-zone-vertical-fit check. ✓

**Build Manifest Row:** `clip_6 | clip-6-four-year-cycle | 1420.30 | 1471.00 | kinetic-type,timeline,nyt-graph,caption-neon-glow | 6 beats | obj-pos 83% | views FULL→MODEA→FULL (14.7/25.5/10.5) | R6 index removed | R7 Mode-A graphic-filled entire block (no blank-left) | timeline=cadence, chart=decay`

---

## CHANGE SUMMARY FOR THE BUILD AGENT (the exact edits to ship v4 from the on-disk v3 files)

> **BUILD-STATE WARNING:** the on-disk files are at v3 and the existing HQ render (`renders/clip-6-four-year-cycle-HQ.mp4`, 09:58) is the **rejected v3 render — DELETE it first** (`rm renders/clip-6-four-year-cycle-HQ.mp4`). `beat-c6b2` still renders `#b2-idx` "06" (line 28) and is in Mode-A; `beat-c6b3` still fires the 2028 tick at offset 9.4, has reward-ladder captions, a solid cyan node, and no exit tween; `beat-c6b4` uses v3 offsets (data-start 25.4); `index.html` still shrinks to Mode-A at comp 3.0 with c6b2 `data-start="3.0"`. This table is the work order; the spec does NOT equal the current files. Apply every row, then render a draft and run §VBF before claiming done. **Lock to the canonical pair 14.7 / 40.2 — there is no 14.0/14.95/40.4 in v4.**

| file | change |
|---|---|
| `compositions/beat-c6b1-host-cycle-dead.html` | **NO content change; ONE timing change (#10).** The 3 lines stay at 0.12 / 0.94 / 2.02. **MOVE the on-disk stack-exit tween from offset 2.74 → 7.8** so "IS DEAD?" holds lit ~5.8s and clears just before c6b2. (On-disk it exits at 2.74 — too fast.) |
| `compositions/beat-c6b2-was-dead-it-is.html` | **REWRITE as a FULL-FRAME kinetic (R6 + R7).** DELETE `#b2-idx` ("06") + its CSS + GSAP; DELETE `#b2-eye`, `#b2-rule`, and the four `.b2-reg` corner marks (+ their CSS/GSAP). Build `.b2-backdrop` (left-zone dark gradient, mirror c6b1) + `.b2-words`: LINE 1 "THOUGHT IT WAS DEAD" @ offset **0.52**, LINE 2 cyan "NOW IT IS" @ offset **4.66**, stack exit @ offset **5.6**. Set `data-duration="6.7"`. (2 phrase lines — do NOT add a third.) |
| `compositions/beat-c6b3-halving-timeline.html` | **EDIT (captions + retime + #5 stronger graphic).** (a) Change the 5 captions from the reward ladder to **CYCLE 1 / CYCLE 2 / CYCLE 3 / CYCLE 4 / ↓ NEXT** (fixes #3 + #4). (b) Keep the 5 ticks/years (2012/2016/2020/2024/2028) — do NOT add a 2009 tick. (c) **#5:** make the 2028 node a HOLLOW CYAN RING (`.b3-node-accent` → `background:transparent; border:3px solid #00d4ff`, keep glow); split `.b3-base` so 2012→2024 is SOLID neutral `#2a2a2a` and **2024→2028 is a DASHED neutral extension** (`border-top:3px dashed #2a2a2a`). Both baseline segments stay neutral — the ring is the only cyan. (d) Retime: eyebrow **0.52**, baseline **0.2**, ticks **2.54 / 3.48 / 4.9 / 6.76 / 10.98**; **add an axis fade-out at offset 11.4** (on-disk has none). Set `data-duration="11.7"`. Delete stale 11.68/9.4 comments. |
| `compositions/beat-c6b4-halving-decay.html` | **RETIME + 3 targeted clarity edits (#7 + #11); values/colours unchanged.** Offsets: eyebrow **0.04**, rule **0.20**, bars **0.0 / 0.70 / 1.50 / 2.60 / 3.80 / 5.32**, annotation-1 "INCREASINGLY MEANINGLESS" **2.16**, `.b4-inner` exit **14.2**. **#7 breathing room:** `.b4-chart` `gap: 34px → 48px` + right pad (not edge-to-edge). **#7 motion:** `#b4-b6` enters TALLER (~120px) and `scaleY 1→0.23`-collapses to the 28px sliver landing comp 31.32 (the decay is an action). **#11:** add ONE neutral caption **"MINERS · ENERGY · INPUT COST"** (JetBrains Mono 500 ~28px, `#B6BEC6`, no accent bar, no cyan, beneath/right of annotation-1, not overlapping bars), slow opacity+y reveal at offset **8.20** (comp 34.20). Confirm eyebrow/rule/first-bars neutral; only the 1.56 bar is cyan; both annotations neutral. Do NOT add a third device, a stat grid, or a 3-item list. |
| `compositions/beat-c6b5-doesnt-matter.html` | **NO content change.** Offsets shift +0.2 with the new data-start (LINE fire-times stay comp 40.84 / 41.50 / 43.46). |
| `compositions/beat-c6b6-strong-narrative.html` | **NO change** (already correct: adapted neon = brand cyan, no dim-back, Inter 900, single word). Do not regress the neon adaptation. |
| `index.html` | **Beat windows + tracks:** `c6b1 0.0/8.5` · `c6b2 8.5/6.7` (track 3) · `c6b3 14.7/11.7` (**track 4**) · `c6b4 26.0/14.3` (**track 3**) · `c6b5 40.2/6.2` · `c6b6 46.4/4.3`. **Master GSAP view-timeline:** **REMOVE the comp-3.0 shrink and its glow/rule/Ken-Burns at 3.x**; FULL→Mode-A shrink at **comp 14.7** (0.5s expo.inOut), `#bg-glow` @14.7, `#zone-rule` draw @14.9; Mode-A→FULL expand at **comp 40.2** (0.4s), glow/rule fade @40.0; re-anchor the Ken-Burns to start at 14.9 (not 3.5). Update the stale c6b1–c6b5 `data-start`/comment ranges (they still say 3.0/14.0/25.4/40.4). Confirm the z-index:3 rule lists all 6 ids. |

**After building: DELETE the stale 09:58 HQ render, render a fresh draft, run §VBF (11 frames — start with #2.5 at comp 5.0), and confirm R6 (no "06"), R7 (no blank-left at comp 14.7), and R8 (one cyan at comp 26.2, only valid post-retime) BEFORE claiming done or re-rendering HQ.**
