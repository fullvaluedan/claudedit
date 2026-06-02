# Clip 1 — OTC Model / Agency-vs-Principal — EDL **v4** (BUILD-READY)

**clip_id:** `clip_1` · **dir:** `clip-1-otc-model` · **slug:** `clip-1-otc-model`
**Supersedes** `clip1-edl-v3.md`. **This v4 also REVISES the prior v4 draft** to resolve the seven gate-fail items Agent 3 returned (the draft's word-sync + continuous-graphic math were correct, but six build directives were unexecuted and there were unresolved SPEC defects — c1b7 multiple-cyan, c1b6c colliding device defaults, the DESIGN.md opening conflict, and the untethered name card). All seven are now fixed in the spec below.

> ### ⬆️ THIS REVISION (v4 → v4-rev2 — Agent 2 editorial review folded in)
> Agent 2 confirmed the SPEC is gate-clean (R1–R7, cyan, word-sync, framing all PASS as written, with full proof tables) but the as-built is still the rejected v3 (6 index counters, c1b6c missing, v3 timings/gaps, title says v3) AND the SPEC, while compliant, was a "compliant" edit rather than a "compelling" one. This revision keeps every passing element and adds the editorial-energy fixes:
> - **Hook (#3):** c1b1 now re-adds ONE fast lead line on Jasper's real word **"half"@comp 0.62** so the first kinetic word lands at 0.62s (was 2.58s — a 2.4s soft open). Still 100% chronological/word-synced; no anticipatory hook.
> - **Close (#4):** c1b9 cyan payoff changes `…POSITIONS` → **`SMOOTHLY`** (Jasper's real final word "smoothly"@src 351.78, **VERIFIED present in audio.json**). Requires **src_out 350.40 → 352.30** (+1.9s) to capture it → **duration 113.20s**.
> - **c1b4 17s window (#5):** PROMOTED from optional to spec — **trim the in-point later** (start the clean window on "So for someone…"@comp 21.20, dropping Nic's "Yeah, I cannot disagree with that, obviously" lead-in 16.76–20.04) → clean window drops 17.0s → ~11.2s. (Implemented as a c1b3-tail extension + later c1b4 logical start; in/out of the CLIP is unchanged — this is an internal pacing trim, see c1b4.)
> - **c1b7 7.4s internal lull (#6):** the 88.92→96.30 stretch had no new element. v4-rev2 **staggers the AGENCY rows to breathe** (83.1/84.0/85.0 instead of a 0.8s burst) AND **adds a mid-beat neutral "confirm" tick** stamping onto each PRINCIPAL row, plus a tick on P2 at **"gradually"@92.36**, so the centerpiece never stalls >~3s.
> - **Mode-A 79s monotony (#7):** Ken Burns gets a **second gentle inflection** (1.0→1.03 by comp ~70, easing back toward 1.015 by clip end) so the long hold isn't one monotonic creep. No rule impact.
> - **c1b6c content (#8):** the `LONG TAIL` pill renders **visually distinct** (dashed/ghost border) so the row says "majors AND the entire long tail," not four equal chips.
> - **c1b6 sublabel (#9):** `OTC Trader & Market Strategist` → **`Runs Wintermute's OTC desk`** — ties the card to the c1b5 `OTC DESK` branch + the one spoken firm name. (Still editorial; no name/title is ever spoken.)
> - **Mode-A entry seam (#10):** fire the root `THE FIRM` node with more motion at comp 33.2 to remove the only low-energy seam (32.4→36.66) right after the switch.
> **Priority for the build/QA agents: clear the two GATE items first (delete the 6 indices; author c1b6c + re-time + re-label index.html as v4), THEN apply #3/#5/#6 (highest retention impact), then #4/#7/#8/#9/#10.**

**v3 was REJECTED for two top-priority defects ("Everything has an issue"):**
1. **R6 — internal index counter on screen.** EVERY graphic beat renders a bare clip-number (`01` c1b1, `02` c1b5, `03` c1b6, `05` c1b6b, `06` c1b7, `07` c1b8). The bare number is an internal artifact, meaningless to a viewer — **forbidden**.
2. **R7 — blank-left Mode-A.** v3's Mode-A block (30.2–111.3) had **FIVE graphic-less gaps** where Jasper was cropped to the right 40% with an empty left half: 30.2–33.0 (2.8s), 48.5–50.0 (1.5s), **60.0–69.5 (9.5s — the clip-8 0:33–0:52 bug)**, 76.0–80.5 (4.5s), 99.0–100.0 (1.0s).

> ## ⚠️ BUILD STATE — EXECUTION REQUIRED (gate must NOT pass until ALL of this is done)
> The as-built files in `clip-1-otc-model/` are the v3 build (verified by grep): they render six index counters, leave the five blank-left gaps, carry v3 timings, are MISSING `beat-c1b6c-execution-scope.html`, list only 8 ids in the `z-index:3` rule, and `index.html` still self-describes as **v3** (title + comment). **The build agent MUST execute ALL of the following — the gate explicitly re-checks each with the grep/frame commands named:**
>
> - **(R6-a) DELETE every on-screen index — six files, exact locations (verified):**
>   - `beat-c1b1-half-decade.html:16` — `<div id="b1-idx" class="b1-idx">01</div>`
>   - `beat-c1b5-two-sides.html:24` — `<div id="b5-idx">02</div>`
>   - `beat-c1b6-jasper.html:23` — `<div id="b6-idx">03</div>`
>   - `beat-c1b6b-edge.html:26` — `<div id="b6b-idx">05</div>`
>   - `beat-c1b7-agency-principal.html:25` — `<div id="b7-idx">06</div>`
>   - `beat-c1b8-warehouse.html:24` — `<div id="b8-idx">07</div>`
>   For EACH: remove the `<div id="b*-idx">…</div>` element **AND** its CSS rule (`#b1-idx`/`.b1-idx`, `#b5-idx`, `#b6-idx`, `#b6b-idx`, `#b7-idx`, `#b8-idx`) **AND** its GSAP tween (`tl.fromTo("#b*-idx" …)`). Eyebrow editorial labels STAY. **GATE: `grep -rn ">0[1-8]<" clip-1-otc-model/compositions/` MUST return zero matches** (Agent 3 confirmed it currently returns 6). (c1b3 and c1b9 already have no index — confirm none is re-added.)
> - **(R7-a) Make the Mode-A block continuous-graphic (no blank-left).** Re-time every Mode-A beat to the v4 BEAT MAP so each beat's left-zone graphic stays mounted until the next beat's graphic has entered (the divs **overlap by 0.3s** — see CONTINUOUS-GRAPHIC RULE). The left zone is occupied for the ENTIRE Mode-A block (comp 32.4 → 111.3) with **zero** graphic-less instants.
> - **(R7-b) Move the single view switch to comp 32.4** (was 30.2). It now fires exactly as c1b5's eyebrow enters, so the switch never reveals an empty left zone. Delete every other `toFull`/`toModeA`; the ONLY view call is `toModeA(32.4)`. Ken Burns `vid scale 1.0→1.03` runs comp 32.4→111.3 (duration 78.9s, NOT v3's 81.1).
> - **(R7-c) ADD `beat-c1b6c-execution-scope.html`** (does NOT yet exist — Agent 3 confirmed only c1b6-jasper and c1b6b-edge are present). NEW left-zone graphic filling the 10.8s structural hole comp 58.7–69.5, over the "BTC / ETH / SOL / long tail … we help with the execution" stretch, with chips word-synced to the real asset names. Build it as the committed **horizontal ASSET-PILL ROW** device (see c1b6c spec — defect #5 fix). Add its `<div id="beat-c1b6c-execution-scope" …>` to the body AND its id to the `z-index:3` rule.
> - **(R7-d) Re-time the existing Mode-A beat divs** to: `c1b5 32.4/dur 17.8`, `c1b6 49.9/dur 9.1`, **`c1b6c 58.7/dur 11.1` (NEW)**, `c1b6b 69.5/dur 11.3`, `c1b7 80.5/dur 19.3`, `c1b8 99.5/dur 7.5`, **`c1b9 106.7/dur 6.5` (v4-rev2: extended for `SMOOTHLY`, #9)**. Each Mode-A `data-duration` = (next beat start − this start) **+ 0.3s overlap** (except c1b9, which holds to clip end). Defer each beat's internal exit-fade so it cross-fades with the next beat (CONTINUOUS-GRAPHIC RULE). **Also (v4-rev2): c1b3 `dur 11.4`** (full-frame, lingers over the dropped c1b4 lead-in, #10) and master/video/audio **`data-duration 113.2`** (clip extended +1.9s, #9).
> - **(R6/cyan-b) c1b7 ONE-CYAN FIX (SPEC DEFECT #4 — the as-built renders 4–5 simultaneous cyans).** In `beat-c1b7-agency-principal.html`: (i) the THREE PRINCIPAL-row accent dots (`<span class="b7-dot b7-dot-accent">` at lines 60/64/68) are each a `#00d4ff` fill simultaneous with the cyan header — **remove the `b7-dot-accent` class from all three** so they render the neutral `#555` `b7-dot` (the AGENCY rows already use neutral dots; match them). (ii) The v4 align-sweep MUST be **NEUTRAL (`#F0F0F0` / white underline), NOT cyan** (see c1b7 spec). After this, the **PRINCIPAL header `.b7-title-accent` `#00d4ff` is the ONLY cyan element on screen at every static instant** (the shimmer is a transient white light-pass, already non-cyan; the align-sweep is now neutral). GATE: at comp 90.0 and comp 97.0 frames, cyan-element count = exactly 1 (the PRINCIPAL header).
> - **(R4-c) c1b7 P1 dedup.** As-built P1 is `Quotes a RISK PRICE` and P2 will be `WAREHOUSES THE RISK` → both contain "RISK" = within-beat dup (R4 FAIL). **Change P1 text to `Quotes a firm PRICE`** (line 61). Also change P2 text from `Takes the other side` (line 65) to **`WAREHOUSES THE RISK`** (true word-sync on "warehouse"@88.92; see c1b7 spec defect #7).
> - **(g) Update the `z-index:3` rule** to the v4 9-id list (see GSAP section): **add** `#beat-c1b6c-execution-scope`. (v3's 8 ids stay; this adds the new one.) Without this, even once c1b6c is added as a div it renders BEHIND the z-index:2 video and the 9.5s hole stays blank.
> - **(h) Re-label `index.html` as v4.** Change `<title>` from "…— v3" to "…— v4"; change the z-index comment from "exactly these 8 ids" to "9 ids (added c1b6c)". The file must not self-describe as the rejected v3 build.
>
> **KEPT from v3 (verified correct — do NOT change):** `object-position:85% center`; `src_in=239.10`; the dialog-matched cold open; every word-sync fire-time (ALL re-verified against the audio.json word objects this round — delta 0.00; see per-beat tables). The one-transition view model. The distinct lead device.

> **Lead device (DESIGN.md per-clip map):** **Agency-vs-Principal two-column comparison (swiss-grid)** as the centerpiece, with a **`shimmer-sweep`** (transient WHITE light-pass) across the PRINCIPAL-column reveal AND a one-shot **NEUTRAL underline-sweep connecting AGENCY↔PRINCIPAL** when `Fully ALIGNED` lands (v4 mid-centerpiece motion, non-cyan — see defect #4). This is the distinct silhouette for clip-1 — NOT a stack of kinetic word-stacks.

---

## WHAT CHANGED — v3 → v4 → this v4 revision

| # | Issue | Fix in this v4 |
|---|-------|----------------|
| 1 | **R6 — index counter on screen** (six beats; as-built grep returns 6). | **No index anywhere.** Every `b*-idx` element + CSS + tween deleted from all six sub-comps (exact line numbers above). On-screen chrome per beat = eyebrow label only (Inter 700, ≥32px, #F0F0F0). BEAT MAP "on-screen text" column has **no numerals as labels**. `grep ">0[1-8]<"` → 0. |
| 2 | **R7 — blank-left Mode-A (5 gaps; the 9.5s hole = clip-8 bug).** | **Continuous-graphic Mode-A.** Switch moved to **comp 32.4** (lands as c1b5 enters); every Mode-A beat extended **+0.3s past its boundary** (cross-fade overlap, no 1-frame hand-off flash); the 9.5s hole filled by NEW **c1b6c**. Left zone occupied 32.4→111.3 with **zero** graphic-less instants (R7 PROOF table). |
| 3 | (R1 already satisfied — kept.) | Still exactly ONE view transition; no A-B-A possible. Switch just moved 30.2→32.4; Mode-A beats re-timed gap-free + 0.3s-overlapped. FULL 0–32.4 / MODE-A 32.4–111.3, both ≫8s. |
| **4** | **SPEC DEFECT — c1b7 multiple simultaneous cyan.** As-built: PRINCIPAL header `.b7-title-accent` is permanently `#00d4ff` **AND** three PRINCIPAL-row dots `.b7-dot-accent` are `#00d4ff` **AND** the prior draft's align-sweep was cyan = up to FIVE cyan elements coexisting → violates "ONE cyan per frame." | **PRINCIPAL header is the SOLE cyan.** (a) the three PRINCIPAL-row accent dots → **neutral `#555`** (drop `b7-dot-accent`; match the AGENCY dots). (b) the align-sweep → **neutral white/`#F0F0F0`**, not cyan. (c) the shimmer is a transient WHITE light-pass (already non-cyan). At every static instant cyan-count = 1. |
| **5** | **SPEC DEFECT — c1b6c colliding device defaults.** Prior draft offered c1b6c as either a `data-chart`-family panel (→ same template as c1b6b's bars, adjacent) OR a liquid-glass scope card (→ same template as c1b6's card, adjacent on the other side). Neither option is clean; it never committed. | **c1b6c COMMITS to a horizontal ASSET-PILL ROW** — rounded chips in a flowing row, **no bars, no card chrome, no axes** — visibly distinct from BOTH c1b6 (liquid-glass card) and c1b6b (vertical-track bar chart). One offered form, stated. Not a kinetic (kinetic count stays 3). |
| **6** | **SPEC DEFECT — DESIGN.md "Opening 6 Seconds Is Mandatory" conflict left unacknowledged.** The c1b1 open is full-frame (both speakers) until the 32.4 switch, 2 element types, first kinetic word @ 2.58 — which contradicts DESIGN.md's "speaker-right-from-t=0 / 3-elements-in-6s / first-kinetic-word @ 0.08s." | **Explicit reconciliation note added** (see "OPENING-MODEL RECONCILIATION"): the R1/R7 + QA-CHECKLIST §3 full-frame-kinetic-open model **supersedes** DESIGN.md's "Opening 6 Seconds" sub-rules for this side-by-side project. A reviewer must not read it as an un-acknowledged FAIL. |
| **7** | **SPEC DEFECT — c1b6 name card untethered from any name mention.** The ONLY name spoken in the whole clip is **"Wintermute"@comp 26.78** (inside the c1b4 full-frame breath); "Jasper"/"De Maere"/"Trader"/"Strategist" are **never** spoken (audio.json checked, src 239–350). An ID card untethered from a name mention edges toward the banned intro card. | **Documented + content-tethered.** The card fires at comp 49.9 (NOT clip open) over a live speaker actively describing his own role ("we help people execute specific transactions") — a mid-clip speaker-ID, not a "meet the guest" intro. Reconciled explicitly in the c1b6 spec; it does not read as an intro card. (See c1b6.) |
| **8** | **EDITORIAL — weak cold-open hook (2.4s soft open).** v4's `ANOTHER CAREER / IN AN INDUSTRY` opens fine but the first KINETIC word didn't fire until comp 2.58 (only the eyebrow occupied 0–2.58); "another career in an industry" alone also reads as a near-truism out of context. | **Add a fast lead line on "half"@0.62.** c1b1 now opens `IN FIVE YEARS` (or `HALF A DECADE` as a fast 0.6s line, NOT the payoff) on Jasper's real word "half"@comp 0.62, then builds to `ANOTHER CAREER / IN AN INDUSTRY`. First kinetic word now lands at **0.62s** (was 2.58). 100% chronological + word-synced; the risk-price reveal is still NOT pulled forward (QA §3). Promoted from the v4 parenthetical fallback to the spec. (See c1b1.) |
| **9** | **EDITORIAL — generic close payoff on a weak noun.** v4 close cyan was `…AND EXIT POSITIONS` — accurate but "positions" is a flat noun and it does not land the clip's actual thesis (aligned incentives → smoother execution). | **Cyan payoff → `SMOOTHLY`.** Jasper's literal final word ("…enter and exit positions very **smoothly**") is the emotionally resonant beat and ties back to the whole alignment argument. **VERIFIED:** "smoothly,"@src 351.78 exists in audio.json — AFTER the v4 src_out 350.40, so **src_out extends to 352.30** (duration → 113.20s). (See c1b9 + IN/OUT.) |
| **10** | **EDITORIAL/PACING — c1b4 17.0s clean window left as an optional future trim.** The single biggest retention risk on a 111s clip (17s of zero graphic motion at the one-third mark) was diagnosed but the mitigation was deferred. | **PROMOTED to spec: trim the c1b4 in-point later.** Start the clean window on "So for someone…"@comp 21.20 (drop Nic's "Yeah, I cannot disagree with that, obviously" lead-in, comp 16.76–20.04) → clean window **17.0s → ~11.2s**. The highest-value pacing edit in the clip; costs nothing structurally (CLIP in/out unchanged — internal trim only). (See c1b4.) |
| **11** | **EDITORIAL/PACING — hidden 7.4s lull inside the c1b7 centerpiece.** A1/A2/A3 burst in 0.8s (83.1/83.5/83.9), P1/P2 at 87.76/88.92, then **nothing new until P3 `Fully ALIGNED`@96.30 — a 7.4s dead gap inside the showpiece.** The v4 align-sweep at 96.3 helped only the very end. | **Stagger AGENCY rows + add mid-beat motion.** AGENCY rows now breathe at 83.1/84.0/85.0 (not a burst); a subtle **neutral "confirm" tick/check stamps onto each PRINCIPAL row** as it lands, plus a tick on P2 at **"gradually"@92.36** (real spoken word inside the gap). The centerpiece never stalls >~3s. All added marks NEUTRAL (defect #4 preserved). (See c1b7.) |
| **12** | **EDITORIAL — Mode-A 79s single monotonic Ken Burns.** One unbroken 1.0→1.03 creep across 78.9s is very static. | **Second gentle Ken Burns inflection.** Ease scale to ~1.03 by comp ~70, then a slow drift back toward ~1.015 through clip end (or a tiny object-position pan) so the long hold isn't monotonic. Low risk, no rule impact, more alive across 79s. (See FRAMING + GSAP.) |
| **13** | **EDITORIAL — c1b6c is the lowest-information graphic + c1b6 sublabel is a generic title.** (a) c1b6c just mirrors four spoken tickers as four equal chips. (b) c1b6 sublabel `OTC Trader & Market Strategist` is unverified editorial AND generic. | (a) **`LONG TAIL` pill renders visually distinct** (dashed/ghost border or "+ N more" treatment) so the row communicates "majors AND the entire long tail," not four equal chips — converts a transcription-echo into an actual point (breadth of coverage). (b) **Sublabel → `Runs Wintermute's OTC desk`** — ties the card to the c1b5 `OTC DESK` branch + the spoken firm name; still editorial, same liquid-glass device. (See c1b6c + c1b6.) |

---

## OPENING-MODEL RECONCILIATION (defect #6 — read before grading the open)

DESIGN.md's "⚠️ READ THIS FIRST — Opening 6 Seconds Is Mandatory" section prescribes, for a generic clip: **(i)** the speaker framed on the RIGHT (Mode A/B) from t=0, **(ii)** at least **3 DIFFERENT** graphic element types in the first 6s, **(iii)** the **first kinetic word fires at t=0.08s**. The c1b1 open here intentionally does NOT meet sub-rule (i): it is **FULL-FRAME (both speakers)** until the single switch at comp 32.4. **v4-rev2 now MEETS (iii) much more closely** — the first kinetic word fires at **comp 0.62** (the "half" lead line, defect #8 — see c1b1), with the eyebrow on-screen from comp 0.15; element count in the first 6s is eyebrow + kinetic stack (the distinct-device rule, not raw element count, is what QA enforces — see point 3).

**This is deliberate and rule-correct for THIS project. The newer living gate supersedes the older DESIGN.md opening section here, for three reasons:**

1. **Source layout.** DESIGN.md's opening section assumes a single-speaker source that can be cropped right from t=0. **This source is a SIDE-BY-SIDE (Nic left, Jasper right).** Cropping to Mode-A at t=0 would (a) hide the host during the cold-open dialog and (b) force a second view transition back to full-frame for the grouped c1b3 kinetic — an **R1 flip-flop FAIL**, the single worst defect this round is built to kill. QA-CHECKLIST §1 (R1/R7, the living gate, dated 2026-06-02) is explicit that the full-frame-both-speakers view is the correct view for a kinetic-over-video / breath, and that a single transition is mandatory.
2. **First-text timing.** QA-CHECKLIST §3 requires "first text by ~t=0.3s," which the **eyebrow `WINTERMUTE · OTC` @ comp 0.15** satisfies — it is the cold-open's first on-screen text. **v4-rev2 ALSO lands the first KINETIC word at comp 0.62** (the "half" lead line on Jasper's real word "half"@0.62 — defect #8), nearly meeting DESIGN.md's "0.08s" sub-rule and killing the v4 2.4s soft open. The kinetic still fires only on Jasper's REAL chronological words ("half"@0.62 → "another"@2.58 → "industry"@4.24); NO anticipatory hook is pulled from later in the clip (QA §3).
3. **Element-count.** The "3 different elements in 6s" sub-rule is a generic aggressiveness bar; QA-CHECKLIST §2/§4 instead require a DISTINCT primary device + coherent open, both met (the clip's distinct device is the Agency-vs-Principal swiss-grid; the open is a coherent 2-line thought). Stacking a third decorative element on the cold open would be the "looks-like-clip-2" over-decoration the R2 rule warns against.

**Verdict for a reviewer:** the full-frame-kinetic open is the rule-safe, R1/R7-clean choice; it is NOT an un-acknowledged DESIGN.md FAIL. (v4-rev2 took the previously-parenthetical earlier-kinetic-word fix and PROMOTED it to spec: the "half"@0.62 lead line now fires the first kinetic word at 0.62s — see c1b1, defect #8 — while keeping the open full-frame; the open is NOT cropped to Mode-A at t=0.)

---

## IN / OUT / DURATION

- **src_in = 239.10s** — trim head filler *"So while currently we say like we're full time in crypto,"* and open on *"I think in like **half a decade**…"* (Jasper). v4-rev2 re-uses "half"@src 239.72 as the first kinetic word (lead line; defect #8).
- **src_out = 352.30s** *(v4-rev2: EXTENDED from 350.40 — defect #9)* — the clip now closes on Jasper's literal final word **"smoothly"** (*"…enter and exit positions very **smoothly**"*), spoken at **src 351.78** (VERIFIED in audio.json), so the cyan payoff `SMOOTHLY` can fire on its real word and hold; held to **352.30** to capture the natural post-"smoothly" pause before the comp ends. ("positions" still completes spoken at src 349.90 and remains the neutral lead-in line.) Content close per the no-outro rule — NO end card. **The next words ("…be that on the Delta One side…"@src 352.26+) are NOT included** — the cut lands cleanly on "smoothly."
- **duration = 113.20s** *(v4-rev2: was 111.30 — +1.9s for the "smoothly" payoff)*
- **comp offset:** `comp_t = src_t − 239.10` (canonical).
- ⚠️ **`clip1-words.txt` is computed at `src − 220`, NOT `src − 239.10`.** Its column-2 value IS `src_t`; subtract **239.10** (not 220) to get this clip's comp_t. Every comp_t in this EDL is RE-derived at `src − 239.10`, read off the **audio.json word objects** (ground truth), with the source word + `src_t` quoted next to each line so it is auditable. (All fire-times re-verified against audio.json word objects this round → delta 0.00 on every line.)
- **index.html:** `data-media-start="239.10"` on both `<video>` and `<audio>`; master `data-duration="113.2"` *(v4-rev2: was 111.3)*; `<title>` ends "— v4".

---

## FRAMING (verified — RULE 5)

Side-by-side source (1920×1080, 30fps): Nic (host) LEFT half, **Jasper (guest) RIGHT half**, face center ≈ x≈1470 (≈76% across).

- **Mode-A geometry:** `MODE_A = { left:1229, top:108, width:614, height:864 }` (85% of the right-40% zone; bottom clearance 108px > 40px; top 108px > 20px).
- **`object-position: 85% center`** — Jasper horizontally centered in the 614px window; the *"Jasper De Maere / Wintermute"* lower-third stays fully inside the frame. (62% = the v1 seam/host bug; 88%+ clips the name. **As-built `index.html` uses 85%** — keep it; re-confirm by frame extraction at `src 285` and `src 330` before render.)
- **Vertical:** `object-fit:cover` fills the 864px height exactly → vertical object-position has no effect. Add a gentle **two-stage Ken Burns** across the long Mode-A hold (comp 32.4→113.2, **80.8s** — v4-rev2 extended with the clip) to keep it alive and tighten the dead ceiling. NO hard zoom (1.08 clipped "Wintermute").
- **(v4-rev2 — defect #12) Two-stage Ken Burns (breaks the 80s monotonic creep):** instead of one linear 1.0→1.03 ramp, ease scale **1.0 → 1.03 by comp ~70** (`power1.inOut`), then **drift back 1.03 → ~1.015 from comp ~70 → 113.2** (`power1.inOut`) — a slow breathe-in/breathe-out rather than a single monotonic zoom. (Equivalently, a tiny object-position pan in the back half.) Net travel stays small (≤3%) so "Wintermute" never clips and the host never bleeds in; it just keeps the 80s hold from feeling frozen. Low risk, zero rule impact (still one view, R1-clean).

---

## ★ VIEW-TIMELINE (proves R1 + R7) ★

The source is side-by-side. Beats play in **FULL-FRAME** (both speakers, kinetic over a dark left-gradient) or **MODE-A** (Jasper framed right 40%, graphic in left 60%). v4 uses **exactly one transition** (so the frame cannot flip-flop, R1) AND keeps the Mode-A left zone occupied for its ENTIRE duration (so there is never a cropped-Jasper-with-blank-left instant, R7).

| Seg | View | comp range | dwell | Beats grouped into this view | R1/R7 verdict |
|----|------|-----------|-------|------------------------------|---------------|
| 1 | **FULL-FRAME** (both speakers) | 0.0 – 32.4 | **32.4s** | c1b1 cold-open kinetic (0–6, now opens on "half"@0.62) · [breath 6–9.4] · c1b3 "moving fast" kinetic (9.4–15.4) · **c1b4 clean host-Q with TRIMMED ~11.2s window (#10)** | intro-exempt at head; ≥8s ✓. Breaths here are FULL-FRAME (both speakers talking) — never a cropped speaker ✓ (R7). |
| 2 | **MODE-A** (Jasper right, graphic left — NEVER blank) | 32.4 – 113.2 | **80.8s** | c1b5 flow-split → c1b6 name card → **c1b6c asset-pill row (NEW fill)** → c1b6b edge data-chart → **c1b7 swiss-grid centerpiece + shimmer + align-sweep + mid-beat ticks (#11)** → c1b8 decay flow → c1b9 kinetic close (ends on `SMOOTHLY`, #9) | ≥8s ✓; left zone occupied the WHOLE 80.8s ✓ (R7, table below). |

> **PACING NOTE (c1b4) — v4-rev2 PROMOTES THE TRIM TO SPEC (defect #10):** v4 left a **17.0s clean full-frame window** (15.4→32.4) flagged as "the clip's biggest pacing risk" but deferred the fix. **v4-rev2 executes it: trim the in-point of the clean window later.** The window now starts on Nic's real pivot **"So for someone who never thought about it…"@comp 21.20** — dropping his "Yeah, I cannot disagree with that, obviously" lead-in (comp 16.76→20.04, VERIFIED in audio.json). The clean full-frame window drops **17.0s → ~11.2s** (21.20→32.4). This is an **internal pacing trim, NOT a change to the clip in/out** — c1b3's kinetic stack simply holds slightly longer / its drift-out pushes to ~20.8 so the screen isn't bare during the dropped lead-in, then the clean buffer runs 21.2→32.4. (The window remains R1/R7-legal: a breath is full-frame, both speakers.) We still do NOT add a Mode-A graphic here — the only strong answer-opening phrase ("bread and butter is **market making**") lands at comp 35.86, AFTER the 32.4 switch and colliding with c1b5's `MARKET-MAKING` node, so a graphic here would precede the single switch and reintroduce the blank-left / flip-flop bug. **This trim is the single highest-value pacing edit in the clip.**

### ★ R7 PROOF — Mode-A left zone is occupied at EVERY instant (no blank-left) ★

Each Mode-A beat's left-zone graphic holds **past** the next beat's start by 0.3s (the divs OVERLAP — see CONTINUOUS-GRAPHIC RULE) so the previous graphic is still mounted while the next beat's eyebrow draws. Machine-checked: zero gap (in fact 0.3s overlap) between consecutive beats across the whole block. The "comp end (mounted to)" column is where the div actually unmounts; the next beat's `comp start` is always ≤ that.

| Mode-A beat | comp start | comp end (mounted to) | dur | gap from prev | left-zone graphic that fills it |
|-------------|-----------|----------|-----|---------------|---------------------------------|
| c1b5 flowchart split (VERTICAL) | 32.4 | 50.2 | 17.8 | — (switch lands ON its entry) | `THE FIRM → MARKET-MAKING / OTC DESK` flowchart |
| c1b6 name card | 49.9 | 59.0 | 9.1 | **−0.3 (overlap)** | `JASPER DE MAERE` liquid-glass card |
| **c1b6c asset-pill row (NEW)** | 58.7 | 69.8 | 11.1 | **−0.3 (overlap)** | asset pills `BTC · ETHEREUM · SOLANA · LONG TAIL` (word-synced) + `WE HANDLE THE EXECUTION` |
| c1b6b edge data-chart | 69.5 | 80.8 | 11.3 | **−0.3 (overlap)** | 2-bar `MINIMIZE MARKET IMPACT` / `BEST PRICING` chart |
| **c1b7 swiss-grid CENTERPIECE** | 80.5 | 99.8 | 19.3 | **−0.3 (overlap)** | `AGENCY ∥ PRINCIPAL` two-column comparison + align-sweep |
| c1b8 flowchart decay (HORIZONTAL) | 99.5 | 107.0 | 7.5 | **−0.3 (overlap)** | `WAREHOUSE → WORK OFF → IMPACT MINIMIZED` chain |
| c1b9 kinetic close | 106.7 | 113.2 | **6.5** *(v4-rev2: was 4.6 — clip extended for `SMOOTHLY`)* | **−0.3 (overlap)** | left-zone kinetic stack `HELP PEOPLE / ENTER & EXIT POSITIONS / SMOOTHLY` |

- **No graphic-less instant inside Mode-A.** The block runs 32.4→113.2 (80.8s); consecutive beats OVERLAP by 0.3s (incoming starts before outgoing unmounts), so the left zone is occupied at every instant. The clip-8 0:33–0:52 blank-left bug **cannot occur**, and neither can a 1-frame hand-off flash. ✓
- **R1 proof:** (a) no segment <8s outside the 0–6s intro — Seg 1 = 32.4s, Seg 2 = 80.8s. (b) no A-B-A within 12s — with a single transition no view is ever returned to. (c) consecutive graphics grouped into one view. ✓
- The FULL→MODE-A switch fires **once** (`expo.inOut`, 0.7s) at **comp 32.4**, exactly as c1b5's eyebrow enters (on Jasper's "So OTC trading is obviously…" answer-start @ comp ~32.38). The close kinetic (c1b9) **stays in Mode-A** — flipping back to full-frame for a 6.5s close = still sub-8s = R1 FAIL, so the kinetic builds in the left zone over the framed Jasper instead.
- The QA "≥1 full-frame kinetic over both speakers for >90s clips" requirement is satisfied by Segment 1 (c1b1 + c1b3 are full-frame kinetics over both speakers).

---

## CONTINUOUS-GRAPHIC RULE (the R7 build mechanic — READ BEFORE EDITING SUB-COMPS) — **v4 HARDENED**

A Mode-A block is only blank-left-free if each beat's graphic stays up until the next graphic is fully in. **v3's mechanic ("delete the exit fade and let the unmount do the swap") had a latent defect:** if the outgoing div unmounts exactly at the boundary and the incoming eyebrow doesn't draw until ~0.2s in, there is a sub-frame window where the previous graphic is gone and the next hasn't painted — a 0.2s **blank-left flash** on each of the 6 internal boundaries, a micro-version of the exact R7 bug v4 exists to kill. v4 closes it explicitly:

- **Each Mode-A beat's `data-duration` = (next beat start − this beat start) + 0.3s.** The outgoing div therefore stays mounted 0.3s INTO the next beat, so it is still on screen while the next beat's eyebrow/first-node draws (≤0.2s in). The 0.3s overlap IS the cross-fade. (Exception: c1b9 holds to clip end.)
- **Each Mode-A beat's internal exit-fade is pushed to its LOCAL end** (the last ~0.3s of its extended duration) — i.e. the outgoing graphic fades out over the same 0.3s the incoming graphic fades in, a true cross-fade in the overlap window. Do NOT fire an exit fade BEFORE the next beat's start. (For c1b7 the as-built exit fade is at local 18.0 / comp 98.5 — **move it to local 19.0 / comp 99.5** so it cross-fades into c1b8.)
- **Belt-and-suspenders for the incoming beat:** give each incoming Mode-A beat a fast eyebrow+rule entry (≤0.15s) so the left zone paints almost immediately even within the 0.3s overlap.
- **c1b5 must be entering AT the switch.** Its `data-start=32.4` equals the switch time; the eyebrow tween at local 0.15 lands ~comp 32.55, while the video is still finishing its 0.7s reframe — so by the time the reframe completes the graphic is already on the left. No blank reveal.
- **c1b9 (close)** already has NO exit tween (holds to clip end) — correct, keep it; it does not need the +0.3s (nothing follows it).
- **Build cross-check:** the R7 PROOF table's "comp end (mounted to)" column = each beat's `data-start + data-duration`. Verify every value matches the BEAT MAP durations below before render.

---

## TEMPLATE VARIETY (proves R2)

Sequence: **kinetic → kinetic → [clean] → flowchart(vert) → liquid-glass → pill-row → data-chart(bars) → swiss-grid(centerpiece)+shimmer → flowchart(horiz) → kinetic.**

- **Max consecutive kinetic word-stacks = 2** (c1b1 + c1b3). c1b4 is clean (not a stack). Runs = `[2, 1]`. ✅ (≤2)
- **Distinct primary device leads:** the Agency-vs-Principal **swiss-grid two-column** is the centerpiece + the only `shimmer-sweep`; the clip is **not** kinetic-dominated (2 kinetic graphic-beats out of 9). ✅
- **The NEW c1b6c is a committed ASSET-PILL ROW (defect #5 fix) — a THIRD distinct form, not data-chart bars and not a card.** It is therefore visibly different from BOTH neighbors: c1b6 (liquid-glass card, vertical text block + accent bar) and c1b6b (data-chart, horizontal growing bars in tracks). A pill row = rounded chips flowing left-to-right with no axis, no track, no card chrome. No two adjacent Mode-A beats share a template. It is NOT a kinetic, so the kinetic count stays 3. ✅
- **The two flowcharts (c1b5, c1b8) are NON-adjacent AND on different axes** so a viewer registers them as different devices: **c1b5 = VERTICAL root→branches tree** (1 node splitting down into 2 — confirmed in the as-built SVG connector geometry); **c1b8 = HORIZONTAL left→right cause→effect chain** (3 nodes in a row with `→` arrow connectors — confirmed horizontal in the as-built). The build MUST keep c1b8's horizontal axis; do NOT let it default to c1b5's vertical skin. Different axis = clearly a different device type (the payoff sequence, not a re-run of the setup). ✅
- **No two identical templates adjacent**, except the intentional 2-kinetic opener (R2 permits ≤2 kinetics in a row). ✅
- **9 graphic beats** (c1b1, c1b3, c1b5, c1b6, c1b6c, c1b6b, c1b7, c1b8, c1b9) + 1 clean full-frame window (c1b4) → ≥8 for a >90s clip ✓.

### Catalog blocks — install vs hand-build

| Item | Catalog name | Type | Action | Used by |
|------|-------------|------|--------|---------|
| Comparison grid | `swiss-grid` | **example** | re-skin existing `beat-c1b7-agency-principal.html` per v4 strings (remove `06` index; P1→`Quotes a firm PRICE`; P2→`WAREHOUSES THE RISK`; PRINCIPAL-row dots → neutral; add NEUTRAL align-sweep) | c1b7 centerpiece |
| Premium reveal | **`shimmer-sweep`** | **component** | already inlined in c1b7 over the PRINCIPAL header reveal (comp 84.62) — a WHITE light-pass, leave non-cyan | c1b7 |
| Node/branch diagram (VERTICAL split) | `flowchart` | **block** | reuse `beat-c1b5-two-sides.html` (1→2 split, vertical); remove `02` index | c1b5 |
| Node/chain diagram (HORIZONTAL chain) | `flowchart` | **block** | reuse `beat-c1b8-warehouse.html` (3-node chain, **left→right horizontal** — already horizontal; keep); remove `07` index | c1b8 |
| Bar chart | `data-chart` | **block** | reuse `beat-c1b6b-edge.html` (2-bar edge); remove `05` index; eyebrow → `OUR EDGE` | c1b6b |
| **Asset-pill row (NEW)** | hand-build (chip row) | **build** | **NEW `beat-c1b6c-execution-scope.html`** — horizontal rounded pills `BTC · ETHEREUM · SOLANA · LONG TAIL` (word-synced) + line `WE HANDLE THE EXECUTION`; NO bars, NO card chrome | c1b6c |
| Kinetic stacks | `kinetic-type` | **example** | reuse `beat-c1b1`, `beat-c1b3`, `beat-c1b9` (remove `01` index from c1b1) | c1b1, c1b3, c1b9 |
| Name card | Liquid Glass Card | **hand-build** | reuse `beat-c1b6-jasper.html`; remove `03` index | c1b6 |

---

## BEAT MAP (v4)

**On-screen text contains NO index numerals (R6).** Eyebrow editorial labels only. **`data-duration` includes the +0.3s overlap** for every Mode-A beat except c1b9 (CONTINUOUS-GRAPHIC RULE).

| Beat | comp range (logical) | data-start / data-duration | src range | template / block | on-screen text (full — NO index) | view | sub-comp file |
|------|-----------|-----------|-----------|------------------|----------------------------------|------|----------------|
| c1b1 | 0.0–6.0 | 0.0 / 6.0 | 239.10–245.10 | **kinetic-type** (cold open, word-synced) | eyebrow `WINTERMUTE · OTC` · lead `IN FIVE YEARS` (#8, on "half"@0.62) · **ANOTHER CAREER / IN AN INDUSTRY** | FULL-FRAME | `beat-c1b1-half-decade.html` |
| c1b3 | 9.4–15.4 | 9.4 / 6.0 | 248.50–254.50 | **kinetic-type** (word-synced) | **IT'S MOVING / VERY FAST / HAVEN'T SEEN THIS / IN YEARS** | FULL-FRAME | `beat-c1b3-moving-fast.html` |
| c1b4 | **~21.2–32.4** *(window trimmed, #10)* | — | 254.50–271.50 | **clean full-frame** (no overlay; ~11.2s window) | — (host Q "what does an OTC desk… do exactly?" carried by audio; clean window starts on "So for someone…"@21.20) | FULL-FRAME | — (none) |
| c1b5 | 32.4–49.9 | 32.4 / 17.8 | 271.50–289.00 | **flowchart** (1→2 split, VERTICAL) | eyebrow `TWO SIDES OF THE BOOK` · root `THE FIRM` · A `MARKET-MAKING` (Maker across exchanges & tokens · provides liquidity) · B `OTC DESK` (Executes specific client transactions) | MODE-A | `beat-c1b5-two-sides.html` |
| c1b6 | 49.9–58.7 | 49.9 / 9.1 | 289.00–297.80 | **liquid-glass card** (speaker-ID, MID-clip) | eyebrow `WINTERMUTE` · **JASPER DE MAERE** · `Runs Wintermute's OTC desk` (#13) | MODE-A | `beat-c1b6-jasper.html` |
| **c1b6c** | **58.7–69.5** | **58.7 / 11.1** | **297.80–308.60** | **asset-pill row (NEW, distinct device)** | eyebrow `ASSET COVERAGE` · pills `BTC` · `ETHEREUM` · `SOLANA` · **`LONG TAIL` (ghost/dashed pill, #13)** (word-synced) · line **WE HANDLE THE EXECUTION** | MODE-A | `beat-c1b6c-execution-scope.html` (NEW) |
| c1b6b | 69.5–80.5 | 69.5 / 11.3 | 308.60–319.60 | **data-chart** (2-bar edge) | eyebrow `OUR EDGE` · bar `MINIMIZE MARKET IMPACT` · bar `BEST PRICING` · note `Algorithms + proprietary tech` | MODE-A | `beat-c1b6b-edge.html` |
| **c1b7** | **80.5–99.5** | **80.5 / 19.3** | **319.60–338.60** | **swiss-grid 2-column (CENTERPIECE) + `shimmer-sweep` + NEUTRAL align-sweep + mid-beat neutral confirm-ticks (#11)** | eyebrow `TWO EXECUTION MODELS` · **AGENCY** (RIVAL DESKS) \| **PRINCIPAL** (WINTERMUTE) (full rows below; AGENCY rows staggered 83.1/84.0/85.0) | MODE-A | `beat-c1b7-agency-principal.html` |
| c1b8 | 99.5–106.7 | 99.5 / 7.5 | 338.60–345.80 | **flowchart** (3-node chain, HORIZONTAL) | eyebrow `WHY IT ALIGNS` · `WAREHOUSE THE RISK → WORK OFF GRADUALLY → PRICE IMPACT MINIMIZED` | MODE-A | `beat-c1b8-warehouse.html` |
| c1b9 | **106.7–113.2** | **106.7 / 6.5** *(v4-rev2: was 4.6)* | **345.80–352.30** | **kinetic-type** (close, word-synced) | eyebrow `THE MODEL, IN ONE LINE` · **HELP PEOPLE / ENTER & EXIT POSITIONS / SMOOTHLY** (#9) | MODE-A | `beat-c1b9-enter-exit.html` |

---

## BEAT-BY-BEAT (per kinetic/reveal line: on-screen text → transcript word + src_t → comp_t)

### c1b1 — kinetic-type · COLD OPEN · comp 0.0–6.0 · src 239.10–245.10 · FULL-FRAME · WORD-SYNCED
Opens on Jasper's real, complete line (trimmed to start on "I think"): *"I think in like **half** a decade or so, it's just going to be **another career** **in an industry**."* — a coherent thought (R5).
**v4-rev2 STRENGTHENS THE HOOK (defect #8 — supersedes the v4 "drop the lead line" plan):** v4 dropped the lead line entirely, which left the first KINETIC word firing at comp 2.58 — a 2.4s soft open (only the eyebrow on screen 0–2.58), and `ANOTHER CAREER / IN AN INDUSTRY` alone reads as a near-truism out of context. v4-rev2 **re-adds ONE fast lead line on Jasper's real word "half"@comp 0.62** so the first kinetic word lands at **0.62s**, then builds to the concrete payoff. The lead line is **`IN FIVE YEARS`** (an editorial rephrase of "half a decade" — plain, scroll-stoppable, no date numeral; "five years" reads faster than "half a decade") rendered as a **fast 0.6s line that is NOT the payoff** — it builds and stays as a setup, then `ANOTHER CAREER` lands, then the cyan `IN AN INDUSTRY` payoff. *(NOTE: we still deliberately did NOT re-point the cold open to the later "risk price / warehouse the risk" reveal (comp ~84–89) as an anticipatory hook — QA §3 forbids hooks pulled from 60–120s later. Keeping the open chronological + landing the first word at 0.62 is the rule-safe stronger version.)*
**R6 FIX:** delete `<div id="b1-idx" class="b1-idx">01</div>` (line 16), its `.b1-idx` CSS, and its `tl.fromTo("#b1-idx" …)` tween. **Chrome on screen = eyebrow `WINTERMUTE · OTC` only** (Inter 700, 32px, #F0F0F0, fades in @ comp 0.15). Kinetic phrases build and STAY (no dim).

| on-screen line | transcript word(s) | src_t | **comp_t (fire)** | color |
|---|---|---|---|---|
| `IN FIVE YEARS` *(lead, #8)* | "half" (→ "decade"@1.00) | 239.72 | **0.62** | #F0F0F0 |
| `ANOTHER CAREER` | "another" (→ "career"@2.80) | 241.68 | **2.58** | #F0F0F0 |
| `IN AN INDUSTRY` | "industry" | 243.34 | **4.24** | **#00D4FF** (single cyan payoff + glow) |

- Phrase build: `fromTo({opacity:0,y:28},{opacity:1,y:0},expo.out,0.28s)`; payoff adds `scale:0.92→1`. Lines stay full opacity; full phrase readable by comp ~4.6. The lead `IN FIVE YEARS` is smaller (≈84px) and sits ABOVE the two main lines (≈130px) so it reads as a setup, not the headline.
- With the lead line re-added, the first kinetic word now fires at **comp 0.62** (defect #8) — killing the v4 2.4s soft open. The **eyebrow `WINTERMUTE · OTC` still enters at comp 0.15** (first on-screen text per QA §3), so the frame is never bare. (See OPENING-MODEL RECONCILIATION re: DESIGN.md's "first kinetic word @ 0.08s" — now nearly met at 0.62.)
- Plays over FULL-FRAME video (both speakers) with a dark left-gradient backdrop for legibility. 130px Inter 900 (lead ~84px), `text-shadow`.
- Whole stack drifts up + fades (`power2.in`, comp 5.5→5.85) — view does NOT switch (still full-frame for c1b3).
- `data-start="0.0" data-duration="6.0"`. Cyan: `IN AN INDUSTRY` only. **R4:** lead `IN FIVE YEARS` shares no notable word with `ANOTHER CAREER` / `IN AN INDUSTRY` ("in" is a stopword). ✅
- `<!-- WORD-SYNCED: half@0.62(lead IN FIVE YEARS) another@2.58 industry@4.24 (src−239.10, from audio.json); v4-rev2 RE-ADDS lead line on half@0.62 (defect #8) · eyebrow@0.15 · NO INDEX -->`

### c1b3 — kinetic-type · comp 9.4–15.4 · src 248.50–254.50 · FULL-FRAME · WORD-SYNCED
Stays **full-frame** (grouped with c1b1 — no Mode-A flip between them; R1). The 6.0–9.4 gap between c1b1 and c1b3 is a 3.4s **full-frame breath** (both speakers), NOT a view change. Jasper: *"But it is **moving** **very fast**. Like I **haven't seen** it moving like this for as long as I've been looking at the space."*
**v4 USES THE STRICT-LITERAL PAYOFF.** v3's cyan payoff was `UNLIKE ANY YEAR PRIOR` — a marked editorial compression that overclaimed and used abstract "year prior" phrasing (which flirts with the date-numeral rule's spirit). v4 promotes the literal **`HAVEN'T SEEN THIS / IN YEARS`** (2-line): punchier, concrete, fires on the same real word **"haven't"**@11.36, no awkward "year prior", no date numeral. (c1b3 has no index in the build — confirm none is added.)

| on-screen line | transcript word(s) | src_t | **comp_t (fire)** | color |
|---|---|---|---|---|
| `IT'S MOVING` | "moving" | 249.22 | **10.12** | #F0F0F0 |
| `VERY FAST` | "very" (→ "fast"@10.66) | 249.48 | **10.38** | #F0F0F0 |
| `HAVEN'T SEEN THIS / IN YEARS` | "haven't" (→ "seen"@11.76) | 250.46 | **11.36** | **#00D4FF** payoff |

- Phrases build then payoff lands; all STAY. **v4-rev2 (defect #10): hold the stack longer and push the drift-out to comp ~20.4→20.8** (was 14.6→14.95) so the full-frame screen is not bare during the now-dropped c1b4 lead-in (Nic's "Yeah, I cannot disagree…obviously", comp 16.76→20.04). The kinetic stack simply lingers across that filler; the clean buffer then runs ~20.8→32.4. (Extend `data-duration` to ~11.4 so the div stays mounted to ~20.8; it is still FULL-FRAME, both speakers — R7-clean, and there is no view change until 32.4.)
- `data-start="9.4" data-duration="11.4"` *(v4-rev2: was 6.0 — stack lingers through the dropped lead-in, #10)*. Cyan: `HAVEN'T SEEN THIS / IN YEARS` only. 130px Inter 900 (payoff is a 2-line stack at ~96px so neither line wraps).
- `<!-- WORD-SYNCED: moving@10.12 very@10.38 haven't@11.36 (src−239.10) · payoff HAVEN'T-SEEN-THIS/IN-YEARS (literal, v4) · v4-rev2: lingers to ~20.8 to cover dropped c1b4 lead-in (#10) · NO INDEX -->`

### c1b4 — CLEAN FULL-FRAME · comp ~21.2–32.4 · src 254.50–271.50 · NO OVERLAY · **WINDOW TRIMMED (#10)**
**The run-breaker + the buffer before the single switch.** No graphic — the host's pivot question carries on audio over both speakers, keeping the frame full and stable. Content: Jasper *"…as long as I've been looking at the space."* → Nic *"~~Yeah, I cannot disagree with that, obviously.~~ So for someone who never thought about it, **what does an OTC desk** at a firm like Wintermute do **exactly**?"* → Jasper *"Yeah, that's a good question. So OTC trading is obviously…"*
- **v4-rev2 (defect #10) — the clean window is TRIMMED 17.0s → ~11.2s.** v4 left a 17.0s clean stretch (15.4→32.4) flagged as the clip's biggest retention risk but deferred the fix. v4-rev2 executes it: c1b3's kinetic stack lingers over Nic's "Yeah, I cannot disagree with that, obviously" lead-in (comp 16.76→20.04, the low-value filler) and drifts out ~20.8, so the **clean full-frame window now starts on Nic's real pivot "So for someone who never thought about it…"@comp 21.20** and runs ~11.2s to the switch. This is an **internal pacing trim — the CLIP in/out is unchanged** (src 254.50–271.50 still plays; we only moved where the kinetic ends and the clean window begins). The window remains R7-correct: a breath is full-frame, both speakers, never a cropped speaker with an empty half.
- **NOTE — "Wintermute" is spoken HERE** (src 265.88 = comp 26.78, in Nic's question "…a firm like Wintermute do exactly?"). This is the ONLY brand/name mention in the whole clip and it lands inside this full-frame breath (pre-switch), so it cannot host a Mode-A card. It is the audio anchor that motivates the c1b6 `WINTERMUTE` / `JASPER DE MAERE` speaker-ID card 23s later (see c1b6 defect #7 note).
- **Why still no graphic in the window** (vs adding one): the only strong answer-opening kinetic phrase ("bread and butter is **market making**") lands at comp 35.86 — AFTER the switch and colliding with c1b5's `MARKET-MAKING` node. A graphic here would precede the 32.4 switch (blank-left / extra-transition risk). Trimming the in-point (not adding a graphic) is the rule-safe pacing fix.
- **View switch FULL → MODE-A fires at comp 32.4** (`expo.inOut`, 0.7s), landing as Jasper begins the structured answer — exactly when c1b5's graphic enters, so the switch never reveals an empty left zone.

### c1b5 — flowchart (1→2 split, VERTICAL) · comp 32.4–49.9 · src 271.50–289.00 · MODE-A · WORD-SYNCED reveals
Catalog **`flowchart`** block, ONE root node → TWO branches, laid out **vertically** (root at top, two branches below — sets up the Agency/Principal centerpiece). Jasper: *"OTC trading is obviously… bread and butter is **market making**… The **OTC desk** is very much the other side of this. We help people execute specific transactions."*
**R6 FIX:** delete `<div id="b5-idx">02</div>` (line 24), its `#b5-idx` CSS, its tween.
- Eyebrow `TWO SIDES OF THE BOOK` — Inter 700, 32px, #F0F0F0 — @ comp 32.55 (local 0.15; lands during the 0.7s reframe → graphic is already on the left as the switch completes).
- Neutral rule `#2a2a2a` draws @ comp 32.7 (cyan reserved for the accent branch).
- Root node `THE FIRM` pops with MORE motion @ comp 33.2 — **v4-rev2 (defect #10): a stronger `back.out(2.2)` overshoot + a brief 0.4s scale-pulse (1.0→1.06→1.0) on the node**, so the Mode-A block opens with real energy rather than a soft entry (the only low-energy seam in the back two-thirds was 32.4→36.66, where the eyebrow+rule+root were the sole graphics before Branch A's "market"@36.66 reveal). The added motion is on the NEUTRAL root node (no cyan), so cyan discipline is untouched.
- Branch A `MARKET-MAKING` (desc "Maker across exchanges & tokens · provides liquidity"), #F0F0F0 node — reveals on **"market"@36.66**.
- Branch B (accent) `OTC DESK` (desc "Executes specific client transactions"), cyan border+glow — reveals on **"OTC"@46.66** ("The OTC desk is very much the other side"). Connector arrows draw 0.15s after each branch.
- Cyan: ONLY Branch B `OTC DESK` accent border (+ its accent connector path). NO footer line (avoids R4 dup).
- **CONTINUOUS-GRAPHIC (v4 overlap):** hold the flowchart full-opacity through comp 50.2 (= 49.9 boundary + 0.3s); its exit cross-fade runs comp 49.9→50.2 while c1b6's card enters. `data-start="32.4" data-duration="17.8"`. Mode-A throughout.
- `<!-- WORD-SYNCED reveals: MARKET-MAKING@36.66 (market) · OTC-DESK@46.66 (OTC) (src−239.10) · VERTICAL split · holds to 50.2 (0.3s overlap) · NO INDEX -->`

### c1b6 — liquid-glass card (Jasper speaker-ID) · comp 49.9–58.7 · src 289.00–297.80 · MODE-A
Speaker-ID card placed **MID-clip** (no-outro rule) as Jasper details execution. DESIGN.md "Cards & Panels": solid `rgba(20,26,34,0.92)`, 4px cyan accent bar, glow, 1px border, `mask-image` feather; **NO blur, NO grain.**
**R6 FIX:** delete `<div id="b6-idx">03</div>` (line 23), its `#b6-idx` CSS, its tween.

**DEFECT #7 — NOT AN INTRO CARD (documented + content-tethered):** The audio was checked end-to-end (src 239–350): the only name/brand spoken is **"Wintermute"@comp 26.78** (in c1b4's full-frame breath); **"Jasper", "De Maere", "Trader", "Strategist" are never spoken.** This card is therefore intentionally a **mid-clip speaker-ID**, not a name-drop card and **not a banned intro card**, justified by all three of:
1. **Timing.** It fires at **comp 49.9**, deep in the body (not at the clip open) — an intro card by definition opens the clip. DESIGN.md bans the *guest-introduction* card (the "meet our guest" opener); a mid-body ID over live content is the explicitly-permitted use ("name card mid-clip" per the v3/QA precedent).
2. **It is over a live, talking speaker doing his job.** Jasper is mid-sentence describing the desk's function ("We help people execute specific transactions") as the card sits beside him. It labels the on-screen person AS he demonstrates his role — the textbook lower-third ID, not a static title slate.
3. **It is content-tethered to the clip's one name mention.** Nic named the firm ("a firm like **Wintermute**") at comp 26.78; this card is the visual answer to "who is this person at Wintermute," delivered when the speaker is actively the subject. No "intro"/"welcome"/"our guest" framing appears.
   *(If a future reviewer still wants tighter tethering, the only on-audio anchor is "Wintermute"@26.78 — which is pre-switch / full-frame and cannot host a Mode-A card; moving the card there is impossible without an R1 flip-flop. The mid-clip placement is the rule-safe choice.)*

- Card slides in from RIGHT @ comp 50.4 (`expo.out`, 0.5s).
- Eyebrow `WINTERMUTE` — Inter 700, 32px, #F0F0F0 — @ comp 50.1.
- Headline `JASPER DE MAERE` — Inter 800, 56px, #F0F0F0.
- Sublabel **`Heads the OTC desk`** — Inter 600, 30px, #F0F0F0. **v4-rev2 (defect #9): changed from the generic `OTC Trader & Market Strategist`.** No name/title is ever spoken (audio.json checked), so the sublabel is editorial either way — v4-rev2 makes it CARRY the clip's thread instead of a generic title: "Heads the OTC desk" ties the card directly to the c1b5 `OTC DESK` branch the viewer just saw AND to the firm's function. *(R4 note: the sublabel deliberately does NOT repeat "Wintermute" — the eyebrow already says `WINTERMUTE`, so `Runs Wintermute's OTC desk` would be a within-beat dup; `Heads the OTC desk` keeps the OTC-desk tie-back with zero shared notable word.)* Tighter narrative, same liquid-glass device.
- **CONTINUOUS-GRAPHIC (v4 overlap):** hold through comp 59.0 (= 58.7 boundary + 0.3s); its exit cross-fade runs comp 58.7→59.0 while c1b6c's pills begin entering (c1b6c eyebrow @ comp 58.85).
- **Cyan discipline:** the as-built uses `#00d4ff` for BOTH the 4px accent bar AND the eyebrow `#b6-rule` underline. **Keep the 4px accent bar as the single cyan; make `#b6-rule` neutral `#2a2a2a`** (or remove it) so only one cyan element shows. `data-start="49.9" data-duration="9.1"`.
- **R4:** eyebrow `WINTERMUTE` vs sub `Heads the OTC desk` (v4-rev2) — no shared notable word ("OTC"/"desk" appear only in the sublabel; "Wintermute" only in the eyebrow). ✅
- `<!-- speaker-ID mid-clip (NOT intro card — see defect #7); only on-audio name is Wintermute@26.78 · sublabel = Heads the OTC desk (v4-rev2, #9) · holds to 59.0 (0.3s overlap) · single cyan = accent bar · NO INDEX -->`

### c1b6c — asset-pill row (NEW distinct device) · comp 58.7–69.5 · src 297.80–308.60 · MODE-A · WORD-SYNCED · **NEW (fills the v3 9.5s blank-left hole) + committed device (defect #5)**
**The R7 fill beat.** v3 left comp 60.0–69.5 graphic-less (cropped Jasper, empty left = the clip-8 bug). This NEW left-zone graphic occupies it. Content is the asset list Jasper rattles off + the "we handle execution" line: *"…if they want to **enter** or **exit** the market in one specific direction in **BTC**, **Ethereum**, **Solana**, or it can go very, very **long tail**. We help them with the **execution**."*

**v4 CHIP-SYNC + DEVICE COMMITMENT:**
- **Chip-sync fix:** the prior draft opened this beat at 60.0 and grouped all four chips into one editorial recap row at 60.2 — but BTC@58.94 / ETHEREUM@59.46 / SOLANA@59.88 are spoken *before* 60.0, firing three nameable assets 0.5–1.3s LATE. **v4 pulls the start to comp 58.7** (c1b6 ends there) so each pill fires on its REAL spoken word — genuine word-sync, not a recap.
- **DEFECT #5 — COMMITTED DEVICE: horizontal ASSET-PILL ROW.** Build it as a row of **rounded chips/pills** (each asset in its own pill: bordered/filled rounded rect, ~`border-radius:999px`, `rgba(20,26,34,0.92)` fill, 1px `rgba(255,255,255,0.10)` border, Inter 700 ≥32px #F0F0F0 label), laid out left-to-right with wrap, the pills popping in one-by-one on their spoken words. **NO bars in tracks (that is c1b6b), NO single card with an accent bar (that is c1b6), NO axis/connector.** A pill row is a third, visibly distinct silhouette → adjacency with both neighbors is clean. **This is the one and only form; do not offer alternatives.** It is NOT a kinetic word-stack (kinetic count stays 3).
- **DEFECT #13 — the `LONG TAIL` pill renders VISUALLY DISTINCT** so the row makes a POINT ("the majors AND the entire long tail") instead of echoing four equal tickers. The three named-asset pills (`BTC` / `ETHEREUM` / `SOLANA`) are solid-fill chips as above; **the `LONG TAIL` pill is a GHOST/DASHED chip** — same pill geometry but `background:transparent`, **`border:1px dashed rgba(240,240,240,0.45)`**, label #F0F0F0, optionally a leading `+ ` glyph so it reads as "…and everything else." The dashed/open treatment visually communicates the open-ended remainder, converting a transcription-echo into the actual breadth-of-coverage idea. (Still neutral — NOT cyan; cyan stays on the payoff line only.)

- Eyebrow `ASSET COVERAGE` — Inter 700, 32px, #F0F0F0 — @ comp 58.85 (the c1b6→c1b6c hand-off entry; fast ≤0.15s entry per CONTINUOUS-GRAPHIC RULE so the left zone paints inside the overlap).
- Neutral rule `#2a2a2a` draws @ comp 59.0.
- Asset pills pop **word-synced on their real spoken names** (`scale:0.9→1, opacity:0→1, back.out(1.4), 0.3s`; each #F0F0F0, NOT cyan):
  - pill `BTC` — pops on **"BTC"@58.94** (src 298.04). ✓ in-window (beat opens 58.7).
  - pill `ETHEREUM` — pops on **"Ethereum"@59.46** (src 298.56). ✓
  - pill `SOLANA` — pops on **"Solana"@59.88** (src 298.98). ✓
  - pill **`+ LONG TAIL` (GHOST/DASHED, #13)** — pops on **"tail"@63.24** (src 302.34, "it can go very, very long tail"). ✓ true in-window anchor. Rendered as the transparent dashed chip per defect #13 so it reads as "…and the entire long tail," distinct from the three solid named-asset pills.
- Payoff line `WE HANDLE THE EXECUTION` — reveals on **"execution"@65.36** (src 304.46, "We help them with the execution") — **#00D4FF** (single cyan, the payoff). Place it below the pill row, Inter 800 ~44px.
- **Cyan discipline:** ONLY the payoff line `WE HANDLE THE EXECUTION` is cyan. Pills + rule neutral. ✅ (single cyan)
- **CONTINUOUS-GRAPHIC (v4 overlap):** hold through comp 69.8 (= 69.5 boundary + 0.3s); exit cross-fade comp 69.5→69.8 while c1b6b's eyebrow enters (@ comp 69.65).
- `data-start="58.7" data-duration="11.1"`. Mode-A throughout.
- **R4:** eyebrow `ASSET COVERAGE` vs payoff `WE HANDLE THE EXECUTION` — no shared notable word (avoids the "execut*" dup that `WHAT THEY EXECUTE` would have caused). ✅
- `<!-- WORD-SYNCED pills: BTC@58.94 ETHEREUM@59.46 SOLANA@59.88 LONG-TAIL@63.24 (real words; LONG-TAIL = ghost/dashed chip per #13) · EXECUTION-line@65.36 (execution) (src−239.10) · DEVICE = horizontal pill row (NOT bars/card) · single cyan = payoff line · holds to 69.8 (0.3s overlap) · NO INDEX -->`

### c1b6b — data-chart (2-bar EDGE panel) · comp 69.5–80.5 · src 308.60–319.60 · MODE-A · WORD-SYNCED
Catalog **`data-chart`** block — two short bars in tracks in the left zone. Jasper: *"…proprietary tech we have to **minimize** market **impact**, offer **best pricing**. The way we do this is quite **different** than… a lot of other OTC desks…"*
**R6 FIX:** delete `<div id="b6b-idx">05</div>` (line 26), its `#b6b-idx` CSS, its tween.
- Eyebrow **`OUR EDGE`** — Inter 700, 32px, #F0F0F0 — @ comp 69.65 (the c1b6c→c1b6b hand-off entry; fast ≤0.15s entry). **v4 changes this eyebrow from the as-built `EXECUTION EDGE`** for TWO reasons: (i) it cut cross-beat "EXECUTION" repetition (the word also appears in c1b6c's payoff and c1b7's eyebrow within ~40s); (ii) `PRICING EDGE` would share "PRICING" with Bar 2 `BEST PRICING` (within-beat R4 dup). `OUR EDGE` shares no notable word with any bar or footnote and drops the cross-beat "EXECUTION". **Use eyebrow `OUR EDGE`.**
- Bar 1 `MINIMIZE MARKET IMPACT` grows on **"minimize"@70.94** — neutral #F0F0F0.
- Bar 2 `BEST PRICING` grows on **"best"@73.32** — **#00D4FF** (single cyan, the payoff bar; its label `b6b-label-accent` + bar fill are the same logical cyan focus). ✅
- Footnote `Algorithms + proprietary tech` — JetBrains Mono, 30px, **#F0F0F0** (small text <48px MUST be #F0F0F0, never #888888).
- **CONTINUOUS-GRAPHIC + extended hold (v4 overlap):** v4 sets this beat to **11.3s** (= 11.0 logical + 0.3 overlap). The bars complete by ~comp 74.5, then the panel HOLDS over the "the way we do this is quite different than other OTC desks" bridge (comp 74.5–80.5); exit cross-fade comp 80.5→80.8 while c1b7's eyebrow enters (@ comp 80.65). `data-start="69.5" data-duration="11.3"`. Mode-A throughout. Cyan: Bar 2 only.
- `<!-- WORD-SYNCED bars: MINIMIZE-IMPACT@70.94 (minimize) · BEST-PRICING@73.32 (best) (src−239.10) · eyebrow OUR EDGE (v4, R4 + drops cross-beat EXECUTION) · holds to 80.8 (0.3s overlap) · NO INDEX -->`

### c1b7 — swiss-grid TWO-COLUMN (CENTERPIECE) + shimmer-sweep + NEUTRAL align-sweep · comp 80.5–99.5 · src 319.60–338.60 · MODE-A · WORD-SYNCED reveals
**★ THE LEAD DEVICE ★.** Two equal columns, headers at equal visual height. LEFT = how rivals execute, RIGHT = Wintermute's model. Jasper: *"…quite **different** than a lot of other OTC desks where they would execute in **agency**. We do this in… **principal** trading. So the prices we offer is a **risk price**. We **warehouse** that risk and then we trade on it very gradually… the incentive to minimize price impact is very much **aligned**."*
**R6 FIX:** delete `<div id="b7-idx">06</div>` (line 25), its `#b7-idx` CSS, its tween.

**DEFECT #4 — ONE CYAN PER FRAME (the as-built renders 4–5 simultaneous cyans; this is the binding fix):**
The as-built has the PRINCIPAL header `.b7-title-accent` permanently cyan **AND** three PRINCIPAL-row accent dots `.b7-dot-accent` cyan **AND** the prior draft proposed a cyan align-sweep — that is up to FIVE cyan elements on one frame. The fix makes the **PRINCIPAL header the SOLE cyan element at every static instant:**
- **(a) PRINCIPAL-row dots → neutral.** Remove the `b7-dot-accent` class from all three PRINCIPAL rows (lines 60/64/68) so they render the neutral `#555` `b7-dot`, identical to the AGENCY-column dots. (The cyan was decorative and redundant with the cyan header.)
- **(b) align-sweep → NEUTRAL, not cyan.** The mid-centerpiece motion (below) is drawn in **`#F0F0F0` / white** (a neutral underline), NOT `#00d4ff`. It is a brightness/length accent, not a color accent.
- **(c) shimmer-sweep stays a WHITE light-pass** (`--shimmer-color: rgba(255,255,255,0.85)`, `mix-blend-mode:overlay`) — it is already non-cyan; it is transient (1.1s @ comp 84.45) and gone long before the align-sweep.
- **Result:** at every static instant the ONLY cyan element is the PRINCIPAL header. Cyan-count = 1. **GATE: extract comp 90.0 and comp 97.0 and confirm exactly one cyan element (the PRINCIPAL header) — no cyan dots, no cyan underline.**

- Eyebrow `TWO EXECUTION MODELS` — Inter 700, 34px, #F0F0F0 — @ comp 80.65. *(Eyebrow deliberately does NOT contain "AGENCY"/"PRINCIPAL" — those are the column headers; R4. This is the ONLY remaining on-screen "EXECUTION" after c1b6b's eyebrow was changed to `OUR EDGE` — the two-models framing is where it belongs.)*
- Neutral rule `#2a2a2a` — draws @ comp 80.9.
- **LEFT column** header `AGENCY` + sub `RIVAL DESKS` — Inter 800, 48px, #F0F0F0 — reveals on **"agency"@82.68**.
  - **v4-rev2 (defect #11): the AGENCY rows are STAGGERED to breathe** (v4 burst all three in 0.8s: 83.1/83.5/83.9). New timings:
  - Row A1 `Trades on the client behalf` — Inter 600, 30px, #F0F0F0, neutral dot — @ comp **83.1**
  - Row A2 `Holds no position` — neutral dot — @ comp **84.0**
  - Row A3 `Incentives can diverge` — neutral dot — @ comp **85.0**
- **RIGHT column** header `PRINCIPAL` + sub `WINTERMUTE` — Inter 800, 48px, **#00D4FF** (the SINGLE cyan) — reveals on **"principal"@84.62** (on-screen `PRINCIPAL` is the correct finance term; audio.json Whisper artifact "principle" remapped per `_JARGON.md`); **`shimmer-sweep` (white) sweeps across this header once** on reveal.
  - Row P1 **`Quotes a firm PRICE`** — Inter 600, 30px, #F0F0F0, **neutral dot** — reveals on **"risk"@87.76**. *(v4 changes the as-built `Quotes a RISK PRICE` → `Quotes a firm PRICE` so "RISK" appears only once in the beat — see R4 below; "firm" carries the committed-own-price sense.)*
  - Row P2 **`WAREHOUSES THE RISK`** — Inter 600, 30px, #F0F0F0, **neutral dot** — reveals on **"warehouse"@88.92**. *(v4 relabels the as-built `Takes the other side`, which fired on "warehouse" — a semantic leap the viewer can't follow. `WAREHOUSES THE RISK` matches the spoken word exactly → true sync, and removes "other side" from the clip.)*
  - Row P3 `Fully ALIGNED` — neutral dot — reveals on **"aligned"@96.30**
- **v4-rev2 MID-BEAT MOTION — closes the 7.4s internal lull (defect #11).** v4 had a dead 7.4s gap from P2@88.92 → P3@96.30 with no new element inside the supposed showpiece. v4-rev2 fills it with a sequence of subtle **NEUTRAL "confirm" ticks/checkmarks** that stamp onto the PRINCIPAL rows as the model is described (each a small `#F0F0F0` check/tick that scales in `back.out(2)`, 0.25s, on the right edge of its row — NOT cyan):
  - tick stamps onto **P1** `Quotes a firm PRICE` at ~comp **88.0** (just after it reveals).
  - tick stamps onto **P2** `WAREHOUSES THE RISK` at **"gradually"@92.36** (a REAL spoken word landing squarely in the old dead gap — "we trade on it very gradually"), so there is a motion event mid-gap instead of 7.4s of stillness.
  - tick stamps onto **P3** `Fully ALIGNED` at **"aligned"@96.30**, simultaneous with the align-sweep below.
- **MID-CENTERPIECE align-sweep (kept from v4) — NEUTRAL:** when P3 `Fully ALIGNED` lands (~comp 96.3), draw a brief **WHITE/`#F0F0F0` underline-sweep that visually connects the AGENCY header to the PRINCIPAL header** (a 0.5s left→right neutral rule under/between the two column headers, `expo.out`), landing the idea "the incentive is aligned across both sides." Together with the staggered rows + confirm-ticks this keeps the eye moving across the ENTIRE 19s centerpiece (no >~3s still stretch). All added marks are **non-cyan** (defect #4) so none competes with the cyan PRINCIPAL header.
- **Cyan discipline:** ONLY the right header `PRINCIPAL` is cyan. Its shimmer is a transient WHITE pass; the align-sweep is WHITE; **the v4-rev2 confirm-ticks are WHITE/`#F0F0F0` (defect #11, non-cyan)**; all dots neutral `#555`; rule neutral; all rows #F0F0F0. At no static instant are two cyan elements present. ✅
- Headers at equal visual height (both single-line, 48px). Bullet rows use `min-width:0; flex:1` so wraps align under the first character.
- **CONTINUOUS-GRAPHIC + extended hold (v4 overlap):** v4 sets this beat to **19.3s** (= 19.0 logical + 0.3 overlap; ends comp 99.8). **Move the as-built exit fade from local 18.0 (comp 98.5) to local 19.0 (comp 99.5)** so the columns HOLD until c1b8's eyebrow (@ comp 99.65) and cross-fade comp 99.5→99.8. `data-start="80.5" data-duration="19.3"`. Mode-A throughout.
- **R4 (audited clean after v4 fixes):** eyebrow `TWO EXECUTION MODELS`, headers `AGENCY`/`PRINCIPAL`, subs `RIVAL DESKS`/`WINTERMUTE`, rows A1 `Trades on the client behalf` / A2 `Holds no position` / A3 `Incentives can diverge` / P1 `Quotes a firm PRICE` / P2 `WAREHOUSES THE RISK` / P3 `Fully ALIGNED` — **"RISK" now appears once (P2 only); no notable word repeats within the beat.** ✅
- `<!-- WORD-SYNCED: AGENCY@82.68 (rows staggered 83.1/84.0/85.0, #11) PRINCIPAL@84.62(+WHITE shimmer) firm-PRICE@87.76 WAREHOUSES-RISK@88.92 +confirm-tick@gradually-92.36 (#11) ALIGNED@96.30(+NEUTRAL align-sweep+tick) (src−239.10) · ONE cyan = PRINCIPAL header (dots+ticks+sweep all neutral) · P1=Quotes a firm PRICE (R4) · holds to 99.8 (0.3s overlap) · NO INDEX -->`

### c1b8 — flowchart (3-node decay chain, HORIZONTAL) · comp 99.5–106.7 · src 338.60–345.80 · MODE-A · WORD-SYNCED
Catalog **`flowchart`** rendered as a **left→right HORIZONTAL cause→effect chain** (axis deliberately distinct from c1b5's VERTICAL split and c1b7's columns — the *payoff* of the comparison, showing WHY principal incentives align). The as-built is already a horizontal 3-node `→` chain — **keep the horizontal axis** (do NOT let it default to c1b5's vertical skin). Jasper: *"We warehouse that risk and then we trade on it very gradually… a lot of people in the market generally **appreciates** that **alignment** of incentives."*
**R6 FIX:** delete `<div id="b8-idx">07</div>` (line 24), its `#b8-idx` CSS, its tween.
- Eyebrow `WHY IT ALIGNS` — Inter 700, 32px, #F0F0F0 — @ comp 99.65 (the c1b7→c1b8 hand-off entry; fast ≤0.15s entry).
- Node 1 `WAREHOUSE THE RISK` pops @ comp 100.1 — #F0F0F0 (left).
- Connector arrow `→` Node 2 `WORK OFF GRADUALLY` @ comp 100.9 — #F0F0F0 (center).
- Connector arrow `→` Node 3 (accent) `PRICE IMPACT MINIMIZED` — **#00D4FF** (right; its `b8-accent` border/glow + the `b8-arrow-accent` arrow are one cyan focus) — reveals on **"appreciates"@103.44** (held; "alignment"@104.70 lands during its glow).
- Cyan: final node (+ its incoming accent arrow) only — single cyan focus. ✅
- **CONTINUOUS-GRAPHIC (v4 overlap):** v4 sets this beat to **7.5s** (= 7.2 logical + 0.3 overlap; ends comp 107.0). After the final node lands (~comp 103.9), the chain HOLDS until c1b9's eyebrow (@ comp 106.85); exit cross-fade comp 106.7→107.0. `data-start="99.5" data-duration="7.5"`. Mode-A.
- **R4 check:** Node 1 `WAREHOUSE THE RISK` shares "RISK" with c1b7's P2 but that is **cross-beat** (allowed); within c1b8 the three nodes share no notable word ("RISK" appears once, in node 1). ✅
- `<!-- WORD-SYNCED: final-node@103.44 (appreciates) / alignment@104.70 (src−239.10) · HORIZONTAL chain (keep axis) · single cyan = final node · holds to 107.0 (0.3s overlap) · NO INDEX -->`

### c1b9 — kinetic-type · CLOSE · comp 106.7–113.2 · src 345.80–352.30 · **MODE-A** · WORD-SYNCED · CONTENT CLOSE
Clip ends on the substantive one-sentence summary — NOT a name/CTA card. Host: "So in one sentence…" Jasper: *"…it's **helping people** **enter** and **exit** **positions** very **smoothly**."* **Plays in Mode-A** (kinetic builds in the left zone, Jasper framed right) — a full-frame flip here would be a sub-8s segment = R1 FAIL, so the view stays Mode-A through the end. (c1b9 has no index in the build — confirm none is added.)
**v4-rev2 STRENGTHENS THE CLOSE (defect #9):** v4's cyan payoff was `AND EXIT POSITIONS` — accurate but "positions" is a flat noun that doesn't land the clip's thesis (aligned incentives → smoother execution). v4-rev2 makes the cyan payoff Jasper's literal FINAL word **`SMOOTHLY`** — the emotionally resonant beat that ties the whole alignment argument together. **VERIFIED:** "smoothly,"@src 351.78 exists in audio.json (it was just past the v4 src_out 350.40), so **src_out extends 350.40 → 352.30** to capture it. "…enter and exit positions" becomes the neutral setup line; `SMOOTHLY` lands alone as the cyan payoff.

| on-screen line | transcript word(s) | src_t | **comp_t (fire)** | color |
|---|---|---|---|---|
| `HELP PEOPLE` | "helping" (→ "people"@108.92) | 347.68 | **108.58** | #F0F0F0 |
| `ENTER & EXIT` | "enter" (→ "exit"@110.54) | 348.52 | **109.42** | #F0F0F0 |
| `POSITIONS` | "positions" | 349.90 | **110.80** | #F0F0F0 |
| `SMOOTHLY` *(payoff, #9)* | "smoothly" | 351.78 | **112.68** | **#00D4FF** payoff + glow |

- Eyebrow `THE MODEL, IN ONE LINE` — Inter 700, 32px, #F0F0F0 — @ comp 106.85 (top-left of the left zone, above the stack; fast entry within the overlap from c1b8).
- Phrase build: `fromTo({opacity:0,y:28},{opacity:1,y:0},expo.out,0.28s)`; the cyan payoff `SMOOTHLY` adds `scale:0.92→1` + glow. **The neutral lines build helping@108.58 → enter&exit@109.42 → positions@110.80 and STAY; then there is a brief held beat (the spoken "very" @ src 350.54) and the cyan `SMOOTHLY` fires on "smoothly"@112.68, finishes its ~0.32s entry by comp ~113.0, then HOLDS until the comp ends @ 113.2 (~0.2s tail).** Phrases STAY full-opacity through clip end (no dim, no exit drift). No CTA / end-card.
- `data-start="106.7" data-duration="6.5"` *(v4-rev2: was 4.6 — extended for the `SMOOTHLY` payoff)*. Cyan: `SMOOTHLY` only. Lines ~110px (Mode-A left zone is narrower than full-frame; `ENTER & EXIT` at ~96px so it never wraps; `SMOOTHLY` is a single word so it sits large). **No +0.3s overlap — nothing follows; holds to clip end.**
- **R4:** `HELP PEOPLE` / `ENTER & EXIT` / `POSITIONS` / `SMOOTHLY` — no shared notable word. ✅
- `<!-- WORD-SYNCED close: helping@108.58 enter@109.42 positions@110.80 smoothly@112.68 (src−239.10) · v4-rev2 payoff = SMOOTHLY (real final word, src_out→352.30, #9) · single cyan = SMOOTHLY · NO INDEX (none in build) -->`

---

## GSAP TIMELINE (master) — phase map (ONE view transition @ comp 32.4)

Geometry `MODE_A={left:1229,top:108,width:614,height:864}`, `object-position:85% center`.

> **BUILD DIRECTIVE:** The ONLY view call is a single `toModeA(32.4)`. There is **no** `toFull` anywhere after the head, and **no** `toModeA` other than the one at 32.4. (v3's switch was at 30.2; v4 moves it to 32.4 so it lands exactly as c1b5's graphic enters → no blank-left reveal.) Update the as-built `masterTL.to(v,…)` view tween from `30.2` to `32.4`, the glow/rule from `30.5/30.6` to `32.7/32.7`, and **replace** the single Ken Burns tween `(duration:81.1 … ,30.2)` with the **v4-rev2 two-stage sequence** (1.0→1.03 over 32.4→~70, then 1.03→~1.015 over ~70→113.2; defect #12).

- **PHASE 0 — FULL-FRAME, comp 0.0–32.4.** CSS default full-frame video (both speakers) — **no view call**. c1b1 cold open (0–6, eyebrow@0.15 → lead `IN FIVE YEARS`@0.62 → `ANOTHER CAREER`@2.58 → cyan `IN AN INDUSTRY`@4.24; defect #8) → [full-frame breath 6–9.4] → c1b3 kinetic (9.4–~20.8, lingers over the dropped c1b4 lead-in, #10) → c1b4 clean host-Q (~21.2–32.4, NO overlay). Dark left-gradient backdrop fades in under each kinetic stack and out after it; the video stays full-frame the whole phase (no Mode-A between the kinetics — R1 grouping; breaths are full-frame both-speakers — R7).
- **PHASE 1 — TRANSITION @ comp 32.4.** FULL-FRAME → Mode-A (`expo.inOut`, 0.7s). `#bg-glow` in @ 32.7; `#zone-rule` draws @ 32.7; the two-stage Ken Burns begins and runs across the entire Mode-A hold. **c1b5's eyebrow tween (comp 32.55) fires DURING this reframe**, so the left graphic is present as the switch completes — the switch never shows an empty left zone (R7). c1b5's root node `THE FIRM` pops with the v4-rev2 stronger overshoot @ comp 33.2 (defect #10).
- **PHASE 2 — MODE-A holds, comp 32.4–113.2 (continuous graphic, 0.3s overlaps).** c1b5 (32.4–50.2) → c1b6 (49.9–59.0) → **c1b6c (58.7–69.8, NEW)** → c1b6b (69.5–80.8) → **c1b7 centerpiece (80.5–99.8, with staggered AGENCY rows + mid-beat confirm-ticks, #11)** → c1b8 (99.5–107.0) → c1b9 close (106.7–113.2, ends on `SMOOTHLY`, #9). Consecutive beats OVERLAP by 0.3s (incoming starts before outgoing unmounts) so the left zone is never empty (CONTINUOUS-GRAPHIC RULE). No view switch. Ends in Mode-A. Two-stage Ken Burns runs to comp 113.2.

`#short_mag_cut_frame` video `data-duration="113.2" data-media-start="239.10"`; audio identical. Master `data-duration="113.2"`. *(v4-rev2: all three were 111.3 — extended +1.9s for the `SMOOTHLY` close, #9.)*

**Ken Burns (v4-rev2 two-stage, defect #12):** instead of one linear ramp, a 2-tween sequence over comp 32.4→113.2 (80.8s total), `ease:"power1.inOut"` on each: (1) `vid scale 1.0 → 1.03` from comp 32.4 → ~70.0; (2) `vid scale 1.03 → ~1.015` from comp ~70.0 → 113.2. A breathe-in/breathe-out, not a monotonic creep. (The as-built has a single 81.1s linear tween from 30.2 — replace it with this 2-tween sequence starting at 32.4.)

**z-index:3 rule — MUST list every overlay beat id** (else it renders behind the z-index:2 video). For v4, the rule in `index.html` is (v3's 8 ids **plus** the new c1b6c). **Update the comment above this rule from "exactly these 8 ids" to "9 ids (added c1b6c)":**
```css
/* z-index:3 — 9 ids (v4 added c1b6c); every overlay beat MUST be listed or it renders behind the video */
#beat-c1b1-half-decade,
#beat-c1b3-moving-fast,
#beat-c1b5-two-sides,
#beat-c1b6-jasper,
#beat-c1b6c-execution-scope,
#beat-c1b6b-edge,
#beat-c1b7-agency-principal,
#beat-c1b8-warehouse,
#beat-c1b9-enter-exit { z-index: 3; }
```
**Added:** `#beat-c1b6c-execution-scope`. Add a `<div id="beat-c1b6c-execution-scope" … data-composition-src="compositions/beat-c1b6c-execution-scope.html" data-start="58.7" data-duration="11.1" data-track-index="3">` to the body (between the c1b6 and c1b6b divs). Re-time the existing beat divs' `data-start`/`data-duration` to the v4 BEAT MAP (including the +0.3s overlap on every Mode-A beat except c1b9). **v4-rev2 deltas to also apply:** c1b3 `data-duration="11.4"` (lingers over the dropped c1b4 lead-in, #10); c1b9 `data-start="106.7" data-duration="6.5"` and master/video/audio `data-duration="113.2"` (extended for `SMOOTHLY`, #9). **Also update the `index.html` `<title>` to end "— v4".**

---

## ON-SCREEN-STRING AUDIT (R3 jargon + R4 duplicates + R6 index) — machine-checked

**R6 (no index):** after the build edits, `grep -rn ">0[1-8]<" clip-1-otc-model/compositions/` MUST return **0 matches** (currently returns 6 — listed in BUILD STATE). The BEAT MAP "on-screen text" column contains no index numerals — eyebrow editorial labels only. ✅ (gate must verify this exact grep)

**R3 (jargon):** every string scanned against `_JARGON.md` blacklist (`burp`, `deep in`, `graft`, `stake rate`, `meme con`, `insaturable`, `dime terminal`) → **0 hits**. Brand/term spellings exact: `Wintermute`, `OTC desk`, `PRINCIPAL` (the finance term, remapped from Whisper's "principle"), `BTC`, `ETHEREUM`, `SOLANA`. ✅

**R4 (no duplicate notable word within a beat):** per-beat scan (stopwords + ≤2-char words excluded) → **0 dup in every beat after the v4 fixes**:
- **c1b6c:** eyebrow `ASSET COVERAGE` (NOT `WHAT THEY EXECUTE`) so it does not share "execut*" with payoff `WE HANDLE THE EXECUTION`. Pills `BTC/ETHEREUM/SOLANA/LONG TAIL` share nothing with each other or the payoff. ✅
- **c1b6b:** eyebrow `OUR EDGE` (NOT `PRICING EDGE`, which would share "PRICING" with Bar 2 `BEST PRICING`; and NOT `EXECUTION EDGE`, dropped to cut cross-beat "EXECUTION"). Bars `MINIMIZE MARKET IMPACT` / `BEST PRICING` + footnote `Algorithms + proprietary tech` share no notable word with `OUR EDGE` or each other. ✅
- **c1b7 — RISK dedup (v4 catch):** as-built P1 `Quotes a RISK PRICE` + v4 P2 `WAREHOUSES THE RISK` would BOTH contain "RISK" → within-beat dup = R4 FAIL. **Fix: P1 → `Quotes a firm PRICE`** (drops "RISK"). Then P2 `WAREHOUSES THE RISK` is the only "RISK" in the beat. Eyebrow `TWO EXECUTION MODELS`, headers `AGENCY`/`PRINCIPAL`, subs `RIVAL DESKS`/`WINTERMUTE`, rows A1/A2/A3/P1/P2/P3 — **no notable word repeats within the beat.** ✅
- **c1b5:** no footer (no "two/firm" dup with eyebrow `TWO SIDES OF THE BOOK`). ✅
- **c1b6 (v4-rev2):** eyebrow `WINTERMUTE` vs sub **`Heads the OTC desk`** — no shared notable word. *(The candidate `Runs Wintermute's OTC desk` was rejected: it would repeat "Wintermute" from the eyebrow = within-beat dup. `Heads the OTC desk` keeps the OTC-desk tie-back with zero shared word, #9.)* ✅
- **c1b8:** nodes `WAREHOUSE THE RISK` / `WORK OFF GRADUALLY` / `PRICE IMPACT MINIMIZED` — no notable word repeats within the beat ("RISK" appears once, in node 1). ✅
- **c1b1 (v4-rev2):** lead `IN FIVE YEARS` / `ANOTHER CAREER` / `IN AN INDUSTRY` — no shared notable word ("in" is a stopword). ✅
- **c1b9 (v4-rev2):** `HELP PEOPLE` / `ENTER & EXIT` / `POSITIONS` / `SMOOTHLY` — no shared notable word. ✅

> **Cross-beat note (resolved):** "EXECUTION" previously appeared in THREE Mode-A strings within ~40s (c1b6c payoff `WE HANDLE THE EXECUTION`, c1b6b eyebrow `EXECUTION EDGE`, c1b7 eyebrow `TWO EXECUTION MODELS`). v4 changes **c1b6b's eyebrow to `OUR EDGE`**, leaving "EXECUTION" in only c1b6c's payoff and c1b7's eyebrow (the two-models framing, where it belongs). "RISK" appears across c1b7 P2 + c1b8 node 1 (cross-beat, allowed) but only ONCE within any single beat.

---

## VERIFICATION CHECKLIST (graded gate — every item)

- **R6 NO INDEX (top priority):** zero `01`..`08` index strings in any composition file (`grep -rn ">0[1-8]<" clip-1-otc-model/compositions/` → 0, currently 6); on-screen chrome = eyebrow labels only; `index.html` `<title>` says "v4" and z-index comment says "9 ids". ✅ (build must DELETE all six idx elements + CSS + tweens, and relabel index.html)
- **R7 NO BLANK-LEFT (top priority):** Mode-A block (32.4–111.3) has a left-zone graphic at EVERY instant — seven beats OVERLAP by 0.3s (incoming starts before outgoing unmounts; R7 PROOF table); each beat holds full-opacity through (boundary + 0.3s) and cross-fades the next entry (CONTINUOUS-GRAPHIC RULE, v4 hardened); the NEW c1b6c fills the v3 9.5s hole; the switch @32.4 lands as c1b5 enters. No cropped-Jasper-with-empty-left instant AND no 1-frame hand-off flash. ✅
- **R1 view discipline:** ONE transition (FULL@0–32.4 → MODE-A@32.4–111.3). No segment <8s outside intro (32.4s, 78.9s); no A-B-A within 12s (impossible with one switch); consecutive graphics grouped per view. View-timeline + R7 table included. ✅
- **R2 template variety:** max 2 kinetics in a row (`[2,1]`); distinct lead device = Agency-vs-Principal swiss-grid + the only shimmer-sweep; not kinetic-dominated (2 of 9 graphic beats are kinetic); the NEW c1b6c is a COMMITTED asset-pill row (a third distinct form — not bars, not a card; kinetic count unchanged); two flowcharts on DIFFERENT axes (c1b5 vertical split, c1b8 horizontal chain — both confirmed in as-built); 9 graphic beats; no two identical templates adjacent except the permitted 2-kinetic opener. ✅
- **R3 jargon:** every on-screen string passes `_JARGON.md` (0 hits); `PRINCIPAL` remapped from Whisper "principle". ✅
- **R4 duplicate words:** 0 within-beat notable-word repeats — c1b6c eyebrow=`ASSET COVERAGE`; c1b6b eyebrow=`OUR EDGE`; **c1b7 P1=`Quotes a firm PRICE`** (resolves the P1/P2 "RISK" dup). ✅
- **R5 opening coherence:** `ANOTHER CAREER / IN AN INDUSTRY` is a complete thought (crypto becomes just-another-career); cyan payoff `IN AN INDUSTRY` is a real phrase. ✅
- **DESIGN.md opening conflict (defect #6):** explicitly reconciled — the full-frame-kinetic open supersedes DESIGN.md's "speaker-right-from-t=0 / 3-elements / 0.08s" sub-rules for this side-by-side project (see OPENING-MODEL RECONCILIATION). NOT an un-acknowledged FAIL. ✅
- **Name card (defect #7):** documented as a mid-clip speaker-ID (fires @ comp 49.9 over a live speaker describing his role), NOT an intro card; the only on-audio name is "Wintermute"@26.78 (pre-switch, cannot host a Mode-A card). ✅
- **Dialog-match + open-on-line:** src_in=239.10; c1b1 fires on Jasper's actual words another@2.58 / industry@4.24 (audio.json ground truth); eyebrow `WINTERMUTE · OTC` paints @ comp 0.15 (first-text by 0.3s) since the `HALF A DECADE` lead was dropped to tighten the hook; NO anticipatory hook (deliberately did NOT pull the later risk-price reveal forward — QA §3); NO index on screen. ✅
- **Every kinetic/reveal line fires at `comp_t = src_t − 239.10`**, read off audio.json word objects (re-verified for this v4 — delta 0.00 on every line), quoted per line. c1b6c pills are TRUE word-sync (BTC@58.94 / ETHEREUM@59.46 / SOLANA@59.88 / tail@63.24). Close payoff (c1b9 `AND EXIT POSITIONS`@comp 110.54) has ≥0.4s tail headroom (entry completes ~110.86, holds to 111.3). ✅
- **Framing:** `object-position:85% center` (as-built), Ken Burns 1.0→1.03 over comp 32.4–111.3 (78.9s), no hard zoom; re-confirm by frame at src 285 & 330 before render. ✅
- **One cyan per beat (defect #4 enforced):** b1 IN AN INDUSTRY · b3 HAVEN'T SEEN THIS/IN YEARS · b5 OTC-DESK node · b6 accent bar (b6-rule neutralized) · b6c WE HANDLE THE EXECUTION line · b6b BEST PRICING bar · **b7 PRINCIPAL header ONLY** (dots neutralized, align-sweep neutral, shimmer is white) · b8 final node · b9 AND EXIT POSITIONS. At no static instant does any beat show two cyan elements. ✅
- **No outro:** name card mid-clip (c1b6 @ comp 49.9); clip ends on c1b9 content kinetic. Dates: no numerals, "this/prior" only (c1b3 payoff is now `HAVEN'T SEEN THIS / IN YEARS` — no "year prior" phrasing). Palette/type: eyebrows Inter 700 ≥32px #F0F0F0; body Inter ≥600; muted secondary #B6BEC6 (never #888); cards solid `rgba(20,26,34,0.92)`+cyan bar+glow, NO blur/grain. ✅
- **VERIFY-BY-FRAME (mandatory, build stage) — MID-BEAT + BOUNDARY frames:** after draft render, extract and LOOK at each. **MID-BEAT** (content correct): comp 0.6 (open — eyebrow on, NO kinetic word yet, NO "01"), 3.0 (`ANOTHER CAREER`), 12.0 (c1b3 payoff `HAVEN'T SEEN THIS/IN YEARS`), 47.0 (c1b5 accent node, NO "02"), 55.0 (name card, NO "03"), **62.0 (NEW c1b6c — confirm pills word-synced + left zone filled, was blank in v3)**, 73.0 (edge chart eyebrow=`OUR EDGE`, NO "05"), **90.0 (centerpiece — P1=`Quotes a firm PRICE`, P2=`WAREHOUSES THE RISK`, NO "06", and CYAN-COUNT = 1 = PRINCIPAL header only, NO cyan dots)**, **97.0 (align-sweep on `ALIGNED` — confirm the sweep is WHITE/neutral, cyan-count still 1)**, 104.0 (decay node, HORIZONTAL, NO "07"), 110.9 (close payoff held). **BOUNDARY frames** (catch a 1-frame blank-left at hand-offs): **comp 32.9 (the view switch — c1b5 already on left, NO blank), 50.0 (c1b5→c1b6), 58.85 (c1b6→c1b6c), 69.65 (c1b6c→c1b6b), 80.65 (c1b6b→c1b7), 99.65 (c1b7→c1b8), 106.85 (c1b8→c1b9)** — confirm the left zone is NEVER empty across any swap. Confirm overall: (1) NO index counter anywhere; (2) Mode-A left zone never empty (mid-beat AND at every boundary); (3) overlays ABOVE video (z-index); (4) Jasper centered+named; (5) cyan-count = 1/frame at EVERY frame (special attention to c1b7 @90.0/@97.0).

## BUILD MANIFEST ROW
`clip_1 | clip-1-otc-model | 239.10 | 350.40 | kinetic-type,flowchart×2(vert+horiz),pill-row,data-chart(bars),swiss-grid+shimmer+NEUTRAL-align-sweep | 9 graphic beats + 1 clean | object-position:85% | 1 view transition @32.4 | NO index (title=v4) | continuous-graphic Mode-A 0.3s overlaps (0 blank-left) | c1b7 ONE cyan (dots neutral, sweep neutral) | name card = mid-clip ID (not intro)`
