# REMOTION-PROMPT-CATALOG.md — Community Prompt Reference
# claudedit / [Your Channel Name]
# Version: 1.0
# Source: https://www.remotion.dev/prompts (Pages 1 & 2)
# Last scraped: May 2026

---

## HOW TO USE THIS FILE

These are real community-built prompts from the Remotion showcase.
Use them as **inspiration and structural templates** — not copy-paste.
Adapt each one to your brand using DESIGN.md before running.

**When to call Remotion vs HyperFrames:**
- Call **Remotion** for: 3D effects, complex React animations, data-driven visualizations, multi-scene product demos, canvas effects
- Call **HyperFrames** for: captions, lower thirds, stat callouts, simple overlays, section breaks
- When in doubt: HyperFrames is simpler and faster to iterate

---

## CATEGORY INDEX

| Category | Prompts |
|---|---|
| 🗺️ Maps & Data | Travel Route, Rocket Timeline, Strava Run, Real Estate, BMS Animation |
| 📰 Text & Typography | News Headline, Kinetic Marketing, Shape-to-Words, 3D Retro Font, Vignelli-style |
| 🎬 Product & Brand | Product Demo Presscut, Launch Video X, Promo VVTerm, Music CD, Cursor Announcement |
| 🎨 Visual FX | Cinematic Intro, Spinning 3D Logo, Glitch Effect, Magnifying Glass, Vintage Screen |
| 📊 Charts & Data | Bar+Line Chart, NYT Graph style, Audio Spectrum |
| 🌌 Creative/3D | Three.js Games Ranking, Solar System, Shape Transform |
| 🎯 Overlays | Transparent CTA, Lower Third |

---

## PAGE 1 PROMPTS

---

### 01 — Travel Route on Map with 3D Landmarks
**Votes:** 242 | **Tool:** Claude Code | **Model:** Opus 4.5
**URL:** https://www.remotion.dev/prompts/travel-route-on-map-with-3d-landmarks

**What it produces:** Animated map starting over LA, camera zooms out, then a route line animates from LA → NY → Paris, with a 3D Eiffel Tower rendered at the destination.

**Original prompt:**
```
use remotion best practices. make a new composition and add a map and zoom out of LA
while staying focused on it. once done, animate a line from LA to NY and make the 
camera follow it.

add another stop to the trip, this time we go to paris. animate the eiffel tower 
and show it in 3D!
```

**claudedit use case:** Travel/location content, city-specific analysis videos, geography-based segments
**Adaptation notes:** Replace cities with your content's relevant locations. The 3D landmark technique works for any recognizable building (substitute Eiffel Tower with relevant architecture). Keep camera follow pattern — it's clean.

---

### 02 — News Article Headline Highlight
**Votes:** 238 | **Tool:** Claude Code (Opus 4.5)
**URL:** https://www.remotion.dev/prompts/news-article-headline-highlight

**What it produces:** A newspaper screenshot displayed on white background with slow 3D rotation and subtle zoom. A rough.js highlighter marker draws across specific keywords from left to right, appearing behind the text.

**Original prompt:**
```
use remotion best practices. import the following image into the project: 
'~/Desktop/Screenshot.png' use tesseract CLI to do OCR and find the positions of 
the text. in remotion, make a new composition where you load the image and pad the 
article generously on a white full HD background. while the composition is running 
for 5 seconds, slowly, very subtly, zoom into it and slightly rotate the article 
in 3d from left to right. the overall rotation should be around 15deg for each axis. 
at the beginning, blur the whole composition and unblur it over 1 second. after the 
blur is done, evolve a highlighter from left to right using rough.js over the words 
"government shutdown" and "funding lapses". the image has a white background. make 
sure the marker appears behind the text.
```

**claudedit use case:** Referencing news articles, citing research, showing quotes from external sources
**Adaptation notes:** Replace with screenshot of relevant article. Swap highlighted words for the specific claim you want to call attention to. The OCR + rough.js highlighter combo is a signature look — very credible on finance/crypto content.

---

### 03 — Product Demo for Presscut
**Votes:** 183 | **Tool:** Claude Code | **Model:** Claude Opus 4.5
**URL:** https://www.remotion.dev/prompts/product-demo-for-presscut

**What it produces:** A full product demo video replicating the app's UI in React components, showing key features as if a founder were doing a live demo walkthrough.

