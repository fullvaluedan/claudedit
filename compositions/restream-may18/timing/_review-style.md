Now I have a very complete picture. Let me deliver the full per-clip assessment.

---

## EDL Review — restream-may18 Social Clips

### Preliminary: Transcript Verification Summary

Word timings in the EDL are largely accurate against audio.json. Key confirmed timings:
- "half" = 239.72, "decade" = 240.10, "career" = 241.90 — Clip 1 c1b3 offsets correct
- "warehouse" = 328.02, "risk" = 328.80, "incentive" = 332.24 — Clip 1 c1b6 correct
- "pivoted" = 1135.84, "aggressively" = 1137.10, "equity" = 1138.08 — Clip 5 hook correct
- "two" = 1682.00, "three" = 1683.68 — Clip 8 hook correct
- "blue wave" = 1807.70, "short" = 1815.68, "oil" = 1816.12 — Clip 8 c8b7 correct

---

## Clip 1 — OTC Model / Crypto as Career (220s–350s, 130s)

**Hook phrase: "CRYPTO IS JUST / ANOTHER CAREER / IN AN INDUSTRY"**

WEAK. This is a soft landing as an opener. The hook fires BEFORE Jasper says the line, which means it reads as the author editorializing — not as a confirmation punchline. The real punchline in this window is beat 4: "WE WAREHOUSE THAT RISK" is fresher, more specific, and signals something the audience has never heard before. A Wintermute principal-model hook would stop a finance-native scroller; a generic "crypto is a career" hook is too broad and gets scrolled past.

**Recommended replacement hook:** "WE WAREHOUSE / THAT RISK / PRICE IS INCENTIVE" (c1b6 language). This is unique to the Wintermute model, not available anywhere else, and forces an explanation. Alternatively: "WE OWN / EVERY FILL" from the principal-model concept.

**Pacing issue — c1b4:** A 14s clean window from t=24–38s is 4s over the dead-air ceiling (DESIGN.md: FAIL if dead air >4s without a graphic). The spec allows a clean window for breathing room, but this one abuts right after the swiss-grid at c1b2 ends at ~15s and there's another 9s of kinetic at c1b3 (15–24s). Actually the sequence is: c1b3 kinetic ends at 23.8, c1b4 clean starts at 24, ends at 38. That is 14 consecutive seconds with zero graphic. With a pacing audience on mobile, this will cause drop-off at the 30s mark before the decision-tree at c1b5 fires. Trim this window to 6–8s max, or fire the decision-tree earlier (pull c1b5 to t=30).

**c1b8 is straight filler.** "WE WAREHOUSE RISK / INCENTIVE" fires at t=99 — this is a direct repeat of c1b6 from t=60–76 (same vocabulary, same three-line structure, same cyan payoff word "INCENTIVE"). The spec says no same template twice in a row, but this beats that with the same CONTENT twice. Replace with the strongest unused line from the window: "WE OFFER THE PRICE / WE OWN THE FILL" (distinct from the warehouse line). Or drop this beat entirely and extend c1b7's swiss-grid by 8s — the clip does not need padding here.

**c1b9 (liquid-glass name card at 116s):** The DESIGN.md says "Every name-drop has a Liquid Glass Card." Jasper's name was dropped at the episode start (beat 1 in edl.json). This closing card is superfluous in a social clip because the DESIGN.md hard rule says no outros — and a name card at the very end of a clip functions as an outro regardless of label. The spec prohibits it. Remove it. If a Jasper card belongs anywhere in Clip 1, it belongs at t=3s as part of the swiss-grid eyebrow, not as the last 14 seconds.

**QA Pre-Check claim for Opening 6s:** The EDL claims this PASSES, but re-read: c1b1 is kinetic full-frame at 0.08s, and it says "Mode A transition begins" at t=3.0, then c1b2 fires with index+eyebrow. The DESIGN.md opening rule requires the SPEAKER to be visible from t=0 on the RIGHT — but c1b1 is marked "full-frame (both speakers)" which means the video is not repositioned into Mode A from the first frame. The speaker is there, but not in the framed 40% right zone. This is a technical FAIL against the spec: "Video animates to its framed position (Mode A or B)" is supposed to happen at t=0.3–1.0, during the kinetic hook. The EDL implies it doesn't happen until t=3.0. The builder should be instructed to animate into Mode A during c1b1 (speaker reframes right at t=0.3–0.6 while kinetic holds), so the visual expectation is set immediately.

