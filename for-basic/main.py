# boolean型を使わないループもある
# リスト形式
# numbers = [100,200,300]
# タプル形式
# numbers = (100,200,300)
# for num in numbers:
#   print(num)

# 辞書形式はキーと値があるため書き方が変わる
studentA = {
  "name": "yamada",
  "age": 20,
  "gender": "male"
}
# キーをくりかえす
# for val in studentA.keys():
  # print(val)

# 値を繰り返す
# for val in studentA.values():
  # print(val)

# キーと値を繰り返す
for key,val in studentA.items():
  print(key,val)
