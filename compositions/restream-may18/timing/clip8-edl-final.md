# CLIP 8 — AI MULTIPLIER · FINAL BUILD-READY EDL

**clip_id:** clip_8 · **dir:** `clip-8-ai-multiplier` · **src window:** 1675s–1845s · **duration:** 170s
**comp = src − 1675** (canonical). **Beat count: 13** (D-table range: "13, use _clip8-revised.md").
**Init template:** kinetic-type. **Palette:** charcoal `#0a0a0a` bg · cyan `#00D4FF` (one per beat) · text `#F0F0F0` · market red `#FF4D4F` / green `#16C784` · muted `#888888` only ≥48px.
**Type:** Inter — eyebrow 700 ≥32px, body/bullets ≥600, kinetic Black 900 ~130px.

Status vs. `_clip8-revised.md`: spec confirmed as-is. Every non-editorial kinetic line below was re-verified against `clip8-words.txt`. Source structure taken from `_original-edl.md` Clip 8; all of its comp numbers discarded.

---

## TEMPLATE SEQUENCE (no two identical in a row — VERIFIED)

`kinetic → clean → kinetic → swiss-grid → liquid-glass → clean → decision-tree → kinetic(editorial) → swiss-grid → decision-tree → kinetic → liquid-glass → clean`

Full-frame beats: c8b1, c8b3, c8b8, c8b11. All others Mode A.
D3 swaps applied: **c8b5** kept liquid-glass, reframed on Jasper as named subject (avoids a 5th kinetic). **c8b11/closer** = the verified BLUE WAVE kinetic; the name-card role moved to **c8b12** liquid-glass mid/late (NOT a held outro). D4: clip ends on **c8b13 clean video**, no card holding to end.

---

## OPENING PATTERN (D1 — copy clip-2-altcoin-options/index.html exactly)

- t=0.0–3.0s: video FULL-FRAME 1920×1080, BOTH speakers visible. Kinetic hook (3 lines) over left dark-gradient backdrop (`#bg-glow` region). This is c8b1.
- t≈3.0s: GSAP shrinks video to Mode A `{left:1229, top:108, width:614, height:864, borderRadius:6px, duration:0.7, ease:expo.inOut}`; `#bg-glow` fades in @3.3, `#zone-rule` draws @3.4, Ken-Burns scale 1.0→1.04 over ~115s from 3.5.
- "3+ element types before 6s" satisfied: hook kinetic (1) + swiss-grid index/eyebrow (2) + cyan rule draw (3) + two-column stat (4) all fire from c8b4 — but note c8b4 starts at 12s; the opening-density rule is satisfied within c8b1's hook (3 distinct kinetic lines + backdrop glow + rule) per D1. PASS.

GSAP full-frame⇄Mode A pattern for every transition: copy the masterTL.to(v,…) / `[gr,zr]` opacity tweens from clip-2.

---

## BEAT-BY-BEAT EDL

### c8b1 — OPENING HOOK (kinetic-type) · FULL-FRAME
- **comp:** 0.0–3.0s · **src:** 1675.0–1678.0s
- **template:** kinetic-type (hook) · **mode:** full-frame (both speakers) · **sub-comp:** `beat-c8b1-hook.html`
- **content / lines:**
  - Line 1 `ONE TRADER` — comp **0.08** — white `#F0F0F0`, 130px — `<!-- EDITORIAL: not word-synced (anticipatory hook) -->`
  - Line 2 `DOING THE WORK OF` — comp **0.88** — white `#F0F0F0`, 130px — `<!-- EDITORIAL -->`
  - Line 3 `2–3 ANALYSTS` — comp **1.60** — **cyan `#00D4FF`**, 130px — `<!-- EDITORIAL -->`
  - Exit all lines upward (power2.in) by ~2.7s.
- **cyan element:** Line 3 payoff only.
- **note:** Quantified core claim. Verified the claim is real in-window: "two" @ src 1682.00 / "three" @ src 1683.68 (clip8-words) — the hook pre-fires it editorially, same technique as clip 2/3.

