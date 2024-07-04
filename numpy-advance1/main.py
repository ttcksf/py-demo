# pip install numpy
import numpy
# ndarrayを2次元配列のように書くと行列になる
test = numpy.array([[1,2,3],[4,5,6]])
print(test)
# 0行0列の値
print(test[0,0])
# 1行2列の値
print(test[1,2])
# 0行目
print(test[0])

# 特徴的な行列(デフォルトが小数点なので整数であればdtype=int64を第二引数に指定)
# ゼロ行列(第一引数はタプル型)
print(numpy.zeros((3,3), dtype=numpy.int64))
# 三角行列
print(numpy.tri(4, dtype=numpy.int64))
# 全ての要素が１の行列
print(numpy.ones((3,3), dtype=numpy.int64))
