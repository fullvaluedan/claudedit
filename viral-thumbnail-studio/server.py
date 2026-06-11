"""FastAPI app: all endpoints for Tool A (Create) and Tool B (Analyze).

Run with:  uvicorn server:app --reload
Pages:     http://127.0.0.1:8000/static/create.html
           http://127.0.0.1:8000/static/analyze.html
"""
import base64
import io
import json
import os
import re
import tempfile
import time

from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

import analyze_yt
import brief
import compose
import config
import imagery
import library

app = FastAPI(title="Viral Thumbnail Studio")


@app.exception_handler(Exception)
async def readable_errors(request: Request, exc: Exception):
    """Every error becomes readable JSON that the pages show in the status bar."""
    status = 400 if isinstance(exc, (config.ConfigError, ValueError, KeyError)) else 500
    return JSONResponse(status_code=status, content={"error": str(exc) or type(exc).__name__})


@app.get("/")
def home():
    return RedirectResponse("/static/create.html")


@app.get("/styles")
def styles():
    return {"styles": library.list_styles()}


@app.get("/fonts/list")
def fonts_list():
    fonts = [n for n in sorted(os.listdir(config.FONTS_DIR))
             if n.lower().endswith((".ttf", ".otf"))]
    return {"fonts": fonts}


# ============================ TOOL A — CREATE =================================

@app.post("/generate")
async def generate(topic: str = Form(...), mode: str = Form("auto"),
                   transcript: str = Form(""), face: UploadFile | None = File(None)):
    """Full Auto: briefs -> backgrounds -> 10 composed thumbnails.
    Assisted: returns the editable briefs only (front end continues stepwise)."""
    if not topic.strip():
        raise ValueError("Enter a topic first — it drives every brief.")
    face_path = await _resolve_face_upload(face)
    briefs = brief.make_briefs(topic.strip(), transcript)
    if mode == "assisted":
        return {"briefs": briefs, "face": compose._to_url(face_path)}

    log, results = [], []
    for b in briefs:
        style = library.get_style(b["style_id"])
        bg = imagery.resolve_background(
            b.get("focus_subject", ""), source=b.get("source", "search"),
            query=b.get("query", ""), prompt=b.get("prompt", ""),
            style_suffix=style["background"]["prompt_style_suffix"], log=log)
        spec = compose.layers(style, b, {"background": bg, "face": face_path},
                              brand=library.load_brand())
        png = compose.flatten(spec)
        results.append({"style_id": b["style_id"], "style_name": style["name"],
                        "png": compose._to_url(png), "layers": spec})
    return {"thumbnails": results, "log": log}


async def _resolve_face_upload(face):
    """Uploaded photo -> cached cutout; otherwise default to the last used cutout."""
    if face and face.filename:
        suffix = os.path.splitext(face.filename)[1] or ".jpg"
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
            tmp.write(await face.read())
        return imagery.cutout_face(tmp.name)
    return imagery.last_used_cutout()


@app.post("/backgrounds/candidates")
async def backgrounds_candidates(request: Request):
    """Assisted step 2: search -> 4 clickable results; generate -> echo the prompt."""
    body = await request.json()
    if body.get("source") == "generate":
        return {"mode": "generate", "prompt": body.get("prompt", "")}
    return {"mode": "search",
            "candidates": imagery.search_candidates(body.get("query", ""), count=4)}


@app.post("/backgrounds/generate")
async def backgrounds_generate(request: Request):
    """Assisted: generate (or regenerate) one background from an edited prompt."""
    body = await request.json()
    tmp = imagery.generate_background(body["prompt"], body.get("style_suffix", ""))
    cached = library.add_background(tmp, body.get("focus_subject", body["prompt"][:40]),
                                    body.get("focus_subject", "").split(), source="generate")
    return {"file": compose._to_url(cached)}


