"""Background + face imagery. Resolution order: cache -> SerpAPI search -> GPT-Image-2.

Every fetched/generated background lands in the cache with a manifest entry,
so a second identical run performs zero new downloads or generations.
"""
import base64
import hashlib
import io
import os
import tempfile

import requests
from PIL import Image

import config
import library

REQUEST_HEADERS = {"User-Agent": "Mozilla/5.0 (ThumbnailStudio)"}
GEN_PROMPT_TAIL = ", right third clear, no text"


# --- search ----------------------------------------------------------------

def search_candidates(query, count=4):
    """Top image results from SerpAPI google_images, as [{url, thumbnail}]."""
    config.require_serpapi()
    resp = requests.get("https://serpapi.com/search.json", params={
        "engine": "google_images",
        "q": query,
        "api_key": config.SERPAPI_API_KEY,
        "num": 20,
    }, timeout=30)
    resp.raise_for_status()
    results = resp.json().get("images_results", [])
    out = []
    for r in results:
        url = r.get("original")
        if url:
            out.append({"url": url, "thumbnail": r.get("thumbnail", url)})
        if len(out) >= count:
            break
    if not out:
        raise RuntimeError(f"SerpAPI returned no images for: {query}")
    return out


def download_image(url):
    """Download a URL into the background cache (returns local path)."""
    resp = requests.get(url, headers=REQUEST_HEADERS, timeout=30)
    resp.raise_for_status()
    img = Image.open(io.BytesIO(resp.content)).convert("RGB")  # validates it
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
        img.save(tmp.name, "JPEG", quality=92)
        return tmp.name


# --- generation --------------------------------------------------------------

def generate_background(prompt, style_suffix=""):
    """Generate a 1280x720 background with GPT-Image-2 (returns temp file path)."""
    config.require_openai()
    from openai import OpenAI  # imported lazily: not needed for cache hits
    client = OpenAI(api_key=config.OPENAI_API_KEY)
    full_prompt = prompt.rstrip(". ")
    if style_suffix:
        full_prompt += ", " + style_suffix
    full_prompt += GEN_PROMPT_TAIL
    result = client.images.generate(
        model=config.IMAGE_MODEL,
        prompt=full_prompt,
        size="1280x720",  # gpt-image-2 accepts arbitrary sizes divisible by 16
        quality="high",
        n=1,
    )
    data = base64.b64decode(result.data[0].b64_json)
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        tmp.write(data)
        return tmp.name


# --- resolution (cache -> search -> generate) -------------------------------

def resolve_background(focus_subject, source="search", query="", prompt="",
                       style_suffix="", chosen_url="", log=None):
    """Return a local background path for a brief. Cache first, always.

    chosen_url: in Assisted mode the user already picked a search result.
    log: optional list collecting human-readable cache-hit/generation messages.
    """
    def note(msg):
        if log is not None:
            log.append(msg)
        print(msg)

    cached = library.find_cached_background(focus_subject)
    if cached and not chosen_url:
        note(f"cache hit: background for '{focus_subject}'")
        return cached

    tags = focus_subject.lower().split()
    if chosen_url:
        tmp = download_image(chosen_url)
        note(f"downloaded chosen background for '{focus_subject}'")
        return library.add_background(tmp, focus_subject, tags, source="search")

    if source == "search":
        try:
            candidates = search_candidates(query or focus_subject, count=4)
            tmp = download_image(candidates[0]["url"])
            note(f"searched + downloaded background for '{focus_subject}'")
            return library.add_background(tmp, focus_subject, tags, source="search")
        except config.ConfigError:
            raise
        except Exception as exc:
            note(f"search failed ({exc}); falling back to generation")

    tmp = generate_background(prompt or f"high impact YouTube thumbnail background about {focus_subject}",
                              style_suffix)
    note(f"generated background for '{focus_subject}'")
    return library.add_background(tmp, focus_subject, tags, source="generate")


# --- face cutouts -------------------------------------------------------------

def cutout_face(source_path):
    """Remove the background from a photo with rembg. Cached by file hash."""
    with open(source_path, "rb") as f:
        raw = f.read()
    digest = hashlib.sha256(raw).hexdigest()[:16]
    cached = os.path.join(config.FACES_DIR, f"{digest}.png")
    if os.path.exists(cached):
        print(f"cache hit: face cutout {digest}")
        return cached
    from rembg import remove  # lazy: loads the onnx model on first use
    result = remove(raw)
    img = Image.open(io.BytesIO(result)).convert("RGBA")
    img = trim_to_alpha(img)
    img.save(cached, "PNG")
    return cached


def trim_to_alpha(img):
    """Crop transparent borders so scaling math uses the visible subject only."""
    bbox = img.getchannel("A").getbbox()
    return img.crop(bbox) if bbox else img


def last_used_cutout():
    """Most recent face cutout, used as the default face in Tool A."""
    pngs = [os.path.join(config.FACES_DIR, n) for n in os.listdir(config.FACES_DIR)
            if n.endswith(".png")]
    return max(pngs, key=os.path.getmtime) if pngs else None


def cutout_with_area(source_path, dest_path):
    """Cutout for the channel face library: returns (path, area_fraction) where
    area is measured against the FULL frame before trimming (for the 8-60% person
    heuristic), then the saved file is trimmed for compositing."""
    with open(source_path, "rb") as f:
        raw = f.read()
    from rembg import remove
    img = Image.open(io.BytesIO(remove(raw))).convert("RGBA")
    hist = img.getchannel("A").histogram()
    area = sum(hist[16:]) / (img.width * img.height)
    trim_to_alpha(img).save(dest_path, "PNG")
    return dest_path, area


def alpha_area_fraction(png_path):
    """Fraction of the frame covered by non-transparent pixels (0..1)."""
    img = Image.open(png_path).convert("RGBA")
    alpha = img.getchannel("A")
    hist = alpha.histogram()
    opaque = sum(hist[16:])  # ignore near-transparent noise
    return opaque / (img.width * img.height)
