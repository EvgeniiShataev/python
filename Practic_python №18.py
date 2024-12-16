#Задание 1
from PIL import Image

image = Image.open("E:\\pyt\\screenshot.jpg")
baw = image.convert("L")
baw.save("screenshot_bw.jpg.")
baw.save("screenshot_bw.jpg")
#Задание 2
from PIL import Image

image = Image.open("E:\\pyt\\screen_camera.png")
rot = image.rotate(180)
rot.save("screen_camera.png")
#Задание 3
from PIL import Image

image = Image.open("E:\\pyt\\figures.png")
cube = image.crop((265,115,485,400))
cube.save("figures.png")
cube.save(cube.png)
#Задание 4
from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (200, 200), "green")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", 20)
draw.text((24, 50), "ShatHol was here", fill="white", font=font)
image.show()
#Задание 5
from PIL import Image, ImageDraw

image = Image.open("D:\\pixels.png")
draw = ImageDraw.Draw(image)
draw.rectangle((178,35,221,80), outline="red")
draw1 = ImageDraw.Draw(image)
draw1.rectangle((22,150,51,229), outline="blue")
image.save("pixels_ready.png")
#Задание 6
from PIL import Image, ImageDraw

pixels = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 1, 1, 1, 1, 1, 0, 1],
 [1, 1, 1, 0, 0, 0, 1, 1, 1],
 [1, 1, 0, 1, 0, 1, 0, 1, 1],
 [1, 1, 0, 0, 1, 0, 0, 1, 1],
 [1, 1, 0, 1, 0, 1, 0, 1, 1],
 [1, 1, 1, 0, 0, 0, 1, 1, 1],
 [1, 0, 1, 1, 1, 1, 1, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1]]

image = Image.new("RGB", (9,9), "white")
draw = ImageDraw.Draw(image)
for y, row in enumerate(pixels):
    for x, pixel in enumerate(row):
        if pixel == 1:
            color = "black"
        else:
            color = "white"
        draw.rectangle((x,y,x,y), fill = color)
image.save("my pixel pict.png")
