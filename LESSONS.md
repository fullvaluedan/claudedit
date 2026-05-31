# Podcast → HyperFrames Production — Lessons & Expectations

Hard-won knowledge from producing the **Anndy Lian / Volmex "Web4"** episode: how to *edit* the podcast and how to *create graphics* with HyperFrames. Read this before touching either pipeline.

---

## Part 1 — Editing the podcast (the cut)

**Principle: reproducible & automated, never hand-tuned.** The deliverable is a Premiere sequence that opens already edited. Every cut decision should come from the transcript + rules, not a person nudging clips. Hand-tuning was explicitly rejected.

### What to cut (the editorial standard)
Keep anything that advances the **thesis** — Web4, blockchain-governance failures (money & greed → centralization), AI as an impartial fairness mechanism, the book's arguments. Cut everything else, even when it sounds substantive:
- **Lag / connection trouble** AND the surrounding interrupted take ("we lost you", "how's your internet", "can you repeat the last 30 seconds", "or restart that").
- **Re-taken takes** — keep the clean re-done version, cut the interrupted one + the banter.
- **Off-topic tangents:** specific AI-tool name-drops (Mini Max, Manus, Z.AI), crypto-personality gossip (SBF, Justin Sun, CZ anecdotes), trading-instrument detours, book *backstory* (when/how it was written) vs book *content*, content-creation meta-talk ("my X algorithm").
- **Pre/post-show** chit-chat and recording logistics ("are we recording", "catch you next time").
- **Tight trimming** of repetitive/circling speech ("I mean, I think, I think, you know…") — sounds like real speech, adds nothing.

These are encoded in `podcast-pipeline/exclusion_rules.yaml` (9 categories, patterns + confidence). **The exclusion list is institutional memory** — every time the user says "remove X", that pattern becomes a permanent rule so the same thing is caught next episode.

### QA verifies the OUTPUT, not the spec
The lesson that started it all: validating `content_edit.json` (the spec) is not enough — you must verify what actually got produced.
- `content_qa.py` re-derives the edited transcript and has Claude review it for leftover lag/retake, duplicated takes, abrupt joins.
- `diff_edits.py` re-transcribes the **exported video** and diffs it against the original to learn exactly what the editor kept/cut → feeds the exclusion list.
- **Learn from the user's manual edits:** export FCP XML from Premiere (File → Export → Final Cut Pro XML) or re-transcribe the export. It's source-time-anchored, so it survives heavy reordering — map each clip's source in/out onto the Whisper transcript to reconstruct the new order and diff it.

