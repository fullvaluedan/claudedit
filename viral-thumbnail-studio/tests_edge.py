"""Edge-case battery. Run with the server up:  .venv/bin/python tests_edge.py"""
import io
import os

import requests
from PIL import Image

B = "http://127.0.0.1:8000"
results = []


def check(name, fn):
    try:
        fn()
        results.append(("PASS", name))
    except AssertionError as e:
        results.append(("FAIL", f"{name}: {e}"))
    except Exception as e:
        results.append(("ERROR", f"{name}: {type(e).__name__} {e}"))


def t_invalid_yt_url():
    r = requests.post(B + "/analyze", json={"url": "https://example.com/notavideo"})
    assert r.status_code == 400, r.status_code
    assert "YouTube" in r.json()["error"], r.json()


def t_missing_url_key():
    r = requests.post(B + "/analyze", json={})
    assert r.status_code in (400, 422), r.status_code
    assert "error" in r.json() or "detail" in r.json(), r.text


def t_nonexistent_project():
    r = requests.get(B + "/projects/load", params={"name": "does_not_exist"})
    assert r.status_code == 400, (r.status_code, r.text)
    assert "error" in r.json(), r.text


def t_malformed_export():
    r = requests.post(B + "/export", json={"png": "not-a-data-url", "name": "x"})
    assert r.status_code in (400, 500), r.status_code
    assert "error" in r.json(), r.text


def t_unknown_style():
    r = requests.post(B + "/compose", json={"items": [{"brief": {
        "style_id": "nope", "text": "X", "focus_subject": "y"},
        "chosen_file": "/outputs/x.png"}]})
    assert r.status_code == 400, (r.status_code, r.text)
    assert "nope" in r.json()["error"], r.json()


def t_missing_chosen_file():
    r = requests.post(B + "/compose", json={"items": [{"brief": {
        "style_id": "big_number", "text": "X", "focus_subject": "y"},
        "chosen_file": "/outputs/ghost.png"}]})
    assert r.status_code in (400, 500), r.status_code
    assert "error" in r.json(), r.text


def _edge_bg():
    img = Image.new("RGB", (1280, 720), "blue")
    buf = io.BytesIO()
    img.save(buf, "PNG")
    with open("outputs/edge_bg.png", "wb") as f:
        f.write(buf.getvalue())


def t_minimal_template_composes():
    """A user template saved with missing fields must still compose."""
    r = requests.post(B + "/templates/save", json={"style": {"id": "edge", "name": "Edge"}})
    assert r.status_code == 200, r.text
    sid = r.json()["id"]
    _edge_bg()
    r2 = requests.post(B + "/compose", json={"items": [{"brief": {
        "style_id": sid, "text": "HELLO", "focus_subject": "z"},
        "chosen_file": "/outputs/edge_bg.png"}]})
    assert r2.status_code == 200, (r2.status_code, r2.text[:200])


def t_cutout_non_image():
    r = requests.post(B + "/cutout", files={"image": ("x.png", b"this is not an image")})
    assert r.status_code in (400, 500), r.status_code
    assert "error" in r.json(), r.text


def t_adjust_missing_src():
    r = requests.post(B + "/background/adjust", json={
        "src": "/assets/backgrounds/ghost.jpg", "treatment": "darken_left",
        "darken": 0.5, "shift_x": 0, "saturation": 1})
    assert r.status_code in (400, 500), r.status_code
    assert "error" in r.json(), r.text


def t_extreme_adjust_values():
    _edge_bg()
    r = requests.post(B + "/background/adjust", json={
        "src": "/outputs/edge_bg.png", "treatment": "darken_bottom",
        "darken": 5.0, "shift_x": 99999, "saturation": -3})
    assert r.status_code == 200, (r.status_code, r.text[:200])


def t_weird_text_flattens():
    import compose
    import library
    _edge_bg()
    s = library.get_style("big_number")
    for txt in ["   ", "🚀🚀🚀 MOON", "SUPERCALIFRAGILISTICEXPIALIDOCIOUS LONGWORD", "x"]:
        spec = compose.layers(s, {"text": txt, "focus_subject": "t"},
                              {"background": "outputs/edge_bg.png", "face": None})
        png = compose.flatten(spec)
        assert Image.open(png).size == (1280, 720)


def t_compose_without_face():
    _edge_bg()
    r = requests.post(B + "/compose", json={"items": [{"brief": {
        "style_id": "vs_split", "text": "NO FACE", "focus_subject": "y"},
        "chosen_file": "/outputs/edge_bg.png"}]})
    assert r.status_code == 200, (r.status_code, r.text[:300])


def t_project_name_traversal():
    r = requests.post(B + "/projects/save", json={"name": "../../evil", "state": {}})
    assert r.status_code == 200
    assert not os.path.exists("../evil.json") and not os.path.exists("../../evil.json")
    assert "/" not in r.json()["name"]


def t_rate_image_missing():
    r = requests.post(B + "/analyze/rate-image", json={"file": "/outputs/never.png", "title": "t"})
    assert r.status_code == 400, r.status_code
    assert "Export" in r.json()["error"], r.json()


def t_style_id_sanitized():
    r = requests.post(B + "/templates/save", json={"style": {"id": "My Cool/Style!!", "name": "x"}})
    assert r.status_code == 200, r.text
    sid = r.json()["id"]
    assert "/" not in sid and "!" not in sid, sid


def t_freeform_missing_keys():
    r = requests.post(B + "/freeform", json={"instruction": "x"})
    assert r.status_code in (400, 422, 500), r.status_code
    assert "error" in r.json(), r.text


def t_generate_empty_topic():
    r = requests.post(B + "/generate", data={"topic": "   ", "mode": "auto"})
    assert r.status_code == 400, (r.status_code, r.text[:200])
    assert "topic" in r.json()["error"].lower(), r.json()


def t_face_last_empty_ok():
    r = requests.get(B + "/face/last")
    assert r.status_code == 200, r.text
    assert "face" in r.json()


def t_zip_empty_files():
    r = requests.post(B + "/export/zip", json={"files": []})
    assert r.status_code == 400, r.status_code
    assert "error" in r.json(), r.text


def t_zip_real_files():
    _edge_bg()
    r = requests.post(B + "/export/zip", json={"files": ["/outputs/edge_bg.png", "/outputs/ghost.png"]})
    assert r.status_code == 200, r.text
    assert r.json()["file"].endswith(".zip")


ALL = [v for k, v in sorted(globals().items()) if k.startswith("t_")]

if __name__ == "__main__":
    for fn in ALL:
        check(fn.__name__, fn)
    failed = [r for r in results if r[0] != "PASS"]
    for status, name in results:
        print(f"{status:5} {name}")
    print(f"\n{len(results) - len(failed)}/{len(results)} passed")
    raise SystemExit(1 if failed else 0)