### c8b2 — CLEAN VIDEO · Mode A
- **comp:** 3.0–5.0s · **src:** 1678.0–1680.0s
- **template:** clean video (no graphic) · **mode:** Mode A · **sub-comp:** — (handled in index.html master GSAP)
- **content:** none. 2s breath while video shrinks to Mode A and glow/rule settle. Jasper: "I can tell you that I think the work which I'm doing today…"
- **cyan element:** none (clean).

### c8b3 — WORK / TEAM (kinetic-type) · FULL-FRAME
- **comp:** 5.0–12.0s · **src:** 1680.0–1687.0s
- **template:** kinetic-type · **mode:** full-frame (both speakers) · **sub-comp:** `beat-c8b3-work-team.html`
- **content / lines** (phrase build, lines STAY — no dim):
  - Line 1 `REQUIRES A TEAM` — comp **5.64** (word "require" @ src 1680.64) — white `#F0F0F0`
  - Line 2 `OF TWO TO THREE` — comp **7.00** (word "two" @ src 1682.00) — white `#F0F0F0`
  - Line 3 `PEOPLE` — comp **8.90** (word "people" @ src 1683.90) — **cyan `#00D4FF`** payoff
- **cyan element:** Line 3 "PEOPLE".
- **data-start/data-duration:** start 5.0, duration 7.0 (covers 5.64→8.90 with ≥0.3s headroom each side; holds to ~11.8 then exits).
- **VERIFICATION:** all 3 lines word-synced to real comp_t from clip8-words.txt. Replaces original's "THE WORK @17.2 / REQUIRES A TEAM @18.0 / OF TWO TO THREE @20.0" which fired 12–15s LATE.

### c8b4 — AI PRODUCTIVITY (swiss-grid, two-column) · Mode A
- **comp:** 12.0–26.0s · **src:** 1687.0–1701.0s
- **template:** swiss-grid · **mode:** Mode A · **sub-comp:** `beat-c8b4-productivity.html`
- **content:**
  - Index `08` + eyebrow `AI PRODUCTIVITY · 5 YEARS AGO vs THIS YEAR` (Inter 700, 34px, `#F0F0F0`) — slam @ comp **12.06** (word "least" / settling of the "two to three people… to conduct the research" line @ src 1687.06).
  - Cyan horizontal rule draws @ **12.4** (scaleX 0→1) — **cyan `#00D4FF`** (the single cyan element; stat stays `#F0F0F0`).
  - LEFT column header `5 YEARS AGO` (48px, `#888888` permitted at this size) · value `2–3 ANALYSTS` (`#FF4D4F`).
  - RIGHT column header `THIS YEAR` (48px, `#888888`) · value `1 TRADER + AI` (`#16C784`).
  - Drawn `=` between columns (scaleX 0→1) @ **14.0**.
  - Footer `same research output` (`#F0F0F0`, ≥28px) @ **14.96** (word "And for me" @ src 1689.96).
- **cyan element:** the rule only (D7: swiss-grid = stat OR rule, not both → rule chosen; market red/green are indicators, not the accent).
- **note:** Date language obeys D7 (2026="this year", 2021/"5 years ago" relative). Real anchor: "five years ago" spoken @ src 1707.72 (comp 32.72) confirms the comparison is in-clip; the slam itself is editorial-paced on the productivity claim.

### c8b5 — JASPER · AI-AUGMENTED (liquid-glass card) · Mode A  [D3 SWAP: kept liquid-glass, reframed on Jasper]
- **comp:** 26.0–44.0s · **src:** 1701.0–1719.0s
- **template:** liquid-glass card · **mode:** Mode A · **sub-comp:** `beat-c8b5-jasper-research.html`
- **content** (rows stagger in 0.5s apart; named-subject framing per D3 c8b4-swap rationale):
  - Eyebrow / name `JASPER DE MAERE` (Inter 700, 34px, `#F0F0F0`) @ **28.20** (word "So" @ src 1703.20)
  - Role line `AI-AUGMENTED OTC TRADER` (`#F0F0F0`, ≥26px) @ **28.7**
  - Body row 1 `Research + trading — one person, simultaneously` @ **29.24** (word "I" @ src 1704.24)
  - Body row 2 `Analysis · data gathering · longer-duration graft work` @ ~**30.0** (anchored to "longer duration graft work", words @ src 1696.92–1698.74 spoken just prior; card elaborates)
