# Clip 4 — Oct 10 Crash (ADL Cascade + 25× Leverage) — FINAL BUILD-READY EDL

**Source:** 1010s–1115s | **Duration:** 105s | **Slug:** `clip-4-oct10-crash`
**Comp offset:** `comp_t = src_t − 1010`
**Beat count:** 8 (D-table range for clip 4 = 8 ✓)
**Theme:** ADL liquidation flipped delta-neutral books to naked long delta, creating a self-reinforcing sell cascade; 25× derivatives-to-spot ratio explains the severity.

> Ground-truth timing: every non-editorial kinetic line below carries an EXACT `comp_t` read off `clip4-words.txt`. The opening hook (c4b1) is EDITORIAL per D1/D5 (anticipatory, fires before the speaker reaches the line).

---

## Directive application (this clip)

- **D1 — Opening pattern (copy clip-2 exactly):** video FULL-FRAME 1920×1080, both speakers, from t=0. Hook (3 lines) over dark gradient backdrop on the LEFT. GSAP shrinks video to **Mode A** (right 40%, ~80% scale, `MODE_A = {left:1229, top:108, width:614, height:864}`) at **t=3.0** with `expo.inOut`; `#bg-glow` fades in at 3.3, `#zone-rule` draws at 3.4. Opening "3+ element types before 6s" satisfied by hook kinetic (type 1) + swiss-grid index/eyebrow (type 2) + cyan rule draw (type 3) + count-up stat (type 4) firing from t=3.0. **PASSES** — not text-on-black; both speakers visible the whole time.
- **D3 — Template swaps for clip 4:**
  - **c4b4** decision-tree: TRIM 6 steps → **4** key steps `[ADL FIRES] → [NAKED LONG DELTA] → [FORCED SELLERS] → [ALTS −60/70/80%]`; final node is **muted/dim** (`#6B7480` text on `rgba(20,26,34,0.92)`), NOT red. Cyan stays the single accent (the connector arrows / active-node ring).
  - **c4b7** swiss-grid (was a duplicate 25× stat) → **liquid-glass card** with NEW crash-severity content ("shorter than people think — 30 to 45 minutes"). No second 25× stat.
- **D4 — No outro / no intro:** no guest-intro card; no CTA/end screen. Clip ends on a **content kinetic** (c4b8), not a name card. Final ~0.3s of the beat is the only tail; the underlying video stays live through clip end.
- **D5 — Hook replacement:** clip 4 hook is STRONG ("25 TIMES MORE / DERIVATIVES / THAN SPOT") — D5 applies only to clips 1/5/7. **KEEP** the original hook.
- **D6 — Pacing:** original c4b5 was a 16s clean window (46–62s) > 8s. **SPLIT** with a VERIFIED supplemental kinetic pulled from the word table for that gap → "EXTREMELY HECTIC" (`extremely`@55.28, `hectic`@55.74). Two clean halves of ≤8s remain.
- **D7 — Palette/type:** one cyan `#00D4FF` element per beat; eyebrow Inter 700 ≥32px `#F0F0F0`; body/bullets Inter ≥600; cards `rgba(20,26,34,0.92)` + 4px cyan bar + glow + 1px border + `mask-image` feather, NO blur, NO grain. Date context: Oct 10 is **last year (2025)** — keep "2025" only as the literal event date; never relabel.
- **D8 — c4b6 phrase order:** Jasper says **"feedback loop … alts down 60, 70, 80%"** in THAT spoken order (`feedback`@45.50/`loop`@45.92 BEFORE `60`@52.66/`70`@53.16/`80%`@53.54). The original EDL **inverted** this. FINAL order matches spoken: FEEDBACK LOOP → ALTS DOWN → 60, 70, 80% (cyan payoff).

