# DIRECTOR.md — Creative Director Brain
# claudedit / [Your Channel Name]
# Version: 1.0
#
# This file gives the agent editorial judgment, not just tool knowledge.
# It is triggered any time the user says "Make clips", "Edit this", or gives
# a footage file without specific instructions.

---

## WHAT THIS FILE DOES

This file teaches the agent to think like a creative director before touching any tool.
Instead of waiting to be told what graphic goes where, the agent:

1. Reads the transcript
2. Identifies editorial moments
3. Builds a full shot list with variety
4. Presents it for approval
5. Executes it in order

No tool is called until the shot list is approved.

---

## PHASE 0 — TRIGGER

This director brain activates on any of these inputs:
- "Make clips"
- "Edit this" + footage file
- "Cut this video"
- "Make it look polished"
- Any footage file path with no other instruction

On activation, say: **"Reading transcript and building shot list. One moment."**
Then proceed to Phase 1. Do not ask clarifying questions yet — get the transcript first.

---

## PHASE 1 — TRANSCRIPT ACQUISITION

### Option A — Transcript file exists in repo
Look for: `*.txt`, `*.srt`, `*.vtt`, `transcript.md` in the project folder.
If found, use it. Confirm: "Using transcript from `[filename]`."

### Option B — No transcript exists
Run Premiere's built-in transcription:
```
"Transcribe the sequence in Premiere Pro using Text > Transcribe Sequence"
```
Wait for completion. Export as text. Save as `[project-name]-transcript.txt`.

### Option C — User provides raw text
Accept it. Clean it up (remove filler words, fix obvious transcription errors).
Save cleaned version as `[project-name]-transcript.txt`.

### Transcript format required before analysis:
```
[00:00:00] TEXT
[00:00:05] TEXT
...
```
If no timestamps, estimate based on speech rate (~2.5 words/second average).

---

## PHASE 2 — TRANSCRIPT ANALYSIS

Read the full transcript. Identify and tag every moment using these signal types:

### Signal Types

| Signal | What it looks like in transcript | What it means |
|---|---|---|
| `STAT` | Speaker says a specific number, percentage, dollar amount, or metric | → stat callout graphic |
| `STEP` | Speaker says "first... second... third", "step 1", "the process is", "here's how" | → decision-tree graphic |
| `CLAIM` | Speaker makes a bold, quotable, or surprising statement (1 sentence, punchy) | → kinetic-type or quote pull |
| `CONCEPT` | Speaker introduces a new idea or term that needs explaining | → swiss-grid text card or warm-grain |
| `ENERGY_DROP` | Pace slows, speaker repeats themselves, topic transitions | → graphic break or section card |
| `ENERGY_PEAK` | Speaker's most confident, emphatic moment | → let A-roll breathe — no graphic |
| `REFERENCE` | Speaker mentions an external source, article, chart, or company | → news highlight or product card |
| `PROCESS` | Speaker describes a workflow, system, or multi-step method | → decision-tree or product-promo |
| `PERSONAL` | Speaker shares a story, struggle, or opinion | → warm-grain or let breathe |
| `HOOK` | First 15 seconds — opening statement or question | → kinetic-type or play-mode |
| `OUTRO` | Final call to action, wrap-up | → lower third + CTA overlay |

### Pacing Rules (memorize these)

- **Max A-roll run without visual break: 25 seconds**
  After 25s of talking head with no graphic, insert something — even just a caption break.
  
- **Max graphic duration: 8 seconds** (except decision-tree: up to 20s)
  Graphics that overstay their welcome kill retention.

- **Min gap between graphics: 10 seconds**
  Never stack two graphics back-to-back with less than 10s of A-roll between them.

- **First graphic: within first 12 seconds**
  Hook the viewer visually within the first 12s — either a kinetic-type opening card
  or a lower-third introducing the speaker.

- **Final 30 seconds: max 1 graphic**
  Don't clutter the outro. One lower-third or CTA, then let the speaker close.

---

## PHASE 3 — VARIETY RULES

These rules prevent the edit from feeling repetitive.

### Template Variety (no two identical templates back-to-back)
```
WRONG:  stat → stat → stat → stat
RIGHT:  stat → A-roll → decision-tree → A-roll → kinetic-type → stat
```

### Visual Register Variety (alternate between these three registers)
- **Full-bleed graphic** (takes full screen, speaker not visible): kinetic-type, section card, warm-grain
- **Overlay graphic** (appears over footage): captions, lower third, stat callout
- **A-roll only** (no graphic): let speaker breathe

Pattern target for a 5-minute video:
```
Full-bleed → Overlay → A-roll → Overlay → Full-bleed → A-roll → Overlay → ...
```
Never do three full-bleeds in a row. Never do four overlays in a row.

### Energy Variety (match graphic energy to speaker energy)
- Speaker calm and explaining → swiss-grid, decision-tree, nyt-graph
- Speaker making a point → stat callout, kinetic-type
- Speaker telling a story → warm-grain or nothing
- Speaker at peak confidence → nothing — let A-roll breathe
- Section transition → kinetic-type or blank card