**Verdict:** Rework the hook, cut c1b4 to 6s, replace c1b8 content, remove c1b9. This is 4 actionable edits before build.

---

## Clip 3 — Structured Products (700s–810s, 110s)

**Hook phrase: "AUTOCALLABLES / IN CRYPTO / NOW."**

STRONG. "Autocallables" is an unfamiliar word to most of the TikTok/Twitter finance audience — it produces a "what is that?" pause reflex, which is exactly what you want. "NOW." as a single-word cyan payoff lands with finality. This hook will stop a finance-native scroll. Keep it.

**Window start issue:** The clip starts at src 700s, but the transcript shows 700–703 is "Yeah. Yeah, yeah. I think we're definitely, I was also..." — seven filler words before any substance. That's fine for a kinetic hook that fires before/over the speech, but the hook phrase "AUTOCALLABLES IN CRYPTO NOW" doesn't appear until src ~721s. The hook is verbatim from beat 8 which is src 714–737. The comp offset is correct (c3b1 fires hook immediately at comp t=0 before Jasper reaches that line at src 721). This works as an anticipatory hook. The "NOW." payoff lands at comp t=1.60 while Jasper is still in the preamble — the audience hears the word arrive at ~src 721 and the graphic is already up. This is valid per spec: "pull the strongest phrase from seconds 5–15 of the transcript." Flag for builder: the kinetic hook is sourced from later in the window, so c3b1 is an editorial statement, not a word-sync.

**c3b5 — 18s clean window (43–61s):** Acceptable. The window earns its space (Jasper explains why crypto vol makes autocallables attractive). At 18s this is technically under the dead-air ceiling since the spec says "minimum 2s gap between graphics" not a max of 4s. However for a clip under 90s, 18s of no graphic at t=43–61 is one-sixth of the total runtime with nothing on screen. Consider firing a supplemental kinetic at t=52 using "CRYPTO VOL / STILL ELEVATED / DEMAND FORMING" sourced from the explanation passage around src 743–755. This would split the clean window into two 9s halves and maintain tension.

**c3b7 phrase: "PRICE / CREATES NARRATIVE / NARRATIVE CREATES PRICE"** — this is among the cleanest, most quotable lines in the entire episode. The EDL has it correct. But the c3b7 timing claim says it fires at comp t=76–88 with "src ~787." The transcript confirms "price creates narrative" actually lands at src 784.78 (price), 784.78 (creates), 785.12 (narrative). For Clip 3, src_in = 700, so comp t = 784.78 - 700 = 84.78. But the beat map shows c3b7 starts at comp t=76. There is an 8-second gap between c3b6 (decision-tree ends at 76) and when the actual spoken words land at comp t=84.78. This means c3b7 either fires the kinetic 8 seconds early (as an anticipatory statement) or there's a timing error. The builder must be flagged: verify whether c3b7 is intended to fire early (editorial mode like c3b1) or sync to spoken words. If sync, move c3b7 start to comp t=84 and adjust c3b6 exit accordingly.

**"TAKE RATES / MEANINGFULLY / HIGHER" (c3b9):** Transcript confirms "take rates" src 796.06, "meaningfully" src 798.54, "higher" src 799.04. Comp offsets: 796.06 - 700 = 96.06, 798.54 - 700 = 98.54. The EDL places this at c3b9 comp t=99–110. The word "take" lands at comp 96.06, not 99.1 — the EDL is 3 seconds late on this sync. Fix: fire "TAKE RATES" at comp t=96.06, "MEANINGFULLY" at 98.54, "HIGHER" at 99.04.

**Verdict:** Strongest hook in the series. Three targeted timing fixes before build. Consider splitting c3b5 clean window.

---

## Clip 4 — Oct 10 Crash (1010s–1115s, 105s)

**Hook phrase: "25 TIMES MORE / DERIVATIVES / THAN SPOT"**

STRONG. Hard number, unexpected scale, forces an explanation. The finance audience's gut reaction is "that can't be right" — which means they watch. Keep it.

