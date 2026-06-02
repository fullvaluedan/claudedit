# Clip 4 — Oct 10 Crash (ADL Cascade) — EDL **v3** (BUILD-READY, supersedes clip4-edl-v2.md)

**Source:** `src_in 1030.76 → src_out 1118.98` | **Duration 88.2s** | **Slug:** `clip-4-oct10-crash`
**Comp offset:** `comp_t = src_t − 1030.76`
**Beat count:** 7 (c4b1, c4b2, c4b3, c4b4, c4b5, c4b6, c4b8 — id `c4b7` intentionally skipped to keep the existing index.html z-index slot names)
**Object-position (Mode A):** `83% center` — kept from v2 (verified vs extracted frames at src 1044.7 & 1090.9: Jasper centered, seam/host excluded, name-tag kept).
**Primary device (DESIGN per-clip map):** **`flowchart` ADL cascade as the cold open** (c4b2) + **`caption-kinetic-slam`** on the 25× reveal (c4b5).

---

## Why v3 (what v2 still failed, now fixed)

v2 was close but tripped the graded gate (`_QA-CHECKLIST.md`) on three items:

1. **R1 view flip-flop — TWO sub-8s islands (the headline defect).**
   - v2 c4b3 full-frame = **6.2s** (33.8→40.0) wedged between Mode-A cascade and Mode-A clean → under the 8s floor.
   - v2 c4b6 Mode-A = **6.6s** (73.6→80.2) wedged between full-frame c4b5 and full-frame c4b8 → **full→ModeA→full = A-B-A within 12s** — the exact clip-7/clip-8 bug `_QA-CHECKLIST.md §1` names. **FAIL.**
   - **v3 fix:** regrouped into **5 sustained views**, every non-intro view **≥12.3s**, no A-B-A (proof table below). The 10.8s "clean window" is absorbed into a full-frame block instead of forcing an extra switch.
2. **Task device deviation — 25× was `apple-money-count`, not `caption-kinetic-slam`.** The task mandates `caption-kinetic-slam` for the 25× reveal. **v3 fix:** c4b5 is now `caption-kinetic-slam` (single-word slams, alternating entrance) — installed via `npx hyperframes add caption-kinetic-slam`.
3. **R4 duplicate words in c4b5** — v2 eyebrow `DERIVATIVES vs SPOT` + line `DERIVATIVES THAN SPOT` repeated "DERIVATIVES" and "SPOT" in one beat. **v3 fix:** `caption-kinetic-slam` carries no eyebrow; the slam words are unique within the beat.
4. **25× restated as a swiss-grid micro-stat (v2 c4b6) re-introduced the formulaic chrome the redesign bans and double-stated the clip's headline number.** **v3 fix:** the redundant `20–25×` swiss-grid is **cut**; the old `c4b6` slot is repurposed to a **NEW, non-duplicative** liquid-glass beat that is **word-matched to the line spoken at its fire time** (the leverage-fueled rally — "the melt-up was very heavily supported by leverage"), which also breaks the kinetic run before the closer.

**v3.1 patch (post-QA, this revision):** two gate findings closed —
   - **c4b6 sync re-anchor (QA §3 "text appears as the person says it").** The prior v3 draft fired c4b6 (`PERP-SIDE LIQUIDATION`) at comp 75.48 on `supported`, but at that instant the speaker is saying *"[the melt-up was] very heavily supported by leverage"* — the perp-side-liquidation line (`liquidation`@comp 57.96, `perp side`@comp 58.98) was actually spoken ~16.5s earlier and collides with c4b5 (58.5–72.8), so it is unusable as a fire cue. **Fix:** c4b6 CONTENT is re-anchored to the clause being spoken at fire time — the leverage-ratio point — eyebrow `WHAT FUELED THE MOVE`, headline `LEVERAGE, NOT SPOT`, sub `the rally ran on borrowed size`, firing at **comp 76.20** on `leverage.` (table src 1106.96 − 1030.76). Non-duplicative (no repeated number, no "25×"), single-cyan accent bar kept, still breaks the kinetic run before c4b8.
   - **Ground-truth table gap closed.** `clip4-words.txt` previously ended at `cross`@1114.66 (its comp 104.66), so the c4b8 L3 closer (`wiped`/`out.`) could not be verified against the required reference table. `clip4-words.txt` is now **extended through `So`@1118.98** (covers src_out); the appended words (`margining`@1115.04 … `wiped`@1117.92 … `out.`@1118.26) were pulled from the master `audio.json` and confirm the EDL fire-times exactly (see Verification Gate).

**Kept from v2 (works):** dialog-matched cold open at the re-picked in-point `1030.76` ("your delta completely shifts"); `object-position:83% center`; cascade-as-centerpiece; the re-derived word table; the master-timeline Ken-Burns + glow/zone-rule choreography.

---

## R1 — VIEW-TIMELINE (the flip-flop proof)

Source is a SIDE-BY-SIDE (Nic/host left, Jasper/guest right). Two views: **full-frame** (both speakers, dark gradient backdrop left for text) and **Mode-A** (guest framed right 40%, graphic in left 60%). Consecutive graphic beats are grouped into the SAME view so the frame never bounces.