**Original prompt:**
```
Create a demo video of the Presscut app/product using remotion. Use react components 
to replicate UI elements and replicate the UI of the app as closely as possible. 
The app has a LOT of features/functionality, so take guidance from the marketing 
home page/index for what to highlight, while keeping language simple and to-the-point. 
Really grill me with questions to nail down exactly how the final video should 
look/feel and what content should be there. The ultimate goal is to replicate what 
me, the founder, would be showing/doing with a product demo with a customer.
```

**claudedit use case:** SaaS/tool recommendation segments, app walkthroughs, "tools I use" content
**Adaptation notes:** The key technique is building React mock-UIs rather than using screen recording. Much cleaner output. Tell the agent to scrape your product's homepage for brand colors and copy.

---

### 04 — Launch Video on X
**Votes:** 165 | **Tool:** Claude Code | **Model:** Opus 4.6
**URL:** https://www.remotion.dev/prompts/launch-video-on-x

**What it produces:** Multi-scene 37-second product launch video with terminal animation, app UI mockups, chat interface, feature reveals, and closing CTA. Dark theme with amber accent.

**Original prompt (condensed — full version is very detailed):**
```
Create a Remotion video (1080x700, 30fps, ~37s) for [product]. Dark theme 
(#0c0a09 background, #fbbf24 amber accent). Background music with 1s fade-in 
and 2s fade-out at 40% volume.

Scene 1 — Terminal Install (4s): Terminal window, types install command, shows 
ASCII logo, progressive output lines.
Scene 2 — Home Screen (5s): App window, title, tagline, chat input, spring-
animated fade-in with staggered delays.
Scene 3 — Chat Interface (5.3s): Three-column layout showing key interactions.
[...continues through 8 scenes total]
```

**claudedit use case:** Announcing your own tools, products, or content series launches
**Adaptation notes:** The scene-by-scene specification style is the key technique here. Specify exact frame counts (30fps), exact hex colors, exact scene descriptions. Vague multi-scene prompts produce inconsistent results — be this specific.

---

### 05 — Cinematic Tech Intro
**Votes:** 119 | **Tool:** Gemini | **Model:** k2.5
**URL:** https://www.remotion.dev/prompts/cinematic-tech-intro

**What it produces:** Cinematic-style tech intro with dramatic lighting, text reveals, and high-production motion graphics feel.

**claudedit use case:** Video openers, channel intros, premium B-roll transitions
**Adaptation notes:** The prompt (not fully recovered — page used Gemini/Kimi) focused on premium "cinematic" framing. For Claude Code equivalent: specify "film grain overlay, cinematic color grade, letterbox crop, slow reveals."

---

### 06 — Transparent CTA Overlay
**Votes:** 106 | **Tool:** Claude Code (Opus 4.5)
**URL:** https://www.remotion.dev/prompts/transparent-call-to-action-overlay

**What it produces:** White lower-third that slides up from bottom center showing channel avatar, name, subscriber count, and an animated Subscribe button that transitions from "Subscribe" to "Subscribed" with spring physics. Exported as transparent ProRes.

**Original prompt:**
```
use remotion best practices. use curl scrape youtube to find the avatar and the 
subscriber count. make a white lower third that slides in from the bottom center. 
show the name, subscriber count and avatar. display a typical fixed width black 
youtube subscribe button that changes from "Subscribe" to "Subscribed". use a 
ease-out animation for pressing in the button and a spring animation with a slight 
bounce once the button is released. fade out the lower third. render it as a 
transparent prores video.
```

**claudedit use case:** Subscribe CTAs, end cards, channel promotion overlays
**Adaptation notes:** The ProRes transparent export is the critical detail — it means this drops directly onto your timeline in Premiere with no background. Use this pattern for any overlay you want to composite over footage.

---

### 07 — Rocket Launches Timeline
**Votes:** 97 | **Tool:** Claude Code
**URL:** https://www.remotion.dev/prompts/rocket-launches-timeline

**What it produces:** An animated historical timeline of rocket launches with progressive reveal, data visualization, and event markers. (Prompt text not publicly cached — inferred from video.)

**claudedit use case:** Historical timelines, event sequences, "history of X" segments
**Adaptation notes:** The core pattern: horizontal timeline, events appear progressively left-to-right, each with label + icon/marker. Adapt for: crypto price history, company founding dates, personal milestones.

---

### 08 — Real Estate Investing
**Votes:** 76 | **Tool:** Claude Code | **Model:** Opus 4.5
**URL:** https://www.remotion.dev/prompts/real-estate-investing

**What it produces:** Educational finance explainer video with property data, investment calculations, and animated charts visualizing real estate metrics.

