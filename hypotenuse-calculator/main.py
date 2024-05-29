# 引数は順番通り入れないと思ったような処理にならない
def calc(a,b):
  return a * 2 + b * 3
# result = calc(2,4)
# 組み合わせが同じでも左から順番に入れないと結果が変わることがある
# result = calc(4,2)
# 引数名と値を一致する書き方があり引数の数が増えてくると便利になる
# result = calc(b=4,a=2)
# print(result)

# 引数にはデフォルト値を指定する仕組みがある
def calc(a,b=2):
  return a * 2 + b * 3
# 通常は引数の個数がないとエラーになるがデフォルト値があることで実行時に省略することが可能
# result = calc(2)
# デフォルト値のある引数に値を指定すると上書きして実行される
result = calc(2,4)
print(result)
