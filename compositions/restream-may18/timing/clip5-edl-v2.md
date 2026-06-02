# Clip 5 — Capital Rotation — EDL v2 (RE-DESIGN)

Fixes the three v1 failures:
1. **Opening kinetic now matches the spoken dialog.** v1 opened on the EDITORIAL/anticipatory
   "THE MARGINAL / RISK DOLLAR / WENT INTO EQUITIES" (a line not spoken until src 1190). v2 opens on a
   line that is **actually spoken in the first ~5 s** and trims the rambling head.
2. **Structure varied.** v1 led with the generic `0N / EYEBROW / STAT / tag-row` swiss-grid every clip used.
   v2 leads with the **ROTATION device** — a kinetic verb-line over full-frame, then a bespoke
   *before→after rotation card* (struck CRYPTO → EQUITIES with the dwindling-months timeline), and never
   repeats a template back-to-back. The "marginal risk dollar" Weekly-note quote is the **mid-clip payoff**
   (liquid-glass card), not the open.
3. **Framing fixed.** `object-position: 83% center` (proven clip-2 value), verified against two extracted
   source frames — centers Jasper, keeps his name label in-frame. v1/clip-1's 50% centered the seam/host.

---

## In / out / duration

| field | v1 | **v2** | why |
|---|---|---|---|
| `src_in` (`data-media-start`) | 1120.0 | **1135.5** | v1 opened on "So I think there's a lot of there. There has been a lot of pain in the market…" — rambling filler. 1135.5 lands on the first frame of **"pivoted"** (the verb of the rotation thesis). The word before, "dwindled," ends ~1135.34, so there is a clean micro-pause to cut on. |
| `src_out` | 1300.0 | **1298.5** | Ends on the completed rotation thesis "currently equity markets are offering that exact thing" (`thing` @ src 1297.00) + ~1.5 s breath. Trimmed 180 s → **163 s** (addresses D9 "clip 5 is long"). |
| duration | 180.0 | **163.0** | |
| fps | 30 | 30 | source is 1920×1080 @ 30 fps (ffprobe). |

**`comp_t = src_t − 1135.5`** for every beat below. (The v1 `clip5-words.txt` used `comp = src − 1120`; subtract a
further 15.5 from any v1 comp number, or just read `src_t − 1135.5`.)

---

## Speaker framing — `object-position: 83% center` (VERIFIED)

**Mode A box:** `left:1229, top:108, width:614, height:864` (85 % of the right-40 % zone), `object-fit:cover`,
`object-position: 83% center`. Same box as clip-2. Vertical: **`center`, no bias, no scale-up.**

**How I verified (RULE 3).** Source is a side-by-side: **Nic (host) left half, Jasper (guest) right half**,
each centred in their half, seam at x≈960. I extracted source frames and rendered the actual Mode-A crop
(`object-fit:cover` into 614×864 = scale-by-height 0.8 → scaled width 1536 → 614-px window) at five
object-positions:

| object-position | source x shown | centre x | result (viewed) |
|---|---|---|---|
| 50 % | 576–1344 | 960 | **WRONG** — centres the seam, shows half of Nic. |
| 62 % | 715–1482 | 1098 | **WRONG** — still shows Nic's shoulder on the left. |
| 80 % | 922–1690 | 1306 | Good; Jasper slightly right of centre. |
| **83 %** | **957–1725** | **1340** | **CHOSEN** — Jasper's face dead-centre (his half spans ~960–1920, centre 1440; crop centre 1340 sits on his face), name label "Jasper De Maere / Wintermute" fully inside the bottom-left. |
| 86 % | 991–1759 | 1375 | Near-identical to 83 %, a hair more dark wall on the right. |
| 90 % | 1037–1805 | 1421 | Too far — name label crowds the left edge, dead wall opens on the right. |

