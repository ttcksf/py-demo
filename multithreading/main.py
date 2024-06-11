import threading

# def say_hello():
#   print("hello")

# t1 = threading.Thread(target=say_hello)
# t1.start()

def test1():
  for x in range(10):
    print("test1")

def test2():
  for x in range(10):
    print("test2")
# 通常は上から順番に実行されて次の処理に移行する（シングルスレッド）
# test1()
# test2()

# スレッドモジュールを使うと同時に実行できる（現実世界ではブラウザの複数タブや検索とファイルダウンロードの並行などで使われている）
t1 = threading.Thread(target=test1)
t2 = threading.Thread(target=test2)
t1.start()
t2.start()
