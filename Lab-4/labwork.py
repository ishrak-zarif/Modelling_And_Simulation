import random, math

def bernouli(p):
    x = random.uniform(0, 1)
    if (x < p):
        return 1
    return 0

# print(bernouli(.5))


def binomial(n, p):
    m = 100
    z = []
    for i in range(m):
        ans = 0
        for j in range(n):
            if (random.uniform(0, 1) < p):
                ans = ans + 1
        z.append(ans)
    return z

# print(binomial(10, .5))


def geomatric(n, p):
    z = []
    for i in range(n):
        j = 0
        while(True):
            if (random.uniform(0, 1) < p):
                break
            j += 1
        z.append(j)
    return z

# print(geomatric(10, 0.5))

def exponential(n):
    lmd = 1
    z = []
    for i in range(n):
        x = -math.log1p(-random.uniform(0, 1)) / lmd
        z.append(x)
    return z

print(exponential(10))

