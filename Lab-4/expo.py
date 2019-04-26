lmd = 1
n = int(input())

import math
import random
import matplotlib.pyplot as plt

def inv(x):
    return -math.log1p(-x) / lmd

z = [inv(random.uniform(0, 1)) for i in range(n)]

plt.hist(z)
plt.show()
plt.pause(1)
plt.close()