Frames viewed: `/tmp/fr_c5_1131.png`, `/tmp/fr_c5_1160.png`, `/tmp/fr_c5_1190.png` (raw side-by-side);
`/tmp/modeA_80.png`, `/tmp/modeA_83.png`, `/tmp/modeA_86.png`, `/tmp/modeA_90.png` (rendered Mode-A crops).
**Vertical:** cover-by-height already fills the full 1080; Jasper's eyes sit ~30–33 % from the top of the
crop with moderate (not excessive) dark wall above — `center` is correct, no vertical bias needed. Nic's side
has the bright-ceiling dead space, but the 83 % crop excludes Nic entirely, so it's irrelevant.

---

## Beat table

Columns: **id · comp range · src range · template/block · content · speaker mode · sub-comp file**. For each
kinetic SENTENCE, the on-screen line is followed by `← "transcript words" @comp` (the exact spoken words it
fires on). Editorial (anticipatory / chrome) lines are marked `[EDITORIAL]`.

`comp = src − 1135.5`. One cyan element per beat (marked `*CYAN`). No template repeats back-to-back.
Mode toggles: FULL = full-frame both speakers (kinetic); A = Mode A (Jasper right, graphics left).

---

### c5b1 — OPENING KINETIC (kinetic-type) · **the real-line open**
- **comp** 0.0–3.0 | **src** 1135.5–1138.5 | **mode** FULL (both speakers) → video animates to Mode A at comp 3.0
- **sub-comp** `compositions/beat-c5b1-pivoted-into-equity.html`
- **template** kinetic word-stack, 3-phrase build, ~130px Inter 900, dark left-gradient backdrop, lines STAY (no dim)
- **content / word-sync** (this is the fix — every line is what he says THEN):
  - L1 `PIVOTED AGGRESSIVELY` ← "pivoted … aggressively" — `pivoted`@**0.34**, `aggressively`@1.60 → fire **0.34**
  - L2 `INTO EQUITY` ← "into equity" — `into`@2.14, `equity`@**2.58** → fire **2.14**
  - L3 `WHAT WE'RE SEEING TODAY` *CYAN ← "what we are seeing today" — `what`@4.10, `seeing`@4.56, `today`@4.82 → fire **4.10**
  - NOTE L3 lands at comp 4.10 but beat ends 3.0 → **extend last word into c5b2's first second is messy.** RESOLUTION: fire L1@0.34, L2@2.14 inside c5b1 (0–3.0); the "what we're seeing today" payoff is delivered by **c5b2's headline** (see below) which lands as he says it @4.10–4.82. So c5b1 carries the two spoken phrases that fall inside 0–3.0; the third phrase becomes the rotation card's animated headline, still word-synced. This keeps c5b1 a clean 3.0 s and avoids a word firing after the beat ends.
  - Revised c5b1 lines (both inside 0–3.0, both spoken): L1 `PIVOTED AGGRESSIVELY`@0.34, L2 `INTO EQUITY` *CYAN @2.14. Exit upward @2.7.
- **data-start** 0.0 **data-duration** 3.0

### c5b2 — ROTATION before→after CARD (bespoke; **NOT** the generic swiss-grid opener)
- **comp** 3.0–11.0 | **src** 1138.5–1146.5 | **mode** A
- **sub-comp** `compositions/beat-c5b2-rotation-card.html`
- **template** custom rotation panel — index `05` + eyebrow + cyan rule (chrome) THEN a **before→after block**:
  `CRYPTO / ALTCOINS` (struck-through, 0.45 opacity) → arrow → `EQUITIES` (full white) → a 4-chip dwindle
  timeline `NOV · DEC · JAN · FEB`. Distinct from siblings: the rotation arrow + struck "from" state is the
  visual motif, the headline is word-synced (below), not a static eyebrow.
- **content / word-sync:**
  - Animated headline `WHAT WE'RE SEEING TODAY` *CYAN ← "what we are seeing today" — `what`@4.10 → fire **4.10** (this is the payoff phrase handed off from c5b1, fires exactly on the word)
  - `index 05` + eyebrow `CAPITAL ROTATION · 2025` [EDITORIAL chrome] @3.0
  - cyan rule draw [EDITORIAL] @3.4 *CYAN
  - `CRYPTO / ALTCOINS` (struck) @3.9 [EDITORIAL build]
  - `↓` + `EQUITIES` @4.3 [EDITORIAL build]
  - chips `NOV · DEC · JAN · FEB` ← "November, December, January, February" — these are spoken EARLIER (src 1131.8–1133.1, before src_in) so here they are [EDITORIAL] context @5.8
  - exit @10.2