| # | View | Comp range | Dwell | Beats in this view | R1 check |
|---|------|-----------|-------|--------------------|----------|
| V0 | **full-frame** (intro) | 0.0 → 3.5 | 3.5s | c4b1 cold-open kinetic | intro (0–6s) exempt; never loops back |
| V1 | **Mode-A** | 3.5 → 33.6 | **30.1s** | c4b2 cascade flowchart | ≥8 ✓ |
| V2 | **full-frame** | 33.6 → 46.0 | **12.4s** | c4b3 HECTIC slam, then live video ("shorter than people think / real compression") | ≥8 ✓ |
| V3 | **Mode-A** | 46.0 → 58.3 | **12.3s** | live video, then c4b4 "30–45 MIN" card | ≥8 ✓ |
| V4 | **full-frame** | 58.3 → 88.2 | **29.9s** | c4b5 25× slam → live video → c4b6 "leverage, not spot" card (full-frame backdrop) → c4b8 closer kinetic | ≥8 ✓ |

**A-B-A audit (no return to a view within ~12s):**
- Mode-A appears at V1 (3.5–33.6) and V3 (46.0–58.3). Between them: V2 full-frame is **12.4s** ≥12 ✓ (not A-B-A).
- full-frame appears at V2 (33.6–46.0) and V4 (58.3–88.2). Between them: V3 Mode-A is **12.3s** ≥12 ✓ (not A-B-A).
- V0 intro full-frame (0–3.5) → V1 Mode-A: the intro never loops back to a prior view ✓.
- **No segment <8s outside the 0–6s intro. No A-B-A within 12s. PASS.**

**One-liner:** intro-full(3.5s) → ModeA cascade(30.1s) → full HECTIC+breath(12.4s) → ModeA 30-45min card(12.3s) → full 25×-slam→leverage-card→closer(29.9s). 5 views, all sustained ≥12.3s, zero A-B-A.

---

## R2 — Template variety (don't make another clip-2)

`kinetic(open) → flowchart(cascade) → caption-kinetic-slam → liquid-glass card → caption-kinetic-slam → liquid-glass card → kinetic(closer)`

- **Distinct PRIMARY device = `flowchart` ADL cascade as the cold open** (per DESIGN per-clip map). The cascade is the centerpiece and the clip is NOT kinetic-dominated.
- **3-kinetic opening run BROKEN:** open is `kinetic → flowchart`, not three kinetics. The single cold-open kinetic (c4b1) is the mandatory dialog-match (R3/§3); the flowchart immediately leads.
- **≤2 kinetic word-stacks in a row:** the only adjacency is c4b8 (closer) preceded by a liquid-glass card (c4b6) — never 3 kinetics. `caption-kinetic-slam` beats (c4b3, c4b5) are each separated by non-kinetic beats (flowchart, card).
- **Catalog blocks to INSTALL (`npx hyperframes add <name>`):**
  - `caption-kinetic-slam` (component) — used by **c4b3** (HECTIC) and **c4b5** (25×). *Already required by the task for the 25× reveal.*
  - `flowchart` (block) — used by **c4b2** (ADL cascade). *Note:* the v2 build hand-built the cascade as a custom decision-tree; for v3 install `flowchart` and restyle to DESIGN palette (dark nodes, cyan final node) rather than re-hand-building (anti-pattern per `_QA-CHECKLIST.md §2`).
  - `data-chart` (block) — **considered for the 25× and the duration**, rejected: the 25× is a single hero number (slam reads stronger than a bar) and the duration is a single value (card reads cleaner). Documented per the "did I consider a catalog block?" checklist item.
- **HAND-BUILD (DESIGN "Cards & Panels" recipe, no catalog block needed):** c4b1 kinetic open, c4b4 liquid-glass card, c4b6 liquid-glass card, c4b8 kinetic closer.

---

## R3 — Jargon (every on-screen string mapped through `_JARGON.md`)

Whisper writes **"burp"** for **perps/perp**; **"deep in"** for **DePIN**; etc. Per `_JARGON.md`, the audio.json transcript is for TIMING only — never spelling. Every on-screen string in this clip, audited:

| Beat | On-screen string | Contains a mapped term? | Verdict |
|------|------------------|--------------------------|---------|
| c4b1 | `YOUR DELTA` / `COMPLETELY SHIFTS` | no jargon | ✓ |
| c4b2 | `ADL CASCADE · LAST OCTOBER` / `DELTA-NEUTRAL BOOK` / `PERP CLOSED OUT` / `NAKED LONG DELTA` / `FORCED SELLING → FEEDBACK LOOP` / `ALTS −60 / −70 / −80%` | **PERP** (Whisper "burp"@1044.68) → rendered **PERP** ✓; `ADL` = auto-deleveraging (correct casing) | ✓ |
| c4b3 | `EXTREMELY` / `HECTIC` | no jargon | ✓ |
| c4b4 | `HOW LONG IT LASTED` / `30–45 MINUTES` / `of real stress — then everything picked back up` | no jargon | ✓ |
| c4b5 | `25×` / `TIMES MORE` / `DERIVATIVES` / `THAN SPOT` / `$226K MELT-UP` | no jargon ("derivatives", "spot" are correct finance terms) | ✓ |
| c4b6 | `WHAT FUELED THE MOVE` / `LEVERAGE, NOT SPOT` / `the rally ran on borrowed size` | no jargon ("leverage", "spot" are correct finance terms) | ✓ |
| c4b8 | `NEW TO PERPS` / `CROSS-MARGINING ON` / `WIPED OUT` | **PERPS** (Whisper "burp"@1113.08) → rendered **PERPS** ✓ | ✓ |

