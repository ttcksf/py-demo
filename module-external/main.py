# pip install matplotlib
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7,8,9,10]
y = [0,1,4,9,16,25,36,49,64,81,100]

plt.plot(x,y)
plt.xlabel("products")
plt.ylabel("result")
plt.show()
