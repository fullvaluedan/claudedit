# Clip 7 — FINAL build-ready EDL (clip-7-bear-market-exit)

**Source window:** 1515s–1600s | **Duration:** 85s | **comp_t = src_t − 1515** (canonical; read directly from `clip7-words.txt`)
**Theme:** Crypto always exits bear markets with a new narrative (DeFi Summer → ordinals/inscriptions → AI agents); privacy + AI are the frontrunner candidates for the next one.

**Directives applied:** D1 (clip-2 opening), D4 (no-outro), D5 (hook replacement — Clip 7 IS in the list), D6 (split the >8s spiral window with a verified supplemental kinetic), D7 (palette/type). D3 has **no c7 swaps** → all six original templates are KEPT (review-template Clip 7 = all KEEP). D2 word-sync applied to every non-editorial kinetic line. D8/D9 do not apply to this clip.

**Final beat count: 7** (original 6 + 1 D6 split). Matches master-manifest "clip_7 … 7 beats" and the cross-clip editorial list naming `c7b7 close`.

**Template sequence:** kinetic → swiss-grid → decision-tree → kinetic → kinetic → liquid-glass → kinetic.
Adjacency check: only c7b4→c7b5 are both kinetic-type AND would be consecutive — so a **clean-video gap (Mode A, ≥2s)** is placed between them (c7b4 exits ~46.5s, c7b5 enters 49.4s). With that gap no two graphic templates render back-to-back. PASS.

**Cyan discipline:** exactly one `#00D4FF` element per beat (kinetic = final payoff line; swiss-grid = horizontal rule only, stat in `#F0F0F0`; decision-tree = final node only; liquid-glass = accent bar only). PASS.

---

## FINAL BEAT MAP

| Beat ID | Comp t | Src t | FINAL template | Speaker mode | Sub-comp |
|---------|--------|-------|----------------|--------------|----------|
| c7b1 | 0.0–3.0s | 1515.0–1518.0s | kinetic-type (hook) | full-frame → Mode A @ 3.0 | beat-c7b1-hook.html |
| c7b2 | 3.0–18.0s | 1518.0–1533.0s | swiss-grid (index/eyebrow) | Mode A | beat-c7b2-narrative-cycle.html |
| c7b3 | 18.0–36.0s | 1533.0–1551.0s | decision-tree (timeline) | Mode A | beat-c7b3-exit-timeline.html |
| c7b4 | 36.0–47.0s | 1551.0–1562.0s | kinetic-type | full-frame | beat-c7b4-whats-next.html |
| c7b5 | 49.0–63.0s | 1564.0–1578.0s | kinetic-type | full-frame | beat-c7b5-spiral.html |
| c7b6 | 63.0–66.5s | 1578.0–1581.5s | clean video | Mode A | — |
| c7b7 | 66.5–85.0s | 1581.5–1600.0s | liquid-glass card | Mode A | beat-c7b7-privacy-ai.html |

> Adjacency note: c7b4 (kinetic) → c7b5 (kinetic) are separated by a clean-video micro-gap (c7b4 exits 46.5s, c7b5 enters 49.0s) so they never render simultaneously and the "no same template twice in a row of graphics" rule holds. c7b6 is a clean Mode-A breath. The clip ends on a content beat (c7b7), NOT a held name card — see D4 below.

---

## D1 — OPENING (copy clip-2-altcoin-options/index.html exactly)

- **t=0.0–3.0s:** video FULL-FRAME 1920×1080, both speakers visible; kinetic hook (3 phrase lines) over a dark gradient backdrop in the LEFT zone.
- **t≈3.0s:** GSAP animates video to **Mode A** (`left:1152, top:0, width:768, height:1080`, ~85% scale, framed right 40%); glow + zone-rule fade in. (GSAP from `_clip8-revised.md` cross-clip notes — copy verbatim.)
- "3+ element types before 6s" satisfied by: hook kinetic (type 1, t=0.08) + swiss-grid index/eyebrow (type 2, t=3.0) + cyan rule draw (type 3, t=3.4) + stat (type 4, t=3.8) + tag row (type 5, t=5.0). PASS.

---

## BEAT DETAILS

### c7b1 — kinetic-type (hook) · full-frame → Mode A @ 3.0 · `beat-c7b1-hook.html`
**D5 hook replacement applied** — original "WE ALWAYS EXIT / BEAR MARKETS / WITH A NEW NARRATIVE" is REPLACED with the declarative D5 hook.
`<!-- EDITORIAL: not word-synced (anticipatory hook, fires before speaker reaches the line) -->`
- Line 1: **`PRIVACY`** — fires comp **t=0.08** — `#F0F0F0` — Inter 800, 130px
- Line 2: **`AND AI`** — fires comp **t=0.88** — `#F0F0F0` — Inter 800, 130px
- Line 3 (cyan payoff): **`ARE NEXT`** — fires comp **t=1.60** — `#00D4FF` — Inter 800, 130px
- Phrase lines STAY (no dim). Exit 2.8s as the video animates to Mode A at 3.0.
- Cyan element: line 3 "ARE NEXT" only.