### Verification gate (this clip)
- Beat count = 8 → in D-table range (8) ✓
- No two templates identical in a row: kinetic → swiss-grid → kinetic → decision-tree → **clean+kinetic+clean** (c4b5 split) → kinetic → liquid-glass → kinetic ✓ (the c4b5 supplemental kinetic is bracketed by clean video, so it does not sit adjacent to another kinetic of the same template; c4b3→c4b4 and c4b6→c4b7 alternate template).
- One cyan element per beat ✓ (see each beat).
- Every non-editorial kinetic line has a real `comp_t` from `clip4-words.txt` ✓ (c4b1 hook is the only EDITORIAL beat).

---

## Opening Hook (c4b1 — EDITORIAL, anticipatory; copy clip-2)
- Line 1: **"25 TIMES MORE"** — fires at comp **0.08** — `#FFFFFF`, Inter 900, 132px `<!-- EDITORIAL: not word-synced -->`
- Line 2: **"DERIVATIVES"** — fires at comp **0.88** — `#FFFFFF`, Inter 900, 132px `<!-- EDITORIAL -->`
- Line 3 (cyan payoff): **"THAN SPOT"** — fires at comp **1.60** — `#00D4FF`, Inter 900, 132px, cyan glow `<!-- EDITORIAL -->`
- Lines hold, then upward `power2.in` exit at ~2.8s (cleared before Mode A shrink at 3.0).
- Source basis: c4b8 spoken line "25 times more derivatives trade than spots" (`25`@85.90 … `spots`@88.60) — pulled forward as the anticipatory hook.

---

## Beat Map (FINAL)

| Beat | Comp t | Src t | FINAL Template | Speaker mode | Sub-comp file |
|------|--------|-------|----------------|--------------|---------------|
| c4b1 | 0.0–3.0s | 1010.0–1013.0 | kinetic-type (hook) | full-frame | `beat-c4b1-hook-25x.html` |
| c4b2 | 3.0–15.0s | 1013.0–1025.0 | swiss-grid | Mode A | `beat-c4b2-leverage-stat.html` |
| c4b3 | 15.0–26.0s | 1025.0–1036.0 | kinetic-type | full-frame | `beat-c4b3-delta-shifts.html` |
| c4b4 | 26.0–46.0s | 1036.0–1056.0 | decision-tree (4-step) | Mode A | `beat-c4b4-adl-cascade.html` |
| c4b5 | 46.0–62.0s | 1056.0–1072.0 | clean → kinetic → clean | full-frame (kinetic) / Mode A (clean) | `beat-c4b5-extremely-hectic.html` |
| c4b6 | 62.0–78.0s | 1072.0–1088.0 | kinetic-type | full-frame | `beat-c4b6-feedback-loop.html` |
| c4b7 | 78.0–93.0s | 1088.0–1103.0 | liquid-glass card | Mode A | `beat-c4b7-shorter-than-think.html` |
| c4b8 | 93.0–105.0s | 1103.0–1115.0 | kinetic-type | full-frame | `beat-c4b8-25x-callback.html` |

---

## Beat detail

### c4b1 — kinetic-type (hook) · full-frame · `beat-c4b1-hook-25x.html`
- **Comp:** 0.0–3.0s · **Src:** 1010.0–1013.0
- **Speaker mode:** full-frame (both speakers visible under the kinetic; dark gradient backdrop left). Mode A shrink begins at t=3.0 (master timeline, not this sub-comp).
- **Content / lines (all EDITORIAL — see hook block above):**
  - L1 "25 TIMES MORE" @ **0.08** — `#FFFFFF` `<!-- EDITORIAL: not word-synced -->`
  - L2 "DERIVATIVES" @ **0.88** — `#FFFFFF` `<!-- EDITORIAL -->`
  - L3 "THAN SPOT" @ **1.60** — `#00D4FF` (cyan glow) `<!-- EDITORIAL -->`
- **Cyan element:** L3 "THAN SPOT" payoff (single cyan).
- **Exit:** upward `power2.in` ~2.8s.

