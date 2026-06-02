# Clip 7 — v2 EDL (clip-7-bear-market-exit) — RE-DESIGN

**Why v2:** v1 failed review for (1) opening kinetic ("PRIVACY / AND AI / ARE NEXT") did NOT match the
spoken dialog (those words are spoken ~src1582, but the v1 clip opened at src1515 on "a very healthy
shakeout… leverage flushes out"), (2) repetitive/formulaic structure (the generic `07 / EYEBROW / STAT /
tag-row` swiss-grid open every clip used), and (3) framing. This v2 fixes all three:
- **RULE 1:** new in-point lands ON a real spoken line; the opener kinetic IS the words he says THEN.
- **RULE 2:** structure is built around the LEAD DEVICE (TIMELINE-LED). No swiss-grid index/eyebrow opener.
- **RULE 3:** object-position re-verified from extracted source frames (see below).

---

## NEW IN / OUT / DURATION

| field | v1 | **v2** |
|-------|-----|--------|
| `src_in` (data-media-start) | 1515.0 | **1530.76** |
| `src_out` | 1600.0 | **1597.2** |
| duration | 85.0s | **66.44s** (round in HTML to **66.5s**) |
| `comp_t` formula | src − 1515 | **comp = src − 1530.76** |

**In-point rationale (RULE 1):** v1 opened at 1515 on "a very healthy shakeout… a lot of leverage flushes
out of the system" — shakeout talk, NOT the thesis. The directive says open ON "we always exit bear markets
in a very interesting fashion." From `clip7-words.txt`/`audio.json` that sentence is "Well, to your point
around building as well, I feel like **we always exit bear markets in a very interesting fashion**…" The
filler head ("Well, to your point around building as well, I feel like") is trimmed; the cut lands on the
breath right before **"we" @ src1530.94**, so `src_in = 1530.76`. The clip opens cold on the thesis sentence,
word-synced.

**Out-point rationale:** the thesis payoff completes on Jasper's "…either completely in that vertical or at
least **adjacent to it**" (`it` @ src1595.84). The next word, "Yeah" @ src1597.32, is **Nic**. End on Jasper's
content beat → `src_out = 1597.2` (≈1.4s settle after "adjacent to it", before Nic's reply). This also strips
v1's dead tail and tightens the clip 85s→66.5s, which directly addresses the "repetitive/too long" feel.

---

## OBJECT-POSITION (RULE 3 — verified from real frames)

**Chosen: `object-position: 84% center`** (one point right of clip-2's proven 83%; NOT 50%/62%).

**Frames extracted & viewed** (source.mp4 is 1920×1080, 30fps):
- `ffmpeg -nostdin -ss 1535  -i …/source.mp4 -frames:v 1 /tmp/fr_c7_1535.png`  (just before Mode A starts)
- `ffmpeg -nostdin -ss 1582  -i …/source.mp4 -frames:v 1 /tmp/fr_c7_1582.png`  (inside c7b5 Mode-A payoff)
- `ffmpeg -nostdin -ss 1593  -i …/source.mp4 -frames:v 1 /tmp/fr_c7_1593.png`  (inside c7b5 Mode-A payoff)
- (+ 1530.2 at the in-point)

**What I saw:** classic SIDE-BY-SIDE. Nic (host) fills the LEFT half, **Jasper (guest) fills the RIGHT half**,
each centered in their own half. Jasper's **face/body center sits at ≈ x1390–1410** (slightly right of his
half-center 1440 toward frame center). His head top is ≈ y90px (moderate ceiling/wall above — breathing room,
not excessive), **eyes ≈ y290–320 (≈ 27–30% from top)**. His "Jasper De Maere / Wintermute" name lower-third
sits bottom-left of his panel, **left edge ≈ x990, baseline ≈ y1010–1060**. Stable across all four frames.

**Why 84% (math, source coords):** Mode A crops to a 614×864 portrait. `object-fit: cover` scales the source
by height (0.8) → the 614px-wide window shows a **768px-wide source slice**. `object-position: X%` puts that
slice's center at `X%×(1920−768)+384 = X%×1152+384`:
- 50% → center 960 (the seam between the two men) — **WRONG** (centers the divider/host edge).
- 62% → center 1098 — **WRONG** (still includes the seam, half-host).
- 83% (clip-2) → center 1340; window source 956–1724 — correct guest framing (approved reference).
- **84% (chosen) → center 1352; window source 968–1736.** Centers Jasper's ~1400 face a touch better than 83%
  while keeping his name lower-third (left edge ~990) just inside the window-left (968), and trimming the dead
  right-wall. **No vertical bias / scale-up needed:** with eyes at ~28%, the 864-tall window puts them in the
  upper third with the moderate ceiling reading as natural headroom — no dead-ceiling correction required.

Mode A geometry (unchanged from clip-2/clip-1 convention): `left:1229, top:108, width:614, height:864`
(bottom clearance 108px > 40px so the name never clips; top clearance 108px > 20px).

---

## LEAD DEVICE — TIMELINE-LED

The hero is the **narrative-cycle timeline** (ETF → ordinals/inscriptions → DeFi → AI agents → **?**). It
builds node-by-node ON each spoken era, and ends on an **unresolved cyan "?" node**. The rest of the clip
answers that "?": the closing payoff RESOLVES the "?" into **PRIVACY + AI**. This structural pose-and-answer
is unique to this clip and replaces the formulaic swiss-grid open. No `07 / EYEBROW / STAT / tag-row` block
anywhere in this clip.

**Template sequence:** kinetic → **decision-tree (HERO timeline)** → kinetic → [clean] → kinetic → liquid-glass.
**Adjacency:** the only same-template neighbors are c7b3 (kinetic) and c7b4 (kinetic); they are separated by a
≥2s clean Mode-A window, so no two graphic beats of the same template render back-to-back. PASS.
**Cyan discipline:** exactly one `#00D4FF` element per beat (kinetic = payoff line; tree = the open "?" node;
card = accent bar). PASS.

