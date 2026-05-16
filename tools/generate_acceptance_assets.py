from __future__ import annotations

import hashlib
import json
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def color(hex_value: str, alpha: int = 255) -> tuple[int, int, int, int]:
    hex_value = hex_value.lstrip("#")
    return (
        int(hex_value[0:2], 16),
        int(hex_value[2:4], 16),
        int(hex_value[4:6], 16),
        alpha,
    )


INK = color("#2f2a22")
PAPER = color("#e8dcc4")
PAPER_DARK = color("#d8c8a7")
GOLD = color("#b78a30")
GOLD_LIGHT = color("#e1bd65")
BLACK = color("#171611")


def ensure_dirs() -> None:
    for name in ["cards", "icons", "map", "status", "ui", "preview"]:
        (ASSETS / name).mkdir(parents=True, exist_ok=True)


def paper_layer(size: tuple[int, int], seed: int, base: tuple[int, int, int, int] = PAPER) -> Image.Image:
    rng = random.Random(seed)
    image = Image.new("RGBA", size, base)
    draw = ImageDraw.Draw(image, "RGBA")
    w, h = size
    for _ in range(max(80, (w * h) // 9000)):
        x = rng.randrange(w)
        y = rng.randrange(h)
        radius = rng.randrange(1, 4)
        tone = rng.choice([color("#f3ead9", 20), color("#a4895d", 16), color("#ffffff", 12)])
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=tone)
    for _ in range(max(18, w // 18)):
        y = rng.randrange(h)
        x0 = rng.randrange(-w // 5, w)
        x1 = x0 + rng.randrange(w // 8, w // 2)
        draw.line((x0, y, x1, y + rng.randrange(-3, 4)), fill=color("#8d7755", 22), width=1)
    return image


def draw_shadow(base: Image.Image, box: tuple[int, int, int, int], radius: int, opacity: int = 70) -> None:
    shadow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(shadow, "RGBA")
    x0, y0, x1, y1 = box
    draw.rounded_rectangle((x0 + 6, y0 + 8, x1 + 6, y1 + 8), radius=radius, fill=(0, 0, 0, opacity))
    shadow = shadow.filter(ImageFilter.GaussianBlur(8))
    base.alpha_composite(shadow)


def draw_corner(draw: ImageDraw.ImageDraw, x: int, y: int, sx: int, sy: int, line: tuple[int, int, int, int]) -> None:
    x2 = x + sx * 46
    y2 = y + sy * 46
    box = (min(x, x2), min(y, y2), max(x, x2), max(y, y2))
    draw.arc(box, start=0 if sx > 0 else 180, end=90 if sy > 0 else 270, fill=line, width=3)
    draw.line((x, y + sy * 20, x + sx * 42, y + sy * 20), fill=line, width=2)
    draw.line((x + sx * 20, y, x + sx * 20, y + sy * 42), fill=line, width=2)
    draw.ellipse((x + sx * 34 - 4, y + sy * 34 - 4, x + sx * 34 + 4, y + sy * 34 + 4), fill=line)


def save(image: Image.Image, relative: str) -> None:
    path = ASSETS / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path)


def make_card_frame(relative: str, accent: tuple[int, int, int, int], seed: int, motif: str) -> None:
    w, h = 512, 736
    image = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw_shadow(image, (16, 16, w - 16, h - 16), 30, 72)
    paper = paper_layer((w, h), seed, color("#eee2cb"))
    mask = Image.new("L", (w, h), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle((18, 18, w - 18, h - 18), radius=30, fill=255)
    image.alpha_composite(Image.composite(paper, Image.new("RGBA", (w, h), (0, 0, 0, 0)), mask))
    draw = ImageDraw.Draw(image, "RGBA")

    draw.rounded_rectangle((18, 18, w - 18, h - 18), radius=30, outline=accent, width=9)
    draw.rounded_rectangle((31, 31, w - 31, h - 31), radius=23, outline=GOLD_LIGHT, width=3)
    draw.rounded_rectangle((44, 44, w - 44, h - 44), radius=17, outline=color("#2a2118", 210), width=2)
    draw.rounded_rectangle((57, 57, w - 57, h - 57), radius=12, outline=color("#ffffff", 45), width=1)

    for y in range(138, 624, 48):
        draw.line((78, y, w - 70, y + 12), fill=color("#8a785e", 28), width=1)
    for x in range(128, w - 86, 52):
        draw.arc((x, 600, x + 86, 706), 200, 340, fill=color("#52685f", 28), width=2)

    draw.rounded_rectangle((31, 27, 119, 115), radius=44, fill=accent, outline=GOLD_LIGHT, width=6)
    draw.ellipse((45, 41, 105, 101), outline=color("#f7ead0"), width=3)
    draw.arc((54, 51, 96, 93), 40, 315, fill=color("#fff6dd", 95), width=3)

    draw.rounded_rectangle((51, 148, 105, h - 112), radius=10, fill=color("#171611", 242), outline=GOLD, width=3)
    draw.line((78, 166, 78, h - 130), fill=accent, width=2)
    draw.ellipse((63, 166, 93, 196), fill=accent, outline=GOLD_LIGHT, width=3)
    draw.ellipse((63, h - 158, 93, h - 128), fill=accent, outline=GOLD_LIGHT, width=3)

    title_box = (128, 42, w - 54, 106)
    draw.rounded_rectangle(title_box, radius=12, fill=color("#efe3cb", 244), outline=accent, width=3)
    draw.line((title_box[0] + 20, title_box[1] + 12, title_box[2] - 20, title_box[1] + 12), fill=color("#7d694d", 46), width=2)
    draw.line((title_box[0] + 28, title_box[3] - 13, title_box[2] - 28, title_box[3] - 13), fill=color("#ffffff", 75), width=2)

    art_box = (128, 158, w - 56, 370)
    draw.rounded_rectangle(art_box, radius=12, fill=color("#ded4bc", 232), outline=accent, width=3)
    art = Image.new("RGBA", (art_box[2] - art_box[0], art_box[3] - art_box[1]), (0, 0, 0, 0))
    art_draw = ImageDraw.Draw(art, "RGBA")
    rng = random.Random(seed + 300)
    for i in range(7):
        yy = 142 + i * 8
        art_draw.arc((-70 + i * 22, yy - 85, 235 + i * 22, yy + 80), 190, 345, fill=color("#45564b", 48), width=2)
    for _ in range(10):
        x = rng.randrange(18, art.size[0] - 18)
        y = rng.randrange(18, art.size[1] - 18)
        art_draw.line((x, y, x + rng.randrange(28, 86), y + rng.randrange(-18, 14)), fill=color("#7c6548", 50), width=1)
    if motif == "attack":
        for offset in [70, 108, 146]:
            art_draw.line((offset, 34, offset + 74, 150), fill=color("#74b7cb", 135), width=5)
            art_draw.line((offset + 12, 42, offset + 84, 158), fill=color("#f4fbff", 145), width=2)
        art_draw.arc((52, 92, 260, 210), 195, 338, fill=color("#2c8bb0", 100), width=4)
    elif motif == "defense":
        cx, cy = art.size[0] // 2, 104
        for r in [34, 58, 82]:
            art_draw.ellipse((cx - r, cy - r, cx + r, cy + r), outline=color("#24836f", 90), width=4)
        art_draw.polygon([(cx, 38), (cx + 70, 80), (cx + 48, 158), (cx, 188), (cx - 48, 158), (cx - 70, 80)], outline=color("#24836f", 130), fill=color("#d8eadc", 35))
    elif motif == "skill":
        art_draw.rounded_rectangle((82, 42, 246, 158), radius=10, fill=color("#ead8ac", 95), outline=color("#a87921", 120), width=4)
        for y in range(62, 142, 20):
            art_draw.line((104, y, 226, y + 8), fill=color("#6d5430", 82), width=2)
        art_draw.arc((30, 98, 160, 204), 205, 345, fill=color("#a87921", 88), width=4)
    elif motif == "support":
        for x in [76, 130, 184, 238]:
            art_draw.rounded_rectangle((x, 36, x + 36, 168), radius=5, fill=color("#efe4c8", 145), outline=color("#1f8e78", 110), width=3)
            art_draw.line((x + 18, 54, x + 18, 140), fill=color("#a23b2c", 85), width=3)
            art_draw.arc((x + 7, 86, x + 29, 116), 15, 335, fill=color("#a23b2c", 92), width=2)
    else:
        for _ in range(9):
            x = rng.randrange(22, art.size[0] - 20)
            art_draw.line((x, 12, x + rng.randrange(-26, 26), art.size[1] - 16), fill=color("#6b3aa1", 118), width=3)
        for r in [36, 64, 92]:
            art_draw.arc((art.size[0] // 2 - r, 76 - r, art.size[0] // 2 + r, 76 + r), 20, 330, fill=color("#2b182d", 78), width=3)
    image.alpha_composite(art, (art_box[0], art_box[1]))

    draw.rounded_rectangle((120, 398, w - 62, 456), radius=10, fill=color("#efe3cb", 238), outline=GOLD, width=2)
    draw.line((144, 416, w - 86, 416), fill=color("#8a785e", 45), width=2)
    draw.line((158, 438, w - 100, 438), fill=color("#ffffff", 68), width=2)
    draw.rounded_rectangle((96, 482, w - 62, 630), radius=12, fill=color("#eadfc8", 232), outline=accent, width=2)
    for y in range(504, 610, 25):
        draw.line((124, y, w - 94, y + rng.randrange(-3, 4)), fill=color("#8a785e", 30), width=1)
    draw.rounded_rectangle((142, 656, w - 138, 708), radius=18, fill=accent, outline=GOLD_LIGHT, width=3)

    draw_corner(draw, 38, 38, 1, 1, GOLD_LIGHT)
    draw_corner(draw, w - 38, 38, -1, 1, GOLD_LIGHT)
    draw_corner(draw, 38, h - 38, 1, -1, GOLD_LIGHT)
    draw_corner(draw, w - 38, h - 38, -1, -1, GOLD_LIGHT)

    for x in [208, 256, 304]:
        draw.ellipse((x - 11, h - 48, x + 11, h - 26), fill=color("#d7c6a3"), outline=accent, width=3)

    save(image, relative)


def make_icon(relative: str, accent: tuple[int, int, int, int], kind: str, seed: int) -> None:
    size = 128
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw_shadow(image, (14, 14, 114, 114), 50, 48)
    draw = ImageDraw.Draw(image, "RGBA")
    draw.ellipse((14, 14, 114, 114), fill=color("#e8dcc4", 238), outline=accent, width=6)
    draw.ellipse((25, 25, 103, 103), outline=GOLD_LIGHT, width=3)
    if kind == "heart":
        draw.polygon([(64, 91), (34, 58), (44, 35), (64, 48), (84, 35), (94, 58)], fill=accent)
    elif kind == "shield":
        draw.polygon([(64, 28), (94, 41), (88, 82), (64, 101), (40, 82), (34, 41)], fill=accent)
        draw.line((64, 35, 64, 92), fill=color("#f5ead0"), width=4)
    elif kind == "drop":
        draw.polygon([(64, 25), (91, 68), (77, 97), (51, 97), (37, 68)], fill=accent)
    elif kind == "coin":
        draw.ellipse((36, 30, 92, 98), fill=accent, outline=color("#f6e2a8"), width=4)
        draw.arc((48, 42, 80, 86), 70, 290, fill=color("#7b5319"), width=4)
    elif kind == "socket":
        draw.ellipse((42, 42, 86, 86), fill=color("#f6ecd7"), outline=accent, width=5)
        draw.line((64, 26, 64, 102), fill=accent, width=3)
        draw.line((26, 64, 102, 64), fill=accent, width=3)
    elif kind == "spark":
        draw.polygon([(64, 24), (74, 54), (104, 64), (74, 74), (64, 104), (54, 74), (24, 64), (54, 54)], fill=accent)
    else:
        draw.ellipse((43, 43, 85, 85), fill=accent)
    save(image, relative)


def make_status(relative: str, accent: tuple[int, int, int, int], kind: str) -> None:
    image = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image, "RGBA")
    draw.rounded_rectangle((16, 16, 112, 112), radius=28, fill=color("#171611", 230), outline=accent, width=5)
    if kind == "sword":
        draw.polygon([(67, 20), (76, 28), (55, 88), (44, 100), (50, 82)], fill=color("#e8dcc4"))
        draw.line((43, 77, 75, 94), fill=accent, width=7)
    elif kind == "guard":
        draw.polygon([(64, 27), (92, 42), (84, 86), (64, 101), (44, 86), (36, 42)], fill=accent)
    elif kind == "buff":
        draw.arc((35, 35, 93, 93), 40, 320, fill=accent, width=8)
        draw.polygon([(89, 28), (104, 47), (80, 49)], fill=accent)
    elif kind == "fire":
        draw.polygon([(65, 23), (92, 66), (80, 101), (50, 101), (36, 70)], fill=accent)
        draw.polygon([(65, 54), (76, 78), (66, 96), (54, 80)], fill=color("#ffd98a"))
    elif kind == "ice":
        for angle in range(0, 180, 30):
            r = math.radians(angle)
            draw.line((64 - math.cos(r) * 34, 64 - math.sin(r) * 34, 64 + math.cos(r) * 34, 64 + math.sin(r) * 34), fill=accent, width=5)
    elif kind == "bolt":
        draw.polygon([(72, 22), (42, 72), (64, 72), (54, 106), (91, 55), (68, 56)], fill=accent)
    elif kind == "poison":
        draw.ellipse((42, 34, 86, 96), fill=accent)
        draw.ellipse((52, 46, 61, 55), fill=color("#171611"))
        draw.ellipse((72, 46, 81, 55), fill=color("#171611"))
        draw.arc((54, 58, 78, 80), 0, 180, fill=color("#171611"), width=4)
    save(image, relative)


def make_node(relative: str, accent: tuple[int, int, int, int], kind: str) -> None:
    image = Image.new("RGBA", (192, 192), (0, 0, 0, 0))
    draw_shadow(image, (24, 24, 168, 168), 72, 55)
    draw = ImageDraw.Draw(image, "RGBA")
    draw.ellipse((24, 24, 168, 168), fill=color("#e6d6b8", 238), outline=accent, width=8)
    draw.ellipse((42, 42, 150, 150), outline=GOLD_LIGHT, width=4)
    if kind == "battle":
        draw.line((72, 52, 122, 132), fill=INK, width=8)
        draw.line((120, 52, 70, 132), fill=INK, width=8)
    elif kind == "elite":
        draw.polygon([(96, 42), (126, 84), (110, 138), (82, 138), (66, 84)], fill=accent)
    elif kind == "event":
        draw.arc((58, 48, 134, 124), 200, 520, fill=accent, width=10)
        draw.ellipse((88, 134, 104, 150), fill=accent)
    elif kind == "shop":
        draw.rounded_rectangle((54, 70, 138, 132), radius=12, fill=accent)
        draw.polygon([(48, 72), (144, 72), (126, 48), (66, 48)], fill=GOLD_LIGHT)
    elif kind == "forge":
        draw.polygon([(62, 78), (130, 78), (114, 138), (78, 138)], fill=accent)
        draw.polygon([(96, 42), (118, 76), (74, 76)], fill=color("#d25535"))
    elif kind == "boss":
        draw.polygon([(96, 34), (138, 70), (128, 134), (96, 158), (64, 134), (54, 70)], fill=accent)
        draw.ellipse((78, 78, 114, 114), fill=color("#f4ead0"))
    save(image, relative)


def make_panel(relative: str, size: tuple[int, int], popup: bool = False) -> None:
    w, h = size
    image = Image.new("RGBA", size, (0, 0, 0, 0))
    draw_shadow(image, (18, 18, w - 18, h - 18), 18, 60)
    paper = paper_layer(size, 900 + w + h)
    mask = Image.new("L", size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle((18, 18, w - 18, h - 18), radius=18, fill=255)
    image.alpha_composite(Image.composite(paper, Image.new("RGBA", size, (0, 0, 0, 0)), mask))
    draw = ImageDraw.Draw(image, "RGBA")
    draw.rounded_rectangle((18, 18, w - 18, h - 18), radius=18, outline=GOLD, width=6)
    draw.rounded_rectangle((32, 32, w - 32, h - 32), radius=12, outline=INK, width=2)
    for offset in range(0, w, 90):
        y = h - 70 + int(math.sin(offset * 0.06) * 6)
        draw.arc((offset - 80, y - 50, offset + 160, y + 80), 190, 345, fill=color("#596556", 36), width=2)
    if popup:
        draw.rounded_rectangle((54, 48, w - 54, h - 52), radius=14, outline=GOLD_LIGHT, width=3)
    save(image, relative)


def make_button(relative: str, fill: tuple[int, int, int, int], border: tuple[int, int, int, int]) -> None:
    w, h = 480, 128
    image = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw_shadow(image, (14, 18, w - 14, h - 18), 18, 45)
    draw = ImageDraw.Draw(image, "RGBA")
    draw.rounded_rectangle((14, 18, w - 14, h - 18), radius=18, fill=fill, outline=border, width=5)
    draw.rounded_rectangle((28, 31, w - 28, h - 31), radius=12, outline=color("#f1d48a", 90), width=2)
    draw.line((58, 34, w - 58, 34), fill=color("#fff0bd", 55), width=2)
    draw.line((58, h - 35, w - 58, h - 35), fill=color("#2d160f", 70), width=2)
    save(image, relative)


def make_background(relative: str) -> None:
    w, h = 1920, 1080
    rng = random.Random(2601)
    image = Image.new("RGBA", (w, h), color("#efe7d8"))
    draw = ImageDraw.Draw(image, "RGBA")

    for _ in range(48):
        x = rng.randrange(w)
        y = rng.randrange(h)
        radius = rng.randrange(1, 2)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=rng.choice([color("#fff6e8", 12), color("#9b825d", 7), color("#5d6a64", 5)]))
    for _ in range(12):
        y = rng.randrange(90, h - 260)
        x0 = rng.randrange(-120, w - 160)
        x1 = x0 + rng.randrange(160, 360)
        draw.line((x0, y, x1, y + rng.randrange(-1, 2)), fill=color("#8d7755", 8), width=1)

    wash = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    wash_draw = ImageDraw.Draw(wash, "RGBA")
    for _ in range(40):
        x = rng.randrange(-220, w + 120)
        y = rng.randrange(730, 990)
        rx = rng.randrange(110, 360)
        ry = rng.randrange(28, 96)
        tone = rng.choice([color("#61736b", 7), color("#39524f", 6), color("#b58c48", 5)])
        wash_draw.ellipse((x - rx, y - ry, x + rx, y + ry), fill=tone)
    wash = wash.filter(ImageFilter.GaussianBlur(38))
    image.alpha_composite(wash)

    for layer, alpha in enumerate([22, 18, 14]):
        base_y = 790 + layer * 68
        points: list[tuple[int, int]] = [(-80, h)]
        x = -80
        while x <= w + 120:
            peak = base_y + rng.randrange(-36, 48)
            points.append((x, peak))
            x += rng.randrange(170, 280)
        points.append((w + 120, h))
        fill = color("#263f3d", alpha)
        draw.polygon(points, fill=fill)
        for index in range(1, len(points) - 2):
            x0, y0 = points[index]
            x1, y1 = points[index + 1]
            draw.line((x0, y0, x1, y1), fill=color("#2d3028", max(7, alpha // 3)), width=1)

    river = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    river_draw = ImageDraw.Draw(river, "RGBA")
    for i in range(9):
        y = 870 + i * 14
        river_draw.arc((-200 + i * 28, y - 120, w + 300, y + 95), 188, 350, fill=color("#6b8c88", 5), width=1)
    river = river.filter(ImageFilter.GaussianBlur(1.8))
    image.alpha_composite(river)

    mist = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    mist_draw = ImageDraw.Draw(mist, "RGBA")
    for i in range(7):
        y = 700 + i * 46
        mist_draw.rectangle((0, y, w, y + rng.randrange(28, 58)), fill=color("#f3ead9", 34))
    mist = mist.filter(ImageFilter.GaussianBlur(42))
    image.alpha_composite(mist)

    for _ in range(4):
        x = rng.randrange(0, w)
        y = rng.randrange(80, 430)
        length = rng.randrange(120, 360)
        draw.arc((x - length, y - 18, x + length, y + 44), 195, 345, fill=color("#6f7667", 10), width=1)

    for x, y, scale in [(1510, 805, 0.8), (1580, 824, 0.58)]:
        draw.arc((x - int(34 * scale), y - int(12 * scale), x + int(28 * scale), y + int(18 * scale)), 200, 345, fill=color("#33332a", 34), width=max(1, int(2 * scale)))
        draw.arc((x + int(18 * scale), y - int(10 * scale), x + int(72 * scale), y + int(14 * scale)), 195, 340, fill=color("#33332a", 34), width=max(1, int(2 * scale)))
        draw.line((x, y, x + int(10 * scale), y + int(30 * scale)), fill=color("#33332a", 28), width=1)

    vignette = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    vignette_draw = ImageDraw.Draw(vignette, "RGBA")
    vignette_draw.rectangle((0, 0, w, 90), fill=color("#ffffff", 18))
    vignette_draw.rectangle((0, h - 120, w, h), fill=color("#223b38", 5))
    vignette = vignette.filter(ImageFilter.GaussianBlur(34))
    image.alpha_composite(vignette)
    save(image, relative)


def make_tab(relative: str, active: bool) -> None:
    w, h = 240, 80
    image = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image, "RGBA")
    fill = color("#e6d6b8", 240) if active else color("#b9ad93", 210)
    border = GOLD if active else color("#74634a")
    draw.rounded_rectangle((10, 12, w - 10, h - 8), radius=16, fill=fill, outline=border, width=4)
    draw.line((28, h - 14, w - 28, h - 14), fill=border, width=3)
    save(image, relative)


def generate() -> None:
    ensure_dirs()
    make_card_frame("cards/card_attack.png", color("#2c8bb0"), 10, "attack")
    make_card_frame("cards/card_defense.png", color("#24836f"), 20, "defense")
    make_card_frame("cards/card_skill.png", color("#a87921"), 30, "skill")
    make_card_frame("cards/card_support.png", color("#1f8e78"), 40, "support")
    make_card_frame("cards/card_curse.png", color("#5a328a"), 50, "curse")

    make_icon("icons/icon_health.png", color("#9b3628"), "heart", 1)
    make_icon("icons/icon_armor.png", color("#287d70"), "shield", 2)
    make_icon("icons/icon_energy.png", color("#3588a7"), "drop", 3)
    make_icon("icons/icon_coin.png", color("#bd8622"), "coin", 4)
    make_icon("icons/socket_empty.png", color("#766c5a"), "socket", 5)
    make_icon("icons/socket_attack.png", color("#2c8bb0"), "spark", 6)
    make_icon("icons/socket_spell.png", color("#5a328a"), "spark", 7)
    make_icon("icons/socket_poison.png", color("#34894a"), "drop", 8)

    make_node("map/node_battle.png", color("#9b3628"), "battle")
    make_node("map/node_elite.png", color("#5a328a"), "elite")
    make_node("map/node_event.png", color("#3588a7"), "event")
    make_node("map/node_shop.png", color("#bd8622"), "shop")
    make_node("map/node_forge.png", color("#b2502e"), "forge")
    make_node("map/node_boss.png", color("#7c241d"), "boss")

    make_status("status/icon_intent_attack.png", color("#c45131"), "sword")
    make_status("status/icon_intent_guard.png", color("#287d70"), "guard")
    make_status("status/icon_intent_buff.png", color("#bd8622"), "buff")
    make_status("status/icon_status_burn.png", color("#e05c2b"), "fire")
    make_status("status/icon_status_freeze.png", color("#7bb6c8"), "ice")
    make_status("status/icon_status_lightning.png", color("#9361cc"), "bolt")
    make_status("status/icon_status_poison.png", color("#3f9b55"), "poison")

    make_panel("ui/panel_large.png", (960, 540))
    make_panel("ui/popup_panel.png", (640, 360), popup=True)
    make_background("ui/background_ink_landscape.png")
    make_button("ui/button_normal.png", color("#743521", 242), GOLD)
    make_button("ui/button_hover.png", color("#9b4327", 246), GOLD_LIGHT)
    make_button("ui/button_pressed.png", color("#5d281c", 246), color("#8f681e"))
    make_button("ui/button_disabled.png", color("#8f8874", 210), color("#6e624f"))
    make_tab("ui/tab_active.png", True)
    make_tab("ui/tab_inactive.png", False)
    make_preview()
    write_manifest()


def make_preview() -> None:
    thumbs: list[Path] = []
    for sub in ["cards", "icons", "map", "status", "ui"]:
        thumbs.extend(sorted((ASSETS / sub).glob("*.png")))
    cell = 150
    cols = 7
    rows = math.ceil(len(thumbs) / cols)
    preview = Image.new("RGBA", (cols * cell, rows * cell), color("#efe6d3"))
    draw = ImageDraw.Draw(preview, "RGBA")
    for idx, path in enumerate(thumbs):
        im = Image.open(path).convert("RGBA")
        im.thumbnail((120, 120), Image.Resampling.LANCZOS)
        x = (idx % cols) * cell + (cell - im.width) // 2
        y = (idx // cols) * cell + (cell - im.height) // 2
        draw.rounded_rectangle((idx % cols * cell + 8, idx // cols * cell + 8, idx % cols * cell + cell - 8, idx // cols * cell + cell - 8), radius=12, fill=color("#f7f0df"), outline=color("#b78a30", 170), width=2)
        preview.alpha_composite(im, (x, y))
    save(preview, "preview/acceptance_asset_pack_preview.png")


def write_manifest() -> None:
    files = []
    for path in sorted(ASSETS.rglob("*.png")):
        rel = path.relative_to(ROOT).as_posix()
        image = Image.open(path)
        files.append(
            {
                "path": rel,
                "size": list(image.size),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
        )
    manifest = {
        "id": "worldseed_acceptance_asset_pack_v0_1",
        "style": "xianxia_card_handpainted_acceptance",
        "generated_by": "tools/generate_acceptance_assets.py",
        "files": files,
    }
    (ASSETS / "acceptance_asset_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    generate()
    print("acceptance-assets: generated")