- **cyan element:** 4px **cyan `#00D4FF`** left accent bar only.
- **card CSS:** `background:rgba(20,26,34,0.92)` + 4px cyan bar + soft glow + 1px border + `mask-image` feather. NO `backdrop-filter`. NO grain. (D7 / `_clip8-revised.md` recipe.)
- **note:** This is the named name-drop justification — Jasper as the subject doing the 2–3-analyst work. Avoids a 5th kinetic (D3 c8b4 swap intent).

### c8b6 — CLEAN VIDEO · Mode A
- **comp:** 44.0–56.0s · **src:** 1719.0–1731.0s
- **template:** clean video (no graphic) · **mode:** Mode A · **sub-comp:** —
- **content:** none. 12s substantive window — Jasper: "now you can do any trading application yourself with AI… completely revamping the whole trading experience." Earns the space (D6 8s-cap applies to clips <120s; this is 170s, and the original 18s window was already split into c8b5+c8b6+c8b7).
- **cyan element:** none (clean).

### c8b7 — RESEARCH→ALPHA PIPELINE (decision-tree) · Mode A
- **comp:** 56.0–76.0s · **src:** 1731.0–1751.0s
- **template:** decision-tree · **mode:** Mode A · **sub-comp:** `beat-c8b7-pipeline.html`
- **content** (4 nodes pop `back.out(1.5)` 0.4s apart; looping/flow arrows):
  - Eyebrow `TALK-TO-TERMINAL · UNIFIED TRADING UX` (Inter 700, 34px, `#F0F0F0`) @ **56.2**
  - Node 1 `[ State your market view ]` @ **56.52** (word "books" /"talk to a terminal" region, src 1731.52)
  - Node 2 `[ AI knows your profile ]` @ **72.12** (word "AI" @ src 1747.12 — "you talk with an AI, it knows your profile")
  - Node 3 `[ Routes the trade ]` @ **75.14** (word "route" @ src 1750.14)
  - Node 4 `[ Embedded in exchange + Paradigm ]` — **cyan `#00D4FF`** final node @ ~**67.74** is the product mention ("paradigm" @ src 1743.74); place as the terminal cyan node after Node 3 animates.
  - Sublabel `"Here is my view about the market" → executed trade` (`#F0F0F0`, ≥24px).
- **cyan element:** final node only.
- **note:** Nodes time to the spoken pipeline ("talk to a terminal… it knows your profile… it knows how to route your trade"). Final cyan node = the embedding/Paradigm product payoff. Pop-in cadence 0.4s; whole tree holds to ~75.6.

### c8b8 — NIGHT & DAY (kinetic-type) · FULL-FRAME · **EDITORIAL**
- **comp:** 76.0–96.0s · **src:** 1751.0–1771.0s
- **template:** kinetic-type · **mode:** full-frame (both speakers) · **sub-comp:** `beat-c8b8-night-day.html`
- **content / lines** (anticipatory callback — the literal "night and day difference" is spoken @ comp 29.88–31.10; replayed here as a designed echo while host asks the "thematics you're exploring?" question and Jasper opens on intent/front-end):
  - Line 1 `NIGHT AND DAY` — comp **76.5** — white `#F0F0F0` — `<!-- EDITORIAL: not word-synced (callback echo; literal line @ src 1704.88) -->`
  - Line 2 `DIFFERENCE` — comp **77.4** — white `#F0F0F0` — `<!-- EDITORIAL -->`
  - Line 3 `FROM 5 YEARS AGO` — comp **78.4** — **cyan `#00D4FF`** payoff — `<!-- EDITORIAL -->`
  - Exit upward by ~95.6; full-frame conversation window holds underneath until c8b9.
- **cyan element:** Line 3 payoff only.
- **note:** Listed as editorial in `_clip8-revised.md` ("Editorial beats … c8b8 night-day"). Per D2 it fires on chosen comp times, not words. The real "five years ago" anchor exists @ src 1707.96 (comp 32.96) — this beat is the late echo of it.

