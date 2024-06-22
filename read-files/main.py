# with open("read-files/test1.txt") as f:
#   lines = f.readline()
#   print(lines)


def filter_line(line):
  return "@" not in line

with open("read-files/test1.txt") as f:
  lines = f.readline()
  # print(lines)
  # filterなど他の関数とセットにして読み込んだ内容を関数実行することもできる
  print(list(filter(filter_line,lines)))
