import matplotlib.pyplot as plt
import numpy

# 平均値165, 標準偏差（ばらつき具合）6, 要素数100個
x = numpy.random.normal(165, 6, 100)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.hist(x, bins=20, color="#666", ec="#000")

plt.show()
