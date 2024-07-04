# pip install Pillow
from PIL import Image
image = Image.open("./image.png")
new_image = image.resize((400,400))
new_image.save("./sample1.jpeg")

# トリミング
image = Image.open("./image.png")
rect = (100,100,200,200)
rect_image = image.crop(rect)
rect_image.save("./sample2.png")

# グレースケール
image = Image.open("./image.png")
grey_image = image.convert("L")
grey_image.save("./sample3.png")
