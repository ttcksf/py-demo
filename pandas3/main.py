# pip install pandas

import pandas

# 辞書からデータフレームを作る
dict = {
    "data": [100,200,300,400,500]
}
df = pandas.DataFrame(dict)
print(df)

# pandasではデータフレームという構造に変換することで統計することができる
# 平均
# print(df.mean())

# データ件数
# print(df.count())

# 最大値、最小値
# print(df.max(), df.min())

# ランダム
print(df.sample())

# 統計の一括取得
print(df.describe())