**c4b3 spoken claim:** EDL says "ADL" fires at comp 15.46 synced to src 1023.46. Transcript at 1013.46 shows "something that happens" — the word "ADL" doesn't appear until much later. Let me clarify: the ADL concept is described at beat 11 in the source edl.json (in_secs 1012.5). The spoken window for clip 4 starts at src 1010. The speech around src 1023–1031 per the transcript is "something that happens, which threw a lot of..." (1013.16–1014.76) and then the content continues. The word "ADL" does not appear to be spoken verbatim in the 1010–1040 window — the concept is described but using the term "perpetual futures" and "delta." The builder must not fire a kinetic with "ADL" as if it's word-synced, because that word may not be uttered in that window. Verify against the full transcript; if "ADL" isn't spoken, the kinetic must be editorial (like c3b1) and labeled as such, or reworded to match what is actually spoken ("SHIFTS YOUR / DELTA / COMPLETELY").

**c4b4 decision-tree runs 20 seconds (26–46s):** This is the longest single beat in the clip. A 6-step decision-tree with 0.3s stagger per node = all 6 nodes visible after ~1.8s — you then hold a fully-revealed static diagram for 18+ seconds. That's a dead-air problem with graphics present. The decision-tree needs to either (a) be trimmed to 4 steps (the original edl.json beat 11 flow is 6 steps, so compress to the key 4) or (b) have supplemental kinetic text interleaved within the beat. Best option: trim the 6-step flow to 4 steps ([ADL Fires] → [Naked Long Delta] → [Forced Sellers] → [Alts -60/70/80%]) which captures the causal chain without the preamble, and move the beat to comp t=30–45 freeing 4s before and after.

**c4b6 — "ALTS DOWN / 60, 70, 80 PERCENT / FEEDBACK LOOP":** The transcript confirms alts language appears around src 1066–1075 (after the cascade description). For Clip 4 with src_in = 1010, this is comp t=56–65 range, not the t=62–78 the EDL places it. Check that the clean window c4b5 (46–62) is actually clear speech — the transcript at src 1056–1072 shows the cascade description is still ongoing. Verify this window doesn't cut off mid-explanation.

**c4b8 callback kinetic:** "25 TIMES / MORE DERIVATIVES / THAN SPOT" at t=93–105 is a direct word-for-word repeat of the hook (c4b1). This is a structural callback technique that works when there's substantive development in between — and there is (20s of ADL explanation). However at 105s total this clip is the second shortest in the set. The callback eats 12s of the final 12s with no new information. Replace with a forward-looking close: "LEVERAGE IS / THE AMPLIFIER / NOT THE CAUSE" (a synthesis the audience can take away) or use the actually spoken line from src ~1110: "melt up to 226K was built on this leverage." That's a concrete synthesis rather than a hook repeat.

**Verdict:** Hook is excellent. Three timing/content fixes needed. The clip is mechanically sound but the ending is weak.

---

## Clip 5 — Capital Rotation (1120s–1300s, 180s)

**Hook phrase: "RETAIL PIVOTED / AGGRESSIVELY / INTO EQUITIES"**

ADEQUATE but not the strongest possible. The word "aggressively" is doing all the work here. More magnetic for finance Twitter: "THE MARGINAL / RISK DOLLAR / WENT INTO EQUITIES" — this is the thesis-level statement from beat 15 (src 1186), a Wintermute Weekly verbatim that signals this is institutional-grade analysis, not casual commentary. The JPMorgan data confirmation from beat 14 would then land as a surprise inside the clip rather than being telegraphed in the hook.

**At 180s this is the longest clip in the set.** Social media retention data suggests clips over 150s on LinkedIn/Twitter lose roughly 40% of viewers by the midpoint without a structural re-hook. The EDL provides one at c5b5/c5b6 (t=51–88s) with the pull-quote, which is well-placed. But c5b7 is an 18s clean window immediately after a 20s decision-tree (c5b6, 68–88s). That's 38s of relatively low-density content from t=68–106s — the 70s mark is where you'll see the biggest drop. Insert a supplemental kinetic at t=88 (the start of c5b7) rather than going straight to clean video. The host question about "what brings retail back to crypto" is actually a compelling on-screen moment if it's treated as a kinetic word stack from the host side: "WHAT BRINGS / RETAIL BACK / TO CRYPTO?" (per DESIGN.md: "Host questions are fine as their own stack"). This would convert 18s dead air into an engagement prompt.

