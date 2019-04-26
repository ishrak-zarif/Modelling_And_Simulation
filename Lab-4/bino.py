# random number generating from binomial distribution using bernoulli trial

import random
import matplotlib.pyplot as plt

def rn(x):
    ans = 0
    for i in range(x):
        if (random.uniform(0, 1) < .3):
            ans = ans + 1

    return ans


n, m = map(int, input().split())
# n is the range
# m is the number of random numbers

z = [rn(n) for i in range(m)]

plt.hist(z, bins = 100)
plt.show()
plt.pause(1)
plt.close()