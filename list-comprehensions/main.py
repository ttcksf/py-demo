numbers = [1,2,3,4,5]
# 元のnumbersは変更せず新しいリストに入れ直す
# lists = []
# for num in numbers:
#   lists.append(num + 1)
# print(lists)

# ループの後に結果をリストで返す書き方は短くできる
lists = [num + 1 for num in numbers]
print(lists)
