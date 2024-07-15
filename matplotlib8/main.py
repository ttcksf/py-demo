import matplotlib.pyplot as plt

label = ["AAA","BBB","CCC"]
x = [10,20,40]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# 値、ラベル、色、Trueで時計回り、開始角度
ax.pie(x, labels=label, colors=['red', 'blue', 'green'], counterclock=False, startangle=90)

# 表示補正
ax.axis("equal")

plt.show()
