# pip install pandas

import pandas

# シリーズが複数組み合わさったものがデータフレーム
# データフレームの１列分がシリーズ
# https://docs.pyq.jp/python/pydata/pandas/series.html
df = pandas.DataFrame([[1,2],[3,4],[5,6]], columns=["sample1","sample2"], index=[0,1,2])

print(df)

# 辞書からデータフレームを作ることもできる(プロパティがカラムになる)
dict = {
  "sample1": [1,3,5],
  "sample2": [2,4,6]
}
df = pandas.DataFrame(dict, index=[0,1,2])
print(df)
