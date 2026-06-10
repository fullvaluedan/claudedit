"""Topic -> per-style thumbnail briefs, in ONE headless Claude call."""
import json

import config
import library

CHANNEL_CONTEXT = (
    "Channel context: crypto / AI / trading channel with 226K subscribers. "
    "Tone: punchy and confident but NEVER overpromising or scammy.")

RULES = (
    "Hard rules: thumbnail text is 4 words or fewer; never repeat a brand name "
    "that will already be visible in the background image; text must create a "
    "curiosity gap with the topic, not summarize it.")


def make_briefs(topic, transcript="", styles=None):
    """Return a list of briefs, one per style:
    {style_id, text, focus_subject, source: 'search'|'generate', query, prompt}
    """
    styles = styles or library.list_styles()
    style_summaries = [
        {"id": s["id"], "name": s["name"], "description": s["description"]}
        for s in styles
    ]
    transcript_part = ""
    if transcript:
        transcript_part = f"\nVideo transcript (use for specifics):\n{transcript[:6000]}\n"

    prompt = f"""You are a YouTube thumbnail strategist. Create one thumbnail brief
for EACH of these styles, for the video topic below.

Topic: {topic}
{transcript_part}
{CHANNEL_CONTEXT}
{RULES}

Styles (one brief per style, keep the exact style id):
{json.dumps(style_summaries, indent=1)}

Key CTR rules from our guide:
{config.ctr_guide_rules(2500)}

For each brief decide the background imagery:
- source "search" when a real photo exists (a logo, a person, a product, a place):
  give a Google Images "query".
- source "generate" when an imagined scene works better: give a detailed image
  "prompt" describing the BACKGROUND ONLY (no text in image, no people or faces
  — the real face cutout is composited on top — leave the right third clear).
Always fill BOTH query and prompt so the user can switch source later.
"focus_subject" is a short 2-4 word noun phrase naming the main background
subject (used for caching, e.g. "bitcoin crash chart").

Return a JSON array of {len(style_summaries)} objects, each:
{{"style_id": "...", "text": "max 4 words", "focus_subject": "...",
 "source": "search" or "generate", "query": "...", "prompt": "..."}}"""

    briefs = config.claude_json(prompt)
    if isinstance(briefs, dict):  # tolerate {"briefs": [...]} wrapping
        briefs = briefs.get("briefs", [])
    by_style = {b.get("style_id"): b for b in briefs if isinstance(b, dict)}
    # Guarantee one brief per requested style even if Claude skipped one.
    out = []
    for s in styles:
        b = by_style.get(s["id"]) or {
            "style_id": s["id"], "text": topic.split()[0] if topic else "WATCH",
            "focus_subject": topic[:40] or "abstract background",
            "source": "generate", "query": topic,
            "prompt": f"high impact background about {topic}",
        }
        b.setdefault("query", b.get("focus_subject", topic))
        b.setdefault("prompt", f"high impact background about {b.get('focus_subject', topic)}")
        out.append(b)
    return out