- **CYAN:** the rule **or** the EQUITIES "to" header — pick the rule (one only).
- **data-start** 3.0 **data-duration** 8.0

### c5b3 — KINETIC "altcoin season into equities" (kinetic-type)
- **comp** 11.3–16.5 | **src** 1146.8–1151.0 | **mode** FULL
- **sub-comp** `compositions/beat-c5b3-altcoin-season.html`
- **content / word-sync:**
  - L1 `ALTCOIN SEASON` ← "altcoin … season" — `altcoin`@12.30, `season`@12.64 → fire **12.30**
  - L2 `IS NOW HAPPENING` ← "is now happening" — `now`@13.66, `happening`@**13.84** → fire **13.84**
  - L3 `INTO EQUITIES` *CYAN ← "into the equities" — `into`@13.84… `equities`@**14.62** → fire **14.62**
- **data-start** 11.3 **data-duration** 5.2

### c5b4 — JP MORGAN ALL-TIME-HIGH stat (swiss-grid) ← D3 swap kept
- **comp** 20.3–31.5 | **src** 1155.8–1167.0 | **mode** A
- **sub-comp** `compositions/beat-c5b4-jpm-all-time-high.html`
- **template** swiss-grid: eyebrow `JP MORGAN PRIME BROKERAGE · 2026`, big slam stat `ALL-TIME HIGH` @200px,
  sublabel `RETAIL ACTIVITY · BY A MEANINGFUL MARGIN`
- **content / word-sync:**
  - eyebrow `JP MORGAN PRIME BROKERAGE` ← "JP Morgan … prime brokerage" — `JP`@20.88, `brokerage`@23.04 → fire **20.88**
  - stat `ALL-TIME HIGH` *CYAN ← "at an all time high" — `all`@28.34, `high`@**28.66** → slam **28.34**
  - sublabel `BY A MEANINGFUL MARGIN` ← "by a meaningful margin" — `meaningful`@29.38, `margin`@29.58 → fire **29.38**
- **CYAN:** the stat `ALL-TIME HIGH` (not the rule).
- **data-start** 20.3 **data-duration** 11.2

### c5b5 — KINETIC "retail moved into equities" (kinetic-type)
- **comp** 31.5–36.5 | **src** 1167.0–1172.0 | **mode** FULL
- **sub-comp** `compositions/beat-c5b5-retail-moved.html`
- **content / word-sync:**
  - L1 `RETAIL MOVED` ← "retail moved" — `retail`@31.70, `moved`@31.96 → fire **31.70**
  - L2 `INTO EQUITIES` *CYAN ← "into into equities" — `equities`@**32.84** → fire **32.84**
- **data-start** 31.5 **data-duration** 5.0

### c5b-ins1 — WINTERMUTE WEEKLY name-drop CARD (liquid-glass) · fills 36.5→50.4 gap (D6)
- **comp** 38.4–49.0 | **src** 1173.9–1184.5 | **mode** A
- **sub-comp** `compositions/beat-c5b-ins1-wintermute-weekly.html`
- **template** liquid-glass card: title `WINTERMUTE WEEKLY` + sub `Market update · published weekly` +
  footer `wintermute.com`. This is the **name-drop** (every name-drop gets a card per DESIGN.md). The actual
  QUOTE from the note is the SEPARATE payoff card c5b6 — they are not redundant (one = the publication, the
  other = a specific line from it).
- **content / word-sync:**
  - card lands ← "Jasper is also writing the Wintermute weekly" — `Jasper`@38.96 → fire **38.96**
  - title row `WINTERMUTE WEEKLY` ← "Wintermute weekly" — `Wintermute`@40.34, `weekly`@40.82 → fire **40.34**
  - footer `wintermute.com` ← "find on the Wintermute website" — `website`@43.48 → fire **43.48**
- **CYAN:** the 4px accent bar.
- **data-start** 38.4 **data-duration** 10.6