**claudedit use case:** Financial explainers, investment breakdowns, "how X works" educational segments
**Adaptation notes:** Finance/investing content benefits heavily from this style — animated numbers, property cards, ROI charts. Replace real estate data with your topic's metrics.

---

### 09 — Three.js "Top 20 Games Sold" Ranking
**Votes:** 66 | **Tool:** Claude Code
**URL:** https://www.remotion.dev/prompts/threejs-top-20-games-sold-ranking-1

**What it produces:** 3D bar chart race using Three.js showing ranking changes over time for top-selling games, with animated camera movement around the 3D scene.

**claudedit use case:** Ranking visualizations, "top X" content, competitive data comparisons
**Adaptation notes:** The Three.js 3D chart is overkill for most content — use nyt-graph in HyperFrames for 2D. Only reach for this when you specifically want camera-controlled 3D charts for dramatic effect.

---

### 10 — Promotion Video for VVTerm
**Votes:** 47 | **Tool:** Claude Code | **Model:** Opus 4.5
**URL:** https://www.remotion.dev/prompts/promotion-video-for-vvterm

**What it produces:** ~20-second Apple-presentation-style product promo using Inter + Nerd Fonts, pulling assets from the product's website.

**Original prompt:**
```
Make a promotion video in Apple presentation style for VVTerm. Check its website 
VVTerm.com for details and assets like logo. Use nerd fonts and inter. 
Make it around 20 seconds.
```

**claudedit use case:** Short product promos, tool reviews, app spotlights
**Adaptation notes:** "Apple presentation style" is a reliable shorthand the model understands well — clean white/black, large type, slow zoom, product screenshot reveal. Simple prompt, clean output.

---

### 11 — Music CD Store Promo
**Votes:** 45 | **Tool:** OpenCode | **Model:** Kimi K2.5
**URL:** https://www.remotion.dev/prompts/music-cd-store-promo

**What it produces:** 30-second promo video with hook text, logo reveal, animated counter, CD album cards sliding in, artist name labels, and a final CTA section.

**Original prompt (condensed):**
```
Use Remotion best practices skill. Create a 30-second video at 30fps. 
Start with a hook: white text on black background, 'Where do you even buy music 
anymore?' — fade it in, hold for 2 seconds, fade out.

Next section: show the logo from public/logo.png. Use a warm orange gradient 
background. Add a subtle tagline below.

In the next section, add a counter that counts up to 12,000 with a plus sign. 
Label it 'Happy customers'.

Create 5 product cards as abstract gradient cards. Different color combinations. 
Animate them sliding in one by one, arranged in a row. Add labels and details.

[Final section: CTA]
```

**claudedit use case:** Promotional content, product launch hooks, countdown/counter animations
**Adaptation notes:** The counter-up animation is highly reusable — extract this pattern for any stat you want to dramatize. The hook→logo→stat→product→CTA structure is a solid social promo formula.

---

## PAGE 2 PROMPTS

---

### 13 — Shape to Words Transformation
**Votes:** 35 | **Tool:** Gemini | **Model:** k2.5
**URL:** https://www.remotion.dev/prompts/shape-to-words-transformation

**What it produces:** Premium 10-second motion graphics intro where geometric shapes morph/transform into word text, clean white background, particle effects.

**Original prompt (partial):**
```
Create a premium 10-second motion graphics intro using Remotion and React.
Background: Clean white...
[shape morphing to text animation]
```

**claudedit use case:** Logo reveals, brand intros, concept transitions ("chaos → order" visual metaphors)
**Adaptation notes:** Useful for segment transitions where you're introducing a new concept. The shape-to-text morph communicates "things coming together" — good for explainer sections.

---

### 14 — Cursor Agent Skills Announcement
**Votes:** 33 | **Tool:** Cursor
**URL:** https://www.remotion.dev/prompts/cursor-agent-skills-announcement

**What it produces:** Product announcement video for a developer tool feature launch, with code editor UI mockups and feature callout animations.

**claudedit use case:** Tech announcement segments, developer tool content
**Adaptation notes:** Strong reference for "tool announcement within a video" — UI appears, key features highlight progressively, clean tech aesthetic.

---

### 15 — Spinning, Glitching SVG Logo Turned 3D
**Votes:** 28 | **Tool:** Claude Code | **Model:** Opus 4.5
**URL:** https://www.remotion.dev/prompts/spinning-glitching-svg-logo-turned-3d

**What it produces:** Takes an SVG logo, extrudes it to 3D with metallic material using Three.js, adds spin animation and glitch effects.

