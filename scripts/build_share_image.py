#!/usr/bin/env python3
"""Render a social sharing card using our real app assets. Requires Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT = '/System/Library/Fonts/Avenir Next.ttc'
def font(size, index=7):
    return ImageFont.truetype(FONT, size, index=index)

im = Image.new('RGB', (1200, 630), '#f5f6f9')
draw = ImageDraw.Draw(im)
draw.ellipse((740, 64, 1270, 594), fill='#e7effb', outline='#cfdaea', width=2)
draw.ellipse((768, 92, 1242, 566), outline='#cfdaea', width=2)
icon = Image.open(ROOT/'assets/app-icon-128.webp').convert('RGBA').resize((56, 56))
im.paste(icon, (65, 56), icon)
draw.text((137, 60), 'FeedFare', font=font(30, 0), fill='#18212e')
draw.text((62, 168), 'Walk first.', font=font(80, 0), fill='#18212e')
draw.text((62, 260), 'Scroll later.', font=font(80, 0), fill='#0865d5')
draw.text((67, 386), 'Turn your steps into time', font=font(28), fill='#586576')
draw.text((67, 429), 'for the apps you choose.', font=font(28), fill='#586576')
draw.text((67, 545), 'feedfare.app', font=font(23, 2), fill='#064caa')
shot = Image.open(ROOT/'assets/dashboard-native-800.webp').convert('RGB')
shot.thumbnail((237, 516), Image.Resampling.LANCZOS)
mask = Image.new('L', shot.size)
ImageDraw.Draw(mask).rounded_rectangle((0, 0, shot.width, shot.height), radius=25, fill=255)
x, y = 857, 71
draw.rounded_rectangle((x-7, y-7, x+shot.width+7, y+shot.height+7), radius=31, fill='white', outline='#d6dfeb', width=2)
im.paste(shot, (x, y), mask)
draw.text((829, 32), 'NATIVE PREVIEW · TESTFLIGHT', font=font(15, 2), fill='#46566d')
im.save(ROOT/'og-image.png', optimize=True)
print('Created 1200 × 630 social image:', (ROOT/'og-image.png').stat().st_size, 'bytes')
