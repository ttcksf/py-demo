import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

x1 = [0,4,8,12,16,20]
y1 = [0,8,16,24,32,40]
ax.plot(x1,y1)

x2 = [0,2,4,6,8,10,12,14,16,18,20]
y2 = [0,2,4,6,8,10,12,14,16,18,20]
ax.plot(x2,y2)

# グリッド線をオンにする
ax.grid(True)

# x軸の範囲
ax.set_xlim(left=0, right=20)
# y軸の範囲
ax.set_ylim(bottom=0, top=40)
# x軸のラベル
ax.set_xlabel("speed")
# y軸のラベル
ax.set_ylabel("km")
# グラフのタイトル
ax.set_title("sample image")
# グラフのラベル
ax.legend(["f(x)=2x", "f(x)=x"])

plt.show()
