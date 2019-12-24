from PIL import Image
img = Image.open("stelth.jpg")
print(img.size)
print(img.format)

img.show()
