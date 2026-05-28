# WORKFLOW.md — End-to-End Editing Workflow
# claudedit / [Your Channel Name]
# Version: 1.0

---

## OVERVIEW

This file defines the complete workflow for AI-assisted video editing.
Two systems work in parallel — they are never mixed.

| System | Handles | When to call |
|---|---|---|
| **Premiere MCP** (leancoderkavy) | Raw footage editing — cuts, trims, silence removal, positioning, fades, color, audio | Always first |
| **HyperFrames** | Motion graphics, captions, B-roll overlays | Only when graphics are needed |

---

## PHASE 1 — INGEST & PREP (Premiere MCP)

**You do this before calling any AI agent.**

1. Import all raw footage into Premiere
2. Organize into bins: `[DATE]-[TOPIC]-[TAKE]`
3. Create a new sequence: 1920×1080, 30fps
4. Place main A-roll (talking head) on V1/A1

**Premiere MCP commands to use:**
```
"Import all files from [folder path]"
"Create a new sequence named [name], 1920x1080, 30fps"
"Place [filename] on V1 starting at 00:00:00"
```

---

## PHASE 2 — ROUGH CUT (Premiere MCP)

**Goal:** Get a first pass edit with all key content kept.

Tell the Premiere MCP agent:
```
"Review the sequence. Remove all sections where the speaker is silent 
for more than 1.5 seconds. Use ripple delete to close gaps."

"Remove any section where the speaker repeats themselves. 
Keep the clearest take of each point."

"Add a 3-frame cross-dissolve between each cut."
```

**Do not add graphics yet.** Get the cut right first.

---

## PHASE 3 — TRANSCRIPT (External — before HyperFrames)

Before calling HyperFrames for captions, you need a transcript.

Options:
- Premiere Pro built-in: **Text > Transcribe Sequence** (uses Adobe AI)
- Export audio → run through Whisper locally
- Export audio → paste into any transcription service

**Save transcript as:** `[project-name]-transcript.txt` in your project folder.
Include timestamps: `[00:00:00] TEXT`

This transcript feeds into Template 1 (Caption Block) and Template 12 (Long-form Captions).

---

## PHASE 4 — FINE CUT (Premiere MCP)

After rough cut, refine with Premiere MCP:

```
"Adjust audio levels on A1 to -12dB average, peaks not exceeding -6dB"

"Add a 15-frame fade in at the beginning of V1"
"Add a 15-frame fade to black at the end of V1"

"Set clip [name] position to X:[value] Y:[value]"
"Set clip [name] scale to [value]%"
```

---

## PHASE 5 — IDENTIFY GRAPHIC MOMENTS

Before calling HyperFrames, review your cut and make a list.

For each graphic moment, note:
- Timecode in the sequence (where the B-roll will go)
- Duration needed
- Which template to use (see TEMPLATE-CATALOG.md Decision Guide)
- Exact content (stats, text, steps — from what the speaker actually said)

**Example brief:**
```
00:01:23 – 00:01:31 (8s): Stat callout — speaker says "revenue grew 340%"
  → Template 2 (Stat Callout), swiss-grid
  → Stat: "340%" | Label: "Revenue Growth YoY" | Source: "Internal, 2024"

00:02:10 – 00:02:40 (30s): Captions needed
  → Template 1 (Caption Block), swiss-grid
  → Transcript: [paste from transcript file]

00:03:45 – 00:04:00 (15s): 3-step process explainer
  → Template 6 (Decision Tree)
  → Step 1: "Connect wallet" | Step 2: "Deposit USDC" | Step 3: "Confirm trade"
```

---

## PHASE 6 — GENERATE GRAPHICS (HyperFrames)

**Only now do you call HyperFrames.**

For each graphic moment identified in Phase 5:

1. Open a new session with `/hyperframes`
2. Attach: `DESIGN.md`, `TEMPLATE-CATALOG.md`
3. Use the appropriate template from `PROMPT-TEMPLATES.md`
4. Fill in ALL bracketed fields — no blanks
5. After generation → run QA-CHECKLIST.md
6. If QA passes → render: `npx hyperframes render`
7. Output: MP4 file saved to `[project]/graphics/[name].mp4`

**One graphic per HyperFrames session.** Don't try to batch multiple graphics in one prompt — quality degrades.

---

## PHASE 7 — IMPORT GRAPHICS TO PREMIERE (Premiere MCP)

After each graphic is rendered:

```
"Import [graphic-name].mp4 from [path]"
"Place [graphic-name].mp4 on V2 at timecode [00:00:00]"
"Set duration to [X] seconds"
```

Stack graphics on V2 (or V3 for overlays) above the main footage on V1.

---

## PHASE 8 — FINAL REVIEW (Human)

This phase is always human. The AI does not sign off on final quality.

Check:
- [ ] All cuts feel natural
- [ ] Graphics appear at the right moments
- [ ] No graphic obscures the speaker's face
- [ ] Audio levels consistent throughout
- [ ] Captions are accurate
- [ ] Opening and closing fades work
- [ ] Total runtime is appropriate

---

## PHASE 9 — EXPORT (Premiere MCP or Manual)

```
"Export the sequence as H.264, 1920x1080, 30fps, target bitrate 20Mbps"
"Export to [output path]"
```

Or export manually via File > Export > Media in Premiere.

---

## QUICK REFERENCE — Agent Scope

```
Raw footage editing           → Premiere MCP ONLY
Silence removal               → Premiere MCP ONLY
Repeated phrase removal       → Premiere MCP ONLY  
Positioning / scaling clips   → Premiere MCP ONLY
Fades (video + audio)         → Premiere MCP ONLY
Color correction              → Premiere MCP ONLY

Captions / subtitles          → HyperFrames ONLY
Lower thirds                  → HyperFrames ONLY
Stat callout graphics         → HyperFrames ONLY
Section title cards           → HyperFrames ONLY
Data charts                   → HyperFrames ONLY
Intro/outro motion graphics   → HyperFrames ONLY
Quote pull graphics           → HyperFrames ONLY
```

---

## COMMON MISTAKES TO AVOID

1. **Calling HyperFrames before the cut is done** — waste of render time if the edit changes
2. **Skipping the transcript step** — captions without a transcript will hallucinate content
3. **Describing graphic content vaguely** — "show something about growth" produces garbage; provide exact numbers
4. **One giant HyperFrames prompt for all graphics** — do them one at a time
5. **Skipping QA** — renders without QA catch the wrong-speaker problem you already experienced
6. **Using play-mode for serious content** — the energy clash is obvious to viewers
