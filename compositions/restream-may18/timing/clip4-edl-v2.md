# Clip 4 — Oct 10 Crash (ADL Cascade) — EDL **v2** (RE-DESIGN, supersedes clip4-edl-final.md)

**Source:** **src_in 1030.76 → src_out 1118.98** | **Duration: 88.2s** | **Slug:** `clip-4-oct10-crash`
**Comp offset:** `comp_t = src_t − 1030.76`
**Beat count:** 8
**Object-position:** `83% center` (Mode A) — see rationale below.

> Supersedes `clip4-edl-final.md`. That v1 FAILED review for (1) opening kinetic ("25 TIMES MORE / DERIVATIVES / THAN SPOT") was pulled from src~1095, ~85s AFTER the old in-point 1010 where Jasper was actually saying "offsetting that with perpetual futures… centralized exchanges… issued their ADL" — anticipatory text that did not match the dialog; (2) formulaic structure — every clip opened on the same swiss-grid `index/eyebrow/stat/footer` chrome, and the 25× stat appeared **three** times (hook + c4b2 swiss-grid + c4b8 callback); (3) framing (clip-1 used object-position 50%, which centers the seam/host). v2 fixes all three.

---

## RULE 1 — Open on a real line (re-picked in-point)

**Old in-point 1010.0 was wrong** — there Jasper is mid-build ("offsetting that with perpetual futures. And I think something that happens, which threw a lot of dealers off…"), so the 25× hook was anticipatory.

**New in-point `src_in = 1030.76`** = the word **"your"** in **"your delta completely shifts in your structure."** The "…in the money. But as a result, …" filler head (src 1029.02–1030.22) is **trimmed**. First audible words at comp 0.0 = the concrete crash-mechanic line. The opening kinetic is the words he is saying THEN, word-synced — no anticipatory pull.

Opening kinetic (c4b1), word-synced to the transcript:
- **"YOUR DELTA"** — matches spoken **"your"** (`your`@src1030.76 → **comp 0.00**) / **"delta"** (`delta`@src1030.92 → comp 0.16). Fire at **comp 0.08**.
- **"COMPLETELY SHIFTS"** (cyan payoff) — matches spoken **"completely"** (`completely`@src1031.24 → **comp 0.48**) / **"shifts"** (`shifts`@src1031.74 → comp 0.98). Fire at **comp 0.48**.

These are the literal words spoken in the first second — auditable against `clip4-words.txt` recomputed for the new in-point (table inlined at the end of this file). **No line in this clip is anticipatory; the only EDITORIAL marks are structural (eyebrow labels / flow node labels), called out per beat.**

**LEAD DEVICE — CASCADE-LED:** the ADL cause→effect cascade is the centerpiece. It is promoted to **beat 2** (was beat 4 in v1) and its nodes build **in sync with the spoken chain** (delta shifts → perp closed out → naked long → forced selling → alts −60/70/80%) instead of being a static editorial diagram. The 25× stat is the climax payoff and appears **once** (beat 5), as a kinetic count-up landing on the spoken "25x", not as repeated swiss-grid chrome.

## RULE 2 — Varied structure (no formulaic swiss-grid open)

v1 opened on the universal `0N / EYEBROW / cyan-rule / STAT / footer` swiss-grid (c4b2). **v2 does NOT.** It opens cold on a word-synced **kinetic sentence** (the delta-shift line), then goes straight into the **cascade flowchart** centerpiece. Template sequence:

`kinetic → flowchart(decision-tree) → caption-kinetic-slam → (clean) → liquid-glass → apple-money-count → swiss-grid(micro-stat) → kinetic`

No two identical templates are adjacent. The 25× is an `apple-money-count`-style count-up (catalog block family), the cascade is a `flowchart`/decision-tree, the "hectic" beat is a `caption-kinetic-slam` treatment — each beat looks distinct from its siblings, and the open is unmistakably different from clips 1/3/5/6/8.

## RULE 3 — Framing (verified from extracted source frames)

Frames extracted with `ffmpeg -nostdin -ss <t> -i …/clip-4-oct10-crash/source.mp4 -frames:v 1 …` and viewed at **src 1030.76 (in-point), 1044.7, 1090.9, 1023, 1029.9** (5 frames total; 1044.7 and 1090.9 are the two Mode-A timestamps below).