---

## BEAT TABLE

> `comp = src − 1530.76`. Every kinetic SENTENCE below is word-synced to the transcript; the matched words +
> their `src_t`/`comp_t` are quoted inline so it is auditable. EDITORIAL (anticipatory / label) lines are marked.

### c7b1 — KINETIC opener · full-frame (both speakers) → Mode A @ 5.4 · `beat-c7b1-hook.html`
- **comp 0.0–5.4 · src 1530.76–1536.16**
- Block/template: `kinetic-type` (3-line phrase build, lines STAY, no dim). Dark gradient backdrop left zone.
- Speaker mode: **full-frame 1920×1080** (both speakers visible) for the whole opener; GSAP shrinks video to
  Mode A at comp 5.4 as the opener wipes up.
- **This is the RULE-1 fix:** the opener IS the spoken line, word-synced (NOT anticipatory):
  | on-screen line | transcript words it matches | src_t | **comp_t fire** | color |
  |---|---|---|---|---|
  | `WE ALWAYS EXIT` | "we always exit" | we 1530.94 / always 1531.52 / exit 1532.66 | **0.18** | #F0F0F0 |
  | `BEAR MARKETS` | "bear markets" | bear 1533.86 / markets 1534.40 | **3.10** | #F0F0F0 |
  | `IN A WILD WAY` | "in a very interesting fashion" | very 1535.02 / interesting 1535.02 / fashion 1535.56 | **4.26** | **#00D4FF** (payoff) |
- Note on line 3 text: spoken is "in a very interesting fashion"; on-screen condensed to **`IN A WILD WAY`** to
  fit 3-word kinetic rhythm — fires on the same beat ("very/interesting" @4.26). If a literal match is
  preferred, use `IN AN INTERESTING WAY` at the same comp (still word-synced to "interesting" @4.26). Either is
  acceptable; both land on the spoken phrase. Cyan element: line 3 only.
