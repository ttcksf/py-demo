import matplotlib.pyplot as plt

x = ["J","F","M","A"]
y = [100,150,80,120]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# x軸、y軸、線の形、線の色、線の太さ、点の形
ax.plot(x, y, "-", c="#666", linewidth=1, marker="+")

plt.show()
