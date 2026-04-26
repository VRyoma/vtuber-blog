#!/usr/bin/env python3
"""
gen_cover.py — OGP / thumbnail cover generator for Virtual Village.

Usage:
  python3 scripts/gen_cover.py              # generate all missing cover.jpg
  python3 scripts/gen_cover.py <slug> ...   # specific slug(s)
  python3 scripts/gen_cover.py --force      # regenerate even existing covers

Output: content/{ja,en}/post/<slug>/cover.jpg  (1200x630 JPEG)
        Frontmatter image field is also added automatically.
"""

import re
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ── Config ────────────────────────────────────────────────────────────────────

WIDTH, HEIGHT = 1200, 630
FONT     = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
BASE_DIR = Path(__file__).resolve().parent.parent
JA_DIR   = BASE_DIR / "content" / "ja" / "post"
EN_DIR   = BASE_DIR / "content" / "en" / "post"

SITE_NAME = "Virtual Village"

BG = (11, 12, 20)  # near-black with slight blue tint

# Category accent colors (RGB)
COLORS = {
    "haishin-neta": (124, 58,  237),   # purple
    "game-ideas":   (22,  163, 74),    # green
    "utawaku":      (219, 39,  119),   # pink
    "unei-tips":    (2,   132, 199),   # blue
    "ai-tips":      (234, 88,  12),    # orange
}
DEFAULT_COLOR = (107, 114, 128)

CATEGORY_LABELS = {
    "haishin-neta": "配信ネタ・企画",
    "game-ideas":   "ゲーム実況",
    "utawaku":      "歌枠・歌ってみた",
    "unei-tips":    "運営・裏方 Tips",
    "ai-tips":      "AI 活用",
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def parse_frontmatter(path: Path) -> tuple[str, list[str]]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.+?)\n---", text, re.DOTALL)
    if not m:
        return "", []
    fm = m.group(1)
    title_m = re.search(r'^title:\s*["\'](.+?)["\']', fm, re.MULTILINE)
    title   = title_m.group(1) if title_m else ""
    cats_m  = re.search(r"^categories:\s*\n((?:\s+- .+\n?)+)", fm, re.MULTILINE)
    cats    = re.findall(r"- (.+)", cats_m.group(1)) if cats_m else []
    return title, cats

def add_image_field(path: Path) -> None:
    text  = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3 or "image:" in parts[1]:
        return
    parts[1] = parts[1].rstrip() + '\nimage: "cover.jpg"\n'
    path.write_text("---".join(parts), encoding="utf-8")
    print(f"    + image field → {path.relative_to(BASE_DIR)}")

def wrap(text: str, font, max_w: int, draw) -> list[str]:
    lines, cur = [], ""
    for ch in text:
        test = cur + ch
        if draw.textbbox((0, 0), test, font=font)[2] <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines

def fit_title(text: str, max_w: int, draw, max_sz=68, min_sz=34, max_lines=3):
    for sz in range(max_sz, min_sz - 1, -4):
        font  = ImageFont.truetype(FONT, sz)
        lines = wrap(text, font, max_w, draw)
        if len(lines) <= max_lines:
            return font, lines
    font  = ImageFont.truetype(FONT, min_sz)
    lines = wrap(text, font, max_w, draw)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1][:-1] + "…"
    return font, lines

# ── Core renderer ─────────────────────────────────────────────────────────────

