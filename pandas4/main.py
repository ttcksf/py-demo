# pip install pandas

import pandas

# 辞書からデータフレームを作る
dict = {
    "aaa": [100,200,300],
    "bbb": [400,500,600]
}
df = pandas.DataFrame(dict)
print(df)
# 列単位で取得
print(df.aaa)
# 列単位で値の更新（書いた順に上から並ぶ仕組みなので順番に注意）
df.aaa = pandas.Series([101,102,103])
print(df)

# 行単位で取得
print(df.loc[0])
# 行単位で値の更新（indexでどの列かを見分けるのでindexの順番に注意）
df.loc[0] = pandas.Series([101,102], index=["aaa","bbb"])
print(df)
