# 引数のパッキング
def func1(a,b,c):
  print(a + b + c)
func1(1,2,3)
# これはできない
# func1([1,2,3])
# これならOKというルール
func1(*[1,2,3])

# 引数のアンパッキング
def func2(*args):
  for i in args:
    print(i)
func2(1)
func2(1,2,3)