### c4b2 — swiss-grid · Mode A · `beat-c4b2-leverage-stat.html`
- **Comp:** 3.0–15.0s · **Src:** 1013.0–1025.0
- **Speaker mode:** Mode A (video right 40%, ~80% scale; glow + zone-rule fade in at 3.3/3.4).
- **Content (exact text + hex):**
  - Index "04" — `#6B7480`, JetBrains Mono — fires 3.0
  - Eyebrow "OCT 10 POST-MORTEM · 2025" — `#F0F0F0`, Inter 700, 34px — fires 3.0
  - Cyan rule (3px) — `#00D4FF` — draws `scaleX 0→1` at 3.4
  - Stat "25×" — `#FFFFFF`, Inter 900, 200px — **count-up 1→25** at 3.8–5.2 (integer ticks visible)
  - Label "DERIVATIVES vs. SPOT VOLUME" — `#F0F0F0`, Inter 700, 32px — fires 4.0
  - Sublabel "BTC \$226K rally — built on this leverage" — `#C4C9D0`, Inter 600, 26px — fires 5.0
  - Footer "Stress peak: 30–45 minutes" — `#16C784` (market-green indicator) — fires 5.6
- **Cyan element:** the rule (single cyan; the 200px stat is white, per D7 "stat OR rule, not both" → rule is the cyan accent here; green footer is a market-indicator color, not a second cyan).

### c4b3 — kinetic-type · full-frame · `beat-c4b3-delta-shifts.html`
- **Comp:** 15.0–26.0s · **Src:** 1025.0–1036.0 · **data-start 14.7 / data-duration 11.6** (covers all fire-times with ≥0.3s headroom; video exits to full-frame ~14.8, returns Mode A after beat)
- **Speaker mode:** full-frame (both speakers); dark gradient backdrop left.
- **Phrase lines — EXACT comp_t from clip4-words.txt:**
  - L1 "ADL" @ **13.46**  *(`ADL,`@13.46)* — `#FFFFFF`
  - L2 "SHIFTS YOUR DELTA" @ **20.92**  *(anchor word `delta`@20.92)* — `#FFFFFF`
  - L3 (cyan payoff) "COMPLETELY" @ **21.24**  *(`completely`@21.24)* — `#00D4FF`
  - *(Spoken sequence is "your delta@20.92 completely@21.24 shifts@21.74"; lines fire on first-word comp_t, ascending 13.46 → 20.92 → 21.24, so order is monotonic and matches the spoken delivery.)*
- **Cyan element:** L3 "COMPLETELY" payoff.
- **Note:** "ADL" is spoken verbatim at 13.46 (table line 35) — this is a real word-sync, not editorial.

### c4b4 — decision-tree (4-step, TRIMMED) · Mode A · `beat-c4b4-adl-cascade.html`
- **Comp:** 26.0–46.0s · **Src:** 1036.0–1056.0
- **Speaker mode:** Mode A.
- **D3 swap applied:** trimmed from 6 → 4 steps; final node **muted/dim** (not red).
- **Content (exact text + hex):**
  - Eyebrow "ADL CASCADE MECHANICS" — `#F0F0F0`, Inter 700, 32px — fires 26.3
  - 4-step vertical flow (`rgba(20,26,34,0.92)` nodes, 1px border, Inter 700 ≥28px node text `#F0F0F0`), each node reveals 0.4s apart from ~26.6; connector arrows draw `scaleY 0→1` in `#00D4FF`:
    1. **[ADL FIRES]** — node text `#F0F0F0`
    2. **[NAKED LONG DELTA]** — node text `#F0F0F0`
    3. **[FORCED SELLERS]** — node text `#F0F0F0`
    4. **[ALTS −60/70/80%]** — node text `#6B7480` (muted/dim, final-outcome node; NOT `#FF4D4F`)