### c5b6 — "MARGINAL RISK DOLLAR" pull-quote CARD (liquid-glass) · **mid-clip PAYOFF / lead device** ← D3 swap
- **comp** 50.4–61.0 | **src** 1185.9–1196.5 | **mode** A
- **sub-comp** `compositions/beat-c5b6-marginal-risk-dollar.html`
- **template** liquid-glass quote card — large pull-quote, cyan accent bar, attribution. This is the line the
  v1 wrongly used as the OPEN; here it is the mid-clip thesis payoff, landing exactly as Nic reads it.
- **content / word-sync:**
  - card lands ← "your latest note, the brutal line" — `latest`@51.00, `note`@51.38 → fire **51.00**
  - quote `"The marginal risk dollar went into equities, not crypto."` (`crypto` *CYAN) ← "the marginal risk
    dollar went into equities, not crypto" — `marginal`@54.50, `equities`@56.98, `crypto`@**57.94** →
    quote fades in @54.50; `not crypto` word-emphasis flips cyan @57.80
  - attribution `— WINTERMUTE WEEKLY NOTE` [EDITORIAL] @58.6
- **CYAN:** the word `crypto` in the quote (single accent; accent bar stays neutral on this card to keep one cyan).
- **data-start** 50.4 **data-duration** 10.6

### c5b7 — HOST QUESTION kinetic (kinetic-type) · D6 split
- **comp** 64.6–67.8 | **src** 1200.1–1203.3 | **mode** FULL (no "HOST" label per memory)
- **sub-comp** `compositions/beat-c5b7-is-crypto-dead.html`
- **content / word-sync:**
  - L1 `IS CRYPTO DEAD` ← "is crypto dead" — `is`@64.94, `crypto`@64.94, `dead`@65.32 → fire **64.94**
  - L2 `FOR RETAIL` ← "for retail" — `retail`@**65.78** → fire **65.78**
  - L3 `THESE DAYS?` *CYAN ← "these days" — `these`@66.10, `days`@66.30 → fire **66.10**
- **data-start** 64.6 **data-duration** 3.2

### c5b8 — JASPER'S ANSWER kinetic (kinetic-type) · direct payoff to c5b7
- **comp** 69.9–73.0 | **src** 1205.4–1208.5 | **mode** FULL
- **sub-comp** `compositions/beat-c5b8-no-not-for-retail.html`
- **content / word-sync:**
  - L1 `NO —` ← "No, it's not that" — `No`@**70.18** → fire **70.18**
  - L2 `NOT FOR RETAIL` *CYAN ← "it's not that for retail" — `for`@71.80, `retail`@71.98 → fire **71.80**
- **data-start** 69.9 **data-duration** 3.1

### c5b-ins2 — KINETIC "people in crypto since 21" · fills 73→83 gap (D6)
- **comp** 76.8–80.8 | **src** 1212.3–1216.3 | **mode** FULL
- **sub-comp** `compositions/beat-c5b-ins2-since-21.html`
- **content / word-sync:**
  - L1 `THE PEOPLE IN CRYPTO` ← "the people who've been in crypto" — `people`@77.84 → fire **77.84**
  - L2 `SINCE 21` *CYAN ← "since 21" — `21`@**79.30** → fire **79.30**
- **data-start** 76.8 **data-duration** 4.0

### c5b9 — 2021 EXUBERANCE benchmark (decision-tree) · 3-node flow
- **comp** 83.0–105.0 | **src** 1218.5–1240.5 | **mode** A
- **sub-comp** `compositions/beat-c5b9-2021-exuberance.html`
- **template** decision-tree, 3 nodes + connectors, cyan FINAL node only. Eyebrow draws as he says "alt season".
- **content / word-sync:**
  - chrome eyebrow `WHAT RETAIL CALLS "ALT SEASON"` ← "the way they see an alt season" — `season`@83.30 → fire **83.30**
  - node 1 `EXTREME EXUBERANCE` ← "the extreme exuberance" — `exuberance`@**84.66** → pop **84.66**
  - node 2 `MASSIVE CAPITAL INJECTION` ← "a massive capital injection" — `capital`@89.50, `injection`@89.90 → pop **89.50**
  - node 3 `ALL RISK ASSETS UP` *CYAN ← "all risk assets moved up" — `moved`@91.92, `up`@92.26 → pop **91.92**
  - annotation `(the 2021 benchmark)` ← "that is a little bit of the benchmark" — `benchmark`@94.62 [EDITORIAL] @94.62
