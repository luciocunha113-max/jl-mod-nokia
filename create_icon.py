from PIL import Image, ImageDraw, ImageFont
import os

sizes = {
    'mdpi': 48, 'hdpi': 72, 'xhdpi': 96,
    'xxhdpi': 144, 'xxxhdpi': 192
}

for density, size in sizes.items():
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    r = size // 5
    draw.rounded_rectangle([0, 0, size-1, size-1], radius=r, fill=(139, 0, 0, 255))
    jl_size = int(size * 0.42)
    me_size = int(size * 0.22)
    try:
        font_jl = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", jl_size)
        font_me = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", me_size)
    except:
        font_jl = ImageFont.load_default()
        font_me = ImageFont.load_default()
    jl_bbox = draw.textbbox((0,0), "JL", font=font_jl)
    jl_w = jl_bbox[2] - jl_bbox[0]
    jl_h = jl_bbox[3] - jl_bbox[1]
    me_bbox = draw.textbbox((0,0), "2ME", font=font_me)
    me_w = me_bbox[2] - me_bbox[0]
    total_h = jl_h + me_bbox[3] - me_bbox[1] + int(size * 0.04)
    y_start = (size - total_h) // 2
    draw.text(((size - jl_w) // 2, y_start), "JL", fill=(255,255,255,255), font=font_jl)
    draw.text(((size - me_w) // 2, y_start + jl_h + int(size*0.04)), "2ME", fill=(255,220,220,255), font=font_me)
    out = f'JL-Mod/app/src/main/res/mipmap-{density}/ic_launcher.png'
    img.save(out)
    print(f'Saved {out}')
