# pip install numpy
import numpy
# 行列を作る
row_column = numpy.array([[1,2,3],[4,5,6]])
print(row_column)
# arrayを使って生成した行列はndarrayというデータになる(リストではない)
# リストは要素をカンマで区切る書き方
# print([1,2,3])

# 範囲指定した上で行列を作る
# 1以上６未満を１ずつの間隔で作る
row_column = numpy.arange(1,6,1)
print(row_column)
# 作成した行列にはインデックス番号のような添え字でアクセスできる
print(row_column[0])
# 要素の変更も可能
row_column[0] = 2
print(row_column)
# 小数点にする
test = numpy.arange(1,6,1, dtype=numpy.float64)
print(test)

# 行列の各要素に関数を実行する（for文が不要）
# 1を加算
print(numpy.add(test,1))
# 2乗する
print(numpy.square(test))
