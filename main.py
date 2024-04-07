from PIL import Image, ImageDraw, ImageFont


# Create a new blank image with white background
width, height = 400, 200
background_color = (255, 255, 255)
image = Image.new("RGB", (width, height), background_color)

# Create a drawing context
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('OpenSans-Bold.ttf')
# Text to write
text = "Привет, мир!"
draw.text((100, 100), text, fill=(0, 0, 0), font=font)

# Save the image
image.save("cyrillic_image.png")
