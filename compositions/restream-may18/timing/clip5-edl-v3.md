# Clip 5 — Capital Rotation — EDL **v3** (BUILD-READY)

**Slug:** `clip-5-capital-rotation` · **Source:** `clip-2-altcoin-options/source.mp4` (1920×1080 @ 30 fps, side-by-side: Nic host LEFT, Jasper guest RIGHT)
**`src_in` = 1135.5** · **`src_out` = 1298.5** · **duration = 163.0 s** · **`comp = src − 1135.5`**

> The word table `clip5-words.txt` lists `comp = src − 1120`. Every fire-time below is given as **my comp** (`src − 1135.5`) **AND** the table comp it was read from (`= table − 15.5`). Read fire-times off the table — none are hand-computed.

## Why v3 (what the v2 rejections demanded, and the fix in one line each)
- **View flip-flopping (R1):** v2 bounced FULL↔Mode-A ~13 times. v3 has **5 sustained view phases**, every one ≥8 s, no A-B-A inside 12 s. The two formerly-stranded 1-2 s FULL kinetics ("retail moved", "vol compressed") are **folded into the adjacent Mode-A graphic** so the frame never twitches.
- **All-looking-like-clip-2 / kinetic-dominated (R2):** the **5-kinetic run (old beats 6-10) is broken** — max **2** kinetics in a row anywhere. The clip now **leads its back half with the distinct device**: a **before→after rotation card** + a **`data-chart` vol-profile comparison**. Kinetic share 5/11.
- **Jargon errors on screen (R3):** every on-screen string routed through `_JARGON.md` — no burp/deep-in/graft/stake-rate; Wintermute / JP Morgan / Jasper De Maere spelled exactly; "alt season" written correctly (Whisper's "old season" corrected).
- **Duplicate words (R4):** no notable word repeats across a beat's eyebrow vs title/sublabel (audited per beat below — all clean).
- **Opening coherence (R5):** opens on a line **actually spoken in the first ~2.6 s** ("pivoted very aggressively into equity"), parsing as a complete thought; cyan payoff is a real phrase ("INTO EQUITY"), not a dangling number.

---

## VIEW-TIMELINE (proves R1)

`object-position: 83% center`; Mode-A box `{left:1229, top:108, width:614, height:864}` (clip-2 proven, re-verified in v2 against extracted frames — see Framing below).

| phase | view | dwell | beats in phase | content |
|---|---|---:|---|---|
| **0.0–15.5** | **FULL** (both speakers) | **15.2 s** | b1, b2 | intro: 2 kinetics grouped (≤2 rule), video full-frame both speakers w/ dark left-gradient |
| **15.5–64.9** | **Mode-A** (Jasper right, graphics left) | **49.4 s** | b3, b4, b5 | rotation card → JPM all-time-high stat → Wintermute/quote card (3 graphics, ONE stable frame) |
| **64.9–84.1** | **FULL** (both speakers) | **19.2 s** | b6, b7 | Q/A exchange: host question + Jasper's answer (2 kinetics grouped) |
| **84.1–154.6** | **Mode-A** (Jasper right, graphics left) | **70.5 s** | b8, b9, b10 | exuberance flowchart → **vol-profile data-chart** → vol-comparison swiss (3 graphics, ONE stable frame) |
| **154.6–163.0** | **FULL** (both speakers) | **8.4 s** | b11 | closer kinetic, then video settles to clean for the last beat (D4 no-outro) |

**R1 checks — ALL PASS:**
- **No segment < 8 s** outside the 0–6 s intro. Smallest sustained phase = **8.4 s** (closer). ✔
- **No A-B-A within 12 s.** Same-view return gaps: FULL left@15.5→return@64.9 = **49 s**; Mode-A left@64.9→return@84.1 = **19 s**; FULL left@84.1→return@154.6 = **70 s**. All ≫12 s. ✔
- **Consecutive graphic beats grouped into one view:** the two Mode-A phases each carry 3 graphics back-to-back without a single switch. The two FULL phases each carry 2 kinetics. ✔
- **One-liner:** `FULL 15s → Mode-A 49s → FULL 19s → Mode-A 70s → FULL 8s` — 5 phases, all ≥8 s, every A-B-A gap ≥19 s.

### Master-timeline mode toggles (`index.html` GSAP) — only 4 switches in 163 s
| comp | action |
|---|---|
| 0.0 | FULL (CSS default; both speakers; b1 over dark left-gradient) |
| **15.0** | FULL → **Mode-A** (cinematic shrink, clip-2 PHASE-1 tween: `left/top/width/height` to MODE_A, expo.inOut 0.5 s) as b3 rotation card builds |
| **64.4** | **Mode-A → FULL** (video expands back; b6 host-Q fires over both speakers @64.94) |
| **83.6** | FULL → **Mode-A** (shrink again for b8 flowchart; first node pops @84.14) |
| **154.0** | **Mode-A → FULL** (expand for b11 closer @154.60) |
| 161.7 | b11 lines drift out; **video holds FULL clean** to 163.0 (no outro card — D4) |

Ken-Burns on the video element: deterministic `scale 1.0 → 1.04` across the full 163 s (no `Math.random`, no `repeat:-1`).

---

## Speaker framing — `object-position: 83% center` (VERIFIED, carried from v2)
**Mode-A box:** `left:1229, top:108, width:614, height:864` (85 % of right-40 % zone), `object-fit:cover`, `object-position: 83% center`, vertical `center` (no bias, no scale-up). Source is side-by-side (Nic left, Jasper right, seam ≈ x960); the 83 % crop shows source x≈957–1725 → **Jasper's face dead-centre, his "Jasper De Maere / Wintermute" name lower-third fully in-frame, no host bleed, no dead ceiling.** (v2 verified this against `/tmp/modeA_83.png` vs 50/62/80/86/90 %; 50 %/62 % centre the seam = the rejected clip-1 bug.) **Builder must re-extract the rendered Mode-A frame and LOOK before claiming done (QA §5/§9).** Opening + Q/A + closer FULL phases show BOTH speakers (never text on black).

---

## Template variety (proves R2) — the distinct device LEADS

**Sequence:** `kinetic → kinetic → ROTATION-CARD → swiss → glass → kinetic → kinetic → flowchart → DATA-CHART → swiss → kinetic`

- **Max kinetics in a row = 2** (intro pair b1-b2; Q/A pair b6-b7). 5-kinetic run **broken**. ✔
- **Distinct PRIMARY device (DESIGN.md per-clip map = "before/after rotation + `data-chart` vol profile"):** delivered by **b3 rotation before→after card** (CRYPTO/ALTCOINS struck → EQUITIES, with the dwindling-months timeline) and **b9 `data-chart` two-series vol-profile** (crypto vol ↓ vs equity vol ↑ converging). These two are the spine; the kinetics support, they don't dominate. ✔
- **No init-from-kinetic default** for the chart/comparison beats. ✔

### Catalog blocks — INSTALL vs HAND-BUILD
| beat | device | action |
|---|---|---|
| **b9 vol-profile** | two-series before/after chart | **INSTALL** `npx hyperframes add data-chart --dir clip-5-capital-rotation --no-clipboard`. Wire as a sub-comp; **re-scope into the LEFT zone** (wrap in a 0–1152 px container, scale the block to fit, keep speaker Mode-A right). If the block's fixed internal padding fights the 1152 px width, **hand-build** a compact 2-series step/bar chart using the block's bar+axis styling as reference (DESIGN.md palette). |
| **b8 exuberance flow** | 3-node causal chain | **INSTALL** `npx hyperframes add flowchart --dir clip-5-capital-rotation --no-clipboard`. Wire as sub-comp scaled to the left zone; nodes pop on the spoken words (below). Final node = the one cyan. |
| b3 rotation card | bespoke before→after | **HAND-BUILD** (no catalog block does the struck-from-state + arrow + dwindle-timeline motif). |
| b4, b10 | swiss-grid stat / two-col | **HAND-BUILD** (project swiss-grid pattern; do NOT re-init from kinetic-type). |
| b5 | liquid-glass card | **HAND-BUILD** (project card recipe). |
| b1,b2,b6,b7,b11 | kinetic word-stack | init `--example kinetic-type`. Optional polish: `caption-kinetic-slam` component on the cyan payoff line (b11 closer) — but keep the phrase-build-and-STAY behaviour (no dim). |

---

## BEAT TABLE

Per beat: **id · comp range · src range · template/block · full on-screen text · view · sub-comp file · per-kinetic-line `comp_t` + matched transcript words.** `*CYAN` = the single cyan `#00D4FF` element. `[EDITORIAL]` = chrome / anticipatory (not word-synced). Eyebrows Inter 700 ≥32px `#F0F0F0`; body/bullets Inter ≥600; payoff/slam 130px.

---

### b1 — OPENING KINETIC · *the dialog-matched open* (kinetic-type)
- **comp** 0.0–4.6 | **src** 1135.5–1140.1 | **view** FULL (both speakers; dark left-gradient backdrop) | **data-start** `-0.2` **data-duration** `5.2` (brackets all fire-times +0.3 s headroom)
- **sub-comp** `compositions/beat-c5b1-pivoted-into-equity.html`
- **template** kinetic word-stack, 3-phrase build (~130px Inter 900), lines slam in and **STAY (no dim)**, over full-frame video. First text by t≈0.34 (R3 §3).
- **On-screen lines + word-sync** (R5 — reads as a complete thought; "retail" is the spoken subject 10 s prior, carried as context on L1, "PIVOTED" is the word-locked anchor):
  - **L1 `RETAIL PIVOTED`** — fire **comp 0.34** ← "pivoted" (table 15.84). ("RETAIL" = carried context, spoken @src 1125.56.)
  - **L2 `VERY AGGRESSIVELY`** — fire **comp 1.60** ← "aggressively" (table 17.10)
  - **L3 `INTO EQUITY` *CYAN** — fire **comp 2.58** ← "equity" (table 18.08)
- **Exit:** b1's 3-line stack clears @ comp ~3.4 (drift up, power2.in 0.28 s) so the FULL frame is clean before b2's stack begins. The **FULL view persists 0.0–15.5 across both b1 and b2** (one grouped phase — the video does NOT switch between them).
- **R4 audit:** {retail, pivoted} / {aggressively} / {equity} — no repeat. ✔

### b2 — KINETIC "altcoin season into equities" (kinetic-type)
- **comp** 12.3–14.6 | **src** 1147.8–1150.1 | **view** FULL | **data-start** `12.0` **data-duration** `3.4`
- **sub-comp** `compositions/beat-c5b2-altcoin-season.html`
- **template** kinetic 3-phrase build, STAYS. (2nd of the intro pair — ≤2 rule satisfied.)
- **On-screen lines + word-sync:**
  - **L1 `ALTCOIN SEASON`** — fire **comp 12.30** ← "altcoin" (table 27.80) / "season" (table 28.14)
  - **L2 `IS NOW HAPPENING`** — fire **comp 13.66** ← "now" (table 29.16) / "happening" (table 29.34)
  - **L3 `IN EQUITIES` *CYAN** — fire **comp 14.62** ← "equities" (table 30.12)
- **Exit:** stack drifts out @ ~14.9; at comp **15.0 the video shrinks FULL→Mode-A** for b3.
- **R4 audit:** {altcoin, season} / {now, happening} / {equities} — no repeat. ✔ (Note: "EQUITY/EQUITIES" is the cyan payoff in b1+b2 — the rotation thesis hammer; differing singular/plural as spoken. Per-beat R4 clean.)

### b3 — ROTATION before→after CARD · *distinct PRIMARY device, part 1* (HAND-BUILD)
- **comp** 15.5–20.4 | **src** 1151.0–1155.9 | **view** Mode-A | **data-start** `15.5` **data-duration** `~4.9` *(shortened so it clears before b4's JP-Morgan stat starts @comp 20.5 — all b3 elements are [EDITORIAL] and build by ~comp 19.6, so no fire is lost; prevents two Mode-A graphics sharing the left zone)*
- **sub-comp** `compositions/beat-c5b3-rotation-card.html`
- **template** bespoke rotation panel in the LEFT zone (feathered `mask-image`, no blur, no grain): index `05` + eyebrow + cyan rule (chrome), THEN the before→after motif —
  `CRYPTO / ALTCOINS` (struck-through, 0.45 opacity, white) → down-arrow `↓` → `EQUITIES` (full `#F0F0F0`) → a 4-chip dwindle timeline `NOV · DEC · JAN · FEB`.
- **Full on-screen text:**
  - index **`05`** (JetBrains Mono 20px muted) `[EDITORIAL]` @15.7
  - eyebrow **`CAPITAL ROTATION`** (Inter 700, 32px, #F0F0F0) `[EDITORIAL]` @15.9
  - cyan rule draws L→R **`*CYAN`** `[EDITORIAL]` @16.3
  - from-state **`CRYPTO / ALTCOINS`** (struck, 0.45) `[EDITORIAL build]` @17.0
  - arrow **`↓`** + to-state **`EQUITIES`** (#F0F0F0) `[EDITORIAL build]` @17.8
  - timeline chips **`NOV · DEC · JAN · FEB`** `[EDITORIAL]` @18.8 (spoken at src 1131.8–1133.1, *before* src_in → editorial context)
  - footer date **`2025 → 2026`** (Inter 600, #F0F0F0; 2026="this year") `[EDITORIAL]` @19.6
- ***CYAN:** the rule (one only; `EQUITIES` stays white). 
- **R4 audit:** eyebrow {capital, rotation} vs from {crypto, altcoins} vs to {equities} vs timeline {nov,dec,jan,feb} — no repeat. ✔
- **Opening-6s element types (DESIGN.md):** intro kinetic (type 1, b1) + index/eyebrow (type 2) + rule (type 3) + before/after block (type 4) + chips (type 5) all by ~t=6 of *this phase* → PASS.

### b4 — JP MORGAN ALL-TIME-HIGH stat (swiss-grid; HAND-BUILD) ← absorbs old c5b5 "retail moved"
- **comp** 20.5–33.0 | **src** 1156.0–1169.0 | **view** Mode-A | **data-start** `20.5` **data-duration** `~12.5` *(brackets the eyebrow "JP" fire @comp 20.88 with +0.3 s headroom; the JP-Morgan words are spoken src 1156.38–1165.08 = comp 20.88–29.58, with "retail moved" @src 1167.20 = comp 31.70, so the beat STARTS @~20.5 — every fire below now falls at positive data-time)*
- **sub-comp** `compositions/beat-c5b4-jpm-all-time-high.html`
- **template** swiss-grid in left zone: eyebrow + 200px slam stat + sublabel + footer. The folded-in "retail moved into equities" confirmation animates as the **sublabel** on its spoken words (so the old stranded FULL kinetic c5b5 becomes Mode-A content — kills a flip-flop).
- **Full on-screen text + word-sync:**
  - eyebrow **`JP MORGAN PRIME BROKERAGE · MAY 2026`** (Inter 700, 32px, #F0F0F0) — slam **comp 20.88** ← "JP" (table 36.38) *(date suffix `· MAY 2026` is [EDITORIAL] dateline per binding directive D3/c5b4; consistent with D7 "2026 = this year")*
  - sublabel **`RETAIL MOVED INTO EQUITIES`** (Inter 600, #F0F0F0) — fire **comp 31.70** ← "retail moved" (table 47.20) *(this is the folded-in c5b5 line, now word-synced inside Mode-A)*
  - stat **`ALL-TIME HIGH`** (Inter 800, 200px, #F0F0F0, no count-up — not a number) — slam **comp 28.34** ← "all…high" (table 43.84/44.16)
  - footer **`BY A MEANINGFUL MARGIN`** (Inter 600, #F0F0F0) — fire **comp 29.38** ← "meaningful margin" (table 44.88/45.08)
- ***CYAN:** a short cyan rule beneath the stat (swiss-grid = stat OR rule; rule chosen so the 200px stat reads white).
- **R4 audit:** eyebrow {jp, morgan, prime, brokerage, may, 2026} vs stat {all-time, high} vs sublabel {retail, moved, equities} vs footer {meaningful, margin} — no repeat. ✔ ("MAY 2026" dateline is editorial; introduces no notable-word collision.)

### b5 — WINTERMUTE WEEKLY + "marginal risk dollar" QUOTE CARD (liquid-glass; HAND-BUILD)
- **comp** 38.9–59.0 | **src** 1174.4–1194.5 | **view** Mode-A | **data-start** `38.9` **data-duration** `~20.1` *(card lands @comp 38.96 as Nic names the note, eyebrow @40.34, holds while he reads the line; pull-quote @54.50 and the "not crypto" cyan flip @57.94 both fall inside this corrected range — header now matches data-start + table fires)*
- **sub-comp** `compositions/beat-c5b5-wintermute-weekly-quote.html`
- **template** ONE liquid-glass card (merges the publication name-drop + the line from it — they are the same source, so one card, not two; this removes the v2 double-card smell). `rgba(20,26,34,0.92)` fill, **4px cyan accent bar inset-left** (not border-left), soft glow, 1px border, `mask-image` feather. **No backdrop-filter, no grain.**
- **Full on-screen text + word-sync:**
  - card slides in from right — **comp 38.96** ← "Jasper is also writing…" (table 54.46)
  - eyebrow **`WINTERMUTE WEEKLY`** (Inter 700, 32px) — fire **comp 40.34** ← "Wintermute weekly" (table 55.84/56.32)
  - pull-quote **`"The marginal risk dollar went into equities, not crypto."`** (Inter 700, 64px, #F0F0F0) — quote fades in **comp 54.50** ← "the marginal risk dollar…" (table 70.00); the words **`not crypto` flip `*CYAN` @ comp 57.94** ← "not crypto" (table 73.44)
  - attribution **`— Jasper De Maere`** (Inter 600, 32px) `[EDITORIAL]` @58.6
- ***CYAN:** the words `not crypto` in the quote (single accent; accent bar stays neutral so only one cyan).
- **R4 audit:** eyebrow {wintermute, weekly} vs quote {marginal, risk, dollar, went, equities, crypto} vs attrib {jasper, maere} — no repeat. ✔ ("Wintermute" appears once on screen; the attribution uses the person name, not the firm → no dup.)

### b6 — HOST QUESTION kinetic (kinetic-type; no "HOST" label) ← Q of the Q/A pair
- **comp** 64.9–66.3 | **src** 1200.4–1201.8 | **view** FULL (both speakers) | **data-start** `64.6` **data-duration** `2.2`
- **sub-comp** `compositions/beat-c5b6-is-crypto-dead.html`
- **template** kinetic 2-line build over both speakers (host question shown as text only, no "HOST" chrome — per memory).
- **On-screen lines + word-sync:**
  - **L1 `IS CRYPTO DEAD`** — fire **comp 64.94** ← "crypto" (table 80.44) / "dead" (table 80.82)
  - **L2 `FOR RETAIL TODAY` *CYAN** — fire **comp 65.78** ← "for retail" (table 81.28) ("TODAY" = editorial, tightens "these days")
- *(Video expanded FULL @64.4 for this; both speakers visible.)*
- **R4 audit:** {crypto, dead} vs {retail, today} — no repeat. ✔

### b7 — JASPER'S ANSWER kinetic (kinetic-type) ← A of the Q/A pair (2-in-a-row OK)
- **comp** 70.2–79.3 | **src** 1205.7–1214.8 | **view** FULL | **data-start** `69.9` **data-duration** `9.7`
- **sub-comp** `compositions/beat-c5b7-not-for-the-og-holders.html`
- **template** kinetic 3-phrase build, STAYS.
- **On-screen lines + word-sync:**
  - **L1 `NO —`** — fire **comp 70.18** ← "No" (table 85.68)
  - **L2 `NOT FOR THE OG HOLDERS`** — fire **comp 71.60** ← "not that for retail" (table 87.10) ("THE OG HOLDERS" = editorial gloss of the next clause "the people who've been in crypto since 21")
  - **L3 `SINCE 2021` *CYAN** — fire **comp 79.30** ← "since 21" (table 94.80) (2021 spelled in full per date rule)
- *(Video returns to Mode-A @83.6 for b8.)*
- **R4 audit:** {no} vs {og, holders} vs {since, 2021} — no repeat. ✔ ("NOT" and "FOR" are stop-words, not notable.)

### b8 — 2021 EXUBERANCE flowchart (block: `flowchart`) · 3-node causal chain
- **comp** 83.0–121.0 | **src** 1218.5–1256.5 | **view** Mode-A | **data-start** `83.0` **data-duration** `~38` (set so the eyebrow @comp 83.30 has +0.3 s headroom — fixes the negative data-time; holds while Jasper continues; clears before b9)
- **sub-comp** `compositions/flowchart.html` (installed) wired + scaled into the LEFT zone; cyan FINAL node only.
- **template** 3 nodes + connectors (`back.out(1.5)` pop 0.45 s; connector `strokeDashoffset` draw). Eyebrow draws as he says "alt season".
- **Full on-screen text + word-sync** ("alt season" = corrected from Whisper "old season", framed as retail's slang in quotes):
  - eyebrow **`WHAT RETAIL CALLS "ALT SEASON"`** (Inter 700, 32px) — fire **comp 83.30** ← "season" (table 98.80)
  - node 1 **`EXTREME EXUBERANCE`** — pop **comp 84.66** ← "exuberance" (table 100.16)
  - node 2 **`MASSIVE CAPITAL INJECTION`** — pop **comp 89.50** ← "capital" (table 105.00) / "injection" (table 105.40)
  - node 3 **`ALL RISK ASSETS UP` *CYAN** — pop **comp 91.92** ← "all risk assets moved up" (table 106.78/107.42)
  - annotation **`THE 2021 BENCHMARK`** (Inter 600, #F0F0F0) `[EDITORIAL]` — @ **comp 94.62** ← "the benchmark" (table 110.12)
- ***CYAN:** node 3 only.
- **R4 audit:** eyebrow {retail, calls, alt, season} vs node1 {extreme, exuberance} vs node2 {massive, capital, injection} vs node3 {risk, assets} vs annot {benchmark} — no repeat. ✔

### b9 — VOL-PROFILE **DATA-CHART** · *distinct PRIMARY device, part 2 — the required new chart* (block: `data-chart`)
- **comp** 121.5–137.5 | **src** 1257.0–1273.0 | **view** Mode-A | **data-start** `121.0` **data-duration** `16.5`
- **sub-comp** `compositions/data-chart.html` (installed) wired + **re-scoped into the LEFT zone** (hand-build fallback if the block's fixed layout won't fit 1152 px — see catalog table above).
- **template** two-series before→after comparison chart (the literal content: crypto vol was HIGH in 2021–22 then **compressed**; equity vol was low then **rose**; the two **profiles converged**). Series A = CRYPTO (red `#FF4D4F`, descending 2021→NOW), Series B = EQUITY (green `#16C784`, ascending 2021→NOW). Two x-anchors `2021` and `NOW`. Animate Series A drawing down and Series B drawing up so they **cross/converge** — the convergence point is the cyan accent.
- **Full on-screen text + word-sync:**
  - eyebrow **`VOLATILITY PROFILE`** (Inter 700, 32px) — fire **comp 123.52** ← "the volatility of crypto" (table 139.02)
  - x-labels **`2021`** … **`NOW`** (Inter 600, #F0F0F0) `[EDITORIAL]` @122
  - series labels **`CRYPTO`** (red) / **`EQUITIES`** (green) `[EDITORIAL]` @122.5 *(directional red/green are the allowed market indicators per D7 — NOT the cyan accent)*
  - the crypto line drawing DOWN keys on **comp 135.12** ← "volatility in crypto compressed" (table 150.62) — i.e. the folded-in old c5b11 "compressed" lands here as the chart's down-move, not a stranded FULL kinetic
  - convergence callout **`THEY CONVERGED` *CYAN** — fire **comp 136.44** ← "compressed" (table 151.94), drawn at the crossing point *(reads "THEY CONVERGED", not "PROFILES CONVERGED", to avoid sharing the "profile" stem with the eyebrow — R4)*
- ***CYAN:** the convergence point/callout (one only; the two series are red/green indicators).
- **R4 audit:** eyebrow {volatility, profile} vs series {crypto, equities} vs callout {they, converged} — no repeated notable word. ✔

### b10 — VOL COMPARISON crypto↓ vs equity↑ (swiss-grid two-column; HAND-BUILD) ← absorbs the "became equal" close
- **comp** 143.5–154.5 | **src** 1279.0–1290.0 | **view** Mode-A | **data-start** `143.4` **data-duration** `11.1`
- **sub-comp** `compositions/beat-c5b10-vol-comparison.html`
- **template** two-column in left zone: directional indicators with a cyan divider rule.
- **Full on-screen text + word-sync:**
  - eyebrow **`THE VOL TRADE MOVED`** (Inter 700, 32px) `[EDITORIAL]` @143.5
  - col-L **`CRYPTO  ↓ DOWN`** (red `#FF4D4F`) `[EDITORIAL build]` @143.6
  - col-R **`EQUITY  ↑ RISING`** (green `#16C784`) — fire **comp 143.98** ← "the equity market became more volatile" (table 159.48/160.06/160.52)
  - cyan divider draws between columns **`*CYAN`** @144.4
  - footer **`PROFILES NOW EQUAL`** (Inter 600, #F0F0F0) — fire **comp 147.20** ← "volatility profile became quite equal" (table 162.70/164.12)
- ***CYAN:** the divider rule (red/green are directional indicators per D7).
- **R4 audit:** eyebrow {vol, trade, moved} vs colL {crypto, down} vs colR {equity, rising} vs footer {profiles, equal} — no repeat. ✔

### b11 — CLOSER kinetic "they just want a vol trade → equity offers it" (kinetic-type) ← VERIFIED closer
- **comp** 154.6–161.7 | **src** 1290.1–1297.2 | **view** FULL → settles to clean FULL for last ~1.3 s (D4: end on content, not a card) | **data-start** `154.3` **data-duration** `7.4`
- **sub-comp** `compositions/beat-c5b11-vol-trade-closer.html`
- **template** kinetic 3-phrase build, STAYS; optional `caption-kinetic-slam` polish on the cyan payoff (keep no-dim phrase behaviour).
- **On-screen lines + word-sync:**
  - **L1 `THEY JUST WANT`** — fire **comp 154.60** ← "They just want" (table 170.10)
  - **L2 `A VOLATILITY TRADE`** — fire **comp 156.68** ← "a volatility trade" (table 172.18/172.64)
  - **L3 `EQUITY OFFERS IT` *CYAN** — fire **comp 160.66** ← "currently equity markets are offering that exact thing" (table 176.16; "offering" anchor)
  - lines drift out @161.7; **video holds clean FULL to 163.0** — no outro card (D4).
- **R4 audit:** {they, just, want} vs {volatility, trade} vs {equity, offers} — no repeat. ✔ ("VOL" in b10 eyebrow vs "VOLATILITY" here are different beats — R4 is per-beat.)

---

## VERIFICATION SUMMARY (grade against `_QA-CHECKLIST.md` — every item)

**§1 View-switching (R1):** view-timeline table above; 5 phases, smallest sustained 8.4 s, all A-B-A gaps ≥19 s, only 4 GSAP toggles in 163 s. ✔
**§2 Template variety (R2):** max 2 kinetics in a row; distinct device (rotation card b3 + data-chart b9) leads; `data-chart`+`flowchart` installed from catalog; swiss/card/rotation hand-built; no chart/comparison beat inits from kinetic-type. ✔
**§3 Dialog-match + word-sync:** opens on "pivoted very aggressively into equity" (spoken comp 0.34–2.58, first 2.6 s); first text @0.34; every kinetic line fires at a table comp_t (listed per line); editorial lines marked. ✔
**§4 Opening coherence (R5):** "RETAIL PIVOTED / VERY AGGRESSIVELY / INTO EQUITY" is a complete thought; cyan payoff "INTO EQUITY" is a real phrase, no dangling number. ✔
**§5 Framing:** `object-position: 83% center`, Mode-A box {1229,108,614,864}; centres Jasper, name in-frame; opening/Q-A/closer FULL show both speakers; builder re-verifies by frame. ✔
**§6 Jargon (R3):** no burp/deep-in/graft/stake-rate; "alt season" corrected (Whisper "old season"); Wintermute / JP Morgan / Jasper De Maere exact; dates 2021(benchmark, accurate)/2025/2026, never 2024. ✔
**§7 Duplicate words (R4):** per-beat audit above — all clean (b9 callout changed to "THEY CONVERGED" to avoid "profile/profiles" stem clash). ✔
**§8 Carry-over hard rules:** ONE cyan per beat (marked); cards `rgba(20,26,34,0.92)`+4px inset cyan bar+glow+mask, no blur, no grain; eyebrows Inter 700 ≥32px #F0F0F0, body ≥600, no #888888 under 48px; no intro/outro (ends on clean video b11); phrase kinetics build-and-STAY (no dim). **Builder MUST add every overlay id (`beat-c5b1…`, plus installed `flowchart`/`data-chart` ids) to the `z-index:3` rule in `index.html` or it renders behind the video.** ✔ (z-index is a build step — flagged.)
**§9 Verify-by-frame:** builder extracts frames at the opening, each of the 4 view toggles (15.0 / 64.4 / 83.6 / 154.0), and each distinct beat, and LOOKS before reporting done. ✔

**Beat count:** **11** (within the clip-5 11–13 range). Kinetic share 5/11. Two installed catalog blocks (`flowchart`, `data-chart`).

## Build manifest row
`clip_5 | clip-5-capital-rotation | src_in 1135.5 | src_out 1298.5 | 163.0s | kinetic-type, rotation-card(custom), swiss-grid, liquid-glass, flowchart(block), data-chart(block) | 11 beats | object-position 83%`
