import urllib.request

def dl_image(url,file_name):
  full_path = file_name + ".png"
  urllib.request.urlretrieve(url,full_path)

url = input("URLを入力してください：")
file_name = input("ファイル名を決めてください：")

dl_image(url,file_name)
