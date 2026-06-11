"""Style + brief -> layer description AND flattened 1280x720 PNG.

layers() produces the editable description the Fabric.js editor consumes;
flatten() renders the exact same description to pixels with Pillow.
Positions/scales in the description are fractions of the 1280x720 canvas.
"""
import math
import os
import time

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

import config

W, H = 1280, 720


# --- layer description -------------------------------------------------------

def layers(style, brief, assets, brand=None):
    """Build the layer stack for one thumbnail.

    style:  style JSON dict
    brief:  {"text": "...", "focus_subject": "..."} (text drives the text layer)
    assets: {"background": local path, "face": local path or None}
    brand:  optional brand kit; when enabled it locks the text font/colors and
            recolors decorative extras with the brand accent.
    """
    if brand and brand.get("enabled"):
        style = _apply_brand(style, brand)
    spec = {"canvas": {"width": W, "height": H}, "style_id": style["id"], "layers": []}

    bg = style["background"]
    # Pre-render the treated background once so the editor canvas and the
    # flattened PNG use the exact same pixels.
    rendered = render_background(assets["background"], bg["treatment"],
                                 bg["darken"], bg.get("shift_x", 0),
                                 bg.get("saturation", 1.0))
    rendered_path = os.path.join(config.OUTPUTS_DIR, f"bg_{int(time.time()*1000)}.png")
    rendered.save(rendered_path, "PNG")
    spec["layers"].append({
        "type": "background",
        "src": _to_url(assets["background"]),
        "rendered_src": _to_url(rendered_path),
        "treatment": bg["treatment"],
        "darken": bg["darken"],
        "shift_x": bg.get("shift_x", 0),
        "saturation": bg.get("saturation", 1.0),
    })

    face = style["face"]
    if assets.get("face"):
        x_frac = {"left": 0.0, "center": 0.5, "right": 1.0}[face["anchor"]]
        spec["layers"].append({
            "type": "face",
            "src": _to_url(assets["face"]),
            "height_frac": face["height_frac"],
            "anchor": face["anchor"],
            "x_frac": x_frac,
            "x_bleed_px": face.get("x_bleed_px", 0),
            "rim_light": face.get("rim_light", True),
            "drop_shadow": face.get("drop_shadow", True),
        })

    for extra in style.get("extras", []):
        spec["layers"].append(dict(extra, type="extra", shape=extra["type"]))

    txt = style["text"]
    words = (brief.get("text") or "").split()
    text_value = " ".join(words[: txt["max_words"]])
    if txt["case"] == "upper":
        text_value = text_value.upper()
    elif txt["case"] == "title":
        text_value = text_value.title()
    spec["layers"].append({
        "type": "text",
        "value": text_value,
        "position": txt["position"],
        "font": txt["font"],
        "start_size": txt["start_size"],
        "max_lines": txt["max_lines"],
        "fill": txt["fill"],
        "stroke": txt["stroke"],
        "stroke_width": txt["stroke_width"],
        "accent_bar": txt.get("accent_bar", False),
    })
    return spec


def _apply_brand(style, brand):
    """Return a copy of the style with brand colors/font locked in."""
    import copy
    s = copy.deepcopy(style)
    s["text"]["font"] = brand["font"]
    s["text"]["fill"] = brand["headline_fill"]
    s["text"]["stroke"] = brand["stroke"]
    accent = brand["accent"]
    for extra in s.get("extras", []):
        if extra["type"] == "circle":
            extra["stroke"] = accent
        elif extra["type"] == "arrow":
            extra["fill"] = accent
        elif extra["type"] in ("badge", "banner"):
            extra["fill"] = accent
            extra["text_fill"] = brand["stroke"]
    return s


def _to_url(path):
    """Local asset path -> URL the browser can load (served from /assets etc.)."""
    if not path:
        return None
    rel = os.path.relpath(os.path.abspath(path), config.BASE_DIR)
    return "/" + rel.replace(os.sep, "/")


def _from_url(src):
    return os.path.join(config.BASE_DIR, src.lstrip("/")) if src else None


# --- flatten ------------------------------------------------------------------

def flatten(spec, out_name=None):
    """Render a layer description to a 1280x720 PNG in outputs/. Returns path."""
    canvas = Image.new("RGB", (W, H), "#101010")
    for layer in spec["layers"]:
        kind = layer["type"]
        if kind == "background":
            _draw_background(canvas, layer)
        elif kind == "face":
            _draw_face(canvas, layer)
        elif kind == "extra":
            _draw_extra(canvas, layer)
        elif kind == "text":
            _draw_text(canvas, layer)
    out_name = out_name or f"{spec.get('style_id', 'thumb')}_{int(time.time() * 1000)}.png"
    out_path = os.path.join(config.OUTPUTS_DIR, out_name)
    canvas.save(out_path, "PNG")
    return out_path