- `data-start=0.0 data-duration=5.4` (covers 0.18→4.26 + 0.3s headroom; exit wipe at ~5.0).

### c7b2 — DECISION-TREE: the narrative-cycle TIMELINE (HERO) · Mode A · `beat-c7b2-narrative-cycle.html`
- **comp 5.4–31.5 · src 1536.16–1562.26**
- Block/template: `decision-tree` re-skinned as a **vertical narrative-cycle timeline** (spine + nodes, each
  pops `back.out(1.5)` ON its spoken word). This is the hero centerpiece — replaces the v1 swiss-grid open.
- Speaker mode: **Mode A** (video framed right 40%, object-position 84%); glow + zone-rule fade in at 5.4.
- Eyebrow (EDITORIAL label, marked): `HOW CRYPTO EXITS BEAR MARKETS` — Inter 700, 34px, #F0F0F0, slam @ 5.8.
  `<!-- EDITORIAL: section label, not word-synced -->`
- Cyan rule draw @ 6.2 — NOTE: rule is **#2A2A2A (neutral)**, NOT cyan, because the single cyan element in
  this beat is the open "?" node (D7: one cyan element per beat). The rule is a structural divider only.
- Nodes (each fires ON its spoken word; quoted):
  | node | on-screen | transcript words | src_t | **comp_t fire** | color |
  |---|---|---|---|---|---|
  | n1 | `2024 · ETF ANNOUNCEMENTS` | "the sort of 24, we had the ETF announcements" | ETF 1541.26 | **10.50** | #F0F0F0 |
  | n2 | `ORDINALS + INSCRIPTIONS` | "suddenly we had like inscriptions and ordinals" | inscriptions 1543.76 | **13.00** | #F0F0F0 |
  | n3 | `DeFi SUMMER` | "excited about like Bitcoin, DeFi" | DeFi 1547.58 | **16.82** | #F0F0F0 |
  | n4 | `AI AGENTS` | "Then we had AI agents… very early inflection" | AI 1550.82 | **20.06** | #F0F0F0 |
  | n5 | `?  ·  NEXT` | "very curious what we will come up with as the next narrative" (EDITORIAL turn) | curious 1556.28 / next 1559.54 | **25.52** | **#00D4FF** |
