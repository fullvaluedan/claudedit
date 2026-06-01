# Restream Clips — Graphics Plan
# Guest: Jasper De Maere (Wintermute OTC Desk)
# Host: Nic (Paradigm / Paradex)
# Audience: Institutional Crypto Traders

## Source Video Layout
Side-by-side split: Nic left, Jasper right. Both full-frame cams.
Lower-third name burns already in source: "Nic" + "Jasper De Maere / Wintermute"

## Overlay Design System
- Canvas: 1920×1080, 30fps
- Panel zone: y=740, h=340, full-width (overlays both speakers safely)
- Panel bg: rgba(10,10,10,0.88) — dark, readable, not full-opaque
- Accent: #00D4FF — ONE element per scene (the key stat or eyebrow label)
- Text: #FFFFFF headlines, #F0F0F0 body, #888888 muted labels
- Font: Inter 800 headlines, Inter 700 numbers, Inter 600 sub, Inter 400 labels
- Monospace labels: JetBrains Mono 400
- Dividers: #2A2A2A
- Animation: panel slides up from bottom (0.5s expo.out), content staggers in

---

## Clip 1: "Altcoin Options 3.5× YoY" 
**Timestamps**: 6:35–9:04 (149s) | absolute: 395–544s
**Hook**: Wintermute's OTC data reveals altcoin options notional is growing 3.5× YoY — family offices, asset managers, and UHNWIs are all coming in.

