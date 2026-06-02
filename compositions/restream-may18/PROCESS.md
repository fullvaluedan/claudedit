# Clip Production Process — goal: revisions to zero

## The one principle that fixes everything
**Gate the rendered pixels, not the plan.** Every revision this project hit came from the same hole: we verified the EDL (a plan) and that each beat *had* a graphic, and we spot-checked convenient frames — but nothing ever measured **the rendered output, comprehensively, across the whole timeline**. A beat can be "correct" in the EDL and blank on screen (graphic word-synced to a word spoken 18s into the beat → left zone empty until then). That gap was invisible to the EDL, to QA agents grading the EDL, and to frame-checks that sampled mid-beat payoffs.

**Rule: nothing reaches the user until `timing/check-render.py <clip>` is green AND a human has eyeballed the beat-START of every Mode-A beat.** The plan is an input; the pixels are the truth.

### The render gate is the AUTHORITY; the pre-render check is only a fast filter
We tried to check before rendering (`check-edl.py`). It helps and is instant, but it has **false negatives on hand-authored clips** and CANNOT give 100% certainty: it can't see (a) a beat whose content *exits* before its host window ends (clip-4: host mounted 0–7.5s but kinetic gone by ~3s → blank 4–8s, static says "covered"), (b) graphics that render too dark, (c) every timeline-authoring form (parser blind spots). So: run `check-edl.py` to catch obvious issues fast, but **`check-render.py` (pixels) is the only thing that makes a clip "done."** Never skip the render gate.

### Three causes of blank-left (all must be prevented)
1. **Fires late** — beat's first element word-synced to a word spoken seconds into the beat (clip-8 c8b7 +6s, c8b13 +12s).
2. **Gap between beats** — Mode-A segment not tiled; one beat ends before the next starts (clip-1: c1b6 ends 60.0, c1b6b starts 69.5 → 9.5s blank).
3. **Exits early** — content fades to 0 before the host/Mode-A window ends.

### The truly optimal path = GENERATE, don't hand-author (the only "zero future mistakes")
Hand-authoring the timeline and beats separately is why all three causes exist and why a parser-based pre-check is unreliable. The optimal end-state: a **generator** — one per-clip data spec (beats: content, word-times, view-class) → deterministically emit the master timeline so **Mode-A exactly tiles the graphic-beat spans (no gaps), every beat's frame fires at its start and holds to its end, full-frame everywhere else**, plus the z-index rule and no index counter. All three blank causes become structurally impossible, and the pre-render check becomes trivial+reliable (it verifies a generated structure, not a guessed one). Until the generator exists, the render gate is the backstop and every clip must pass it.

