import matplotlib.pyplot as plt
import numpy

x1 = numpy.random.rand(10)
y1 = numpy.random.rand(10)
x2 = numpy.random.rand(10)
y2 = numpy.random.rand(10)


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# xの値、yの値、点の大きさ、点の透明度、点の太さ、マーカーの形、マーカーの色
ax.scatter(x1, y1, s=50, alpha=1, linewidths=1, marker="X",c="c")
ax.scatter(x2, y2, s=50, alpha=1, linewidths=1, marker="D",c="y")
plt.show()
