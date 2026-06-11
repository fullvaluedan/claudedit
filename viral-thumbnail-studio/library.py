"""Template/asset library helpers + CLI to add backgrounds to the cache.

Usage from the command line:
    python library.py add path/to/image.jpg --subject "bitcoin chart" --tags "crypto,chart"
"""
import argparse
import hashlib
import json
import os
import re
import shutil

import config


def list_styles():
    """All style JSONs. User-saved styles (user_ prefix) come first so they
    win in style pickers."""
    styles = []
    for name in sorted(os.listdir(config.STYLES_DIR)):
        if not name.endswith(".json"):
            continue
        with open(os.path.join(config.STYLES_DIR, name)) as f:
            styles.append(json.load(f))
    # User styles first, then built-ins, each alphabetical.
    styles.sort(key=lambda s: (0 if s["id"].startswith("user_") else 1, s["id"]))
    return styles


def get_style(style_id):
    for s in list_styles():
        if s["id"] == style_id:
            return s
    raise KeyError(f"Unknown style: {style_id}")


# Defaults merged into saved styles so a minimal/partial template still
# composes without KeyErrors.
DEFAULT_STYLE = {
    "description": "User template saved from the editor.",
    "face": {"height_frac": 0.85, "anchor": "right", "x_bleed_px": 30,
             "rim_light": True, "drop_shadow": True},
    "text": {"position": "left", "max_words": 4, "case": "upper", "font": "Anton",
             "start_size": 130, "max_lines": 2, "fill": "#FFFFFF",
             "stroke": "#000000", "stroke_width": 8, "accent_bar": False},
    "background": {"treatment": "darken_left", "darken": 0.5, "shift_x": 0,
                   "saturation": 1.1,
                   "prompt_style_suffix": "dramatic lighting, bold colors, high contrast"},
    "extras": [],
}


def save_style(style):
    """Save a user-created style: sanitize the id, ensure a user_ prefix so it
    sorts first, and fill any missing fields with safe defaults."""
    sid = re.sub(r"[^a-z0-9_]+", "_", str(style.get("id", "untitled")).strip().lower())
    sid = sid.strip("_") or "untitled"
    if not sid.startswith("user_"):
        sid = "user_" + sid
    merged = json.loads(json.dumps(DEFAULT_STYLE))  # deep copy
    for key, value in style.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key].update(value)
        else:
            merged[key] = value
    merged["id"] = sid
    merged.setdefault("name", sid)
    path = os.path.join(config.STYLES_DIR, sid + ".json")
    with open(path, "w") as f:
        json.dump(merged, f, indent=2)
    return sid


# --- brand kit ---------------------------------------------------------------

BRAND_PATH = os.path.join(config.BASE_DIR, "templates", "brand.json")

# Defaults seeded from the channel design system (DESIGN.md): white headlines,
# near-black stroke, cyan accent used sparingly. Disabled until switched on.
DEFAULT_BRAND = {
    "enabled": False,
    "font": "Anton",
    "headline_fill": "#FFFFFF",
    "stroke": "#0A0A0A",
    "accent": "#00D4FF",
}

_HEX = re.compile(r"^#[0-9a-fA-F]{6}$")


def load_brand():
    if os.path.exists(BRAND_PATH):
        with open(BRAND_PATH) as f:
            return {**DEFAULT_BRAND, **json.load(f)}
    return dict(DEFAULT_BRAND)


def save_brand(brand):
    """Validate + persist the brand kit. Bad colors fall back to defaults."""
    clean = dict(DEFAULT_BRAND)
    clean["enabled"] = bool(brand.get("enabled"))
    clean["font"] = str(brand.get("font") or DEFAULT_BRAND["font"])[:40]
    for key in ("headline_fill", "stroke", "accent"):
        value = str(brand.get(key, "")).strip()
        if _HEX.match(value):
            clean[key] = value.upper()
    with open(BRAND_PATH, "w") as f:
        json.dump(clean, f, indent=2)
    return clean


# --- background cache manifest -------------------------------------------

MANIFEST_PATH = os.path.join(config.BACKGROUNDS_DIR, "manifest.json")


def load_manifest():
    if os.path.exists(MANIFEST_PATH):
        with open(MANIFEST_PATH) as f:
            return json.load(f)
    return []


def save_manifest(entries):
    with open(MANIFEST_PATH, "w") as f:
        json.dump(entries, f, indent=2)


def add_background(file_path, focus_subject, tags, source="manual"):
    """Copy an image into the background cache and register it in the manifest."""
    with open(file_path, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()[:16]
    ext = os.path.splitext(file_path)[1].lower() or ".jpg"
    dest_name = f"{digest}{ext}"
    dest = os.path.join(config.BACKGROUNDS_DIR, dest_name)
    if not os.path.exists(dest):
        shutil.copyfile(file_path, dest)
    entries = load_manifest()
    if not any(e["key"] == digest for e in entries):
        entries.append({
            "key": digest,
            "focus_subject": focus_subject.strip().lower(),
            "tags": [t.strip().lower() for t in tags if t.strip()],
            "source": source,
            "file": dest_name,
        })
        save_manifest(entries)
    return dest


def find_cached_background(focus_subject):
    """Manifest match: exact focus_subject, else any tag appearing in the subject."""
    subject = focus_subject.strip().lower()
    entries = load_manifest()
    for e in entries:
        if e["focus_subject"] == subject:
            return os.path.join(config.BACKGROUNDS_DIR, e["file"])
    words = set(subject.split())
    for e in entries:
        if words & set(e["tags"]):
            return os.path.join(config.BACKGROUNDS_DIR, e["file"])
    return None


def main():
    parser = argparse.ArgumentParser(description="Asset library tools")
    sub = parser.add_subparsers(dest="cmd", required=True)
    add = sub.add_parser("add", help="Add a background image to the cache")
    add.add_argument("file")
    add.add_argument("--subject", required=True, help='e.g. "bitcoin chart"')
    add.add_argument("--tags", default="", help='comma separated, e.g. "crypto,chart"')
    args = parser.parse_args()
    if args.cmd == "add":
        dest = add_background(args.file, args.subject, args.tags.split(","))
        print(f"Added {dest} (subject: {args.subject})")


if __name__ == "__main__":
    main()
