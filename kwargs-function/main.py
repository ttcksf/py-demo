# 辞書形式の引数のパッキング
def func1(name,age,gender):
  print(f"{name}さんは{age}歳で{gender}です")
func1("山田",20,"男性")

# 辞書にまとめて一括で引数に渡す
user1 = {
  "name": "山田",
  "age": 20,
  "gender": "男性"
}
# これはできない
# func1(user1)
# これならOKというルール
func1(**user1)

# 辞書形式の引数のアンパッキング(引数が何個渡されるかわからない時に便利)
def func2(**kwargs):
  for key in kwargs:
    print(f"{key}:{kwargs[key]}")
func2(name="山田",age=20,gender="男性")
