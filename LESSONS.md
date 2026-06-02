# Podcast → Video Production — Lessons & the Repeatable Clip Workflow

Institutional memory for the **Anndy Lian / Volmex "Web4"** episode: how to *cut* the podcast, *design* graphics, *render* them, and — most importantly — **the repeatable workflow that catches issues before the expensive render** so we stop repeating the mistakes we made all week (blank zones, hollow boxes, text over faces, mis-synced/garbled text, view jitter).

Read **THE META-LESSON** and **THE CLIP WORKFLOW** before touching any clip. The rest is the *why* behind each gate.

---

## THE META-LESSON (the one that explains almost every rejection)

> **We kept validating an abstraction instead of the artifact the user sees.** The plan, the EDL, a convenient mid-beat frame, a symptom-level patch, or a self-written gate we *wanted* to pass — none of those is the rendered pixels across the whole timeline. Every blank box, empty card, and off-position title traces to this.

Two corollaries, both earned the hard way:

1. **A guard that lives only as prose is not a guard.** "Remember to check X" fails under pressure exactly when it matters. Convert every taste rule into a *mechanical* check or it will recur. The gate set only grows (monotonic) — each new rejection becomes a permanent check.
2. **Gates are necessary, not sufficient.** Every gate we have is false-pass-prone (a glowing *empty* card pegs a luminance check; a flip-flop is invisible to a content check). So: exhaust cheap mechanical gates first, render once, then **human eyes on every flagged window** — and *show the frames*, don't assert "green."

---

## THE CLIP WORKFLOW (run this, in order, every time)

