import random

def jumble(word):
  result = list(word)
  random.shuffle(result)
  return ''.join(result)

words = ["red","blue","green"]
results = []

# for word in words:
#   results.append(jumble(word))
# print(results)

# 複数データに特定の関数を実行して新しいリストに返す方法には短く書くMapがある
# map(関数名、複数データ)で書くことで短く書ける
print(list(map(jumble,words)))
