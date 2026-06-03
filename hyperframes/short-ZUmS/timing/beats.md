# short-ZUmS — Ground-truth beat table

Source: YouTube Short `ZUmS00hezgU` — "How She Taught an AI to Write Cantonese Lyrics"
Hong Kong AI Podcast EP11, guest Jenny Wong (founder, Cantolyrics.ai).
Audio is **Cantonese**; the **burned-in subtitles are English** (center-bottom band) — DO NOT cover them, DO NOT duplicate them.
Source 608×1080 30fps 40.1s → render at **1080×1920** (full-frame b-roll, cover).

Timings derived from per-second caption sampling (frames/sheet_*.jpg). Caption band ≈ y 1065–1565 of 1920 → keep all graphics ABOVE y≈1000 (left column) or in the TOP band (y<440, clear sky above her head). Her body/hands occupy right-center and occasionally lower-left below y≈1000.

| beat | start | end  | spoken (EN sub)                                              | supporting graphic (white Swiss) | zone |
|------|-------|------|-------------------------------------------------------------|----------------------------------|------|
| gA   | 0.0   | 5.8  | I approached it through 0243 — the core of my whole AI.      | HERO: 0243 tone-contour reveal + "THE 0243 SYSTEM / 粵語九聲" | LEFT col |
| gB   | 5.8   | 8.8  | So I asked the 0243 godfather, Master Wong Chi-wah:          | Dossier name card "THE 0243 GODFATHER · 黃志華" | LEFT upper |
| gC   | 8.8   | 11.8 | was my whole idea just wrong?                               | Doubt stamp "WRONG?" / HYPOTHESIS UNVERIFIED | LEFT |
| gD   | 11.8  | 16.8 | Applying 0243 to an AI — was it even right?                 | LLM failure grid: GPT·CLAUDE·GEMINI → TONE-MATCH ✗ FAILED | TOP strip |
| gE   | 16.8  | 21.8 | He told me so much. We'd met once, talked for hours.        | Field log: 1 MEETING · HOURS OF TALK | LEFT |
| gF   | 21.8  | 24.8 | He kept showing me how to simplify it.                      | SIMPLIFY: many rules → one (reduction) | LEFT |
| gG   | 24.8  | 29.8 | In the end I found a dead-simple mapping — just one sentence.| ONE SENTENCE payoff panel | TOP/mid wide |
| gH   | 29.8  | 32.8 | I could teach the AI what 0243 is.                          | TEACH: sentence → [ AI ] node | LEFT |
| gI   | 32.8  | 36.8 | And it worked. Suddenly — like magic.                       | ✓ IT WORKED → spark | LEFT/top |
| gK   | 36.8  | 40.1 | The AI just got it.                                         | CANTOLYRICS.AI brand lockup + contour mark | LEFT lower |

Persistent chrome (chrome.html, 0–40.1): top identity row "HONG KONG AI PODCAST · EP.11" + "0243 / CANTOLYRICS" mono, thin red progress rule, corner registration crosshairs. Subtle — b-roll leads.

## Design tokens (white Swiss grid)
- paper:  #F6F4EE (warm white, 0.95 alpha)   ink: #14110D   ink-soft: #4A463E
- accent: #E5392B (Swiss vermillion — ONE per frame, also auspicious red)
- display font: Inter (800/900), tight tracking on numerals
- meta font: 'JetBrains Mono', ui-monospace, Menlo, monospace — uppercase, +0.14em tracking
- corners: SHARP (border-radius 0). Edge = 2px ink border + hard offset shadow (8px 8px 0 rgba(0,0,0,.16)), NO blur.
- rules animate scaleX 0→1. Numerals tabular-nums.

## 0243 system (correct content)
0243 = Cantonese lyric-tone notation by lyricist/scholar Wong Chi-wah (黃志華). Maps the relative
pitch of Cantonese syllables to four levels so lyrics "sing right" against a melody.
Pitch levels (low→high): 0 (lowest) · 2 · 3 · 4 (highest). The motif "0 2 4 3" is plotted as a
melodic CONTOUR (not a sorted ladder) — that non-monotonic shape is the visual hook.
