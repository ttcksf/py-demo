# pip install numpy
# pip install matplotlib

import numpy
# 連立一方程式
# x + 2y = 4
# 2x + 3y = 5
left_val = numpy.array([[1,2],[2,3]])
right_val = numpy.array([4,5])
result = numpy.linalg.solve(left_val, right_val)
print(result)

import matplotlib.pyplot as plt

# 乱数
# 10個の小数点で乱数を生成
num = numpy.random.rand(10)
print(num)

# 正規分布の乱数
# 要素数100個、平均３、標準偏差４
test = numpy.random.normal(3, 4, 100)
print(test)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.hist(test, bins=10, color="#333", ec="#eee", alpha=0.5)
plt.show()
