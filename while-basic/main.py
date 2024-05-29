# boolean型を使ったwhile文がある
# 条件がTrueである限り繰り返し処理を継続する
count = 0
while(count <= 20):
  print(count)
  # 別の条件を書くこともできる
  if(count == 10):
    print("半分です")
  count += 1