def render_background(path, treatment, darken, shift_x, saturation):
    """Background pipeline shared by flatten() and /background/adjust:
    cover-fit to 1280x720, pan, saturate, then gradient darkening."""
    img = Image.open(path).convert("RGB")
    scale = max(W / img.width, H / img.height)
    img = img.resize((round(img.width * scale), round(img.height * scale)),
                     Image.LANCZOS)
    left = (img.width - W) // 2 + int(shift_x)
    left = max(0, min(img.width - W, left))
    top = (img.height - H) // 2
    img = img.crop((left, top, left + W, top + H))
    if saturation != 1.0:
        img = ImageEnhance.Color(img).enhance(saturation)
    return _apply_darkening(img, treatment, darken)


def _draw_background(canvas, layer):
    if layer.get("rendered_src"):  # already treated when layers() ran
        img = Image.open(_from_url(layer["rendered_src"])).convert("RGB")
        img = img.resize((W, H)) if img.size != (W, H) else img
    else:
        img = render_background(_from_url(layer["src"]), layer["treatment"],
                                layer["darken"], layer.get("shift_x", 0),
                                layer.get("saturation", 1.0))
    canvas.paste(img, (0, 0))


def _apply_darkening(img, treatment, darken):
    """All darkening is done with smooth gradients — never hard-edge rectangles."""
    overlay = Image.new("L", (W, H), 0)
    if treatment in ("darken_left", "split_desaturate_left"):
        for x in range(W):
            # strongest on the left, fading to nothing past 60% width
            strength = max(0.0, 1.0 - x / (W * 0.6))
            _set_column(overlay, x, int(255 * darken * strength))
    elif treatment == "darken_bottom":
        for y in range(H):
            strength = max(0.0, (y - H * 0.45) / (H * 0.55))
            _set_row(overlay, y, int(255 * darken * strength))
    elif treatment in ("red_vignette", "dark_vignette"):
        cx, cy = W / 2, H / 2
        max_d = math.hypot(cx, cy)
        px = overlay.load()
        for y in range(0, H, 2):  # step 2 then resize: 4x faster, visually identical
            for x in range(0, W, 2):
                strength = (math.hypot(x - cx, y - cy) / max_d) ** 1.5
                px[x, y] = int(255 * darken * strength)
        overlay = overlay.resize((W // 2, H // 2)).resize((W, H), Image.BILINEAR)
    else:  # uniform gentle darken
        overlay = Image.new("L", (W, H), int(255 * darken * 0.5))

    if treatment == "split_desaturate_left":
        # left half loses color (the "before" side), blended with a soft seam
        gray = ImageEnhance.Color(img).enhance(0.1)
        mask = Image.new("L", (W, H), 0)
        for x in range(W):
            _set_column(mask, x, max(0, min(255, int(255 * (0.55 - x / W) / 0.1))))
        img = Image.composite(gray, img, mask)

    color = (120, 0, 0) if treatment == "red_vignette" else (0, 0, 0)
    tint = Image.new("RGB", (W, H), color)
    return Image.composite(tint, img, overlay)


def _set_column(img_l, x, value):
    ImageDraw.Draw(img_l).line([(x, 0), (x, H)], fill=value)


def _set_row(img_l, y, value):
    ImageDraw.Draw(img_l).line([(0, y), (W, y)], fill=value)


def _draw_face(canvas, layer):
    cut = Image.open(_from_url(layer["src"])).convert("RGBA")
    target_h = int(H * layer["height_frac"])
    scale = target_h / cut.height
    cut = cut.resize((round(cut.width * scale), target_h), Image.LANCZOS)

    bleed = layer.get("x_bleed_px", 0)
    anchor = layer.get("anchor", "right")
    if anchor == "right":
        x = W - cut.width + bleed
    elif anchor == "left":
        x = -bleed
    else:
        x = (W - cut.width) // 2
    y = H - cut.height  # faces always sit on the bottom edge

    if layer.get("drop_shadow", True):
        # soft shadow = blurred copy of the alpha, offset down-left
        shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        alpha = cut.getchannel("A").point(lambda a: int(a * 0.55))
        black = Image.new("RGBA", cut.size, (0, 0, 0, 255))
        black.putalpha(alpha)
        shadow.paste(black, (x - 12, y + 10), black)
        shadow = shadow.filter(ImageFilter.GaussianBlur(14))
        canvas.paste(shadow, (0, 0), shadow)

    if layer.get("rim_light", True):
        # 2-3px light rim traced on the alpha edge: dilated alpha minus alpha
        alpha = cut.getchannel("A")
        dilated = alpha.filter(ImageFilter.MaxFilter(7))
        rim_mask = Image.eval(Image.composite(
            Image.new("L", cut.size, 0), dilated, alpha), lambda v: v)
        rim = Image.new("RGBA", cut.size, (255, 244, 214, 255))
        rim.putalpha(rim_mask.point(lambda a: int(a * 0.9)))
        canvas.paste(rim, (x, y), rim)

    canvas.paste(cut, (x, y), cut)


def _draw_extra(canvas, layer):
    draw = ImageDraw.Draw(canvas, "RGBA")
    shape = layer["shape"]
    if shape == "circle":
        cx, cy = layer["x_frac"] * W, layer["y_frac"] * H
        r = layer["r_frac"] * W
        draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                     outline=layer.get("stroke", "#FF2A2A"),
                     width=layer.get("stroke_width", 10))
    elif shape == "arrow":
        _draw_arrow(draw, layer)
    elif shape == "badge":
        cx, cy = layer["x_frac"] * W, layer["y_frac"] * H
        r = layer.get("size_frac", 0.15) * H
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=layer.get("fill", "#E60000"))
        font = _load_font("Anton", int(r * 1.0))
        draw.text((cx, cy), layer.get("label", "!"), font=font,
                  fill=layer.get("text_fill", "#FFFFFF"), anchor="mm")
    elif shape == "banner":
        y = layer.get("y_frac", 0) * H
        bh = layer.get("height_frac", 0.12) * H
        draw.rectangle([0, y, W, y + bh], fill=layer.get("fill", "#C00000"))
        font = _load_font("Anton", int(bh * 0.72))
        draw.text((W * 0.03, y + bh / 2), layer.get("label", ""),
                  font=font, fill=layer.get("text_fill", "#FFFFFF"), anchor="lm")


