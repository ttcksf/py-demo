import matplotlib.pyplot as plt
import numpy

x = numpy.random.rand(10)
y = numpy.random.rand(10)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# xの値、yの値、点の大きさ、点の透明度、点の太さ、マーカーの形、マーカーの色
ax.scatter(x,y,s=100, alpha=1, linewidths=1, marker="+",c="#666")
plt.show()