**c5b11 — "NOT ENOUGH CAPITAL / FOR EVERYTHING / TO PUMP":** The transcript search shows the exact phrase in the window (src 1282–1300) is NOT "not enough capital for everything to pump." What's actually spoken around that range is about volatility trade and equity markets offering it. The phrase "not enough capital for that to happen" doesn't appear in the 1282–1300 window — src beat 29 in edl.json (2599s) has "Not enough capital for that to happen." This is a wrong-window attribution. The clip ends at src 1300 and there is no "pump" language anywhere near there. c5b11 as written is fabricated content. Replace with the actual last strong line in the window: the DESIGN.md thesis-relevant synthesis from the vol comparison. Best option: fire a closing kinetic at t=162 sourced from src ~1295: "THEY JUST WANT / A VOL TRADE" (spoken: "they don't really care about the underlying, they just want to have a volatility trade around") — this closes the rotation loop cleanly and is word-verified.

**c5b9 kinetic:** "CRYPTO VOL / COMPRESSED / EQUITY VOL RISING" — the transcript confirms these exact words land at src 1270.62 (volatility/crypto), 1271.94 (compressed), and equity context around src 1295. Comp offset: 1271.94 - 1120 = 151.94. The EDL places this at comp t=125–143, which maps to src 1245–1263 — that's 8–10 seconds too early for the "compressed" word. Fix: fire this kinetic at comp t=151 to align with the spoken words.

**Verdict:** Content selection is correct and thesis-aligned throughout. Fix c5b11 (wrong window), fix c5b9 timing, convert c5b7 clean window into a host kinetic. Consider whether this clip should be 150s instead of 180s — the last 30s (c5b10 + c5b11) don't add new information.

---

## Clip 6 — 4-Year Cycle Dead? (1350s–1470s, 120s)

**Hook phrase: "4-YEAR CYCLE / IS IT / DEAD?"**

STRONG. Question hooks perform consistently well on finance Twitter because they create an immediate information gap. "DEAD?" as a single cyan word is aggressive. This is the correct hook for this window. The transcript confirms the host actually asks "Would you say the four year cycle is dead?" at src 1420.84–1422.32. Since the clip starts at src 1350, the word "dead" lands at comp t=72, not in the opening. The hook is editorial (fires before the question is asked), which is valid per DESIGN.md: "pull the strongest phrase from seconds 5–15 of the transcript." Keep it.

