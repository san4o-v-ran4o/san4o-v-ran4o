from PIL import Image, ImageDraw, ImageFont

text = "I am a Python developer"
font = ImageFont.truetype("arial.ttf", 40)
frames = []

for i in range(20):
    img = Image.new('RGB', (600, 100), color=(10, 10, 10))
    draw = ImageDraw.Draw(img)
  
    offset = (i * 10) % 600
    draw.text((600 - offset, 30), text, font=font, fill=(0, 255, 100))

    frames.append(img)

frames[0].save("animated_text.gif", format="GIF", append_images=frames[1:], save_all=True, duration=100, loop=0)
