# pip install pandas

import pandas

df1 = pandas.DataFrame({
      "data": [100,200,300]
})
df2 = pandas.DataFrame({
      "data": [400,500,600]
})
print(df1)
print(df2)
# データフレーム同士の計算
# df = df1 + df2
df = df2 - df1
print(df)

# データフレーム内の置換
df3 = pandas.DataFrame({
      "aaa": [100,200,300],
      "bbb": [200,400,600]
})
print(df3)
df3 = df3.replace(200, 201)
print(df3)