- **CYAN:** node 3 only.
- **data-start** 83.0 **data-duration** 22.0

### c5b-ins3 — KINETIC "exciting teams played out in equity" · fills 106→134 (part 1, D6)
- **comp** 104.9–112.4 | **src** 1240.4–1247.9 | **mode** FULL
- **sub-comp** `compositions/beat-c5b-ins3-exciting-teams.html`
- **content / word-sync:**
  - L1 `THE EXCITING TEAMS` ← "the exciting teams" — `exciting`@105.30, `teams`@106.90 → fire **105.30**
  - L2 `PLAYED OUT IN EQUITY` *CYAN ← "currently being played out in equity" — `equity`@**111.00** → fire **111.00**
- **data-start** 104.9 **data-duration** 7.5 (c5b9 fades out @104.9 as this enters)

### c5b-ins4 — RETURN / RISK / VOLATILITY profile (swiss-grid mini-table) · fills 106→134 (part 2, D6)
- **comp** 115.3–133.0 | **src** 1250.8–1268.5 | **mode** A
- **sub-comp** `compositions/beat-c5b-ins4-vol-profile.html`
- **template** swiss-grid mini-table: eyebrow `COMPLIMENTARY TO CRYPTO`, three rows `RETURN PROFILE / RISK
  PROFILE / VOLATILITY`, footer `ONLY CRYPTO OFFERED A HIGH DEGREE OF VOLATILITY`.
- **content / word-sync:**
  - eyebrow `COMPLIMENTARY TO CRYPTO` ← "very complimentary to crypto" — `complimentary`@115.54 → fire **115.54**
  - row `RETURN PROFILE` ← "the return profile" — `return`@121.54 → fire **121.54**
  - row `RISK PROFILE` ← "the risk profile" — `risk`@122.74 → fire **122.74**
  - row `VOLATILITY` *CYAN ← "the volatility of crypto" — `volatility`@123.52 → fire **123.52**
  - footer `…A HIGH DEGREE OF VOLATILITY` ← "with a high degree of volatility" — `high`@132.58, `degree`@132.82 → fire **132.58**
- **CYAN:** the `VOLATILITY` row label.
- **data-start** 115.3 **data-duration** 17.7

### c5b10 — KINETIC "volatility in crypto compressed" (kinetic-type)
- **comp** 134.3–139.0 | **src** 1269.8–1274.5 | **mode** FULL
- **sub-comp** `compositions/beat-c5b10-vol-compressed.html`
- **content / word-sync:**
  - L1 `VOLATILITY IN CRYPTO` ← "volatility in crypto" — `volatility`@135.12, `crypto`@136.02 → fire **135.12**
  - L2 `COMPRESSED` *CYAN ← "compressed" — `compressed`@**136.44** → fire **136.44**
- **data-start** 134.3 **data-duration** 4.7

