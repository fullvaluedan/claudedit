# Clip 5 — Capital Rotation (FINAL, build-ready EDL)

**Slug:** `clip-5-capital-rotation` | **Source window:** 1120s–1300s | **Duration:** 180s
**Comp offset:** comp_t = src_t − 1120
**Theme:** Post-Oct-10, retail pivoted aggressively into equities; JPMorgan prime-brokerage data confirms retail equity activity at an all-time high; crypto vol compressed while equity vol rose, so retail follows the vol trade.

**Directives applied:** D1 (clip-2 opening), D2 (word-sync from clip5-words.txt), D3 (c5b4 → swiss-grid, c5b6 → liquid-glass), D4 (no outro), D5 (hook replaced with "THE MARGINAL / RISK DOLLAR / WENT INTO EQUITIES"), D6 (the 18s c5b7 clean window split with a verified host-question kinetic), D7 (palette/type), D9 (c5b11 closer = verified vol-trade line; fabricated "NOT ENOUGH CAPITAL TO PUMP" REMOVED).

**Beat count:** 12 (within the D-table 11–13 range)

---

## Opening Hook (EDITORIAL — D5 replacement, D1 anticipatory)

The hook is the thesis-grade Wintermute Weekly line, fired anticipatorily over full-frame video (both speakers) before Jasper reaches it. It is NOT word-synced.

- Line 1: **"THE MARGINAL"** — fires comp t=0.08 (white, 130px) `<!-- EDITORIAL: not word-synced -->`
- Line 2: **"RISK DOLLAR"** — fires comp t=0.88 (white, 130px) `<!-- EDITORIAL: not word-synced -->`
- Line 3: **"WENT INTO EQUITIES"** — fires comp t=1.60 (cyan `#00D4FF`, 130px) `<!-- EDITORIAL: not word-synced -->`

The verbatim spoken instance of this line lands later in-clip (comp 70.0–72.48) and is the c5b6 liquid-glass card payload, so the hook reads as a confirmation when Jasper says it.

---

## Beat Map

Speaker mode legend: **full-frame** = video 1920×1080 both speakers (kinetic overlay beats); **Mode A** = video reframed right 40%, 85% scale (clip-2 v13).

### c5b1 — Opening hook (kinetic-type)
- **Comp:** 0.0–3.0s | **Src:** 1120.0–1123.0s
- **Template (FINAL):** kinetic-type (hook)
- **Speaker mode:** full-frame (both speakers), per D1 — video animates to Mode A at t≈3.0
- **Sub-comp:** `beat-c5b1-hook-marginal-risk-dollar.html`
- **Content / lines:**
  - "THE MARGINAL" @ 0.08 — white #F0F0F0 130px — `EDITORIAL`
  - "RISK DOLLAR" @ 0.88 — white #F0F0F0 130px — `EDITORIAL`
  - "WENT INTO EQUITIES" @ 1.60 — cyan #00D4FF 130px (single cyan element) — `EDITORIAL`
  - Whole stack drifts up/out at 2.8s; video begins Mode A transition at 3.0 (expo.inOut 0.4s, clip-2 pattern).
- **Cyan:** payoff line "WENT INTO EQUITIES".

