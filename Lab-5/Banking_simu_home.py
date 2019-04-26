import random
import simpy

INTERVAL_CUSTOMERS = 10.0


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
    print('%7.4f %s: Here I am' % (arrive, name))

    with counter.request() as req:
        yield req
        wait = env.now - arrive
        print('%7.4f %s: Waited %6.3f' % (env.now, name, wait))
        tib = random.expovariate(1.0 / time_in_bank)
        yield env.timeout(tib)
        print('%7.4f %s: Finished' % (env.now, name))

print('Bank System')
env = simpy.Environment()

counter = simpy.Resource(env, capacity=1)
env.process(source(env, INTERVAL_CUSTOMERS, counter))
env.run(until=100)