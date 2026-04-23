from PIL import Image, ImageDraw, ImageFont
import os

GAP = 20
LABEL_H = 36
BG = (30, 30, 30)
LABEL_HTML = (60, 80, 140)
LABEL_PPTX = (100, 50, 50)
TEXT_COLOR = (255, 255, 255)

out_dir = r"D:\tmp\compare"
os.makedirs(out_dir, exist_ok=True)

for i in range(1, 9):
    html_path = rf"D:\tmp\compare\html_s{i:02d}.png"
    pptx_path = rf"D:\tmp\pptx_check\v4_s{i:02d}.png"

    html_img = Image.open(html_path).convert("RGB")
    pptx_img = Image.open(pptx_path).convert("RGB")

    target_h = html_img.height
    ratio = target_h / pptx_img.height
    pptx_w = int(pptx_img.width * ratio)
    pptx_img = pptx_img.resize((pptx_w, target_h), Image.LANCZOS)

    total_w = html_img.width + GAP + pptx_img.width
    total_h = LABEL_H + target_h
    canvas = Image.new("RGB", (total_w, total_h), BG)

    draw = ImageDraw.Draw(canvas)
    draw.rectangle([0, 0, html_img.width, LABEL_H - 1], fill=LABEL_HTML)
    draw.rectangle([html_img.width + GAP, 0, total_w, LABEL_H - 1], fill=LABEL_PPTX)

    try:
        font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 18)
    except:
        font = ImageFont.load_default()

    draw.text((html_img.width // 2, LABEL_H // 2), "HTML (Original)",
              fill=TEXT_COLOR, font=font, anchor="mm")
    draw.text((html_img.width + GAP + pptx_img.width // 2, LABEL_H // 2), "PPTX v4 (latest)",
              fill=TEXT_COLOR, font=font, anchor="mm")

    canvas.paste(html_img, (0, LABEL_H))
    canvas.paste(pptx_img, (html_img.width + GAP, LABEL_H))

    out_path = os.path.join(out_dir, f"new_cmp_s{i:02d}.png")
    canvas.save(out_path)
    print(f"Saved: {out_path}")

print("Done.")
