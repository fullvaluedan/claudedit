/**
 * hyperframes-remotion.ts
 *
 * MCP tools bridging Hyperframes templates and Remotion compositions
 * into Adobe Premiere Pro via the file-based IPC bridge.
 *
 * Drop this file into:  src/tools/hyperframes-remotion.ts
 * Then register tools in: src/server.ts  (see REGISTRATION NOTE at bottom)
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
import { execSync, spawn } from "child_process";
import * as fs from "fs";
import * as path from "path";
import { FileBridge } from "../bridge/file-bridge.js";

// ─── Brand tokens (Paradex / Dime TV) ────────────────────────────────────────
const BRAND = {
  bg: "#000000",
  accent: "#00D4FF",
  text: "#F5F5F7",
  font: "'Space Grotesk', 'Inter', sans-serif",
  ease: "cubic-bezier(0.16, 1, 0.3, 1)",
};

// ─── Hyperframes template → CLI example name map ─────────────────────────────
const TEMPLATE_MAP: Record<string, string> = {
  "swiss-grid":    "swiss-grid",
  "warm-grain":    "warm-grain",
  "decision-tree": "decision-tree",
  "nyt-graph":     "nyt-graph",
  "kinetic-type":  "kinetic-type",
  "play-mode":     "play-mode",
  "product-promo": "product-promo",
  "vignelli":      "vignelli",
};

// ─── Content tag → template mapping (from Hyperframes Director skill) ─────────
const TAG_TO_TEMPLATE: Record<string, string> = {
  NUMBER:        "swiss-grid",
  COMPARISON:    "swiss-grid",
  CONCEPT:       "decision-tree",
  "DATA-TREND":  "nyt-graph",
  INTRO:         "warm-grain",
  MILESTONE:     "play-mode",
  "SECTION-BREAK": "kinetic-type",
  OPINION:       "camera",   // no graphic — stay on face
  TERM:          "overlay",  // lower-third overlay
};

// ─── EDL segment schema ───────────────────────────────────────────────────────
const EDLSegmentSchema = z.object({
  index:    z.number(),
  in_tc:    z.string().describe("Timecode string e.g. '0:08'"),
  out_tc:   z.string().describe("Timecode string e.g. '0:15'"),
  spoken:   z.string().describe("Spoken text for this segment"),
  tag:      z.enum(["NUMBER","COMPARISON","CONCEPT","DATA-TREND","INTRO","MILESTONE","SECTION-BREAK","OPINION","TERM"]),
  template: z.string().optional(),
  mode:     z.enum(["full-frame","camera","overlay"]).default("full-frame"),
  data:     z.record(z.any()).optional().describe("Template-specific data payload"),
});

type EDLSegment = z.infer<typeof EDLSegmentSchema>;

// ─── Helper: parse timecode string to seconds ─────────────────────────────────
function tcToSeconds(tc: string): number {
  const parts = tc.split(":").map(Number);
  if (parts.length === 2) return parts[0] * 60 + parts[1];
  if (parts.length === 3) return parts[0] * 3600 + parts[1] * 60 + parts[2];
  return Number(tc);
}

// ─── Helper: run a shell command and return stdout ────────────────────────────
function run(cmd: string, cwd?: string): string {
  return execSync(cmd, { cwd, encoding: "utf8", stdio: ["pipe","pipe","pipe"] });
}

// ─── Helper: ensure output directory exists ───────────────────────────────────
function ensureDir(p: string) {
  fs.mkdirSync(p, { recursive: true });
}

// ═════════════════════════════════════════════════════════════════════════════
// TOOL REGISTRATION
// ═════════════════════════════════════════════════════════════════════════════

export function registerHyperframesRemotionTools(server: McpServer, bridge: FileBridge) {

  // ── 1. classify_transcript ─────────────────────────────────────────────────
  server.tool(
    "classify_transcript",
    "Classify a transcript into Hyperframes EDL segments. Returns tagged segments with template assignments and cut decisions following Dime TV pacing rules.",
    {
      transcript: z.string().describe("Full transcript text or array of timed lines"),
      episode_name: z.string().describe("Used for output file naming e.g. 'dimetv-ep42'"),
      output_dir: z.string().optional().describe("Where to save edl.json. Defaults to ./compositions/<episode_name>"),
    },
    async ({ transcript, episode_name, output_dir }) => {
      const outDir = output_dir ?? path.join(process.cwd(), "compositions", episode_name);
      ensureDir(outDir);

      // Parse lines — supports plain text or simple "MM:SS text" format
      const lines = transcript.split("\n").filter(Boolean);
      const segments: EDLSegment[] = [];
      let cursor = 0;

      for (let i = 0; i < lines.length; i++) {
        const line = lines[i].trim();
        if (!line) continue;

        // Try to detect tag from content heuristics
        let tag: EDLSegment["tag"] = "OPINION";
        if (/\d+(\.\d+)?%|\$[\d,]+|bps|tvl|volume/i.test(line))      tag = "NUMBER";
        else if (/vs\.?|versus|compar|cheaper|more than/i.test(line)) tag = "COMPARISON";
        else if (/how it works|process|step|flow|mechanism/i.test(line)) tag = "CONCEPT";
        else if (/over time|since|grew|trend|chart|graph/i.test(line)) tag = "DATA-TREND";
        else if (/welcome|intro|today we|this week/i.test(line))       tag = "INTRO";
        else if (/million|billion|record|launch|hit|achieve/i.test(line)) tag = "MILESTONE";
        else if (/next:|coming up|section|topic/i.test(line))         tag = "SECTION-BREAK";
        else if (/called|known as|defined as|term/i.test(line))       tag = "TERM";

        const template = TAG_TO_TEMPLATE[tag];
        const duration = tag === "SECTION-BREAK" ? 0.6 :
                         tag === "INTRO"         ? 6   :
                         tag === "MILESTONE"     ? 4   :
                         tag === "NUMBER"        ? 4   :
                         tag === "COMPARISON"    ? 6   :
                         tag === "CONCEPT"       ? 7   :
                         tag === "DATA-TREND"    ? 7   : 6;

        const inSec  = cursor;
        const outSec = cursor + duration;

        segments.push({
          index:    i + 1,
          in_tc:    `${Math.floor(inSec/60)}:${String(Math.floor(inSec%60)).padStart(2,"0")}`,
          out_tc:   `${Math.floor(outSec/60)}:${String(Math.floor(outSec%60)).padStart(2,"0")}`,
          spoken:   line,
          tag,
          template: template !== "camera" && template !== "overlay" ? template : undefined,
          mode:     template === "camera" ? "camera" : template === "overlay" ? "overlay" : "full-frame",
        });

        cursor = outSec;
      }

      // Write EDL to disk
      const edlPath = path.join(outDir, "edl.json");
      fs.writeFileSync(edlPath, JSON.stringify({ episode_name, brand: BRAND, segments }, null, 2));

      // Build human-readable table
      const table = [
        "| # | In    | Out   | Tag            | Template      | Mode       | Spoken (truncated)        |",
        "|---|-------|-------|----------------|---------------|------------|---------------------------|",
        ...segments.map(s =>
          `| ${s.index} | ${s.in_tc.padEnd(5)} | ${s.out_tc.padEnd(5)} | ${s.tag.padEnd(14)} | ${(s.template ?? "—").padEnd(13)} | ${s.mode.padEnd(10)} | ${s.spoken.slice(0,25).padEnd(25)} |`
        )
      ].join("\n");

      return {
        content: [{
          type: "text",
          text: `EDL written to: ${edlPath}\n\n${table}\n\nReview EDL then call render_hyperframes_template or generate_remotion_composition per segment, or use build_full_graphic_sequence to do it all.`,
        }],
      };
    }
  );

  // ── 2. render_hyperframes_template ────────────────────────────────────────
  server.tool(
    "render_hyperframes_template",
    "Render a single Hyperframes template to a video file. Uses npx hyperframes render. Returns the output file path.",
    {
      template:      z.enum(Object.keys(TEMPLATE_MAP) as [string, ...string[]]).describe("Template name"),
      output_path:   z.string().describe("Full path for output .mp4 file"),
      duration_ms:   z.number().default(5000).describe("Duration in milliseconds"),
      data:          z.record(z.any()).optional().describe("Template data payload — title, value, items, etc."),
      width:         z.number().default(1920),
      height:        z.number().default(1080),
      fps:           z.number().default(30),
      hyperframes_dir: z.string().describe("Absolute path to your local Hyperframes project directory"),
    },
    async ({ template, output_path, duration_ms, data, width, height, fps, hyperframes_dir }) => {
      ensureDir(path.dirname(output_path));

      // Write data payload as a temp JSON so hyperframes CLI can consume it
      const dataFile = path.join(hyperframes_dir, `.mcp-data-${Date.now()}.json`);
      fs.writeFileSync(dataFile, JSON.stringify({
        brand: BRAND,
        duration: duration_ms,
        ...(data ?? {}),
      }));

      try {
        const cmd = [
          "npx hyperframes render",
          `--example ${TEMPLATE_MAP[template]}`,
          `--output "${output_path}"`,
          `--width ${width}`,
          `--height ${height}`,
          `--fps ${fps}`,
          `--duration ${duration_ms}`,
          `--data "${dataFile}"`,
        ].join(" ");

        run(cmd, hyperframes_dir);
        fs.unlinkSync(dataFile);

        return {
          content: [{
            type: "text",
            text: `Rendered: ${output_path}\nTemplate: ${template} | ${duration_ms}ms | ${width}x${height}@${fps}fps`,
          }],
        };
      } catch (err: any) {
        fs.unlinkSync(dataFile);
        throw new Error(`Hyperframes render failed: ${err.message}`);
      }
    }
  );

  // ── 3. generate_remotion_composition ──────────────────────────────────────
  server.tool(
    "generate_remotion_composition",
    "Generate a Remotion React composition file for a Dime TV segment. Writes a .tsx file to your Remotion project that you can then render.",
    {
      segment:        EDLSegmentSchema.describe("EDL segment to generate composition for"),
      remotion_dir:   z.string().describe("Absolute path to your local Remotion project"),
      composition_id: z.string().optional().describe("Overrides auto-generated composition ID"),
    },
    async ({ segment, remotion_dir, composition_id }) => {
      const compId = composition_id ?? `DiMeTV_${segment.tag}_${segment.index}`;
      const duration = tcToSeconds(segment.out_tc) - tcToSeconds(segment.in_tc);
      const fps = 30;
      const durationFrames = Math.round(duration * fps);

      const compDir = path.join(remotion_dir, "src", "compositions");
      ensureDir(compDir);
      const outFile = path.join(compDir, `${compId}.tsx`);

      // Generate Remotion composition based on tag
      const tsx = generateRemotionTSX({ segment, compId, durationFrames, fps, brand: BRAND });
      fs.writeFileSync(outFile, tsx);

      return {
        content: [{
          type: "text",
          text: `Composition written: ${outFile}\nID: ${compId} | ${durationFrames} frames @ ${fps}fps (${duration}s)\n\nTo render:\n  npx remotion render ${compId} --output out/${compId}.mp4\n\nOr call render_remotion_composition next.`,
        }],
      };
    }
  );

  // ── 4. render_remotion_composition ───────────────────────────────────────
  server.tool(
    "render_remotion_composition",
    "Render a Remotion composition to an MP4 file using npx remotion render.",
    {
      composition_id: z.string().describe("Remotion composition ID"),
      output_path:    z.string().describe("Full path for output .mp4"),
      remotion_dir:   z.string().describe("Absolute path to your Remotion project"),
      fps:            z.number().default(30),
      width:          z.number().default(1920),
      height:         z.number().default(1080),
      codec:          z.enum(["h264","prores-4444","prores"]).default("h264").describe("Use prores-4444 for Premiere import quality"),
    },
    async ({ composition_id, output_path, remotion_dir, fps, width, height, codec }) => {
      ensureDir(path.dirname(output_path));

      const cmd = [
        "npx remotion render",
        composition_id,
        `"${output_path}"`,
        `--fps=${fps}`,
        `--width=${width}`,
        `--height=${height}`,
        `--codec=${codec}`,
      ].join(" ");

      try {
        run(cmd, remotion_dir);
        return {
          content: [{
            type: "text",
            text: `Rendered: ${output_path}\n${composition_id} | ${width}x${height}@${fps}fps | codec: ${codec}`,
          }],
        };
      } catch (err: any) {
        throw new Error(`Remotion render failed: ${err.message}`);
      }
    }
  );

  // ── 5. import_and_place_graphic ──────────────────────────────────────────
  server.tool(
    "import_and_place_graphic",
    "Import a rendered graphic file into Premiere Pro and place it on the timeline at the correct timecode. Wraps import_media + add_to_timeline.",
    {
      file_path:      z.string().describe("Absolute path to the rendered .mp4 or .mov graphic file"),
      in_tc:          z.string().describe("Timeline in-point timecode e.g. '0:08'"),
      video_track:    z.number().default(2).describe("V2 by default — sits above main footage on V1"),
      sequence_name:  z.string().optional().describe("Target sequence name. Uses active sequence if omitted."),
    },
    async ({ file_path, in_tc, video_track, sequence_name }) => {
      if (!fs.existsSync(file_path)) {
        throw new Error(`File not found: ${file_path}`);
      }

      const inSeconds = tcToSeconds(in_tc);

      // Step 1: Import the file
      const importResult = await bridge.executeScript(`
        var item = app.project.importFiles(
          ["${file_path.replace(/\\/g, "\\\\")}"],
          true,
          app.project.rootItem,
          false
        );
        item ? "imported" : "failed";
      `);

      if (importResult.includes("failed")) {
        throw new Error(`Failed to import: ${file_path}`);
      }

      // Step 2: Add to timeline at correct position
      const clipName = path.basename(file_path);
      const placeResult = await bridge.executeScript(`
        var seq = ${sequence_name ? `(function(){ for(var i=0;i<app.project.sequences.numSequences;i++){ if(app.project.sequences[i].name=="${sequence_name}") return app.project.sequences[i]; } return app.project.activeSequence; })()` : "app.project.activeSequence"};
        var item = null;
        for(var i=0;i<app.project.rootItem.children.numItems;i++){
          if(app.project.rootItem.children[i].name=="${clipName}"){
            item=app.project.rootItem.children[i]; break;
          }
        }
        if(!item){ "item_not_found"; }
        else {
          seq.videoTracks[${video_track - 1}].insertClip(item, ${inSeconds});
          "placed";
        }
      `);

      return {
        content: [{
          type: "text",
          text: placeResult.includes("placed")
            ? `Placed "${clipName}" on V${video_track} at ${in_tc} (${inSeconds}s)`
            : `Import succeeded but placement failed: ${placeResult}`,
        }],
      };
    }
  );

  // ── 6. build_full_graphic_sequence (orchestrator) ─────────────────────────
  server.tool(
    "build_full_graphic_sequence",
    "Orchestrator: reads an EDL JSON, renders all non-camera segments via Hyperframes or Remotion, and places them on the Premiere timeline. One command to go from EDL to finished timeline.",
    {
      edl_path:         z.string().describe("Path to edl.json produced by classify_transcript"),
      renderer:         z.enum(["hyperframes","remotion"]).default("hyperframes").describe("Which renderer to use for graphic segments"),
      hyperframes_dir:  z.string().optional().describe("Required if renderer=hyperframes"),
      remotion_dir:     z.string().optional().describe("Required if renderer=remotion"),
      output_dir:       z.string().describe("Where rendered graphic files will be saved"),
      video_track:      z.number().default(2).describe("Premiere track for graphics (V2 default)"),
      codec:            z.enum(["h264","prores-4444"]).default("prores-4444"),
      dry_run:          z.boolean().default(false).describe("If true, shows what would be rendered without actually rendering"),
    },
    async ({ edl_path, renderer, hyperframes_dir, remotion_dir, output_dir, video_track, codec, dry_run }) => {
      if (!fs.existsSync(edl_path)) throw new Error(`EDL not found: ${edl_path}`);

      const edl = JSON.parse(fs.readFileSync(edl_path, "utf8"));
      const segments: EDLSegment[] = edl.segments;
      ensureDir(output_dir);

      const results: string[] = [];
      const skipped: string[] = [];

      for (const seg of segments) {
        // Skip camera-only and overlay segments
        if (seg.mode === "camera") {
          skipped.push(`#${seg.index} ${seg.tag} — camera-only, no graphic`);
          continue;
        }
        if (!seg.template) {
          skipped.push(`#${seg.index} ${seg.tag} — no template assigned`);
          continue;
        }

        const duration = tcToSeconds(seg.out_tc) - tcToSeconds(seg.in_tc);
        const outFile = path.join(output_dir, `seg-${seg.index}-${seg.tag}.mp4`);

        if (dry_run) {
          results.push(`[DRY RUN] #${seg.index} ${seg.tag} → ${seg.template} → ${outFile} (${duration}s)`);
          continue;
        }

        if (renderer === "hyperframes") {
          if (!hyperframes_dir) throw new Error("hyperframes_dir required when renderer=hyperframes");

          const dataFile = path.join(hyperframes_dir, `.mcp-seg-${seg.index}.json`);
          fs.writeFileSync(dataFile, JSON.stringify({ brand: BRAND, duration: duration * 1000, ...(seg.data ?? {}) }));

          run([
            "npx hyperframes render",
            `--example ${TEMPLATE_MAP[seg.template] ?? seg.template}`,
            `--output "${outFile}"`,
            `--duration ${Math.round(duration * 1000)}`,
            `--data "${dataFile}"`,
          ].join(" "), hyperframes_dir);

          fs.unlinkSync(dataFile);

        } else {
          // Remotion path
          if (!remotion_dir) throw new Error("remotion_dir required when renderer=remotion");
          const compId = `DiMeTV_${seg.tag}_${seg.index}`;
          const fps = 30;
          const durationFrames = Math.round(duration * fps);
          const compDir = path.join(remotion_dir, "src", "compositions");
          ensureDir(compDir);
          fs.writeFileSync(
            path.join(compDir, `${compId}.tsx`),
            generateRemotionTSX({ segment: seg, compId, durationFrames, fps, brand: BRAND })
          );
          run([
            "npx remotion render",
            compId,
            `"${outFile}"`,
            `--fps=30`,
            `--codec=${codec}`,
          ].join(" "), remotion_dir);
        }

        // Place in Premiere
        const clipName = path.basename(outFile);
        const inSeconds = tcToSeconds(seg.in_tc);

        await bridge.executeScript(`
          app.project.importFiles(["${outFile.replace(/\\/g, "\\\\")}"], true, app.project.rootItem, false);
          var seq = app.project.activeSequence;
          for(var i=0;i<app.project.rootItem.children.numItems;i++){
            if(app.project.rootItem.children[i].name=="${clipName}"){
              seq.videoTracks[${video_track - 1}].insertClip(app.project.rootItem.children[i], ${inSeconds});
              break;
            }
          }
        `);

        results.push(`✓ #${seg.index} ${seg.tag} → placed on V${video_track} at ${seg.in_tc}`);
      }

      return {
        content: [{
          type: "text",
          text: [
            `=== build_full_graphic_sequence complete ===`,
            `Renderer: ${renderer} | Codec: ${codec} | Track: V${video_track}`,
            dry_run ? "\n⚠️  DRY RUN — nothing was rendered or placed\n" : "",
            "\nPlaced:",
            ...results,
            skipped.length ? "\nSkipped:" : "",
            ...skipped,
          ].join("\n"),
        }],
      };
    }
  );

}

// ═════════════════════════════════════════════════════════════════════════════
// REMOTION TSX GENERATOR
// ═════════════════════════════════════════════════════════════════════════════

function generateRemotionTSX({ segment, compId, durationFrames, fps, brand }: {
  segment: EDLSegment;
  compId: string;
  durationFrames: number;
  fps: number;
  brand: typeof BRAND;
}): string {

  const componentMap: Record<string, string> = {
    "swiss-grid":    swissGridComponent,
    "warm-grain":    warmGrainComponent,
    "kinetic-type":  kineticTypeComponent,
    "nyt-graph":     nytGraphComponent,
    "decision-tree": decisionTreeComponent,
    "play-mode":     playModeComponent,
  };

  const template = segment.template ?? "swiss-grid";
  const innerComponent = (componentMap[template] ?? swissGridComponent)
    .replace(/SPOKEN_TEXT/g, segment.spoken.replace(/"/g, '\\"'))
    .replace(/ACCENT_COLOR/g, brand.accent)
    .replace(/BG_COLOR/g, brand.bg)
    .replace(/TEXT_COLOR/g, brand.text)
    .replace(/BRAND_FONT/g, brand.font);

  return `/**
 * Auto-generated by premiere-pro-mcp Hyperframes-Remotion bridge
 * Segment: #${segment.index} | Tag: ${segment.tag} | Template: ${template}
 * In: ${segment.in_tc} | Out: ${segment.out_tc}
 */
