# FINAL EDL DIRECTIVES — clips 1,3,4,5,6,7,8

This file resolves the three reviewers' feedback into binding decisions. Every finalize/QA/build
agent MUST follow this. Where a reviewer conflicts with this file, THIS FILE WINS.

Inputs in this folder:
- `clipN-words.txt` — GROUND-TRUTH word timing for clip N. Format: `comp_t  src_t  word`. **comp_t is the
  exact composition time to fire a word's kinetic line.** Never compute timing any other way. Just read it off.
- `_original-edl.md` — the first-draft EDL (beat maps for all 7 clips). Structure is good; **its word-sync
  comp times are systematically WRONG** — ignore every comp number in it and re-derive from `clipN-words.txt`.
- `_review-template.md` — template-fitness review (the 12 swaps).
- `_review-style.md` — style/pacing/hook review + transcript verification.
- `_review-qa.md` — strict DESIGN.md QA review.
- `_clip8-revised.md` — clip 8 is ALREADY finalized here (13 beats, verified timings). Use it as-is.

---

## D1 — OPENING PATTERN (resolves review-qa's "universal FAIL")

review-qa flagged all 7 clips' "full-frame kinetic at t=0 → Mode A at t=3.0" opening as a FAIL. **OVERRULED.**
The user-approved reference clip (`clip-2-altcoin-options/index.html`, v13) uses exactly this pattern: the
video is FULL-FRAME with BOTH speakers visible from t=0, the opening kinetic hook plays over it, and the
video animates to Mode A (framed right 40%) at t≈3.0s. DESIGN.md's "Opening 6 Seconds" section (lines 86–98)
explicitly endorses it. Both speakers are visible the whole time, so it is NOT "text on black."

**Binding opening for every clip (copy clip-2 exactly):**
- t=0.0–3.0s: video full-frame 1920×1080, both speakers; kinetic hook (3 phrase lines) over a dark gradient backdrop on the left.
- Hook line 1 fires at t=0.08, line 2 at ~0.88, line 3 (cyan payoff) at ~1.60. The hook is EDITORIAL (anticipatory) — it does NOT need to word-sync; it fires before the speaker reaches the line. Mark it `<!-- EDITORIAL: not word-synced -->`.
- t≈3.0s: GSAP animates the video to Mode A (right 40%, 85% scale). Glow + zone-rule fade in.
- Opening "3+ element types before 6s" is satisfied by: hook kinetic (type 1) + the swiss-grid index/eyebrow (type 2) + rule draw (type 3) + stat/columns (type 4) that fire from t=3.0 onward. This PASSES.

## D2 — WORD-SYNC (the #1 fix; applies to every non-editorial kinetic beat)

For every kinetic line that is meant to land ON a spoken word, open `clipN-words.txt`, find the word, and use its
`comp_t` as the GSAP fire time (tolerance ±0.05s). Do NOT trust any comp time in `_original-edl.md`.
- EDITORIAL kinetics (opening hooks, and any line explicitly marked editorial in `_review-*` or `_clip8-revised.md`)
  fire on a chosen comp time, not a word — they are anticipatory. Mark them in an HTML comment.
- If a phrase's words are not adjacent in the table, fire each line on its first word's comp_t.
- A kinetic beat's `data-start`/`data-duration` must contain all its line fire-times with ≥0.3s headroom on each side.

## D3 — TEMPLATE SWAPS (from _review-template.md — all ACCEPTED)

