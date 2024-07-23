# pip install pandas

import pandas

test = pandas.Series([100,200,300], index=["a","b","c"])
print(test)
# キーを指定して特定の値だけ取得できる
print(test["a"])
# もしくはこれでもOK
print(test.a)

# キーを指定して更新もできる
test.a = 101
print(test.a)
