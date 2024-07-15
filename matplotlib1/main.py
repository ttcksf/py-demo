# pip install matplotlib
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

# 画面を作成
fig = plt.figure()

# 軸を作成
ax1 = fig.add_subplot(1,1,1)

# データを点で配置
x = [0,1,2]
y = [0,1,2]
ax1.plot(x,y)

# グラフの表示
plt.show()
