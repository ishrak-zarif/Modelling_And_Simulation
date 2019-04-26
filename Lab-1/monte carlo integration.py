import random
import matplotlib.pyplot as plt

a = 0
b = 2
n = 10000
s=0

plt.xlim(0, n)
plt.ylim(0, 5)
plt.hlines(2, 0, n)
plt.ion()
plt.show()

for i in range(1, n):
    s = s+random.uniform(a, b)
    if(i%100==0):
        x = s*(b-a)
        x = x/i
        plt.title(str(x))
        plt.scatter(i, x)
        plt.draw()
        plt.pause(0.1)
plt.close()