Apply these exact swaps when finalizing each clip:
- **c1b5**: decision-tree → **swiss-grid** two-column (Agency vs Principal; cyan accent on RIGHT header).
- **c1b7**: split into clean window (short) + **liquid-glass card** (no stat → not swiss-grid).
- **c1b8**: content too close to c1b6 — change to a **liquid-glass card** OR a distinct line; do NOT repeat "WE WAREHOUSE".
- **c3b4**: keep liquid-glass OR swiss-grid (builder's call) — product taxonomy. Either is fine; ensure rows stagger.
- **c3b8**: swiss-grid → **decision-tree** (4-step cycle is a flow, with looping arrows; cyan last node).
- **c4b4**: 6-step decision-tree — change the red final node to **muted/dim** (palette has only cyan + the red/green market indicators). Keep cyan as the single accent. Per _review-style, TRIM the 6-step flow to 4 key steps ([ADL Fires] → [Naked Long Delta] → [Forced Sellers] → [Alts −60/70/80%]) so it isn't a static hold for 18s.
- **c4b7**: swiss-grid (duplicate of c4b2) → **liquid-glass card** with NEW crash-severity content (not a second 25× stat).
- **c5b4**: liquid-glass → **swiss-grid** ("ALL-TIME HIGH" is a stat; slam it at 200px). Keep eyebrow "JP MORGAN PRIME BROKERAGE · MAY 2026".
- **c5b6**: decision-tree pull-quote → **liquid-glass card** quoting "The marginal risk dollar went into equities, not crypto" + attribution "Wintermute Weekly". (Resolves the consecutive-kinetic issue with c5b5.)
- **c6b3**: decision-tree → **nyt-graph** (halving block-reward decay as a descending step/bar chart: 25→12.5→6.25→3.125→1.56 BTC; 2028 bar = cyan). The 3 bullets become annotations. This is the series' one chart beat — make it distinctive.
- **c8b4**: keep liquid-glass, reframe around Jasper as the named subject (avoids a 5th kinetic).
- **c8b11**: kinetic → **liquid-glass card** closing name (mirrors c1's pattern) BUT see D4 — it must NOT read as an outro.

## D4 — NO-OUTRO / NO-INTRO (hard rule; resolves c1b9, c8b11)

- **c1b9** (review-qa + review-style both flagged): a name card that "holds through clip end" is a functional OUTRO. REMOVE it as the closer. If a Jasper name-card is wanted, place it MID-clip at a natural moment, and end the clip on a content beat (kinetic or clean video), not a card.
- **c8b11**: same rule — do not end on a static name card. End clip 8 on the verified kinetic callback "I'M DOING RESEARCH / AND TRADING / AT THE SAME TIME" (clip8-words: research@? trading@? — read the table; the literal line "I'm doing research and I'm trading" is near comp 16; if firing as a callback at clip end, mark it EDITORIAL). `_clip8-revised.md` already ends with c8b12 liquid-glass + c8b13 clean video — follow `_clip8-revised.md` for clip 8; just confirm the final 2s is clean video, not a card holding to the end.
- No guest-intro card anywhere (edl.json beat 1 excluded). No CTA / end screen (edl.json beat 32 excluded).

## D5 — HOOK REPLACEMENTS (from _review-style, ACCEPTED)

- **Clip 1**: replace weak "CRYPTO IS JUST / ANOTHER CAREER / IN AN INDUSTRY" with **"WE WAREHOUSE / THAT RISK / PRICE IS THE INCENTIVE"** (unique to the Wintermute model; the warehouse line is verified in clip1-words at comp ~108 — but the hook is EDITORIAL, fires at t=0.08/0.88/1.60).
- **Clip 5**: replace "RETAIL PIVOTED / AGGRESSIVELY / INTO EQUITIES" with **"THE MARGINAL / RISK DOLLAR / WENT INTO EQUITIES"** (thesis-grade; cyan on "EQUITIES"). The "retail pivoted" line can still be a mid-clip kinetic (it word-syncs near comp 15–18 — read clip5-words).
- **Clip 7**: replace "WE ALWAYS EXIT / BEAR MARKETS / WITH A NEW NARRATIVE" with **"PRIVACY / AND AI / ARE NEXT"** (declarative; cyan on "ARE NEXT").
- Clips 3, 4, 6, 8 hooks are STRONG — keep as written in `_original-edl.md`.

## D6 — PACING (from _review-style, ACCEPTED)

Cap any single clean-video window at ~8s in clips under 120s. Where the original had 14–18s clean windows
(c1b4, c3b5, c5b7, c8b5), split them with a verified supplemental kinetic pulled from the word table for that
gap. Every supplemental kinetic must be a real spoken line from `clipN-words.txt`, never invented.

## D7 — PALETTE / TYPE HARD RULES (from _review-qa, ACCEPTED)

- "???" labels and any epoch/table text MUST be `#F0F0F0`, never `#888888`, unless ≥48px. No decaying-opacity small text.
- One cyan `#00D4FF` element per beat (kinetic: payoff line; swiss-grid: stat OR rule, not both; card: accent bar; tree: final node; nyt-graph: target bar).
- Eyebrow: Inter 700, ≥32px, `#F0F0F0`. Body/bullets: Inter ≥600.
- Cards: `rgba(20,26,34,0.92)` solid fill + 4px cyan accent bar + soft glow + 1px border + `mask-image` feather. **NO `backdrop-filter` blur. NO grain overlay.**
- Date context: 2026 = "this year", 2025 = prior. Never 2025/2024.

## D8 — C4b6 PHRASE ORDER (from _review-qa, ACCEPTED)

Jasper says "feedback loop ... alts down 60, 70, 80%" in THAT spoken order. If the beat fires both phrases,
the kinetic order must match the spoken order (read clip4-words for the exact comp times of each), or pick ONE
phrase. Do not invert.

## D9 — CLIP 5 LENGTH (from _review-style)

Clip 5 at 180s is long. ACCEPTABLE to keep 180s IF the mid-clip re-hook (c5b5/c5b6 pull-quote) and a host-question
kinetic at the c5b7 gap are present. c5b11 must be a VERIFIED line from clip5-words (the fabricated
"NOT ENOUGH CAPITAL TO PUMP" is REMOVED). Good verified closers near the window end: read clip5-words around
comp 150–180 and pick a real line (e.g. the vol-trade closing thought).

---

## FINAL BEAT COUNTS (after fixes)

| clip | slug | src_in | src_out | dur | beats |
|------|------|--------|---------|-----|-------|
| 1 | clip-1-otc-model | 220 | 350 | 130 | 9–10 |
| 3 | clip-3-structured-products | 700 | 810 | 110 | 9–10 |
| 4 | clip-4-oct10-crash | 1010 | 1115 | 105 | 8 |
| 5 | clip-5-capital-rotation | 1120 | 1300 | 180 | 11–13 |
| 6 | clip-6-four-year-cycle | 1350 | 1470 | 120 | 8–9 |
| 7 | clip-7-bear-market-exit | 1515 | 1600 | 85 | 6–7 |
| 8 | clip-8-ai-multiplier | 1675 | 1845 | 170 | 13 (use _clip8-revised.md) |
