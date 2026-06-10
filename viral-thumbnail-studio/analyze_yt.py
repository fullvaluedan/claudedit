"""Tool B: fetch a YouTube video's metadata + thumbnail, rate it, remake it.

Lightweight only: no video downloads, no frame scraping. Metadata comes from
yt-dlp (--skip-download equivalent), thumbnails from i.ytimg.com, transcripts
from youtube-transcript-api.
"""
import json
import os
import re

import requests

import compose
import config
import imagery
import library

THUMB_URLS = [
    "https://i.ytimg.com/vi/{id}/maxresdefault.jpg",
    "https://i.ytimg.com/vi/{id}/hqdefault.jpg",
]


def video_id_from_url(url):
    m = re.search(r"(?:v=|youtu\.be/|shorts/|embed/)([A-Za-z0-9_-]{11})", url)
    if not m:
        raise ValueError("That doesn't look like a YouTube video URL.")
    return m.group(1)


# --- 1) FETCH -----------------------------------------------------------------

def fetch_video(url):
    """Metadata + saved thumbnail + transcript (graceful if missing)."""
    vid = video_id_from_url(url)
    import yt_dlp
    # no-certifi: trust the system CA store (honors SSL_CERT_FILE; needed
    # behind corporate/sandbox TLS proxies, harmless everywhere else)
    opts = {"skip_download": True, "quiet": True, "no_warnings": True,
            "compat_opts": ["no-certifi"]}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)

    meta = {
        "video_id": vid,
        "title": info.get("title", ""),
        "channel_id": info.get("channel_id", ""),
        "channel": info.get("channel") or info.get("uploader", ""),
        "view_count": info.get("view_count"),
        "upload_date": info.get("upload_date"),
        "description": (info.get("description") or "")[:1500],
    }

    thumb_path = os.path.join(config.OUTPUTS_DIR, f"original_{vid}.jpg")
    for tmpl in THUMB_URLS:
        resp = requests.get(tmpl.format(id=vid), timeout=20)
        if resp.status_code == 200 and len(resp.content) > 2000:
            with open(thumb_path, "wb") as f:
                f.write(resp.content)
            break
    else:
        raise RuntimeError("Could not download the video's thumbnail.")

    transcript, transcript_available = "", True
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        fetched = YouTubeTranscriptApi().fetch(vid)
        transcript = " ".join(snippet.text for snippet in fetched)
    except Exception:
        transcript_available = False

    return {"meta": meta, "thumbnail_path": thumb_path,
            "transcript": transcript[:12000],
            "transcript_available": transcript_available}


# --- 2) RATE -------------------------------------------------------------------

RATE_SCHEMA = """{"score_overall": 0-100, "scores": {"readability": 0-100,
"contrast": 0-100, "face_emotion": 0-100, "curiosity_gap": 0-100,
"title_synergy": 0-100, "mobile_legibility": 0-100},
"strengths": ["..."], "weaknesses": ["..."], "one_line_verdict": "..."}"""


def rate_thumbnail(image_path, title, transcript=""):
    """One claude -p call that Reads the saved image file and returns a scorecard."""
    context = f"Video title: {title}\n"
    if transcript:
        context += f"Transcript summary (first part): {transcript[:3000]}\n"
    prompt = f"""Read the image file at this exact path: {os.path.abspath(image_path)}

It is a YouTube thumbnail. Rate it for click-through rate against these rules:
{config.ctr_guide_rules(3000)}

{context}
Score every category 0-100 (100 = best in class). Be specific and honest in
strengths/weaknesses — they will drive a redesign.

Return JSON exactly in this shape:
{RATE_SCHEMA}"""
    rating = config.claude_json(prompt)
    rating.setdefault("scores", {})
    rating.setdefault("strengths", [])
    rating.setdefault("weaknesses", [])
    return rating


# --- 3) HOST FACE LIBRARY --------------------------------------------------------

