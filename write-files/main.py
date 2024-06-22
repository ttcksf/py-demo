# 書き込みは第二引数が必要
with open("write-files/test1.txt","w") as f:
  f.write("hello")
  # 改行は改行コードが必要
  f.write("\nhello")

# 新規作成もファイル名を決めるだけでコードは同じ
with open("write-files/test2.txt","w") as f:
  f.write("test")

# 前の内容を上書きしたくない時は第二引数はaにする
with open("write-files/test2.txt","a") as f:
  f.write("test")

# 事前に文章を用意
text = [
  "\ntest1",
  "\ntest2",
  "\ntest3",
]
with open("write-files/test2.txt","a") as f:
  # 複数行なのでwritelines
  f.writelines(text)
