def func1(num):
  result = []
  for i in num:
    result.append(i + 2)
  return result
# 空のリストを用意してそこにループでメソッドを実行しながらデータを完成させて結果を最後にループすることで1個ずつのデータを取り出す仕組み
var = func1([1,2,3])
print(var)
for i in var:
  print(i)

def func2(num):
  for i in num:
    yield(i + 2)
var = func2([1,2,3])
# yieldにするとnextを使って1個ずつ実行する都度実行する考え方（空のリストが必要ない、データ全体が完成するまで待たなくて良い、完成形がないのでループで取り出す必要がない）
# print(var)
# print(next(var))
# print(next(var))
# print(next(var))
