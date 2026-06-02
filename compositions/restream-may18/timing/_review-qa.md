Now I have the full picture. Let me conduct a thorough, merciless review of every clip against DESIGN.md.

---

## QA REVIEW — ALL 7 CLIPS

---

### CLIP 1 — OTC Model / Crypto as Career (220s–350s, 130s, 9 beats)

**OPENING 6s:**

- Speaker RIGHT from t=0: FAIL. Beat c1b1 is described as "full-frame (both speakers)" kinetic at t=0. DESIGN.md is unambiguous: "The opening is NEVER full-frame text on a black background. The speaker is framed on the RIGHT (Mode A or B) starting at t=0 — NOT after the text." The EDL specifies "full-frame (both speakers)" for c1b1 (t=0–3s) with Mode A beginning only at t=3.0. The speaker is not framed on the RIGHT in a split layout from t=0 — they are full-frame. This directly violates the opening rule.

  The DESIGN.md opening sequence spec is: `t=0.0–0.3s` — Kinetic Word Stack or large stat slams in over full-frame video (speaker already framed right). The EDL treats t=0–3s as a full-frame kinetic hook with no Mode A/B framing at all, then transitions to Mode A at t=3.0. That is NOT the same as "speaker framed right from t=0."

  Actually, re-reading DESIGN.md: "The opening is NEVER full-frame text on a black background" and "All opening graphics animate in the LEFT 60% zone while the speaker stays visible on the right." BUT there is a separate DESIGN.md section stating for the opening kinetic beats: "Plays OVER the full-frame video (both speakers visible) with a dark gradient backdrop behind the text." This applies to mid-clip kinetic beats. The opening 6s rule explicitly requires the speaker framed RIGHT in Mode A/B.

  The QA checklist rule states: "Speaker is visible and framed on the RIGHT from t=0 (NOT full-frame text on black) — FAIL if speaker first appears after t=1s." The clip has a kinetic hook at t=0–3s as full-frame, with Mode A only starting at t=3.0. The speaker is visible (both speakers on full-frame video), but NOT framed on the RIGHT per Mode A. This is a FAIL on the opening 6s speaker framing rule.

- 3+ DIFFERENT graphic element TYPES before t=6s: The EDL self-declares PASS with "4 distinct element types before t=6s." The elements listed are: c1b1 kinetic (element 1), c1b2 swiss-grid with index+eyebrow (element 2), rule draws (element 3), stat slams (element 4). However elements 2-4 are all sub-elements of a single swiss-grid beat (c1b2). Per DESIGN.md: "Different ELEMENTS, not one element animating." The index+eyebrow, rule, and stat are sequential animations within a single template. They count as ONE beat with multiple animations, not 3 separate element TYPES. The three element TYPES here are: kinetic-type (c1b1) and swiss-grid (c1b2). That is only 2 distinct template types before t=6s. FAIL.

  Note: The DESIGN.md example shows "index+eyebrow, stat block, tag row/word stack" as 3+ distinct element types — and all are within the same Mode A opening. So the intent is that within the opening beat, you can count index, stat, tag row etc. as distinct element types. Re-reading: "at least 3 DIFFERENT graphic element types fire on the left" — the example says the index/eyebrow is element 1, cyan rule is element 2, large stat is element 3. So sub-elements within a swiss-grid beat DO count as distinct types. On this reading the EDL's claim of PASS may hold IF the kinetic itself is framed in Mode A from t=0. But since Mode A doesn't start until t=3.0 per this EDL's design, the sub-elements of c1b2 only fire after Mode A begins. The kinetic (c1b1, t=0–3s full-frame) + swiss-grid sub-elements (c1b2, t=3s+) do give 4+ element types before t=6s — IF we accept the full-frame kinetic as valid. The element-type count can PASS conditionally, but the speaker framing remains FAIL.

- First graphic at t=0.08 or earlier: PASS — kinetic line 1 fires at t=0.08.

**SPEAKER FRAMING:**

- c1b4 (24–38s): "clean video window. Mode A only. No graphic." PASS — Mode A applied.
- c1b7 (76–99s): "Clean video 76–82s (Mode A)." PASS.
- Full-frame kinetic beats (c1b3, c1b6, c1b8): These are "full-frame (both speakers visible)" kinetic overlay beats. DESIGN.md explicitly permits this: "Exception: full-frame kinetic-type word stack beats with no video" — wait, the actual text is "Exception: full-frame kinetic-type word stack beats with no video." But these beats DO have video (both speakers visible under the kinetic overlay with dark gradient). The kinetic word stack spec says: "Plays OVER the full-frame video (both speakers visible) with a dark gradient backdrop behind the text." So full-frame kinetic WITH video is valid for mid-clip beats. PASS for mid-clip full-frame kinetics.

- 40px bottom clearance in Mode A beats: Not explicitly specified per beat, but the rule exists. Cannot fail on omission in EDL (this is a build-time check). No flag.

**GRAPHIC DEPTH:**