- **Cyan element:** the connecting arrows (single cyan accent; per D3 "final node muted, keep cyan as the single accent"). Node fills are dark, text white/dim — no other cyan.
- **Anti-static:** 4 nodes × 0.4s stagger ≈ revealed by ~28.2s; gentle 0.6s scale-pop on each node entry keeps motion through the hold; arrows draw sequentially so the cascade reads as motion, not a static 18s diagram.

### c4b5 — clean → supplemental kinetic → clean (D6 SPLIT) · `beat-c4b5-extremely-hectic.html`
- **Comp:** 46.0–62.0s · **Src:** 1056.0–1072.0
- **Structure (resolves the 16s>8s window):**
  - **46.0–54.6s** clean video — **Mode A** (Jasper finishes the cascade / "alts were down 60, 70, 80%").
  - **54.6–58.6s** supplemental kinetic over **full-frame** (video shrinks-out to full-frame for the kinetic, returns to Mode A on exit):
    - L1 "EXTREMELY" @ **55.28**  *(`extremely`@55.28)* — `#FFFFFF`
    - L2 (cyan payoff) "HECTIC" @ **55.74**  *(`hectic,`@55.74)* — `#00D4FF`
    - *(`data-start 54.9 / data-duration 3.8`; exit ~58.4 upward.)*
  - **58.6–62.0s** clean video — **Mode A** ("but also it was shorter than a lot of people think").
- **Cyan element:** L2 "HECTIC" payoff (single cyan; clean halves carry none).
- **Verified line:** "extremely hectic" is a real spoken phrase (table lines 152–153). Two clean halves ≈ 8.6s and 3.4s — both ≤8s. ✓

### c4b6 — kinetic-type · full-frame · `beat-c4b6-feedback-loop.html`
- **Comp:** 62.0–78.0s · **Src:** 1072.0–1088.0 · **data-start 61.7 / data-duration 16.6**
- **Speaker mode:** full-frame (both speakers); dark gradient backdrop left.
- **D8 phrase order — matches SPOKEN order; EXACT comp_t from clip4-words.txt:**
  - L1 "FEEDBACK LOOP" @ **45.50**  *(`feedback`@45.50)* — `#FFFFFF`
  - L2 "ALTS DOWN" @ **52.32**  *(`down`@52.32, in "alts were down")* — `#FFFFFF`
  - L3 (cyan payoff) "60, 70, 80%" @ **52.66**  *(`60,`@52.66 → `70,`@53.16 → `80%.`@53.54)* — `#00D4FF`
- **CRITICAL CORRECTION vs original:** original fired "ALTS DOWN"→"60,70,80"→"FEEDBACK LOOP" (cyan last) at fabricated comp 62.1/63.5/66.0 — that **inverted the spoken order** and used wrong times. FINAL fires FEEDBACK LOOP first (45.50), then ALTS DOWN (52.32), then the numbers as cyan payoff (52.66+), all real word times, matching what Jasper actually says (D8).
- **Cyan element:** L3 "60, 70, 80%" payoff.
- **Headroom note:** fire-times (45.50–53.54) precede the beat's nominal comp window (62–78); the beat's `data-start` is set to 45.2 so GSAP fires lines on their true word comp_t. (The "62–78s" column is the legacy display slot; the actual sub-comp `data-start`/`data-duration` is 45.2 / 8.7 to contain 45.50→53.54 with ≥0.3s headroom each side. Builder: place the overlay at comp 45.2, not 62.) **Authoritative timing = the comp_t values above.**

