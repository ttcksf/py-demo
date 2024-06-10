# my_list = [1,2,3,4,5]
my_list = [1,2,3,4,5,1]
# my_set = {1,2,3,4,5}
# 重複削除機能があるのがセット
my_set = {1,2,3,4,5,1}

print(my_list)
print(my_set)
# インデックス番号が使えないのがセット(重複削除されるため出現回数や順番を数える必要がない)
# print(my_list[0])
# print(my_set[0])

# セットからリストに変換するとOK
print(list(my_set)[0])
# セットに追加
my_set.add(6)
# セットから削除
my_set.remove(6)

print(my_set)
