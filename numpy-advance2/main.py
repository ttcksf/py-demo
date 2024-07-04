# pip install numpy

import numpy

a = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
b = numpy.array([[10,11,12],[13,14,15],[16,17,18]])
# 1次元のベクトルと同じような計算が2次元の行列にもできる（答えが二次元になる）
# 足し算
print(a + b)
# 引き算
print(b - a)
# 内積
print(numpy.dot(a,b))
# 外積
print(numpy.cross(a,b))

c = numpy.array([[1,2],[3,4]])
# 転置
print(c.T)
# トレース（対角成分の和）
print(c.trace())