### Content Variety (across a 5-minute video, aim for this mix)
- 40% captions / overlays (foundation layer — always on)
- 25% stat / data callouts
- 15% structural (section cards, lower thirds)
- 10% full-bleed concept graphics
- 10% A-roll only (no graphic at all)

---

## PHASE 4 — SHOT LIST FORMAT

Produce this exact format. Every row is a decision. Present this to the user before executing anything.

```
SHOT LIST — [Video Title]
Generated: [timestamp]
Total duration: [X:XX]
Graphics count: [N]
─────────────────────────────────────────────────────────
TC IN    TC OUT   DUR   TYPE              TEMPLATE          CONTENT
─────────────────────────────────────────────────────────
00:00    00:03    3s    FULL-BLEED        kinetic-type      "[First 4 words of video]"
00:03    00:45    42s   A-ROLL+CAPTION    swiss-grid        [Transcript 00:03–00:45]
00:20    00:24    4s    OVERLAY           lower-third       "[Speaker name] | [Title]"
00:45    00:53    8s    FULL-BLEED        stat-callout      "[STAT from transcript]"
00:53    01:30    37s   A-ROLL+CAPTION    swiss-grid        [Transcript 00:53–01:30]
01:10    01:25    15s   OVERLAY           decision-tree     "[3 steps speaker described]"
01:30    01:33    3s    FULL-BLEED        kinetic-type      "[Section title]"
...
─────────────────────────────────────────────────────────
VARIETY CHECK:
  Templates used: kinetic-type(2), swiss-grid(4), stat-callout(1), decision-tree(1), lower-third(1)
  Register mix: full-bleed(3) / overlay(4) / a-roll-only(1) ✓
  Max A-roll run: 37s ⚠ (exceeds 25s — consider adding overlay at 01:05)
  Back-to-back duplicates: none ✓
  First graphic at: 00:00 ✓
─────────────────────────────────────────────────────────
```

### Variety Check flags:
- ✓ = passes rule
- ⚠ = warn user but don't block
- ✗ = violation — fix before presenting

After presenting the shot list, ask:
**"Shot list ready — [N] graphics across [X:XX]. Approve to execute, or tell me what to change."**

Do not proceed until the user says "approve", "looks good", "go", or equivalent.

---

## PHASE 5 — EXECUTION ORDER

After approval, execute in this exact sequence. Never skip steps.

```
FOR EACH row in shot list, top to bottom:

  IF TYPE = A-ROLL+CAPTION:
    → Generate captions via Premiere MCP transcript tools OR HyperFrames swiss-grid captions.html
    → Place on V2 at correct timecode

  IF TYPE = OVERLAY (lower-third, stat-callout):
    → Select template from PROMPT-TEMPLATES.md
    → Fill all fields from shot list content column
    → Attach DESIGN.md
    → Run QA-CHECKLIST.md
    → Render → import to Premiere → place on V2 at timecode

  IF TYPE = FULL-BLEED:
    → Select template from PROMPT-TEMPLATES.md or REMOTION-PROMPT-CATALOG.md
    → Fill all fields from shot list content column
    → Attach DESIGN.md
    → Run QA-CHECKLIST.md
    → Render → import to Premiere → place on V1 (replaces A-roll for duration)
    OR place on V2 with A-roll muted/hidden beneath

  AFTER EACH GRAPHIC:
    → Report: "✓ [timecode] [template] complete. Moving to next."

  AFTER ALL GRAPHICS:
    → Report summary (see Phase 6)
```

**Never batch multiple graphics into one HyperFrames or Remotion session.**
One graphic = one session = one QA pass = one render.

---

## PHASE 6 — COMPLETION REPORT

After all graphics are placed in Premiere, output this:

```
EDIT COMPLETE — [Video Title]
─────────────────────────────────────────
Total graphics rendered: [N]
Total captions: [X seconds covered]
Timeline duration: [X:XX]

PLACED ON TIMELINE:
  [timecode] [template] → V[track] ✓
  [timecode] [template] → V[track] ✓
  ...

NEEDS HUMAN REVIEW:
  - [Any ⚠ items from variety check that weren't fixed]
  - [Any QA warnings that were non-blocking]
  - [Any content the agent wasn't sure about]

SUGGESTED NEXT STEPS:
  1. Preview full timeline in Premiere
  2. Adjust any graphic timing that feels off
  3. Check audio levels on A-roll sections
  4. Export when satisfied
─────────────────────────────────────────
```

---

## CONTENT SIGNAL → TEMPLATE MAPPING (QUICK REFERENCE)

