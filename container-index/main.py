# リストとタプルではインデックス番号を使って中身を管理している
# students = ["yamada","tanaka","yoshida","suzuki","takahashi"]
students = ("yamada","tanaka","yoshida","suzuki","takahashi")
print(students)
# インデックス番号で要素を取得できる
print(students[0])
# 0番目から3つ取得する
print(students[0:3])

# 辞書はキー名を使って中身を管理している
dict_test = {
  "name": "yamada",
  "age": 21,
  "gender": "male"
}
print(dict_test)
print(dict_test["name"])
# 追加はappnedのようなメソッドは必要なく新しいキー名さえ指定すれば良い
dict_test["address"] = "tokyo"
print(dict_test)
