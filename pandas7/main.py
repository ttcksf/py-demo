# pip install pandas

import pandas

data = {
    "aaa": [1,2,3],
    "bbb": [4,5,6],
    "ccc": [7,8,9]
}
df = pandas.DataFrame(data, index=[0,1,2])
print(df)

# 昇順　
print(df.sort_values(["aaa"],ascending=[True]))
# 降順
print(df.sort_values(["aaa"],ascending=[False]))