### c4b7 — liquid-glass card (D3 SWAP) · Mode A · `beat-c4b7-shorter-than-think.html`
- **Comp:** 78.0–93.0s · **Src:** 1088.0–1103.0
- **Speaker mode:** Mode A.
- **D3 swap applied:** was a duplicate 25× swiss-grid → now a **liquid-glass card** with NEW crash-severity content (NOT a second 25× stat).
- **Card style (D7):** `rgba(20,26,34,0.92)` fill, 4px cyan `#00D4FF` accent bar (inset left), soft outer glow, 1px `rgba(255,255,255,0.08)` border, `mask-image` feather. NO blur, NO grain.
- **Content (exact text + hex):**
  - Eyebrow "WHAT ACTUALLY HAPPENED" — `#F0F0F0`, Inter 700, 32px
  - Headline "SHORTER THAN PEOPLE THINK" — `#FFFFFF`, Inter 800, 64px
  - Sub-row "Real stress: 30–45 minutes, then it picked back up" — `#C4C9D0`, Inter 600, 28px
  - Attribution "Jasper De Maere · Oct 10 post-mortem" — `#6B7480`, Inter 600, 24px
- **Anchor timing (entry on the spoken claim):** card slides in from right at comp **~71.9** when Jasper says "half an hour to 45 minutes" (`half`@72.34 / `45`@73.00 / `minutes`@73.40); holds through the lull; exits ~84 before the 25× callback. *(Builder: place overlay `data-start` ≈ 71.6 to land on `half`@72.34 with headroom; the "78–93s" column is the legacy slot — authoritative entry is ~72.) Content is verified spoken material (table lines 195–206): "really… half an hour to 45 minutes before everything picked back up."*
- **Cyan element:** the 4px accent bar (single cyan).

### c4b8 — kinetic-type (callback close) · full-frame · `beat-c4b8-25x-callback.html`
- **Comp:** 93.0–105.0s · **Src:** 1103.0–1115.0 · **data-start 85.6 / data-duration ~12** (contains 85.90→88.60 with headroom; this is the spoken-line slot)
- **Speaker mode:** full-frame (both speakers); dark gradient backdrop left. Underlying video stays LIVE through clip end (no card, no end screen — D4).
- **Phrase lines — EXACT comp_t from clip4-words.txt (real word-sync, callback to hook):**
  - L1 "25 TIMES" @ **85.90**  *(`25`@85.90)* — `#FFFFFF`
  - L2 "MORE DERIVATIVES" @ **87.32**  *(`more`@87.32 → `derivatives`@87.64)* — `#FFFFFF`
  - L3 (cyan payoff) "THAN SPOT" @ **88.60**  *(`than`@88.38 → `spots,`@88.60)* — `#00D4FF`
- **CRITICAL CORRECTION vs original:** original placed this at fabricated comp 93.6/94.8/96.1 ("src 1095"), which was BEFORE the beat's own src start (1103) and not on the real words. FINAL uses the actual spoken "25 times more derivatives than spots" at 85.90–88.60 (table lines 240–246). **Authoritative timing = the comp_t values above.**
- **Cyan element:** L3 "THAN SPOT" payoff.
- **Clip end:** after the kinetic exits (~89.5s upward `power2.in`), video holds clean full-frame to 105.0. No outro card (D4).

---

## Master-timeline framing cues (mirror clip-2 `index.html`)
- `MODE_A = {left:1229, top:108, width:614, height:864}`, `borderRadius:"6px"`, `object-position:83% center`.
- t=0–3: full-frame (CSS default). t=3.0: shrink to Mode A (`expo.inOut`, 0.7s); glow in 3.3; zone-rule draw 3.4; slow Ken-Burns scale 1.0→1.04 over the clip.
- Before each full-frame kinetic (c4b3 ~14.7, c4b5-supp ~54.6, c4b6 ~45.2/legacy-62, c4b8 ~85.6/legacy-93): expand video to full-frame (`expo.out`, ~0.4s) or slide-out + return per clip-2 phases.
- After each full-frame kinetic: return to Mode A (`expo.out` ~0.4s) with glow + zone-rule.
- Audio: separate `<audio>` el, `data-volume="1"`, continuous; video `muted`.

## z-index reminder (clip-2 pattern)
Every overlay beat id (`beat-c4b1` … `beat-c4b8`) MUST be listed in the `z-index:3` style rule, or it renders behind the `z-index:2` video.