**c6b2 — stat "3.125 BTC" in the Swiss grid:** The stat should be "3.125 BTC" (current halving reward, 2024 cycle). The EDL correctly identifies this. However the date label in the footer says "2028: 1.56 BTC" — this should be the NEXT halving reward that makes the argument, not the current one. Consider making the Swiss-grid stat "1.56 BTC" (the 2028 forward stat that makes the miner-pressure-irrelevant case, since that's the argument Jasper is making) and move "3.125 BTC" to the sublabel as context. The punchline is where it's going, not where it is.

**c6b3 — decision-tree with epoch table:** The epoch table rows per the EDL show "decaying opacity" per row — but DESIGN.md says "Never use muted grey (#888888) for any text smaller than 48px" and the epoch table rows are in JetBrains Mono which will be smaller than 48px. Decaying opacity creates exactly this problem: later rows will be small muted-grey text. This is a hard rule violation. Instead of decaying opacity, use a descending-size approach (2012 row largest, 2028 row smallest) or use consistent opacity with a different accent strategy. The 2028 row should be the BRIGHTEST (cyan), not faded, since it's the thesis payoff.

**c6b6 kinetic — "FOUR YEAR CYCLE / BECOMING / MEANINGLESS":** Transcript around src 1420–1430 shows the host asking if it's dead (src 1421), Jasper responding "I've been going on record multiple times thinking that it was dead." The word "meaningless" appears in the source edl.json beat 18 spoken text: "becoming increasingly meaningless as block rewards half." Comp offset for this would be src ~1443 → comp t = 1443 - 1350 = 93, not the t=73 the EDL places it. Check: the EDL's c6b6 is sourced from "beat 18 core spoken line" but the spoken word "meaningless" lands at comp t=93, not t=73. The beat fires 20 seconds before the word is spoken. Either (a) this is editorial mode (acceptable if labeled), or (b) there's a 20s timing error. Given the clip window is src 1350–1470 and beat 18 in edl.json has in_secs=1420, the relevant language starts at comp t=70, which aligns with c6b6 at t=73. This is plausibly correct. Flag for builder to word-sync on render.

**Overall clip structure:** The three decision-tree beats (c6b3, c6b5 at t=55–73, and the template sequence) work well together. The epoch-table beat is the most visually distinctive in the series — nothing else has a mono data table. Keep it.

**Verdict:** Hook is excellent. Two targeted fixes (stat direction, epoch table opacity rule violation). Timing on c6b6 needs builder flag.

---

## Clip 7 — What Kills Bear Markets (1515s–1600s, 85s)

**Hook phrase: "WE ALWAYS EXIT / BEAR MARKETS / WITH A NEW NARRATIVE"**

ADEQUATE. "We always exit bear markets with a new narrative" is a true statement that most finance people already believe — it doesn't force a stop-scroll. A stronger version of this hook uses the specificity of the examples: "ORDINALS. / DEFI SUMMER. / WHAT'S NEXT?" — three words that function as pattern recognition for crypto-native audiences, with the question creating the information gap. Alternatively, "PRIVACY / AND AI / ARE NEXT." (sourced from beat 20) is more declarative and more provocative.

**The clip is 85s — the second shortest in the set.** At 6 beats with 3 full-frame kinetics, this is spare. The content does not support expansion (it ends at src 1600 and the next topic starts at src 1675 — 75s gap that belongs to other content). The clip is correctly bounded. However c7b5 (liquid-glass card, 54–71s) shows "PRIVACY" and "AI" as two stacked 130px words with a Jasper attribution — this is fundamentally a Liquid Glass Card used as a Kinetic Word Stack replacement. The attribution line "Jasper De Maere · Wintermute" at the bottom makes this a soft outro. Remove the attribution line — the eyebrow already establishes this is Jasper's take. Per DESIGN.md: "No outros." A name at the bottom of the penultimate beat reads as a closing credit.

**c7b3 decision-tree timeline:** The EDL claims "inscriptions" fires at comp 27.0 synced to src 1542. The transcript confirms "inscriptions" at src 1543.76 — comp offset = 1543.76 - 1515 = 28.76, not 27.0. Close but off by 1.76s. "AI agents" fires at comp 35.0 synced to src 1550 — transcript shows "AI" at src 1550.82, offset = 35.82. These are within 1–2s which is acceptable for a decision-tree beat (not word-sync precision), but the builder should use the correct offsets.

**Thesis filter check:** Bears, narratives, ordinals, AI, privacy — all of this is forward-looking market structure analysis. This passes the Web4/governance/AI-fairness thesis filter cleanly.

**Verdict:** Change hook to "PRIVACY / AND AI / ARE NEXT." Remove attribution from c7b5. Minor timing corrections for decision-tree. Clip is correctly sized.

---

## Clip 8 — AI Multiplier (1675s–1845s, 170s)

**Hook phrase: "ONE TRADER / DOING THE WORK OF / 2–3 ANALYSTS"**

EXCELLENT. This is the strongest hook in the entire set. It's quantified, it's personal (first-person from a credible source), and it's directly relevant to every finance professional watching. The "2–3 ANALYSTS" cyan payoff in numbers is visually punchy. The transcript confirms "two" at src 1682.00, "three" at src 1683.68. At comp t=1.60, src = 1675 + 1.60 = 1676.60 — the hook fires before Jasper reaches this line (he says it at src ~1682). This is editorial pre-fire, same technique as clip 3. Valid. Keep the hook exactly as written.

**c8b5 — 18s clean window (50–68s):** The AI research task automation detail is genuinely substantive. However, the transcript shows that around src 1725–1743 (comp 50–68s), Jasper is discussing how AI changes the research process. This is prime kinetic territory — this is exactly the "strong sentence with a strong verb" situation where the spec says to fire a Kinetic Word Stack. A supplemental kinetic at t=58 using "RESEARCH / AND TRADING / SIMULTANEOUSLY" would convert 10s of this window without cutting the explanation. The clean window can shrink to 8s (comp 50–58) and the kinetic fills 58–68.

**c8b9 kinetic — "AN AGENT NEEDS / TO CONTROL RISK / UNDERSTAND YOUR PROFILE":** Transcript confirms "agent" at src 1826.88, "control risk" at 1828.34, "risk profile" at 1830.20. Comp offsets: 1826.88 - 1675 = 151.88, 1828.34 - 1675 = 153.34, 1830.20 - 1675 = 155.20. The EDL places this at comp t=124 with lines firing at 124.3, 126.1, 128.0 — that's 27–28 seconds early. This is a major timing error, not editorial pre-fire. At comp t=124 (src ~1799), Jasper is still discussing infrastructure requirements, not yet at the "agent needs to control risk" line. Either (a) move c8b9 to comp t=151 and adjust surrounding beats, or (b) source c8b9 from an earlier line that actually occurs at src ~1799. What's spoken at src 1799 ("high quality data, I think, to be able to allow agents to express risk") would work as a different kinetic: "HIGH QUALITY / DATA / TO ALLOW AGENTS" at comp t=124–138 using src 1799.90, 1803.56.

**c8b7 — "BLUE WAVE / STRAIT OF HORMUZ / SHORT OIL":** Transcript confirms "blue wave" at src 1807.88, "Hormuz" at src 1812.06, "short oil" at src 1815.68. Comp offsets: 1807.88 - 1675 = 132.88, 1812.06 - 1675 = 137.06, 1815.68 - 1675 = 140.68. The EDL places this at comp t=86–106 with fires at 86.1, 88.2, 90.5 — that's 47 seconds early. This is the most significant timing error in the entire EDL. The "Blue Wave" example occurs at src ~1808, not src ~1761. The surrounding beats need to be restructured: c8b7 should move to comp t=132–148. This cascades: c8b8 and c8b9 also need to move, and c8b6 decision-tree (comp t=68–86) would need to be followed by additional content to fill the gap until comp t=132. Specifically, the src 1761–1808 window (the 47s between c8b6 and when "Blue Wave" is actually spoken) needs beats inserted. The transcript shows src 1761–1795 contains Jasper discussing pre-ChatGPT vs. today's AI tools — a supplemental kinetic at comp t=86: "NIGHT AND DAY / DIFFERENCE / FROM 5 YEARS AGO" (src ~1705–1708) or from the actual src 1795 window: "YOU NEED / A LOT OF / INFRASTRUCTURE" (src 1796.46–1797.30).

**c8b11 callback — "I'M DOING RESEARCH / AND TRADING / AT THE SAME TIME":** Transcript confirms "I'm doing research AND I'm trading" at src 1691.12–1692.14. Comp offset = 1691.12 - 1675 = 16.12. This line occurs at the START of the clip window, not the end. The EDL places this callback at comp t=162, which is src ~1837 — but Jasper doesn't say "doing research and trading" again at src 1837. The transcript at src 1837–1845 shows "I think it makes a lot of sense. I don't think we're that far off." This callback at t=162 is built on a word that was spoken 145 seconds earlier in the clip. That's a valid editorial callback technique IF the builder sources it from the earlier spoken instance (comp t=16.12) and treats it as a designed echo, making clear in the build notes it's an intentional replay, not a word-sync.

**Verdict:** Best hook in the series. Major timing error on c8b7 (47s off) and c8b9 (27s off) must be corrected before build — these would produce kinetics that visually precede the spoken content by nearly a minute. Convert c8b5 partial-clean to kinetic. The clip is structurally the strongest in the set once the timing errors are resolved.

---

## Cross-Clip Assessment

### Q1: Hook strength ranking
1. Clip 8 — "ONE TRADER / DOING THE WORK OF / 2–3 ANALYSTS" — EXCELLENT, keep
2. Clip 3 — "AUTOCALLABLES / IN CRYPTO / NOW." — STRONG, keep
3. Clip 4 — "25 TIMES MORE / DERIVATIVES / THAN SPOT" — STRONG, keep
4. Clip 6 — "4-YEAR CYCLE / IS IT / DEAD?" — STRONG, keep
5. Clip 7 — "WE ALWAYS EXIT / BEAR MARKETS / WITH A NEW NARRATIVE" — ADEQUATE, replace with "PRIVACY / AND AI / ARE NEXT."
6. Clip 5 — "RETAIL PIVOTED / AGGRESSIVELY / INTO EQUITIES" — ADEQUATE, replace with "THE MARGINAL / RISK DOLLAR / WENT INTO EQUITIES"
7. Clip 1 — "CRYPTO IS JUST / ANOTHER CAREER / IN AN INDUSTRY" — WEAK, replace with "WE WAREHOUSE / THAT RISK / PRICE IS INCENTIVE"

### Q2: Pacing assessment
Four dead-air violations to address: Clip 1 c1b4 (14s), Clip 3 c3b5 (18s in a 110s clip), Clip 5 c5b7 (18s post-decision-tree), Clip 8 c8b5 (18s). The 4s ceiling isn't in DESIGN.md verbatim but "no dead air >4s" appears in the review prompt — worth clarifying: the spec says "minimum 2s gap between graphics," not a maximum. However the 14–18s clean windows in Clips 1, 3, 5, 8 will cause measurable retention drop on short-form platforms where the average viewer decides in 8–12s whether to continue. Practical recommendation: cap any single clean window at 8s in clips under 120s.

### Q3: Series visual variety across openers
All 7 hooks are kinetic-type full-frame. Per DESIGN.md this is explicitly permitted ("every strong phrase = kinetic-type") but visually the openers look identical. The series benefits from having at least one non-kinetic opener. Clip 6 ("4-YEAR CYCLE DEAD?") could open with the epoch table visual on the left + kinetic on the right, which would be a distinctive frame-1 that differentiates it in a playlist thumbnail context.

### Q4: Clip length assessment
- Clip 5 at 180s is borderline too long for the content density. Trim to 150s by ending at src 1270 (after the vol comparison, before the retail follow-on explanation). The last 30s (c5b10 decision-tree + c5b11) adds a structural re-iteration without new information. Ending at "The marginal risk dollar went into equities, not crypto" (src ~1194) as the thesis statement is a cleaner out-point.
- Clip 7 at 85s is correctly sized.
- Clip 4 at 105s could be trimmed to 90s by cutting the clean window c4b5 from 16s to 8s and adjusting c4b6 entry.

### Q5: Thesis filter compliance
All 7 clips pass the thesis filter. Clips 1 (market structure), 3 (institutional adoption), 4 (market mechanics), 5 (capital flows), 6 (cycle theory), 7 (narrative formation), 8 (AI trading) are all Web4/governance/market-structure content. No crypto gossip, no book backstory, no personal biography beyond beat 21's "I'm doing research AND I'm trading" which is the thesis point itself.

### Q6: Weak beats (filler that doesn't earn a graphic)
- **c1b8** (Clip 1, t=99–116): Verbatim repeat of c1b6 vocabulary. Replace or drop.
- **c1b9** (Clip 1, t=116–130): Functions as an outro. Remove per hard rules.
- **c4b8** (Clip 4, t=93–105): Hook callback with no new information. Replace with synthesis line.
- **c5b11** (Clip 5, t=162–180): Wrong-window content attribution. Replace with verified line.
- **c8b7 timing** (Clip 8): Not a weak beat but a 47s timing error that makes an otherwise excellent beat structurally broken. This is the highest-priority fix in the entire EDL.

---

## Priority Fix List (Ordered by Impact)

1. **Clip 8 c8b7 timing error** — "Blue Wave" fires at src 1808, not src 1761. Move beat to comp t=132. Fill comp t=86–132 with new content from src 1761–1808 window.
2. **Clip 5 c5b11 wrong attribution** — "NOT ENOUGH CAPITAL FOR EVERYTHING TO PUMP" is not in the src 1282–1300 window. Replace with verified line.
3. **Clip 8 c8b9 timing error** — "AN AGENT NEEDS TO CONTROL RISK" fires at src 1827, not src 1799. Shift beat 27s later.
4. **Clip 1 hook replacement** — Replace "CRYPTO IS JUST / ANOTHER CAREER" with "WE WAREHOUSE / THAT RISK / PRICE IS INCENTIVE."
5. **Clip 1 c1b9 removal** — Name card at clip end violates no-outro rule.
6. **Clip 1 c1b4 trim** — 14s clean window to 6–8s max.
7. **Clip 3 c3b9 timing** — "TAKE RATES" fires at comp 96.06, not 99.1.
8. **Clip 6 epoch table** — Remove decaying opacity (hard rule violation on small text). Make 2028 row cyan, not faded.
9. **Clip 5 hook replacement** — "THE MARGINAL RISK DOLLAR WENT INTO EQUITIES" is stronger.
10. **Clip 7 hook replacement** — "PRIVACY / AND AI / ARE NEXT." is more declarative.

## Overall Series Verdict

**Structurally PASS with targeted fixes before build.** The template sequencing discipline is excellent across all 7 clips — no two identical templates in a row, no intro/outro cards, cyan discipline is correctly specified. The source material selection is on-thesis throughout. The primary risks are: (a) two significant timing errors in Clip 8 that would produce graphics visually decoupled from the spoken content by 30–47 seconds, (b) one wrong-window content attribution in Clip 5, and (c) three weak beats that should be replaced before build investment is made. Fix items 1–3 from the priority list before any rendering begins — they affect structural integrity. Items 4–10 are quality improvements that can be addressed in the EDL pass without blocking build start.