def _draw_arrow(draw, layer):
    x1, y1 = layer["from"][0] * W, layer["from"][1] * H
    x2, y2 = layer["to"][0] * W, layer["to"][1] * H
    width = layer.get("width", 24)
    fill = layer.get("fill", "#FF2A2A")
    angle = math.atan2(y2 - y1, x2 - x1)
    head = width * 2.4
    # shaft stops where the head begins
    sx, sy = x2 - head * math.cos(angle), y2 - head * math.sin(angle)
    draw.line([x1, y1, sx, sy], fill=fill, width=width)
    left = (x2 - head * math.cos(angle - 0.45), y2 - head * math.sin(angle - 0.45))
    right = (x2 - head * math.cos(angle + 0.45), y2 - head * math.sin(angle + 0.45))
    draw.polygon([(x2, y2), left, right], fill=fill)


# --- text ---------------------------------------------------------------------

TEXT_REGIONS = {
    # position -> (x_frac, y_frac, width_frac, vertical anchor, horizontal align)
    "left":         (0.04, 0.50, 0.55, "middle", "left"),
    "right":        (0.41, 0.50, 0.55, "middle", "right"),
    "top":          (0.04, 0.10, 0.92, "top", "center"),
    "bottom":       (0.04, 0.97, 0.92, "bottom", "center"),
    "top-left":     (0.04, 0.06, 0.55, "top", "left"),
    "bottom-right": (0.41, 0.96, 0.55, "bottom", "right"),
}


def _load_font(name, size):
    """Font from assets/fonts by family name; falls back to DejaVu so the app
    still renders before the user downloads Anton/Archivo Black."""
    candidates = [name.replace(" ", ""), name.replace(" ", "-"), name]
    for c in candidates:
        for ext in (".ttf", ".otf"):
            path = os.path.join(config.FONTS_DIR, c + ext)
            if os.path.exists(path):
                return ImageFont.truetype(path, size)
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
    except OSError:
        return ImageFont.load_default(size)


def _wrap(text, font, max_width, draw):
    """Greedy word wrap to a pixel width."""
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_width or not line:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def _draw_text(canvas, layer):
    if not layer.get("value"):
        return
    draw = ImageDraw.Draw(canvas)
    region = TEXT_REGIONS.get(layer["position"], TEXT_REGIONS["left"])
    rx, ry, rw, v_anchor, align = region
    max_width = rw * W
    size = layer["start_size"]
    # auto-shrink until the wrap fits max_lines (and no single word overflows)
    while size > 24:
        font = _load_font(layer["font"], size)
        lines = _wrap(layer["value"], font, max_width, draw)
        widest = max(draw.textlength(l, font=font) for l in lines)
        if len(lines) <= layer["max_lines"] and widest <= max_width:
            break
        size = int(size * 0.92)
    line_h = size * 1.08
    block_h = line_h * len(lines)
    if v_anchor == "middle":
        y = ry * H - block_h / 2
    elif v_anchor == "bottom":
        y = ry * H - block_h
    else:
        y = ry * H

    if layer.get("accent_bar"):
        bar_x = rx * W - 4
        draw.rectangle([bar_x - 18, y + 6, bar_x - 4, y + block_h - 6],
                       fill=layer["fill"])

    for line in lines:
        lw = draw.textlength(line, font=font)
        if align == "center":
            x = rx * W + (max_width - lw) / 2
        elif align == "right":
            x = rx * W + max_width - lw
        else:
            x = rx * W
        draw.text((x, y), line, font=font, fill=layer["fill"],
                  stroke_width=layer.get("stroke_width", 0),
                  stroke_fill=layer.get("stroke"))
        y += line_h
