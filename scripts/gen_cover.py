#!/usr/bin/env python3
"""
gen_cover.py — OGP / thumbnail cover generator for VTuber blog posts.

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
from PIL import Image, ImageDraw, ImageFont

# ── Config ────────────────────────────────────────────────────────────────────

WIDTH, HEIGHT = 1200, 630
FONT     = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
BASE_DIR = Path(__file__).resolve().parent.parent
JA_DIR   = BASE_DIR / "content" / "ja" / "post"
EN_DIR   = BASE_DIR / "content" / "en" / "post"

SITE_NAME = "VTuber ネタ帳"

# Category accent colors  (RGB)
COLORS = {
    "haishin-neta": (124, 58,  237),   # purple
    "game-ideas":   (22,  163, 74),    # green
    "utawaku":      (219, 39,  119),   # pink
    "unei-tips":    (2,   132, 199),   # blue
    "ai-tips":      (234, 88,  12),    # orange
}
DEFAULT_COLOR = (107, 114, 128)        # gray

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

def lighten(rgb: tuple, t: float = 0.88) -> tuple:
    return tuple(min(255, int(c + (255 - c) * t)) for c in rgb)

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

def fit_title(text: str, max_w: int, draw, max_sz=64, min_sz=34, max_lines=3):
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

    img  = Image.new("RGB", (WIDTH, HEIGHT), (252, 252, 252))
    draw = ImageDraw.Draw(img)

    # Left accent bar
    draw.rectangle([(0, 0), (18, HEIGHT)], fill=color)

    # Top tint band
    draw.rectangle([(18, 0), (WIDTH, 86)], fill=lighten(color, 0.88))

    # Bottom dark bar
    BAR_H = 88
    draw.rectangle([(0, HEIGHT - BAR_H), (WIDTH, HEIGHT)], fill=(28, 28, 28))

    # Category badge in bottom bar
    font_cat = ImageFont.truetype(FONT, 28)
    PX, PY   = 18, 8
    cb       = draw.textbbox((0, 0), cat_label, font=font_cat)
    bw, bh   = cb[2] - cb[0] + PX * 2, cb[3] - cb[1] + PY * 2
    bx       = 56
    by       = HEIGHT - BAR_H + (BAR_H - bh) // 2
    draw.rounded_rectangle([(bx, by), (bx + bw, by + bh)], radius=6, fill=color)
    draw.text((bx + PX, by + PY), cat_label, font=font_cat, fill=(255, 255, 255))

    # Site name (bottom right)
    font_site = ImageFont.truetype(FONT, 22)
    sb  = draw.textbbox((0, 0), SITE_NAME, font=font_site)
    sw  = sb[2] - sb[0]
    sh  = sb[3] - sb[1]
    draw.text(
        (WIDTH - 48 - sw, HEIGHT - BAR_H + (BAR_H - sh) // 2),
        SITE_NAME, font=font_site, fill=(155, 155, 155),
    )

    # Title — auto-fit into centre area
    MARGIN_L  = 64
    TITLE_W   = WIDTH - MARGIN_L - 48
    TITLE_TOP = 104
    TITLE_BOT = HEIGHT - BAR_H - 16
    clean     = re.sub(r'^[「『"\'【]+|[」』"\'】]+$', "", title)
    font_t, lines = fit_title(clean, TITLE_W, draw)
    lh        = int(font_t.size * 1.48)
    total_h   = len(lines) * lh
    ty        = TITLE_TOP + (TITLE_BOT - TITLE_TOP - total_h) // 2
    for i, line in enumerate(lines):
        draw.text((MARGIN_L, ty + i * lh), line, font=font_t, fill=(22, 22, 22))

    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(str(out), "JPEG", quality=90)
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

    # Japanese cover
    ja_cover = JA_DIR / slug / "cover.jpg"
    if force or not ja_cover.exists():
        render(title, category, ja_cover)
        add_image_field(ja_md)
    else:
        print(f"  – {slug} (ja cover exists, use --force to overwrite)")

    # English cover — use English title if en version exists
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