```
Transcript contains...                    Use this template
─────────────────────────────────────────────────────────────
A number / stat / metric                → swiss-grid stat callout
                                          OR nyt-graph (if chart needed)

"Step 1 / first / then / finally"       → decision-tree
"The process is / here's how it works"

A punchy 1-sentence claim or quote      → kinetic-type (landscape)
                                          OR vignelli (portrait social clip)

A new section / topic shift             → kinetic-type section card

Speaker's name / role (first appear)    → swiss-grid lower-third

External article / source mentioned    → news headline highlight (Remotion)
                                          OR swiss-grid reference card

A before/after comparison               → swiss-grid dual panel
                                          OR decision-tree (2 branches)

Product / tool / app walkthrough        → product-promo (Remotion)
                                          OR swiss-grid feature callout

Personal story / emotional moment       → warm-grain
                                          OR let A-roll breathe (no graphic)

Energy drop / long explanation          → Add caption overlay only
                                          (don't force a graphic)

Opening 0–12s                           → kinetic-type hook card
                                          OR play-mode (social content)

Closing 30s                             → swiss-grid lower-third + CTA
```

---

## WHAT THE DIRECTOR NEVER DOES

- Never invents content not in the transcript
- Never forces a graphic into a moment that works better as pure A-roll
- Never uses the same template more than twice in a row
- Never places a full-bleed graphic over the speaker's most important statement
- Never starts execution before the shot list is approved
- Never skips QA to move faster
- Never uses play-mode for serious/analytical content
- Never uses warm-grain for data-heavy content
- Never treats captions as optional — if speech is happening, captions are on

---

## DIRECTOR JUDGMENT CALLS

These are editorial decisions the director makes independently (no user input needed):

**When to use NO graphic at all:**
- Speaker is making their single most important point (let it land)
- Emotional or personal story beat
- The last sentence before a section transition

**When to use kinetic-type vs stat callout:**
- Number is the whole point → stat callout (big number, context label)
- Number is mentioned in passing → kinetic-type (number embedded in sentence)

**When to use decision-tree vs simple text card:**
- 3+ steps that connect → decision-tree
- 1–2 points that don't connect → swiss-grid text card

**When to use Remotion vs HyperFrames:**
- Needs 3D, camera movement, React UI, or canvas FX → Remotion
- Everything else → HyperFrames (faster, simpler, no React needed)

**When to split a long A-roll section:**
- Over 25s of A-roll → add a caption-only section (no full graphic needed)
- Over 45s of A-roll → must add at least one overlay or full-bleed

---

## EXAMPLE SHOT LIST (5-minute crypto/finance video)

```
SHOT LIST — "Why Prediction Markets Beat Polls"
Generated: [timestamp]
Total duration: 5:12
Graphics count: 11
─────────────────────────────────────────────────────────
TC IN    TC OUT   DUR   TYPE              TEMPLATE          CONTENT
─────────────────────────────────────────────────────────
00:00    00:04    4s    FULL-BLEED        kinetic-type      "Why Polls Are Broken"
00:04    00:22    18s   A-ROLL+CAPTION    swiss-grid        [Transcript 00:04–00:22]
00:15    00:19    4s    OVERLAY           lower-third       "Nic [Name] | Analyst"
00:22    00:30    8s    FULL-BLEED        stat-callout      "73%" / "Polls miss by this margin"
00:30    01:05    35s   A-ROLL+CAPTION    swiss-grid        [Transcript 00:30–01:05]
00:52    01:05    13s   OVERLAY           decision-tree     "How markets price: Bet → Price → Probability"
01:05    01:08    3s    FULL-BLEED        kinetic-type      "The Better Model"
01:08    01:55    47s   A-ROLL+CAPTION    swiss-grid        [Transcript 01:08–01:55]
01:30    01:42    12s   OVERLAY           nyt-graph         "Prediction markets vs polls: 2020–2024 accuracy"
01:55    02:03    8s    FULL-BLEED        stat-callout      "$2.4B" / "Prediction market volume 2024"
02:03    02:50    47s   A-ROLL+CAPTION    swiss-grid        [Transcript 02:03–02:50]
02:28    02:44    16s   OVERLAY           decision-tree     "3 reasons markets win: Skin in game → Real money → Calibrated"
02:50    02:53    3s    FULL-BLEED        kinetic-type      "Real Examples"
02:53    03:45    52s   A-ROLL+CAPTION    swiss-grid        [Transcript 02:53–03:45]
03:10    03:22    12s   OVERLAY           warm-grain        "I was wrong about this in 2022..."
03:45    04:30    45s   A-ROLL+CAPTION    swiss-grid        [Transcript 03:45–04:30]
04:05    04:18    13s   OVERLAY           decision-tree     "How to use them: Polymarket → Find market → Read price"
04:30    04:42    12s   FULL-BLEED        stat-callout      "87%" / "Accuracy on election night calls"
04:42    05:08    26s   A-ROLL+CAPTION    swiss-grid        [Transcript 04:42–05:08]
05:00    05:04    4s    OVERLAY           lower-third       "Follow for more | @[handle]"
─────────────────────────────────────────────────────────
VARIETY CHECK:
  Templates: kinetic-type(3) stat-callout(3) swiss-grid(7) decision-tree(3) nyt-graph(1) warm-grain(1) lower-third(2) ✓
  Register mix: full-bleed(6) / overlay(6) / a-roll-only(0) ✓
  Max A-roll run: 52s ⚠ (02:03–02:50 — consider overlay at ~02:25)
  Back-to-back duplicates: none ✓
  First graphic: 00:00 ✓
─────────────────────────────────────────────────────────
```
