from PIL import Image

im = Image.open("017.png")
print(im.format,im.size)