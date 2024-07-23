# pip install pandas

import pandas

# 辞書からデータフレームを作る
df= pandas.DataFrame({
    "aaa":[100,200,300,400],
    "bbb":[500,600,700,800]
})
print(df)

# パターンを使って行を取得する
# 値が偶数の行だけ取得する
# pattern = [False, True, False, True]
# インデックスが偶数の行だけ取得する
# pattern = (df.index % 2 == 0)
# aaa列の値が３００より大きい行だけを取得する
# pattern = (df.aaa > 300)
# print(df[pattern])
# aaaが100より大きく400より小さい行だけ取得する
pattern1 = (df.aaa > 100)
pattern2 = (df.aaa < 400)
pattern = pattern1 & pattern2
print(df[pattern])
