# pip install numpy
import numpy
# ndarrayをベクトルとみなしてベクトルで使う計算が使える
a = numpy.array([1,2,3])
b = numpy.array([4,5,6])
print(a)
print(b)
# 足し算
add_result = a + b
print(add_result)
# 引き算
sub_result = b - a
print(sub_result)

# 内積
inner_result = numpy.dot(a,b)
print(inner_result)

# 外積
cross_result = numpy.cross(a,b)
print(cross_result)