### c8b9 — INTENT-BASED TRADING (swiss-grid) · Mode A
- **comp:** 96.0–118.0s · **src:** 1771.0–1793.0s
- **template:** swiss-grid · **mode:** Mode A · **sub-comp:** `beat-c8b9-intent-agents.html`
- **content:**
  - Eyebrow `INTENT-BASED TRADING · BACK-END / MARKET INFRASTRUCTURE` (Inter 700, 34px, `#F0F0F0`) — slam @ comp **96.28** (word "us" @ src 1771.28 — "For us, where we would explore the AI…").
  - Stat `INTENT → RISK` (Inter 900, 200px, `#F0F0F0`).
  - Cyan horizontal rule draws @ **96.7** — **cyan `#00D4FF`** (rule is the single cyan; stat stays `#F0F0F0`).
  - Label `Quick law analysis · make/take fees · trade selection` (`#F0F0F0`, ≥26px) @ **103.04** (word "can we do quick law analysis" region, src 1778.04).
  - Sublabel `Biggest fit: analysis at the infrastructure layer` @ **117.68** (word "biggest" @ src 1792.68).
- **cyan element:** the rule only.
- **note:** Replaces original c8b8 "4 STEPS @107" (the "4 steps" framing was a fabricated count — the spoken content here is intent-based trading at the back-end/infra layer). All anchors verified in clip8-words.

### c8b10 — WHAT MAKES AGENTS VIABLE (decision-tree) · Mode A
- **comp:** 118.0–132.0s · **src:** 1793.0–1807.0s
- **template:** decision-tree · **mode:** Mode A · **sub-comp:** `beat-c8b10-agent-viable.html`
- **content** (3 nodes pop 0.4s apart):
  - Eyebrow `WHAT MAKES AGENTS VIABLE` (Inter 700, 34px, `#F0F0F0`) @ **119.12** (word "intent" @ src 1794.12 — "intent based trading… super interesting").
  - Node 1 `[ Lots of infrastructure ]` @ **122.30** (word "infrastructure" @ src 1797.30)
  - Node 2 `[ High-quality data ]` @ **124.52** (word "quality" @ src 1799.52 — "high quality data")
  - Node 3 `[ Agents express risk ]` — **cyan `#00D4FF`** final node @ **128.56** (word "express" @ src 1803.56 — "allow agents to express risk")
  - Sublabel `Infrastructure is the unlock` (`#F0F0F0`, ≥24px).
- **cyan element:** final node only.
- **note:** Nodes word-synced to the actual src 1793–1807 content ("you need a lot of infrastructure and high quality data… to allow agents to express risk"). This is the correct fill for the window the original EDL left broken.

### c8b11 — BLUE WAVE / SHORT OIL (kinetic-type) · FULL-FRAME  ★HIGHEST-PRIORITY TIMING FIX
- **comp:** 132.0–155.0s · **src:** 1807.0–1830.0s
- **template:** kinetic-type · **mode:** full-frame (both speakers) · **sub-comp:** `beat-c8b11-blue-wave.html`
- **content / lines** (phrase build, lines STAY):
  - Line 1 `BLUE WAVE` — comp **132.70** (word "blue" @ src 1807.70) — white `#F0F0F0`
  - Line 2 `STRAIT OF HORMUZ` — comp **136.44** (word "Strait" @ src 1811.44) — white `#F0F0F0`
  - Line 3 `SHORT OIL` — comp **140.68** (word "short" @ src 1815.68) — **cyan `#00D4FF`** payoff
  - Hold the full stack; underneath, Jasper continues "couple of industries you'd go long or short on… agent needs to control risk, understand your risk profile" through ~154. Exit upward ~154.4.
- **cyan element:** Line 3 "SHORT OIL".
- **data-start/data-duration:** start 132.0, duration 23.0 (covers 132.70→140.68 with headroom; stack persists as the dramatic in-clip example through the window).
- **VERIFICATION:** all 3 lines word-synced. This corrects the original's catastrophic placement at comp **86–106** (47s EARLY) — the single biggest error in the original EDL. "blue"@1807.70, "Strait"@1811.44, "short"@1815.68 all confirmed in clip8-words.txt.

