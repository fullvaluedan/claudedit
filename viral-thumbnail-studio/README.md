# 🎬 Viral Thumbnail Studio

A localhost web app with two tools:

- **Create** — type a topic, get 10 viral YouTube thumbnails in 10 different
  styles, then fine-tune any of them in a Photopea-style layered editor.
- **Analyze** — paste any YouTube link. The app rates that video's thumbnail
  (scorecard with sub-scores) and builds 3 improved versions grounded in the
  video's transcript, using the **real** host face pulled from the channel's
  own images (never AI-generated).

All AI text work (briefs, ratings, free-form edits) runs through **headless
Claude Code** (`claude -p`), so it bills to your Claude subscription — no
Anthropic API key needed or used. Backgrounds come from your local cache,
Google Images (SerpAPI), or GPT-Image-2.

---

## Setup (first time, ~10 minutes)

You need: **Python 3.11+**, the **Claude Code CLI** installed and logged in
(`claude` must work in your terminal).

1. **Open a terminal in this folder** (`viral-thumbnail-studio`).

2. **Create a virtual environment** (a private Python sandbox for this app):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   (The first background-removal call also downloads a ~170 MB AI model
   automatically. One time only.)

4. **Create your `.env` file:**

   ```bash
   cp .env.example .env
   ```

   Open `.env` in any text editor and paste in your two keys:
   - `OPENAI_API_KEY` — from https://platform.openai.com/api-keys
     (used only for GPT-Image-2 background generation)
   - `SERPAPI_API_KEY` — from https://serpapi.com/manage-api-key
     (used for Google Images background search; free tier is fine)

   ⚠️ Do **not** put an `ANTHROPIC_API_KEY` anywhere. If one is set in your
   shell, the app warns and ignores it so Claude calls bill to your
   subscription instead.

5. **Download the two fonts** (free, for the big thumbnail text):
   - Anton: https://fonts.google.com/specimen/Anton
   - Archivo Black: https://fonts.google.com/specimen/Archivo+Black

   Click "Get font" → "Download all", unzip, and drop `Anton-Regular.ttf`
   (rename to `Anton.ttf`) and `ArchivoBlack-Regular.ttf` (rename to
   `ArchivoBlack.ttf`) into `assets/fonts/`. The app still works without
   them — it falls back to a system font — but these look much better.

6. **Start the server:**

   ```bash
   uvicorn server:app --reload
   ```

7. **Open the tools in your browser:**
   - Create:  http://127.0.0.1:8000/static/create.html
   - Analyze: http://127.0.0.1:8000/static/analyze.html

---

## Using Tool A — Create

1. Type your video topic. Optionally paste the transcript and upload a face
   photo (the background is removed automatically; your last cutout is reused
   next time).
2. Pick a mode:
   - **Full Auto** — one click. Claude writes 10 briefs (one per style),
     backgrounds are resolved (cache → search → generate), and a grid of 10
     finished thumbnails appears. No questions asked.
   - **Assisted** — you approve each stage: edit the briefs, untick styles,
     pick among 4 search results per style (or edit/regenerate the image
     prompt), then compose.
3. Click any thumbnail to open it in the **editor**: drag/scale/flip the face,
   double-click text to edit it, recolor, reorder layers, undo/redo, snap
   guides, add text/circles/arrows/badges/images, adjust the background
   (pan/darken/saturation), re-apply any style, or type a free-form change
   ("make the text yellow and move my face left") and let Claude do it.
4. **Export PNG** saves an exact 1280x720 copy to `outputs/` and downloads it.
   **Save Template** turns your layout into a reusable style (it shows up
   first in every style list). **Save Project** stores the full editor state
   in `projects/` so you can reopen it later.

## Using Tool B — Analyze

1. Paste a YouTube URL and hit **Go**. You get a scorecard: overall score,
   six sub-scores with bars, strengths, weaknesses, and a one-line verdict.
   (If the video has no transcript the report says so and uses title +
   description only.)
2. The app then pulls the channel's avatar and recent thumbnails, cuts out
   the people it finds, and shows you the candidates — pick the best one.
   These are real photos; faces are never AI-generated or AI-altered.
3. **Make 3 improved versions** — Claude picks the 3 best-fitting styles to
   attack the weaknesses and composes 3 remakes, each with a one-line
   "what changed and why". Open any of them in the editor.
4. After editing and exporting, hit **Rate my remake** to score your version
   against the original.

---

## The caches (how a second run gets fast and free)

- `assets/backgrounds/` + `manifest.json` — every searched/generated
  background, keyed by focus subject and tags. A repeat run with the same
  subject logs `cache hit` and performs **zero** new searches/generations.
- `assets/faces/` — face cutouts, keyed by source-photo hash.
- `assets/channels/<channel_id>/` — Tool B's per-channel face library.

Add your own backgrounds to the cache from the command line:

```bash
python library.py add path/to/image.jpg --subject "bitcoin chart" --tags "crypto,chart"
```

## Editor shortcuts

| Keys | Action |
|---|---|
| `Delete` / `Backspace` | delete selected object |
| `Ctrl/Cmd + Z` · `Ctrl/Cmd + Shift + Z` (or `Ctrl+Y`) | undo · redo |
| `Ctrl/Cmd + D` | duplicate selected object |
| `← ↑ ↓ →` (hold `Shift` for 10px) | nudge selected object |

The editor also shows a live **mobile preview** under the canvas — your
thumbnail at YouTube-sidebar size (168px), which is where most CTR is won
or lost.

## Tests

With the server running:

```bash
python tests_edge.py
```

runs a 20-case edge battery (bad URLs, missing keys, malformed exports,
path-traversal names, minimal templates, no-face composes, extreme slider
values, emoji/overflow text, …).

## Notes

- The CTR rulebook lives in `references/thumbnail-ctr-guide.md` (vendored from
  the MIT-licensed claude-youtube repo) and is injected into every brief and
  rating prompt.
- Style templates are JSON files in `templates/styles/`. Built-ins are plain
  ids; your saved ones get a `user_` prefix and sort first.
- Errors always come back as readable JSON and show up in the status bar at
  the top of each page (e.g. exactly which API key is missing).
- `static/vendor/fabric.min.js` is a local fallback so the editor keeps
  working when the CDN is unreachable.
