import matplotlib.pyplot as plt

a = 5
c = 3
m = 16
zi_1 = 0
l=[]

def rnd(zi_1, a, c, m):
    global zi
    while 1:
        zi_1 = (a*zi_1 + c)%m
        yield zi_1

def gcd(n1, n2):
    if n2%n1 == 0:
        return n1
    else:
        return gcd(n2%n1, n1)

k=0
while k<m:
    print("For seed value : %s" %(zi_1))
    temp = 1
    if gcd(c, m) == 1:
        for i in range(2, m+1):
            for j in range(2, i):
                if i%j == 0:
                    break
                else:
                    if m%i == 0:
                        if (a-1)%i == 0:
                            continue
                        else:
                            print("No full period")
                            temp = 0
                            break
        if temp==1 and m%4==0 and (a-1)%4==0:
            print("Full period")


    for i in rnd(zi_1, a, c, m):
        if i in l:
            # print(len(l))
            break
        else:
            l.append(i)
    zi_1 = zi_1 + 1
    k = k + 1
    # print(l)

# def rng():
#     global zi_1
#     zi_1 = (a * zi_1 + c) % m
#     return zi_1
#
# for i in range(16):
#     print(rng())

plt.hist(l, bins = 5, normed = True)
plt.show()