### c5b2 — Index / eyebrow launch (swiss-grid)
- **Comp:** 3.0–18.0s | **Src:** 1123.0–1138.0s
- **Template (FINAL):** swiss-grid (index/eyebrow + before→after comparison)
- **Speaker mode:** Mode A
- **Sub-comp:** `beat-c5b2-rotation-index.html`
- **Content (all text):**
  - Index **"05"** + eyebrow **"CAPITAL ROTATION · OCT 2025"** (Inter 700, 32px, #F0F0F0) slam in @ 3.0
  - Cyan rule draws left→right @ 3.4 (single cyan element)
  - Before→after columns @ 4.0: LEFT **"CRYPTO / ALTCOINS"** (muted #F0F0F0 dim, struck) → RIGHT **"EQUITIES"** (#F0F0F0 active), pivot label between: **"OCT 10 LIQUIDATION →"**
  - Date row @ 4.8: **"OCT 2025"** → **"NOV 2025 – MAY 2026"** (#F0F0F0; per D7, "this year" framing — never decaying-opacity grey)
  - Tag row @ 5.8: **"NOVEMBER · DECEMBER · JANUARY · FEBRUARY"** (Inter 600)
- **Cyan:** the horizontal rule only (NOT the columns).
- **Opening 6s element types (D1):** hook kinetic (1) + index/eyebrow (2) + rule (3) + before/after columns (4) + tag row (5) → PASS.

### c5b3 — "retail pivoted aggressively into equity" (kinetic-type)
- **Comp:** 18.0–31.0s | **Src:** 1138.0–1151.0s
- **Template (FINAL):** kinetic-type
- **Speaker mode:** full-frame (both speakers)
- **Sub-comp:** `beat-c5b3-retail-pivoted.html`
- **Content / lines (word-synced, comp_t read from clip5-words.txt):**
  - "RETAIL PIVOTED" @ **15.84** (word "pivoted" = comp 15.84; "retail" itself is @ 5.56 earlier, so fire the line on "pivoted" per D2 first-word rule) — white 130px
  - "VERY AGGRESSIVELY" @ **17.10** (word "aggressively" = comp 17.10) — white 130px
  - "INTO EQUITY" @ **18.08** (word "equity" = comp 18.08) — cyan #00D4FF 130px (payoff)
  - Stack stays (no dim) through beat end ~30.8.
- **Cyan:** "INTO EQUITY".
- **Note:** Beat window opens at comp 18.0 but lines 1–2 fire at 15.84/17.10 — these spoken words sit just before the nominal window. Set this beat's `data-start` = 15.5 and `data-duration` ≥ 16 so all three fire-times (15.84, 17.10, 18.08) have ≥0.3s headroom. (Window in the table above is the visual hold; the GSAP fire-times are the table values.)

### c5b4 — JP Morgan all-time-high stat (swiss-grid)  ← D3 SWAP (was liquid-glass)
- **Comp:** 31.0–51.0s | **Src:** 1151.0–1171.0s
- **Template (FINAL):** **swiss-grid** (per D3: "ALL-TIME HIGH" is a stat — slam at 200px)
- **Speaker mode:** Mode A
- **Sub-comp:** `beat-c5b4-jpm-all-time-high.html`
- **Content (all text, exact hex):**
  - Eyebrow **"JP MORGAN PRIME BROKERAGE · MAY 2026"** (Inter 700, 32px, #F0F0F0) — slam @ 36.38 (word "JP" = comp 36.38)
  - Stat **"ALL-TIME HIGH"** in 200px Inter 800 #F0F0F0 — slam @ 44.16 (word "high" = comp 44.16). No count-up (not a number).
  - Sublabel **"RETAIL EQUITY ACTIVITY"** (Inter 600, #F0F0F0) @ 41.84 (word "activity" = comp 41.84)
  - Footer **"BY A MEANINGFUL MARGIN"** (Inter 600, #F0F0F0) @ 45.08 (word "margin" = comp 45.08)
  - Cyan accent: a single short cyan rule beneath the stat (drawn @ 44.5). (Swiss-grid rule = the one cyan element; stat stays white.)
- **Cyan:** the rule beneath the stat (per D7 swiss-grid = stat OR rule, not both → rule chosen so the 200px stat reads white).

### c5b5 — "the marginal risk dollar" (kinetic-type)
- **Comp:** 51.0–68.0s | **Src:** 1171.0–1188.0s
- **Template (FINAL):** kinetic-type
- **Speaker mode:** full-frame (both speakers)
- **Sub-comp:** `beat-c5b5-marginal-risk-dollar.html`
- **Content / lines (word-synced):**
  - "THE MARGINAL" @ **70.00** (word "marginal" = comp 70.00) — white 130px
  - "RISK DOLLAR" @ **71.44** (word "dollar" = comp 71.44) — white 130px
  - "WENT INTO EQUITIES" @ **72.20** (word "into" = comp 72.20; "equities" = 72.48) — cyan #00D4FF 130px (payoff)
  - Stack stays through ~74.0.
- **Cyan:** "WENT INTO EQUITIES".
- **Note:** Spoken words land comp 70.0–72.48 — set `data-start` = 69.7, `data-duration` ≥ 5. The visual window 51–68 above is the beat's screen-hold lead-in; GSAP fires on the table comp_t values. (The line is verbatim the c5b6 card text, deliberately echoed.)

### c5b6 — Wintermute Weekly pull-quote (liquid-glass card)  ← D3 SWAP (was decision-tree)
- **Comp:** 68.0–88.0s | **Src:** 1188.0–1208.0s
- **Template (FINAL):** **liquid-glass card** (per D3 — resolves the c5b5→c5b6 consecutive-kinetic issue)
- **Speaker mode:** Mode A
- **Sub-comp:** `beat-c5b6-wintermute-weekly-quote.html`
- **Content (all text, exact hex):**
  - Eyebrow **"WINTERMUTE WEEKLY NOTE"** (Inter 700, 32px, #F0F0F0)
  - Pull-quote **"The marginal risk dollar went into equities, not crypto."** (Inter 700, 64px, #F0F0F0)
  - Attribution **"Jasper De Maere · Wintermute Weekly"** (Inter 600, 32px, #F0F0F0)
  - Card spec (D7): `background: rgba(20,26,34,0.92)`, **4px cyan `#00D4FF` accent bar** (inset left edge, NOT border-left), soft glow `0 0 40px rgba(0,212,255,0.10)`, 1px border, `mask-image` feather. NO backdrop-filter blur, NO grain.
  - Card slides in from right @ 68.9 (word "marginal" spoken @ 70.0 — card lands just before the quote is uttered, then holds as Jasper says it verbatim).
- **Cyan:** the 4px accent bar.

### c5b7 — Host question (kinetic-type)  ← D6 SPLIT of the old 18s clean window
- **Comp:** 88.0–106.0s | **Src:** 1208.0–1226.0s
- **Template (FINAL):** kinetic-type (host-question stack)
- **Speaker mode:** full-frame (both speakers)
- **Sub-comp:** `beat-c5b7-is-crypto-dead-host-q.html`
- **Content / lines (word-synced — verified host line "is crypto dead for retail these days"):**
  - "IS CRYPTO" @ **80.44** (word "crypto" = comp 80.44) — white 130px
  - "DEAD FOR RETAIL" @ **81.28** (word "retail" = comp 81.28) — white 130px
  - "THESE DAYS?" @ **81.80** (word "days" = comp 81.80) — cyan #00D4FF 130px (payoff)
  - Stack stays ~3s, then clears; the back half of this window (comp ~84–106) is clean Mode A video (Jasper's "no, it's not… I do think retail" + 2021-exuberance answer). This keeps any single clean stretch under ~8s (D6).
- **Cyan:** "THESE DAYS?".
- **Note:** This is the verified host question that splits the formerly-18s clean window. `data-start` = 80.1, `data-duration` ≥ 2.5. Per D2, a host-question stack is legitimate; words are real (comp 80.44 / 81.28 / 81.80).

### c5b8 — 2021 exuberance benchmark (decision-tree)
- **Comp:** 106.0–125.0s | **Src:** 1226.0–1245.0s
- **Template (FINAL):** decision-tree (causal chain — what retail calls an "alt season")
- **Speaker mode:** Mode A
- **Sub-comp:** `beat-c5b8-2021-exuberance.html`
- **Content (all text):**
  - Eyebrow **"WHAT RETAIL CALLS 'ALT SEASON'"** (Inter 700, 32px, #F0F0F0)
  - 3-step chain, nodes pop back.out(1.5) 0.35s apart:
    1. **[2021 EXTREME EXUBERANCE]**
    2. **[MASSIVE CAPITAL INJECTION]**
    3. **[ALL RISK ASSETS MOVED UP]** — cyan #00D4FF final node
  - Sublabel **"The benchmark retail still anchors to"** (Inter 600, #F0F0F0)
  - First node reveal @ 100.16 (word "exuberance" = comp 100.16); chain completes by ~107.5 (word "moved up" @ 107.42). The Mode-A graphic then holds while Jasper continues ("I don't think retail is gone forever").
- **Cyan:** final node "[ALL RISK ASSETS MOVED UP]".

### c5b9 — "volatility in crypto compressed" (kinetic-type)
- **Comp:** 125.0–149.0s | **Src:** 1245.0–1269.0s
- **Template (FINAL):** kinetic-type
- **Speaker mode:** full-frame (both speakers)
- **Sub-comp:** `beat-c5b9-vol-compressed.html`
- **Content / lines (word-synced — verified, late-window per QA correction):**
  - "VOLATILITY IN CRYPTO" @ **150.62** (word "volatility" = comp 150.62; "crypto" = 151.52) — white 130px
  - "COMPRESSED" @ **151.94** (word "compressed" = comp 151.94) — white 130px
  - "NO LONGER THE GO-TO" @ **155.72** (word "no" = comp 155.72; "longer" 155.96; "go" 156.84) — cyan #00D4FF 130px (payoff)
  - Stack stays through ~158.
- **Cyan:** "NO LONGER THE GO-TO".
- **Note (QA fix):** the original placed this at comp 125 with a fabricated "src ~1192." The verified spoken vol-compression line is at comp 150.62–157.80. The beat's visual window opens at 125 (graphic-density), but the GSAP fire-times are the table values (150.62 / 151.94 / 155.72). `data-start` = 150.3, `data-duration` ≥ 8. Mode-A video covers comp 125–150 (Jasper's "complimentary to crypto… return/risk/volatility profile" build).

### c5b10 — Vol comparison (swiss-grid)
- **Comp:** 149.0–162.0s | **Src:** 1269.0–1282.0s
- **Template (FINAL):** swiss-grid (two-column comparison)
- **Speaker mode:** Mode A
- **Sub-comp:** `beat-c5b10-vol-comparison.html`
- **Content (all text, exact hex):**
  - Eyebrow **"VOLATILITY PROFILE · CRYPTO vs EQUITIES"** (Inter 700, 32px, #F0F0F0)
  - LEFT column **"CRYPTO VOL"** + **"COMPRESSED ↓"** (directional down indicator `#FF4D4F`)
  - RIGHT column **"EQUITY VOL"** + **"RISING ↑"** (directional up indicator `#16C784`)
  - Sublabel **"Retail follows the risk-on vol trade"** (Inter 600, #F0F0F0)
  - Cyan accent: a single cyan rule between the two columns (drawn @ 160.06, word "became more volatile" = comp 160.06–160.52). Columns reveal left-first 0.5s gap, starting @ 159.48 (word "equity market" = comp 159.48).
- **Cyan:** the divider rule (the red/green are directional market indicators per D7 palette, NOT the cyan accent — exactly one cyan element).

### c5b11 — Verified closer "they just want a vol trade" (kinetic-type)  ← D9 (fabricated line REMOVED)
- **Comp:** 162.0–178.0s | **Src:** 1282.0–1298.0s
- **Template (FINAL):** kinetic-type
- **Speaker mode:** full-frame (both speakers)
- **Sub-comp:** `beat-c5b11-just-want-vol-trade.html`
- **Content / lines (word-synced — VERIFIED real spoken closer; replaces fabricated "NOT ENOUGH CAPITAL TO PUMP"):**
  - "THEY DON'T CARE" @ **168.28** (word "really" = comp 168.28; "care" = 168.52 — line on "don't really care about the underlying") — white 130px
  - "ABOUT THE UNDERLYING" @ **169.28** (word "underlying" = comp 169.44; fire on "about" @ 169.08) — white 130px
  - "THEY JUST WANT A VOL TRADE" @ **172.18** (word "volatility" = comp 172.18; "trade" = 172.64) — cyan #00D4FF 130px (payoff)
  - Stack stays through ~175.
- **Cyan:** "THEY JUST WANT A VOL TRADE".
- **Note (D9):** verified against clip5-words.txt: "they don't really care about the underlying. They just want to have a volatility trade around." (comp 167.56–173.36). This is the thesis-closing line and the clean out-point.

### c5b12 — Clean close (clean video window)  ← D4 (no outro card)
- **Comp:** 178.0–180.0s | **Src:** 1298.0–1300.0s
- **Template (FINAL):** clean video window (no graphic)
- **Speaker mode:** Mode A
- **Sub-comp:** *(none — clean video; no sub-comp file)*
- **Content:** Jasper finishes "equity markets are offering that exact thing… so that I think is one of the main reasons" (comp 174.72–179.96). Final ~2s is clean Mode-A video — NOT a card holding to the end (D4). Ends the clip on a content beat.
- **Cyan:** none (clean video).

---

## Verification

**Beat count:** 12 — within the D-table range (11–13) for clip 5. ✓

**Template sequence (no two identical in a row):**
kinetic (c5b1) → swiss-grid (c5b2) → kinetic (c5b3) → swiss-grid (c5b4) → kinetic (c5b5) → liquid-glass (c5b6) → kinetic (c5b7) → decision-tree (c5b8) → kinetic (c5b9) → swiss-grid (c5b10) → kinetic (c5b11) → clean (c5b12). No adjacent duplicates. ✓ (The D3 swap of c5b6 → liquid-glass is what breaks the original c5b5→c5b6 kinetic/“cinematic-split” collision.)

**One cyan element per beat:** ✓ — b1 payoff line; b2 rule; b3 payoff; b4 stat-rule (stat stays white); b5 payoff; b6 accent bar; b7 payoff; b8 final node; b9 payoff; b10 divider rule (red/green are directional indicators, not the accent); b11 payoff; b12 none (clean).

**Every non-editorial kinetic line has a real comp_t from clip5-words.txt:**
- c5b3: pivoted 15.84 / aggressively 17.10 / equity 18.08 ✓
- c5b5: marginal 70.00 / dollar 71.44 / into 72.20 ✓
- c5b7: crypto 80.44 / retail 81.28 / days 81.80 ✓
- c5b9: volatility 150.62 / compressed 151.94 / no-longer-go-to 155.72 ✓
- c5b11: care 168.52 / about 169.08 / volatility-trade 172.18 ✓
- EDITORIAL (not word-synced): c5b1 hook lines 1/2/3 @ 0.08 / 0.88 / 1.60 only. ✓

**D-rule compliance:** D1 opening (full-frame→Mode A @ 3.0, copy clip-2) ✓ · D3 swaps c5b4→swiss-grid, c5b6→liquid-glass ✓ · D4 no outro (ends on clean video c5b12) ✓ · D5 hook = "THE MARGINAL / RISK DOLLAR / WENT INTO EQUITIES", cyan on "EQUITIES" ✓ · D6 the 18s clean window split by verified host-question kinetic c5b7, no clean stretch > ~8s ✓ · D7 palette/type (one cyan/beat, eyebrows Inter 700 ≥32px #F0F0F0, cards rgba(20,26,34,0.92)+4px cyan bar, no blur/grain, no #888888) ✓ · D9 c5b11 = verified vol-trade closer, fabricated "NOT ENOUGH CAPITAL TO PUMP" REMOVED ✓.

**Full-frame kinetic moments (clip > 90s):** c5b3, c5b5, c5b7, c5b9, c5b11 — five, all over both speakers. ✓

## Build Manifest Row
`clip_5 | clip-5-capital-rotation | 1120 | 1300 | kinetic-type,swiss-grid,liquid-glass,decision-tree | 12 beats`