### Scene 1 (clip t=22s–53s, absolute 7:00): 3.5× Stat
- Eyebrow [JetBrains Mono, #00D4FF]: "WINTERMUTE OTC DESK · 2025 H1"
- Big number [Inter 800, 120px, #FFFFFF, count-up 1.0→3.5]: "3.5×"
- Label [Inter 600, 48px]: "MORE ALTCOIN OPTIONS NOTIONAL"
- Sub-label [Inter 400, 32px, #888888]: "vs. same period 2024"
- Animation: count-up from 1.0× over 1.4s (power3.out), panel slides from bottom

### Scene 2 (clip t=54s–139s, absolute 7:29): Who's Buying
- Eyebrow [JetBrains Mono, #00D4FF]: "INSTITUTIONAL DEMAND"
- Headline [Inter 800, 72px]: "WHO'S TRADING ALTCOIN OPTIONS"
- Three rows stagger in (80ms apart):
  · "Family Offices" | "Asset Managers" | "Ultra-HNW Individuals"
- Each row: Inter 600 48px, preceded by #00D4FF dash
- Sub [#888888 32px]: "Trend: yield via covered calls, not just directional bets"

### Scene 3 (clip t=140s–149s, absolute 8:55): Why (Yield Angle)
- Eyebrow [JetBrains Mono, #888888]: "THE TRADE"
- Two columns:
  - Left: "HIGH IMPLIED VOL" (Inter 700, 54px, #FFFFFF)
  - Center: "→" (#00D4FF)
  - Right: "COVERED CALL YIELD" (Inter 700, 54px, #FFFFFF)
- Sub: "Altcoin IV still elevated → compelling passive APY" (#888888)

---

## Clip 2: "October 10 Post-Mortem: ADL Cascade"
**Timestamps**: 16:20–18:30 (130s) | absolute: 980–1110s
**Hook**: Delta-neutral dealers got wiped by ADL — a cascade most traders didn't understand. 25× leverage ratio exposed.

### Scene 1 (clip t=32s–64s, absolute 16:52): ADL Mechanism
- Eyebrow [JetBrains Mono, #00D4FF]: "OCT 10 POST-MORTEM"
- Headline [Inter 800, 64px]: "THE ADL CASCADE"
- 5-step flow (each step slides in sequentially, 0.3s apart):
  "LONG SPOT + SHORT PERP" → "PRICE DROPS" → "PERP DEEPLY ITM" → "ADL CLOSES PERP" → "NAKED LONG DELTA"
- Steps: Inter 600 36px #F0F0F0, arrows in #2A2A2A, last step in #FF4D4F (negative)

### Scene 2 (clip t=65s–115s, absolute 17:25): Naked Delta Forced Sell
- Eyebrow [JetBrains Mono, #888888]: "FEEDBACK LOOP"
- Left column: "DEALERS" [Inter 800 56px]
  Sub: "Long spot + short perp = delta neutral" [#888888 30px]
- Right column: "POST-ADL" [Inter 800 56px, #FF4D4F]
  Sub: "Naked long delta → forced sellers" [#888888 30px]
- Divider: vertical line #2A2A2A

### Scene 3 (clip t=116s–130s, absolute 18:15): 25× Leverage
- Eyebrow [JetBrains Mono, #00D4FF]: "MARKET STRUCTURE"
- Count-up number: "25×" [Inter 800 120px #FFFFFF, count from 1×]
- Label: "DERIVATIVES vs. SPOT VOLUME" [Inter 600 48px]
- Sub: "The BTC $226K rally was built on this leverage" [#888888 32px]
- Sub2: "Duration of max stress: 30–45 minutes" [#16C784 28px]

---

## Clip 3: "Retail Rotated to Equities — ETF Flows Self-Fulfilling"
**Timestamps**: 19:10–21:40 (150s) | absolute: 1150–1300s
**Hook**: JP Morgan prime brokerage retail at ATH equity positioning. Crypto vol compressed to equity vol levels — retail follows the volatility.

### Scene 1 (clip t=5s–57s, absolute 19:15): JP Morgan Data
- Eyebrow [JetBrains Mono, #00D4FF]: "JP MORGAN PRIME BROKERAGE · MAY 2026"
- Headline [Inter 800, 80px]: "RETAIL EQUITY ACTIVITY"
- Stat: "ALL-TIME HIGH" [Inter 800 96px #FFFFFF]
- Sub: "by a meaningful margin (JPM prime brokerage data)" [#888888 32px]

### Scene 2 (clip t=58s–120s, absolute 20:08): Vol Rotation
- Eyebrow [JetBrains Mono, #888888]: "WHY RETAIL LEFT CRYPTO"
- Two columns:
  Left [card]: "CRYPTO VOL" [Inter 700 54px] + ↓ + "COMPRESSED" [#FF4D4F]
  Right [card]: "EQUITY VOL" [Inter 700 54px] + ↑ + "RISING" [#16C784]
- Center label: "Retail follows the risk-on vol trade" [#888888 36px]
- Bottom sub: "#00D4FF accent → only crypto will re-attract once vol reprices"

### Scene 3 (clip t=121s–150s, absolute 21:09): ETF Self-Fulfilling
- Eyebrow [JetBrains Mono, #00D4FF]: "ETF FLOW DYNAMICS"
- Headline [Inter 800 72px]: "SELF-FULFILLING OUTFLOWS"
- Two bullet items:
  · "Institutions: sticky (slow to exit)"
  · "Retail: spivy (rotate in/out via ETF)"
- Sub: "ETF outflows create their own selling pressure cycle" [#888888 32px]

---

## Clip 4: "4-Year Halving Cycle — Dead?"
**Timestamps**: 23:40–25:20 (100s) | absolute: 1420–1520s
**Hook**: Hot take — Bitcoin block rewards becoming negligible. The halving's mechanical market impact is fading. Only the narrative remains.

### Scene 1 (clip t=8s–100s, holds entire clip): Halving Dead
- Eyebrow [JetBrains Mono, #00D4FF]: "HOT TAKE"
- Headline [Inter 800 96px]: "4-YEAR CYCLE"
- Sub-headline [Inter 800 72px, strikethrough animation]: "DEAD?"
- Three bullet items stagger in (0.5s apart):
  · "Block rewards → negligible" [#F0F0F0]
  · "Miner sell pressure → irrelevant" [#F0F0F0]
  · "Narrative persists > fundamentals" [#888888]
- Right side: small decay curve (SVG drawn via clip-path) showing halving epochs

---

## Clip 5: "AI Collapsed My Research Team — 1 Trader > 2-3 Analysts"
**Timestamps**: 27:13–29:30 (137s) | absolute: 1633–1770s
**Hook**: Jasper does research that would require 2-3 people — alone, with AI. Night and day vs. 5 years ago.

### Scene 1 (clip t=12s–43s, absolute 27:25): Day-to-Day Impact
- Eyebrow [JetBrains Mono, #00D4FF]: "AI IMPACT ON TRADING RESEARCH"
- Three items slide in:
  · "TASK MANAGEMENT" [Inter 600 40px]
  · "DATA PROCESSING" [Inter 600 40px]
  · "CROSS-SOURCE ANALYSIS" [Inter 600 40px]
- Label: "ALL collapsed into one workflow" [#888888 32px]

### Scene 2 (clip t=44s–137s, absolute 27:57): Team Compression
- Eyebrow [JetBrains Mono, #888888]: "PRE-AI vs. TODAY"
- Left: "2–3 ANALYSTS" [Inter 800 80px, #FF4D4F]
  Sub: "required for same research output" [#888888 28px]
- Center: "=" [Inter 400 80px, #2A2A2A] (with arrow: → #00D4FF)
- Right: "1 TRADER + AI" [Inter 800 80px, #16C784]
  Sub: "Jasper De Maere, Wintermute OTC" [#888888 28px]
- Animated: left panel fades in, then arrow draws, then right panel fades in

---

## Clip 6: "VTFs — The On-Chain Programmable ETF"
**Timestamps**: 31:20–33:50 (150s) | absolute: 1880–2030s
**Hook**: VTFs (Vault Traded Funds) are the crypto-native ETF. Permissionless, programmable, any strategy. Wintermute just went live as vault curator.

### Scene 1 (clip t=6s–74s, absolute 31:26): ETF vs VTF Comparison
- Eyebrow [JetBrains Mono, #00D4FF]: "DEFI INNOVATION"
- Two columns:
  Left header: "ETF" [Inter 800 64px, #888888]
  Right header: "VTF" [Inter 800 64px, #FFFFFF]
  - "Centralized" vs "Permissionless"
  - "Fixed basket" vs "Any strategy"  
  - "Regulated gatekeeping" vs "On-chain composable"
  - "TradFi access only" vs "Accessible to anyone"
- Right column has #00D4FF left border accent

### Scene 2 (clip t=75s–150s, absolute 32:35): Wintermute Live
- Eyebrow [JetBrains Mono, #888888]: "WINTERMUTE VAULT CURATOR · MORPHO"
- Headline [Inter 800 80px]: "2 WEEKS OLD"
- Sub: "High take rates, risk-adjusted returns" [#F0F0F0 42px]
- Detail: "Demand: OTC clients asking Wintermute to manage capital" [#888888 32px]
- Source [JetBrains Mono 26px #888888]: "Source: Jasper De Maere, Wintermute"

---

## Clip 7: "Institutional Edge: Options, Not Spot — Delta-1 Is Commoditized"
**Timestamps**: 14:28–16:00 (92s) | absolute: 868–960s
**Hook**: Delta-1 is fully transparent on-chain. Institutions' real edge is options — structured vol positions that retail can't yet replicate.

### Scene 1 (clip t=20s–92s, holds most of clip): Delta-1 vs Options Edge
- Eyebrow [JetBrains Mono, #00D4FF]: "INSTITUTIONAL ALPHA MAP"
- Left column: "DELTA-1 / SPOT"
  Items: "On-chain settlement visible" | "Retail tracks within hours" | "Edge: MINIMAL" [#FF4D4F]
- Right column: "OPTIONS"
  Items: "Greeks-based structures" | "Vol surface expertise" | "Yield via writing" | "Edge: SIGNIFICANT" [#16C784]
- Vertical divider #2A2A2A
- Bottom sub: "Perp vol last year: institutions surprised by retail catching up" [#888888 30px]

---

## Clip 8: "Accumulation Zone — But Not 2021 Rising Tide"
**Timestamps**: 42:22–44:05 (103s) | absolute: 2542–2645s
**Hook**: Jasper says 12-18 month risk/reward is "screaming attractive." BUT: it's not 2021. Rising tide won't lift all boats. Selective is mandatory.

### Scene 1 (clip t=8s–56s, absolute 42:30): 12-18 Month Horizon
- Eyebrow [JetBrains Mono, #00D4FF]: "RISK/REWARD ANALYSIS · MAY 2026"
- Headline [Inter 800 96px]: "12–18 MONTHS"
- Sub: "risk/reward screaming attractive" [Inter 600 52px #F0F0F0]
- Caveat [#888888 32px]: "bottom timing: extremely difficult to call"
- Small label [JetBrains Mono #888888 24px]: "Jasper De Maere, Wintermute OTC Desk"

### Scene 2 (clip t=57s–103s, absolute 43:19): Not 2021
- Eyebrow [JetBrains Mono, #888888]: "CYCLE COMPARISON"
- Left column: "2021" [Inter 800 72px, #888888]
  Sub: "Rising tide lifts all boats" [#888888 36px]
  Bottom: "✓ Buy everything" [#888888]
- Right column: "2026" [Inter 800 72px, #FFFFFF]
  Sub: "Not enough capital for all alts" [#F0F0F0 36px]
  Bottom: "→ Be selective" [#00D4FF]
- Diagonal strikethrough on 2021 column (scaleX animation from left)

---

## Rendering Plan
Each composition rendered as:
- ProRes 4444 MOV (transparent-capable) for Premiere compositing
- 1920×1080 @ 30fps
- Lower-third panel only (no video embedded) → drop on V2 in Premiere

OR alternatively:
- H.264 MP4 with video embedded → standalone shareable clips

Both options available post-build.
