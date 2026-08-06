"""
Genera el set de iconos/favicon a partir de la paleta núcleo.
Requiere Pillow (pip install Pillow --break-system-packages).
Ejecutar desde esta carpeta: python3 generate_icons.py
Los PNG/ICO resultantes ya están commiteados; solo hace falta
re-ejecutar esto si cambia la paleta o el monograma.
"""
from PIL import Image, ImageDraw, ImageFont

BG = (10, 10, 11, 255)       # --bg
FG = (242, 240, 234, 255)    # --fg
ACCENT = (232, 64, 44, 255)  # --accent
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def make_icon(size, accent_bar=True):
    img = Image.new("RGBA", (size, size), BG)
    draw = ImageDraw.Draw(img)

    font_size = int(size * 0.46)
    font = ImageFont.truetype(FONT_PATH, font_size)
    text = "RG"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size - tw) / 2 - bbox[0]
    y = (size - th) / 2 - bbox[1]
    draw.text((x, y), text, font=font, fill=FG)

    if accent_bar:
        bar_h = max(2, int(size * 0.045))
        bar_w = int(size * 0.34)
        bx = (size - bar_w) / 2
        by = y + th + int(size * 0.06)
        draw.rectangle([bx, by, bx + bar_w, by + bar_h], fill=ACCENT)

    return img


def make_ico(path, sizes=(16, 32, 48)):
    base = make_icon(max(sizes), accent_bar=False).convert("RGB")
    imgs = [base.resize((s, s), Image.LANCZOS) for s in sizes]
    imgs[0].save(path, format="ICO", sizes=[(s, s) for s in sizes])


if __name__ == "__main__":
    make_icon(192).save("icon-192.png")
    make_icon(512).save("icon-512.png")
    make_icon(180, accent_bar=False).convert("RGB").save("apple-touch-icon.png")
    make_ico("../../../favicon.ico")
    print("done")