**Original prompt (partial):**
```
use remotion best practices. create a new composition with the following SVG in 3D. 
add a metallic material to it: <svg...>
then add a spin and glitch effect.
```

**claudedit use case:** Brand intros, logo reveals, visual identity moments
**Adaptation notes:** If you have an SVG logo, this is a one-prompt brand intro. Paste your SVG directly into the prompt. Skip the glitch effect unless your brand aesthetic supports it.

---

### 16 — 3D Retro Pixel Font
**Votes:** 25 | **Tool:** Claude Code | **Model:** Opus 4.6
**URL:** https://www.remotion.dev/prompts/3d-retro-pixel-font

**What it produces:** 1080×1080 8-second animation where 4 colored cursors fly in and collaboratively "build" pixel text block by block, like real-time collaborative code editing.

**Original prompt (partial):**
```
use remotion skills. Create a 1080×1080 brand animation video, 8 seconds, 
black background.

Core effect: Pixel block text-building animation. 4 colored cursors (purple, blue, 
pink, indigo) fly in from off-screen, scatter to four corners, line up on the left 
side, then each cursor "builds" its assigned section of pixel text — blocks light 
up one by one as the cursor passes over them, like multiple people collaboratively 
editing code in real-time.
```

**claudedit use case:** Crypto/tech brand content, channel intros, collaborative theme segments
**Adaptation notes:** The "multiple cursors building text" metaphor works well for content about teams, collaboration, or code. Strong for developer-adjacent or fintech content.

---

### 17 — Strava Run Visualized
**Votes:** 24 | **Tool:** Claude Code | **Model:** Opus 4.5
**URL:** https://www.remotion.dev/prompts/strava-run-visualized

**What it produces:** Animated visualization of a running route from Strava data — map trace, pace data, elevation, animated stats appearing progressively.

**claudedit use case:** Personal data storytelling, fitness content, GPS/route visualizations
**Adaptation notes:** The technique (animate a GPX/JSON data file into a visual story) transfers to any data set — crypto wallet history, trading routes, business metric timelines.

---

### 18 — Audio Spectrum Visualizer
**Votes:** 18 | **Tool:** OpenCode | **Model:** Opus 4.5
**URL:** https://www.remotion.dev/prompts/audio-spectrum-visualizer

**What it produces:** 1920×1080 dark-themed audio waveform/spectrum visualizer that reacts to audio frequency data, animated bars or waveform display.

**Original prompt (partial):**
```
Create a 1920x1080 dark-themed composition called 'AudioSpectrum' featuring an 
audio spectrum visualizer...
```

**claudedit use case:** Podcast clips, music segments, audio-driven B-roll
**Adaptation notes:** Great for podcast/interview content where you want visual interest on a talking-head shot. Render as a loop, composite in Premiere on V2 at reduced opacity.

---

### 19 — The Kinetic Marketing
**Votes:** 17 | **Tool:** Gemini | **Model:** k2.5
**URL:** https://www.remotion.dev/prompts/the-kinetic-marketing

**What it produces:** High-velocity kinetic typography promo with Aurora Glassmorphism aesthetic, 3D floating React logos, depth-of-field blur, rotating radar rings, elastic word-crashing physics.

**Original prompt (partial):**
```
A high-velocity kinetic typography promo for a modern developer tool.

Visual Style: Premium "Aurora Glassmorphism" aesthetic. Backgrounds are seamless, 
breathing radial gradients in Pastel Pink, Lavender, and Soft Blue. Dozens of 3D 
Floating React Logos drift through the scene. Rotating dashed "Radar Rings" add 
technical texture. Color Palette: Electric Azure Blue (#0b84f3) for primary accents. 
Motion Physics: Elastic "Layout Smoothing" — new words crash in and physically push 
existing words...
```

**claudedit use case:** High-energy social promo clips, launch teasers
**Adaptation notes:** ⚠️ This style clashes with the DESIGN.md aesthetic (glassmorphism + pastel gradients are on the anti-patterns list). Reference this for structural technique only — elastic word physics + staggered crashing entries — adapted to your dark palette.

---

### 20 — BMS Active Cell Balancing Animation
**Votes:** 9 | **Tool:** OpenCode
**URL:** https://www.remotion.dev/prompts/bms-active-cell-balancing-animation-8s1p-pack-with-energy-flow-visualization

**What it produces:** Technical engineering animation showing battery cell balancing with energy flow arrows, charge levels animating between cells in an 8S1P pack configuration.