def render(title: str, category: str, out: Path) -> None:
    color     = COLORS.get(category, DEFAULT_COLOR)
    cat_label = CATEGORY_LABELS.get(category, category)
    clean     = re.sub(r'^[「『"\'【]+|[」』"\'】]+$', "", title)

    # ── Dark base with soft color glow ────────────────────────────────────────
    base = Image.new("RGBA", (WIDTH, HEIGHT), (*BG, 255))

    glow = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    gd   = ImageDraw.Draw(glow)
    # Primary glow: large ellipse at bottom-right
    gd.ellipse(
        [int(WIDTH * 0.42), int(HEIGHT * 0.20),
         int(WIDTH * 1.38), int(HEIGHT * 1.18)],
        fill=(*color, 55),
    )
    # Secondary glow: smaller, top-left
    gd.ellipse([-100, -100, 340, 340], fill=(*color, 28))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=100))

    img  = Image.alpha_composite(base, glow).convert("RGB")
    draw = ImageDraw.Draw(img)

    # ── Top accent stripe (5px) ───────────────────────────────────────────────
    draw.rectangle([(0, 0), (WIDTH, 5)], fill=color)

    # ── Category badge (pill, top-left) ───────────────────────────────────────
    MARGIN   = 80
    BADGE_Y  = 56
    font_cat = ImageFont.truetype(FONT, 26)
    PX, PY   = 22, 9
    cb  = draw.textbbox((0, 0), cat_label, font=font_cat)
    bw  = cb[2] - cb[0] + PX * 2
    bh  = cb[3] - cb[1] + PY * 2
    draw.rounded_rectangle(
        [(MARGIN, BADGE_Y), (MARGIN + bw, BADGE_Y + bh)],
        radius=8, fill=color,
    )
    draw.text((MARGIN + PX, BADGE_Y + PY), cat_label, font=font_cat, fill=(255, 255, 255))

    # ── Title (white, left-aligned, vertically centred in remaining space) ────
    TITLE_W   = WIDTH - MARGIN - 80
    TITLE_TOP = BADGE_Y + bh + 36
    TITLE_BOT = HEIGHT - 88

    font_t, lines = fit_title(clean, TITLE_W, draw, max_sz=68, min_sz=34, max_lines=3)
    lh      = int(font_t.size * 1.50)
    total_h = len(lines) * lh
    ty      = TITLE_TOP + (TITLE_BOT - TITLE_TOP - total_h) // 2

    for i, line in enumerate(lines):
        draw.text((MARGIN, ty + i * lh), line, font=font_t, fill=(240, 240, 252))

    # ── Bottom separator + site name ──────────────────────────────────────────
    SEP_Y = HEIGHT - 70
    draw.line([(MARGIN, SEP_Y), (WIDTH - MARGIN, SEP_Y)], fill=(55, 58, 80), width=1)

    font_site = ImageFont.truetype(FONT, 21)
    sb  = draw.textbbox((0, 0), SITE_NAME, font=font_site)
    sw, sh = sb[2] - sb[0], sb[3] - sb[1]
    draw.text(
        (WIDTH - MARGIN - sw, SEP_Y + (70 - sh) // 2),
        SITE_NAME, font=font_site, fill=(110, 115, 148),
    )

    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(str(out), "JPEG", quality=92)
    print(f"  ✓ {out.relative_to(BASE_DIR)}")

# ── Per-slug processing ───────────────────────────────────────────────────────

def process(slug: str, force: bool) -> None:
    ja_md = JA_DIR / slug / "index.md"
    en_md = EN_DIR / slug / "index.md"

    if not ja_md.exists():
        print(f"  ✗ {slug}: ja/index.md not found")
        return

    title, cats = parse_frontmatter(ja_md)
    if not title:
        print(f"  ✗ {slug}: could not parse title")
        return
    category = cats[0] if cats else ""

    ja_cover = JA_DIR / slug / "cover.jpg"
    if force or not ja_cover.exists():
        render(title, category, ja_cover)
        add_image_field(ja_md)
    else:
        print(f"  – {slug} (ja cover exists, use --force to overwrite)")

    if en_md.exists():
        en_title, en_cats = parse_frontmatter(en_md)
        en_category       = en_cats[0] if en_cats else category
        en_cover          = EN_DIR / slug / "cover.jpg"
        if force or not en_cover.exists():
            render(en_title or title, en_category, en_cover)
            add_image_field(en_md)
        else:
            print(f"  – {slug} (en cover exists, use --force to overwrite)")

# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    force = "--force" in sys.argv
    slugs = [a for a in sys.argv[1:] if not a.startswith("--")]

    if slugs:
        for slug in slugs:
            process(slug, force)
    else:
        all_slugs = sorted(p.name for p in JA_DIR.iterdir() if p.is_dir())
        print(f"Processing {len(all_slugs)} posts…")
        for slug in all_slugs:
            process(slug, force)

if __name__ == "__main__":
    main()