- Minimum 8 beats for 130s clip: PASS — 9 beats.
- No same template twice in a row: The sequence is kinetic → swiss-grid → kinetic → clean → decision-tree → kinetic → clean+swiss-grid → kinetic → liquid-glass. c1b7 is "clean window → swiss-grid" — no consecutive duplicate. PASS.
- Every name-drop has a Liquid Glass Card: c1b9 has the liquid-glass card for "JASPER DE MAERE · WINTERMUTE." But this is used as an outro/closing card ("holds through clip end"), not triggered by a name-drop mid-clip. No other name is dropped in this clip. PASS (the card is present even if used as a closer).
- Every stat has a swiss-grid: c1b2 has swiss-grid with stat "½ DECADE." c1b7 has swiss-grid with "PRINCIPAL TRADING." The "½ DECADE" stat is valid. PASS.
- Every strong sentence has a kinetic word stack: c1b3 "HALF A DECADE ANOTHER CAREER" PASS. c1b6 "WE WAREHOUSE THAT RISK / PRICE IS INCENTIVE / ALIGNED" PASS. c1b8 callback PASS. PASS overall.

**HARD RULES:**

- No intro cards, no outros: c1b9 is a Liquid Glass Card with Jasper's name/title that "holds through clip end." This functions as a closing name card. DESIGN.md: "No outros. Never generate an end card, CTA card, or closing screen of any kind." A liquid glass name card that explicitly "holds through clip end" with no more content after it IS an outro by function even if not labeled as one. FAIL.
- One cyan per frame: Each beat specifies one cyan element. The EDL claims PASS and the beat-level descriptions are consistent. PASS.
- Eyebrow min 32px Inter 700: PASS — specified throughout.
- No backdrop-filter blur: PASS — cross-clip notes specify the correct solid fill approach.
- No grain overlays: PASS — not mentioned.

**FULL-FRAME RULE (clip >90s):**

- c1b3 (t=15–24), c1b6 (t=60–76), c1b8 (t=99–116): All specified as full-frame kinetic over both speakers with dark gradient. PASS.

**WORD SYNC:**

- c1b3: "HALF" fires at comp 15.0, sourced to src 239.72 → comp offset = 239.72 - 220 = 19.72. The EDL says "HALF @ 15.0 (synced to src 239.72)." But 239.72 - 220 = 19.72, not 15.0. That is a 4.72s discrepancy. FAIL — the comp time does not match the stated source time using the clip's own offset formula.

  The beat occupies c1b3 at comp t=15–24s, src 235–244s. Src 239.72 → comp = 239.72 - 220 = 19.72s, not 15.0s. The EDL fires "HALF" at comp 15.0 but says it's "synced to src 239.72." These are inconsistent. Either the comp time is wrong or the source time is wrong.

  "A DECADE" fires at comp 15.38 (src 240.10): 240.10 - 220 = 20.10, not 15.38. Same 4.72s discrepancy throughout c1b3.

  "ANOTHER CAREER" fires at comp 17.18 (src 241.90): 241.90 - 220 = 21.90, not 17.18. Same pattern.

  This is a systematic error in c1b3: all three word timings are off by approximately 4.72s. The EDL's own cross-clip note says "Comp t = src t minus clip's src_in. Example for clip 1: src 239.72 ('half') → comp t = 239.72 - 220 = 19.72s. Every kinetic beat above already has this arithmetic applied inline." But the table shows comp 15.0 for the same src 239.72. The inline arithmetic is NOT applied correctly. FAIL — c1b3 word sync timings are wrong.

- c1b6: "WE WAREHOUSE @ 60.1 (synced to src 328.02)." Comp check: 328.02 - 220 = 108.02, not 60.1. Beat c1b6 src is 278–294s. "THAT RISK @ 60.9 (src 328.80)": 328.80 - 220 = 108.80, not 60.9. "INCENTIVE @ 73.3 (src 332.2)": 332.2 - 220 = 112.2, not 73.3. All three are wrong.

  Additionally, src 328.02 is outside the clip's source window (220–350s) — wait, 328.02 IS within 220–350. But c1b6 beat window is src 278–294s. Src 328.02 is not within the beat's own src window (278–294s). The beat is 16s at comp 60–76s, mapping to src 280–296s. Src 328 is 34s beyond the beat's start — the word "we warehouse" at src 328 does not occur within the c1b6 beat window. FAIL — source timestamps for c1b6 are inconsistent with the beat's declared src range.

- c1b8: "WE WAREHOUSE @ 99.1": This maps to src 99.1 + 220 = 319.1. The beat is src 319–335s. That is within range. Comp 99.1 → src 319.1 ✓. "RISK @ 99.9" → src 319.9 ✓. "INCENTIVE @ 99.1+12.1 = 111.2" → src 331.2 vs stated src 332.2. Minor 1s discrepancy. PASS approximately.

**CLIP 1 VERDICT: FAIL**

Failures:
1. Opening speaker framing: full-frame kinetic at t=0–3s without Mode A right-side framing violates the opening rule. Speaker must be framed RIGHT in Mode A from t=0 with graphics on the left, not full-frame.
2. c1b9 liquid-glass card: functions as a closing outro (holds through clip end with no content after), violating the no-outros rule. Must be repositioned mid-clip or removed.
3. c1b3 word sync: comp times ("HALF @ 15.0") do not match stated src times (239.72 → comp 19.72). Off by ~4.72s throughout the beat.
4. c1b6 word sync: comp times ("WE WAREHOUSE @ 60.1") do not match src times (328.02 → comp 108.02). Also, src 328.02 falls outside the beat's declared src window (278–294s).

---

### CLIP 3 — Structured Products (700s–810s, 110s, 9 beats)

**OPENING 6s:**

- Speaker RIGHT from t=0: FAIL — same structural issue as Clip 1. c3b1 is "full-frame" kinetic at t=0–3s. Mode A begins at t=3.0. Speaker not framed RIGHT in Mode A from t=0.

