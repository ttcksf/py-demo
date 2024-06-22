numbers = [1,2,3,4,5,6]

def test(n):
  return n * 2

# 第二引数のリストから一つずつ取り出して第一引数の関数に渡すmap関数
# print(list(map(test, numbers)))

# ラムダ式で書くとこうなる(関数に名前を持たせない省略記法、1回しか使用しない関数などに使うと便利)
print(list(map(lambda n: n * 2,numbers)))

