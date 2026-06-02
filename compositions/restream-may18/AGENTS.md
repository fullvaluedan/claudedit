# restream-may18 clips — agent instructions

This directory holds the podcast social clips. We have an established house style, hard-won across
several review rounds. **Read `PROCESS.md` first — it is the production SOP (pipeline + the gate + the revisions-to-zero loop).**

**THE GATE — ONE COMMAND (non-negotiable).** Canonical workflow + reasoning live in **`../../LESSONS.md` → "THE CLIP WORKFLOW"**. Run:

```
python3 timing/gate.py <clip-dir>            # all STATIC gates (instant, no render) — BEFORE rendering
python3 timing/gate.py <clip-dir> --render   # + the pixel gate, after ONE HQ render
```

`gate.py` runs, cheapest-first: `lint` · `check-edl.py` (blank-left predict + content-exit model) · `check-content.py` (empty/hollow box) · `check-views.py` (R1 view discipline) · `check-selectors.py` (every GSAP `#id`/`.class` target resolves — the text-over-face bug) · `check-text.py` (jargon via `_JARGON.md` / on-screen index / blur-grain) — then `check-render.py` (rendered-pixel blank-left + lint + z-index + index + jargon). Nothing ships until ALL print PASS **AND** a human has eyeballed every Mode-A beat-START + every previously-flagged window (gates are necessary, not sufficient — they can't see wrong/dark/semantically-off content; eyes can). Design rule: a container never appears emptier than it will be a frame later — full-frame the talky lead-in, then enter Mode-A + container + first content together.

**Before building, QA'ing, or planning ANY clip here, READ these files and grade against them — they are the source of truth and override generic instincts:**

1. **`../../DESIGN.md`** — brand (dark charcoal + electric cyan `#00D4FF` + Inter), hard rules (R1–R5), per-clip device map.
2. **`timing/_QA-CHECKLIST.md`** — the graded PASS/FAIL gate. Every clip must pass every item before render.
3. **`timing/_JARGON.md`** — correct spellings of crypto/AI terms (transcript mis-hears them; transcript = timing, not spelling).

## The rules that get violated most (check these first)
- **Open on the line actually spoken** in the first ~5s (trim filler heads); kinetic text = what he's saying NOW, word-synced from `timing/clipN-words.txt`. Never anticipatory text from later.
- **No view flip-flopping** — full-frame vs Mode-A holds ≥8s, no A-B-A within ~12s; group beats by view. Plan a view-timeline.
- **Template variety** — ≤2 kinetic word-stacks in a row; distinct primary device per clip; use catalog blocks (`npx hyperframes add data-chart|flowchart|shimmer-sweep|caption-neon-glow`), don't hand-build the same swiss-grid.
- **Framing** — Mode-A `object-position` centers the GUEST (~80–85%), never the seam (50%). Verify by extracting the rendered frame and looking.
- **Jargon** — every on-screen term passes `_JARGON.md` (DePIN not "deep in", perps not "burp", etc.).
- **No duplicate words** in a beat (eyebrow vs sublabel).
- **z-index:3** must list every overlay beat id. **One cyan element per frame.** No blur, no grain. No intro/outro cards.
- **Verify by frame** — never report done from self-report; extract frames at the opening + every view transition and LOOK.

Reference build: `clip-2-altcoin-options/` (structure + sub-comp patterns). Source is a SIDE-BY-SIDE (host left, guest right). Renders go in each clip's `renders/` (gitignored).

> When a new mistake is found and fixed, append the rule to `timing/_QA-CHECKLIST.md` so it never recurs. That living checklist is what makes this fork's style improve over time.