- 3+ different element types before t=6s: PASS (conditionally on same logic as Clip 1 — kinetic + swiss-grid sub-elements give 4+ types).

- First graphic at t=0.08: PASS.

**SPEAKER FRAMING:**

- c3b5: "Mode A, no graphic." PASS.
- Mid-clip full-frame kinetics (c3b3, c3b7, c3b9): same logic as Clip 1 — valid for mid-clip. PASS.

**GRAPHIC DEPTH:**

- Minimum 8 beats for 110s: PASS — 9 beats.
- No same template twice in a row: kinetic → swiss-grid → kinetic → liquid-glass → clean → decision-tree → kinetic → swiss-grid → kinetic. No consecutive duplicates. PASS.
- Every name-drop: No named person is introduced in this clip's content; the clip covers "structured products in crypto." No liquid glass card for a person is needed mid-clip. PASS.
- Every stat has swiss-grid: c3b2 has swiss-grid with "UHNW" stat, c3b8 has swiss-grid with cycle content. PASS.
- Every strong sentence has kinetic: c3b3, c3b7, c3b9 cover the strong spoken lines. PASS.

**HARD RULES:**

- No intro cards, no outros: No closing card. PASS.
- One cyan per frame: PASS — one cyan element per beat as specified.
- Eyebrow min 32px: PASS.
- No backdrop-filter blur: PASS.

**FULL-FRAME RULE:**

- c3b3 (t=16–26), c3b7 (t=76–88), c3b9 (t=99–110): Full-frame kinetic beats present. PASS.

**WORD SYNC:**

- c3b3: "AUTOCALLABLES @ 16.38 (src 721.38)." Comp check: 721.38 - 700 = 21.38, not 16.38. Off by 5s. FAIL.

  "ACCELERATORS @ 17.44 (src 722.44)": 722.44 - 700 = 22.44, not 17.44. Same 5s error.

  "VIA PRIVATE BANKING @ 21.0 (cyan payoff)": src not given explicitly, but if the pattern holds the src would be around 726, → comp 26. The beat ends at comp 26s, so this might barely be in-range but the 5s offset is present throughout.

- c3b7: "PRICE @ 76.0 (src ~787)": 787 - 700 = 87, not 76. The beat is comp 76–88s, src 776–788s. Src ~787 → comp = 787 - 700 = 87. Off by 11s. FAIL — "PRICE" fires at comp 76.0 but the spoken word is at src ~787 = comp 87. That means the graphic fires 11 seconds BEFORE the speaker says the word.

  "NARRATIVE CREATES PRICE @ 80.0 (cyan payoff, src ~1192)": src ~1192 is completely outside the clip window (700–810s). This is clearly an error — src ~1192 belongs to the capital rotation clip (src 1120–1300). FAIL — wrong source timestamp.

- c3b9: "TAKE RATES @ 99.1" src not given. Beat src is 799–810s → comp 99–110. Comp 99.1 → src 799.1, plausible. No explicit src timestamp to cross-check. PASS conditionally.

**CLIP 3 VERDICT: FAIL**

Failures:
1. Opening speaker framing: same as Clip 1 — full-frame kinetic t=0–3s without Mode A right-side framing.
2. c3b3 word sync: comp times off by ~5s from stated src times (721.38 → comp 21.38, not 16.38).
3. c3b7 word sync: "PRICE @ 76.0" fires 11s before spoken word (src 787 = comp 87). "NARRATIVE CREATES PRICE" uses src ~1192 which is outside this clip's source window entirely — belongs to a different clip.

---

### CLIP 4 — Oct 10 Crash (1010s–1115s, 105s, 8 beats)

**OPENING 6s:**

- Speaker RIGHT from t=0: FAIL — same structure, c4b1 full-frame kinetic t=0–3s, Mode A starts t=3.0.
- 3+ element types before t=6s: PASS (conditionally).
- First graphic t=0.08: PASS.

**SPEAKER FRAMING:**

- c4b5: "Mode A, no graphic." PASS.
- Full-frame kinetics (c4b3, c4b6, c4b8): valid mid-clip. PASS.

**GRAPHIC DEPTH:**

- Minimum 8 beats for 105s: PASS — exactly 8. But note: c4b8 occupies comp t=93–105s (12s), which is a kinetic beat. The beat map has 8 beats. PASS.
- No same template twice in a row: kinetic → swiss-grid → kinetic → decision-tree → clean → kinetic → swiss-grid → kinetic. No consecutive duplicates. PASS.
- Every stat has swiss-grid: c4b2 and c4b7 both have swiss-grid with "25×" stat. PASS.
- Every strong sentence has kinetic: c4b3 (ADL delta), c4b6 (alts down 60/70/80%), c4b8 (25 times callback). PASS.
- Every name-drop: No new name drop in this clip. PASS.

**HARD RULES:**

