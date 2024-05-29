# 既存の関数、メソッド以外に自分のオリジナルの関数も作れる
def test():
  print("test")
# 作成と実行は分かれている
test()
# 複数実行するときも名前を呼び出せば良い
# test()
# test()

# 中身の値を引数で動的に変化させることもできる
# def parameter(name):
#   print(name)
# parameter("田中")
# 引数を関数の外で呼ぶことはできない
# print(name)

# 引数は2つ以上あっても良い
def parameter(name1, name2):
  print(f"{name1} {name2}")
parameter("山田","太郎")
