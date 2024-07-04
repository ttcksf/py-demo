# pip install Pillow

from PIL import Image

image = Image.open("./image.png")
print(image)
# ファイル形式
print(image.format)
# ピクセル形式
print(image.mode)
# サイズ
print(image.size)
# サイズ変更（タプル型で入れる）
new_image = image.resize((100,100))
# 変更した画像を新しい画像として保存する
new_image.save("./sample1.jpeg")