- The spine slow-draws from comp ~6.6 down to n5 across the beat. n5 is the **open question** — the single cyan
  element, rendered ≥48px (so D7's `#F0F0F0`-under-48px rule does not apply; cyan is the node fill/glow). It
  holds unresolved through the beat end — this is the pose the clip will answer.
  `<!-- EDITORIAL: n5 "?" is the open-question turn, fires on "curious/next" — anticipatory of the answer -->`
- `data-start=5.4 data-duration=26.5` (covers 10.50→25.52 with headroom; nodes 1–4 word-synced, n1 lead
  spacing is fine because the prior eras are being narrated 9–20s). Cyan element: n5 only.

### c7b3 — KINETIC: the "spiral" mechanism · full-frame (both speakers) · `beat-c7b3-spiral.html`
- **comp 31.5–41.0 · src 1562.26–1571.76**
- Block/template: `kinetic-type` (4-line phrase build, lines STAY). Explains WHY the cycle repeats.
- Speaker mode: **full-frame** (both speakers); video expands from Mode A → full-frame at ~31.5 (resets
  Ken-Burns). A different template + a full-frame moment right after the Mode-A timeline = variety.
- Word-synced (verified spoken: "it is again… a spiral where like prices go up. We find the narrative. People
  get excited about it late in the cycle."):
  | on-screen line | transcript words | src_t | **comp_t fire** | color |
  |---|---|---|---|---|
  | `IT'S A SPIRAL` | "a spiral where" | spiral 1564.66 | **33.90** | #F0F0F0 |
  | `PRICES GO UP` | "like prices go up" | prices 1565.70 / go 1566.30 / up 1566.54 | **34.94** | #F0F0F0 |
  | `WE FIND THE NARRATIVE` | "We find the narrative" | We 1567.02 / find 1567.12 / narrative 1567.48 | **36.26** | #F0F0F0 |
  | `EXCITED LATE IN THE CYCLE` | "People get excited about it late in the cycle" | People 1568.02 (line lead) / excited 1568.34 / late 1569.32 / cycle 1570.96 | **37.26** (fires on first word "People" per D2) | **#00D4FF** (payoff) |
- `data-start=31.5 data-duration=9.5` (covers 33.90→37.26, lines hold; exit ~40.6). Cyan: line 4 only.

### (clean breath) · Mode A · no sub-comp
- **comp 41.0–44.8 · src 1571.76–1575.56** — ~3.8s clean Mode-A window. Video returns to Mode A at 41.0.
  Speaker breath after the spiral kinetic (he's saying "For example we had like perp dexes, meme coin launch
  platforms"). Separates the two kinetics (c7b3, c7b4) so no two same-template graphic beats render
  back-to-back. Within the D6 ≤8s cap.

### c7b4 — KINETIC: "cadence of innovation" bridge · full-frame · `beat-c7b4-cadence.html`
- **comp 44.8–49.4 · src 1575.56–1580.16**
- Block/template: `kinetic-type` (2-line phrase build). The thesis bridge before the payoff.
- Speaker mode: **full-frame** (video expands from Mode A → full-frame at ~44.8). Separated from c7b3 by the
  clean breath above.
- Word-synced (verified spoken: "But that cadence of innovation, I think is super interesting to see."):
  | on-screen line | transcript words | src_t | **comp_t fire** | color |
  |---|---|---|---|---|
  | `THE CADENCE` | "that cadence of" | cadence 1576.08 | **45.32** | #F0F0F0 |
  | `OF INNOVATION` | "of innovation" | innovation 1576.64 | **45.88** | **#00D4FF** (payoff) |
- `data-start=44.8 data-duration=4.6` (covers 45.32→45.88; lines hold to ~49.0 exit). Cyan: line 2 only.

### c7b5 — LIQUID-GLASS payoff: the "?" RESOLVES → PRIVACY + AI · Mode A · `beat-c7b5-privacy-ai.html`
- **comp 49.4–66.5 · src 1580.16–1597.26** (clip end)
- Block/template: **liquid-glass card** that pays off the timeline's open "?" node — the answer. Card spec per
  D7: `rgba(20,26,34,0.92)` solid fill, **4px cyan accent bar** (inset left), soft glow, 1px border,
  `mask-image` feather into the video. **NO backdrop-filter blur. NO grain.**
- Speaker mode: **Mode A** (video framed right 84%); glow + zone-rule return at 49.4. Card holds over live
  continuing speaker video through clip end.
- Structural rhyme: the card opens with a small **`?  →`** glyph (echoing c7b2's open node) that the two
  candidate words slam in beside — visually "filling in" the answer.
- Eyebrow (EDITORIAL label, marked): `THE FRONTRUNNERS` — Inter 700, 32px, #F0F0F0, @ 49.6.
  `<!-- EDITORIAL: section label -->`
- Word-synced reveal (verified spoken: "I think it's anyone's guess currently **privacy and AI**… top of mind
  for many… the **front runners** in terms of what we might see"):
  | on-screen | transcript words | src_t | **comp_t fire** | color |
  |---|---|---|---|---|
  | `PRIVACY` (word 1, 130px) | "currently privacy" | privacy 1581.92 | **51.16** | #F0F0F0 |
  | `AI` (word 2, 130px) | "and AI" | AI 1583.44 | **52.68** | #F0F0F0 |
  | `Top of mind — the frontrunners` (sublabel, 26px) | "top of mind for many… the front runners" | mind 1585.04 / front 1587.84 | **54.28** | #F0F0F0 |
- **D4 no-outro:** this is a CONTENT reveal (the thesis answer), NOT a name/credit card. There is **NO "Jasper
  De Maere · Wintermute" attribution** (v1's name sublabel is removed — review flagged it as a soft outro). The
  card lands on Jasper's spoken "privacy and AI," then holds while he finishes "…either completely in that
  vertical or at least adjacent to it" (it @ src1595.84 / comp 65.08). The clip ends on this live content beat;
  the final ~1.4s is the card gently settling over continuing speaker video — not a static end screen.
- Cyan element: the accent bar only (`?` glyph is #F0F0F0; words #F0F0F0).
- `data-start=49.4 data-duration=17.1`.

---

## SUB-COMP FILES (compositions/)
| beat | sub-comp filename | status |
|------|-------------------|--------|
| c7b1 | `beat-c7b1-hook.html` | REWRITE (new word-synced opener text + offsets) |
| c7b2 | `beat-c7b2-narrative-cycle.html` | REWRITE (5-node timeline ending on cyan "?" node; new comp times) |
| c7b3 | `beat-c7b3-spiral.html` | NEW (rename of v1 beat-c7b5-spiral; recomputed comps) |
| c7b4 | `beat-c7b4-cadence.html` | NEW (cadence-of-innovation 2-line kinetic) |
| c7b5 | `beat-c7b5-privacy-ai.html` | REWRITE (rename of v1 beat-c7b7; "?"→answer rhyme, new comps) |
| — | (v1 `beat-c7b2-narrative-cycle.html` swiss-grid, `beat-c7b3-exit-timeline.html`, `beat-c7b4-whats-next.html`) | RETIRE — replaced |

**index.html updates required:** new `data-media-start="1530.76"`, `data-duration="66.5"` on video+audio and
master-root; update the z-index:3 rule to list exactly the 5 new beat ids
(`#beat-c7b1-hook, #beat-c7b2-narrative-cycle, #beat-c7b3-spiral, #beat-c7b4-cadence, #beat-c7b5-privacy-ai`);
re-time the GSAP phase map to the new Mode-A/full-frame windows above; set `object-position: 84% center`.

---

## VERIFICATION CHECKLIST
- **RULE 1 (open on a real line):** opener c7b1 fires `WE ALWAYS EXIT`@0.18 / `BEAR MARKETS`@3.10 /
  `IN A WILD WAY`@4.26 — all matched to spoken we/bear/interesting at the NEW in-point 1530.76. No anticipatory
  text. PASS.
- **RULE 2 (vary structure):** NO `07/EYEBROW/STAT/tag-row` swiss-grid open. Hero = vertical narrative-cycle
  timeline ending on an open cyan "?" node; the closing card RESOLVES that "?" — a pose/answer device unique to
  this clip. PASS.
- **RULE 3 (framing):** object-position **84%** chosen from viewing real frames (Jasper face ≈x1400, name
  lower-third left edge ≈x990); 50%/62% rejected (center the seam). PASS.
- **Word-sync (D2):** every kinetic SENTENCE has a real `comp_t` from `clip7-words.txt` quoted above; only the
  two eyebrow labels + the n5 "?" turn are marked EDITORIAL. PASS.
- **Adjacency:** kinetic→tree→kinetic→[clean]→kinetic→card; the only same-template pair (c7b3/c7b4 kinetic)
  is split by a clean Mode-A window. PASS.
- **One cyan per beat:** c7b1 line3 / c7b2 "?" node / c7b3 line4 / c7b4 line2 / c7b5 accent bar. PASS.
- **D4 no-outro:** ends on c7b5 content reveal over live video; no name/credit card. PASS.
- **D7 palette/type:** "?" node ≥48px so #F0F0F0-under-48 rule moot; eyebrows Inter 700 ≥32px #F0F0F0; card no
  blur/grain; date label "2024" only (no 2025/2024 ambiguity — 2024 is the historical ETF year he names). PASS.

**Build Manifest Row:** `clip_7 | clip-7-bear-market-exit | 1530.76 | 1597.2 | decision-tree (timeline-led) | 5 beats`
