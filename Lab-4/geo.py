n = int(input())
p = float(input())

import random
import matplotlib.pyplot as plt

def rn():
    i = 0
    while(True):
        if(random.uniform(0, 1) < p):
            return i
        i += 1

z = [rn() for i in range(n)]

plt.hist(z)
plt.show()
plt.pause(1)
plt.close()
