import random, math

def fun(a, x):
    for i in range(x):
        t = random.uniform(0, 1)
        if (t <=a):
            return random.uniform(0, 1)
        else:
            x=random.uniform(0, 1)
            return math.sqrt(x)

h=fun(0.5, 1)
print(h)