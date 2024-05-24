# いろんな場所で再利用や修正が可能なデータを変数として使うことで効率的なコードが書ける
# 変数は宣言しただけでは実行されない
test = "hello"
print(test)
# 文字列の一部として埋め込むことも可能
print(test + "yamada")
# 途中で再代入して値を変更できる
test = "hey"
print(test)
# 変数名は英語と数字と「_」を使う
human1 = "yamada"
# 最初に数字を持ってくることはできない
# 1human = "yamada"

old_value = "test"
# -や+などを使うことはできない
# old-value = "test"
# old+value = "test"