**Principle: cheapest-catch-first.** ~32 of our ~36 known failures are catchable with *instant, no-render* checks. Render is the one expensive step — do it **once, in HQ, on the affected SEGMENT** (never a blind full render, never a draft — draft's 2 fps sampling gave false greens). Only after the mechanical gates are green do human eyes go on the flagged windows.

| # | Stage | What you do | Gate to advance | Mechanical? | Before render? |
|---|-------|-------------|-----------------|-------------|----------------|
| 1 | **INTAKE** | Gather episode-once inputs: `clipN-words.txt` (word table, `comp = src − src_in`), source **fps** (`ffprobe`; this podcast = 24, never assume 30), intro location, list of hand-built comps to restyle if DESIGN changed | Inputs exist & written down | input prep | ✅ |
| 2 | **LAYOUT-PROBE** | `ffmpeg` one real source frame and **look at it**. Confirm framing class (host-left/guest-right side-by-side here) + guest-center target | Human confirms layout from the frame, in writing | extract=auto, confirm=human | ✅ |
| 3 | **EDL / PLAN** | Write the beat plan: **view-timeline** (grouped, R1), word-locked fire-times read off the table (never computed), distinct device (R2), open on a spoken line, jargon mapped through `_JARGON.md`, no dup words, coherent open, no chapter/index cards | Grade against `_QA-CHECKLIST.md` §1–8 | mostly **prose/human** (see backlog) | ✅ |
| 4 | **BUILD** | Author compositions from the EDL. **Write-then-replace, never destructive `rm`** before write. Every overlay id in the `z-index:3` rule. Container enters *with* its content, never before | Self-check: z-index complete; no shell-before-rows | prose | ✅ |
| 5 | **LINT** | `npx hyperframes lint` | **0 errors AND 0 font-warnings** (use `--json` + fail on warnings — fonts: Inter embedded; Georgia/Garamond/Fraunces warn) | ✅ instant | ✅ |
| 6 | **STATIC GATE — blank-left** | `python3 timing/check-edl.py <clip>` | PASS (no predicted blank-left; no late-firing Mode-A beat) | ✅ instant | ✅ |
| 7 | **STATIC GATE — empty-box + greps** | `python3 timing/check-content.py <clip>` + jargon/index/dup greps | PASS (no empty container, no sparse hold) + greps clean | ✅ instant | ✅ |
| 8 | **PRE-RENDER** | Get **consent for render scope** (segment vs full); `_PREV.mp4` backup if overwriting an approved final; kill `chrome-headless-shell` + `rm work-*`; concurrency ≤ 2 HQ jobs | Consent + backup + hygiene done | prose (→ make structural) | ✅ |
| 9 | **RENDER** | **ONE HQ pass** of the affected SEGMENT (~28 s composite) or single clip. Not draft, not full | Completes without Chrome crash; output is the newest `renders/*-HQ.mp4` | — | render |
| 10 | **RENDER GATE — pixels** | `python3 timing/check-render.py <clip>` on the HQ | PASS (coverage + lint + z-index + index + jargon), reading the **newest** mp4 | ✅ pixels | after |
| 11 | **HUMAN FRAME-VERIFY** | `ffmpeg` a frame at **every Mode-A beat-START** + every previously-flagged window; *look at each*; paste them to the user | Human approves the actual frames | **human (mandatory)** | after |
| 12 | **SHIP** | Full render only if asked (chunked, see §C); delete `work-*`/`_PREV.mp4` after verify; renders gitignored; **commit only when asked** | Re-passes check-render; clean tree | mixed | after |

**What the mechanical gates can and CANNOT see** (never trust a green blindly):

- `check-edl.py` (instant) — predicts blank-left from the view-timeline vs each beat's first-content time. **Blind to:** content that *exits early* (clip-4: graphic gone by ~3 s of a 7.5 s host window → blank, gate says covered); a fragile view-parser that only understands `toModeA/toFull` or literal `width 1920/614/768`/`left 0/>1000` (a Mode-A done via `transform`/`{x:0}` is invisible → whole clip read as full-frame → false PASS).
- `check-content.py` (instant) — separates shell (card/glass/eyebrow/rule) from content; flags a container on screen >2.5 s before its content, or an eyebrow-only hold >5 s. **Blind to:** JS/`innerHTML`/`<canvas>`-built content (no parseable entrance → beat *skipped*, a genuinely empty JS card passes); selector-name misfiling (a `.box` holding real text, or content named `.q`); same fragile view-parser.
- `check-render.py` (after HQ) — the authoritative pixel check: blank-left coverage (left 1120 px, YMAX<100 >1.5 s), lint, z-index, no `0N` index, jargon list. **Blind to:** *semantics* — a glowing **empty** card passes (luminance ≠ content); **wrong/mis-synced/seam-framed** content is all bright and passes; 2 fps sampling floor; jargon is a *frozen list*, not `_JARGON.md`. → This is why **S11 human eyes are mandatory**, not optional.

**Is this optimized?** Yes for *cost order* (every automatable issue is pushed to an instant pre-render gate; render happens once). It is **not yet complete** — several high-value catches are still prose/human (S3, S4, S8) or missing as code. Those are the backlog below; closing them moves catches left (cheaper) and is how revisions actually reach zero.

---

## GATE-HARDENING BACKLOG (prose → code; do these to catch more *before* render)

Prioritized by value × how often it bit us. Each turns a prose/human guard into a mechanical pre-render gate (the monotonic loop).

1. **EXIT model in `check-edl`/`check-content`** — track last-content-offset per beat; flag content that fades before its Mode-A window ends. Closes blank-left **cause #3** (clip-4), the one no static gate catches today.
2. **`check-content` fail-CLOSED on unparseable content** — if a beat builds rows via JS/`innerHTML`/`<canvas>`, don't silently skip it; flag for mandatory frame-verify. Closes the empty-JS-card hole.
3. **`check-sync.py`** — compare each kinetic line's authored fire-time to `clipN-words.txt`; FAIL if off by > ~0.5 s. **No gate reads the word table today** → word-sync drift is currently uncaught by code.
4. **Harden the shared view-parser** (or build the generator that *emits* Mode-A to tile graphic-beat spans) — kills the parser false-negatives + makes blank-left structurally impossible rather than checked.
5. **`check-render` sampling** — raise to ~10 fps and measure *true* blank duration (the clip-1 borderline gap that draft missed was a temporal-sampling problem, not draft-vs-HQ).
6. **Jargon reads `_JARGON.md`** — replace the frozen regex so new mis-hearings + brand spellings (Wintermute/Paradex/Morpho/zkML) are covered and can't drift.
7. **Small static greps** (instant, high ROI): `check-dup.py` (duplicate notable words across a beat's slots — *claimed but doesn't exist*), `check-views.py` (R1 flip-flop / <8 s segment), `check-selectors.py` (every GSAP target id/class actually resolves — catches the `#br-title`-vs-`.br-title` exit that left text on the face), grain/`backdrop-filter` grep, `check-variety.py` (≤2 kinetic in a row).
8. **Make hygiene & recovery structural, not prose** — backup-to-`_PREV.mp4` and orphan-chrome/`work-*` reap *inside* the render scripts; `build_full.py` writes-then-replaces (never `glob().unlink()` in place).

---

## FAILURE → GUARD MATRIX (every issue we hit, where it's caught, and how)

`M` = mechanical gate exists · `P` = prose/human rule · `S` = structural (made impossible) · `TODO` = backlog above.

| Failure | Root cause (not symptom) | Guard | Caught at | Status |
|---|---|---|---|---|
| Blank-left Mode-A (late-fire / inter-beat gap / early-exit) | Verified the plan, not the rendered pixels; timeline & beats hand-authored separately so Mode-A never guaranteed to tile graphics | check-edl (predict) + check-render (pixels) + R7 frame-at-start; **exit case = TODO #1** | S6/S10 | M (partial) |
| Empty / hollow box (bright card, no rows) | Luminance gate reads a glowing border as "filled"; card shell mounted before its content | check-content (shell-vs-content) + rule: container never emptier than a frame later | S7 | M |
| Text over the speaker's face / wrong zone | GSAP exit targeted a selector that didn't match (`#br-title` vs `.br-title`); overlays placed without respecting side-by-side layout | lower-third-only rule + design-QA agent; **selector-resolution check = TODO #7** | S11 | P |
| View flip-flopping (A-B-A < 12 s) | No planned view-timeline; view chosen per-beat | R1 + EDL view-timeline table; **check-views = TODO #7** | S3 | P |
| Wrong assumed source layout | Assumed framing instead of looking at a real frame | LAYOUT-PROBE: extract + view a frame first | S2 | P (web4) |
| Jargon mis-spellings on screen | Treated transcript as ground truth for *spelling* (it's only *timing*) | `_JARGON.md` + check-render grep (frozen list; **TODO #6**) | S7/S10 | M (partial) |
| Duplicate words across a beat's slots | No dedup across text slots | R4; **check-dup = TODO #7 (claimed, not built)** | S3 | P |
| Word-sync drift (3–47 s off) | Computed timing live / topic-level beats; `comp = src − src_in` | Word table is ground truth; read fire-times, never compute; **check-sync = TODO #3** | S3 | P |
| Two-speaker duplication (swiss) | Two independent layers can't be frame-synced; base live video exposed | **Structural:** full-frame paper UNDER, speaker window composited ON TOP; luma-floor ≥210 check (TODO) | S (build) | S (web4) |
| Embedded `<video>` in transparent sub-comp | Headless Chrome renders it blank + "Target closed" crash | No `<video>` in sub-comps; ffmpeg places the window via crop+overlay; **grep = TODO** | build | S (web4) |
| Render-format gotchas | WebM alpha opaque; `-map 0:v` bypasses filter; 480p proxy off-canvas | MOV `yuva444p12le`/ProRes 4444; name pad `[o]` + `-map "[o]"`; normalize to 1920×1080 | build | P (web4) |
| Full render without asking (8.4 GB) | Launched a 70k-frame blind render | Ask first; render SEGMENTS + composite; delete artifacts | S8 | P → make structural |
| Full render OOMs Chrome | Single 70k-frame continuous render | Chunk ~485 s on bare seconds, retry 6→4→2→1 workers, resume | S12 | S (web4) |
| Draft passed, HQ failed | 2 fps temporal sampling hid a sub-1.5 s gap (resolution, not draft) | Gate the HQ; **raise fps + true-duration = TODO #5** | S10 | M (partial) |
| Committed mp4s (push blocked) | Videos committed before `*.mp4` gitignore existed | `renders/` + `*.mp4`/`*.mov` gitignored root+web4; commit on request only | S8/S12 | S |
| No backup before overwrite | Re-render overwrote the approved final | `_PREV.mp4` before overwrite (delete after verify); **make it a render-script side-effect = TODO #8** | S8 | P |
| Destructive `rm` corrupted a clip | `build_full.py` rm-before-write | Write-then-replace; backup before destructive edits; **build-script fix = TODO #8** | S4 | P |
| Font warnings (Garamond/Fraunces) | Non-embedded fonts; lint warnings not failed on | Inter embedded; **lint `--json` fail-on-warning = backlog** | S5 | M (partial) |
| Chapter/title/index cards | Anti-pattern carried from a template | NOCHROME + R6; **check-device = TODO** | S3 | P |
| z-index overlay behind video | Beat id missing from the `z-index:3` rule | check-render z-index (broaden to all overlay ids = backlog) | S10 | M |
| Shared logic drift | Window filter duplicated across scripts | Single source `swiss_overlay.py` imported by both | build | S (web4) |
| Dense graphics — bare gaps | Editorial filter is what to CUT, not whether to graphic what remains | A beat every ~15–30 s; **check-density = backlog** | S3 | P |
| Hand-built comps not restyled on palette change | `build_full.py` only regenerates generated beats | Restyle every static comp on a DESIGN change; **check-palette = backlog** | S1 | P (web4) |
| Template monotony ("all look like clip-2") | Everything kinetic; R2 never became code | R2 ≤2 kinetic in a row + distinct device; **check-variety = backlog** | S3 | P |
| Framing on the seam (50%) | Assumed object-position values | Verify framing by frame; guest-center ~80–85%; **check-framing = backlog** | S11 | P |
| **(cut pipeline)** lag/retake/dupe joins; intro recorded last; hook not matching dialog; Volume-keyframe = 0 (silence); source-fps 1-frame gaps | Validated `content_edit.json` (spec), not the exported video; hardcoded 30 fps | `content_qa.py` re-derives edited transcript; `diff_edits.py` re-transcribes the **export**; use source fps, cursor `round(out*fps)−round(in*fps)`; audio crossfade 4 frames; never Volume 0 | cut-pipeline QA | M/P (separate pipeline) |

---

## LESSONS BY AREA (the *why* behind the gates)

### A. Editing the podcast (the cut)
**Reproducible & automated, never hand-tuned** — the deliverable is a Premiere sequence that opens already edited; every cut comes from transcript + rules. Hand-tuning was explicitly rejected.

**What to cut:** keep what advances the **thesis** (Web4, blockchain-governance failures → centralization, AI as impartial fairness, the book's *arguments*). Cut: lag/connection trouble + the interrupted take; re-taken takes (keep the clean redo); off-topic tangents (AI-tool name-drops, crypto-personality gossip, trading detours, book *backstory* vs *content*, content-creation meta-talk); pre/post-show chit-chat; tight-trim circling speech. Encoded in `podcast-pipeline/exclusion_rules.yaml` — **the exclusion list is institutional memory**: every "remove X" becomes a permanent rule.

**QA verifies the OUTPUT, not the spec** (the lesson that started it all): `content_qa.py` re-derives the edited transcript and reviews it; `diff_edits.py` re-transcribes the **exported video** and diffs vs original to learn what was kept/cut → feeds the exclusion list. Learn from the user's manual edits via FCP XML export or re-transcription (source-time-anchored, survives reordering).

**Premiere bridge must-knows:** use the **SOURCE fps** (24 here, not 30) — the sequence inherits it; a 30-fps grid → off-boundary → 1-frame gaps. `TPFRAME = round(254016000000/fps)`; advance cursor by `round(out*fps) − round(in*fps)`, not `round((out−in)*fps)`. Transitions DO work programmatically (`getAudioTransitionByName("Constant Power")` + `clip.addTransition`); **audio crossfades = 4 frames**, hard cuts on video. **Never set a Volume Level keyframe to 0** (linear amplitude, unity = 0.177; 0 = −∞ silence). QA fails on any Volume keyframe; every V1 junction gap must == 0. Caveats: `ANTHROPIC_API_KEY` isn't in the agent sandbox (Stage-2 detection + LLM QA need the user's env); intros are often recorded **last** — search the last 20% for "Hi, I'm [name]".

### B. Creating graphics (style + composition)
**Style = CINEMATIC PREMIUM** (current light-Swiss variant noted where it differs). Deep charcoal `#121318` (or light-Swiss paper `#F4F2EC`), **ONE** accent (electric-cyan `#1FE3C6` / `#00D4FF` dark, or coral `#CC785C` light), real depth (glow, light sweeps, vignette), bold **Inter** 800–900. **Rejected — don't go back:** cream/ivory "Anthropic cloud"; flat Swiss; liquid-glass-everywhere; flat opaque cards; **chapter-title cards**; film grain; backdrop-blur over video; red kinetic text; on-screen clip numbers.

**THE RULE — text appears as the person says it.** Every line/bullet/stat reveals synced to the word timestamps, never front-loaded; each line a short distilled summary.

**Use supporting graphics with a live PiP of the current speaker** (Volmex reference), NOT chapter cards: bullet key-point lists (eyebrow + accent markers + 2–3 per-phrase bullets), flowcharts (`flowchart` catalog block), stat count-ups (glowing numerals; strip SFX + `back.out` eases), liquid-glass reference cards (inset rounded accent bar, **not** `border-left`). Composition: heavy graphics in the first 2 min then one per strong statement; supplemental overlays MUST be **lower-third** (`y≥740`), content-only, off the face (side-by-side leaves no other safe zone); mask the burned-in name tag.

### C. Rendering (HyperFrames + ffmpeg)
- **Two independent layers can't be frame-synced — make overlap structurally impossible.** Swiss "two speakers" = 1-frame desync between the ffmpeg window and the HyperFrames paper. Fix: full-frame paper UNDER, speaker window composited ON TOP, so the window only ever slides over paper. Single source for the filter (`swiss_overlay.py`).
- **No embedded `<video>` in transparent sub-comps** — renders blank + "Target closed" crashes. Let ffmpeg place the window via `crop` + `overlay`.
- **Format gotchas:** WebM alpha is broken (opaque) → MOV `yuva444p12le` / **ProRes 4444** for transparent overlays and Premiere editing (not sparse-keyframe H.264). `-map 0:v` silently bypasses a `filter_complex` → name the pad `[o]` and `-map "[o]"`. Normalize source to 1920×1080 in-filter (a 480p proxy put windows off-canvas).
- **The full render OOMs Chrome — chunk it:** ~485 s chunks on bare seconds (no beat at the seam), per-chunk retry 6→4→2→1 workers, resume (skip existing), concat `-c copy`.
- **A 1080p render is ~5 min per 60 s → ~5 h for the full 48.6-min file.** Confirm the look on a short test/opening before the full overnight job.

### D. Process & workflow discipline
- **Verify visually, iterate on frames; show evidence, don't assert.** The two-Anndy frame and the title-over-face bug were both found by extracting the actual frame, not by reasoning.
- **Verify on a SHORT test before any long/expensive op.** Every accepted fix was first proven on a ~28 s composite, frame-stepped + luma-gated, *then* committed to the full render.
- **A backup before a destructive overwrite is cheap insurance** (`_PREV.mp4`, deleted after verify).
- **Read-only sub-agents work; build sub-agents are blocked in plan mode** (research only). Harvest research, build directly. Don't waste spawns rediscovering this.
- **Decompose synthesis per-item** — one agent emitting a huge multi-part doc truncates to the tail. Pipeline one item per sub-agent; recover lost output from the workflow journal.
- **The user reviews iteratively and precisely** — small concrete corrections. Build the smallest thing that proves a direction, render it, confirm, then scale.

---

## Files & companion memory
- **Cut:** `podcast-pipeline/` (`exclusion_rules.yaml`, `content_qa.py`, `diff_edits.py`, `podcast_content_edit.py`).
- **Graphics + gates:** `compositions/restream-may18/` — `PROCESS.md` (pixel-gate SOP), `DESIGN.md`, `timing/check-edl.py` · `check-content.py` · `check-render.py` · `_QA-CHECKLIST.md` · `_JARGON.md`; web4 project at `hyperframes/web4-first5/` (`design.md`, `swiss_overlay.py`, `render_chunks.py`).
- **Memory (cross-session):** podcast-overlay-style, premiere-clip-placement-fps, premiere-audio-transitions, podcast-intro-detection, subagents-blocked-in-plan-mode, gate-rendered-pixels-not-plan, empty-box-not-just-blank, view-matches-content-no-blank-left, view-switching-no-flipflop, word-table-ground-truth, verify-actual-layout-first, swiss-window-no-duplication, no-full-renders-without-asking, use-template-variety-not-just-kinetic, transcript-jargon-glossary, no-duplicate-words-in-beat, no-grain-no-blur, dense-graphics-support, restyle-hand-built-comps, remotion-editing-codec, workflow-large-synthesis-truncates.