**All four spoken "burp" occurrences (src 1038.90, 1044.68, 1089.74, 1113.08) are perps/perp.** Two surface on screen (c4b2 node "PERP", c4b8 "PERPS") and are spelled correctly; the other two are audio-only (no on-screen text). **No raw "burp", "deep in", "graft", or "stake rate" reaches the render. PASS.**
Proper nouns N/A this clip (no Wintermute/Paradex/etc. on screen). `ADL`, `DERIVATIVES`, `SPOT`, `DELTA`, `LEVERAGE` casing per `_JARGON.md` "Standard term casing."

---

## R4 — No duplicate notable word across a beat (eyebrow vs sub/title)

| Beat | Elements | Duplicate notable word? |
|------|----------|--------------------------|
| c4b1 | `YOUR DELTA` / `COMPLETELY SHIFTS` | none |
| c4b2 | eyebrow `ADL CASCADE · LAST OCTOBER`; nodes `DELTA-NEUTRAL BOOK` / `PERP CLOSED OUT` / `NAKED LONG DELTA` / `FORCED SELLING → FEEDBACK LOOP` / `ALTS −60/−70/−80%` | "DELTA" appears in node1 and node3 — but they are sequential **cascade nodes** (distinct steps of one chain), NOT an eyebrow-vs-sublabel echo. The R4 target (same word in eyebrow AND title of one card) does not occur. ✓ |
| c4b3 | `EXTREMELY` / `HECTIC` | none |
| c4b4 | eyebrow `HOW LONG IT LASTED` / headline `30–45 MINUTES` / sub `of real stress — then everything picked back up` | none |
| c4b5 | slam words `25×` `TIMES` `MORE` `DERIVATIVES` `THAN` `SPOT` then payoff `$226K MELT-UP` | none (v2's `DERIVATIVES`/`SPOT` eyebrow dup is removed — slam has no eyebrow) |
| c4b6 | eyebrow `WHAT FUELED THE MOVE` / headline `LEVERAGE, NOT SPOT` / sub `the rally ran on borrowed size` | none (eyebrow, headline, and sub share no notable word; "SPOT" appears only in the headline) |
| c4b8 | `NEW TO PERPS` / `CROSS-MARGINING ON` / `WIPED OUT` | none |

Cross-beat echoes deliberately avoided: c4b6 sub uses "borrowed size" (not "wiped") so it does not pre-echo c4b8 "WIPED OUT"; c4b6 "SPOT" recurs from c4b5's "THAN SPOT" only as a single shared finance term across two distinct beats (not an in-beat eyebrow/title dup), and the framing differs ("THAN SPOT" = ratio numerator vs "LEVERAGE, NOT SPOT" = what fueled it). **PASS.**

---

## §3 — Dialog-match + open-on-line

- **In-point `src_in = 1030.76`** = the word **"your"** in *"your delta completely shifts in your structure."* The "…in the money. But as a result," filler head (src 1029.02–1030.22) is **trimmed**. First audible words at comp 0.0 are the concrete crash-mechanic line — no anticipatory pull.
- **First text by comp 0.08** (c4b1 L1) — well under the 1.5s cold-open cap.
- Every kinetic / node-reveal fires at `comp_t = word.src_t − 1030.76`, read off the inlined word table (bottom of file), never computed by hand. Genuinely editorial labels are marked `EDITORIAL`. **Every CONTENT beat names the line it lands on, and that line is the one actually spoken at the fire time** (the v3.1 c4b6 re-anchor enforces this).

## R5 — Opening coherence

c4b1 reads **"YOUR DELTA / COMPLETELY SHIFTS"** — a complete thought; cyan payoff `COMPLETELY SHIFTS` is a real verb phrase, not a dangling number. **PASS.**

---

## §5 — Speaker framing (Mode A) — kept & verified from v2

- `MODE_A = {left:1229, top:108, width:614, height:864}`, `borderRadius:"6px"`, `object-fit:cover`, `object-position:83% center`.
- 83% lands the tall narrow `cover` window (AR≈0.71, ~40% of source width visible) on **Jasper's face (~70–88% of source width)**, catching the right of his name-tag and **excluding the center seam + host** (50%/62% center the seam — the clip-1 mistake).
- Bottom clearance in Mode-A box = 1080−108−864 = **108px** (>40 ✓); top = **108px** (>20 ✓). Name lower-third "Jasper De Maere / Wintermute" fully visible.
- Full-frame beats (V0, V2, V4) show **both speakers** with a left dark gradient backdrop for text readability — never text on black.
- **Build-time verify-by-frame (mandatory, `_QA-CHECKLIST.md §9`):** after draft render, extract and LOOK at frames at comp 0.5 (open), 3.7 (Mode-A shrink), 16 (cascade mid), 34.8 (HECTIC full-frame), 47 (Mode-A return), 63.8 (25× slam), 76.5 (leverage card), 80.5 (closer). Re-tune `object-position` if any frame shows host bleed / dead ceiling.

---

## Master-timeline framing (mirror clip-2 `index.html`; values already in the existing index.html — adjust the switch times to v3)

The existing `clip-4-oct10-crash/index.html` already wires the master timeline. **v3 changes ONLY the view switch times** to match the V0–V4 table above (the v2 file switches at 33.8/40.0/58.3/73.6/80.2, which produce the two sub-8s islands). Update to switches **3.5 / 33.6 / 46.0 / 58.3**:

- t=0–3.5 **full-frame** (both speakers) for c4b1; shrink to **Mode A** at **t=3.5** (`expo.inOut`, 0.7s); `#bg-glow` in 3.8, `#zone-rule` draw 3.9; Ken-Burns scale 1.0→1.04 across the clip.
- **t=33.6** expand to **full-frame** for V2 (glow+rule out 33.4) — stays full-frame through the HECTIC slam AND the live "shorter/compression" stretch.
- **t=46.0** return to **Mode A** for V3 (glow in 46.1, zone-rule draw 46.2) — clean video then the c4b4 card.
- **t=58.3** expand to **full-frame** for V4 (glow+rule out 58.1) — **stays full-frame through clip end** (25× slam → live → c4b6 card on full-frame backdrop → c4b8 closer). No return to Mode A (D4 no-outro; clip ends on live full-frame video).
- Audio: separate `<audio>` `data-volume="1"`, continuous; video `muted`. `data-media-start="1030.76"` on both; `data-duration="88.2"`.

**z-index reminder (DESIGN line 58):** every overlay id `beat-c4b1, beat-c4b2, beat-c4b3, beat-c4b4, beat-c4b5, beat-c4b6, beat-c4b8` MUST be in the `z-index:3` rule of index.html (else it renders behind the video). The live index.html z-index:3 rule already lists all 7 ids ✓ — only the c4b5 and c4b6 sub-comp CONTENTS change in this rebuild, the ids stay. **Confirm `beat-c4b6` stays in the z-index:3 rule after re-authoring.**

> **BUILD STATE (required rebuilds — the live files are still v2 and do NOT implement this v3 spec):**
> - **index.html view switches** are still the v2 times `33.8 / 40.0 / 58.3 / 73.6 / 80.2` (which produce the sub-8s islands this spec fixes). → change to **`3.5 / 33.6 / 46.0 / 58.3`** per the master-timeline list above.
> - **c4b5** is still `beat-c4b5-25x-count.html` (apple-money-count). → re-author as **`beat-c4b5-25x-slam.html`** using `caption-kinetic-slam` (task-mandated device for the 25× reveal).
> - **c4b6** is still `beat-c4b6-supported-leverage.html` (swiss-grid). → re-author as **`beat-c4b6-leverage-not-spot.html`** per the c4b6 detail below (liquid-glass card, leverage clause, fire comp 76.20).
> The spec is build-ready; these three edits are the remaining build work.

---

## BEAT MAP (v3)

| Beat | Comp range | Src range | Template / block | View | Sub-comp file |
|------|-----------|-----------|------------------|------|---------------|
| c4b1 | 0.0–7.5 | 1030.76–1038.26 | kinetic-type (cold open, hand-built) | full-frame (V0)→ModeA@3.5 | `beat-c4b1-delta-open.html` |
| c4b2 | 8.0–33.4 | 1038.76–1064.16 | **`flowchart` (CENTERPIECE / primary device)** | Mode A (V1) | `beat-c4b2-adl-cascade.html` |
| c4b3 | 34.0–39.4 | 1064.76–1070.16 | **`caption-kinetic-slam`** | full-frame (V2) | `beat-c4b3-hectic-slam.html` |
| c4b4 | 51.0–58.0 | 1081.76–1088.76 | liquid-glass card (hand-built) | Mode A (V3) | `beat-c4b4-30-45-min.html` |
| c4b5 | 58.5–72.8 | 1089.26–1103.56 | **`caption-kinetic-slam` (25× reveal)** | full-frame (V4) | `beat-c4b5-25x-slam.html` |
| c4b6 | 75.0–80.0 | 1105.76–1110.76 | liquid-glass card (hand-built) on full-frame backdrop | full-frame (V4) | `beat-c4b6-leverage-not-spot.html` |
| c4b8 | 80.6–88.2 | 1111.36–1118.98 | kinetic-type (human closer, hand-built) | full-frame (V4) | `beat-c4b8-wiped-out.html` |

**Opening "3+ element types before 6s" (DESIGN):** c4b1 L1 kinetic (type 1, comp 0.08) + c4b1 cyan payoff line (type 2, comp 0.48) + Mode-A video shrink with cyan `#zone-rule` draw + `#bg-glow` (type 3, comp 3.5–3.9) + cascade eyebrow "ADL CASCADE · LAST OCTOBER" slam (type 4, comp 8.2). Speaker visible from t=0. **PASSES** — and the open is the dialog line, NOT formulaic swiss-grid chrome.

---

## BEAT DETAIL

### c4b1 — kinetic-type cold open · full-frame → Mode A · `beat-c4b1-delta-open.html`
- **Comp:** 0.0–7.5 · **Src:** 1030.76–1038.26 · `data-start 0.0` / `data-duration 7.5`
- **View:** full-frame (both speakers, dark gradient backdrop LEFT for the kinetic). Master shrinks video to **Mode A at comp 3.5**; the kinetic exits up ~comp 3.1 (cleared before the shrink).
- **Kinetic lines — phrase build, STAY (no dim), Inter 900 ~130px:**
  - **L1 `YOUR DELTA`** (`#FFFFFF`) — matches spoken **"your delta"** — `your`@src1030.76=comp 0.00, `delta`@src1030.92=comp 0.16 → **fire comp 0.08**.
  - **L2 `COMPLETELY SHIFTS`** (cyan `#00D4FF` + glow, payoff) — matches spoken **"completely … shifts"** — `completely`@src1031.24=comp 0.48, `shifts`@src1031.74=comp 0.98 → **fire comp 0.48**.
- **Cyan element:** L2 only (single cyan).
- **Exit:** whole stack drifts up `power2.in` ~comp 3.1.

### c4b2 — `flowchart` ADL cascade (CENTERPIECE / PRIMARY DEVICE) · Mode A · `beat-c4b2-adl-cascade.html`
- **Comp:** 8.0–33.4 · **Src:** 1038.76–1064.16 · `data-start 8.0` / `data-duration 25.4`
- **View:** Mode A (video right 40%, ~80% scale; glow + zone-rule already in from the 3.5 shrink).
- **Install:** `npx hyperframes add flowchart` → restyle to DESIGN palette (node fill `rgba(20,26,34,0.92)`, 1px `rgba(255,255,255,0.08)` border, `#F0F0F0` labels, connectors muted `#6B7480`, final node cyan). Strip the catalog's sticky-note/cursor cosmetics. **Do NOT re-hand-build** (anti-pattern §2).
- **Lead-device beat.** Vertical cause→effect flow, 5 nodes, building **in sync with the spoken cascade** (node reveals are WORD-CUED, not editorial):
  - Eyebrow **`ADL CASCADE · LAST OCTOBER`** — `#F0F0F0` Inter 700 32px — `EDITORIAL: structural label` — fire comp **8.2**.
  - Node 1 **`DELTA-NEUTRAL BOOK`** — recap of the starting position ("delta neutral" spoken @1034.22, inside c4b1's window) — reveal comp **8.6** `#F0F0F0` — `EDITORIAL: structural recap node`.
  - Node 2 **`PERP CLOSED OUT`** — cued to spoken **"closed out"** — `closed`@1046.64=comp **15.88**, `out`@1047.00=comp 16.24 → reveal **comp 15.9** `#F0F0F0`. *(spoken "burp"→PERP per _JARGON.md.)*
  - Node 3 **`NAKED LONG DELTA`** — cued to spoken **"naked long delta"** — `naked`@1048.46=comp **17.70**, `long`@1048.90=comp 18.14, `delta.`@1049.28=comp 18.52 → reveal **comp 17.7** `#F0F0F0`.
  - Node 4 **`FORCED SELLING → FEEDBACK LOOP`** — cued to spoken **"feedback loop"** — `feedback`@1055.50=comp **24.74**, `loop`@1055.92=comp 25.16 → reveal **comp 24.7** `#F0F0F0`.
  - Node 5 **`ALTS −60 / −70 / −80%`** (cyan final node) — cued to spoken **"60, 70, 80%"** — `60,`@1062.66=comp **31.90**, `70,`@1063.16=comp 32.40, `80%.`@1063.54=comp 32.78 → the three numbers tick into the node **comp 31.90 → 32.40 → 32.78**; node finalizes cyan `#00D4FF`.
- **Cyan element:** Node 5 only (final-node convention). Connectors muted `#6B7480` (structural, not an accent).
- **Anti-static:** nodes pop on their spoken cues across 8→33s, cyan connectors draw `scaleY 0→1` between reveals, the −60/−70/−80% numbers count into node 5. Continuously building, never frozen. Exit ~comp 33.0 (clears before the V2 full-frame expand at 33.6).

### c4b3 — `caption-kinetic-slam` · full-frame · `beat-c4b3-hectic-slam.html`
- **Comp:** 34.0–39.4 · **Src:** 1064.76–1070.16 · `data-start 34.0` / `data-duration 5.4`
- **View:** full-frame (V2 — both speakers, dark gradient backdrop). Master expanded to full-frame at 33.6; **stays full-frame after this beat through comp 46.0** (live "shorter than people think / real compression" video — same view, no switch).
- **Install:** `npx hyperframes add caption-kinetic-slam` → restyle to white/cyan, Inter 900. Single-word full-screen slams, alternating entrance directions (distinct motion signature from c4b1's y-rise).
- **Slam words — WORD-SYNCED:**
  - **`EXTREMELY`** (`#FFFFFF`) — spoken `extremely`@1065.28=comp **34.52** → slam **comp 34.52** (enters from left).
  - **`HECTIC`** (cyan `#00D4FF`) — spoken `hectic,`@1065.74=comp **34.98** → slam **comp 34.98** (enters from right).
- **Cyan element:** `HECTIC` only.
- **Exit:** scale-down + fade `power2.in` ~comp 39.0. Video stays full-frame; live audio carries the "shorter/compression" lines through comp 46.0.

### c4b4 — liquid-glass card · Mode A · `beat-c4b4-30-45-min.html`
- **Comp:** 51.0–58.0 · **Src:** 1081.76–1088.76 · `data-start 51.0` / `data-duration 7.0`
- **View:** Mode A (V3). Master returned to Mode A at comp 46.0; ~5s of clean Jasper video precedes the card.
- **Card (DESIGN "Cards & Panels"):** `rgba(20,26,34,0.92)` fill, **4px cyan `#00D4FF` inset accent bar** (left), soft outer glow (`0 0 40px rgba(0,212,255,0.10), 0 8px 40px rgba(0,0,0,0.65)`), 1px `rgba(255,255,255,0.08)` border, `mask-image:linear-gradient(to right,black 82%,transparent 100%)` feather. **NO `backdrop-filter` blur, NO grain.** Title+desc vertically centered (`min-height:96px`).
- **Content (exact text + hex):**
  - Eyebrow **`HOW LONG IT LASTED`** — `#F0F0F0` Inter 700 32px — `EDITORIAL: structural label`.
  - Headline **`30–45 MINUTES`** — `#FFFFFF` Inter 900 96px (the duration is the point).
  - Sub **`of real stress — then everything picked back up`** — `#C4C9D0` Inter 600 28px.
- **Entry — WORD-CUED:** card slides in from right at **comp 51.5** to land on spoken **"half an hour to 45 minutes"** — `half`@1082.34=comp 51.58, `45`@1083.00=comp 52.24, `minutes`@1083.40=comp 52.64. (Verified spoken: *"It was really, I think, half an hour to 45 minutes before everything picked up back up."* — "half an hour" = 30 min, so `30–45 MINUTES` is faithful.) Holds, exits ~comp 57.6.
- **Cyan element:** the 4px accent bar only.

### c4b5 — `caption-kinetic-slam` (25× REVEAL — task-required device) · full-frame · `beat-c4b5-25x-slam.html`
- **Comp:** 58.5–72.8 · **Src:** 1089.26–1103.56 · `data-start 58.5` / `data-duration 14.3`
- **View:** full-frame (V4 — both speakers, dark gradient backdrop). Master expanded to full-frame at 58.3; **stays full-frame through clip end.**
- **Install:** `npx hyperframes add caption-kinetic-slam` (same component as c4b3, re-instanced) → white slams, single cyan payoff, Inter 900, hero scale for the number. This is the **only** 25× appearance in the clip (v1 had it 3×; v2 had it 2×).
- **Slam sequence — WORD-SYNCED (single words / short phrases, alternating entrance):**
  - **`25×`** — hero number, Inter 900 ~200px `#FFFFFF` — lands on spoken **"20 or 25x"** — `25x.`@1094.52=comp **63.76** → slam **comp 63.76** (scale-pop entrance, `back.out`).
  - **`TIMES MORE`** (`#FFFFFF`) — spoken **"25 times more"** — `times`@1096.44=comp **65.68**, `more`@1097.32=comp 66.56 → slam **comp 65.68** (enters from left).
  - **`DERIVATIVES`** (`#FFFFFF`) — spoken `derivatives`@1097.64=comp **66.88** → slam **comp 66.88** (enters from right).
  - **`THAN SPOT`** (`#FFFFFF`) — spoken **"than spots"** — `than`@1098.38=comp **67.62**, `spots,`@1098.60=comp 67.84 → slam **comp 67.62** (enters from bottom).
  - **`$226K MELT-UP`** (cyan `#00D4FF` + glow, payoff) — spoken **"the melt up … 226k"** — `melt`@1100.68=comp **69.92**, `226k`@1102.58=comp 71.82 → slam cyan **comp 69.92**, `$226K` emphasized on **comp 71.82**.
- **Cyan element:** `$226K MELT-UP` payoff only (the `25×` hero stays white — D7 "stat OR accent, not both"; the cyan is the payoff line).
- **Anti-static:** five alternating-direction slams across 63.8→71.8 with the hero `25×` scale-pop and the cyan payoff — full kinetic motion. Exits ~comp 72.4.
- **Date (D7 / §8):** the Oct-10 crash + $226K melt-up are last year's event — but §8 is a HARD RULE: never render the literal year "2025"/"2024" on screen. The c4b2 eyebrow uses the relative-time form `LAST OCTOBER` (relabeled to LAST OCTOBER; today is 2026-06-02, so Oct 2025 = last October). No literal year reaches any frame.

### c4b6 — liquid-glass card (NEW — leverage-fueled rally; replaces v2's duplicate 25× swiss-grid) · full-frame backdrop · `beat-c4b6-leverage-not-spot.html`
- **Comp:** 75.0–80.0 · **Src:** 1105.76–1110.76 · `data-start 75.0` / `data-duration 5.0`
- **View:** full-frame (V4 — both speakers; card sits in the LEFT zone over a dark gradient backdrop so the host side is darkened for readability while both speakers stay visible — same backdrop treatment as the full-frame kinetic beats). **Breaks the kinetic run** between the c4b5 slam and the c4b8 closer (slam → card → kinetic = no 3-kinetic adjacency).
- **Why this content (v3.1 re-anchor):** the on-screen claim MUST match the line spoken at its fire time (`_QA-CHECKLIST.md §3`, "text appears as the person says it"). At the c4b6 fire window the speaker is saying *"the melt-up… was **very heavily supported by leverage**"* (`supported`@1106.24=comp 75.48, `leverage.`@1106.96=comp 76.20). The earlier "perp-side liquidation" idea (`liquidation`@1088.72=comp 57.96, `perp side`@1089.74=comp 58.98) is spoken ~16.5s before this window and **collides with c4b5 (58.5–72.8)** — so it cannot be the fire cue here. v3 therefore surfaces the **leverage-ratio point that matches the audio**: the rally was driven by borrowed size, not spot demand. This is the narrative bridge to the human closer, repeats **no number** (no "25×"), and re-introduces **no swiss-grid chrome**.
- **Card (same recipe as c4b4):** `rgba(20,26,34,0.92)` fill, 4px cyan inset bar, glow, 1px border, mask feather. No blur, no grain.
- **Content (exact text + hex):**
  - Eyebrow **`WHAT FUELED THE MOVE`** — `#F0F0F0` Inter 700 32px — `EDITORIAL: structural label`.
  - Headline **`LEVERAGE, NOT SPOT`** — `#FFFFFF` Inter 900 72px. *(matches the spoken "very heavily supported by leverage" — the rally ran on derivatives leverage, not spot buying.)*
  - Sub **`the rally ran on borrowed size`** — `#C4C9D0` Inter 600 28px.
- **Entry — WORD-CUED:** card slides in from right and lands on the operative word **`leverage.`@1106.96=comp 76.20** (the on-screen claim "leverage, not spot" is confirmed the instant he says "leverage"). Card head can begin its slide ~comp 75.4 so the headline is settled by comp 76.20. Holds, exits ~comp 79.6.
- **Cyan element:** the 4px accent bar only.

### c4b8 — kinetic-type human closer · full-frame · `beat-c4b8-wiped-out.html`
- **Comp:** 80.6–88.2 · **Src:** 1111.36–1118.98 · `data-start 80.6` / `data-duration 7.6`
- **View:** full-frame (V4 — both speakers, dark gradient backdrop). Video stays full-frame through clip end — no card, no end screen (D4 no-outro).
- **Kinetic lines — phrase build, STAY (no dim), the human cost:**
  - **L1 `NEW TO PERPS`** (`#FFFFFF`) — spoken **"new to perp"** — `new`@1112.58=comp **81.82**, `to`@1112.86=comp 82.10, `burp`(perp)@1113.08=comp 82.32 → slam **comp 81.82**. *(Whisper "burp"→on-screen "PERPS" per _JARGON.md.)*
  - **L2 `CROSS-MARGINING ON`** (`#FFFFFF`) — spoken **"cross margining enabled"** — `cross`@1114.66=comp **83.90**, `margining`@1115.04=comp 84.28, `enabled`@1115.56=comp 84.80 → slam **comp 83.90**.
  - **L3 `WIPED OUT`** (cyan `#00D4FF` + glow, payoff) — spoken **"absolutely … wiped out"** — `wiped`@1117.92=comp **87.16**, `out.`@1118.26=comp 87.50 → slam cyan **comp 87.16**.
- **Cyan element:** L3 only.
- **Clip end:** L3 lands ~87.5, holds ~0.5s, clip ends at comp 88.2 on **live full-frame video** (no outro, D4). The ending is the human consequence — a different beat-type than the 25× stat, fixing v1's stat-callback repetition.

---

## VERIFICATION GATE (this clip, graded against `_QA-CHECKLIST.md`)

- **§1 R1 view discipline:** 5 views, every non-intro view ≥12.3s; no segment <8s outside the 0–6s intro; no A-B-A within 12s (V2 full=12.4s and V3 ModeA=12.3s are the separators — proof table above). **PASS.**
- **§2 R2 variety:** primary device = `flowchart` cascade cold open; ≤2 kinetics in a row (never 3); `caption-kinetic-slam` used for the 25× per task; catalog blocks named (`caption-kinetic-slam`, `flowchart`) to install vs hand-build (cards/kinetics). Open is kinetic→flowchart, NOT a swiss-grid. **PASS.**
- **§3 dialog-match + text-appears-as-spoken:** opens on the spoken line at re-picked in-point 1030.76; first text comp 0.08; all fire-times read off the table; **every CONTENT beat's on-screen claim is the line spoken at its fire time** (c4b6 re-anchored from the misaligned `supported`@75.48 framing to the leverage clause at `leverage.`@comp 76.20 — the words actually being spoken). **PASS.**
- **§4 R5 coherence:** "YOUR DELTA / COMPLETELY SHIFTS" is a complete thought; cyan payoff is a real phrase. **PASS.**
- **§5 framing:** `object-position:83% center`, Mode-A clearances 108px/108px, full-frame beats show both speakers; verify-by-frame list provided. **PASS** (re-verify at build).
- **§6 R3 jargon:** every on-screen string audited vs `_JARGON.md`; all four "burp"→perps handled (PERP/PERPS on screen; no raw burp); ADL/derivatives/spot/leverage casing correct. **PASS.**
- **§7 R4 duplicates:** no eyebrow-vs-title duplicate in any beat; v2's `DERIVATIVES`/`SPOT` dup removed; c4b6 eyebrow/headline/sub share no word; cross-beat "wiped" pre-echo avoided. **PASS.**
- **§8 hard rules:** all 7 ids in z-index:3; ONE cyan element per beat (listed each beat); no backdrop blur / no grain (card recipe = solid fill + accent bar + glow); eyebrows Inter 700 ≥32px `#F0F0F0`, body ≥600; no intro/outro (ends on live video); **dates use relative-time form — c4b2 eyebrow is `LAST OCTOBER`, NO literal "2025"/"2024" on screen (§8 hard rule)**; phrase kinetics build & STAY (no dim). **PASS.**
- **Beat count = 7.** Clip is 88.2s (<90s), so the 8-beat floor (§ "clips over 90s") does not apply; the redundant 25× swiss-grid was cut deliberately to satisfy R2/R4 rather than padded back.
- **Ground-truth table coverage:** `clip4-words.txt` now spans the full clip through `So`@1118.98 (covers src_out). Every fire-time in this EDL maps to a word in that table — including the c4b8 closer tail (`margining`/`enabled`/`wiped`/`out.`), previously unverifiable. Cross-offset check (words.txt offset 1010 vs EDL offset 1030.76, constant Δ = 20.76):
  - `cross`@1114.66 → words.txt comp 104.66 → EDL 83.90 ✓
  - `margining`@1115.04 → words.txt 105.04 → EDL 84.28 ✓
  - `enabled`@1115.56 → words.txt 105.56 → EDL 84.80 ✓
  - `wiped`@1117.92 → words.txt 107.92 → EDL 87.16 ✓
  - `out.`@1118.26 → words.txt 108.26 → EDL 87.50 ✓
  - c4b6 cue `leverage.`@1106.96 → words.txt 96.96 → EDL 76.20 ✓ (already present in the table; the re-anchored fire cue is verifiable).
- **§9 verify-by-frame:** mandatory at build, frame list above (open / each transition / each beat incl. the leverage card @76.5); do not report done from self-report.

---

## Inlined word table (src_in = 1030.76; `comp = src − 1030.76`) — fire-times read off THIS table AND mirrored in `clip4-words.txt`

```
comp_t   src_t    word
  0.00  1030.76  your        <- c4b1 L1
  0.16  1030.92  delta       <- c4b1 L1
  0.48  1031.24  completely  <- c4b1 L2 (cyan)
  0.98  1031.74  shifts      <- c4b1 L2 (cyan)
  1.46  1032.22  in
  1.62  1032.38  your
  1.74  1032.50  structure
  3.46  1034.22  neutral,    <- c4b2 node1 recap "delta neutral"
  5.44  1036.20  long
  6.80  1037.56  spot,
  8.14  1038.90  burp(perp). <- spoken perp #1 (audio-only, not on screen)
 13.92  1044.68  burp(perp)  <- spoken perp #2 (audio-only; cascade node2 "PERP" uses correct spelling)
 15.88  1046.64  closed       <- c4b2 node2 cue "closed out"
 16.24  1047.00  out          <- c4b2 node2 cue
 17.70  1048.46  naked        <- c4b2 node3 cue "naked long delta"
 18.14  1048.90  long         <- c4b2 node3 cue
 18.52  1049.28  delta.       <- c4b2 node3 cue
 24.74  1055.50  feedback     <- c4b2 node4 cue "feedback loop"
 25.16  1055.92  loop         <- c4b2 node4 cue
 31.90  1062.66  60,          <- c4b2 node5 cue (cyan)
 32.40  1063.16  70,          <- c4b2 node5 cue (cyan)
 32.78  1063.54  80%.         <- c4b2 node5 cue (cyan)
 34.52  1065.28  extremely    <- c4b3 "EXTREMELY"
 34.98  1065.74  hectic,      <- c4b3 "HECTIC" (cyan)
 37.26  1068.02  shorter      (live video, V2 — no overlay)
 43.46  1074.22  compression  (live video, V2 — no overlay)
 51.58  1082.34  half         <- c4b4 card entry cue "half an hour to 45 min"
 52.24  1083.00  45           <- c4b4 cue
 52.64  1083.40  minutes      <- c4b4 cue
 57.96  1088.72  liquidation  <- spoken "the liquidation on the perp side" (the perp-side idea — spoken HERE, inside c4b5's window; NOT used as a fire cue, see c4b6 note)
 58.98  1089.74  burp(perp)   <- spoken perp #3 "the burp side" (audio-only; collides with c4b5, not on screen)
 59.24  1090.00  side,        <- spoken "perp side"
 60.88  1091.64  leverage     (first "leverage" mention; context for c4b5/c4b6)
 63.24  1094.00  20
 63.60  1094.36  or
 63.76  1094.52  25x.         <- c4b5 "25×" hero lands
 65.14  1095.90  25           (the spoken "25" of "25 times more")
 65.68  1096.44  times        <- c4b5 "TIMES MORE"
 66.56  1097.32  more         <- c4b5 "TIMES MORE"
 66.88  1097.64  derivatives  <- c4b5 "DERIVATIVES"
 67.62  1098.38  than         <- c4b5 "THAN SPOT"
 67.84  1098.60  spots,       <- c4b5 "THAN SPOT"
 69.92  1100.68  melt         <- c4b5 "$226K MELT-UP" (cyan)
 70.24  1101.00  up           <- c4b5 (cyan)
 71.82  1102.58  226k         <- c4b5 "$226K" (cyan)
 74.18  1104.94  heavily      (spoken "very heavily supported by leverage")
 75.48  1106.24  supported    (spoken; the c4b6 claim's verb — but the fire cue is the noun "leverage" below)
 76.20  1106.96  leverage.    <- c4b6 card cue (headline "LEVERAGE, NOT SPOT" lands as he says "leverage")
 81.82  1112.58  new          <- c4b8 L1 "NEW TO PERPS"
 82.10  1112.86  to           <- c4b8 L1
 82.32  1113.08  burp(perp)   <- c4b8 L1 (on-screen "PERPS"); spoken perp #4
 83.90  1114.66  cross        <- c4b8 L2 "CROSS-MARGINING ON"
 84.28  1115.04  margining    <- c4b8 L2
 84.80  1115.56  enabled      <- c4b8 L2
 87.16  1117.92  wiped        <- c4b8 L3 "WIPED OUT" (cyan)
 87.50  1118.26  out.         <- c4b8 L3 (cyan)
 88.22  1118.98  So           <- clip end (src_out 1118.98)
```

*(Whisper transcribes perp/perps as "burp" throughout this window — all four occurrences (src 1038.90, 1044.68, 1089.74, 1113.08) are perp/perps. On-screen text uses the correct trading term per `_JARGON.md`; the perp-side-liquidation occurrence (#3, src 1089.74) is audio-only and falls inside c4b5's window, so it carries no on-screen text. Per-word fire-cue timings above are now mirrored end-to-end in `clip4-words.txt` (extended through `So`@1118.98); intermediate non-cue words are in `clip4-words.txt` / `clip4-edl-v2.md`'s fuller table.)*
