import random
import math

bins,nums = map(int, input().split())

observed = []
result = []

def KS_test():

    for i in all_num:
        count=0
        for j in all_num:
            if(j<=i):
                count = count+1
        observed.append(count/nums)
    for j in range(nums):
        a = math.fabs(all_num[j]-observed[j])
        result.append(a)
    res = max(result)
    print(res)


all_num = []


for i in range(nums):
    all_num.append(random.random())

KS_test()