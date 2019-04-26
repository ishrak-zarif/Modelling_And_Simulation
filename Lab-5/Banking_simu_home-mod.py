import random
import simpy
#import matplotlib.pyplot as plt
from matplotlib.pyplot import *

INTERVAL_CUSTOMERS = 10.0

X = []
Y = []

cus_counter = 0

def source(env, interval, counter):
    customer_count = 0
    while True:
        c = customer(env, 'Customer%02d' % customer_count, counter, time_in_bank=12.0)
        env.process(c)
        t = random.expovariate(1.0/ interval)
        yield env.timeout(t)
        customer_count += 1


def customer(env, name, counter, time_in_bank):
    arrive = env.now
    global cus_counter
    cus_counter += 1
    X.append(int(arrive))
    Y.append(cus_counter)
    print('%7.4f %s: Here I am' % (arrive, name))

    with counter.request() as req:
        yield req
        wait = env.now - arrive
        print('%7.4f %s: Waited %6.3f' % (env.now, name, wait))
        tib = random.expovariate(1.0 / time_in_bank)
        yield env.timeout(tib)
        print('%7.4f %s: Finished' % (env.now, name))
        cus_counter -= 1
        X.append(int(env.now))
        Y.append(cus_counter)

print('Bank System')


env = simpy.Environment()

counter = simpy.Resource(env, capacity=1)
env.process(source(env, INTERVAL_CUSTOMERS, counter))
env.run(until=100)


print(X)
print(Y)


# plt.bar(X,Y)
# plt.hist(Y, X, histtype='bar')
# plt.legend(pos="best")
# plt.xlabel("Time")
# plt.ylabel("Number of persons waiting in the queue")
# plt.show()
bar(X,Y)
plot(X,Y)
show()