## The pipeline (per clip, every time)
0. **Inputs (once per episode):** `timing/clipN-words.txt` (word-sync ground truth from audio.json), `_JARGON.md`, `DESIGN.md`; extract one source frame and confirm the layout (side-by-side: host left, guest right).
1. **EDL** (`timing/clipN-edl-*.md`): open on a line actually spoken in the first ~5s; one DISTINCT primary device per clip; a **view-timeline** that is grouped (graphic beats → one Mode-A block, kinetic/breath → full-frame) with **every Mode-A beat's eyebrow/frame at beat-start (offset ≤0.5s)** so the zone is never empty; all on-screen text mapped through `_JARGON.md`; no duplicate words; no clip-number.
2. **Build** from the EDL (match clip-2 patterns; install catalog blocks for variety).
3. **ALL STATIC GATES FIRST — instant, NO render. Fix everything here before spending a single render.** This is the efficiency win: renders are minutes; statics are seconds.
   - `npx hyperframes lint` → 0 errors
   - `python3 timing/check-edl.py <clip>` → PASS (predicts blank-left from view-timeline vs first-content time; names late-firing Mode-A beats)
   - `python3 timing/check-content.py <clip>` → PASS (EMPTY-BOX: container on screen before its content, or eyebrow-only sparse hold — the thing a luminance gate can't see)
4. **ONE HQ render** (not draft — draft's 2fps/low-res sampling misses borderline blanks; gate the deliverable). Render the affected clips only, 2 concurrent.
5. **RENDER GATE — `python3 timing/check-render.py <clip>`** on the HQ → PASS (authoritative pixels: blank-left, lint, z-index, index, jargon).
6. **Human frame-verify — the cheap, mandatory step.** `ffmpeg -ss <t> -i HQ.mp4 -frames:v 1 f.png` at every Mode-A beat-START + every window any gate ever flagged, and LOOK at each (gates are necessary, not sufficient — they can't see a hollow box or wrong content; eyes can). Paste the flagged frames back to the user.
7. **Commit** (renders gitignored) — only when the user asks.

**Why this order saves time:** every defect class we've hit is catchable by a static gate (seconds) EXCEPT dark-rendering and "wrong content on screen" (need the render + eyes). So: exhaust statics → one HQ render → gate + eyeball flagged windows. We stopped doing draft renders (they gave false greens) and stopped sampling convenient frames (confirmation bias).

## The gate — `timing/check-render.py` (mechanical, immune to EDL claims)
Run on the rendered draft. Checks, all FAIL-loud with timestamps:
1. **Blank-left coverage** — scans left 60% max-luminance; any run >1.5s with no bright content = FAIL (catches "graphic fires late"; full-frame host & sparse-but-visible graphics pass). **This is the check that was missing.**
2. **lint** 0 errors · 3. **z-index** every overlay id at z-index:3 · 4. **no clip-number index** · 5. **no garbled jargon** on screen.
Extend it whenever a new defect is automatable (see loop below).

## Build invariants that make the gate pass on the FIRST try
Encoded in `DESIGN.md` (R1–R7) + `_QA-CHECKLIST.md`. The ones that prevent re-work:
- **Open on the spoken line** (word-synced from the table; never anticipatory).
- **Frame-at-beat-start** → Mode-A is never blank (R7). **View-grouped** → no flip-flop (R1).
- **Word-sync read off `clipN-words.txt`** — never computed.
- **Jargon corrected** (R3) · **no dup words** (R4) · **no index** (R6) · **one cyan/frame** · **≤2 kinetic in a row + distinct device** (R2) · **guest-centered framing ~80–85%** verified by frame.

## Revisions-to-zero loop (how this converges)
Every time the user rejects something:
1. If it's automatable → add a check to `check-render.py`. If not → add a PASS/FAIL item to `_QA-CHECKLIST.md` and a frame-check timestamp rule.
2. Fix it; re-run the gate to green.
3. The gate + checklist only GROW (monotonic). Each defect becomes a permanent guard, so it can never recur.
Over enough cycles the gate encodes all the taste → "just make clips" passes first time. That is zero revisions.

## Root-cause ledger (issues hit → permanent guard)
| Issue | Root cause | Permanent guard |
|---|---|---|
| Blank-left Mode-A (graphic fires late) | verified plan, not pixels | **check-render.py coverage** + R7 frame-at-beat-start |
| "0N" index on screen | copied chrome, unquestioned | R6 + check-render.py index grep |
| Word-sync wrong (3–47s off) | agents computed timing | `clipN-words.txt` ground truth; read, never compute |
| Hook didn't match dialog | pulled "best line" from anywhere | open-on-spoken-line rule |
| Framing on the seam (50%) | assumed values | verify framing by frame; guest ~80–85% |
| "All look like clip 2" | hand-built same template | R2 ≤2-kinetic + distinct device + catalog blocks |
| Jargon (burp/DePIN/grunt work) | transcript treated as spelling | `_JARGON.md`; check-render.py grep |
| Duplicate words ("frontrunners") | no dedup check | R4 + grep |
| View flip-flopping (A-B-A) | no view-timeline | R1 + EDL view-timeline table |
| Workflow truncation / session-limit deaths | one agent emits huge doc; over-spawn | decompose per-item; recover from journal.jsonl; cap concurrency; do deterministic fixes in-thread |
| clip-7 corruption | build rm's before write | never destructive-rm a clip without a recoverable copy |
| Render thrash (39 orphan chrome) | no proc hygiene | kill chrome-headless-shell + rm work-* between rounds; ≤2 parallel HQ jobs |
| EMPTY BOX — hollow card 16s (clip-8 2:20) | luminance gate reads a glowing empty card as "filled"; trusted a self-written gate + sampled convenient frames | `check-content.py` (shell-vs-content); design rule "container never emptier than a frame later"; frame-verify every flagged window |
| Draft passed, HQ failed (clip-1 1.5s gap) | draft 2fps sampling misses borderline blanks | gate the HQ deliverable, not the draft |
