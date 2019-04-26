import random
import math

def chi_test(rand_num,bins):
    expected = len(rand_num)/bins
    numbers_in_bin = [0 for i in range(bins)]
    obs_diff_the = [0 for i in range(bins)]
    for i in rand_num:
        numbers_in_bin[int(i*bins)] += 1

    for i in range(bins):
        obs_diff_the[i] = ((numbers_in_bin[i] - expected)**2) / expected

    summed = sum(obs_diff_the)
    return summed


def ks_test(rand_num,bins):
    range_lim = 1 / bins
    expected = []
    incrementor = range_lim
    numbers_in_bin = [0 for i in range(bins)]

    for i in range(bins):
        expected.append(incrementor)
        incrementor += range_lim

    for i in rand_num:
        numbers_in_bin[int(i*bins)] += 1

    for i in range(1,bins):
        numbers_in_bin[i] = numbers_in_bin[i] + numbers_in_bin[i-1]

    observed_vals = [numbers_in_bin[i] / len(rand_num) for i in range(bins)]
    obs_diff_the = [math.fabs(observed_vals[i] - expected[i]) for i in range(bins)]

    maximum = max(obs_diff_the)

    return maximum


rand_num = []
n = 100
bins = 10

for i in range(n):
    rand_num.append(random.random())



print("Chi_test value %f" % chi_test(rand_num,bins))

print("KS_Test value %f" % ks_test(rand_num,bins))