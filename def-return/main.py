# 自分のオリジナルの関数に戻り値を作って結果を保存することができる
def test(name):
  print(name)
  return name
value = test("山田")
# 作った関数を別の処理のパーツに利用することができる
print(f"ユーザー名：{value}")
# 戻り値を関数の外で呼び出すことはできない（ローカルスコープ）
# print(name)

# グローバルスコープ
name = "test"
# 関数の外のnameにはアクセスできるが関数の中のnameを外からアクセスすることはできない
print(name)
