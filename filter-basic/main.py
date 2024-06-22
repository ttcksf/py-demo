str = ["a","b","c","b"]

def testing(str):
  return str != "b"

# filterはオブジェクト形式になって返ってくる
# print(list(filter(testing, str)))

# これと同じ
filtered = []
for s in str:
  if s != "b":
    filtered.append(s)
print(filtered)
