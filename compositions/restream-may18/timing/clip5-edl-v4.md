# Clip 5 — Capital Rotation — EDL **v4** (BUILD-READY · supersedes v3)

**Slug:** `clip-5-capital-rotation` · **Source:** `clip-2-altcoin-options/source.mp4` (1920×1080 @ **30 fps**, side-by-side: Nic host LEFT, Jasper guest RIGHT)
**`src_in` = 1135.5** · **`src_out` = 1298.5** · **duration = 163.0 s** · **clip `comp = src − 1135.5`**

> **Two comp scales (do not confuse them).** The word table `timing/clip5-words.txt` lists `table_comp = src − 1120`. This clip starts at `src_in = 1135.5`, so **`clip_comp = table_comp − 15.5`**. Every fire-time below is given as **clip_comp** (what the builder uses) and the **table_comp** it was read off. **All fires re-verified against `audio.json`/`clip5-words.txt` on 2026-06-02** (the words table matches audio.json exactly — see §VERIFY). No fire is hand-computed.
>
> **⚠ table_comp ≠ clip_comp — the most common review mistake.** A word at table 18.08 ("equity") is at **clip_comp 2.58** (b1's window), NOT clip_comp 18.08. When picking a word to anchor a beat, read the **clip_comp** column relative to the beat's `data-start`, never the table_comp number directly. (This trap produced two off-by-15.5 suggestions in review; both are reconciled below.)

---

## What v4 fixes (the two rejections + the carried QA holes + the v4-review pass)

**The v3-built clip was REJECTED for two confirmed defects — both verified by frame extraction from `renders/clip-5-capital-rotation-HQ.mp4` on 2026-06-02:**

1. **R6 — on-screen index "05".** `grep '>05<'` returns 5 hits: `beat-c5b3`, `beat-c5b4`, `beat-c5b8`, `beat-c5b9`, `beat-c5b10`. Frame @t=17 shows "05" sitting above "CAPITAL ROTATION"; frame @t=122 shows "05" top-left over the chart. **v4 deletes the index element from ALL FIVE sub-comps (BY ID SELECTOR — §0a).** (b1,b2,b5,b6,b7,b11 never had one.)

2. **R7 — blank-left Mode-A (the clip-8 bug).** The v3 graphics are SHORTER than their Mode-A blocks, so the left zone goes EMPTY while Jasper stays cropped right. Confirmed by frame at three instants:
   - **t=35** (gap **33.0→38.9**, 5.9 s) — Jasper cropped right, left zone fully black. **BLANK-LEFT.**
   - **t=61** (gap **59.0→64.4**, 5.4 s) — same. **BLANK-LEFT.**
   - **t=140** (gap **137.5→143.4**, 5.9 s) — same. **BLANK-LEFT.**
   v4 kills all three by the **HOLD-UNTIL-SUCCESSOR** rule: inside a Mode-A block every graphic's `data-duration` is extended to BUTT against the next graphic's `data-start` (left zone never empties), and the **Mode-A→FULL toggle is moved to fire the instant the LAST graphic in the block clears** so the trailing breath is FULL-frame (both speakers), never cropped-with-empty-half. See the VIEW-TIMELINE + §0 BUILD-DELTA.

**Carried QA holes from the prior round (Agent-3 flagged the v3 build-delta was NOT executable) — v4 closes every one:**
- **Word-sync desync (was the biggest hole):** v3's §0 moved `data-start` but never re-derived the sub-comp internal GSAP offsets, so moving data-start shifted every fire by the delta. v4's §0 gives, for the ONE beat whose `data-start` moves, the **complete re-derived internal-offset table** (`offset = clip_comp − new_data_start`), and for every beat whose duration grows it gives a **Δ-proof** that no fire moves; it sets BOTH the `index.html` `data-duration` AND the sub-comp **template** `data-duration` to the same v4 value. Running §0 verbatim lands word-synced fires AND full-block holds.
- **b11 self-contradiction:** v4 sets toggle-4 @153.6 (FULL settles ~154.05) AND b11 `data-start` 153.6 with **L1 offset 0.92** (→ clip_comp 154.52, AFTER the expand) — they now agree.
- **b4 168px overflow:** the stat is **stacked `ALL-TIME` / `▲ HIGH` at 150px** (fits the zone, no wrap; up-arrow gives the slam motion-meaning) — spec'd in §0e and the beat.
- **b9 clutter:** collapsed to **ONE inline `2021 → NOW` anchor** and the equity line drawn at **0.6 reference-opacity** (cyan convergence stays the only accent) — spec'd in §0e and the beat.
- **Verify-by-frame instants** updated for the new holds/toggle (§9).

**v4-review pass (Agent-2, 2026-06-02) — applied in this revision:**
- **[b9 word-sync, was off-by-one] FIXED.** v3-of-v4 pinned the crypto down-draw to clip_comp 135.12 = table 150.62 = **"volatility"** (~1.3 s early) and the convergence callout to "compressed." Now the **down-draw lands on "compressed"** (table 151.94 → clip_comp **136.44**, offset 15.44) and the **convergence callout fires on the breath after** (table 152.88 "to" → clip_comp **137.38**, offset 16.38). See §0e + b9.
- **[b9 chart motion] STAGGERED.** Equity (green) line and crypto (red) line now draw in **overlapping windows** so the convergence reads as one continuous closing motion, not two disconnected bursts with a dead middle. See §0e + b9.
- **[b8 38-s dwell] MID-BEAT REFRESH added.** A deterministic connector-pulse + node-3 single breathe fires ~clip_comp 110.12 ("benchmark") so the 26-s tail isn't a frozen graphic. See §0e + b8. (This is the chosen relief for the 70-s Phase-3 Mode-A stretch — NO new FULL toggle, to avoid A-B-A risk; see VIEW-TIMELINE note.)
- **[b6→b7 Q/A payoff] HOLD QUESTION.** b6's question text now HOLDS on screen (no exit) until b7's "NO —" slams @70.18 — the question is still readable when the answer lands. Still FULL the whole time (R7-safe). See b6.
- **[b3 hook] WORD-LOCKED.** b3's rotation arrow now fires on a word **actually spoken in b3's clip_comp window** ("evidence," table 33.22 → clip_comp 17.72) instead of pure chrome. (The reviewer's "fire on 'equity' 18.08" was a table/clip mixup — "equity" 18.08 is clip_comp 2.58, inside b1; corrected to a real in-window word.) See b3.
- **[b4 slam] MOTION-MEANING.** No number exists in the transcript for "all-time high," so the slam gets an **up-arrow ▲** glyph beside "HIGH" to read as directional, not a flat label. See §0e + b4.
- **[b1 hook] TIGHTENED to fully-spoken.** L1 changed "RETAIL PIVOTED" → **"PIVOTED"** so all three lines are words actually heard in-clip (pivoted/aggressively/equity at clip_comp 0.34/1.60/2.58). The inferred "RETAIL" is dropped. Offsets unchanged. See b1.
- **[b10 footer] DE-DUP.** Footer "PROFILES NOW EQUAL" → **"NOW EQUAL"** so "profile" isn't the 3rd profile-word in the 70-s Mode-A block (b9 eyebrow "VOLATILITY PROFILE" + b10). See b10.
- **[b7 L2→L3 gap] JUSTIFIED.** The 7.7-s gap (L2 @87.10 → L3 @94.80) is real intermediate speech ("…the people who've been in crypto **since 21**"); L2 "NOT FOR THE OG HOLDERS" glosses "the people who've been in crypto," L3 lands on the spoken "since 21." A 4th hold-line is added so the stack isn't two-then-wait-then-one. See b7.
- **[§0a id-based] DONE.** §0a deletes by `#id` selector, order-independent (line numbers shift once §0e is applied). See §0a.
- **[index.html VIEW-TIMELINE comment] REWRITE instruction added.** §0f rewrites the stale v3 comment block so index.html doesn't self-contradict the v4 timeline. See §0f.

**Kept from v3 (it works — do NOT regress):** dialog-matched open ("pivoted very aggressively into equity", spoken clip_comp 0.34–2.58), `object-position: 83% center` framing centering Jasper, the DISTINCT device (before→after rotation card + two-series vol-profile chart), ≤2 kinetics in a row, one cyan per beat, cards `rgba(20,26,34,0.92)` + 4px inset cyan bar + glow + mask feather (no blur, no grain), `#B6BEC6`/`#888`-free.

---

## §0 — BUILD-DELTA (the literal diff to apply to the v3-built files)

> This is the exact, verbatim edit set. Apply ALL of it; running it lands a clip that passes the gate. **Apply §0e (content edits) and §0a (id deletes) in any order — both are id-based, not line-based.** Every duration change is set in **two places** (`index.html` data-duration AND the sub-comp `<div data-composition-id=…>` template data-duration) so the held graphic actually renders for its full length — the R7 hold is otherwise unverified (the v3 templates still carried short v3 durations).

### §0a — R6: delete the on-screen index from all 5 offending sub-comps (BY ID SELECTOR — order-independent)
In each file delete the element **by its id**, its CSS rule block (keyed on the same id), and its GSAP tween line (keyed on the same id selector). **Do NOT delete by line number** — §0e shifts the line numbers in b4 (stat restructure) and b9 (axis collapse), so any "delete L20"/"delete L22" instruction is stale once §0e is applied. Match on the id text instead:

| file | delete element | delete CSS rule | delete GSAP tween |
|---|---|---|---|
| `beat-c5b3-rotation-card.html` | `<div id="c5b3-idx">05</div>` | the `#c5b3-idx { … }` rule block | the `tl.fromTo("#c5b3-idx", …)` line |
| `beat-c5b4-jpm-all-time-high.html` | `<div id="c5b4-idx">05</div>` | the `#c5b4-idx { … }` rule block | the `tl.fromTo("#c5b4-idx", …)` line |
| `beat-c5b8-exuberance-flow.html` | `<div id="c5b8-idx">05</div>` | the `#c5b8-idx { … }` rule block | the `tl.fromTo("#c5b8-idx", …)` line |
| `beat-c5b9-vol-profile-chart.html` | `<div id="c5b9-idx">05</div>` | the `#c5b9-idx { … }` rule block | the `tl.fromTo("#c5b9-idx", …)` line |
| `beat-c5b10-vol-comparison.html` | `<div id="c5b10-idx">05</div>` | the `#c5b10-idx { … }` rule block | the `tl.fromTo("#c5b10-idx", …)` line |

After this edit, `grep -rn '>05<' clip-5-capital-rotation/` MUST return **0 hits.** (The eyebrow editorial labels — `CAPITAL ROTATION`, `VOLATILITY PROFILE`, etc. — stay; only the bare number dies.) **Note:** each id appears in exactly three places (the element, its CSS rule, its one tween) — grep the id within the file to confirm 3 hits before deleting and 0 after.

### §0b — R7: hold-until-successor durations (set in BOTH places) + 2 moved toggles

| beat | `index.html` data-start | OLD dur | **NEW data-duration (set in index.html AND template `<div>`)** | why |
|---|---:|---:|---:|---|
| b3 | 15.5 | 4.9 | **5.0** | hold until b4 lands @20.5 (no blank between b3→b4) |
| b4 | 20.5 | 12.5 | **18.4** | content done ~32.1 but **HOLD to 38.9** (kills the 33.0→38.9 blank-left); b5 lands @38.9 |
| b5 | 38.9 | 20.1 | **24.7** | content done ~59.0 but **HOLD to 63.6** (kills the 59.0→64.4 blank-left); FULL toggle @63.6. **b5 has NO exit tween — the hold is real (see note below).** |
| b8 | 83.0 | 38.0 | **38.0** *(unchanged — already butts b9 @121.0)* | already holds the whole sub-block (mid-beat refresh @110.12 keeps the tail alive — §0e) |
| b9 | 121.0 | 16.5 | **22.4** | content done ~137.4 but **HOLD to 143.4** (kills the 137.5→143.4 blank-left); b10 lands @143.4 |
| b10 | 143.4 | 10.8 | **10.2** | content done ~148.6, **HOLD to 153.6** (FULL toggle); last Mode-A graphic |
| b11 | **153.6** *(was 154.3)* | 7.4 | **8.1** | closer; see §0c for the re-derived offsets (this is the only `data-start` move) |

**Template-side reconciliation (the load-bearing half of the R7 fix):** the v3 sub-comp `<div data-composition-id="…" … data-duration="X">` lines still carry the OLD durations (b3=4.9, b4=12.5, b5=20.1, b9=16.5, b10=10.8; b8=38.0 already correct). For each row above, **also edit the template `<div>` data-duration to the NEW value** so the inner template length does not clip the held graphic early. **b5 specifically:** the `beat-c5b5-wintermute-weekly-quote.html` template `<div … data-duration="20.1">` → **`data-duration="24.7"`**. If the builder confirms `index.html`'s outer data-duration authoritatively overrides the inner template length in this engine, the template edit is belt-and-suspenders; set both regardless to remove the ambiguity.

> **b5 hold is genuine — do NOT add an exit tween.** The b5 template currently has **no stack-exit / card-out tween** (the card slides in @38.96 and never animates out — verified in the file). The hold to 63.6 is therefore real. **Do NOT, by analogy with the kinetic stacks (which drift out), add a b5 card-out** — that would reintroduce the blank-left. The b5 attribution `— Jasper De Maere` fades IN @58.6 and STAYS; nothing in b5 fades out before the 63.6 toggle.

**Two `index.html` GSAP master-toggle moves** (so Mode-A ends exactly when the block's last graphic clears → trailing breath is FULL, not blank Mode-A):

| toggle | v3 fired @ | **v4 fires @** | effect |
|---|---:|---:|---|
| **TOGGLE 2** (Mode-A→FULL, end of Phase 1) | 64.4 (glow-fade @64.2) | **63.6** (glow-fade @63.4) | expands to FULL the instant b5 clears; FULL breath 63.6→64.9 before b6 host-Q @64.94 — no blank-left |
| **TOGGLE 4** (Mode-A→FULL, end of Phase 3) | 154.0 (glow-fade @153.8) | **153.6** (glow-fade @153.4) | expands to FULL the instant b10 clears; **settles ~154.05 BEFORE b11 L1 @154.52** (fixes the v3 mid-expand bug) |

TOGGLE 1 (15.0) and TOGGLE 3 (83.2) are UNCHANGED. (TOGGLE 3 stays at 83.2 — v3 already moved it from 83.6 so the b8 eyebrow @83.30 is not over a stable FULL frame; keep it.)

### §0c — re-derived INTERNAL GSAP offsets for the ONE beat whose `data-start` moved (b11)

b11 `data-start` moves **154.3 → 153.6** (Δ = −0.7). Absolute fire = `data-start + offset`, so **every b11 offset must increase by +0.7** to keep the same clip_comp (this is exactly the desync hole that sank the v3 delta — re-derive, do not just move data-start). Rewrite the b11 `<script>` tweens to:

| line | clip_comp (unchanged) | table_comp | OLD offset | **NEW offset** |
|---|---:|---:|---:|---:|
| L1 `THEY JUST WANT` | 154.52 | 170.02 | 0.30 | **0.92** |
| L2 `A VOLATILITY TRADE` | 156.68 | 172.18 | 2.38 | **3.08** |
| L3 `EQUITY OFFERS IT` *CYAN | 160.66 | 176.16 | 6.36 | **7.06** |
| stack exit (drift up/out) | 161.7 | — | 7.4 | **8.1** |

> Verify: 153.6 + 0.92 = **154.52** ✓ (after the 154.05 expand-settle — no mid-expand text). 153.6 + 8.1 = 161.7 ✓ then clean FULL to 163.0.

### §0d — beats whose `data-start` is UNCHANGED → DO NOT touch their internal offsets (Δ proof)

b3, b4, b5, b9, b10 keep their v3 `data-start`; only their `data-duration` GROWS (§0b). Growing a duration does **not** move any fire (fires are `data-start + offset`), so their internal GSAP offsets are **left exactly as-is** — EXCEPT the explicit content edits in §0e (b3 arrow re-key, b4 stat, b8 refresh, b9 swap+stagger, b10 footer text), which are spelled out per-beat. b1, b2, b6, b7 are untouched on timing except the noted text/hold edits (b1 L1 text only; b6 hold only — neither moves a fire-time).

| beat | data-start v3=v4 | every internal fire absolute clip_comp | offsets change? |
|---|---:|---|:--:|
| b1 | −0.2 | L1 0.34 / L2 1.60 / L3 2.58 / exit 3.4 | none (L1 **text** "RETAIL PIVOTED"→"PIVOTED" only; offset 0.54 unchanged) |
| b2 | 12.0 | L1 12.30 / L2 13.66 / L3 14.62 / exit 14.9 | none |
| b3 | 15.5 | eyebrow 15.9 / rule 16.3 / from-state 17.0 / **arrow+to-state 17.72 (re-keyed §0e)** / chips 18.8 / footer 19.6 | **arrow only — §0e** |
| b4 | 20.5 | eyebrow 20.88 / stat 28.34 / footer 29.38 / sublabel 31.70 | none (stat **glyph+layout** only — §0e) |
| b5 | 38.9 | card 38.96 / eyebrow 40.34 / quote 54.50 / "not crypto" 57.94 / attrib 58.6 | none |
| b6 | 64.6 | L1 64.94 / L2 65.78 | none (**hold-to-70.18** added — no fire moves; §b6) |
| b7 | 69.9 | L1 70.18 / L2 71.60 / **L2b hold 88.42** / L3 79.30→ see §b7 | **L2b added — §b7** |
| b8 | 83.0 | eyebrow 83.30 / n1 84.66 / n2 89.50 / n3 91.92 / annot 94.62 / **refresh 110.12 (new §0e)** | **refresh added — §0e** |
| b9 | 121.0 | x-anchor 122.0 / legend 122.5 / eyebrow 123.52 / **equity-draw start 124.4 / crypto-down start 127.8 / crypto-down lands 136.44 / converge 137.38** (re-staggered + swapped §0e) | **YES — §0e** |
| b10 | 143.4 | eyebrow 143.5 / colR 143.98 / divider 144.4 / footer 147.20 | none (footer **text** "PROFILES NOW EQUAL"→"NOW EQUAL" only — §0e) |
| b11 | **153.6** | see §0c (+0.7 each) | **YES — §0c** |

### §0e — content edits (clutter, slam motion, chart sync — all required, not just timing)

- **b4 stat overflow + flat-slam (168px wraps the ~1152px zone; "ALL-TIME HIGH" reads as a label):** in `beat-c5b4-jpm-all-time-high.html` change `.c5b4-stat` to two stacked lines, `font-size: 168px → 150px`, and add a directional **▲** glyph beside HIGH so the slam carries motion-meaning (no number exists in transcript):
  ```
  <div id="c5b4-stat" class="c5b4-stat"><span>ALL-TIME</span><span>HIGH&nbsp;<i class="c5b4-up">▲</i></span></div>
  .c5b4-stat { font-size:150px; line-height:0.92; display:flex; flex-direction:column; }
  .c5b4-up  { font-style:normal; font-size:0.62em; color:#16C784; }   /* directional up = market indicator, not the cyan accent */
  ```
  (150px stacked reads as the big slam without clipping; the ▲ makes it directional. Verify-by-frame @comp 30: no wrap, no right-edge clip, arrow visible.)
- **b9 axis clutter + word-sync swap + draw stagger (the marquee chart):** in `beat-c5b9-vol-profile-chart.html`:
  - **axis:** collapse `.c5b9-xrow` (two spans "2021"/"NOW") to a **single inline anchor** `<div class="c5b9-xanchor">2021 → NOW</div>` (one element, left-aligned under the chart; remove `justify-content:space-between`).
  - **equity opacity:** add `#c5b9-equity { opacity: 0.6; }` (keep green `#16C784`; the crypto-red descending line + the cyan convergence remain the read). Drop the legend "EQUITIES" swatch fill to 0.6 to match.
  - **WORD-SYNC SWAP (was off-by-one, ~1.3 s early):** the crypto down-draw was keyed to clip_comp 135.12 = table 150.62 = **"volatility"**; re-key it to land on **"compressed"** = table **151.94** → clip_comp **136.44** (offset 15.44 off data-start 121.0). Re-key the convergence callout from "compressed" to the **breath after** = table **152.88 "to"** → clip_comp **137.38** (offset 16.38). So: down-move lands on the word "compressed," convergence lands on the natural pause right after.
  - **DRAW STAGGER (was two disconnected bursts):** start the **crypto (red) descent at offset ~6.8 (clip_comp ~127.8)** and run it ~8.0 s so it is still drawing when it lands its low at 136.44 — overlapping the equity (green) line's draw (which starts offset 3.4 / clip_comp 124.4 over ~5.0 s) so the two series visibly close on each other as ONE converging motion rather than green-finishes-then-5s-dead-then-red-starts. Convergence dot/callout pops at 137.38 at the crossing.
  - Net: ONE cyan accent (convergence) + red (full) + green (0.6 ref) + one inline "2021 → NOW" + 2-item legend. De-cluttered. ✓
- **b8 38-s dwell — mid-beat refresh (26-s tail was a frozen graphic):** in `beat-c5b8-exuberance-flow.html`, after the annotation @94.62, add a **deterministic single refresh** keyed to the spoken word "benchmark": at **clip_comp 110.12** (table 110.12, offset 27.12 off data-start 83.0) the **3 connectors pulse-draw once** (0.8 s) and **node-3's cyan glow does ONE 0.8-s breathe** (scale 1.0→1.04→1.0, opacity pulse). No `repeat:-1`, no randomness — a single deterministic accent so the 110→121 tail is alive, not frozen. All nodes/text STAY (no exit). This is the chosen relief for the long Phase-3 Mode-A run — NOT a new FULL toggle (see VIEW-TIMELINE note on why a toggle here would create A-B-A risk).
- **b10 footer de-dup ("profile" appears 3× in the 70-s Mode-A block):** in `beat-c5b10-vol-comparison.html` change the footer text **`PROFILES NOW EQUAL` → `NOW EQUAL`** (fire-time unchanged @147.20). "Profile" already appears in b9's eyebrow "VOLATILITY PROFILE"; dropping it from b10 keeps the block from reading repetitive. (b9's callout already reads "THEY CONVERGED" not "PROFILES CONVERGED" — same discipline.)
- **b3 arrow word-lock (give the spine device a real spoken beat, not pure chrome):** in `beat-c5b3-rotation-card.html` re-key the **arrow `↓` + to-state `EQUITIES`** entry from its editorial-build timing to land on a word **actually spoken in b3's window**: **clip_comp 17.72** (table 33.22 = "evidence," when Nic says "empirical **evidence** that retail is there" — the rotation-confirmation moment), offset **2.22** off data-start 15.5. (The other b3 elements — eyebrow, rule, from-state, chips, footer — stay editorial-timed; only the arrow/to-state gets the word-lock.) **Why not the reviewer's "equity" 18.08:** that word is at **clip_comp 2.58** (b1's window), not clip_comp 18.08 — using it would desync b3 by 15.5 s. "evidence" (clip_comp 17.72) is the in-window anchor.

> After §0e, b9 carries: red crypto line (full) + green equity line (0.6 ref) + ONE cyan convergence dot/callout + one inline "2021 → NOW" + a 2-item legend, with the two lines drawing toward each other in overlapping windows and the down-move landing on "compressed." One cyan only. ✓

### §0f — rewrite the stale index.html VIEW-TIMELINE comment (so the file doesn't self-contradict v4)

The `index.html` VIEW-TIMELINE comment block still describes the **OLD v3 phases** ("15.5–64.9," "84.1–154.6," "smallest sustained phase = 8.4 s"). **Replace that comment block with the v4 timeline** so the next QA agent reading index.html grades against the right numbers:
```
VIEW-TIMELINE (v4): FULL 0.0–15.5 (b1,b2) → Mode-A 15.5–63.6 (b3⊐b4⊐b5) →
FULL 63.6–84.1 (breath,b6,b7) → Mode-A 84.1–153.6 (b8⊐b9⊐b10) → FULL 153.6–163.0 (b11).
Toggles @15.0 / 63.6 / 83.2 / 153.6. Smallest sustained phase = 9.4 s (closer).
Every Mode-A second has a graphic (hold-until-successor); every breath is FULL-frame.
```
Also update any inline duration comments next to the b3/b4/b5/b9/b10 `<div>`s if they annotate the OLD durations.

---

## VIEW-TIMELINE (proves R1 + R7 — EVERY Mode-A second names the graphic that fills it; no segment is graphic-less)

`object-position: 83% center`; Mode-A box `{left:1229, top:108, width:614, height:864}` (clip-2 proven; **re-verified by frame @t=17/35/61/122/140 on the v3 render — Jasper centered, "Jasper De Maere / Wintermute" lower-third fully in-frame, no host bleed**).

| phase | view | dwell | clip_comp | beats | **what fills the LEFT zone for the ENTIRE phase (R7)** |
|---|---|---:|---|---|---|
| **0.0–15.5** | **FULL** (both speakers) | **15.5 s** | 0.0–15.5 | b1, b2 | kinetic word stacks over both speakers (dark left-gradient). No crop → blank impossible. |
| **15.5–63.6** | **Mode-A** (Jasper R, graphic L) | **48.1 s** | 15.5–63.6 | b3, b4, b5 | **b3** rotation card 15.5→20.5 **→ b4** JPM stat 20.5→38.9 **→ b5** Wintermute quote 38.9→63.6. Each butts the next; **a graphic occupies the left zone at every instant.** |
| **63.6–84.1** | **FULL** (both speakers) | **20.5 s** | 63.6–84.1 | (breath) b6, b7 | FULL breath 63.6→64.9, then host-Q kinetic (HOLDS to b7) + Jasper-answer kinetic over both speakers. No crop → no blank. |
| **84.1–153.6** | **Mode-A** (Jasper R, graphic L) | **69.5 s** | 84.1–153.6 | b8, b9, b10 | **b8** exuberance flow 83.2→121.0 (refresh @110.12) **→ b9** vol-profile chart 121.0→143.4 **→ b10** vol comparison 143.4→153.6. Each butts the next; **a graphic occupies the left zone at every instant.** |
| **153.6–163.0** | **FULL** (both speakers) | **9.4 s** | 153.6–163.0 | b11 | FULL settles ~154.05, closer kinetic 154.52→161.7, then clean FULL both-speakers to 163.0 (D4 no-outro). |

**R7 audit — NO graphic-less Mode-A instant exists:**
- Phase-1 Mode-A graphic coverage 15.5→63.6 continuous (b3⊐b4⊐b5, butting). The v3 holes 33.0→38.9 and 59.0→64.4 are FILLED (b4 holds to 38.9; b5 holds to 63.6 and the toggle expands @63.6). ✓
- Phase-3 Mode-A graphic coverage 84.1→153.6 continuous (b8⊐b9⊐b10, butting). The v3 hole 137.5→143.4 is FILLED (b9 holds to 143.4). b8's 110→121 tail is kept alive by the §0e refresh (not blank — it was never blank, but now not frozen either). ✓
- Every clean/breath moment (63.6–64.9, 153.6–154.05, 161.7–163.0) is **FULL-frame both-speakers**, never cropped. ✓

**R1 checks — ALL PASS:**
- **No segment < 8 s** outside the 0–6 s intro. Smallest sustained phase = **9.4 s** (closer). ✓
- **No A-B-A within 12 s.** Same-view return gaps: FULL left@15.5→return@63.6 = **48 s**; Mode-A left@63.6→return@84.1 = **20.5 s**; FULL left@84.1→return@153.6 = **69.5 s**. All ≫12 s. ✓
- **Consecutive graphic beats grouped:** each Mode-A phase carries 3 graphics back-to-back (one stable frame); each FULL phase carries the intro pair / the Q-A pair. ✓
- **One-liner:** `FULL 15.5s → Mode-A 48.1s → FULL 20.5s → Mode-A 69.5s → FULL 9.4s` — 5 phases, all ≥9.4 s, every A-B-A gap ≥20 s.

> **Phase-3 is 69.5 s of Mode-A (one framing) — deliberate, not an oversight.** Inserting a FULL micro-breath between b8/b9 or b9/b10 would (a) need to be ≥8 s to satisfy R1's min-dwell and (b) create A-B-A risk (FULL→Mode-A→FULL→Mode-A inside Phase 3). The safer relief is the **§0e b8 mid-beat refresh** (connector pulse + node-3 breathe @110.12), which adds motion without a view switch. The build agent should NOT add a Phase-3 toggle.

### Master-timeline mode toggles (`index.html` GSAP) — only 4 switches in 163 s
| clip_comp | action | v3→v4 |
|---|---|---|
| 0.0 | FULL (CSS default; both speakers; b1 over dark left-gradient) | — |
| **15.0** | FULL → **Mode-A** (cinematic shrink to MODE_A, expo.inOut 0.5 s) as b3 builds | unchanged |
| **63.6** | **Mode-A → FULL** (expand; glow/zone-rule fade @63.4) — b5 just cleared; FULL breath then b6 host-Q @64.94 | **64.4 → 63.6** |
| **83.2** | FULL → **Mode-A** (shrink) for b8 flow; eyebrow @83.30 over the settling shrink | unchanged |
| **153.6** | **Mode-A → FULL** (expand; glow fade @153.4) — b10 cleared; **settles ~154.05 before b11 L1 @154.52** | **154.0 → 153.6** |
| 161.7 | b11 lines drift out; **video holds FULL clean** to 163.0 (no outro — D4) | offsets +0.7 |

Ken-Burns on the video element: deterministic `scale 1.0 → 1.04` across the full 163 s (no `Math.random`, no `repeat:-1`) — **unchanged from v3.**

---

## Speaker framing — `object-position: 83% center` (VERIFIED by frame)
**Mode-A box:** `left:1229, top:108, width:614, height:864` (≈85 % of the right-40 % zone), `object-fit:cover`, `object-position: 83% center`, vertical center (no bias, no scale-up). Source is side-by-side (Nic L, Jasper R, seam ≈ x960); the 83 % crop shows source x≈957–1725 → **Jasper's face dead-centre, his "Jasper De Maere / Wintermute" name lower-third fully in-frame, no host bleed, no dead ceiling.** Confirmed against the v3 render frames @t=17/35/61/122/140 (the crop itself is correct — only the left zone was blank, which v4 fixes). **Builder re-extracts the rendered Mode-A frame and LOOKS before claiming done (QA §5/§9).** Opening + Q/A + closer FULL phases show BOTH speakers (never text on black). **No change to the framing in v4.**

---

## Template variety (proves R2) — the distinct device LEADS

**Sequence:** `kinetic → kinetic → ROTATION-CARD → swiss → glass → kinetic → kinetic → flowchart → DATA-CHART → swiss → kinetic`

- **Max kinetics in a row = 2** (intro pair b1-b2; Q/A pair b6-b7). No 3+ run. ✓
- **DISTINCT PRIMARY device (DESIGN.md = "before/after rotation + `data-chart` vol profile"):** **b3 rotation before→after card** (CRYPTO/ALTCOINS struck → EQUITIES + dwindle timeline, arrow word-locked to "evidence") and **b9 two-series vol-profile chart** (crypto vol ↓ vs equity vol ↑ converging, lines staggered to close as one motion). These are the spine; kinetics support. ✓
- Kinetic share 5/11; chart/comparison beats are NOT inited from kinetic-type. ✓

### Devices — already hand-built as DISTINCT dark equivalents (keep; do not regress)
| beat | device | status |
|---|---|---|
| b8 exuberance flow | 3-node causal chain | hand-built dark vertical node-chain + SVG connector draw (the catalog `flowchart` block is a white-bg "learn-to-code" tree — wrong skin). **Keep; add mid-beat refresh §0e.** |
| b9 vol-profile | two-series converging line chart | hand-built dark SVG, two series via `strokeDashoffset`, cyan convergence (the catalog `data-chart` block is cream + serif — wrong skin). **Keep; apply §0e simplification + stagger + word-swap.** |
| b3 rotation card | bespoke before→after | hand-built. **Keep; arrow word-locked §0e.** |
| b4, b10 | swiss-grid stat / two-col | hand-built. **Keep; b4 stat stacked 150px + ▲ per §0e; b10 footer "NOW EQUAL" §0e.** |
| b5 | liquid-glass card | hand-built. **Keep; duration 24.7, no exit tween.** |
| b1,b2,b6,b7,b11 | kinetic word-stack | phrase-build-and-STAY (no dim). **Keep.** |

---

## BEAT TABLE

Per beat: **id · clip_comp range · src range · view · template · sub-comp · data-start/data-duration · full on-screen text (jargon-correct) · per-kinetic-line `clip_comp` + matched spoken words + internal offset.** `*CYAN` = the single cyan `#00D4FF` element. `[EDITORIAL]` = chrome / anticipatory (not word-synced). **No beat renders an index number (R6).** Eyebrows Inter 700 ≥32px `#F0F0F0`; body/bullets Inter ≥600; payoff/slam ~130px. Muted secondary `#B6BEC6` (never `#888`).

---

### b1 — OPENING KINETIC · *the dialog-matched open* (kinetic-type)
- **clip_comp** 0.0–4.6 | **src** 1135.5–1140.1 | **view** FULL (both speakers; dark left-gradient backdrop) | **data-start** `-0.2` **data-duration** `5.2` *(unchanged)*
- **sub-comp** `compositions/beat-c5b1-pivoted-into-equity.html`
- **template** kinetic 3-phrase build (~130px Inter 900), lines slam in and **STAY (no dim)**, over full-frame video. First text by clip_comp ≈0.34.
- **On-screen lines + word-sync** (R5 complete thought; **all three words are spoken in-clip** — the inferred "RETAIL" is dropped per v4-review item 13 so the hook is fully word-locked):
  - **L1 `PIVOTED`** — fire **clip_comp 0.34** ← "pivoted" (table 15.84). offset 0.54. *(was "RETAIL PIVOTED"; "RETAIL" was carried from src 1125.56 before src_in and never heard in-clip — dropped. Only the text changes; the offset is identical.)*
  - **L2 `VERY AGGRESSIVELY`** — fire **clip_comp 1.60** ← "aggressively" (table 17.10). offset 1.80.
  - **L3 `INTO EQUITY` *CYAN** — fire **clip_comp 2.58** ← "equity" (table 18.08). offset 2.78.
- **Exit:** stack drifts up/out @ ~3.4; FULL view persists 0.0–15.5 across b1+b2 (one grouped phase). audio.json-verified.
- **R4 audit:** {pivoted} / {very, aggressively} / {into, equity} — no repeat. ✓

### b2 — KINETIC "altcoin season into equities" (kinetic-type)
- **clip_comp** 12.3–14.9 | **src** 1147.8–1150.4 | **view** FULL | **data-start** `12.0` **data-duration** `3.4` *(unchanged)*
- **sub-comp** `compositions/beat-c5b2-altcoin-season.html`
- **On-screen lines + word-sync:**
  - **L1 `ALTCOIN SEASON`** — fire **clip_comp 12.30** ← "altcoin" (table 27.80) / "season" (table 28.14). offset 0.30.
  - **L2 `IS NOW HAPPENING`** — fire **clip_comp 13.66** ← "now" (table 29.16) / "happening" (table 29.34). offset 1.66.
  - **L3 `IN EQUITIES` *CYAN** — fire **clip_comp 14.62** ← "equities" (table 30.12). offset 2.62.
- **Exit:** drifts out @ ~14.9; **video shrinks FULL→Mode-A @15.0** for b3.
- **R4 audit:** {altcoin, season} / {now, happening} / {equities} — no repeat. ✓

### b3 — ROTATION before→after CARD · *distinct PRIMARY device pt1* (HAND-BUILD)
- **clip_comp** 15.5–20.5 | **src** 1151.0–1156.0 | **view** Mode-A | **data-start** `15.5` **data-duration** `5.0` *(was 4.9 — **HOLD to 20.5 so b4 butts it; no blank**; set in index.html + template)*
- **sub-comp** `compositions/beat-c5b3-rotation-card.html` — **DELETE the `05` index (§0a); RE-KEY the arrow to "evidence" (§0e).**
- **template** bespoke before→after panel in the LEFT zone (feathered `mask-image`, no blur, no grain): eyebrow + cyan rule (chrome), THEN the before→after motif — `CRYPTO / ALTCOINS` (struck, 0.45, white, red strike) → down-arrow `↓` → `EQUITIES` (white) → 4-chip dwindle timeline `NOV · DEC · JAN · FEB`.
- **Full on-screen text** (NO index — R6):
  - eyebrow **`CAPITAL ROTATION`** (Inter 700, 32px, #F0F0F0) `[EDITORIAL]` @15.9 (offset 0.40)
  - cyan rule draws L→R **`*CYAN`** `[EDITORIAL]` @16.3 (offset 0.80)
  - from-state **`CRYPTO / ALTCOINS`** (struck, 0.45) `[EDITORIAL build]` @17.0 (offset 1.50)
  - **arrow `↓` + to-state `EQUITIES`** (#F0F0F0) — **WORD-LOCKED fire clip_comp 17.72** ← "evidence" (table 33.22, "empirical **evidence** that retail is there"). offset **2.22**. *(was an editorial build @17.8; now the rotation motion lands on a real in-window spoken word — §0e. NOTE: not "equity" 18.08, which is clip_comp 2.58 in b1, not here.)*
  - timeline chips **`NOV · DEC · JAN · FEB`** `[EDITORIAL]` @18.8 (offset 3.30) *(spoken src 1131.8–1133.1, before src_in → editorial context)*
  - footer date **`2025 → 2026`** (Inter 600, #F0F0F0; 2026 = "this year") `[EDITORIAL]` @19.6 (offset 4.10)
- ***CYAN:** the rule only (`EQUITIES` stays white).
- **R4 audit:** eyebrow {capital, rotation} / from {crypto, altcoins} / to {equities} / chips {nov,dec,jan,feb} — no repeat. ✓
- **Opening-6s element types (DESIGN.md):** b1 intro kinetic (type 1) + eyebrow (type 2) + rule (type 3) + before/after block (type 4) + chips (type 5) → PASS.

### b4 — JP MORGAN ALL-TIME-HIGH stat (swiss-grid; HAND-BUILD) ← absorbs "retail moved"
- **clip_comp** 20.5–38.9 | **src** 1156.0–1174.4 | **view** Mode-A | **data-start** `20.5` **data-duration** `18.4` *(was 12.5 — content done ~32.1, **HOLD to 38.9** to kill the 33.0→38.9 blank-left; set in index.html + template)*
- **sub-comp** `compositions/beat-c5b4-jpm-all-time-high.html` — **DELETE the `05` index (§0a); STACK the stat at 150px + ▲ glyph (§0e).**
- **template** swiss-grid in left zone: eyebrow + stacked 150px slam stat (with directional ▲) + footer + sublabel.
- **Full on-screen text + word-sync** (NO index — R6):
  - eyebrow **`JP MORGAN PRIME BROKERAGE · MAY 2026`** (Inter 700, 32px, #F0F0F0) — slam **clip_comp 20.88** ← "JP" (table 36.38). offset 0.38. *(`· MAY 2026` dateline [EDITORIAL]; 2026 = this year)*
  - stat **`ALL-TIME` / `HIGH ▲`** *(stacked two lines, Inter 900, 150px, #F0F0F0; the ▲ is green `#16C784` directional, NOT the cyan accent — not a count-up, no number in transcript)* — slam **clip_comp 28.34** ← "all…high" (table 43.84/44.16). offset 7.84.
  - footer **`BY A MEANINGFUL MARGIN`** (Inter 600, #F0F0F0) — fire **clip_comp 29.38** ← "meaningful margin" (table 44.88/45.08). offset 8.88.
  - sublabel **`RETAIL MOVED INTO EQUITIES`** (Inter 600, #F0F0F0) — fire **clip_comp 31.70** ← "retail moved" (table 47.20). offset 11.20. *(folded-in old c5b5, now word-synced inside Mode-A)*
- ***CYAN:** a short cyan rule beneath the stat (swiss-grid = stat OR rule → rule chosen so the 150px stat reads white; the ▲ is green directional, not cyan).
- **R4 audit:** eyebrow {jp, morgan, prime, brokerage, may, 2026} / stat {all-time, high} / sublabel {retail, moved, equities} / footer {meaningful, margin} — no repeat. ✓

### b5 — WINTERMUTE WEEKLY + "marginal risk dollar" QUOTE CARD (liquid-glass; HAND-BUILD)
- **clip_comp** 38.9–63.6 | **src** 1174.4–1199.1 | **view** Mode-A | **data-start** `38.9` **data-duration** `24.7` *(was 20.1 — content done ~59.0, **HOLD to 63.6** to kill the 59.0→64.4 blank-left; FULL toggle @63.6; set in index.html + template; **NO exit tween — see §0b note**)*
- **sub-comp** `compositions/beat-c5b5-wintermute-weekly-quote.html` *(no index in this file — nothing to delete; set template `data-duration="24.7"`)*
- **template** ONE liquid-glass card (the publication name-drop + its line are the same source → one card): `rgba(20,26,34,0.92)` fill, **4px cyan accent bar inset-left**, soft glow, 1px border, `mask-image` feather. **No backdrop-filter, no grain.**
- **Full on-screen text + word-sync:**
  - card slides in from right — **clip_comp 38.96** ← "Jasper is also writing…" (table 54.46)
  - eyebrow **`WINTERMUTE WEEKLY`** (Inter 700, 32px) — fire **clip_comp 40.34** ← "Wintermute weekly" (table 55.84/56.32)
  - pull-quote **`"The marginal risk dollar went into equities, not crypto."`** (Inter 700, 64px, #F0F0F0) — fades in **clip_comp 54.50** ← "the marginal risk dollar…" (table 70.00); the words **`not crypto` flip `*CYAN` @ clip_comp 57.94** ← "not crypto" (table 73.44)
  - attribution **`— Jasper De Maere`** (Inter 600, 32px) `[EDITORIAL]` — fades **IN** @58.6 and **STAYS** (no fade-out before the 63.6 toggle)
- ***CYAN:** the words `not crypto` (accent bar stays neutral so only one cyan).
- **R4 audit:** eyebrow {wintermute, weekly} / quote {marginal, risk, dollar, went, equities, crypto} / attrib {jasper, maere} — no repeat. ✓
- **R7 note:** the card HOLDS on screen 38.9→63.6 (**no element exits early — there is no card-out / stack-exit tween**); the left zone is never blank before the FULL toggle. Do NOT add an exit tween by analogy with the kinetics.

### b6 — HOST QUESTION kinetic (kinetic-type; no "HOST" label) ← Q of the Q/A pair
- **clip_comp** 64.9–70.18 | **src** 1200.4–1205.68 | **view** FULL (both speakers) | **data-start** `64.6` **data-duration** `5.78` *(was 2.2 — **HOLD the question text to b7's "NO —" @70.18** per v4-review item 8, so the question is still readable when the answer slams; no fire moves, only the hold extends)*
- **sub-comp** `compositions/beat-c5b6-is-crypto-dead.html`
- **template** kinetic 2-line build over both speakers (question text only, no "HOST" chrome). **Lines STAY (no exit) until b7 fires** — the Q→A payoff lands while the question is still on screen.
- **On-screen lines + word-sync:**
  - **L1 `IS CRYPTO DEAD`** — fire **clip_comp 64.94** ← "crypto" (table 80.44) / "dead" (table 80.82)
  - **L2 `FOR RETAIL TODAY` *CYAN** — fire **clip_comp 65.78** ← "for retail" (table 81.28) ("TODAY" = editorial, tightens "these days")
- **Exit:** question holds until **70.18**, then clears as b7 "NO —" lands (b6 fades out 70.0→70.4 as b7 L1 slams in — a hard Q→A cut, not a gap). *(FULL breath 63.6→64.9 precedes this — both speakers, no blank.)*
- **R4 audit:** {crypto, dead} / {retail, today} — no repeat. ✓

### b7 — JASPER'S ANSWER kinetic (kinetic-type) ← A of the Q/A pair (2-in-a-row OK)
- **clip_comp** 70.2–79.3 | **src** 1205.7–1214.8 | **view** FULL | **data-start** `69.9` **data-duration** `9.7` *(unchanged; **L2b hold-line added** to bridge the L2→L3 speech gap — §0d/§b7)*
- **sub-comp** `compositions/beat-c5b7-not-for-the-og-holders.html`
- **On-screen lines + word-sync** (the L2→L3 gap is **real intermediate speech** — "I do think retail and especially **the people who've been in crypto since 21**" — not dead air; the added L2b makes the stack build smoothly instead of two-lines-then-7s-wait-then-one):
  - **L1 `NO —`** — fire **clip_comp 70.18** ← "No" (table 85.68)
  - **L2 `NOT FOR THE OG HOLDERS`** — fire **clip_comp 71.60** ← "not that for retail" (table 87.10) ("THE OG HOLDERS" = editorial gloss of "the people who've been in crypto since 21")
  - **L2b `WHO'VE BEEN IN SINCE…`** (Inter 600, #F0F0F0, dimmer build line that bridges to L3) — fire **clip_comp 73.86** ← "who've been in crypto" (table 89.36/94.18). offset 3.96. *(carries the held thought across the 7.7-s span so L3 doesn't feel orphaned; reads as the lead-in to "SINCE 2021")*
  - **L3 `SINCE 2021` *CYAN** — fire **clip_comp 79.30** ← "since 21" (table 94.80) (2021 spelled in full per date rule)
- *(Video returns to Mode-A @83.2 for b8.)*
- **R4 audit:** {no} / {og, holders} / {who've, been, in} / {since, 2021} — no repeat. ✓

### b8 — 2021 EXUBERANCE flowchart (hand-built dark 3-node chain) · distinct from swiss-grid
- **clip_comp** 83.0–121.0 | **src** 1218.5–1256.5 | **view** Mode-A | **data-start** `83.0` **data-duration** `38.0` *(unchanged — already butts b9 @121.0; no blank in this sub-block; **mid-beat refresh @110.12 added §0e** so the 110→121 tail isn't frozen)*
- **sub-comp** `compositions/beat-c5b8-exuberance-flow.html` — **DELETE the `05` index (§0a); ADD the mid-beat refresh (§0e).**
- **template** 3 nodes + connectors (`back.out(1.5)` pop; `strokeDashoffset` draw). Eyebrow draws on "alt season".
- **Full on-screen text + word-sync** ("alt season" = corrected from Whisper "old season", framed as retail's slang in quotes; NO index — R6):
  - eyebrow **`WHAT RETAIL CALLS "ALT SEASON"`** (Inter 700, 32px) — fire **clip_comp 83.30** ← "season" (table 98.80). offset 0.30.
  - node 1 **`EXTREME EXUBERANCE`** — pop **clip_comp 84.66** ← "exuberance" (table 100.16). offset 1.66.
  - node 2 **`MASSIVE CAPITAL INJECTION`** — pop **clip_comp 89.50** ← "capital" (table 105.00) / "injection" (table 105.40). offset 6.50.
  - node 3 **`ALL RISK ASSETS UP` *CYAN** — pop **clip_comp 91.92** ← "all risk assets moved up" (table 106.78/107.42). offset 8.92.
  - annotation **`THE 2021 BENCHMARK`** (Inter 600, #F0F0F0) — @ **clip_comp 94.62** ← "the benchmark" (table 110.12 first mention). offset 11.62.
  - **mid-beat refresh** (NO new text) — @ **clip_comp 110.12** ← "benchmark" (table 110.12 second mention, "a little bit of the **benchmark** which people are putting on all seasons"). offset 27.12. The **3 connectors pulse-draw once (0.8 s)** and **node-3's cyan glow does ONE 0.8-s breathe** (scale 1.0→1.04→1.0). Deterministic, single, no repeat. Keeps the 26-s tail alive.
- ***CYAN:** node 3 only (its single-breathe refresh stays node-3 cyan — no new cyan introduced).
- **R4 audit:** eyebrow {retail, calls, alt, season} / n1 {extreme, exuberance} / n2 {massive, capital, injection} / n3 {risk, assets} / annot {benchmark} — no repeat. ✓
- **R7 note:** all nodes STAY once popped; the flow holds 83.2→121.0 — left zone never empties before b9; the @110.12 refresh prevents a frozen tail.

### b9 — VOL-PROFILE two-series CHART · *distinct PRIMARY device pt2 — the required new chart* (hand-built dark data-chart)
- **clip_comp** 121.0–143.4 | **src** 1256.5–1278.9 | **view** Mode-A | **data-start** `121.0` **data-duration** `22.4` *(was 16.5 — content done ~137.4, **HOLD to 143.4** to kill the 137.5→143.4 blank-left; set in index.html + template)*
- **sub-comp** `compositions/beat-c5b9-vol-profile-chart.html` — **DELETE the `05` index (§0a); SIMPLIFY axis + equity opacity; SWAP the down-draw to "compressed"; STAGGER the two line draws (§0e).**
- **template** two-series before→after line chart (crypto vol HIGH 2021→ then **compressed**; equity vol low → **rose**; profiles **converged**). Series A = CRYPTO (red `#FF4D4F`, descending), Series B = EQUITIES (green `#16C784`, **0.6 reference opacity**, ascending). **ONE inline anchor `2021 → NOW`** (not two ticks). Convergence point = the cyan accent. **The two lines draw in OVERLAPPING windows so they visibly close on each other as one converging motion (§0e stagger).**
- **Full on-screen text + word-sync** (NO index — R6; the down-draw lands on "compressed" and the callout on the breath after — v4-review item 1 swap):
  - eyebrow **`VOLATILITY PROFILE`** (Inter 700, 32px) — fire **clip_comp 123.52** ← "the volatility of crypto" (table 139.02). offset 2.52.
  - x-anchor **`2021 → NOW`** (Inter 600, #F0F0F0, single inline element) `[EDITORIAL]` @122 (offset 1.0)
  - series legend **`CRYPTO`** (red) / **`EQUITIES`** (green @0.6) `[EDITORIAL]` @122.5 (offset 1.5) *(directional red/green = allowed market indicators per D7, NOT the cyan accent)*
  - **equity (green) line draws UP** — starts **clip_comp 124.4** (offset 3.4) over ~5.0 s `[EDITORIAL build, ref 0.6]`
  - **crypto (red) line draws DOWN** — starts **clip_comp 127.8** (offset 6.8) over ~8.0 s and **lands its low on "compressed"** → key the descent end at **clip_comp 136.44** ← "compressed" (table 151.94). *(overlaps the equity draw so the two series close as ONE motion; folds-in old c5b11 "compressed" as the chart's down-move, not a stranded FULL kinetic. FIXED off-by-one: was keyed to "volatility" 150.62 / clip_comp 135.12.)*
  - convergence callout **`THEY CONVERGED` *CYAN** — fire **clip_comp 137.38** ← the breath after "compressed" (table 152.88 "to"). offset 16.38. (drawn at the crossing once both lines arrive; reads "THEY CONVERGED" not "PROFILES CONVERGED" to avoid sharing "profile" with the eyebrow — R4)
- ***CYAN:** the convergence point/callout only.
- **R4 audit:** eyebrow {volatility, profile} / series {crypto, equities} / callout {they, converged} — no repeat. ✓
- **R7 note:** lines + callout STAY drawn after they animate; the chart is on screen 121.0→143.4 (the ~6.0 s past the last fire is the drawn chart holding, NOT a blank frame) — left zone never empties before b10.

### b10 — VOL COMPARISON crypto↓ vs equity↑ (swiss-grid two-column; HAND-BUILD) ← absorbs "became equal"
- **clip_comp** 143.4–153.6 | **src** 1278.9–1289.1 | **view** Mode-A | **data-start** `143.4` **data-duration** `10.2` *(was 10.8 — content done ~148.6, **HOLD to 153.6** = the FULL toggle; last Mode-A graphic; set in index.html + template)*
- **sub-comp** `compositions/beat-c5b10-vol-comparison.html` — **DELETE the `05` index (§0a); change footer text to "NOW EQUAL" (§0e).**
- **template** two-column in left zone: directional indicators with a cyan divider rule.
- **Full on-screen text + word-sync** (NO index — R6):
  - eyebrow **`THE VOL TRADE MOVED`** (Inter 700, 32px) `[EDITORIAL]` @143.5 (offset 0.10)
  - col-L **`CRYPTO  ↓ DOWN`** (red `#FF4D4F`) `[EDITORIAL build]` @143.6 (offset 0.20)
  - col-R **`EQUITY  ↑ RISING`** (green `#16C784`) — fire **clip_comp 143.98** ← "the equity market became more volatile" (table 159.48/160.06). offset 0.58.
  - cyan divider draws between columns **`*CYAN`** @144.4 (offset 1.0)
  - footer **`NOW EQUAL`** (Inter 600, #F0F0F0) — fire **clip_comp 147.20** ← "volatility profile became quite equal" (table 162.70/164.12). offset 3.80. *(was "PROFILES NOW EQUAL"; "profiles" dropped to avoid the 3rd "profile" in the 70-s Mode-A block — §0e)*
- ***CYAN:** the divider rule (red/green are directional indicators per D7).
- **R4 audit:** eyebrow {vol, trade, moved} / colL {crypto, down} / colR {equity, rising} / footer {now, equal} — no repeat. ✓
- **R7 note:** all columns + footer STAY; holds 143.4→153.6 (FULL toggle) — left zone never empties before the closer.

### b11 — CLOSER kinetic "they just want a vol trade → equity offers it" (kinetic-type) ← VERIFIED closer
- **clip_comp** 154.52–161.7 | **src** 1290.0–1297.2 | **view** FULL (both speakers) → settles to clean FULL for the last ~1.3 s (D4: end on content, not a card) | **data-start** `153.6` *(was 154.3)* **data-duration** `8.1` *(was 7.4)*
- **sub-comp** `compositions/beat-c5b11-vol-trade-closer.html` — **RE-DERIVE offsets per §0c (+0.7 each).**
- **template** kinetic 3-phrase build, STAYS (no dim).
- **On-screen lines + word-sync** (re-derived offsets in §0c so they survive the data-start move):
  - **L1 `THEY JUST WANT`** — fire **clip_comp 154.52** ← "They just want" (table 170.02). **offset 0.92** (AFTER the 154.05 expand-settle — no mid-expand text; fixes the v3 bug).
  - **L2 `A VOLATILITY TRADE`** — fire **clip_comp 156.68** ← "a volatility trade" (table 172.18/172.64). **offset 3.08.**
  - **L3 `EQUITY OFFERS IT` *CYAN** — fire **clip_comp 160.66** ← "currently equity markets are offering that exact thing" (table 176.16; "offering" anchor). **offset 7.06.**
  - lines drift out @161.7 (offset 8.1); **video holds clean FULL to 163.0** — no outro card (D4).
- **R4 audit:** {they, just, want} / {volatility, trade} / {equity, offers} — no repeat. ✓

---

## VERIFICATION SUMMARY (grade against `_QA-CHECKLIST.md` — every item)

**§1 R1 + R7:** view-timeline above; 5 phases, smallest sustained 9.4 s, all A-B-A gaps ≥20 s, only 4 GSAP toggles. **R7: every Mode-A second has a NAMED graphic (b3⊐b4⊐b5 cover 15.5→63.6; b8⊐b9⊐b10 cover 84.1→153.6, all butting); the three v3 blank-left gaps (33→38.9, 59→64.4, 137.5→143.4) are filled by hold-until-successor + the two moved toggles. Every breath is FULL-frame. b8's tail kept alive by §0e refresh; Phase-3's 69.5-s Mode-A is deliberate (no toggle — A-B-A risk).** ✓
**§1 R6:** §0a deletes the `05` index from b3/b4/b8/b9/b10 BY ID SELECTOR (order-independent); `grep '>05<'` → 0 hits post-edit. No beat renders any index/clip-number. ✓
**§2 R2:** max 2 kinetics in a row; distinct device (rotation card b3 + vol-profile chart b9) LEADS; chart/flow/swiss/card hand-built (not from kinetic-type); kinetic share 5/11. ✓
**§3 Dialog-match + word-sync:** opens on "pivoted very aggressively into equity" (spoken clip_comp 0.34–2.58; all three now in-clip words after dropping "RETAIL"); first text @0.34; **every kinetic line fires at a table/audio.json clip_comp (listed per line, audio.json-verified)**; editorial lines marked. **b9 down-draw/callout swap corrected to "compressed"/breath; b3 arrow word-locked to "evidence."** ✓
**§4 Opening coherence (R5):** "PIVOTED / VERY AGGRESSIVELY / INTO EQUITY" is a complete thought, all words spoken in-clip; cyan payoff "INTO EQUITY" is a real phrase. ✓
**§5 Framing:** `object-position: 83% center`, Mode-A box {1229,108,614,864}; verified by frame (Jasper centered, name in-frame); opening/Q-A/closer FULL show both speakers. ✓
**§6 Jargon (R3):** no burp/deep-in/graft/stake-rate; "alt season" corrected (Whisper "old season"); Wintermute / JP Morgan / Jasper De Maere exact; dates 2021(benchmark)/2025/2026, never 2024. ✓
**§7 Duplicate words (R4):** per-beat audit above — all clean; cross-beat "profile" reduced (b10 footer → "NOW EQUAL"). ✓
**§8 Carry-over hard rules:** ONE cyan per beat (marked; b9 simplified to one cyan + red/green indicators; b4 ▲ is green directional not cyan); cards `rgba(20,26,34,0.92)` + 4px inset cyan bar + glow + mask, no blur, no grain; eyebrows Inter 700 ≥32px #F0F0F0, body ≥600, no #888; ends on clean video b11 (no outro); phrase kinetics build-and-STAY. **z-index:3 rule in `index.html` already lists all 11 ids (`#beat-c5b1…#beat-c5b11`) — verified present; deleting the index sub-elements does NOT change that rule.** ✓
**§9 Verify-by-frame (MANDATORY before done):** after draft render, extract and LOOK at:
  - opening (comp 1, 2.6) — speaker right + 3 element types; **b1 L1 reads "PIVOTED" (not "RETAIL PIVOTED")**,
  - **the four toggles (15.0 / 63.6 / 83.2 / 153.6)** and the formerly-blank instants **comp 36, 61, 140** — must now show a graphic in the left zone (b4 stat / b5 quote / b9 chart respectively), NOT a blank crop,
  - **comp 18** — b3 arrow/EQUITIES lands as Nic says "evidence" (word-locked, §0e),
  - **comp 30** — b4 stacked stat does NOT wrap/clip and the green ▲ is visible (§0e),
  - **comp 70** — b6 question still on screen as b7 "NO —" slams (the hold, §b6),
  - **comp 110** — b8 connectors pulse / node-3 breathes (mid-beat refresh alive, not frozen — §0e),
  - **comp 122–124** — b9 eyebrow + single "2021 → NOW" anchor + 0.6 equity line present, lines drawing toward each other (§0e), no "05",
  - **comp 136.4** — b9 crypto line bottoms on "compressed" and **comp 137.4** convergence callout pops (the swap, §0e),
  - **comp 154.5** — b11 L1 is fully settled and NOT mid-expand (the §0c fix),
  - each distinct beat — no "05" anywhere (R6).

**Beat count:** **11** (within the clip-5 11–13 range). Kinetic share 5/11. Two hand-built distinct devices (flow b8, vol-chart b9).

## Build manifest row
`clip_5 | clip-5-capital-rotation | src_in 1135.5 | src_out 1298.5 | 163.0s | kinetic-type, rotation-card(custom), swiss-grid, liquid-glass, flowchart(custom-dark), data-chart(custom-dark) | 11 beats | object-position 83% | v4: R6 index removed by-id (5 beats), R7 blank-left filled (3 gaps via hold-until-successor + 2 toggle moves), b11 offsets re-derived (+0.7), b4 stat stacked 150px+▲, b9 axis simplified + down-draw swapped to "compressed" + lines staggered, b8 mid-beat refresh @110, b6 question holds to b7, b3 arrow word-locked to "evidence", b1 hook → "PIVOTED", b10 footer → "NOW EQUAL", index.html VIEW-TIMELINE comment rewritten`