### Technical must-knows (Premiere bridge)
- **Use the SOURCE frame rate, never hardcode 30.** This podcast is **24fps**. The sequence inherits the source fps; snapping clip positions to a 30fps grid puts them off the real frame boundaries → Premiere re-snaps → **1-frame gaps**. Detect via `ffprobe r_frame_rate`; `TPFRAME = round(254016000000/fps)`.
- **Advance the cursor by `round(out*fps) - round(in*fps)`**, not `round((out-in)*fps)` — they differ by a frame at boundaries.
- **Transitions DO work programmatically** — the QE transition *list* is empty, but `getAudioTransitionByName("Constant Power")` + `clip.addTransition(obj, false, durFrames)` adds real crossfades. **Audio crossfades = 4 frames** (12 was too long). **No video dissolves** (hard cuts on video).
- **Never set Volume Level keyframes to 0** (= silence/−∞; it's linear amplitude, unity = 0.17782). This caused "no audio on the first clips". The QA gate now fails on any Volume keyframe.
- Word-boundary snapping puts every cut in a silent inter-word gap. QA checks every V1 junction gap == 0.

### Caveats
- `ANTHROPIC_API_KEY` is **not** available in the agent sandbox — the Claude-driven detection (Stage 2) and the LLM QA review need it in the user's env to run.
- Intros are often recorded **last** (end of the raw file). Search the last 20% for "Hi, I'm [name]".

---

## Part 2 — Creating graphics with HyperFrames

**Style = CINEMATIC PREMIUM.** Deep charcoal `#121318`, ONE electric-cyan accent `#1FE3C6`, real depth (glows, light sweeps, vignette), bold **Inter** (800–900). Dramatic, expensive, like a high-end tech product film.

**Rejected along the way (don't go back):** cream/ivory "Anthropic cloud" look; flat Swiss grid; generic liquid-glass-everywhere; flat opaque card backgrounds; **chapter-title cards** ("01 / AI is the bigger market").

### THE RULE — text appears as the person says it
Every line / bullet / stat / keyword reveals **synced to the transcript word timestamps**, never front-loaded. Keep each line a **short distilled summary**. (Book stats: `#1 New Release` at 0:35, `#11 Bestseller` at 0:38 — each when spoken. Bullet lists reveal one line per phrase.)

### Use supporting graphics, NOT chapter cards
A library of dark + cyan + glow beats, each with a **live PiP of the current speaker on the right** (the Volmex reference style):
- **Bullet key-point lists** — topic eyebrow + cyan bar markers + 2–3 short bullets, per-phrase.
- **Flowcharts** — relationships/arguments (centralized → money/greed → AI). Catalog `flowchart`.
- **Stat count-ups** — glowing cyan numerals (`apple-money-count` technique; strip its SFX-on-track-9 + `back.out` eases).
- **Liquid-glass reference cards** — for product/name-drops (NotebookLM). Frosted backdrop-blur DOES render. Use an **inset rounded accent bar, NOT `border-left`** (which bends into rounded corners = "hard corners"); larger radius; soft 1px border.

### Composition rules that earned their place
- **Heavy graphics in the first 2 minutes**, then a supporting graphic on each strong statement.
- **Book intro = split:** book + WEB4 title left, **live PiP right**; live footage shows *through* a semi-transparent scrim (not flat charcoal); duplicate center-speaker subdued; stats stacked vertically.
- **Source reality:** two cameras (Anndy + co-host Daniel) with a **burned-in name tag lower-left** — PiP tracks the on-source speaker, mask the burned-in tag, keep overlays off the face.
- Fonts: **Inter is embedded**; Georgia / EB-Garamond / Fraunces trigger font warnings.

### Workflow
1. `design.md` is the brand source of truth (charcoal + cyan + Inter + motion rules).
2. Build sub-comps in `compositions/`, wire into `index.html` (never touch the base `#bgvideo`/`#bgaudio`).
3. **Add real catalog blocks via `npx hyperframes add <name>`**, restyle to `design.md`.
4. `npm run check` (lint + validate + inspect) → fix all errors; render a draft → **extract frames with ffmpeg and look at them**.
5. Gate every build through a **read-only design-QA agent** (PASS/FAIL per beat, animation polish) before declaring done.
6. Obey the HyperFrames "never do" list: `class="clip"` + data attrs, paused+registered timelines, deterministic only, GSAP visual props only, no banned eases (`back`/`elastic`/bounce), exit animations on overlays (they're not "scenes"), layout-before-animation.
7. A 1080p render is ~5 min for 60s → **~5 hours for the full 48.6-min file** (background/overnight job).

---

## Part 3 — Process lessons (what got us here)

- **Verify visually, iterate on frames.** Every direction was confirmed/corrected by rendering and looking — the QA agent once caught text floating over the speaker's face (an exit tween targeted `#br-title` when the element was class `.br-title`).
- **Read-only sub-agents work; build sub-agents are blocked in plan mode** (they can only research/plan, not Write). Harvest their research, then build directly. Don't waste spawns rediscovering this.
- **The re-transcription diff is the heart of the editing loop** — it turns the user's manual edits into durable, reusable rules instead of one-off fixes.
- **The user reviews iteratively and precisely** — small, concrete corrections (4-frame crossfades, `#11` at 0:38, glass corners, per-line sync). Build the smallest thing that proves a direction, render it, and confirm before scaling.
- **Confirm the look on the opening before committing the ~5-hour full render.**

---

*Files: `podcast-pipeline/` (cut + QA pipeline, `exclusion_rules.yaml`), `hyperframes/web4-first5/` (the graphics project + `design.md`). Companion memory: podcast-overlay-style, premiere-clip-placement-fps, premiere-audio-transitions, podcast-intro-detection, subagents-blocked-in-plan-mode.*
