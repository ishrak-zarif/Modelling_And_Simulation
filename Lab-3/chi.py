import random


bins,nums = map(int, input().split())

observed = []
expected = 1

def chi_sqr_test():
    global expected
    expected = len(all_num) / bins
    count = 0
    ran = 1/bins
    up=ran
    down =0

    for i in range(bins):
        for j in all_num:
            if(down < j and j<=up):
                count = count + 1
        observed.append(count)
        count = 0
        up = up + ran
        down = down + ran
    final()


def final():
    res=0
    for k in range(bins):
        res = ((observed[k]- expected)**2)/expected + res

    print(res)

all_num = []


for i in range(nums):
    all_num.append(random.random())

chi_sqr_test()