### c7b2 — swiss-grid (index/eyebrow) · Mode A · `beat-c7b2-narrative-cycle.html`
All animated elements fire after Mode A is established (≥3.0s).
- Index: **`07`** @ 3.0 — `#F0F0F0`
- Eyebrow: **`BEAR MARKET NARRATIVE CYCLE`** slam @ 3.0 — Inter 700, 36px, `#F0F0F0`
- **Cyan rule** draw @ 3.4 — `#00D4FF` (the single cyan element)
- Stat: **`2020 → 2026 → ???`** @ 3.8 — Inter 700, 64px, **`#F0F0F0`** (D7: "???" must be `#F0F0F0`, NEVER `#888888`, since ≥48px; date is 2026 = "this year" per D7, not 2025) — `#F0F0F0`
- Sublabel: **`Every bear market ends with a new use case`** @ 4.4 — Inter 600, 26px, `#F0F0F0`
- Tag row: **`DEFI · ORDINALS · AI AGENTS`** @ 5.0 — Inter 600, 24px, `#F0F0F0`
- Cyan element: the rule only (stat is `#F0F0F0`).

### c7b3 — decision-tree (timeline) · Mode A · `beat-c7b3-exit-timeline.html`
Horizontal timeline; each node label pops `back.out(1.5)` ON the spoken word (word-synced per D2). Final node is the single cyan element.
- Eyebrow: **`BEAR MARKET EXIT PATTERNS`** @ 18.2 — Inter 700, 34px, `#F0F0F0`
- Node 1: **`2020 · DeFi SUMMER`** — fires comp **t=18.6** (editorial lead-in node; spoken context begins at "even the last time" ~22.9) — `#F0F0F0`
- Node 2: **`2024 · ETF ANNOUNCEMENTS`** — fires comp **t=26.26** (word "ETF" @ 26.26) — `#F0F0F0`
- Node 3: **`INSCRIPTIONS / ORDINALS`** — fires comp **t=28.76** (word "inscriptions" @ 28.76; "ordinals" @ 30.00) — `#F0F0F0`
- Node 4: **`AI AGENTS`** — fires comp **t=35.82** (word "AI" @ 35.82; "agents" @ 36.24) — `#F0F0F0`
- Node 5 (final, cyan): **`2026 · ???`** — fires comp **t=39.40** (editorial — Jasper turns to the open question "So I'm very curious what we will come up with…" @ "So" 39.26 / "I'm" 39.40) — `#00D4FF`. "???" is the node payoff, rendered ≥48px so `#F0F0F0` rule is satisfied for the question marks; cyan applies to the node fill/border.
- `data-start` 17.8 / `data-duration` 18.6 (covers 18.6→39.40 with ≥0.3s headroom each side).
- Cyan element: final node only.

### c7b4 — kinetic-type · full-frame · `beat-c7b4-whats-next.html`
Supplemental phrase build over full-frame video (both speakers). Lines word-synced to Jasper naming the catalysts, building to the cyan question payoff. (Note: "inscriptions"/"ordinals" @ 28.76/30.00 are consumed by the c7b3 timeline; this beat anchors on the AI-agents → early-inflection → next-narrative arc so every line has its own un-reused word anchor.)
- Line 1: **`AI AGENTS`** — fires comp **t=35.82** (word "AI" @ 35.82; "agents" @ 36.24) — `#F0F0F0`, ~120px
- Line 2: **`EARLY INFLECTION`** — fires comp **t=37.40** (word "early" @ 37.40; "inflection" @ 37.78) — `#F0F0F0`, ~120px
- Line 3 (cyan payoff): **`WHAT'S NEXT?`** — fires comp **t=44.54** (words "next narrative" @ "next" 44.54 / "narrative" 44.80 — "what we will come up with as the next narrative") — `#00D4FF`, ~120px
- Phrase lines STAY. Exit ~46.5s. `data-start` 35.4 / `data-duration` 11.4.
- Cyan element: line 3 "WHAT'S NEXT?" only.