- No intro cards, no outros: PASS.
- One cyan per frame: c4b2 lists "stat '25×' counts up 1→25 at 3.8–5.2" — the stat is cyan. At t=5.6 "footer 'Stress peak: 30–45 minutes' (green)" fires. A green element and a cyan element in the same frame is technically 2 accent colors, not 2 cyan — but the "one cyan per frame" rule is about the single cyan accent. Green (#16C784) is not cyan. PASS.
- Eyebrow min 32px: PASS.
- No backdrop-filter blur: PASS.

**FULL-FRAME RULE:**

- c4b3 (t=15–26), c4b6 (t=62–78), c4b8 (t=93–105): PASS.

**WORD SYNC:**

- c4b3: "ADL @ 15.46 (src 1023.46)." Comp check: 1023.46 - 1010 = 13.46, not 15.46. Off by 2s.

  "SHIFTS YOUR DELTA @ 20.92 (src 1030.92)": 1030.92 - 1010 = 20.92. PASS — this one matches.

  "COMPLETELY @ 21.74 (src 1031.74)": 1031.74 - 1010 = 21.74. PASS — this one matches.

  So "ADL @ 15.46" is the only mismatch: src 1023.46 - 1010 = 13.46 ≠ 15.46. Off by 2s. The text fires 2s AFTER the spoken word. FAIL — minor but violates the "within ~0.03s" requirement.

- c4b6: "ALTS DOWN @ 62.1" → src would be 1072.1. Beat src is 1072–1088. Plausible. "FEEDBACK LOOP @ 66.0 (cyan payoff). Sourced from beat 11 spoken: 'feedback loop of continuous pressure... alts down 60, 70, 80%.'" — The EDL puts "ALTS DOWN / 60, 70, 80 PERCENT" at lines 1–2 and "FEEDBACK LOOP" as the cyan payoff. But the original spoken order is "feedback loop... alts down 60, 70, 80%." The EDL has inverted the phrase order: "ALTS DOWN" fires first (@ 62.1), then "FEEDBACK LOOP" fires last (@ 66.0 as cyan payoff). The payoff "FEEDBACK LOOP" fires AFTER "ALTS DOWN" — but Jasper says "feedback loop" BEFORE "alts down 60, 70, 80%." The kinetic stack will fire OUT OF SPOKEN ORDER. The stacks should match the spoken sequence or the EDL notes should clarify it's an editorial reorder. As written it's misaligned. FAIL.

- c4b8: "25 TIMES @ 93.6 (src 1095)": 1095 - 1010 = 85, not 93.6. Off by 8.6s. FAIL. The beat src window is 1103–1115. Src 1095 is before the beat's own src start (1103). The word fires before the beat begins according to the stated src time. FAIL — word fires before beat window.

**CLIP 4 VERDICT: FAIL**

Failures:
1. Opening speaker framing: same as Clips 1 and 3.
2. c4b3 word sync: "ADL @ 15.46" but src 1023.46 → comp 13.46. Off by 2s.
3. c4b6 word sync: phrase order inverted relative to spoken order. "ALTS DOWN" fires first, "FEEDBACK LOOP" last — but Jasper says "feedback loop" before "alts down."
4. c4b8 word sync: "25 TIMES @ 93.6 (src 1095)" — src 1095 → comp 85.0, not 93.6. Also src 1095 falls before the beat's declared src start (1103s).

---

### CLIP 5 — Capital Rotation (1120s–1300s, 180s, 11 beats)

**OPENING 6s:**

- Speaker RIGHT from t=0: FAIL — same pattern. c5b1 is full-frame kinetic t=0–3s. Mode A at t=3.0.
- 3+ element types before t=6s: PASS (5 types claimed: kinetic, index+eyebrow, rule, columns, tag row — all within 6s). PASS conditionally.
- First graphic t=0.08: PASS.

**SPEAKER FRAMING:**

- c5b7: "Mode A, no graphic." PASS.
- Full-frame kinetics (c5b3, c5b5, c5b9, c5b11): valid mid-clip. PASS.

**GRAPHIC DEPTH:**

- Minimum 8 beats for 180s: PASS — 11 beats.
- No same template twice in a row: kinetic → swiss-grid → kinetic → liquid-glass → kinetic → decision-tree → clean → swiss-grid → kinetic → decision-tree → kinetic. No consecutive duplicates. PASS.
- Every stat has swiss-grid: c5b2 and c5b8 have swiss-grid. "ALL-TIME HIGH" in c5b4 is a liquid glass card with the stat text. DESIGN.md: "Every stat has a swiss-grid." "ALL-TIME HIGH" is described as a stat. It is implemented as a liquid-glass card, not a swiss-grid. FAIL — a stat ("ALL-TIME HIGH") in a liquid-glass card instead of swiss-grid.

  Counterargument: the liquid glass card here is triggered by a name-drop ("JP Morgan prime brokerage desk"), which is a valid liquid glass trigger. And c5b2 (swiss-grid) does cover stats. The issue is whether "ALL-TIME HIGH" specifically needs a swiss-grid or whether a liquid-glass card named for JP Morgan can contain it. DESIGN.md's rule is "Every stat has a swiss-grid beat." Given that c5b4 is the primary bearer of the JP Morgan stat and is liquid-glass, this is technically a FAIL, but it's marginal. The stricter reading is FAIL.

- Every name-drop has Liquid Glass Card: JP Morgan (beat 14 in source, c5b4) gets a liquid glass card. PASS.
- Every strong sentence has kinetic: c5b3 (retail pivoted), c5b5 (marginal risk dollar), c5b9 (crypto vol compressed), c5b11 (not enough capital). PASS.

**HARD RULES:**

- No outro: c5b11 is "NOT ENOUGH CAPITAL / FOR EVERYTHING / TO PUMP" described as "closes clip on the 'selective cycle' theme previewing clip 6." This is a thematic closer but it's sourced from spoken content in the window and is not a CTA or produced end card. PASS — it's a content beat that happens to be last, not an outro card.
- One cyan per frame: PASS.
- Eyebrow min 32px: PASS.
- No backdrop-filter blur: PASS.

**FULL-FRAME RULE:**

- c5b3, c5b5, c5b9, c5b11: PASS.

**WORD SYNC:**

- c5b3: "RETAIL PIVOTED @ 18.84 (src 1135.84, offset-adjusted)": 1135.84 - 1120 = 15.84, not 18.84. Off by 3s. FAIL.

  "VERY AGGRESSIVELY @ 20.10" — no src given. If following the same offset, src would be ~1137, → comp 17. Inconsistent.

  "INTO EQUITY @ 21.08 (src 1138.08)": 1138.08 - 1120 = 18.08, not 21.08. Off by 3s. FAIL.

  The EDL's own cross-clip notes say: "Comp t = src t minus clip's src_in. Example for clip 1: src 239.72 ('half') → comp t = 239.72 - 220 = 19.72s. Every kinetic beat above already has this arithmetic applied inline." But the arithmetic is wrong here too. The pattern of ~3s over-offset is systematic.

- c5b5: "THE MARGINAL @ 51.1" → src would be 1171.1. Beat c5b5 src is 1171–1188s. "src ~1186" is given for "WENT INTO EQUITIES @ 54.3": 1186 - 1120 = 66, not 54.3. Off by 11.7s. FAIL.

- c5b9: "CRYPTO VOL @ 125.1" → src 1245.1. Beat src is 1245–1263s. "src ~1192" given for EQUITY VOL RISING: 1192 - 1120 = 72, not 128. Src 1192 is outside the beat's source window (1245–1263s) — it belongs to an earlier beat. FAIL — wrong source timestamp, references a src time from a different part of the clip.

- c5b11: "NOT ENOUGH CAPITAL @ 162.1" — no src given. "sourced from the broader window context." No specific word timing provided. Per DESIGN.md: kinetic stacks must fire "within ~0.03s of the spoken word" — this requires word-level timestamps from audio.json. No timestamps given. FAIL — supplemental beat lacks specific word timing; "broader window context" is not a valid word-sync source.

**CLIP 5 VERDICT: FAIL**

Failures:
1. Opening speaker framing: same as all clips above.
2. "ALL-TIME HIGH" stat in liquid-glass card instead of swiss-grid (DESIGN.md: every stat gets a swiss-grid beat).
3. c5b3 word sync: comp times off by ~3s from stated src times throughout.
4. c5b5 word sync: "WENT INTO EQUITIES @ 54.3 (src ~1186)" — 1186 - 1120 = 66, not 54.3.
5. c5b9 word sync: "EQUITY VOL RISING" uses "src ~1192" which is outside the beat's src window (1245–1263s).
6. c5b11 word sync: no specific word timestamps — "broader window context" is not sufficient. All kinetic stacks require word-level timing from audio.json.

---

### CLIP 6 — 4-Year Cycle Dead? (1350s–1470s, 120s, 8 beats)

**OPENING 6s:**

- Speaker RIGHT from t=0: FAIL — same pattern. c6b1 full-frame kinetic t=0–3s.
- 3+ element types before t=6s: PASS (5 types claimed within c6b2 + c6b1).
- First graphic t=0.08: PASS.

**SPEAKER FRAMING:**

- Full-frame kinetics (c6b4, c6b6, c6b8): valid mid-clip. PASS.
- Mode A beats between graphics: present throughout. PASS.

**GRAPHIC DEPTH:**

- Minimum 8 beats for 120s: PASS — exactly 8.
- No same template twice in a row: kinetic → swiss-grid → decision-tree → kinetic → decision-tree → kinetic → swiss-grid → kinetic. No consecutive duplicates. PASS.
- Every stat has swiss-grid: c6b2 has "3.125 BTC" stat in swiss-grid. c6b7 has "1.56 BTC" stat in swiss-grid. PASS.
- Every strong sentence has kinetic: c6b4 (ETF FLOWS SELF-PROPELLING), c6b6 (FOUR YEAR CYCLE BECOMING MEANINGLESS), c6b8 (BLOCK REWARDS HALF TO THE POINT IT DOESN'T MATTER). PASS.
- Every name-drop: No specific name drop requiring a liquid glass card. PASS.

**HARD RULES:**

- No intro cards, no outros: PASS.
- One cyan per frame: c6b3 has a decision-tree with "bullet stagger in" and epoch table on the right "with decaying opacity: 2012: 25 BTC / ... / 2028: 1.56 BTC (cyan)." The final epoch row is cyan. Also c6b3 has bullets on the left — are any of those cyan? The beat specifies "2028: 1.56 BTC (cyan)" as the single cyan element. PASS.
- Eyebrow min 32px: PASS.
- No backdrop-filter blur: PASS.
- muted grey (#888888) on text: The EDL specifies "???" in c7b3 in "#888888" — that's Clip 7, not 6. In c6b3, the epoch table uses "decaying opacity" — if earlier epochs are rendered in #888888 or similar muted color that's under 48px, it would FAIL the "Minimum eyebrow weight: Inter 700, #F0F0F0. Never use muted grey (#888888) for any text smaller than 48px." The epoch table is in "JetBrains Mono" at unspecified size. Risk flag — not enough information to definitively fail, but the "decaying opacity" treatment on small mono text is suspect.

**FULL-FRAME RULE:**

- c6b4 (t=38–55), c6b6 (t=73–90), c6b8 (t=107–120): PASS.

**WORD SYNC:**

- c6b4: "ETF FLOWS @ 38.1 (src ~1354)": 1354 - 1350 = 4, not 38.1. Off by 34s. FAIL — src 1354 is only 4s into the clip, not 38s in. The beat starts at comp 38s (src 1388). Src 1354 is well before the beat starts.

  "SELF-PROPELLING @ 39.5" and "CYCLE NOW @ 41.0 (cyan payoff)" — no src given. The note says "Sourced from beat 17: 'ETF flows are pretty reactive... very self-propelling.'" Beat 17 in the source EDL is at in_secs 1354.0–1401.0. But comp 38–55 corresponds to src 1388–1405. The word "self-propelling" from beat 17 is at src 1354–1401, which could be around src ~1390 → comp ~40. If src ~1390 → comp = 1390 - 1350 = 40.0, that's close to 39.5. The issue is the "ETF FLOWS @ 38.1 (src ~1354)" — src 1354 → comp 4, not 38. FAIL.

- c6b6: "FOUR YEAR CYCLE @ 73.1 (src ~1420)": 1420 - 1350 = 70, not 73.1. Off by 3.1s. Minor. 

  "MEANINGLESS @ 76.5 (cyan payoff)": no src given. The beat src is 1423–1440. Comp 76.5 → src 1426.5, plausible.

- c6b8: "BLOCK REWARDS @ 107.3 (src ~1444)": 1444 - 1350 = 94, not 107.3. Off by 13.3s. The beat src is 1457–1470. Src 1444 is before the beat's declared start (1457s). FAIL — word fires before beat window.

  "IT DOESN'T MATTER @ 111.2 (cyan payoff)": no src given. Beat src 1457–1470. Comp 111.2 → src 1461.2. Beat 18 spoken "block rewards half to a point where it doesn't even matter" is sourced to in_secs 1420.0 per the source EDL. Src 1461 may be toward the end of that content. Risk flag but no definitive fail.

**CLIP 6 VERDICT: FAIL**

Failures:
1. Opening speaker framing: same as all clips.
2. c6b4 word sync: "ETF FLOWS @ 38.1 (src ~1354)" — src 1354 → comp 4.0, not 38.1. Fires 34s before spoken word, and before the beat's own src window (1388–1405s).
3. c6b8 word sync: "BLOCK REWARDS @ 107.3 (src ~1444)" — src 1444 → comp 94.0, not 107.3. Also src 1444 is before the beat's declared src start (1457s).

---

### CLIP 7 — What Kills Bear Markets (1515s–1600s, 85s, 6 beats)

**OPENING 6s:**

- Speaker RIGHT from t=0: FAIL — same pattern. c7b1 full-frame kinetic t=0–3s.
- 3+ element types before t=6s: PASS (5 types claimed).
- First graphic t=0.08: PASS.

**SPEAKER FRAMING:**

- Full-frame kinetics (c7b4, c7b6): valid mid-clip. PASS.
- Mode A beats: implied between kinetics. PASS.

**GRAPHIC DEPTH:**

- Minimum 6 beats for ≤90s: PASS — exactly 6.
- No same template twice in a row: kinetic → swiss-grid → decision-tree → kinetic → liquid-glass → kinetic. PASS.
- Every stat has swiss-grid: c7b2 has swiss-grid with "2020 → 2025 → ???" — this is a label, not a numeric stat. No numeric stat in this clip. No numeric stat means no swiss-grid stat is needed. PASS.
- Every name-drop: Beat 20 source content is "Privacy and AI — top of mind." No specific person named. But wait — c7b5 has "sublabel 'Jasper De Maere · Wintermute.'" This is an attribution, not a primary name-drop. No separate liquid glass card needed for a sublabel attribution. PASS.
- Every strong sentence has kinetic: c7b1 (hook), c7b4 (ordinals/AI agents), c7b6 (privacy and AI callback). PASS.

**HARD RULES:**

- No intro cards, no outros: PASS.
- One cyan per frame: PASS.
- muted grey text rule: c7b3 uses "'???' in #888888." DESIGN.md: "Never use muted grey (#888888) for any text smaller than 48px." The "???" label is in the decision-tree timeline. Its font size is not specified. If it's smaller than 48px (which is likely for a timeline label), this FAILS the muted grey rule. FAIL.
- Eyebrow min 32px: PASS.
- No backdrop-filter blur: PASS.

**FULL-FRAME RULE:**

- Clip is 85s (≤90s) so full-frame rule is not technically required. c7b4 and c7b6 are present anyway. PASS.

**WORD SYNC:**

- c7b1: "BEAR MARKETS @ 0.88 (src 1527, offset-adjusted to comp t=0.88)": 1527 - 1515 = 12, not 0.88. Off by 11.12s. FAIL — "offset-adjusted to comp t=0.88" is wrong. Src 1527 → comp 12.0.

  The EDL acknowledges this by saying "(src 1527, offset-adjusted to comp t=0.88)" — but the math is 1527 - 1515 = 12.0, not 0.88. This is the hook opener and the timing is wrong by 11+ seconds.

- c7b3: "fires @ comp 27.0" for "2022: Inscriptions / Ordinals (src 1542)": 1542 - 1515 = 27.0. PASS — this one is correct.

  "fires @ comp 35.0" for "2023: AI Agents (src 1550)": 1550 - 1515 = 35.0. PASS — correct. Beat c7b3 is comp 18–36s. Comp 35 is within the beat. PASS.

- c7b4: "ORDINALS @ 36.0 (src 1542)": 1542 - 1515 = 27.0, not 36.0. Off by 9s. FAIL. Also, src 1542 is used in c7b3 at comp 27.0 — the same source word fires in two different beats at two different comp times. The "ORDINALS" line in c7b4 fires at comp 36.0 but the spoken word is at src 1542 = comp 27.0, which is during the c7b3 beat. The kinetic in c7b4 does not sync to the spoken word. FAIL.

  "AI AGENTS @ 43.0 (src 1550)": 1550 - 1515 = 35.0, not 43.0. Same problem — src 1550 is during c7b3 (comp 35.0). FAIL.

- c7b5: "PRIVACY in 130px white slams at 54.6 (src 1579.6 offset-adjusted)": 1579.6 - 1515 = 64.6, not 54.6. Off by 10s. FAIL.

- c7b6: "PRIVACY @ 71.6 (src ~1579.6)": 1579.6 - 1515 = 64.6, not 71.6. Off by 7s. FAIL.

**CLIP 7 VERDICT: FAIL**

Failures:
1. Opening speaker framing: same as all clips.
2. "#888888" muted grey used for "???" label in c7b3 — size unspecified, violates the rule if under 48px (very likely).
3. c7b1 word sync: "BEAR MARKETS @ 0.88 (src 1527)" — 1527 - 1515 = 12.0, not 0.88. Off by 11s.
4. c7b4 word sync: "ORDINALS @ 36.0 (src 1542)" — src 1542 → comp 27.0, not 36.0. Word fires 9s after it's spoken.
5. c7b4 word sync: "AI AGENTS @ 43.0 (src 1550)" — src 1550 → comp 35.0, not 43.0. Word fires 8s after spoken.
6. c7b5 word sync: "PRIVACY @ 54.6 (src 1579.6)" — 1579.6 - 1515 = 64.6, not 54.6. Off by 10s.
7. c7b6 word sync: "PRIVACY @ 71.6 (src ~1579.6)" — same src → comp 64.6, not 71.6.

---

### CLIP 8 — AI Multiplier (1675s–1845s, 170s, 11 beats)

**OPENING 6s:**

- Speaker RIGHT from t=0: FAIL — same structural pattern across all clips. c8b1 full-frame kinetic t=0–3s. Mode A at t=3.0.
- 3+ element types before t=6s: PASS (6 types claimed: kinetic, index+eyebrow, rule, two-column stat, footer, sublabel — all within 6s in c8b2). PASS.
- First graphic t=0.08: PASS.

**SPEAKER FRAMING:**

- c8b5: "Mode A, no graphic." PASS.
- Full-frame kinetics (c8b3, c8b7, c8b9, c8b11): valid mid-clip. PASS.

**GRAPHIC DEPTH:**

- Minimum 8 beats for 170s: PASS — 11 beats.
- No same template twice in a row: kinetic → swiss-grid → kinetic → liquid-glass → clean → decision-tree → kinetic → swiss-grid → kinetic → decision-tree → kinetic. No consecutive duplicates. PASS.
- Every stat has swiss-grid: c8b2 (swiss-grid, "2–3 ANALYSTS vs 1 TRADER+AI"), c8b8 ("4 STEPS" swiss-grid). PASS.
- Every strong sentence has kinetic: c8b3 (two to three people), c8b7 (blue wave/short oil), c8b9 (agent controls risk), c8b11 (research and trading). PASS.
- Every name-drop: No new name drops requiring liquid glass in this clip. PASS.

**HARD RULES:**

- No intro cards, no outros: c8b11 is "supplemental phrase build... Sourced from beat 21... Callback close. Exits at 169.8." Again, a content beat that closes the clip but is not a produced outro card. PASS.
- One cyan per frame: PASS.
- Eyebrow min 32px: PASS.
- No backdrop-filter blur: PASS.

**FULL-FRAME RULE:**

- c8b3, c8b7, c8b9, c8b11: PASS.

**WORD SYNC:**

- c8b1: "2–3 ANALYSTS @ 1.60 (src 'two to three' ~1683)": 1683 - 1675 = 8, not 1.60. Off by 6.4s. FAIL — the hook fires at comp 1.60 but the spoken "two to three" is at src ~1683 = comp ~8.

- c8b3: "THE WORK @ 17.2 (src 1677.2)": 1677.2 - 1675 = 2.2, not 17.2. Off by 15s. FAIL — src 1677.2 is only 2.2s into the clip, but fires at comp 17.2.

  "REQUIRES A TEAM @ 18.0 (src ~1681)": 1681 - 1675 = 6.0, not 18.0. Off by 12s. FAIL.

  "OF TWO TO THREE @ 20.0 (src ~1683, cyan payoff)": 1683 - 1675 = 8.0, not 20.0. Off by 12s. FAIL.

  The systematic offset for c8b3 is approximately 12–15s too late — the comp times fire well after the spoken words.

- c8b7: "BLUE WAVE @ 86.1" → src 1761.1. Beat src is 1761–1781. Plausible. PASS.

  "STRAIT OF HORMUZ @ 88.2" → src 1763.2. Plausible. PASS.

  "SHORT OIL @ 90.5 (cyan payoff)" → src 1765.5. Plausible. PASS.

  c8b7 timings are internally consistent with no explicit src given beyond the beat window. PASS conditionally.

- c8b9: "AN AGENT NEEDS @ 124.3" → src 1799.3. Beat src 1799–1820. PASS. "UNDERSTAND YOUR PROFILE @ 128.0 (cyan payoff)" → src 1803.0. PASS. These check out.

- c8b11: "I'M DOING RESEARCH @ 162.1 → src 1837.1. Beat src 1837–1845. PASS." AND TRADING @ 163.5" → src 1838.5. PASS. "AT THE SAME TIME @ 165.0" → src 1840.0. PASS. These check out.

**CLIP 8 VERDICT: FAIL**

Failures:
1. Opening speaker framing: same as all clips.
2. c8b1 word sync: "2–3 ANALYSTS @ 1.60 (src ~1683)" — 1683 - 1675 = 8.0, not 1.60. The hook fires 6.4s before the spoken phrase.
3. c8b3 word sync: all three lines fire 12–15s after the spoken words. "THE WORK @ 17.2 (src 1677.2)" — 1677.2 - 1675 = 2.2s comp, not 17.2. "REQUIRES A TEAM @ 18.0 (src ~1681)" — src 1681 → comp 6.0. "OF TWO TO THREE @ 20.0 (src ~1683)" — src 1683 → comp 8.0.

---

## MASTER SUMMARY

**ALL 7 CLIPS FAIL.** No clip passes every criterion.

---

### Universal Failure — Applies to ALL 7 Clips

**Opening Speaker Framing (FAIL on every clip):**
Every clip uses the identical structure: full-frame kinetic hook at t=0–3s, then Mode A begins at t=3.0. This violates DESIGN.md's explicit rule: "The speaker is framed on the RIGHT (Mode A or B) starting at t=0 — NOT after the text." The correct structure per DESIGN.md is: speaker framed right in Mode A from t=0, with the kinetic overlay firing over the left 60% zone while the speaker is already positioned right. The EDL treats the opening kinetic as a "no speaker framing" moment (full-frame), then transitions to Mode A. That is WRONG. The fix: Mode A (speaker right, 85% right-40% zone) must be active from t=0.0, and the opening kinetic fires over the LEFT zone only, with the speaker visible right from the first frame.

---

### Per-Clip Additional Failures

**CLIP 1:** c1b9 liquid-glass card is a functional outro (last beat, holds through clip end, no content after); c1b3 word sync off by ~4.72s; c1b6 word sync off by ~48s and src timestamps outside beat's own window.

**CLIP 3:** c3b3 word sync off by ~5s; c3b7 "PRICE" fires 11s before spoken word, and "NARRATIVE CREATES PRICE" references src ~1192 which is outside this clip's source window (700–810s) — belongs to Clip 5.

**CLIP 4:** c4b3 "ADL" off by 2s; c4b6 phrase order inverted relative to spoken order (ALTS DOWN fires before FEEDBACK LOOP, but spoken order is FEEDBACK LOOP then ALTS DOWN); c4b8 word fires before beat's declared src window.

**CLIP 5:** "ALL-TIME HIGH" stat implemented as liquid-glass card instead of swiss-grid; c5b3 word sync off by ~3s; c5b5 off by ~11.7s; c5b9 references src ~1192 (outside this beat's window of 1245–1263s); c5b11 has no word-level timestamps ("broader window context" is insufficient).

**CLIP 6:** c6b4 "ETF FLOWS" fires at src 1354 → comp 4.0, stated as comp 38.1 — off by 34s and before beat's own src window; c6b8 "BLOCK REWARDS" src 1444 → comp 94.0 stated as 107.3, also before beat's declared src start.

**CLIP 7:** "#888888" muted grey on "???" label of unspecified size violates the no-muted-grey-under-48px rule; c7b1 "BEAR MARKETS @ 0.88" — src 1527 → comp 12.0, off by 11s; c7b4 lines fire 8–9s after spoken words; c7b5 and c7b6 "PRIVACY" timings off by 7–10s.

**CLIP 8:** c8b1 hook fires 6.4s before spoken "two to three"; c8b3 all three lines fire 12–15s after their spoken words.

---

### What Must Be Fixed Before Any Clip Renders

1. **All 7 clips — Opening structure redesign.** Mode A (speaker right) must be active from t=0. The opening kinetic fires over the LEFT zone while speaker is already framed right. Remove the "full-frame kinetic t=0–3s" pattern from every clip's opening.

2. **All kinetic beats — Word sync recalculation.** The comp times in the EDL do not consistently match `src_time - clip_src_in`. The arithmetic errors are systematic and clip-specific (not a uniform offset). Every kinetic beat's comp times must be recalculated from the audio.json word timestamps. For any "supplemental" beat without specific word timestamps (e.g., c5b11), word timestamps must be looked up in audio.json before the beat can be specified.

3. **Clip 1 — c1b9:** Reposition the liquid-glass name card to mid-clip (around a natural name-drop moment) rather than as the final beat holding through clip end. Or replace it with a kinetic beat and move the name card earlier.

4. **Clip 3 — c3b7:** Remove the src ~1192 reference (wrong clip). Replace with correct src timestamps from within the 700–810s window.

5. **Clip 4 — c4b6:** Fix phrase order to match spoken order, or explicitly note the editorial reorder and confirm word timings.

6. **Clip 5 — "ALL-TIME HIGH" stat:** Add a swiss-grid beat for the JP Morgan stat, or restructure c5b4 as a swiss-grid with the stat and treat the liquid-glass as a supplemental card.

7. **Clip 7 — "???" label:** Specify font size. If under 48px, change color from #888888 to #F0F0F0 or increase to ≥48px.