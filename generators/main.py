# ジェネレーター関数(yieldを含む関数)
def func1():
  yield 10
  yield 20
  yield 30

# for i in func1():
#   print(i)

def func2():
  yield 100
  yield True
  yield ("Hello")
# ジェネレーター関数の実行（戻り値）はジェネレーターオブジェクトになる
var = func2()
# print(var)
# for以外にnextで中身を呼び出すことも可能
# print(next(var))
# print(next(var))
# print(next(var))