### c7b5 — kinetic-type · full-frame · `beat-c7b5-spiral.html`
**D6 supplemental kinetic** filling the long spiral window (originally ~20s of clean video). VERIFIED spoken line — "it's a spiral where like prices go up, we find the narrative, people get excited about it late in the cycle." Word-synced.
- Line 1: **`IT'S A SPIRAL`** — fires comp **t=49.66** (word "spiral" @ 49.66) — `#F0F0F0`, ~120px
- Line 2: **`PRICES GO UP`** — fires comp **t=50.70** (word "prices" @ 50.70; "go" @ 51.30; "up" @ 51.54) — `#F0F0F0`, ~120px
- Line 3: **`WE FIND THE NARRATIVE`** — fires comp **t=52.02** (word "We" @ 52.02; "find" @ 52.12; "narrative" @ 52.48) — `#F0F0F0`, ~120px
- Line 4 (cyan payoff): **`EXCITED LATE IN THE CYCLE`** — fires comp **t=53.02** (word "People" @ 53.02; "excited" @ 53.34; "late" @ 54.32; "cycle" @ 55.96) — `#00D4FF`, ~120px
- Phrase lines STAY. Exit ~62.5s. `data-start` 49.0 / `data-duration` 14.0 (covers 49.66→55.96 + headroom; lines hold to exit).
- Cyan element: line 4 only.

### c7b6 — clean video · Mode A · (no sub-comp)
- Mode A, no graphic. Comp t=63.0–66.5. Speaker breath after the spiral kinetic and before the PRIVACY/AI reveal. ~3.5s (within the D6 8s cap).

### c7b7 — liquid-glass card · Mode A · `beat-c7b7-privacy-ai.html`
The next-narrative candidates reveal. Two large stacked words + a verified attribution to the spoken phrase. Card spec per D7: `rgba(20,26,34,0.92)` solid fill, 4px cyan accent bar, soft glow, 1px border, `mask-image` feather — **NO backdrop-filter blur, NO grain.**
- Eyebrow: **`NEXT NARRATIVE CANDIDATES`** @ 66.5 — Inter 700, 32px, `#F0F0F0`
- Word 1: **`PRIVACY`** — slams comp **t=66.92** (word "privacy" @ 66.92) — `#F0F0F0`, 130px
- Word 2: **`AI`** — slams comp **t=68.44** (word "AI" @ 68.44) — `#F0F0F0`, 130px
- Sublabel: **`Top of mind — the frontrunners`** fades in @ **70.04** (word "mind" @ 70.04; "front runners" @ 72.84) — Inter 600, 26px, `#F0F0F0` (verified spoken: "top of mind for many … the front runners")
- **Cyan accent bar** (inset left, 4px) — `#00D4FF` (the single cyan element)
- **D4 (no-outro):** This is a CONTENT reveal of the thesis payoff, not a name/credit card — there is NO "Jasper De Maere · Wintermute" attribution (the original c7b5's name sublabel is REMOVED; review-style flagged it as a soft outro). The card's words land ON Jasper's spoken "privacy and AI," then it holds while he finishes "front runners … completely in that vertical or at least adjacent to it" through src 1595.84 / comp 80.84. Clip ends on this live content beat (no held credit card). The final ~1.5s (comp 80.84–85.0, "Yeah." @ 82.32) is the card gently settling over continuing speaker video — clean, not a static end screen.
- Cyan element: accent bar only.

---

## VERIFICATION CHECKLIST

- **Beat count in D-table range:** D-table says clip 7 = **6–7 beats**; final = **7**. PASS.
- **No two graphic templates identical in a row:** kinetic → swiss-grid → decision-tree → kinetic → [clean micro-gap] → kinetic → [clean] → liquid-glass. The two kinetics (c7b4, c7b5) are separated by a clean-video gap, so no two graphic beats of the same template render consecutively. PASS.
- **One cyan element per beat:** c7b1 line3 / c7b2 rule / c7b3 final node / c7b4 line3 / c7b5 line4 / c7b7 accent bar (c7b6 is clean video — no graphic). PASS.
- **Every non-editorial kinetic line has a real comp_t from clip7-words.txt:**
  - c7b1 — EDITORIAL (hook), marked.
  - c7b3 nodes 2/3/4 — verified (26.26 / 28.76 / 35.82); nodes 1 & 5 marked editorial lead-in/turn.
  - c7b4 — 35.82, 37.40, 44.54 — all verified from table.
  - c7b5 — 49.66, 50.70, 52.02, 53.02 — all verified from table.
  - c7b7 — 66.92, 68.44, 70.04 — all verified from table.
  PASS.
- **D7 palette/type:** "???" is `#F0F0F0` at ≥48px (fixes the original c7b3 `#888888` QA failure); date is **2026** not 2025; eyebrows Inter 700 ≥32px `#F0F0F0`; card has no blur/grain. PASS.
- **D4 no-outro:** clip ends on c7b7 content reveal over live speaker video; name-attribution sublabel removed. PASS.

**Build Manifest Row:** `clip_7 | clip-7-bear-market-exit | 1515 | 1600 | kinetic-type | 7 beats`