def face_candidates(channel_id, channel_url=None):
    """Build/refresh the channel face library and return candidate cutouts.

    Pulls the channel avatar + the ~10 most recent video thumbnails (flat
    playlist listing, no video downloads), runs rembg, keeps cutouts whose
    foreground covers 8-60% of the frame (a 'reasonably large person').
    """
    chan_dir = os.path.join(config.CHANNELS_DIR, channel_id)
    os.makedirs(chan_dir, exist_ok=True)
    meta_path = os.path.join(chan_dir, "candidates.json")
    if os.path.exists(meta_path):  # cache: only build once per channel
        with open(meta_path) as f:
            return json.load(f)

    import yt_dlp
    url = channel_url or f"https://www.youtube.com/channel/{channel_id}/videos"
    opts = {"extract_flat": True, "playlist_items": "1-10",
            "skip_download": True, "quiet": True, "no_warnings": True,
            "compat_opts": ["no-certifi"]}
    sources = []  # (key, image_url)
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=False)
        for t in info.get("thumbnails") or []:
            if "avatar" in str(t.get("id", "")):
                sources.append(("avatar", t.get("url")))
                break
        for entry in (info.get("entries") or [])[:10]:
            evid = entry.get("id")
            if evid:
                sources.append((evid, f"https://i.ytimg.com/vi/{evid}/hqdefault.jpg"))
    except Exception as exc:
        print(f"channel listing failed: {exc}")

    candidates = []
    for key, img_url in sources:
        if not img_url:
            continue
        raw_path = os.path.join(chan_dir, f"{key}.jpg")
        cut_path = os.path.join(chan_dir, f"{key}_cutout.png")
        try:
            if not os.path.exists(raw_path):
                resp = requests.get(img_url, timeout=20,
                                    headers=imagery.REQUEST_HEADERS)
                resp.raise_for_status()
                with open(raw_path, "wb") as f:
                    f.write(resp.content)
            _, area = imagery.cutout_with_area(raw_path, cut_path)
            if 0.08 <= area <= 0.60:  # person-sized foreground heuristic
                candidates.append({
                    "key": key,
                    "cutout": compose._to_url(cut_path),
                    "source_image": compose._to_url(raw_path),
                    "area": round(area, 3),
                })
        except Exception as exc:
            print(f"cutout failed for {key}: {exc}")

    candidates.sort(key=lambda c: c["area"], reverse=True)  # biggest face first
    with open(meta_path, "w") as f:
        json.dump(candidates, f, indent=2)
    return candidates


# --- 4) REMAKE -------------------------------------------------------------------

def remake_briefs(title, transcript, weaknesses):
    """One claude -p call: pick the 3 best styles and write targeted briefs."""
    styles = library.list_styles()
    style_summaries = [{"id": s["id"], "name": s["name"], "description": s["description"]}
                       for s in styles]
    prompt = f"""You are redesigning a weak YouTube thumbnail.

Video title: {title}
Transcript excerpt: {transcript[:4000] or '(no transcript available)'}
Weaknesses of the current thumbnail: {json.dumps(weaknesses)}

Available styles:
{json.dumps(style_summaries, indent=1)}

Key CTR rules:
{config.ctr_guide_rules(2000)}

Pick the THREE styles best suited to fixing the weaknesses (e.g. low contrast ->
a high-contrast style) and write one brief per pick. Text max 4 words, curiosity
gap over summary, never repeat a brand name visible in the background.

Imagery rules: "focus_subject" is a SHORT 2-4 word noun phrase naming the
background subject (e.g. "bitcoin crash chart"). The "query"/"prompt" describe
the BACKGROUND ONLY — never any person or face. The real host's photo cutout is
composited on top separately; faces are never AI-generated.

Return a JSON array of exactly 3 objects:
{{"style_id": "...", "text": "...", "focus_subject": "...",
 "source": "search" or "generate", "query": "...", "prompt": "...",
 "what_changed": "one line: what this remake changes and why it fixes a weakness"}}"""
    briefs = config.claude_json(prompt)
    if isinstance(briefs, dict):
        briefs = briefs.get("briefs", briefs.get("remakes", []))
    return briefs[:3]


def build_remakes(briefs, face_path):
    """Resolve backgrounds (cache/search/generate) and compose each remake.

    The real host face cutout is composited as-is; GPT-Image-2 only ever
    generates BACKGROUNDS — it never receives or redraws the face.
    """
    log = []
    results = []
    for b in briefs:
        style = library.get_style(b["style_id"])
        bg = imagery.resolve_background(
            b.get("focus_subject", b.get("query", "")),
            source=b.get("source", "search"),
            query=b.get("query", ""), prompt=b.get("prompt", ""),
            style_suffix=style["background"]["prompt_style_suffix"], log=log)
        spec = compose.layers(style, b, {"background": bg, "face": face_path})
        png = compose.flatten(spec)
        results.append({
            "style_id": b["style_id"],
            "what_changed": b.get("what_changed", ""),
            "layers": spec,
            "png": compose._to_url(png),
        })
    return {"remakes": results, "log": log}