@app.post("/compose")
async def compose_endpoint(request: Request):
    """Compose chosen briefs+backgrounds into thumbnails (Assisted step 3)."""
    body = await request.json()
    face_path = compose._from_url(body.get("face")) if body.get("face") else imagery.last_used_cutout()
    log, results = [], []
    for item in body["items"]:
        b = item["brief"]
        style = library.get_style(b["style_id"])
        if item.get("chosen_file"):  # an already-generated/cached file was picked
            bg = compose._from_url(item["chosen_file"])
        else:
            bg = imagery.resolve_background(
                b.get("focus_subject", ""), source=b.get("source", "search"),
                query=b.get("query", ""), prompt=b.get("prompt", ""),
                style_suffix=style["background"]["prompt_style_suffix"],
                chosen_url=item.get("chosen_url", ""), log=log)
        spec = compose.layers(style, b, {"background": bg, "face": face_path},
                              brand=library.load_brand())
        png = compose.flatten(spec)
        results.append({"style_id": b["style_id"], "style_name": style["name"],
                        "png": compose._to_url(png), "layers": spec})
    return {"thumbnails": results, "log": log}


@app.get("/brand")
def brand_get():
    return {"brand": library.load_brand()}


@app.post("/brand")
async def brand_set(request: Request):
    body = await request.json()
    return {"brand": library.save_brand(body.get("brand", body))}


@app.get("/outputs/list")
def outputs_list():
    """All exported/composed images, newest first (for the Gallery page)."""
    items = []
    for name in os.listdir(config.OUTPUTS_DIR):
        if not name.lower().endswith((".png", ".jpg", ".jpeg")):
            continue
        path = os.path.join(config.OUTPUTS_DIR, name)
        stat = os.stat(path)
        items.append({"file": f"/outputs/{name}", "name": name,
                      "mtime": stat.st_mtime, "size": stat.st_size})
    items.sort(key=lambda i: i["mtime"], reverse=True)
    return {"files": items}


@app.post("/outputs/delete")
async def outputs_delete(request: Request):
    body = await request.json()
    name = os.path.basename(body.get("file", ""))  # no path traversal
    path = os.path.join(config.OUTPUTS_DIR, name)
    if not name or not os.path.exists(path):
        raise ValueError("File not found.")
    os.remove(path)
    return {"deleted": name}


@app.post("/compare")
async def compare(request: Request):
    """A/B test two thumbnails (one Claude call reading both images)."""
    body = await request.json()
    path_a = compose._from_url(body.get("file_a", ""))
    path_b = compose._from_url(body.get("file_b", ""))
    for p, label in ((path_a, "A"), (path_b, "B")):
        if not p or not os.path.exists(p):
            raise ValueError(f"Thumbnail {label} not found — pick two images to compare.")
    return analyze_yt.compare_thumbnails(path_a, path_b, body.get("title", ""))


@app.get("/face/last")
def face_last():
    """The cutout that will be used by default (most recent one)."""
    path = imagery.last_used_cutout()
    return {"face": compose._to_url(path) if path else None}


@app.post("/export/zip")
async def export_zip(request: Request):
    """Bundle a set of generated PNGs into one downloadable zip."""
    import zipfile
    body = await request.json()
    files = [compose._from_url(f) for f in body.get("files", [])]
    files = [f for f in files if f and os.path.exists(f)]
    if not files:
        raise ValueError("Nothing to download yet — generate thumbnails first.")
    out = os.path.join(config.OUTPUTS_DIR, f"thumbnails_{int(time.time())}.zip")
    with zipfile.ZipFile(out, "w") as zf:
        for f in files:
            zf.write(f, os.path.basename(f))
    return {"file": compose._to_url(out)}


@app.post("/cutout")
async def cutout(image: UploadFile = File(...)):
    """Remove the background from an uploaded image (editor 'add image' helper)."""
    suffix = os.path.splitext(image.filename or "x.png")[1] or ".png"
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        tmp.write(await image.read())
    return {"cutout": compose._to_url(imagery.cutout_face(tmp.name))}


@app.post("/background/adjust")
async def background_adjust(request: Request):
    """Re-render just the background image with new pan/darken/saturation."""
    body = await request.json()
    img = compose.render_background(
        compose._from_url(body["src"]), body.get("treatment", "darken_left"),
        float(body.get("darken", 0.5)), int(body.get("shift_x", 0)),
        float(body.get("saturation", 1.0)))
    out = os.path.join(config.OUTPUTS_DIR, f"bgadj_{int(time.time()*1000)}.png")
    img.save(out, "PNG")
    return {"file": compose._to_url(out)}


