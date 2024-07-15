import matplotlib.pyplot as plt

label = ["a", "b", "c"]
x = ["J","F","M"]
y = [100,200,300]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# x軸、y軸、棒の太さ（１が基準）、枠線の太さ、枠線の色
ax.bar(x, y, width=0.4, linewidth=10, edgecolor="#eee")
plt.show()
