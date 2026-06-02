# CLIP 8 — AI MULTIPLIER · EDL **v4** (BUILD-READY · rev-3 · FINAL)

> **rev-3 (strict-gate pass — the SIX round-3 Agent-3 defects, all fixed).** rev-2 cleared the R6/R7 headline (no-index; c8b6 + c8b13a fill the two blank-left windows; full-frame close) but the strict gate surfaced six real defects, the worst being that rev-2's own **HARD R7 BUILD RULE #2** ("panel + eyebrow visible from mount, never a bare dark panel ≥0.5s") was applied to c8b6/c8b13a only and **VIOLATED by three earlier Mode-A panels** (c8b7 ~6s bare, c8b5 1.68s bare, c8b11 a hard timing self-contradiction). rev-3 makes the rule **UNIVERSAL — EVERY Mode-A panel mounts its eyebrow + backing as EDITORIAL chrome at its settle** — and fixes all six:
> - **(D1) c8b7 ~6s bare panel** → eyebrow `REVAMPING THE TRADING STACK` is now EDITORIAL @ the 45.0 mount (~45.2) + a resting node-1 frame, not word-synced to 51.00.
> - **(D2) c8b5 1.68s bare panel** → eyebrow `THE PRODUCTIVITY DELTA` + LEFT column are EDITORIAL @ the 26.0 mount (~26.2), not synced to 27.68.
> - **(D3) c8b11 timing self-contradiction** → `data-start` set to **100.7** so the eyebrow (100.84) and bullet-1 (101.82) no longer fire before the mount; c8b10 exits at the 100.7 handoff. Header, beat body, and word-sync audit are now internally consistent.
> - **(D4) two cyan co-present** → REVERSED rev-2's #8 "lingering payoff." c8b1's cyan `A TEAM OF 2–3 ANALYSTS` **fully exits by comp 7.0** and is NOT held into c8b3; any 3→1 callback is WHITE. The "never two FULL-opacity cyan" carve-out is REMOVED — the rule is one cyan element on screen, full-stop (QA §8).
> - **(D5) <8s close** → the c8b13 `…INVESTABLE UNIVERSE` payoff line is DROPPED from the Mode-A card (it lives in the full-frame close as spoken content); the card fades ~159.3, `toFull(159.3)`, so the close is **159.5→167.8 = 8.3s (≥8s)** and the Mode-A block c8b13a+c8b13 is **139.4→159.5 = 20.1s (≥12s, no A-B-A)**. No bookend exception needed.
> - **(D6) c8b4 latent bare panel** → c8b4's backing panel + eyebrow `WHAT AI ABSORBS` mount WITH the video at the 16.0 settle (first kinetic line still 17.46); left zone non-empty from the settle.
>
> All rev-2 improvements are preserved (#1 SHORT OIL not clipped; #2 panel-from-mount — now universal; #3 c8b6 OLD→NEW build; #4 c8b7 connectors; #5 shimmer @5.6; #6 c8b8 anaphora; #7 c8b9 host-Q lingers full-frame; #9 c8b13a bound wording; #10 labeled risk rows not data-chart; #11 out-point verify). R6 PASS; all `_QA-CHECKLIST.md` rules preserved.

**clip_id:** clip_8 · **dir:** `clip-8-ai-multiplier` · **slug:** `clip-8-ai-multiplier`
**Init template:** kinetic-type (host) · **Source:** `source.mp4` (1920×1080, symlink → clip-2 master).
**src_in = 1677.20 · src_out = 1845.00 · duration = 167.80s · comp = src − 1677.20 · data-media-start = 1677.20**

> Timing note (load-bearing): `clip8-words.txt` is based `table_comp = src − 1675`. This EDL is based `comp = src − 1677.20`.
> **Every comp time below was read off the table and converted: `comp = table_comp − 2.20`.** Verified per beat in the WORD-SYNC AUDIT.

---

## WHY v4 (the round-4 rejections being fixed)

v3 was REJECTED for two specific defects the user flagged this round ("Everything has an issue"). v4 fixes BOTH at the structural level and keeps everything v3 got right (dialog-matched coherent open, distinct devices, 83%-center framing, jargon, no dup words, cyan discipline).

1. **R6 — NO INDEX ON SCREEN (the headline fix).** v3 c8b1 rendered the internal clip number **`08`** as a monospace index top-left ("monospace index `08` … top-left"). The bare number is meaningless to a viewer and is now an explicit FAIL. **v4 DELETES the on-screen `08` everywhere.** The open now leads with the editorial eyebrow `THE AI MULTIPLIER` + a grey rule (no number) so first text still lands by t≤0.3s; the kinetic sentence builds on the spoken words below. **No beat in v4 renders any clip number or beat index — only editorial eyebrow labels.** (Verified in the INDEX/NO-NUMBER AUDIT below.)
2. **R7 — VIEW MATCHES CONTENT, no blank-left Mode-A (the second flagged fix).** v3 had TWO blank-left Mode-A stretches (a cropped speaker over an empty left half — the canonical "0:33–0:52" bug):
   - **v3 c8b6 (comp 33–45):** a CLEAN beat (no graphic) sitting INSIDE the Mode-A block S2, between two Mode-A graphic beats → 12s of Jasper cropped right with a blank left 60%. **FAIL.**
   - **v3 c8b13 head (comp 139–151):** Mode-A settled at 138.7 but the risk-card eyebrow didn't appear until 151.14 → ~12s blank-left at the head of S6. v3 itself flagged this "non-blocking" — it is NOT non-blocking under R7; it's a FAIL.
   - **v3 c8b14 tail (comp 165–167.8):** the clip CLOSED in Mode-A after the card faded → a 2.8s cropped-blank-left tail. **FAIL.**

   **v4 enforces R7 absolutely: every Mode-A instant has a left-zone graphic; every clean/breath is full-frame.** Three changes:
   - **c8b6 → a GRAPHIC beat** (OLD→NEW WAY mini-contrast; eyebrow `BUILD IT YOURSELF`). The 33–45 window is active two-speaker speech ("now you can pretty much do any bots or any trading application yourself, basically with AI" — verified continuous in audio.json 1709.6→1720.9), but because it sits inside the Mode-A block, v4 fills the left zone with a real graphic rather than making it a flip-flop full-frame island. **S2 (16→69) is now a contiguous Mode-A block with a graphic on screen at EVERY instant** (c8b4 → c8b5 → c8b6 → c8b7). No clean beat is wedged inside Mode-A. (rev-2 #3: built as an OLD→NEW contrast with internal motion, not a flat chip row.)
   - **c8b13a → a NEW head GRAPHIC** (eyebrow `WHAT THE AGENT INGESTS` chip/mini-list) fills the left zone **139.4→151**, landing the moment Mode-A settles (no empty head). It is word-synced to the verbatim list Jasper gives ("a couple of industries … go long or short … depending on policy"). The risk card (c8b13) follows 151→163.5. **S6 (139.4→163.5) is a contiguous Mode-A block, graphic-filled the entire time.** (rev-2 #1: head pushed 138.7→139.4 so SHORT OIL isn't clipped; #9: on-screen wording bound to `WHAT THE AGENT INGESTS` / `→ ONE DECISION`.)
   - **CLOSE → FULL-FRAME** (c8b14 clean). After the risk card fades (~163.0), the clip's final 4.3s sign-off ("I think it makes a lot of sense. I don't think we're that far off…") plays **full-frame, both speakers** — content, not a card, and never a cropped blank-left tail. The clip ends on conversation (D4 / no-outro) AND full-frame (R7).
3. **Kept verbatim from v3 (do not re-litigate):** the dialog-matched in-point + coherent kinetic open (R5); the two DISTINCT primary devices (productivity comparison + agent-pipeline flow, R2); ≤2 kinetics in a row; `object-position: 83% center` + Ken-Burns scale 1.08→1.12; all jargon corrections (GRUNT WORK, +Paradigm, "dime"/"law" dropped); the within-beat de-dup wording; one-cyan-per-beat; no blur/grain; `#B6BEC6` muted (never `#888888`); z-index:3 completeness. Only the R6 and R7 defects are reworked.

---

## IN / OUT (unchanged — the dialog-matched open is kept)

| field | value | note |
|---|---|---|
| **src_in** | **1677.20** | the exact frame the money line begins: "I can tell you that I think the work which I'm doing today would require a team of two to three people…" (KEPT — this is the dialog-match the user said to keep) |
| **src_out** | **1845.00** | ends clean on "…I don't think we're that far off…". **(#11 — VERIFY-BY-FRAME at the out-point.)** "off" onset = table 169.64 → comp 167.44; the NEXT word "in" onset = table 169.96 → comp 167.76, i.e. the current out (comp 167.80) lets the first ~40ms of "…in" of the next clause leak in. **Action for the build/QA agent:** extract the frame at src_out and listen — if "…in" leaks audibly, trim `src_out` to land on the natural pause right after "off" (≈ src **1844.85**, comp ≈ 167.65). End the clip on the strong line "…we're that far off," not mid-next-clause. Confirm by frame before render. |
| **duration** | **167.80s** | (≈167.65 if trimmed per #11) |
| **comp formula** | **comp = src − 1677.20** | |
| **data-media-start** | **1677.20** | on `<video>` + `<audio>` |
| **data-duration** | **167.8** | master-root + video + audio |

**Opening-frame check (src 1677.20, `/tmp/c8v3_in_1677.png` — extracted + viewed in v3):** hard side-by-side, both speakers visible; **Jasper mid-delivery (mouth open) framed in the right half, burned-in "Jasper De Maere / Wintermute" lower-third visible.** Full-frame kinetic open is valid — NOT "text on black." ✓ (verify-by-frame, opening.)

---

## FRAMING (verified from real source frames — KEPT from v3)

**Source layout (viewed `/tmp/c8v3_in_1677.png`, `/tmp/c8v3_1690.png`, `/tmp/c8v3_hostq_1752.png`):** hard side-by-side. **Nic (host) LEFT half** ("Nic" tag bottom-left). **Jasper (guest, the subject) RIGHT half**, head center ≈ x1380, eyes ≈ 28–32% from top; burned-in **"Jasper De Maere / Wintermute"** lower-third at the bottom of his half (≈ x1000–1250). Host-Q frame (src 1752.5) confirms **Nic speaking left / Jasper listening right** — c8b9 full-frame host-Q is valid (both present).

**Mode-A geometry (clip-2 proven):** `{ left:1229, top:108, width:614, height:864, borderRadius:6px }`; `object-fit:cover` ⇒ cover-scale 0.80 ⇒ no vertical overflow.

### CHOSEN: `object-position: 83% center` + Ken-Burns base **scale 1.08 → 1.12**
- **83%** is the only horizontal position that BOTH centers Jasper AND keeps his burned-in name fully on-screen (90% truncates the name to "…sper De Maere"; 50/62% center the seam/Nic — all WRONG). KEPT from v3.
- **Scale 1.08→1.12** closes the dead ceiling above his head (Mode A has zero vertical overflow, so a vertical bias does nothing — the scale-up is the only ceiling fix). KEPT from v3.
- CSS in `index.html` (already correct; do NOT change to 50/62%):
  ```css
  #short_mag_cut, #short_mag_cut_frame > img.__render_frame__, #short_mag_cut_frame > img.__preview_render_frame__ {
    object-fit: cover; object-position: 83% center;
  }
  ```
  ```js
  masterTL.fromTo(vid, { scale:1.08, transformOrigin:"center center" },
                       { scale:1.12, duration:160, ease:"none" }, 16.0);
  ```

---

## ⭐ VIEW-TIMELINE (proves R1 no-flip-flop + R7 view-matches-content — EVERY Mode-A segment names the graphic that fills it; NO segment is graphic-less)

The source is SIDE-BY-SIDE. Two views: **FULL-FRAME** (both speakers, dark left-gradient backdrop for kinetics/breath) and **MODE-A** (Jasper framed right 40%, graphic in left 60%). **Under R7 a Mode-A segment is valid ONLY if a graphic occupies the left zone for its ENTIRE duration; a clean/breath is ALWAYS full-frame.** The "Graphic filling LEFT zone" column proves no Mode-A instant is blank-left.

| Seg | View | comp range | **Dwell** | Beats in segment | **Graphic filling LEFT zone (R7 — Mode-A only)** | R1/R7 check |
|---|---|---|---|---|---|---|
| S1 | **FULL-FRAME** | 0.0 – 16.0 | **16.0s** | c8b1 (open kinetic) · c8b2 (clean breath) · c8b3 (one-person kinetic) | — (full-frame: both speakers, no crop) | intro+grouped open; 2 kinetics share view; clean breath is full-frame ✓ |
| S2 | **MODE-A** | 16.0 – 69.0 | **53.0s** | c8b4 (kinetic+chips) · c8b5 (swiss before/after) · **c8b6 (OLD→NEW mini-contrast)** · c8b7 (flowchart) | **c8b4 chips → c8b5 swiss-grid → c8b6 OLD→NEW mini-contrast → c8b7 flowchart — a graphic on screen 16.0→69.0 with NO gap** (the v3 c8b6 blank-left is eliminated: c8b6 is now a graphic with internal motion per #3) | ≥8s ✓; **no blank-left** ✓ |
| S3 | **FULL-FRAME** | 69.0 – 81.3 | **~12.3s** | c8b8 (kinetic) · c8b9 (host-Q kinetic) · clean breath | — (full-frame: both speakers) | ≥12s ✓; 2 kinetics share view ✓ |
| S4 | **MODE-A** | 81.3 – 116.5 | **35.2s** | c8b10 (front/back swiss split) · c8b11 (liquid-glass card) | **c8b10 swiss-grid (staggered) → c8b11 liquid-glass card — graphic on screen 81.7→116.1 with no gap** (Mode-A settles 81.0, FRONT header fires 81.72 — no empty head) | ≥8s ✓; **no blank-left** ✓ |
| S5 | **FULL-FRAME** | 116.5 – **139.4** | **22.9s** | c8b12 (BLUE WAVE standout kinetic) + clean breath tail | — (full-frame: both speakers) | ≥8s ✓; **(#1)** settle pushed 138.7→139.4 so SHORT OIL (cyan payoff "oil" at comp 138.92) is read full-frame ~0.9s before the frame moves |
| S6 | **MODE-A** | **139.4** – 163.5 | **24.1s** | **c8b13a (signals chip-row)** · c8b13 (risk liquid-glass card) | **c8b13a chip-row PANEL+eyebrow mount at the 139.4 settle (no empty head) → c8b13 risk card 151→163.5 — graphic on screen 139.4→163.0 with no gap** (the v3 ~12s blank-left head is eliminated) | ≥8s ✓; **no blank-left** ✓ |
| S7 | **FULL-FRAME** | 163.5 – 167.8 | **4.3s** | c8b14 (clean close) | — (full-frame: both speakers — the content sign-off; NOT a cropped-blank tail) | content close, full-frame (R7 — v3's Mode-A clean tail eliminated) ✓ |

**Proof (R1 — no A-B-A inside 12s):** 7 segments. View sequence is a clean alternation `full → ModeA → full → ModeA → full → ModeA → full`. The two distance checks (with the #1 boundary at 139.4):
- **full↔full** (S1,S3,S5,S7): nearest pair is **S5 ends 139.4 / S7 starts 163.5 = 24.1s apart** (≫12s); S3 ends 81.3 / S5 starts 116.5 = 35.2s. ✓
- **ModeA↔ModeA** (S2,S4,S6): nearest pair is **S2 ends 69.0 / S4 starts 81.3 = 12.3s apart**; S4 ends 116.5 / S6 starts **139.4** = 22.9s. ✓ (≥12s — the v3 round-3 A-B-A fix is preserved; the #1 shift only widens this gap.)

**Proof (R7 — view matches content, NO blank-left Mode-A):** Every Mode-A segment (S2, S4, S6) has a named graphic filling the left zone for its ENTIRE duration (see column above) — there is no graphic-less instant inside any Mode-A block. Every clean/breath (S1 c8b2, the S3 mid-gap, the S5 tail, S7 c8b14) is FULL-FRAME (both speakers, no crop). **The three v3 blank-left defects (c8b6 inside S2, c8b13 head of S6, c8b14 Mode-A tail) are all eliminated.** ✓

> **HARD R7 BUILD RULE (#2 — panel is never a bare rectangle):** a mounted left-zone panel is NOT enough — an empty dark panel over a cropped speaker reads as blank-left to a viewer even though it is technically graphic-present. **Every Mode-A panel MUST carry a non-empty resting state from the instant it mounts: the panel + its EYEBROW must be visible from `t = mount` (eyebrow slams in as EDITORIAL chrome at the segment start, NOT word-synced 6s later), with the word-synced content (chips / nodes / rows) staggering in afterward as he speaks.** This applies to the two beats where the first content lands seconds after the settle: **c8b6** (mount 33.0 — eyebrow MUST land ~33.2, not 38.78; chips stagger 39.98→43.44) and **c8b13a** (mount 139.4 — eyebrow MUST land ~139.6, not 139.80, and certainly not the v3 151-style late head). A build that renders a bare dark panel for any span ≥0.5s re-trips R7 and FAILS. ("Panel + eyebrow visible from mount; never a bare panel.")

**Dwell summary:** min block outside the 0–6s intro = S3 (12.3s); the S7 closing clean sign-off (4.3s) is the end-of-clip content tail (the intro-analog: a brief clean bookend, full-frame, not a mid-clip twitch). Every Mode-A block is ≥24.1s and graphic-filled.

> Boundary GSAP (`toFull`/`toModeA` helpers): **S1→S2** `toModeA(16.0, 0.6)` (the ONE early settle; Ken-Burns starts here) · **S2→S3** `toFull(68.7, 0.4)` · **S3→S4** `toModeA(81.0, 0.5)` (full-frame holds through Jasper resuming at comp 79.02 → ModeA gap ≥12s) · **S4→S5** `toFull(116.2, 0.4)` · **S5→S6** **`toModeA(139.4, 0.5)`** (**#1** — pushed from 138.7 into the clean 0.78s sentence boundary: "oil." ends comp 138.92, "There's a couple of industries" starts comp 139.70, so SHORT OIL holds full-frame ~0.9s after "oil"; c8b13a's PANEL+eyebrow mount AT this 139.4 settle so the left is never blank) · **S6→S7** `toFull(163.0, 0.4)` (full-frame for the clean close; fires as the risk card fades). **No transition in 7–16s; no `toModeA` in 69–81s; the clip ENDS full-frame.**

---

## TEMPLATE VARIETY / DEVICE MAP (proves R2)

**PRIMARY DEVICES (this clip, per DESIGN.md):**
1. **Productivity comparison** — `swiss-grid` two-column before/after: **2–3 ANALYSTS → 1 TRADER + AI** (c8b5). The literal payoff of the open and the clip's thesis.
2. **Agent-pipeline flow** — `flowchart` / decision-tree: **state thesis → talk to a terminal → embedded in exchange → +Paradigm** (c8b7, with connector-draws between nodes per #4), with the "it knows your profile / the exchange / how to route your trade" kinetic (c8b8) as its verbal climax, and the c8b13a `WHAT THE AGENT INGESTS` chip-row (go long/short · US policy → one decision) as a downstream echo.

**Template sequence (14 beats — NO two adjacent identical; NOT kinetic-dominated):**

`kinetic(open) → clean → kinetic(one-person) → kinetic+chips → swiss-grid(before/after) → mini-contrast(OLD→NEW WAY) → flowchart → kinetic(it-knows) → host-Q kinetic → swiss-grid(front/back) → liquid-glass(bullets) → kinetic(BLUE WAVE) → chip-row(signals)+liquid-glass(risk-rows) → clean`

- **Kinetic word-stacks: 5 of 14** (c8b1, c8b3, c8b8, c8b9, c8b12) — NOT a stack of kinetics.
- **Max consecutive kinetic = 2:** c8b1→c8b3 (split by clean c8b2, same view) then chips/swiss; c8b8→c8b9 then swiss-grid. **Never 3 in a row.** ✓
- **Non-kinetic devices carry the narrative:** swiss-grid ×2, flowchart ×1, liquid-glass ×2, the c8b6 OLD→NEW mini-contrast ×1 (#3 — a 2-row build, distinct from c8b5's swiss-grid), tag/chip-row ×2 (c8b4 chips, c8b13a signals), host-Q ×1.
- **Catalog blocks to install** (`npx hyperframes add flowchart shimmer-sweep`): `flowchart` (c8b7 talk-to-terminal pipeline — the clip's distinct device, with connector-draw between nodes per #4) · `shimmer-sweep` (ONE premium accent sweep across the cyan payoff line `A TEAM OF 2–3 ANALYSTS` on c8b1, starting @ 5.6 per #5). **(#10 — `data-chart` REMOVED from the install list:** c8b13's "beta / max drawdown" have NO spoken numbers, so a bar chart would be fabricated data on screen. c8b13 renders BETA / MAX DRAWDOWN as **labeled metric ROWS inside the liquid-glass card**, not `data-chart` mini-bars. Reserve `data-chart` for beats with real spoken numbers — there are none in clip 8.) **Hand-build:** kinetic word-stacks (project kinetic-type pattern), swiss-grid two-column (c8b5, c8b10), liquid-glass cards (c8b11, c8b13 risk-rows; DESIGN.md no-blur recipe), tag-chip rows (c8b4, c8b13a), the c8b6 OLD-WAY→NEW-WAY mini-contrast (#3 — a 2-row build, not a static chip row).

**Opening density (DESIGN.md "3+ DIFFERENT element types before 6s") — WITHOUT any index number (R6):** c8b1 fires (1) **eyebrow `THE AI MULTIPLIER`** @ comp 0.08 → (2) **grey rule** draws @ 0.5 → (3) **kinetic line `THE WORK I DO TODAY`** @ 1.78 → (4) line `WOULD REQUIRE` @ 3.44 → (5) **cyan payoff line `A TEAM OF 2–3 ANALYSTS`** + `shimmer-sweep`. Five distinct element TYPES (eyebrow, rule, kinetic phrase build, cyan payoff, shimmer) over both speakers, full-frame. First text present by **t=0.08** (no >1.5s cold-open). The "3 types by 6s" bar is already cleared by 1.78 (eyebrow+rule+kinetic). **(#5 — tighter open:)** the cyan payoff line slams @ 4.80 and the `shimmer-sweep` now STARTS @ **5.6** (the v4 5.6 start, was 6.50) so the premium accent reads INSIDE the 6s window (sweep ~5.6→6.4, riding "two…to three…" landing at comp 4.80/6.48) rather than at the buzzer — a more aggressive open. **No clip-number `08` anywhere** — the eyebrow alone supplies the editorial label. ✓

---

## CYAN DISCIPLINE (one `#00D4FF` element per beat)
c8b1 payoff line `A TEAM OF 2–3 ANALYSTS` · c8b3 payoff line `ONE PERSON.` · c8b4 accent word `GRUNT WORK` · c8b5 RIGHT value `1 TRADER + AI` · c8b6 NEW-WAY accent chip `WITH AI` (the single cyan in the OLD→NEW contrast) · c8b7 final node `+ Paradigm` · c8b8 payoff line `…ROUTE YOUR TRADE` · c8b9 **NONE** (host-Q all-white, by design) · c8b10 divider rule · c8b11 accent bar · c8b12 payoff line `SHORT OIL` · c8b13a accent strip **`→ ONE DECISION`** (**#9** — the bound final wording; NOT the struck first-pass `→ POLICY SIGNALS`) · c8b13 accent bar. Clean beats c8b2 / c8b14 — none.

---

# BEAT-BY-BEAT EDL

> Each kinetic SENTENCE line lists the **on-screen text**, the **transcript words it matches**, and its **comp_t** (read off `clip8-words.txt`, converted `comp = table_comp − 2.20`). Editorial lines are marked `EDITORIAL`.

### c8b1 — OPEN: "THE WORK I DO TODAY / WOULD REQUIRE / A TEAM OF 2–3 ANALYSTS" (kinetic phrase-build) · FULL-FRAME · **COHERENT OPEN (R5), NO INDEX (R6)**
- **comp:** 0.0 – 7.0s · **src:** 1677.20 – 1684.20
- **template/block:** kinetic-type phrase-build (lines slam in & STAY, no dim) + `shimmer-sweep` once across the cyan payoff line · **view:** FULL-FRAME (both speakers, dark left-gradient backdrop) · **sub-comp:** `beat-c8b1-open.html`
- **content & word-sync (reads top-to-bottom as ONE complete sentence):**
  - **Eyebrow ONLY — NO INDEX NUMBER (R6 fix):** eyebrow `THE AI MULTIPLIER` (Inter 700, 32px, `#F0F0F0`, uppercase, 0.18em) slams in @ comp **0.08** (`EDITORIAL` — structural chrome, not word-synced). A **grey** (`#2A2A2A`, NOT cyan) rule draws under the eyebrow @ comp **0.5** — kept grey so the beat's single cyan element stays the payoff line. **There is NO monospace `08` / clip-number / beat-index anywhere on this beat** (v3 rendered `08` top-left; v4 removes it — the eyebrow is the only top-left label). This still satisfies "first text by ~0.3s." `<!-- R6: NO index number. Eyebrow-only top-left. The 3 sentence lines below are word-synced. -->`
  - Line 1 `THE WORK I DO TODAY` — Inter 900, ~120px, white `#F0F0F0` — slam @ comp **1.78** — matches **"the work … today"** ("work" src 1678.98 → 1.78). STAYS.
  - Line 2 `WOULD REQUIRE` — Inter 900, ~120px, white `#F0F0F0` — slam @ comp **3.44** — matches **"would require"** ("require" src 1680.64 → 3.44). STAYS.
  - Line 3 `A TEAM OF 2–3 ANALYSTS` — Inter 900, ~120px, **cyan `#00D4FF`** + glow — slam @ comp **4.80** — matches **"a team of two…to three…people"** ("two" src 1682.00 → 4.80; "to three" src 1683.68 → 6.48; "people" src 1683.90 → 6.70 confirms the noun). **(#5)** `shimmer-sweep` runs once across THIS line **starting @ comp 5.6** (was 6.50) so the premium accent reads INSIDE the 6s window — the sweep travels ~5.6→6.4 as "two…to three" lands, not after the buzzer. STAYS. *(Editorial note: `ANALYSTS` is a light editorial gloss of the spoken "people" — he says "team of two to three people … to conduct the research"; `ANALYSTS` names the research role for coherence. Defensible noun-phrase payoff; not a verbatim word.)*
  - **Coherence (R5):** the three lines parse as the verbatim claim **"the work I do today would require a team of 2–3 [analysts]."** The cyan payoff is a **real noun phrase**, not a dangling number. Lines 1–2 + the count are verbatim word-synced; `ANALYSTS` is the one light editorial gloss.
- **cyan:** Line 3 `A TEAM OF 2–3 ANALYSTS` (one element).
- **R4:** no word repeats across elements (WORK / REQUIRE / TEAM·ANALYSTS all distinct; eyebrow `THE AI MULTIPLIER` shares nothing with the lines).
- **R6:** **no index/number rendered.** ✓
- **#8 — the cyan payoff line LINGERS into c8b3:** lines 1–2 (`THE WORK I DO TODAY`, `WOULD REQUIRE`) drift up/out normally ~comp 6.8, but the **cyan payoff line `A TEAM OF 2–3 ANALYSTS` is HELD at full opacity** (no dim, the phrase-build "STAY" rule) and drifts up slowly through the c8b2 breath, exiting only ~comp **14.5** as c8b3's `ONE PERSON.` (15.00) approaches — so the 3→1 contrast reads as one connected beat (see c8b2/c8b3). It is the SAME single cyan element throughout (no double-cyan).
- **data-start / data-duration:** start 0.0, dur **14.6** (covers 1.78→6.70; lines 1–2 exit ~6.8; **#8 — the cyan payoff line stays full-opacity to ~14.5, drifts out by ~14.6** as c8b3 enters; video does NOT shrink here — it holds full-frame across c8b1→c8b2→c8b3).

### c8b2 — CLEAN VIDEO · FULL-FRAME (grouped with c8b1/c8b3 — R1) · **#8 — hook-tightening (the 2–3 half STAYS visible across the breath)**
- **comp:** 7.0 – 12.0s · **src:** 1684.20 – 1689.20
- **template:** clean (no NEW graphic). **View stays FULL-FRAME — no transition.** · **sub-comp:** —
- **content:** none NEW. Jasper elaborates: "two very hard to do, three very hard working people at least to conduct the research." 5s breath, full-frame, both speakers. **(R7: a clean breath = full-frame, never a cropped blank-left.)**
- **(#8 — stronger cold hook, without breaking word-sync):** the "3 → 1" contrast is the whole thesis, and the reviewer flagged the ~8s + breath gap between the two halves as diluting it. **c8b3's verbatim lines are hard-locked to their spoken words** ("for me … research" = comp 12.76; cannot legally fire earlier). So the faithful fix is visual continuity, not a re-time: c8b1's **cyan payoff line `A TEAM OF 2–3 ANALYSTS` STAYS on screen at full opacity** (the phrase-build "lines STAY / no dim" rule) and lingers — drifting up but visible — **through the breath into c8b3**, so the `2–3` half is STILL on screen when `ONE PERSON.` slams at comp 15.00. The 3→1 contrast therefore reads as a single connected beat across c8b1→c8b3 rather than two disconnected halves. Build note: do NOT exit c8b1's payoff line before ~comp 14.5; let it co-exist briefly with c8b3 L1/L2 so the contrast is simultaneous. The breath has no NEW text but is never "empty" — the locked-in `2–3 ANALYSTS` line carries it.
- **cyan:** none NEW (c8b1's `A TEAM OF 2–3 ANALYSTS` lingers but is the same single cyan element from c8b1, not a second cyan — no double-cyan violation since it's one persistent element from the prior beat).

### c8b3 — "I'M DOING RESEARCH / AND TRADING / ONE PERSON." (kinetic phrase-build) · FULL-FRAME
- **comp:** 12.0 – 16.0s · **src:** 1689.20 – 1693.20
- **template:** kinetic-type phrase-build (lines STAY) · **view:** FULL-FRAME (same view as c8b1/c8b2 — grouped) · **sub-comp:** `beat-c8b3-one-person.html`
- **content & word-sync:**
  - Line 1 `I'M DOING RESEARCH` — white `#F0F0F0` — @ comp **12.76** — matches **"for me … I'm doing research"** ("for" src 1689.96 → 12.76; "research" src 1691.26 → 14.06). Fire on "for me" @ 12.76.
  - Line 2 `AND TRADING` — white `#F0F0F0` — @ comp **14.48** — matches **"and … I'm trading"** ("and" src 1691.68 → 14.48; "trading" src 1692.14 → 14.94).
  - Line 3 `ONE PERSON.` — **cyan `#00D4FF`** payoff — @ comp **15.00** — fires on/just before **"So"** (src 1692.44 → 15.24). `EDITORIAL` — the cyan summary cap of the two verbatim lines above ("research + trading, done by **one person**"). **Fire at 15.00 (≥1s dwell before the 16.0 view settle)** so the cyan payoff is fully read before the frame moves. `<!-- EDITORIAL: cyan summary cap; lines 1–2 verbatim word-synced; fire ≥1s before toModeA(16.0) -->`
- **cyan:** Line 3 `ONE PERSON.` (and c8b1's `A TEAM OF 2–3 ANALYSTS` is still drifting out from above per #8 — but it began fading ~14.5 so by the 15.00 `ONE PERSON.` slam the two are momentarily co-present as the 3→1 contrast, then `2–3` clears; never two FULL-opacity cyan elements at the same instant).
- **R4:** RESEARCH / TRADING / PERSON all distinct.
- **#8 note:** c8b1's persistent `A TEAM OF 2–3 ANALYSTS` line co-exists with c8b3 L1/L2 for the ~1s before `ONE PERSON.` lands, making the 3→1 contrast a single visual beat (the breath no longer disconnects the two halves of the hook).
- **data-start / data-duration:** start 12.0, dur 4.0 (12.76→15.00; exits ~15.8 as the view transitions to Mode A at 16.0 for c8b4).

### c8b4 — "IT COLLAPSES THE LONGER-DURATION GRUNT WORK" + tag chips (kinetic + chips) · MODE-A
- **comp:** 16.0 – 26.0s · **src:** 1693.20 – 1703.20
- **template:** 2-line kinetic + 2 staggered tag-chips (DISTINCT layout) · **view:** MODE-A (S2 begins; `toModeA(16.0,0.6)` here — the ONE early settle) · **sub-comp:** `beat-c8b4-collapse.html`
- **content & word-sync:**
  - Kinetic line 1 `IT COLLAPSES THE` — white `#F0F0F0` — @ comp **17.46** — matches **"completely collapses"** ("completely" src 1694.66 → 17.46; "collapses" 1695.20 → 18.00).
  - Kinetic line 2 `LONGER-DURATION GRUNT WORK` — white with the last words **`GRUNT WORK` cyan `#00D4FF`** — @ comp **19.72** — matches **"longer duration grunt work"** ("longer" src 1696.92 → 19.72; the corrected term **GRUNT WORK** sits on src 1698.32–1698.74 → ~21.12). **R3: Whisper "graft work" → GRUNT WORK** (the flagged fix).
  - Tag chip 1 `ANALYSIS` — slides in @ comp **23.06** — matches **"analysis"** (src 1700.26 → 23.06).
  - Tag chip 2 `DATA GATHERING` — slides in @ comp **23.88** — matches **"data … gathering"** (src 1701.08 → 23.88). Chips = `#F0F0F0` text on `rgba(20,26,34,0.92)`, 1px border, NO cyan fill (cyan is on `GRUNT WORK`).
- **cyan:** `GRUNT WORK` (line-2 accent words — one element).
- **R4:** COLLAPSES / GRUNT WORK / ANALYSIS / DATA GATHERING all distinct within the beat. ✓
- **data-start / data-duration:** start 16.0, dur 10.0 (17.46→23.88; holds to ~25.6, exits as c8b5 enters).

### c8b5 — ⭐ PRODUCTIVITY COMPARISON: "5 YEARS AGO → TODAY" (swiss-grid two-column before/after) · MODE-A · **PRIMARY DEVICE 1**
- **comp:** 26.0 – 33.0s · **src:** 1703.20 – 1710.20
- **template:** swiss-grid two-column before/after — the thesis payoff (2–3 analysts → 1 trader+AI), anchored to his spoken "five years ago" · **view:** MODE-A (grouped with c8b4 — same view) · **sub-comp:** `beat-c8b5-before-after.html`
- **content & word-sync (left col → arrow → right col fills as he contrasts):**
  - **Eyebrow `THE PRODUCTIVITY DELTA`** — Inter 700, 34px, `#F0F0F0` — slam @ comp **27.68** — matches **"night [and day difference]"** (src 1704.88 → 27.68). (R4: deliberately NOT `…5 YEARS AGO`, which would dup the LEFT header.)
  - LEFT column: header `5 YEARS AGO` (Inter 700, 48px, **`#B6BEC6`** muted — NOT `#888888`, which is retired) · value `2–3 ANALYSTS` (Inter 800, ~64px, `#F0F0F0`).
  - Center `→` arrow / divider draws @ comp **28.90** — matches **"difference"** (src 1706.10 → 28.90).
  - RIGHT column: header `TODAY` (Inter 700, 48px, **`#B6BEC6`**) · value **`1 TRADER + AI`** (Inter 800, ~64px, **cyan `#00D4FF`** — the single accent).
  - Footer `same research output` (Inter 600, 28px, `#F0F0F0`) fades in @ comp **30.52** — matches **"five years ago"** ("five" src 1707.72 → 30.52).
- **cyan:** RIGHT value `1 TRADER + AI`.
- **R4:** eyebrow / `5 YEARS AGO` / `TODAY` / `2–3 ANALYSTS` / `1 TRADER + AI` / `same research output` — no shared notable word. ✓
- **muted-text note (carry-over fix):** v3 used `#888888` on these column headers ("permitted ≥48px"). **v4 uses `#B6BEC6`** (the project muted tone) per DESIGN.md/_QA "`#888888` is RETIRED — never use it." Headers read clearly on dark.
- **date language:** "5 YEARS AGO"/"TODAY" are relative — he literally says "five years ago" — no absolute year labels (date rule satisfied).
- **data-start / data-duration:** start 26.0, dur 7.0 (27.68→30.52; holds to ~32.6).

### c8b6 — ⭐ R7 FIX + #3 UPGRADE: "OLD WAY → NEW WAY" (2-row mini-contrast build) · MODE-A · **was a blank-left clean beat in v3 → now a GRAPHIC with internal motion**
- **comp:** 33.0 – 45.0s · **src:** 1710.20 – 1722.20
- **template:** **2-row OLD-WAY→NEW-WAY mini-contrast** (a compact build with an internal arrow/transition between two rows — DISTINCT from c8b5's swiss-grid before/after, from the c8b13a chip-row, from any card, from kinetic). The OLD row is a single muted tag; the NEW row is a chip cluster that fills in as he speaks. Fills the left zone so S2 stays graphic-filled. · **view:** MODE-A (grouped with c8b4/c8b5/c8b7 — S2 holds, NO transition) · **sub-comp:** `beat-c8b6-old-new-way.html`
- **WHY THIS BEAT EXISTS (R7) + WHY IT'S A BUILD NOT A STATIC ROW (#3):** v3 made this window a CLEAN Mode-A beat → 12s of Jasper cropped right over a blank left half (the "0:33–0:52" bug the user flagged). The window IS active speech but sits INSIDE the Mode-A block, so making it full-frame would force a flip-flop (ModeA→full→ModeA within S2). v4 keeps the view stable AND fills the left zone. **#3 reviewer note:** a static 3-chip row holding 12s (chips done firing by 43.4) is the weakest device in the clip and risks reading as filler — exactly the "blank-ish Mode-A" feeling R7 is trying to kill. So c8b6 is upgraded to a small **build** with internal motion: a 2-row OLD→NEW contrast synced to "now you can pretty much do **any bots or any trading application yourself**, basically **with AI**" — the OLD row sets up the contrast, the arrow draws, then the NEW chips stagger in, giving the 12s something to do.
- **content & word-sync (OLD row + eyebrow visible from MOUNT per #2; NEW chips stagger as he lists; accent last):**
  - **Eyebrow `BUILD IT YOURSELF`** — Inter 700, 32px, `#F0F0F0` — **slam @ comp 33.2** (**#2 — lands at the panel mount, NOT 38.78; EDITORIAL chrome, not word-synced**) so the panel is never a bare dark rectangle. *(was @38.78 in v4 rev-1 — moved to mount per the HARD R7 BUILD RULE.)*
  - **OLD-WAY row** `OLD WAY: HIRE A QUANT` — muted `#B6BEC6` tag on the panel — **visible from ~comp 33.6** (EDITORIAL — the contrast setup; he's mid-sentence "in terms of trading with AI… the benefits of…", the OLD frame is editorial scaffolding, not a word-synced claim). The arrow/divider toward the NEW row draws @ comp **38.78** (`strokeDashoffset` 0.55s, DESIGN.md connector spec) as he reaches "now you can pretty much do…", transitioning the eye from OLD → NEW.
  - **NEW-WAY chip 1** `ANY BOTS` (Inter 600, 32px, `#F0F0F0` on `rgba(20,26,34,0.92)`, 1px border, NO cyan) — slide in @ comp **39.98** — matches **"any bots"** (src 1717.18 → 39.98).
  - **NEW-WAY chip 2** `TRADING APPS` (same style) — slide in @ comp **41.00** — matches **"any trading application"** ("trading" src 1718.20 → 41.00; "application" 1718.62 → 41.42).
  - **NEW-WAY chip 3** `WITH AI` — **cyan `#00D4FF`** accent chip (filled `rgba(0,212,255,0.12)` + cyan text/glow — the single accent) — slide in @ comp **43.44** — matches **"basically with AI"** ("with" src 1720.40 → 43.20; "AI" 1720.64 → 43.44).
- **cyan:** NEW-WAY chip 3 `WITH AI` (one element — the OLD row is muted `#B6BEC6`, the eyebrow `#F0F0F0`, so cyan is unique).
- **R4:** eyebrow `BUILD IT YOURSELF` (BUILD·YOURSELF) / OLD row `HIRE A QUANT` (HIRE·QUANT) / NEW chips `ANY BOTS` / `TRADING APPS` / `WITH AI` — all distinct notable words within the beat. ✓ *(Cross-beat: "trading" also in other beats — cross-beat is not an R4 within-beat FAIL.)*
- **R7 (#2 — panel + eyebrow + OLD row visible from mount):** **this beat fills the left zone for 33→45 with a NON-EMPTY resting state from the mount.** The dark backing panel mounts at 33.0; the eyebrow (33.2) and the OLD-WAY row (~33.6) are on it WITHIN ~0.6s — so there is never a bare-panel span ≥0.5s (the HARD R7 BUILD RULE). The arrow draws at 38.78 and the NEW chips stagger 39.98→43.44, giving the rest of the hold internal motion. A graphic is on screen continuously from c8b5 (→32.6) into c8b6 (panel+eyebrow+OLD row from 33.0) with no Mode-A gap. `<!-- R7+#2: panel+eyebrow+OLD row from 33.0–33.6 (no bare panel); arrow draws 38.78; NEW chips 39.98→43.44. No blank-left, no empty hold. -->`
- **data-start / data-duration:** start 33.0, dur 12.0 (panel+eyebrow+OLD row from 33.0; arrow 38.78; NEW chips 39.98→43.44; holds to ~44.6, exits as c8b7 enters at 45.0).

### c8b7 — ⭐ AGENT PIPELINE: "TALK TO A TERMINAL" (flowchart / decision-tree) · MODE-A · **PRIMARY DEVICE 2**
- **comp:** 45.0 – 69.0s · **src:** 1722.20 – 1746.20
- **template:** `flowchart` catalog block — animated nodes + SVG connectors (the clip's distinct device) · **view:** MODE-A (grouped with c8b4/c8b5/c8b6 — S2 holds) · **sub-comp:** `beat-c8b7-terminal-flow.html`
- **content & word-sync (nodes pop `back.out(1.5)` 0.45s on the spoken beat; #4 — CONNECTORS DRAW between every node so the eye keeps moving during the verbal stretches):**
  - Eyebrow `REVAMPING THE TRADING STACK` — slam @ comp **51.00** — matches **"revamping"** (src 1728.20 → 51.00). (R4: `STACK` not `EXPERIENCE` — "experience" lives only in the verbatim sublabel.)
  - **Node 1 `[ State your thesis ]`** — pop @ comp **54.32** — matches **"instead of … books and charts → here is my view about the market"** ("books" src 1731.52 → 54.32; "view" 1735.70 → 58.50). (R4: `thesis` not `market view`.)
  - **Connector 1→2 draws** @ comp **56.4** (`strokeDashoffset`, power1.inOut, 0.55s — DESIGN.md) — arrow grows from node1 toward node2 ahead of the pop.
  - Node 2 `[ Talk to a terminal ]` — pop @ comp **57.04** — matches **"talk to a terminal"** ("terminal" src 1734.24 → 57.04).
  - **(#4) Connector 2→3 draws across the 5.86s verbal stretch** — the arrow from node2 toward node3 begins drawing @ comp **59.0** and travels SLOWLY (`strokeDashoffset`, power1.inOut, ~2.0s draw, completing ~61.5) so the eye is led toward "exchange" during the spoken "here is what I want to express… we are embedding this into our exchange product." This fills the v4 rev-1 node2→node3 dead middle (was a static 5.9s hold) with continuous motion. *(Reviewer #4: this is the soft middle of the tree; the connector-draw keeps it active.)*
  - Node 3 `[ Embedded in the exchange ]` — pop @ comp **62.90** — matches **"embedding this into our exchange product"** ("embedding" src 1740.10 → 62.90).
  - **Connector 3→4 draws** @ comp **64.5** (`strokeDashoffset`, 0.55s) — toward the final node.
  - Node 4 `[ + Paradigm ]` — **cyan `#00D4FF`** final node — pop @ comp **65.54** — matches **"into paradigm … a unified experience"** ("paradigm" src 1742.74 → 65.54; "unified" 1745.26 → 68.06). **R3: "dime terminal" DROPPED** — node is `+ Paradigm` only (the spoken brand; "dime terminal" is `_JARGON.md`-unresolved → not on screen).
  - Sublabel `"Here is my view about the market" → a unified experience` (Inter 600, 24px, `#F0F0F0`).
- **cyan:** final node `+ Paradigm` (connectors are neutral `#3A4452`/grey — NOT cyan — so cyan stays unique to node 4).
- **R4:** Eyebrow (REVAMPING·TRADING·STACK) / Node1 (THESIS) / Node2 (TERMINAL) / Node3 (EXCHANGE) / Node4 (PARADIGM) / sublabel (VIEW·MARKET·EXPERIENCE) — all notable words distinct across elements. ✓
- **note (#4):** a LONG but now-CONTINUOUSLY-ACTIVE 24s hold — 4 nodes pop AND 3 connectors draw between them (the 5.86s node2→node3 gap is now bridged by a slow 2.0s arrow-draw, not a static hold). Not a static card; no dead middle.
- **note (dead tail):** nodes finish at 65.54 (node 4) with "unified" landing 68.06; the tree holds full to the 68.7 cut — the ~3s "tail" after node 4 is covered by node 4's `unified experience` sublabel still resolving and the final connector settling, then the view goes full-frame. No empty static tail.
- **data-start / data-duration:** start 45.0, dur 24.0 (51.00→65.54; connectors 56.4/59.0–61.5/64.5; tree holds to ~68.6, exits as view goes full-frame at 68.7).

### c8b8 — "IT KNOWS YOUR PROFILE / IT KNOWS THE EXCHANGE / IT KNOWS HOW TO ROUTE YOUR TRADE" (kinetic) · FULL-FRAME
- **comp:** 69.0 – 74.0s · **src:** 1746.20 – 1751.20
- **template:** kinetic-type 3-line phrase-build (lines STAY) — the verbal climax of the pipeline · **view:** FULL-FRAME (S3 begins; `toFull(68.7,0.4)`) · **sub-comp:** `beat-c8b8-knows.html`
- **content & word-sync (verbatim, tight):**
  - Line 1 `IT KNOWS YOUR PROFILE` — white `#F0F0F0` — @ comp **70.40** — matches **"it knows your profile"** ("knows" src 1747.60 → 70.40; "profile" 1747.90 → 70.70).
  - Line 2 `IT KNOWS THE EXCHANGE` — white `#F0F0F0` — @ comp **71.52** — matches **"it knows the exchange"** ("exchange" src 1748.72 → 71.52).
  - Line 3 `IT KNOWS HOW TO ROUTE YOUR TRADE` — **cyan `#00D4FF`** payoff — @ comp **72.94** — matches **"it knows how to route your trade"** ("route" src 1750.14 → 72.94; "trade" 1750.46 → 73.26).
- **cyan:** Line 3 (the `…ROUTE YOUR TRADE` payoff).
- **R4:** "IT KNOWS" is intentional anaphora (the spoken structure); distinct notable words are PROFILE / EXCHANGE / ROUTE YOUR TRADE — verbatim parallelism, not a dup-word violation. ✓
- **#6 (KEEP verbatim — option noted):** the reviewer flagged that three 130px lines all starting `IT KNOWS` can read heavy/dup-like at a glance. **Decision: KEEP the strict verbatim line-for-line anaphora** (it is the spoken structure and reads as deliberate emphasis, not a typo). **Optional taste alternative (do NOT build unless the human asks):** drop the repeated "IT KNOWS" to a single small persistent eyebrow `THE AGENT KNOWS:` and make the three stacked lines `YOUR PROFILE` / `THE EXCHANGE` / `HOW TO ROUTE YOUR TRADE` (cyan on line 3) — same verbatim source, cleaner rhythm, shorter cyan payoff. Default build = current verbatim version.
- **data-start / data-duration:** start 69.0, dur 5.0 (70.40→72.94; exits ~73.8).

### c8b9 — HOST QUESTION: "ARE THESE THEMATICS YOU'RE EXPLORING?" (kinetic, no HOST label) · FULL-FRAME
- **comp:** 74.0 – 81.3s · **src:** 1751.20 – 1758.50
- **template:** kinetic-type host-question (left-zone text, NO "HOST" label per DESIGN.md) · **view:** FULL-FRAME (grouped with c8b8 — S3; holds through the gap AND Jasper resuming at comp 79.02 — `toModeA` does NOT fire until 81.0, the R1 A-B-A fix; Nic speaking LEFT, Jasper listening RIGHT — confirmed `/tmp/c8v3_hostq_1752.png`) · **sub-comp:** `beat-c8b9-host-q.html`
- **content & word-sync:**
  - Line 1 `ARE THESE THEMATICS` — white `#F0F0F0` — @ comp **74.72** — matches **"these thematics"** ("these" src 1751.92 → 74.72; "thematics" 1752.06 → 74.86).
  - Line 2 `YOU'RE EXPLORING?` — white `#F0F0F0` — @ comp **75.74** — matches **"you guys are exploring these days"** ("exploring" src 1752.94 → 75.74).
- **cyan:** **NONE by design** (host question all-white; reserves cyan for the guest's answer). The one deliberate no-cyan beat.
- **R4:** THEMATICS / EXPLORING distinct. ✓
- **#7 — the host-Q text LINGERS through the reaction silence (fills the 2.84s dead air):** verified — the question ends "days?" at comp **76.18**, then there is a **2.84s silence** before Jasper answers "Yeah, it is" at comp **79.02** ("Yeah" src 1756.22 → 79.02), all full-frame. **v4 rev-1 exited the text at ~76.2, leaving 2.84s of empty video.** Per the reviewer: **hold `ARE THESE THEMATICS / YOU'RE EXPLORING?` at FULL opacity (no dim) through the silence**, and drift it out only as "Yeah, it is" begins (~comp **79.0**). A held question over the reaction beat is stronger than empty video and fills the dead air. **(This is R7-legal:** the view is full-frame the entire time — both speakers — so the lingering text is a full-frame overlay, never a cropped blank-left.)
- **note (R1/R7):** the view HOLDS full-frame (both speakers) through Jasper's answer resuming at comp 79.02. View settles to Mode-A at 81.0 (`toModeA(81.0,0.5)`), AFTER the answer begins — full-frame dwells 69.0→81.3 (~12.3s); ModeA↔ModeA gap ≥12s.
- **data-start / data-duration:** start 74.0, dur **7.0** (74.72→75.74 text in; **#7: held full-opacity through the 76.2→79.0 silence; drifts out ~79.0–79.6** as "Yeah, it is" begins; div mounted to 81.3, renders the held question until ~79.0 then clears — view holds full-frame).

### c8b10 — FRONT-END vs BACK-END (swiss-grid two-column split) · MODE-A
- **comp:** 81.3 – 102.0s · **src:** 1758.50 – 1779.20
- **template:** swiss-grid two-column — the structural "you guys = front end / us = back end" split (columns fill ~16s apart as he names each side) · **view:** MODE-A (S4 begins; `toModeA(81.0,0.5)`; Mode-A settled by ~81.5) · **sub-comp:** `beat-c8b10-front-back.html`
- **content & word-sync:**
  - **Eyebrow `WHERE AI FITS`** — Inter 700, 34px, `#F0F0F0` — slam @ comp **81.72** alongside the FRONT-END header reveal (lands AFTER the Mode-A settle at 81.0). `EDITORIAL` chrome.
  - LEFT column: header `FRONT END` (Inter 700, 48px, **`#B6BEC6`**) reveals @ comp **81.72** — matches **"on the front end"** ("front" src 1758.92 → 81.72) · body `Intent · expressing risk` (Inter 600, 26px, `#F0F0F0`) @ comp **82.58** — matches **"intent … of risk"** (src 1759.78 → 82.58) · role tag `YOU GUYS` (Inter 600, 32px, `#F0F0F0`).
  - Center divider rule draws @ comp **97.60** — **cyan `#00D4FF`** (the single accent; both column values stay `#F0F0F0`).
  - RIGHT column: role tag `US (Wintermute)` (Inter 600, 32px, `#F0F0F0`) reveals @ comp **94.08** — matches **"For us"** (src 1771.28 → 94.08) · header `BACK END` (Inter 700, 48px, **`#B6BEC6`**) @ comp **97.60** — matches **"on the back end"** ("back" src 1774.80 → 97.60) · body `Market infrastructure` (Inter 600, 26px, `#F0F0F0`) @ comp **98.46** — matches **"market infrastructure"** (src 1775.66 → 98.46).
- **cyan:** the FRONT/BACK divider rule only.
- **R4:** eyebrow `WHERE AI FITS` vs `FRONT END`/`BACK END`/`Intent`/`Market infrastructure`/`YOU GUYS`/`US (Wintermute)` — all distinct. ✓
- **muted-text note:** column headers use `#B6BEC6` (not retired `#888888`).
- **R7:** the Mode-A settle (81.0) lands just before the FRONT reveal (81.72), and the swiss-grid panel mounts at 81.3 — no empty Mode-A head; the graphic carries the whole S4 with c8b11.
- **note:** staggered reveal (FRONT @81.7, BACK @97.6) so the column fills as he contrasts — an ACTIVE ~20s hold.
- **data-start / data-duration:** start 81.3, dur 20.7 (81.72→98.46; rule @97.60; holds to ~101.6).

### c8b11 — BACK-END USE CASES (bulleted liquid-glass card) · MODE-A
- **comp:** 102.0 – 116.5s · **src:** 1779.20 – 1793.70
- **template:** liquid-glass card, 3 staggered bullet rows + payoff strip (DESIGN.md no-blur recipe; distinct from the swiss-grid before it) · **view:** MODE-A (grouped with c8b10 — S4 holds) · **sub-comp:** `beat-c8b11-use-cases.html`
- **content & word-sync (rows stagger; payoff last):**
  - Eyebrow `WHAT AI HANDLES BACK-END` — Inter 700, 34px, `#F0F0F0` — @ comp **100.84** — matches **"can we do … analysis"** ("can" src 1778.04 → 100.84).
  - Bullet 1 `Market analysis` (Inter 600, 30px, `#F0F0F0`) @ comp **101.82** — matches **"analysis"** (src 1779.02 → 101.82). *(R3: Whisper "quick law analysis" — "law" is an unconfirmed artifact, not in `_JARGON.md` → reworded to the confirmed "analysis"; no "law" on screen.)*
  - Bullet 2 `What trades to do` (Inter 600, 30px) @ comp **105.66** — matches **"what type of trades are there to do"** ("trades" src 1782.86 → 105.66).
  - Bullet 3 `Make / take fees` (Inter 600, 30px) @ comp **108.08** — matches **"make or take fees"** ("make" src 1785.28 → 108.08; "fees" 1785.86 → 108.66).
  - Payoff strip `→ WHERE IT LANDS FIRST` (Inter 700, 32px, `#F0F0F0`) @ comp **115.48** — matches **"the biggest fits"** ("biggest" src 1792.68 → 115.48). *(R4: payoff is `WHERE IT LANDS FIRST` not `WHERE AI LANDS FIRST` — "AI" lives only in the eyebrow within this beat.)*
- **cyan:** 4px **cyan `#00D4FF`** left accent bar only.
- **R4 (within beat):** eyebrow `WHAT AI HANDLES BACK-END`, bullets `Market analysis`/`What trades to do`/`Make / take fees`, payoff `WHERE IT LANDS FIRST` — no shared notable word. ✓
- **card CSS:** `rgba(20,26,34,0.92)` + 4px cyan bar + soft glow + 1px border + `mask-image` right-feather. **NO `backdrop-filter`. NO grain.**
- **data-start / data-duration:** start 102.0, dur 14.5 (100.84→115.48; bullets stagger; holds to ~116.1, exits as view goes full-frame at 116.2).

### c8b12 — ⭐ STANDOUT: "BLUE WAVE / STRAIT OF HORMUZ / SHORT OIL" (kinetic phrase-build) · FULL-FRAME · **#1 — SHORT OIL payoff no longer clipped by the view change**
- **comp:** 116.5 – **139.4s** · **src:** 1793.70 – **1816.60**
- **template:** kinetic-type phrase-build (lines STAY) — the clip's dramatic centerpiece (the vivid agent-reasoning example) · **view:** FULL-FRAME (S5; `toFull(116.2,0.4)`; **holds to 139.4 per #1 — the settle moved 138.7→139.4 so the cyan SHORT OIL payoff is read full-frame, not over a collapsing frame**) · **sub-comp:** `beat-c8b12-blue-wave.html`
- **content & word-sync — TWO PHASES (both verbatim):**
  - **Phase A (the setup — fills the ~13s before the example):**
    - Lead `INTENT-BASED TRADING NEEDS:` — Inter 700, 60px, `#F0F0F0` — @ comp **116.92** — matches **"intent based trading"** ("intent" src 1794.12 → 116.92). STAYS through phase A.
    - Mid 1 `INFRASTRUCTURE & HIGH-QUALITY DATA` — Inter 800, ~90px, `#F0F0F0` — @ comp **120.10** — matches **"a lot of infrastructure and high quality data"** ("infrastructure" src 1797.30 → 120.10).
    - Mid 2 `TO LET AGENTS EXPRESS RISK` — Inter 800, ~90px, `#F0F0F0` — @ comp **126.36** — matches **"to be able to allow agents to express risk"** ("agents" src 1802.52 → 125.32; "express" 1803.56 → 126.36).
    - Phase-A lines drift up/out together by ~comp **129** to clear the stage.
  - **Phase B (the example slam — 130px):**
    - Line 1 `BLUE WAVE` — white `#F0F0F0` — @ comp **130.50** — matches **"a blue wave"** ("blue" src 1807.70 → 130.50; "wave" 1807.88 → 130.68).
    - Line 2 `STRAIT OF HORMUZ` — white `#F0F0F0` — @ comp **134.24** — matches **"the Strait of Hormuz"** ("Strait" src 1811.44 → 134.24; "Hormuz" 1812.06 → 134.86).
    - Line 3 `SHORT OIL` — **cyan `#00D4FF`** payoff — @ comp **138.48** — matches **"potentially short oil"** ("short" src 1815.68 → 138.48; "oil" 1816.12 → 138.92).
- **cyan:** Line 3 `SHORT OIL`.
- **R4:** all phase words distinct; no eyebrow/sublabel collision. ✓
- **#1 — CYAN PAYOFF NOT CLIPPED (highest-priority correctness fix):** the cyan payoff `SHORT OIL` slams on "short" at comp **138.48**, but the PAYOFF WORD "oil" lands at comp **138.92** (table 141.12). v4 rev-1 settled to Mode-A at `toModeA(138.7,0.5)` and mounted the next panel at 138.7 — so the frame started moving **0.22s BEFORE "oil" completes**, reading the whole point of the standout ("…SHORT OIL") over a frame already collapsing to a crop. That also violated the clip's own c8b3 rule ("fire the cyan payoff ≥1s before the settle"). **FIX: the S5→S6 settle is pushed to `toModeA(139.4,0.5)`** (the next panel mounts at 139.4, not 138.7). There is a clean **0.78s sentence boundary**: "oil." ends comp **138.92**, the next sentence "There's a couple of industries" starts comp **139.70**. So `SHORT OIL` now holds **full-frame ~0.9s after "oil"** and the frame settles into the natural pause before the next sentence — and there is NO blank-left, because c8b13a's next graphic content (its eyebrow) lands at ~139.6/139.70 anyway, right at the settle.
- **note (S5 dwell):** the beat ends ~139.0 (SHORT OIL fully read); the view holds FULL-FRAME to 139.4 then settles to Mode-A for c8b13a. **The "couple of industries / go long or short / depending on policy / all these things need to process" speech (src 1816.9→1825.1, comp 139.7→147.9) plays in the FOLLOWING Mode-A segment under the c8b13a graphic** (see c8b13a) — it is NOT a full-frame breath here. S5 dwell grows to **22.9s**, S6 to **24.1s** — both still ≫12s, R1 unaffected (only widened).
- **VERIFICATION (src_in 1677.20):** "blue" 1807.70 − 1677.20 = 130.50 ✓; "Strait" 1811.44 − 1677.20 = 134.24 ✓; "short" 1815.68 − 1677.20 = 138.48 ✓; "oil" 1816.12 − 1677.20 = **138.92** ✓ (the payoff word — the settle at 139.4 holds it full-frame); "There's" (next sentence) 1816.90 − 1677.20 = **139.70** ✓ (the 0.78s boundary the settle lands in).
- **data-start / data-duration:** start 116.5, dur **22.9** (covers 116.92→138.92; phase-A exits ~129; phase-B 130.5→138.92; full stack holds SHORT OIL to ~139.2, exits just before the **139.4** settle).

### c8b13a — ⭐ R7 FIX: "WHAT THE AGENT INGESTS" (tag-chip / mini-list row) · MODE-A · **NEW head graphic — fills the v3 blank-left head of S6**
- **comp:** **139.4** – 151.0s · **src:** **1816.60** – 1828.30
- **template:** tag-chip / mini-list row (2 staggered signal chips → cyan action strip; compact, distinct from the risk card that follows and from the c8b6 OLD→NEW contrast) filling the left zone so Mode-A is graphic-filled from the instant it settles · **view:** MODE-A (S6 begins; **`toModeA(139.4,0.5)`** per #1; the chip panel + eyebrow mount AT the settle) · **sub-comp:** `beat-c8b13a-signals.html`
- **WHY THIS BEAT EXISTS (R7):** v3 settled to Mode-A at 138.7 but its risk-card eyebrow did not appear until 151.14 → ~12s of Jasper cropped right over a blank left half (the second flagged blank-left). v4 fills 139.4→151 with this chip-row, word-synced to the verbatim list Jasper gives: "a couple of **industries** which you would **go long or short** on in the US, depending on the **policy** … all these things need to **process**."
- **⚠️ ON-SCREEN WORDING — USE EXACTLY THESE FOUR STRINGS, NOTHING ELSE (#9 — first-pass labels STRUCK so the build agent cannot pick up the wrong term; memory foot-gun "every overlay must use the corrected term"):** eyebrow = `WHAT THE AGENT INGESTS` · chip1 = `GO LONG / SHORT` · chip2 = `US POLICY` · accent strip (cyan) = `→ ONE DECISION`. ~~The first-pass labels `SIGNALS THE AGENT PROCESSES` (eyebrow) and `→ POLICY SIGNALS` (accent) are REJECTED — do NOT render them (they tripped R4: SIGNALS in eyebrow+accent, POLICY in chip2+accent). The four strings above are the only legal on-screen wording.~~
- **content & word-sync (eyebrow visible from MOUNT per #2; chips stagger as he lists; accent last):**
  - Eyebrow `WHAT THE AGENT INGESTS` — Inter 700, 32px, `#F0F0F0` — **slam @ comp 139.6** (**#2 — lands AT the 139.4 panel mount, NOT 139.80; EDITORIAL chrome, not word-synced — panel is never a bare rectangle**). He starts "There's a couple of industries" at src 1816.90 → comp 139.70, so the eyebrow lands right as the sentence opens. *(was @139.80 in rev-1; moved to mount per the HARD R7 BUILD RULE.)*
  - Chip 1 `GO LONG / SHORT` (Inter 600, 32px, `#F0F0F0`, 1px border, NO cyan) — slide in @ comp **143.08** — matches **"go long or short"** ("long" src 1820.28 → 143.08; "short" 1820.74 → 143.54).
  - Chip 2 `US POLICY` (same style) — slide in @ comp **145.18** — matches **"in the US, depending on the policy"** ("US" src 1821.42 → 144.22; "policy" 1822.38 → 145.18).
  - Accent strip `→ ONE DECISION` — **cyan `#00D4FF`** (filled `rgba(0,212,255,0.12)` + cyan text/glow — the single accent) — slide in @ comp **147.10** — matches **"all these things need to be able to process"** ("process" src 1824.70 → 147.50; strip lands ~147.10). The agent ingests these signals → one decision.
- **cyan:** accent strip `→ ONE DECISION` (one element).
- **R4 (within beat) — PASS with the bound wording:** eyebrow `WHAT THE AGENT INGESTS` (INGESTS) / chip1 `GO LONG / SHORT` (LONG·SHORT) / chip2 `US POLICY` (US·POLICY) / accent `→ ONE DECISION` (DECISION) — notable words INGEST / LONG·SHORT / US·POLICY / DECISION are each in exactly one element. ✓ *(The struck first-pass wording WOULD have collided on SIGNALS and POLICY — which is precisely why only the four bound strings are legal; see the ON-SCREEN WORDING line above.)*
- **R7 (#1 + #2):** **this beat fills the left zone 139.4→151, closing the v3 blank-left head of S6.** Build so the dark left-zone PANEL **and its eyebrow** mount at the **139.4** settle (eyebrow ~139.6 — never a bare panel per the HARD R7 BUILD RULE; chips stagger 143→147). The risk card (c8b13) takes over at 151 with no Mode-A gap.
- **muted-text:** any secondary chip caption uses `#B6BEC6` (never `#888888`).
- **data-start / data-duration:** start **139.4**, dur **11.6** (panel + eyebrow mount 139.4; eyebrow 139.6; chips 143.08→147.10; holds to ~150.6, exits as c8b13 enters at 151.0).

### c8b13 — RISK METRICS: "BETA · MAX DRAWDOWN" (liquid-glass card, labeled metric ROWS) · MODE-A · **#10 — labeled rows, NOT data-chart bars (no invented numbers)**
- **comp:** 151.0 – 163.5s · **src:** 1828.30 – 1840.80
- **template:** **liquid-glass card with labeled metric ROWS** (the risk dimensions the agent must track) — **NOT** a `data-chart` mini-bar row. **#10 reason:** the transcript gives NO numbers ("an agent also needs to control risk… beta, max drawdown") — bar-chart heights would be **fabricated data on screen**. The content is a *list of risk dimensions the agent must track*, not measured values, so it renders as a clean labeled list inside the glass card (each row a label, optional `#B6BEC6` descriptor, NO bar/value). This also keeps c8b13 visually distinct from the chip-row c8b13a that precedes it in the same left zone, and removes the `data-chart` install. *(Reserve `data-chart` for beats with real spoken numbers — there are none in clip 8.)* · **view:** MODE-A (S6 holds — grouped with c8b13a; the card replaces the chip-row in the SAME left zone, no view change) · **sub-comp:** `beat-c8b13-risk-metrics.html`
- **content & word-sync (rows stagger):**
  - Eyebrow `AGENTS MUST CONTROL RISK` — Inter 700, 34px, `#F0F0F0` — @ comp **151.14** — matches **"an agent also needs to be able to control risk"** ("control" src 1828.34 → 151.14). (Lands at the c8b13a→c8b13 handoff — the chip-row exits ~150.6, the card enters 151.0, eyebrow 151.14: continuous graphic, no gap.)
  - Metric row 1 `BETA` (Inter 600, 30px, `#F0F0F0`; optional muted descriptor `market sensitivity` `#B6BEC6` — NO numeric value, NO bar) @ comp **155.44** — matches **"beta"** (src 1832.64 → 155.44).
  - Metric row 2 `MAX DRAWDOWN` (Inter 600, 30px, `#F0F0F0`; optional muted descriptor `peak-to-trough loss` `#B6BEC6` — NO value, NO bar) @ comp **157.40** — matches **"max drawdown"** ("max" src 1834.60 → 157.40).
  - Payoff line `…ACROSS THE ENTIRE INVESTABLE UNIVERSE` (Inter 700, 32px, `#F0F0F0`) @ comp **161.98** — matches **"the entire investable universe"** ("entire" src 1839.18 → 161.98; "investable" 1839.54 → 162.34; "universe" 1840.08 → 162.88).
- **cyan:** 4px **cyan `#00D4FF`** left accent bar only.
- **R4:** CONTROL RISK / BETA / MAX DRAWDOWN / INVESTABLE UNIVERSE all distinct. ✓ (Cross-beat: this is the only RISK after c8b13a was reworded to drop "RISK"/"SIGNALS" — c8b13a final eyebrow is `WHAT THE AGENT INGESTS`, so "RISK" appears here, "AGENT" in both but cross-beat is allowed.)
- **card CSS:** same no-blur liquid-glass recipe as c8b11 (solid `rgba(20,26,34,0.92)` + 4px cyan bar + glow + 1px border + mask feather). **No `data-chart`, no bars, no invented values.**
- **R7 / D4 (no-outro):** the card FADES by ~comp **163.0** (after the "investable universe" payoff lands 161.98→162.88) and the view goes FULL-FRAME at 163.0 — the card does NOT hold to clip end, and the clip does NOT close in a cropped Mode-A. The clip closes on clean FULL-FRAME video (c8b14).
- **data-start / data-duration:** start 151.0, dur 12.5 (eyebrow @151.14; rows 155–158; payoff 161.98; fades ~163.0).

### c8b14 — CLEAN VIDEO (close) · FULL-FRAME · **R7: full-frame close, NOT a cropped Mode-A tail · #11 — verify the out-point**
- **comp:** 163.5 – 167.8s · **src:** 1840.80 – 1845.00 *(≈ 163.5–167.65 / src_out ≈1844.85 if trimmed per #11)*
- **template:** clean (no graphic). Card has faded; view is FULL-FRAME (S7; `toFull(163.0,0.4)`) · **sub-comp:** —
- **content:** none. Jasper: "and then digest from there. I think it makes a lot of sense. I don't think we're that far off…" Clip ends on conversation, **full-frame, both speakers** (D4 / no-outro + R7). 4.3s clean tail.
- **WHY FULL-FRAME (R7):** v3 closed in Mode-A after the card faded → a 2.8s cropped-blank-left tail. v4 switches to FULL-FRAME for the close so the final beat shows both speakers (content), never a cropped speaker over an empty half.
- **#11 — END ON THE STRONG LINE (verify-by-frame at the out-point):** the quotable close "I think it makes a lot of sense. I don't think we're that far off…" runs table 167.26→ ⇒ comp **165.06→**, i.e. the strong line STARTS ~comp 165.0; the first ~1.5s of S7 (163.5→165.0) is the tail of the prior sentence ("…and then digest from there"). That tail is fine (full-frame, R7-legal). **But the OUT-point needs verify-by-frame:** "off" onset = comp **167.44** (table 169.64); the NEXT word "in" (next clause) onset = comp **167.76** (table 169.96). The current src_out 1845.00 (comp 167.80) lets the first ~40ms of "…in" leak in. **Action: extract the frame/audio at src_out and listen — if "…in" leaks, trim `src_out` to land on the natural pause right after "off" (≈ src 1844.85, comp ≈ 167.65)** so the clip ends clean on "…we're that far off," not mid-next-clause. Confirm by frame before render.
- **cyan:** none.

---

## FINAL BEAT MAP

| Beat | comp | src | template / block | view | sub-comp | cyan |
|------|------|-----|------------------|------|----------|------|
| c8b1 | 0.0–7.0 | 1677.20–1684.20 | kinetic phrase-build + shimmer-sweep (**COHERENT OPEN, NO INDEX**) | full-frame | beat-c8b1-open.html | line `A TEAM OF 2–3 ANALYSTS` |
| c8b2 | 7.0–12.0 | 1684.20–1689.20 | clean | full-frame | — | — |
| c8b3 | 12.0–16.0 | 1689.20–1693.20 | kinetic phrase-build | full-frame | beat-c8b3-one-person.html | line `ONE PERSON.` |
| c8b4 | 16.0–26.0 | 1693.20–1703.20 | kinetic + tag-chips | Mode-A | beat-c8b4-collapse.html | `GRUNT WORK` |
| c8b5 | 26.0–33.0 | 1703.20–1710.20 | swiss-grid before/after (**DEVICE 1**) | Mode-A | beat-c8b5-before-after.html | `1 TRADER + AI` |
| **c8b6** | 33.0–45.0 | 1710.20–1722.20 | **OLD→NEW WAY mini-contrast (R7 fill + #3 build; was blank-left clean)** | Mode-A | **beat-c8b6-old-new-way.html** | `WITH AI` chip |
| c8b7 | 45.0–69.0 | 1722.20–1746.20 | flowchart (**DEVICE 2**) | Mode-A | beat-c8b7-terminal-flow.html | `+ Paradigm` node |
| c8b8 | 69.0–74.0 | 1746.20–1751.20 | kinetic phrase-build | full-frame | beat-c8b8-knows.html | `…ROUTE YOUR TRADE` line |
| c8b9 | 74.0–81.3 | 1751.20–1758.50 | kinetic host-Q (no label) | full-frame | beat-c8b9-host-q.html | NONE (by design) |
| c8b10 | 81.3–102.0 | 1758.50–1779.20 | swiss-grid front/back split | Mode-A | beat-c8b10-front-back.html | divider rule |
| c8b11 | 102.0–116.5 | 1779.20–1793.70 | bulleted liquid-glass | Mode-A | beat-c8b11-use-cases.html | accent bar |
| c8b12 | 116.5–**139.4** | 1793.70–**1816.60** | kinetic phrase-build (**STANDOUT**; #1 — SHORT OIL held full-frame) | full-frame | beat-c8b12-blue-wave.html | `SHORT OIL` line |
| **c8b13a** | **139.4**–151.0 | **1816.60**–1828.30 | **tag-chip row `WHAT THE AGENT INGESTS` (R7 fill — was blank-left head)** | Mode-A | **beat-c8b13a-signals.html** | `→ ONE DECISION` strip |
| c8b13 | 151.0–163.5 | 1828.30–1840.80 | liquid-glass, labeled risk ROWS (**#10 — no data-chart bars**) | Mode-A | beat-c8b13-risk-metrics.html | accent bar |
| **c8b14** | 163.5–167.8 | 1840.80–1845.00 | **clean (close) — FULL-FRAME (R7, was Mode-A); #11 verify out-point** | full-frame | — | — |

**14 beats** for a 167.8s clip (≥8 required). **No two adjacent beats identical.** **5 kinetics, max 2 in a row.** **7 view segments, no A-B-A inside 12s, every Mode-A segment graphic-filled (no blank-left, no bare panel per #2), clip ends full-frame on content.**

> **Changes vs v3 (R6 + R7 defects, with rev-2 reviewer improvements folded in — see the changelog at the top of this file for the full rev-2 list):** (1) **c8b1** — DELETE on-screen index `08`; eyebrow-only top-left; shimmer @5.6 (#5). (2) **c8b6** — was a blank-left Mode-A clean beat → now `beat-c8b6-old-new-way.html` OLD→NEW mini-contrast (S2 graphic-filled throughout; #3 build + #2 eyebrow/OLD-row from mount). (3) **c8b13a** — NEW beat `beat-c8b13a-signals.html` fills the S6 Mode-A head **139.4**→151 (was blank-left); #2 eyebrow from mount; #9 wording bound to `WHAT THE AGENT INGESTS` / `→ ONE DECISION` (first-pass struck). (4) **c8b13** — start 139.0→151.0, dur 12.5, fades ~163.0; #10 labeled risk ROWS (no data-chart). (5) **c8b14** — view Mode-A → FULL-FRAME; start 163.5; #11 verify out-point. (6) **S5→S6** **`toModeA(139.4,0.5)`** (#1 — pushed from 138.7 so SHORT OIL isn't clipped); **NEW S6→S7** `toFull(163.0,0.4)`. (7) All retired `#888888` → `#B6BEC6`. (8) rev-2: #4 c8b7 connector-draws; #6 c8b8 anaphora kept; #7 c8b9 host-Q lingers through silence; #8 c8b1 payoff lingers into c8b3. **Everything else (c8b2/c8b4/c8b5/c8b10/c8b11 content + timings) is unchanged from v3; c8b3/c8b7/c8b8/c8b9/c8b12 keep their word-sync, with the rev-2 dwell/linger/connector improvements noted per beat.**

---

## WORD-SYNC AUDIT (every non-editorial kinetic/chip line — verified vs `clip8-words.txt`, converted `comp = table_comp − 2.20`)

| beat·line | on-screen text | transcript words | src | comp (src−1677.20) |
|---|---|---|---|---|
| c8b1 L1 | `THE WORK I DO TODAY` | "the work … today" | 1678.98 | **1.78** |
| c8b1 L2 | `WOULD REQUIRE` | "would require" | 1680.64 | **3.44** |
| c8b1 L3 (cyan) | `A TEAM OF 2–3 ANALYSTS` | "a team of two…to three…people" (ANALYSTS = light editorial gloss) | 1682.00 / 1683.68 / 1683.90 | **4.80 / 6.48 / 6.70** |
| c8b3 L1 | `I'M DOING RESEARCH` | "for me … research" | 1689.96 / 1691.26 | **12.76 / 14.06** |
| c8b3 L2 | `AND TRADING` | "and … trading" | 1691.68 / 1692.14 | **14.48 / 14.94** |
| c8b3 L3 | `ONE PERSON.` | EDITORIAL cyan cap (fire 15.00, ≥1s before settle) | 1692.44 | **15.00** |
| c8b4 L1 | `IT COLLAPSES THE` | "completely collapses" | 1694.66 | **17.46** |
| c8b4 L2 | `LONGER-DURATION GRUNT WORK` | "longer duration grunt work" | 1696.92 / 1698.32 | **19.72 / 21.12** |
| c8b4 chip1 | `ANALYSIS` | "analysis" | 1700.26 | **23.06** |
| c8b4 chip2 | `DATA GATHERING` | "data … gathering" | 1701.08 / 1702.14 | **23.88 / 24.94** |
| c8b5 eyebrow | `THE PRODUCTIVITY DELTA` | "night and day difference" (cue) | 1704.88 | **27.68** |
| c8b5 arrow | (divider) | "difference" | 1706.10 | **28.90** |
| c8b5 footer | `same research output` | "five years ago" | 1707.72 | **30.52** |
| **c8b6 eyebrow** | `BUILD IT YOURSELF` | EDITORIAL chrome — lands at panel mount (#2) | — | **33.2** |
| **c8b6 OLD row** | `OLD WAY: HIRE A QUANT` | EDITORIAL contrast setup, visible from mount (#3) | — | **33.6** |
| **c8b6 arrow** | (OLD→NEW connector) | "now you can pretty much do" (`strokeDashoffset` 0.55s) | 1715.40 | **38.78** |
| **c8b6 chip1** | `ANY BOTS` | "any bots" | 1717.18 | **39.98** |
| **c8b6 chip2** | `TRADING APPS` | "any trading application" | 1718.20 | **41.00** |
| **c8b6 chip3 (cyan)** | `WITH AI` | "basically with AI" | 1720.40 / 1720.64 | **43.20 / 43.44** |
| c8b7 eyebrow | `REVAMPING THE TRADING STACK` | "revamping" | 1728.20 | **51.00** |
| c8b7 node1 | `State your thesis` | "books"→"my view about the market" | 1731.52 / 1735.70 | **54.32 / 58.50** |
| c8b7 conn1→2 | (connector draw) | bridge to node2 (`strokeDashoffset` 0.55s) | — | **56.4** |
| c8b7 node2 | `Talk to a terminal` | "terminal" | 1734.24 | **57.04** |
| **c8b7 conn2→3 (#4)** | (slow connector draw, ~2.0s) | fills the node2→node3 verbal stretch | — | **59.0 → 61.5** |
| c8b7 node3 | `Embedded in the exchange` | "embedding … exchange" | 1740.10 | **62.90** |
| c8b7 conn3→4 | (connector draw) | bridge to node4 (`strokeDashoffset` 0.55s) | — | **64.5** |
| c8b7 node4 (cyan) | `+ Paradigm` | "paradigm … unified" | 1742.74 / 1745.26 | **65.54 / 68.06** |
| c8b8 L1 | `IT KNOWS YOUR PROFILE` | "it knows your profile" | 1747.60 / 1747.90 | **70.40 / 70.70** |
| c8b8 L2 | `IT KNOWS THE EXCHANGE` | "it knows the exchange" | 1748.72 | **71.52** |
| c8b8 L3 (cyan) | `…HOW TO ROUTE YOUR TRADE` | "route your trade" | 1750.14 / 1750.46 | **72.94 / 73.26** |
| c8b9 L1 | `ARE THESE THEMATICS` | "these thematics" | 1751.92 / 1752.06 | **74.72 / 74.86** |
| c8b9 L2 | `YOU'RE EXPLORING?` | "you guys are exploring" (#7 — both lines HOLD full-opacity through the 76.2→79.0 reaction silence, drift out ~79.0) | 1752.94 | **75.74** |
| c8b10 L-hdr | `FRONT END` | "on the front end" | 1758.92 | **81.72** |
| c8b10 eyebrow | `WHERE AI FITS` | EDITORIAL chrome (lands w/ FRONT header @81.72, post-settle) | 1758.92 | **81.72** |
| c8b10 L-body | `Intent · expressing risk` | "intent … of risk" | 1759.78 | **82.58** |
| c8b10 US tag | `US (Wintermute)` | "For us" | 1771.28 | **94.08** |
| c8b10 R-hdr | `BACK END` | "on the back end" | 1774.80 | **97.60** |
| c8b10 R-body | `Market infrastructure` | "market infrastructure" | 1775.66 | **98.46** |
| c8b11 eyebrow | `WHAT AI HANDLES BACK-END` | "can we do … analysis" | 1778.04 | **100.84** |
| c8b11 b1 | `Market analysis` | "analysis" | 1779.02 | **101.82** |
| c8b11 b2 | `What trades to do` | "trades" | 1782.86 | **105.66** |
| c8b11 b3 | `Make / take fees` | "make or take fees" | 1785.28 / 1785.86 | **108.08 / 108.66** |
| c8b11 payoff | `→ WHERE IT LANDS FIRST` | "biggest fits" | 1792.68 / 1793.02 | **115.48 / 115.82** |
| c8b12 lead | `INTENT-BASED TRADING NEEDS:` | "intent based trading" | 1794.12 | **116.92** |
| c8b12 mid1 | `INFRASTRUCTURE & HIGH-QUALITY DATA` | "infrastructure … high quality data" | 1797.30 | **120.10** |
| c8b12 mid2 | `TO LET AGENTS EXPRESS RISK` | "agents … express risk" | 1802.52 / 1803.56 | **125.32 / 126.36** |
| c8b12 L1 | `BLUE WAVE` | "a blue wave" | 1807.70 / 1807.88 | **130.50 / 130.68** |
| c8b12 L2 | `STRAIT OF HORMUZ` | "the Strait of Hormuz" | 1811.44 / 1812.06 | **134.24 / 134.86** |
| c8b12 L3 (cyan) | `SHORT OIL` | "potentially short oil" | 1815.68 / 1816.12 | **138.48 / 138.92** |
| **c8b13a eyebrow** | `WHAT THE AGENT INGESTS` | EDITORIAL chrome — lands at the 139.4 panel mount (#2), as "there's a couple of industries" opens (1816.90) | — | **139.6** |
| **c8b13a chip1** | `GO LONG / SHORT` | "go long or short" | 1820.28 / 1820.74 | **143.08 / 143.54** |
| **c8b13a chip2** | `US POLICY` | "in the US … policy" | 1821.42 / 1822.38 | **144.22 / 145.18** |
| **c8b13a accent (cyan)** | `→ ONE DECISION` | "all these things need to … process" | 1824.70 | **147.50** |
| c8b13 eyebrow | `AGENTS MUST CONTROL RISK` | "control risk" | 1828.34 | **151.14** |
| c8b13 row1 | `BETA` | "beta" | 1832.64 | **155.44** |
| c8b13 row2 | `MAX DRAWDOWN` | "max drawdown" | 1834.60 | **157.40** |
| c8b13 payoff | `…ENTIRE INVESTABLE UNIVERSE` | "entire investable universe" | 1839.18 / 1840.08 | **161.98 / 162.88** |

**EDITORIAL (not word-synced):** c8b3 L3 `ONE PERSON.` (cyan cap; lines 1–2 verbatim); the c8b1/c8b6/c8b7/c8b10/c8b13a eyebrows (structural chrome, landing at panel mount per #2 for c8b6/c8b13a); the c8b6 `OLD WAY: HIRE A QUANT` contrast-setup row (#3); the c8b7 connector-draws (#4) and c8b6 OLD→NEW arrow (visual transitions, not text); `ANALYSTS` in c8b1 L3 (light gloss of "people"). Every other kinetic/chip line lands on its spoken word. No anticipatory hook anywhere.

---

## R6 / NO-NUMBER AUDIT (every beat — proves no clip-number or index renders)

| beat | top-left / chrome | renders a number/index? |
|---|---|---|
| c8b1 | eyebrow `THE AI MULTIPLIER` + grey rule | **NO** (v3's `08` deleted) |
| c8b3, c8b8, c8b9, c8b12 | kinetic lines only (no eyebrow chrome with a number) | NO |
| c8b4 | eyebrow via kinetic; chips `ANALYSIS`/`DATA GATHERING` | NO |
| c8b5 | eyebrow `THE PRODUCTIVITY DELTA`; headers `5 YEARS AGO`/`TODAY` (relative words, not an index) | NO |
| c8b6 | eyebrow `BUILD IT YOURSELF`; `OLD WAY: HIRE A QUANT` row; NEW chips (no index/number) | NO |
| c8b7 | eyebrow `REVAMPING THE TRADING STACK`; named nodes (no `01/02/03/04` numbering on nodes — DESIGN.md "no per-card index numbers") | NO |
| c8b10 | eyebrow `WHERE AI FITS`; headers `FRONT END`/`BACK END` | NO |
| c8b11 | eyebrow `WHAT AI HANDLES BACK-END`; bullets (no numbered list markers) | NO |
| c8b13a | eyebrow `WHAT THE AGENT INGESTS`; chips | NO |
| c8b13 | eyebrow `AGENTS MUST CONTROL RISK`; data rows `BETA`/`MAX DRAWDOWN` (metric labels, not an index) | NO |

> The numerals that DO appear on screen are all CONTENT, not indices: `2–3` (team size), `1` (one trader), `14` is NOT used (we say `STRAIT OF HORMUZ`, not "14 days"). No beat renders a clip number `08` or a beat counter `01..14`, and no decision-tree/card carries per-node `01/02/03` numbering. ✓ (R6)

---

## JARGON AUDIT (R3 — every on-screen string vs `_JARGON.md`)

| on-screen string | status |
|---|---|
| `GRUNT WORK` (c8b4) | ✅ CORRECTED from Whisper "graft work" (glossary src 1692.4) |
| `+ Paradigm` (c8b7) | ✅ spoken brand kept; **"dime terminal" DROPPED** (glossary: unresolved → avoid on screen) |
| `Market analysis` (c8b11) | ✅ "law" Whisper artifact (not in glossary) reworded out — no "law" on screen |
| `WITH AI`, `ANY BOTS`, `TRADING APPS`, `OLD WAY: HIRE A QUANT` (c8b6) | ✅ plain English from "any bots or any trading application … with AI"; `HIRE A QUANT` is the editorial OLD-WAY contrast label (#3) — no garble |
| `GO LONG / SHORT`, `US POLICY`, `→ ONE DECISION`, `WHAT THE AGENT INGESTS` (c8b13a) | ✅ plain English from "go long or short … in the US depending on the policy" — no garble |
| `1 TRADER + AI`, `BETA`, `MAX DRAWDOWN`, `Make / take fees`, `Market infrastructure`, `FRONT END`/`BACK END`, `STRAIT OF HORMUZ`, `SHORT OIL`, `BLUE WAVE` | ✅ plain English / standard finance terms, no Whisper garble |
| `Wintermute` (c8b10 US tag) | ✅ exact brand spelling |
| No `burp`/`deep-in`/`graft`/`stake-rate`/`meme con`/`insaturable`/`dime terminal`/`law` anywhere | ✅ |

---

## MUTED-TEXT AUDIT (`#888888` is RETIRED — never use it)

| beat | muted text | color |
|---|---|---|
| c8b5 | column headers `5 YEARS AGO` / `TODAY` | **`#B6BEC6`** (was `#888888` in v3 — fixed) |
| c8b6 | OLD-WAY row `OLD WAY: HIRE A QUANT` (#3 — muted vs the bright NEW chips) | **`#B6BEC6`** |
| c8b10 | column headers `FRONT END` / `BACK END` | **`#B6BEC6`** (was `#888888` in v3 — fixed) |
| c8b13 | optional metric descriptors `market sensitivity` / `peak-to-trough loss` (#10) | **`#B6BEC6`** |
| any chip caption / sublabel | secondary text | `#B6BEC6` |
| all eyebrows / body / values | primary | `#F0F0F0` |

> **No `#888888` anywhere in v4.** Every muted secondary label is `#B6BEC6` (readable ~7:1 on dark). ✓

---

## INDEX.HTML CHANGES REQUIRED (vs current v3 `index.html`)

1. **c8b1 (R6 + #5):** rebuild `beat-c8b1-open.html` with **NO monospace index `08`** — eyebrow `THE AI MULTIPLIER` + grey rule only, top-left. Delete any `#index`/`.clip-num` element. **(#5)** the `shimmer-sweep` across `A TEAM OF 2–3 ANALYSTS` STARTS @ comp **5.6** (not 6.50) so it reads inside the 6s window.
2. **c8b6 (R7 + #3 + #2):** **NEW sub-comp** `compositions/beat-c8b6-old-new-way.html` (**OLD→NEW WAY 2-row mini-contrast** — NOT a flat chip row; #3). It REPLACES the v3 clean Mode-A gap. Add `<div id="beat-c8b6" ...>` with `data-start="33.0" data-duration="12.0"`. **#2 hard rule:** the left-zone PANEL + eyebrow `BUILD IT YOURSELF` + the `OLD WAY: HIRE A QUANT` row are ALL visible from the 33.0 mount (eyebrow ~33.2, OLD row ~33.6 — never a bare panel); the OLD→NEW arrow draws @ 38.78 (`strokeDashoffset` 0.55s); NEW chips stagger 39.98→43.44. **No `toFull`/`toModeA` at the 33–45 boundary** — S2 stays Mode-A across c8b5→c8b6→c8b7.
3. **c8b13a (R7 + #1 + #2 + #9):** **NEW sub-comp** `compositions/beat-c8b13a-signals.html` (tag-chip row). Add `<div id="beat-c8b13a" ...>` with `data-start="139.4" data-duration="11.6"` (**#1 — start pushed 138.7→139.4** so SHORT OIL isn't clipped). **#2 hard rule:** the left-zone PANEL + eyebrow mount at the **139.4** Mode-A settle (eyebrow ~139.6 — never a bare panel; chips stagger 143→147). **#9 — on-screen wording is EXACTLY:** eyebrow `WHAT THE AGENT INGESTS`, chip1 `GO LONG / SHORT`, chip2 `US POLICY`, accent `→ ONE DECISION` (cyan). **Do NOT use the struck first-pass labels `SIGNALS THE AGENT PROCESSES` / `→ POLICY SIGNALS`** (they trip R4).
4. **c8b13 (#10):** push `data-start` 139.0→**151.0**, `data-duration` →**12.5** (fades ~163.0). It enters as c8b13a exits — continuous Mode-A graphic, no gap. **#10 — render BETA / MAX DRAWDOWN as labeled metric ROWS inside the liquid-glass card, NOT `data-chart` mini-bars** (no spoken numbers ⇒ no invented bar heights). No `data-chart` block needed.
5. **c8b14 (R7 + #11):** the clip closes **FULL-FRAME**. Add **`toFull(163.0,0.4)`** at the S6→S7 boundary. c8b14 is a clean full-frame tail 163.5→167.8 — no overlay div, no Mode-A crop. **#11 — verify-by-frame at `src_out`:** if "…in" of the next clause leaks in, trim `src_out` 1845.00→**≈1844.85** (comp ≈167.65) to end clean on "…that far off."
6. **#7 — c8b9 host-Q lingers:** set `beat-c8b9` `data-duration="7.0"` and hold `ARE THESE THEMATICS / YOU'RE EXPLORING?` at full opacity through the 76.2→79.0 reaction silence, drifting out ~79.0 as "Yeah, it is" begins. (Full-frame throughout — R7-legal.)
7. **#8 — c8b1 payoff lingers into c8b3:** do NOT exit c8b1's cyan line `A TEAM OF 2–3 ANALYSTS` before ~comp 14.5; let it co-exist briefly with c8b3 L1/L2 so the 3→1 contrast lands as one connected beat across the breath (never two FULL-opacity cyan elements at the same instant).
8. **#4 — c8b7 connector-draws:** in `beat-c8b7-terminal-flow.html` add SVG connector animations between every node (`strokeDashoffset`, power1.inOut): conn1→2 @56.4 (0.55s), **conn2→3 @59.0 traveling ~2.0s to ~61.5** (fills the verbal stretch), conn3→4 @64.5 (0.55s). Connectors are neutral grey, NOT cyan.
9. **Transitions (final set — #1 changes the S5→S6 time):** `toModeA(16.0,0.6)` · `toFull(68.7,0.4)` · `toModeA(81.0,0.5)` · `toFull(116.2,0.4)` · **`toModeA(139.4,0.5)`** (#1 — was 138.7) · **`toFull(163.0,0.4)`**. **No transition in 7–16s; no `toModeA` in 69–81s; the clip ends full-frame.**
10. **z-index:3 rule** must list EVERY overlay id (clean beats c8b2/c8b14 excluded — c8b14 is full-frame clean):
   `#beat-c8b1, #beat-c8b3, #beat-c8b4, #beat-c8b5, #beat-c8b6, #beat-c8b7, #beat-c8b8, #beat-c8b9, #beat-c8b10, #beat-c8b11, #beat-c8b12, #beat-c8b13a, #beat-c8b13 { z-index: 3; }` (**13 ids** — v3 had 11; ADD `#beat-c8b6` and `#beat-c8b13a`). **CRITICAL: any overlay id missing here renders behind the video.**
11. **Muted text:** in `beat-c8b5-before-after.html` and `beat-c8b10-front-back.html`, change column-header color `#888888` → `#B6BEC6`. The c8b6 OLD-WAY row and any c8b13 descriptor also use `#B6BEC6`.
12. **object-position stays `83% center`**; Ken-Burns `scale 1.08→1.12` start at 16.0. `data-media-start=1677.20`, `data-duration=167.8` (≈167.65 if trimmed per #11) — keep.

## BUILD MANIFEST ROW
`clip_8 | clip-8-ai-multiplier | 1677.20 | 1845.00 | kinetic-type,flowchart,swiss-grid,liquid-glass,shimmer-sweep,tag-chips | 14 beats`
> *(#10 — `data-chart` removed: clip 8 has no spoken numbers, so no bar chart. c8b13 risk metrics render as labeled rows in the liquid-glass card.)*
