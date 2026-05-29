# Hyperframes + Remotion → Premiere Pro MCP
## Install Guide

---

## What you're doing

Adding 6 new tools to the leancoderkavy Premiere MCP server:

| Tool | What it does |
|------|-------------|
| `classify_transcript` | Reads your transcript, assigns Hyperframes tags, outputs EDL |
| `render_hyperframes_template` | Renders one Hyperframes template to MP4 |
| `generate_remotion_composition` | Writes a Remotion .tsx composition file for a segment |
| `render_remotion_composition` | Runs `npx remotion render` on that composition |
| `import_and_place_graphic` | Drops a rendered graphic onto your Premiere timeline |
| `build_full_graphic_sequence` | Does all of the above in one command from an EDL |

---

## Step 1 — Clone leancoderkavy if you haven't

```
git clone https://github.com/leancoderkavy/premiere-pro-mcp.git
cd premiere-pro-mcp
npm install
```

---

## Step 2 — Copy the new tool file

Copy `hyperframes-remotion.ts` into the tools folder:

```
# From wherever you saved this file:
copy hyperframes-remotion.ts  premiere-pro-mcp\src\tools\

# macOS/Linux:
cp hyperframes-remotion.ts premiere-pro-mcp/src/tools/
```

---

## Step 3 — Register the tools in server.ts

Open `premiere-pro-mcp/src/server.ts` in any text editor.

Find this section near the top where other tools are imported
(look for lines starting with `import {`):

```typescript
// ADD this line with the other imports:
import { registerHyperframesRemotionTools } from "./tools/hyperframes-remotion.js";
```

Then scroll down inside the same file and find where other tools
are registered (look for lines like `registerProjectTools(server, bridge)`).

Add this line in the same place:

```typescript
registerHyperframesRemotionTools(server, bridge);
```

Save the file.

---

## Step 4 — Build

```
cd premiere-pro-mcp
npm run build
```

If you see errors, copy them and send to me — I'll fix them.

---

## Step 5 — Restart your MCP client

Restart Claude Desktop (or whatever client you use).
The 6 new tools will appear automatically.

---

## Step 6 — Test it

In Claude, try:

```
classify_transcript with this transcript:
"Welcome to Dime TV. Today we're looking at Paradex fees — 0.0075% taker,
versus Binance at 0.1%. That's 13x cheaper. Over the last 30 days,
volume has grown 40%. Next: let's talk leverage."

episode_name: "dimetv-test"
output_dir: "C:/compositions/dimetv-test"
```

Claude will produce an EDL table showing which template fires for each line.

---

## Full workflow example

```
1. classify_transcript  →  produces edl.json

2. build_full_graphic_sequence with:
   - edl_path: path to edl.json
   - renderer: "hyperframes"  (or "remotion")
   - hyperframes_dir: "C:/your/hyperframes/project"
   - output_dir: "C:/compositions/dimetv-test/renders"
   - video_track: 2
   - codec: "prores-4444"

   This renders every tagged segment and drops them
   onto V2 in Premiere at the right timecodes.

3. Your main footage stays on V1.
   Graphics sit on V2 above it.
   Done.
```

---

## Notes

- `prores-4444` codec recommended for Premiere imports (lossless alpha)
- Camera-only segments (`OPINION` tag) are automatically skipped — no graphic rendered
- Brand tokens (black bg, cyan accent) are baked in — no need to set them manually
- You can override any segment's data by editing edl.json before rendering
