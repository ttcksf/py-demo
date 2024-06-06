# テンプレートリテラル
f_name = "山田"
l_name = "太郎"
age = 20
# これはできない
# print(f_name + l_name + "さんは" + age + "才です")
# 文字列以外はstrで文字列に変換する必要がある
# print(f_name + l_name + "さんは" + str(age) + "才です")
# 文字列以外との合体や結合の＋記号を省略できる
print(f"{f_name}{l_name}さんは{age}才です")
