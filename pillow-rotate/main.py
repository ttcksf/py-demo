# pip install Pillow
from PIL import Image
image = Image.open("./image.png")
image1 = image.rotate(30)
image1.save("./sample1.jpeg")
# 枠に収めるにはexpand=true
image2 = image.rotate(30, expand=True)
image2.save("./sample2.jpeg")

# 左右反転
image3 = image.transpose(Image.FLIP_LEFT_RIGHT)
image3.save("./sample3.jpeg")
# 上下反転
image4 = image.transpose(Image.FLIP_TOP_BOTTOM)
image4.save("./sample4.jpeg")
