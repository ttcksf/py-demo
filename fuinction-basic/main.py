# printも関数の一つ(戻り値を持たないだけ)
# print("hello")

# 戻り値を持つ例
# input("入力してください")
# inputの戻り値がprintに入ったことで表示までできる
# print(input("入力してください"))
# printは戻り値がないのでこれではNoneが表示されることになる
# print(print("hello"))

# 特定のデータ型に付属した関数をメソッドという
# 文字列にのみ使用できて小文字を大文字にするメソッド
print("hello".upper())
# 特定の文字を別の文字に置換するメソッド
print("hello".replace("l","o"))
# 文字列以外には使えないためメソッドは使用できる対象が限定的な関数とも言える
# print(100.upper())

# 数字にのみ使用できる絶対値を返すメソッド
print(abs(-100))
# 文字列には使用できない
# print(abs("hello"))