@app.post("/freeform")
async def freeform(request: Request):
    """Free-form edit: send current layer state + instruction to Claude,
    apply the returned updated state to the canvas."""
    body = await request.json()
    prompt = f"""You are editing a YouTube thumbnail in a Fabric.js canvas (1280x720).
Here is the current layer state as JSON (Fabric object list; left/top are pixels,
text objects have fill/stroke/fontSize/text, images have scaleX/scaleY/flipX):

{json.dumps(body['state'])[:14000]}

User instruction: {body['instruction']}

Return the SAME JSON structure with ONLY the properties needed to satisfy the
instruction changed. Keep every object (same order, same count) and keep all
unrelated properties identical. Return the full updated JSON object."""
    return {"state": config.claude_json(prompt)}


@app.post("/export")
async def export(request: Request):
    """Save the canvas PNG (data URL, exactly 1280x720) to outputs/."""
    body = await request.json()
    data_url = body["png"]
    raw = base64.b64decode(data_url.split(",", 1)[1])
    name = re.sub(r"[^A-Za-z0-9_-]", "_", body.get("name", "thumbnail")) or "thumbnail"
    out = os.path.join(config.OUTPUTS_DIR, f"{name}_{int(time.time())}.png")
    with open(out, "wb") as f:
        f.write(raw)
    return {"file": compose._to_url(out)}


@app.post("/templates/save")
async def templates_save(request: Request):
    """Save the current layout as a new style JSON."""
    body = await request.json()
    sid = library.save_style(body["style"])
    return {"id": sid}


@app.post("/projects/save")
async def projects_save(request: Request):
    body = await request.json()
    name = re.sub(r"[^A-Za-z0-9_-]", "_", body.get("name", "project")) or "project"
    path = os.path.join(config.PROJECTS_DIR, f"{name}.json")
    with open(path, "w") as f:
        json.dump({"name": name, "saved_at": time.time(), "state": body["state"]}, f)
    return {"name": name}


@app.get("/projects/list")
def projects_list():
    items = []
    for n in sorted(os.listdir(config.PROJECTS_DIR)):
        if n.endswith(".json"):
            items.append(n[:-5])
    return {"projects": items}


@app.get("/projects/load")
def projects_load(name: str):
    path = os.path.join(config.PROJECTS_DIR,
                        re.sub(r"[^A-Za-z0-9_-]", "_", name) + ".json")
    if not os.path.exists(path):
        raise ValueError(f'Project "{name}" not found.')
    with open(path) as f:
        return json.load(f)


# ============================ TOOL B — ANALYZE =================================

@app.post("/analyze")
async def analyze(request: Request):
    """Fetch + rate. Face candidates and remakes are separate calls so the
    page can show the scorecard immediately."""
    body = await request.json()
    fetched = analyze_yt.fetch_video(body["url"])
    rating = analyze_yt.rate_thumbnail(
        fetched["thumbnail_path"], fetched["meta"]["title"], fetched["transcript"])
    return {
        "meta": fetched["meta"],
        "thumbnail": compose._to_url(fetched["thumbnail_path"]),
        "transcript_available": fetched["transcript_available"],
        "transcript": fetched["transcript"][:8000],
        "rating": rating,
    }


@app.post("/analyze/face-candidates")
async def analyze_face_candidates(request: Request):
    body = await request.json()
    return {"candidates": analyze_yt.face_candidates(body["channel_id"])}


@app.post("/analyze/remake")
async def analyze_remake(request: Request):
    body = await request.json()
    briefs = analyze_yt.remake_briefs(
        body["title"], body.get("transcript", ""), body.get("weaknesses", []))
    face_path = compose._from_url(body["face"]) if body.get("face") else None
    return analyze_yt.build_remakes(briefs, face_path)


@app.post("/analyze/rate-image")
async def analyze_rate_image(request: Request):
    """'Rate my remake': re-run the RATE step on an exported edit."""
    body = await request.json()
    path = compose._from_url(body["file"])
    if not path or not os.path.exists(path):
        raise ValueError("Export the thumbnail first, then rate it.")
    rating = analyze_yt.rate_thumbnail(path, body.get("title", ""),
                                       body.get("transcript", ""))
    return {"rating": rating}


# Static mounts (after routes so endpoint paths win).
app.mount("/static", StaticFiles(directory=os.path.join(config.BASE_DIR, "static")), name="static")
app.mount("/assets", StaticFiles(directory=os.path.join(config.BASE_DIR, "assets")), name="assets")
app.mount("/outputs", StaticFiles(directory=config.OUTPUTS_DIR), name="outputs")
