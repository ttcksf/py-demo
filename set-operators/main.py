set1 = {1,2,3}
set2 = {4,5,6}
# 交わってないことを確認
# Trueが出ればOK
print(set1.isdisjoint(set2))
#空のセットが出ればOK
print(set1 & set2)

# 片方に含まれている例
set1 = {1,2,3}
set2 = {1,2,3,4}
print(set1 <= set2)
print(set1.issubset(set2))
print(set2 >= set1)
print(set2.issuperset(set2))

# 文字の重複削除も可能
text = "fbafbnafnana"
symbols = set(text)
print(symbols)