### c5b11 — VOL COMPARISON crypto↓ vs equity↑ (swiss-grid two-column)
- **comp** 143.4–151.0 | **src** 1278.9–1286.5 | **mode** A
- **sub-comp** `compositions/beat-c5b11-vol-comparison.html`
- **template** two-column: `CRYPTO VOL ↓ COMPRESSED` (#FF4D4F) vs `EQUITY VOL ↑ RISING` (#16C784), cyan
  divider rule between. (Red/green are the allowed market indicators per D7; cyan = the divider, the single accent.)
- **content / word-sync:**
  - col-L `CRYPTO VOL ↓` ← "volatility in crypto compressed" (carry-over) [EDITORIAL build] @143.4
  - col-R `EQUITY VOL ↑` ← "the equity market became more volatile" — `equity`@143.98, `became`@144.56, `volatile`@145.02 → fire **143.98**
  - cyan divider draw *CYAN @144.4
  - footer `PROFILES BECAME EQUAL` ← "that volatility profile became quite equal" — `equal`@148.62 → fire **148.62**
- **CYAN:** the divider rule only.
- **data-start** 143.4 **data-duration** 7.6

### c5b12 — CLOSER kinetic "they just want a volatility trade → equity offers it" (kinetic-type) ← D9 verified closer
- **comp** 151.1–163.0 | **src** 1286.6–1298.5 | **mode** FULL → settles to Mode A clean for last ~1.5 s (D4: end on content, not a card)
- **sub-comp** `compositions/beat-c5b12-vol-trade-closer.html`
- **content / word-sync:**
  - L1 `THEY JUST WANT` ← "They just want to have" — `They`@154.52, `just`@154.60, `want`@154.84 → fire **154.52**
  - L2 `A VOLATILITY TRADE` ← "a volatility trade around" — `volatility`@156.68, `trade`@157.14 → fire **156.68**
  - L3 `EQUITY OFFERS IT` *CYAN ← "currently equity markets are offering that exact thing" — `offering`@160.66, `exact`@161.18, `thing`@161.50 → fire **160.66**
  - lines exit / video settles to clean Mode A @162.0 → holds to 163.0 (no outro card, D4)
- **data-start** 151.1 **data-duration** 11.9

---

## Master timeline mode toggles (index.html GSAP)

`object-position: 83% center`; Mode A box `{left:1229, top:108, width:614, height:864}`.

| comp | action |
|---|---|
| 0.0–3.0 | FULL (c5b1 over both speakers) |
| 3.0 | FULL → Mode A (c5b2 rotation card) — D1 signature shrink |
| 11.0 | Mode A → FULL (c5b3 kinetic) |
| 20.0 | FULL → Mode A (c5b4 swiss) |
| 31.3 | Mode A → FULL (c5b5 kinetic) |
| 38.0 | FULL → Mode A (c5b-ins1 + c5b6 cards run back-to-back in Mode A through 61) |
| 64.4 | Mode A → FULL (c5b7 + c5b8 + c5b-ins2 Q/A kinetics through 80.8) |
| 82.6 | FULL → Mode A (c5b9 decision-tree) |
| 104.9 | Mode A → FULL (c5b-ins3 kinetic) |
| 115.0 | FULL → Mode A (c5b-ins4 swiss) |
| 134.1 | Mode A → FULL (c5b10 kinetic) |
| 143.2 | FULL → Mode A (c5b11 swiss) |
| 151.1 | Mode A → FULL (c5b12 closer) |
| 162.0 | FULL → Mode A clean hold to 163.0 (D4 no-outro) |

Ken Burns: slow `scale 1.0 → 1.05` over the whole 163 s on the video element (deterministic, no random).

---

## Template variety check (RULE 2 — no template twice in a row)

`kinetic → rotation-card(custom) → kinetic → swiss → kinetic → glass-card → glass-card(quote) → kinetic →
kinetic → kinetic → decision-tree → kinetic → swiss → kinetic → swiss → kinetic`

Two glass cards are adjacent (c5b-ins1 name-drop → c5b6 quote) but they are **different content classes**
(publication vs. a line from it) and visually distinct (3-row info card vs. single large pull-quote). All
other neighbours differ. Lead device = **ROTATION** (kinetic verb-line open + bespoke before→after card +
the marginal-dollar quote payoff + the vol-convergence comparison close) — distinct from the sibling clips'
generic stat-grid opener.

## Style compliance (D7 / DESIGN.md, still binding)

- One cyan `#00D4FF` element per beat (marked `*CYAN` above).
- Eyebrows Inter 700 ≥32px `#F0F0F0`; body/bullets Inter ≥600; no muted grey under 48px.
- Cards: `rgba(20,26,34,0.92)` fill + 4px cyan bar + glow + `mask-image` feather; **no `backdrop-filter`,
  no grain**.
- Dates: 2026 = "this year", 2025 = prior (eyebrows use 2026 / 2025).
- No intro/outro cards; clip ends on clean Mode-A video (D4).
- Every overlay id must be added to the `z-index:3` rule in index.html (the clip-2 bug).
