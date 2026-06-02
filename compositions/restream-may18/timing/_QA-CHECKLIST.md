# QA CHECKLIST — restream-may18 podcast clips (graded EVERY build)

This is the living gate. Every EDL/QA/build agent reads this BEFORE working and grades against it.
ANY single FAIL = the clip fails and must be fixed before render. New failure modes get appended here
(that is the point — we never make the same mistake twice). Companion files: `_JARGON.md` (term spellings),
`DESIGN.md` (palette/type/brand). Source layout is a SIDE-BY-SIDE: Nic (host) left half, Jasper (guest) right half.

---

## 0. THE GATES (mandatory — nothing ships until both green). See `PROCESS.md`.
- [ ] **Pre-render (instant, no render):** `python3 timing/check-edl.py <clip-dir>` prints **PASS** — predicts blank-left from the source (view-timeline vs each beat's first-content time) and names late-firing Mode-A beats. Fix here before rendering.
- [ ] **Render (authoritative backstop):** `python3 timing/check-render.py <clip-dir>` prints **PASS** — measures the rendered pixels (blank-left coverage, lint, z-index, no-index, jargon). Immune to what the EDL claims.
- [ ] **Empty-box (no render):** `python3 timing/check-content.py <clip-dir>` prints **PASS** — separates the SHELL (card/glass/panel/eyebrow/rule) from the SUBSTANTIVE CONTENT inside it, and FAILs any Mode-A beat where a CONTAINER is on screen >2.5s before its content (the literal "empty box" — clip-8 c8b13 was a hollow card for 16s) or only a title/eyebrow shows >5s with no content (sparse hold). The brightness gate (check-render) CANNOT catch this — a glowing empty card pegs luminance. R7 "frame-at-start" is satisfied by CONTENT, not by an empty container.
- A clip is NOT done until ALL THREE are green AND a human has watched every Mode-A beat-START + every previously-flagged window (the gates are necessary, not sufficient; a luminance/timeline check can't see "the box is hollow" — eyes can). This is why revisions trend to zero.
- **Design rule (so check-content passes by construction):** a container must never appear emptier than it will be one frame later. If the data is word-locked late, hold FULL-FRAME (both speakers) until it arrives, then bring Mode-A + container + first content in together. Never stage an empty card ahead of its rows.

## 1. View-switching discipline (R1) + view-follows-content (R7)
- [ ] **R7 — NO blank-left Mode-A.** Every Mode-A segment has a left-zone GRAPHIC on screen for its ENTIRE duration. A clean/breath beat (no graphic) MUST be full-frame (both speakers) — never a speaker cropped right with an empty left half. A no-graphic gap inside a Mode-A block = FAIL (the clip-8 0:33–0:52 bug). Classify each beat (graphic→Mode-A, kinetic/breath→full-frame); the view must match.
- [ ] **R6 — NO index/clip-number on screen.** No "01".."08" or beat index rendered anywhere. Eyebrow editorial labels are fine; the bare number is a FAIL.
- [ ] **Build a view-timeline** for the clip: list every full-frame↔Mode-A segment with its dwell seconds AND what graphic fills each Mode-A segment (none allowed). Include it in the EDL.
- [ ] **No segment < 8s** outside the 0–6s intro. A 4–5s view sandwiched between others is a FAIL.
- [ ] **No A-B-A within ~12s.** The video must NOT return to a view it just left within 12s. (full→ModeA→full or ModeA→full→ModeA in a short span = FAIL.) This was the clip-7 41–49s and clip-8 11–16s bug.
- [ ] **Group consecutive graphic beats into the SAME view** so the frame doesn't bounce. Two kinetics near each other → stay full-frame across both; two Mode-A graphics → stay Mode-A across both.
- [ ] Quick changes allowed ONLY in the 0–6s intro, and even there never loop back to the same view.

## 2. Template variety (R2) — don't make another clip-2
- [ ] **≤ 2 kinetic word-stacks in a row.** 3+ consecutive kinetic beats = FAIL (clip-5 was 46% kinetic).
- [ ] **Distinct PRIMARY device** per clip (see DESIGN.md per-clip map). The clip must not be kinetic-dominated.
- [ ] **"Did I consider a catalog block?"** For stats/data → `data-chart`; flows/cascades → `flowchart`; premium reveals → `shimmer-sweep`; payoff emphasis → `caption-neon-glow` / `caption-kinetic-slam`. Install via `npx hyperframes add <name>`. Hand-building the same swiss-grid every time is the anti-pattern.
- [ ] Init variety: a clip whose content is a chart/flow/comparison should NOT init from `kinetic-type` by default.

## 3. Dialog-match + open-on-line (proven rule)
- [ ] The clip OPENS on a strong line ACTUALLY SPOKEN in the first ~0–5s (re-pick the in-point; trim "yeah yeah" filler). No anticipatory hook pulled from 60–120s later.
- [ ] Every kinetic line fires at `comp_t = word.src_t − src_in`, read from `clipN-words.txt` (±0.15s). Never compute by hand. Mark genuinely editorial labels.
- [ ] First text appears by ~t=0.3s (a soft >1.5s cold-open before any text = FAIL; tighten the in-point).

## 4. Opening coherence (R5)
- [ ] The opening lines parse as a COMPLETE thought on their own. "REQUIRES A TEAM OF / 2–3" (needs "people") = FAIL.
- [ ] The cyan payoff is a real noun/phrase, not a dangling number or fragment.

## 5. Speaker framing (proven rule) — verify by FRAME, never assume
- [ ] Mode-A `object-position` CENTERS THE GUEST (Jasper, right half): ~80–85%. `50%`/`62%` centers the seam/host = FAIL.
- [ ] Extract the rendered Mode-A frame and LOOK: Jasper head-and-shoulders, centered, name tag visible, no host bleed, no big dead ceiling. Tune object-position / vertical bias / scale until right.
- [ ] Opening full-frame beats show BOTH speakers (never text on black).

## 6. Jargon (R3) — every on-screen term mapped through `_JARGON.md`
- [ ] No garbled Whisper term on screen. Specifically: **DePIN** (not "deep in"), **perps** (not "burp"), **grunt work** (not "graft"), **take rate** (not "stake rate"), **meme coin** (not "meme con"), **insatiable** (not "insaturable").
- [ ] Brand/proper nouns spelled exactly (Wintermute, Paradex, Morpho, HyperLiquid, dYdX, Polymarket, Kalshi, Bittensor, NotebookLM, zkML, Web4, Jasper De Maere).

## 7. Duplicate words (R4)
- [ ] The same notable word does NOT appear in two text elements of one beat (eyebrow vs sublabel/title). "THE FRONTRUNNERS" + "the frontrunners" = FAIL. Each element earns distinct words.

## 8. Carry-over hard rules (DESIGN.md)
- [ ] z-index:3 rule lists EVERY overlay beat id (else it renders invisible behind the video). Verify div-id vs rule.
- [ ] ONE cyan `#00D4FF` element per frame max (kinetic: payoff line; swiss-grid: stat OR rule; card: accent bar; tree/chart: final node/bar).
- [ ] No `backdrop-filter` blur. No film-grain overlay. Cards = solid `rgba(20,26,34,0.92)` + 4px cyan bar + glow + mask feather.
- [ ] Eyebrow Inter 700 ≥32px `#F0F0F0`; body/bullets Inter ≥600. Muted secondary text = `#B6BEC6` (readable ~7:1 on dark). **`#888888` is RETIRED — never use it** (too dim); a build with `#888` = FAIL.
- [ ] No intro cards, no outros, no closing/CTA card; clip ends on a content beat or clean video.
- [ ] Dates: 2026 = "this year", 2025 = prior. Never 2025/2024.
- [ ] Phrase kinetic lines build and STAY (no dim of previous lines).

## 9. Verify-by-frame (MANDATORY before claiming done)
- [ ] After draft render, extract frames at: the opening, EACH view transition, and each distinct beat — and LOOK. Never report "done" from agent self-report alone. The human-side reviewer (me) re-verifies every clip.

## 10. Render hygiene (prevents thrash)
- [ ] BETWEEN render rounds, kill stray workers and temp dirs: `pkill -f chrome-headless-shell; pkill -f hyperframes; rm -rf */renders/work-*`. `chrome-headless-shell` is the render worker (NOT the user's Google Chrome) — it accumulates across rounds and, unkilled, 30–40 procs thrash a 14-core mac so renders crawl (June 2026: a 7-clip HQ batch stalled 64 min stuck on the first clip of each job).
- [ ] Cap concurrency: ≤2 parallel HQ jobs × `--workers 4` (~16 Chrome procs) on a 14-core machine. Each job renders its clips SEQUENTIALLY.
- [ ] After delivering, delete non-deliverable renders (`*-draft.mp4`, `verify.mp4`, `work-*`); keep only `*-HQ.mp4`. Renders are gitignored.

---
### Change log (append new failure modes here — "learn from each iteration")
- 2026-06-02 — Created from round-3 feedback. Added R1 (no flip-flop), R2 (template variety), R3 (jargon), R4 (no dup words), R5 (opening coherence). Earlier proven rules folded in from DESIGN.md + memory.