### c8b12 — JASPER CLOSE (liquid-glass card) · Mode A  [D3 SWAP: c8b11 kinetic → liquid-glass; D4: NOT a held outro]
- **comp:** 155.0–168.0s · **src:** 1830.0–1843.0s
- **template:** liquid-glass card · **mode:** Mode A · **sub-comp:** `beat-c8b12-jasper-close.html`
- **content** (rows stagger 0.5s apart):
  - Eyebrow / name `JASPER DE MAERE` (Inter 700, 34px, `#F0F0F0`) @ **156.24** (word "profile" @ src 1831.24 — "understand your risk profile. So you require…")
  - Role `AI-AUGMENTED OTC TRADER` (`#F0F0F0`, ≥26px)
  - Body row 1 `Agents must control risk — beta, max drawdown` @ **159.60** (word "max" @ src 1834.60 — "beta draw, max drawdown")
  - Body row 2 `…across the entire investable universe` @ **164.18** (word "entire" @ src 1839.18)
- **cyan element:** 4px **cyan `#00D4FF`** left accent bar only.
- **card CSS:** same liquid-glass recipe as c8b5. NO blur. NO grain.
- **D4 note:** This name-card is placed MID/LATE on a natural risk-profile beat and EXITS (fade) at ~167.8 — it does NOT hold to clip end. The clip closes on clean video (c8b13), satisfying the no-outro rule.

### c8b13 — CLEAN VIDEO (close) · Mode A
- **comp:** 168.0–170.0s · **src:** 1843.0–1845.0s
- **template:** clean video (no graphic) · **mode:** Mode A · **sub-comp:** —
- **content:** none. Card has faded. Jasper: "I think it makes a lot of sense. I don't think we're that far off…" Clip ends cleanly on conversation — NOT a held card (D4). 2s clean tail.
- **cyan element:** none (clean).

---

## FINAL VERIFICATION CHECKLIST

- **Beat count:** 13 — matches D-table range for clip 8 ("13, use _clip8-revised.md"). PASS.
- **No two templates identical in a row:** kinetic→clean→kinetic→swiss-grid→liquid-glass→clean→decision-tree→kinetic→swiss-grid→decision-tree→kinetic→liquid-glass→clean. No adjacent repeat. PASS.
- **One cyan `#00D4FF` per beat:** c8b1 L3 · c8b3 L3 · c8b4 rule · c8b5 bar · c8b7 final node · c8b8 L3 · c8b9 rule · c8b10 final node · c8b11 L3 · c8b12 bar. (Clean beats c8b2/c8b6/c8b13 have none.) PASS.
- **Kinetic count:** c8b1(hook), c8b3, c8b8(editorial), c8b11 = 4 kinetics — within DESIGN.md 3–5 max. PASS (the original would have hit 5 had c8b4/c8b11 stayed kinetic; D3 swaps to liquid-glass keep it at 4).
- **Every non-editorial kinetic line has a real comp_t from clip8-words.txt:**
  - c8b3: 5.64 / 7.00 / 8.90 — verified.
  - c8b11: 132.70 / 136.44 / 140.68 — verified.
  - Editorial (chosen comp, marked in HTML): c8b1 (0.08/0.88/1.60), c8b8 (76.5/77.4/78.4). PASS.
- **Full-frame beats:** c8b1, c8b3, c8b8, c8b11 — both speakers visible (side-by-side source), so no "text on black." PASS.
- **D1 opening:** full-frame t=0 → Mode A @3.0, copied from clip-2. PASS.
- **D4 no-outro:** clip ends on c8b13 clean video; c8b12 card fades @~167.8. PASS.
- **D6 pacing:** original 18s clean window (orig c8b5) split into liquid-glass + 12s clean + decision-tree; longest clean window now 12s on a 170s clip. PASS.
- **D7 palette/type:** one cyan/beat; `#888888` only on 48px column headers; eyebrows Inter 700 ≥32px `#F0F0F0`; cards solid-fill no-blur no-grain; dates relative ("this year"/"5 years ago"). PASS.

## BUILD MANIFEST ROW
`clip_8 | clip-8-ai-multiplier | 1675 | 1845 | kinetic-type,swiss-grid,liquid-glass,decision-tree | 13 beats`
