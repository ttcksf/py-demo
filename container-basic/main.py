# タプル
tuple_test = ("yamada","tanaka","yoshida")
# 中身の個数を数える関数
# print(len(tuple_test))
# こちらは使えない
# tuple_test.append("suzuki")
# print(tuple_test)

# リスト（中身の変更ができる）
list_test = ["yamada","tanaka","yoshida"]
# print(len(list_test))
# 中身の追加をする関数を使える
# list_test.append("suzuki")
# print(list_test)
# そのため重複も許可している
list_test = ["yamada","tanaka","yoshida","yamada"]
# print(list_test)

# セット（重複削除される）
# set_test = {"yamada","tanaka","yoshida"}
set_test = {"yamada","tanaka","yoshida","yamada"}
# print(set_test)

# 辞書（キーを使った直感的なデータ管理）
dict_test = {
  "name": "yamada",
  "age": 20,
  "gender": "male"
}
print(dict_test)