**What the frames show:** true side-by-side. Nic (host) fills the LEFT half; **Jasper (guest) fills the RIGHT half (x≈960–1920)**, face horizontally centered in his half at **≈75% of full width**, eyes at **≈25–28% from the top**, moderate dark wood-panel headroom above (not excessive). His name lower-third **"Jasper De Maere / Wintermute"** sits bottom-left of his panel (baseline ≈92% down, left edge ≈x=985). At 1090.9 his hand is raised near his chin — he gestures often, but the head position is stable across all frames.

**Object-position chosen: `83% center`** (matching clip-2, which is the user-approved correct reference).
- *Why 83% and not 50/62:* Mode A crops a tall narrow window (614×864, AR≈0.71) from 1920×1080 with `object-fit:cover`. With `cover`, only ~40% of the source width is visible. At **50%** the window centers on x≈960 — i.e. the **center seam + Nic's shoulder** (this is exactly what made clip-1 wrong). At **62%** it still clips the seam. Jasper's face is at ~75% and his name label runs ~51–62%; **83%** lands the visible window on his face (~70–88% region) while still catching the right portion of his name-tag and **excluding the seam/host**. Verified against the 1044.7 and 1090.9 frames.
- *Vertical:* `center` — eyes at ~26% + moderate headroom keep a clean head-and-shoulders with the name not cut; **no vertical bias and no scale-up needed** (Mode A's 80% scale already trims the dead ceiling). Bottom clearance in the Mode-A box = 1080−108−864 = **108px** (> 40px ✓), top clearance = **108px** (> 20px ✓).

---

## Master-timeline framing (mirror clip-2 `index.html`)

- `MODE_A = {left:1229, top:108, width:614, height:864}`, `borderRadius:"6px"`, `object-position:83% center`.
- **Opening differs from clip-2 on purpose:** clip-2 opens full-frame for an *anticipatory* hook then shrinks at t=3.0. Here the opening kinetic IS the spoken line, so: t=0–3.5 **full-frame** (both speakers) while "YOUR DELTA / COMPLETELY SHIFTS" fires word-synced; at **t=3.5** shrink to Mode A (`expo.inOut`, 0.7s) as he continues "…delta neutral, let's say, like your long spot, you're short to the perp"; `#bg-glow` in 3.8, `#zone-rule` draw 3.9; slow Ken-Burns scale 1.0→1.04 across the clip.
- Before each **full-frame** kinetic (c4b3 ~34.0, c4b5 ~58.5, c4b8 ~80.4): expand video to full-frame (`expo.inOut`, ~0.4s). After each: return to Mode A (`expo.out`, ~0.45s) with glow + zone-rule.
- c4b2 (flowchart), c4b4 (liquid-glass), c4b6 (swiss-grid micro-stat) play in **Mode A**.
- Audio: separate `<audio>` el `data-volume="1"`, continuous; video `muted`. `data-media-start="1030.76"` on both video and audio; `data-duration="88.2"`.

## z-index reminder (DESIGN.md line 58)
Every overlay beat id (`beat-c4b1` … `beat-c4b8`) MUST be listed in the `z-index:3` style rule in `index.html`, or it renders behind the `z-index:2` video.

---

## Beat Map (v2)

| Beat | Comp range | Src range | Template / block | Speaker mode | Sub-comp file |
|------|-----------|-----------|------------------|--------------|---------------|
| c4b1 | 0.0–7.5 | 1030.76–1038.26 | kinetic-type (cold open) | full-frame → Mode A @3.5 | `beat-c4b1-delta-open.html` |
| c4b2 | 8.0–34.0 | 1038.76–1064.76 | **flowchart / decision-tree (CENTERPIECE)** | Mode A | `beat-c4b2-adl-cascade.html` |
| c4b3 | 34.0–40.0 | 1064.76–1070.76 | caption-kinetic-slam | full-frame | `beat-c4b3-hectic-slam.html` |
| — | 40.0–50.8 | 1070.76–1081.56 | clean video (Mode A) | Mode A | — |
| c4b4 | 50.8–58.0 | 1081.56–1088.76 | liquid-glass card | Mode A | `beat-c4b4-30-45-min.html` |
| c4b5 | 58.5–74.0 | 1089.26–1104.76 | **apple-money-count** (25× count-up) | full-frame → Mode A | `beat-c4b5-25x-count.html` |
| c4b6 | 74.4–80.0 | 1105.16–1110.76 | swiss-grid (micro-stat) | Mode A | `beat-c4b6-supported-leverage.html` |
| c4b8 | 80.4–88.2 | 1110.76–1118.98 | kinetic-type (human closer) | full-frame | `beat-c4b8-wiped-out.html` |

*(Beat ids skip "c4b7" — kept as 8 distinct ids; final closer retains id `c4b8` to match the existing index.html z-index slot naming convention. Renumber freely at build, but keep every id in the z-index:3 rule.)*

Opening "3+ element types before 6s" (DESIGN.md): c4b1 kinetic L1 (type 1, comp 0.08) + kinetic cyan payoff line (type 2, comp 0.48) + Mode-A shrink with cyan zone-rule draw + glow (type 3, comp 3.5–3.9) + cascade eyebrow "ADL CASCADE" slam (type 4, comp ~8.2). Speaker visible from t=0 (full-frame, both speakers). **PASSES** — and it is NOT the formulaic swiss-grid open.

---

## Beat detail

### c4b1 — kinetic-type (cold open) · full-frame → Mode A · `beat-c4b1-delta-open.html`
- **Comp:** 0.0–7.5 · **Src:** 1030.76–1038.26 · `data-start 0.0` / `data-duration 7.5`
- **Speaker mode:** full-frame (both speakers, dark gradient backdrop LEFT) for the kinetic; master timeline shrinks video to **Mode A at comp 3.5** while Jasper keeps talking ("…delta neutral… long spot… short to the perp"). Kinetic exits up ~3.2 before the shrink.
- **Kinetic lines — WORD-SYNCED (auditable):**
  - **L1 "YOUR DELTA"** — on-screen text `YOUR DELTA` — transcript words **"your delta"** (`your`@1030.76=comp 0.00, `delta`@1030.92=comp 0.16) — **fire comp 0.08**, `#FFFFFF`, Inter 900 ~130px.
  - **L2 "COMPLETELY SHIFTS"** (cyan payoff) — on-screen text `COMPLETELY SHIFTS` — transcript words **"completely … shifts"** (`completely`@1031.24=comp 0.48, `shifts`@1031.74=comp 0.98) — **fire comp 0.48**, `#00D4FF` + cyan glow, Inter 900 ~130px.
- **Cyan element:** L2 "COMPLETELY SHIFTS" payoff (single cyan).
- **Exit:** whole stack drifts up `power2.in` at ~comp 3.1 (cleared before Mode-A shrink at 3.5).
- **Note:** both lines are literal spoken words at the head — this is the Rule-1 fix. No anticipatory text.

### c4b2 — flowchart / decision-tree (CENTERPIECE, cascade) · Mode A · `beat-c4b2-adl-cascade.html`
- **Comp:** 8.0–34.0 · **Src:** 1038.76–1064.76 · `data-start 8.0` / `data-duration 26.0`
- **Speaker mode:** Mode A (video right 40%, ~80% scale; glow + zone-rule already in from c4b1 shrink).
- **Lead-device beat.** Vertical cause→effect flow (5 nodes) that **builds in sync with the spoken cascade** — each node reveals on its spoken cue (these node reveals are WORD-CUED, not editorial), cyan connector arrows draw between them:
  - Eyebrow **"ADL CASCADE · OCT 2025"** — `#F0F0F0` Inter 700 32px — `<!-- EDITORIAL: structural label -->` fire comp ~8.2.
  - Node 1 **[DELTA-NEUTRAL BOOK]** — cued to **"delta neutral"** (`neutral,`@1034.22 is in c4b1's window; in this beat re-establish at entry) → reveal comp ~8.6 `#F0F0F0`. (Structural recap node; label EDITORIAL.)
  - Node 2 **[PERP CLOSED OUT]** — cued to spoken **"closed out"** (`closed`@1046.64=comp 15.88, `out`@1047.00=comp 16.24) → reveal **comp 15.9** `#F0F0F0`.
  - Node 3 **[NAKED LONG DELTA]** — cued to spoken **"naked long delta"** (`naked`@1048.46=comp 17.70, `long`@1048.90=comp 18.14, `delta.`@1049.28=comp 18.52) → reveal **comp 17.7** `#F0F0F0`.
  - Node 4 **[FORCED SELLING → FEEDBACK LOOP]** — cued to spoken **"feedback loop"** (`feedback`@1055.50=comp 24.74, `loop`@1055.92=comp 25.16) → reveal **comp 24.7** `#F0F0F0`.
  - Node 5 **[ALTS −60 / −70 / −80%]** (cyan final node) — cued to spoken **"60, 70, 80%"** (`60,`@1062.66=comp 31.90, `70,`@1063.16=comp 32.40, `80%.`@1063.54=comp 32.78) → the three numbers tick into the node **comp 31.90 → 32.40 → 32.78**, node finalizes cyan `#00D4FF`.
- **Cyan element:** Node 5 (the final outcome node) — single cyan accent (D7 tree convention). Connector arrows muted `#6B7480` (structural, not an accent).
- **Anti-static / motion:** nodes pop in on their spoken cues across 8→33s (not all at once), cyan arrows draw `scaleY 0→1` between reveals, and the −60/−70/−80% numbers count into node 5 — so across its 26s the diagram is continuously *building to the spoken story*, never a frozen hold. Exits at ~comp 33.6 to clear for c4b3.

### c4b3 — caption-kinetic-slam · full-frame · `beat-c4b3-hectic-slam.html`
- **Comp:** 34.0–40.0 · **Src:** 1064.76–1070.76 · `data-start 34.0` / `data-duration 6.0`
- **Speaker mode:** full-frame (both speakers, dark gradient backdrop). Video expands to full-frame at ~33.8, returns to Mode A on exit (~40.0).
- **Treatment:** `caption-kinetic-slam` style — hard scale-overshoot slam (distinct from c4b1's y-rise), single big line.
- **Kinetic line — WORD-SYNCED:**
  - **"EXTREMELY HECTIC"** (cyan on "HECTIC") — transcript words **"extremely hectic"** (`extremely`@1065.28=comp 34.52, `hectic,`@1065.74=comp 34.98) — "EXTREMELY" slams **comp 34.52**, "HECTIC" slams cyan **comp 34.98**.
- **Cyan element:** "HECTIC" (single cyan).
- **Exit:** scale-down + fade `power2.in` ~comp 39.4.

### (clean window) comp 40.0–50.8 · Mode A
- Video in Mode A, no overlay. Jasper: "it was shorter than a lot of people think… that real compression and the stress was over a shorter period of time…" (src 1067–1081). **10.8s** — exceeds the 8s cap, BUT this clip is 88s (the D6 ≤8s cap is for clips <120s; acceptable here as a single breathing window between dense beats) and it is bracketed by motion on both sides. *Builder option:* if a tighter feel is wanted, drop a one-line supplemental kinetic "SHORTER THAN PEOPLE THINK" on spoken `shorter`@37.26 — but that phrase is better served by the c4b4 card; leaving this as the clip's one clean beat.

### c4b4 — liquid-glass card · Mode A · `beat-c4b4-30-45-min.html`
- **Comp:** 50.8–58.0 · **Src:** 1081.56–1088.76 · `data-start 50.8` / `data-duration 7.2`
- **Speaker mode:** Mode A.
- **Card style (D7):** `rgba(20,26,34,0.92)` fill, **4px cyan `#00D4FF` inset accent bar** (left), soft outer glow, 1px `rgba(255,255,255,0.08)` border, `mask-image` feather. **NO `backdrop-filter` blur, NO grain.**
- **Content (exact text + hex):**
  - Eyebrow **"HOW LONG IT LASTED"** — `#F0F0F0` Inter 700 32px `<!-- EDITORIAL: structural label -->`
  - Headline **"30–45 MINUTES"** — `#FFFFFF` Inter 900 96px (the duration is the point).
  - Sub-row **"of real stress — then everything picked back up"** — `#C4C9D0` Inter 600 28px.
- **Entry timing — WORD-CUED:** card slides in from right at **comp 51.3** to land on spoken **"half an hour to 45 minutes"** (`half`@1082.34=comp 51.58, `45`@1083.00=comp 52.24, `minutes`@1083.40=comp 52.64). Verified spoken material: "It was really, I think, half an hour to 45 minutes before everything picked back up." Holds, exits ~comp 57.6.
- **Cyan element:** the 4px accent bar (single cyan).

### c4b5 — apple-money-count (25× count-up, climax) · full-frame → Mode A · `beat-c4b5-25x-count.html`
- **Comp:** 58.5–74.0 · **Src:** 1089.26–1104.76 · `data-start 58.5` / `data-duration 15.5`
- **Speaker mode:** full-frame (both speakers, dark gradient backdrop) for the count + kinetic; settles to Mode A on exit (~74.0). This is the **only** 25× appearance in the clip (v1 had three).
- **Treatment:** `apple-money-count`-style — a big number **counts up 1× → 25×** with a glow flash + subtle particle pop on landing (catalog motion), NOT the swiss-grid index/eyebrow/footer chrome.
- **Lines / count — WORD-SYNCED:**
  - Eyebrow **"DERIVATIVES vs SPOT"** — `#F0F0F0` Inter 700 32px `<!-- EDITORIAL: structural label -->` fire ~comp 60.5 (as he says "leverage the spot ratio"@`leverage`1091.64=comp 60.88).
  - **Count-up to "25×"** — lands on spoken **"20 or 25x"** (`25x.`@1094.52=comp 63.76). Count runs comp ~61.0 → **63.76** (glow flash + particle pop ON 63.76). `#FFFFFF` 200px stat; the count is the white display.
  - **"25 TIMES MORE"** (kinetic line) — transcript **"25 … times … more"** (`25`@1095.90=comp 65.14, `times`@1096.44=comp 65.68, `more`@1097.32=comp 66.56) → slam **comp 65.14** `#FFFFFF`.
  - **"DERIVATIVES THAN SPOT"** — transcript **"derivatives trade than spots"** (`derivatives`@1097.64=comp 66.88, `than`@1098.38=comp 67.62, `spots,`@1098.60=comp 67.84) → slam **comp 66.9** `#FFFFFF`.
  - **"MELT-UP TO $226K"** (cyan payoff) — transcript **"the melt up … before 226k"** (`melt`@1100.68=comp 69.92, `up`@1101.00=comp 70.24, `226k`@1102.58=comp 71.82) → slam cyan **comp 69.92**, "$226K" emphasized on **comp 71.82**.
- **Cyan element:** "MELT-UP TO $226K" payoff line (single cyan; the 25× count is white per D7 "stat OR rule/accent, not both" — the cyan accent is the payoff line, count stays white).
- **Anti-static:** continuous count-up motion 61→63.76 with the landing flash, then word-synced slams — full kinetic motion across the beat. Exits ~comp 73.4.
- **Date note (D7):** Oct 10 crash is **2025** (literal event date, prior year) — labels say "OCT 2025"; the $226K melt-up is the same Oct-2025 event, no relabel.

### c4b6 — swiss-grid (micro-stat, the leverage ratio) · Mode A · `beat-c4b6-supported-leverage.html`
- **Comp:** 74.4–80.0 · **Src:** 1105.16–1110.76 · `data-start 74.4` / `data-duration 5.6`
- **Speaker mode:** Mode A.
- **Why swiss-grid here (not kinetic):** breaks the c4b5→c4b8 kinetic adjacency (no same template twice in a row) and gives the "supported by leverage" claim a clean data anchor. This is a **single micro-stat**, deliberately minimal (NOT the full opening chrome) so it doesn't re-introduce the formulaic look — one stat + one label only.
- **Content (exact text + hex):**
  - Eyebrow **"THE TAKEAWAY"** — `#F0F0F0` Inter 700 32px `<!-- EDITORIAL: structural label -->`
  - Cyan rule (3px) `#00D4FF` — draws `scaleX 0→1`.
  - Stat **"20–25×"** — `#FFFFFF` Inter 900 200px tabular-nums.
  - Label **"LEVERAGE : SPOT RATIO ON VOLUMES"** — `#F0F0F0` Inter 700 36px.
  - Sub **"the $226K melt-up was supported by it"** — `#C4C9D0` Inter 600 26px.
- **Timing — WORD-CUED:** fires as Jasper says **"supported by leverage"** — `supported`@1106.24=comp 75.48, `leverage.`@1106.96=comp 76.20. Chrome in comp ~74.6, stat slams **comp 75.5**, label/sub by comp ~76.4. (The "20 or 25×" number he stated at `25x.`@1094.52 / restated logic; the on-screen "20–25×" is the literal ratio he gives: "leverage the spot ratio on volumes was like 20 or 25x" — verified.)
- **Cyan element:** the rule (single cyan; the 200px stat is white per D7 "stat OR rule, not both"). Exits ~comp 79.4.

### c4b8 — kinetic-type (human closer) · full-frame · `beat-c4b8-wiped-out.html`
- **Comp:** 80.4–88.2 · **Src:** 1110.76–1118.98 · `data-start 80.4` / `data-duration 7.8`
- **Speaker mode:** full-frame (both speakers, dark gradient backdrop). Video expands to full-frame at ~80.2 and **stays live through clip end** — no card, no end screen (D4 no-outro).
- **Kinetic lines — WORD-SYNCED (the human cost — varies the ending from a stat callback):**
  - **L1 "NEW TO PERPS"** — transcript **"new to perp"** (`new`@1112.58=comp 81.82, `to`@1112.86=comp 82.10, `burp`/perp@1113.08=comp 82.32) → slam **comp 81.82** `#FFFFFF`. *(Whisper mis-hears "perps" as "burp"; on-screen uses the correct term "PERPS".)*
  - **L2 "CROSS-MARGINING ON"** — transcript **"cross margining enabled"** (`cross`@1114.66=comp 83.90, `margining`@1115.04=comp 84.28, `enabled`@1115.56=comp 84.80) → slam **comp 83.90** `#FFFFFF`.
  - **L3 "WIPED OUT"** (cyan payoff) — transcript **"absolutely … wiped out"** (`wiped`@1117.92=comp 87.16, `out.`@1118.26=comp 87.50) → slam cyan **comp 87.16** `#00D4FF` + glow.
- **Cyan element:** L3 "WIPED OUT" payoff (single cyan).
- **Clip end:** after L3 lands (~87.5), holds ~0.5s, clip ends at comp 88.2 on live full-frame video (no outro, D4). The closer is the human consequence ("a lot of people… new to perps… cross-margining… absolutely wiped out"), which is a different ENDING than the v1 25× stat callback — fixes the repetition.

---

## Verification gate (this clip)
- **Rule 1:** opening kinetic = literal spoken words at the new in-point (`your delta` comp 0.00–0.16; `completely shifts` comp 0.48–0.98). No anticipatory text. ✓
- **Rule 2:** opens on kinetic (not swiss-grid chrome); cascade is the centerpiece (beat 2); 25× appears once; template sequence kinetic→flowchart→slam→liquid-glass→money-count→swiss-grid→kinetic with no identical adjacency. ✓
- **Rule 3:** object-position `83% center`, verified against frames at 1044.7 and 1090.9 (Jasper centered, seam/host excluded, name kept). ✓
- Beat count = 8. One cyan element per beat (listed each beat). Every kinetic line carries a real `comp_t` from the table below; the only EDITORIAL marks are structural eyebrow/flow-node labels. ✓
- No outro / no intro (D4): ends on live full-frame video after a content kinetic; no name card, no CTA. ✓
- Date context (D7): Oct 10 crash + $226K melt-up labeled **2025** (literal prior-year event date). ✓

---

## Inlined word table (re-derived for src_in = 1030.76; comp = src − 1030.76)

```
comp_t   src_t    word
  0.00  1030.76  your        <- c4b1 L1
  0.16  1030.92  delta       <- c4b1 L1
  0.48  1031.24  completely  <- c4b1 L2 (cyan)
  0.98  1031.74  shifts      <- c4b1 L2 (cyan)
  1.46  1032.22  in
  1.62  1032.38  your
  1.74  1032.50  structure
  2.12  1032.88  where
  2.40  1033.16  you
  2.96  1033.72  would
  3.10  1033.86  be
  3.20  1033.96  delta
  3.46  1034.22  neutral,    <- c4b2 node1 cue "delta neutral"
  4.02  1034.78  let's
  4.18  1034.94  say,
  4.50  1035.26  like
  4.64  1035.40  your
  5.44  1036.20  long
  6.80  1037.56  spot,
  7.36  1038.12  you're
  7.52  1038.28  short
  7.86  1038.62  to
  8.04  1038.80  the
  8.14  1038.90  burp(perp).
  9.30  1040.06  The
  9.78  1040.54  like
 10.26  1041.02  spots
 10.88  1041.64  goes
 11.60  1042.36  down
 11.92  1042.68  negatively,
 12.64  1043.40  like
 12.76  1043.52  meaningfully.
 13.84  1044.60  Your
 13.92  1044.68  burp(perp)
 14.32  1045.08  is
 14.58  1045.34  deeply
 14.98  1045.74  in
 15.12  1045.88  the
 15.20  1045.96  money.
 15.68  1046.44  You
 15.70  1046.46  get
 15.88  1046.64  closed       <- c4b2 node2 cue "closed out"
 16.24  1047.00  out          <- c4b2 node2 cue
 16.54  1047.30  and
 16.76  1047.52  therefore
 17.04  1047.80  you
 17.22  1047.98  have
 17.40  1048.16  a
 17.70  1048.46  naked        <- c4b2 node3 cue "naked long delta"
 18.14  1048.90  long         <- c4b2 node3 cue
 18.52  1049.28  delta.       <- c4b2 node3 cue
 19.66  1050.42  But
 19.74  1050.50  as
 20.02  1050.78  a
 20.10  1050.86  result,
 20.62  1051.38  I
 20.64  1051.40  think
 20.84  1051.60  a
 21.12  1051.88  lot
 21.20  1051.96  of
 21.30  1052.06  people
 21.62  1052.38  close
 22.00  1052.76  out
 22.18  1052.94  that
 22.38  1053.14  position,
 23.06  1053.82  creating
 23.72  1054.48  this
 24.04  1054.80  very
 24.40  1055.16  strong
 24.74  1055.50  feedback     <- c4b2 node4 cue "feedback loop"
 25.16  1055.92  loop         <- c4b2 node4 cue
 25.62  1056.38  of
 26.00  1056.76  continuous
 26.78  1057.54  pressure
 27.28  1058.04  into
 27.62  1058.38  the
 27.78  1058.54  market,
 28.32  1059.08  which
 28.84  1059.60  then
 29.06  1059.82  led
 29.26  1060.02  to
 29.44  1060.20  like,
 29.96  1060.72  as
 30.12  1060.88  we
 30.22  1060.98  all
 30.36  1061.12  know,
 30.64  1061.40  like
 30.80  1061.56  some
 31.16  1061.92  alts
 31.42  1062.18  were
 31.56  1062.32  down
 31.70  1062.46  like
 31.90  1062.66  60,          <- c4b2 node5 cue (cyan)
 32.40  1063.16  70,          <- c4b2 node5 cue (cyan)
 32.78  1063.54  80%.         <- c4b2 node5 cue (cyan)
 33.26  1064.02  It
 34.36  1065.12  was
 34.52  1065.28  extremely    <- c4b3 "EXTREMELY"
 34.98  1065.74  hectic,      <- c4b3 "HECTIC" (cyan)
 35.44  1066.20  but
 35.90  1066.66  also
 36.24  1067.00  I
 36.58  1067.34  think
 36.78  1067.54  it
 37.10  1067.86  was
 37.26  1068.02  shorter
 37.76  1068.52  than
 38.84  1069.60  a
 39.14  1069.90  lot
 39.24  1070.00  of
 39.36  1070.12  people
 39.62  1070.38  think.
 41.50  1072.26  Like
 41.94  1072.70  that
 42.28  1073.04  real
 43.46  1074.22  compression
 44.20  1074.96  and
 44.54  1075.30  the
 44.66  1075.42  stress
 45.00  1075.76  was
 45.62  1076.38  over
 45.92  1076.68  a
 46.10  1076.86  shorter
 46.30  1077.06  period
 46.64  1077.40  of
 46.82  1077.58  time
 47.00  1077.76  than
 47.16  1077.92  I
 47.28  1078.04  think
 47.44  1078.20  a
 47.56  1078.32  lot
 47.64  1078.40  of
 47.76  1078.52  people
 48.12  1078.88  like
 49.22  1079.98  appreciate.
 50.36  1081.12  It
 50.70  1081.46  was
 50.84  1081.60  really,
 51.12  1081.88  I
 51.30  1082.06  think,
 51.58  1082.34  half         <- c4b4 card entry cue "half an hour to 45 min"
 51.84  1082.60  an
 52.00  1082.76  hour
 52.10  1082.86  to
 52.24  1083.00  45           <- c4b4 cue
 52.64  1083.40  minutes      <- c4b4 cue
 52.92  1083.68  before
 53.22  1083.98  everything
 53.60  1084.36  picked
 53.90  1084.66  up
 54.10  1084.86  back
 54.32  1085.08  up.
 54.54  1085.30  But
 55.04  1085.80  the
 55.18  1085.94  real
 55.42  1086.18  damage,
 55.80  1086.56  I
 56.00  1086.76  think,
 56.34  1087.10  was
 56.46  1087.22  then
 56.70  1087.46  on
 57.18  1087.94  the
 57.96  1088.72  liquidation
 58.76  1089.52  on
 58.90  1089.66  the
 58.98  1089.74  burp(perp)
 59.24  1090.00  side,
 59.62  1090.38  right?
 59.84  1090.60  I
 59.92  1090.68  think
 60.16  1090.92  like
 60.88  1091.64  leverage     <- c4b5 eyebrow cue / c4b6 context
 61.34  1092.10  the
 61.60  1092.36  spot
 61.84  1092.60  ratio
 62.26  1093.02  on
 62.44  1093.20  volumes
 62.84  1093.60  was
 63.10  1093.86  like
 63.24  1094.00  20
 63.60  1094.36  or
 63.76  1094.52  25x.         <- c4b5 count-up lands "25×"
 64.80  1095.56  So
 64.80  1095.56  there
 64.94  1095.70  was
 65.14  1095.90  25           <- c4b5 "25 TIMES MORE"
 65.68  1096.44  times        <- c4b5
 66.56  1097.32  more         <- c4b5
 66.88  1097.64  derivatives  <- c4b5 "DERIVATIVES THAN SPOT"
 67.36  1098.12  trade
 67.62  1098.38  than         <- c4b5
 67.84  1098.60  spots,       <- c4b5
 68.48  1099.24  meaning
 68.60  1099.36  that
 68.92  1099.68  the
 69.92  1100.68  melt         <- c4b5 "MELT-UP TO $226K" (cyan)
 70.24  1101.00  up           <- c4b5 (cyan)
 70.40  1101.16  which
 70.92  1101.68  we
 71.12  1101.88  saw
 71.34  1102.10  before
 71.82  1102.58  226k         <- c4b5 "$226K" (cyan)
 73.30  1104.06  was
 74.22  1104.98  very
 75.08  1105.84  heavily
 75.48  1106.24  supported    <- c4b6 stat cue "supported by leverage"
 75.96  1106.72  by
 76.20  1106.96  leverage.    <- c4b6 cue
 76.60  1107.36  And
 77.14  1107.90  then
 77.26  1108.02  if
 77.54  1108.30  you
 78.46  1109.22  have
 78.72  1109.48  like
 78.92  1109.68  a
 79.12  1109.88  lot
 79.22  1109.98  of
 79.34  1110.10  liquidation,
 80.16  1110.92  I
 80.22  1110.98  think
 80.38  1111.14  also
 80.60  1111.36  a
 80.84  1111.60  lot
 80.92  1111.68  of
 81.06  1111.82  people
 81.38  1112.14  were
 81.58  1112.34  quite
 81.82  1112.58  new          <- c4b8 L1 "NEW TO PERPS"
 82.10  1112.86  to           <- c4b8 L1
 82.32  1113.08  burp(perp)   <- c4b8 L1 (on-screen "PERPS")
 82.64  1113.40  taxes,
 83.50  1114.26  having
 83.68  1114.44  like
 83.90  1114.66  cross        <- c4b8 L2 "CROSS-MARGINING ON"
 84.28  1115.04  margining    <- c4b8 L2
 84.80  1115.56  enabled      <- c4b8 L2
 85.18  1115.94  on
 85.38  1116.14  their
 85.52  1116.28  accounts,
 85.98  1116.74  like
 86.14  1116.90  absolutely
 86.70  1117.46  like
 87.16  1117.92  wiped        <- c4b8 L3 "WIPED OUT" (cyan)
 87.50  1118.26  out.         <- c4b8 L3 (cyan)
 88.22  1118.98  So           <- clip end (src_out 1118.98)
```

*(Whisper transcribes "perp/perps" as "burp" throughout — on-screen text uses the correct trading term "PERP/PERPS". This is a transcription artifact, not invented content.)*
