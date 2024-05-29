# boolean型（TrueかFalse）
# print(1 > 0)
# print(1 < 0)

# boolean型を使うと処理の分岐を作れる
age = 9
if(age >= 20):
# インデントでif文の中身かどうか判断されるので注意
# print("OK")
  print("OK")

if(age >= 20):
  print("OK")
else:
  print("未成年です")

if(age >= 65):
  print("還暦です")
elif (age >= 20):
  print("社会人です")
else:
  print("学生です")