**claudedit use case:** Technical explainers, engineering content, "how X works" with complex diagrams
**Adaptation notes:** The technique — animated energy/data flow between components — transfers to: blockchain transaction flows, API request chains, financial fund flows. Very effective for technical crypto/DeFi content.

---

### 21 — Glitch Effect (HTML-in-Canvas)
**Votes:** 8 | **Tool:** Claude Code | **Model:** Opus 4.7 xhigh
**URL:** https://www.remotion.dev/prompts/glitch-effect-html-in-canvas

**What it produces:** Glitch/distortion effect applied to HTML content rendered inside a Canvas element, with chromatic aberration, RGB channel splitting, and scan line artifacts.

**claudedit use case:** Transition effects, dramatic reveals, cyberpunk/tech aesthetic moments
**Adaptation notes:** Use sparingly as a transition device — 1–2 frames of glitch before a scene cut adds energy without distraction. The HTML-in-canvas technique is useful when you need to apply effects to text that normally can't be post-processed.

---

### 22 — HTML-in-Canvas Magnifying Glass
**Votes:** 6 | **Tool:** Claude Code | **Model:** Opus 4.7 xhigh
**URL:** https://www.remotion.dev/prompts/html-in-canvas-magnifying-glass

**What it produces:** An animated magnifying glass that moves over HTML content, enlarging whatever is beneath it with realistic lens distortion effect.

**claudedit use case:** Highlighting fine print, zooming into documents, "look closer" visual moments
**Adaptation notes:** Excellent for finance content — show a contract, chart, or article screenshot, then animate the magnifier drawing attention to the key line/number. Much more dynamic than a static callout box.

---

### 23 — Vintage Screen Effect (HTML-in-Canvas)
**Votes:** 5 | **Tool:** Claude Code | **Model:** Opus 4.7
**URL:** https://www.remotion.dev/prompts/vintage-screen-effect-html-in-canvas

**What it produces:** CRT monitor / vintage TV screen effect applied to HTML content — scanlines, phosphor glow, screen curvature, noise grain, color bleed.

**claudedit use case:** Retro aesthetic segments, "throwback" moments, historical footage effect
**Adaptation notes:** Use as a filter over archival screenshots or old data to give a "back in 2017" feel. Works well for crypto history content ("what Bitcoin looked like when it was $1,000").

---

### 24 — Solar System Orbit Animation
**Votes:** 4 | **Tool:** Claude Code | **Model:** Opus 4.6
**URL:** https://www.remotion.dev/prompts/solar-system-orbit-animation

**What it produces:** Animated solar system with planets orbiting at correct relative speeds, rendered with realistic gradients and glow effects.

**claudedit use case:** Scientific content, "ecosystem" metaphors, orbital/cyclical data visualization
**Adaptation notes:** The concentric orbit pattern is reusable as a metaphor — substitute planets with companies orbiting a central hub, tokens orbiting a protocol, etc.

---

## PROMPT PATTERN LIBRARY

Extracted techniques from the above prompts that are reusable:

### Pattern A — Scene-by-Scene Spec (from #04)
Specify each scene with: name, duration in frames AND seconds, exact content, exact animation beats.
```
Scene [N] — [Name] ([frames] frames / [X]s)
[Description of what appears]
[Animation: what enters, when, how]
```

### Pattern B — Counter Up (from #11)
```
Add a counter that counts up to [NUMBER] with a [SUFFIX]. 
Animate over [X] seconds using spring interpolation. 
Label it '[LABEL]'.
```

### Pattern C — Transparent ProRes Export (from #06)
For any overlay that needs to composite over footage in Premiere:
```
render it as a transparent prores video.
```

### Pattern D — Scrape + Use Real Data (from #02, #06)
```
use curl scrape [URL] to find [data]. 
use tesseract CLI to [extract text positions].
```

### Pattern E — Apple Presentation Style (from #10)
Shorthand the model understands reliably:
```
Make it in Apple presentation style.
```
Produces: clean white/black, large type, slow zoom reveals, minimal decoration.

### Pattern F — HTML-in-Canvas Post-Processing (from #21, #22, #23)
For applying visual effects to text/HTML that normally can't be processed:
```
use the HTML-in-canvas technique to apply [glitch/magnify/vintage] effect.
```

---

## SCOPE REMINDER

Call Remotion for these prompt types: 3D scenes, React component mockups, complex multi-scene narrative videos, canvas post-effects, data-driven animations that need React state.

Call HyperFrames for: captions, lower thirds, stat cards, section breaks, simple overlays.

Do NOT call either for raw footage editing → use Premiere MCP.