import { Composition } from "remotion";
import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig, spring } from "remotion";

// ── Inner component ──────────────────────────────────────────────────────────
${innerComponent}

// ── Composition export ───────────────────────────────────────────────────────
export const ${compId}Comp: React.FC = () => (
  <Composition
    id="${compId}"
    component={Inner}
    durationInFrames={${durationFrames}}
    fps={${fps}}
    width={1920}
    height={1080}
  />
);
`;
}

// ── Template inner components ─────────────────────────────────────────────────

const swissGridComponent = `
const Inner: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const progress = spring({ frame, fps, config: { damping: 80, stiffness: 200 } });
  const opacity = interpolate(frame, [0, 10], [0, 1], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ backgroundColor: "BG_COLOR", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "BRAND_FONT" }}>
      <div style={{ opacity, transform: \`translateY(\${interpolate(progress, [0,1], [40,0])}px)\`, textAlign: "center", padding: 80 }}>
        <div style={{ fontSize: 96, fontWeight: 700, color: "ACCENT_COLOR", letterSpacing: -2 }}>
          SPOKEN_TEXT
        </div>
      </div>
    </AbsoluteFill>
  );
};`;

const warmGrainComponent = `
const Inner: React.FC = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ backgroundColor: "BG_COLOR", fontFamily: "BRAND_FONT" }}>
      <div style={{ position: "absolute", inset: 0, background: "radial-gradient(ellipse at center, #1a1a1a 0%, BG_COLOR 100%)" }} />
      <div style={{ position: "absolute", inset: 0, display: "flex", alignItems: "center", justifyContent: "center", opacity }}>
        <div style={{ color: "TEXT_COLOR", fontSize: 64, fontWeight: 300, letterSpacing: 4, textTransform: "uppercase" }}>
          SPOKEN_TEXT
        </div>
      </div>
    </AbsoluteFill>
  );
};`;

const kineticTypeComponent = `
const Inner: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const progress = spring({ frame, fps, config: { damping: 100, stiffness: 400 } });
  const x = interpolate(progress, [0,1], [-200, 0]);

  return (
    <AbsoluteFill style={{ backgroundColor: "BG_COLOR", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "BRAND_FONT", overflow: "hidden" }}>
      <div style={{ transform: \`translateX(\${x}px)\`, color: "TEXT_COLOR", fontSize: 120, fontWeight: 900, letterSpacing: -4, textTransform: "uppercase" }}>
        SPOKEN_TEXT
      </div>
      <div style={{ position: "absolute", bottom: 0, left: 0, right: 0, height: 6, backgroundColor: "ACCENT_COLOR", transform: \`scaleX(\${progress})\`, transformOrigin: "left" }} />
    </AbsoluteFill>
  );
};`;

const nytGraphComponent = `
const Inner: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const progress = interpolate(frame, [10, durationInFrames - 5], [0, 1], { extrapolateRight: "clamp" });

  // Placeholder chart — replace data array with real values via segment.data
  const points = [20, 35, 28, 55, 48, 72, 65, 88];
  const maxVal = Math.max(...points);
  const w = 1400; const h = 500;

  return (
    <AbsoluteFill style={{ backgroundColor: "BG_COLOR", fontFamily: "BRAND_FONT", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center" }}>
      <div style={{ color: "TEXT_COLOR", fontSize: 40, marginBottom: 40, opacity: interpolate(frame, [0,15],[0,1],{extrapolateRight:"clamp"}) }}>
        SPOKEN_TEXT
      </div>
      <svg width={w} height={h} viewBox={\`0 0 \${w} \${h}\`}>
        <polyline
          points={points.map((v,i) => \`\${(i/(points.length-1))*w},\${h - (v/maxVal)*h*progress}\`).join(" ")}
          fill="none" stroke="ACCENT_COLOR" strokeWidth={4}
        />
      </svg>
    </AbsoluteFill>
  );
};`;

const decisionTreeComponent = `
const Inner: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const nodes = ["SPOKEN_TEXT".split(".")[0], "Step 2", "Step 3"];

  return (
    <AbsoluteFill style={{ backgroundColor: "BG_COLOR", fontFamily: "BRAND_FONT", display: "flex", alignItems: "center", justifyContent: "center" }}>
      <div style={{ display: "flex", gap: 80, alignItems: "center" }}>
        {nodes.map((n, i) => {
          const delay = i * 8;
          const opacity = interpolate(frame, [delay, delay+12], [0,1], { extrapolateRight:"clamp" });
          return (
            <React.Fragment key={i}>
              <div style={{ opacity, background: "#111", border: \`2px solid ACCENT_COLOR\`, borderRadius: 16, padding: "24px 32px", color: "TEXT_COLOR", fontSize: 28, textAlign: "center", maxWidth: 280 }}>
                {n}
              </div>
              {i < nodes.length-1 && (
                <div style={{ color: "ACCENT_COLOR", fontSize: 48, opacity }}>→</div>
              )}
            </React.Fragment>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};`;

const playModeComponent = `
const Inner: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const scale = spring({ frame, fps, config: { damping: 12, stiffness: 180 } });

  return (
    <AbsoluteFill style={{ backgroundColor: "BG_COLOR", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "BRAND_FONT" }}>
      <div style={{ transform: \`scale(\${scale})\`, textAlign: "center" }}>
        <div style={{ fontSize: 120, fontWeight: 900, color: "ACCENT_COLOR", letterSpacing: -4 }}>
          SPOKEN_TEXT
        </div>
        <div style={{ marginTop: 20, fontSize: 32, color: "TEXT_COLOR", opacity: 0.7 }}>
          🎯
        </div>
      </div>
    </AbsoluteFill>
  );
};`;

/*
 * ─────────────────────────────────────────────────────────────────────────────
 * REGISTRATION NOTE — add this to src/server.ts:
 *
 *   import { registerHyperframesRemotionTools } from "./tools/hyperframes-remotion.js";
 *
 *   // Inside your server setup, after existing tool registrations:
 *   registerHyperframesRemotionTools(server, bridge);
 *
 * ─────────────────────────────────────────────────────────────────────────────
 */
