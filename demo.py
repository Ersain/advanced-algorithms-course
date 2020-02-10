from precomputed_rmq import PrecomputedRMQ

a = [3, 1, 5, 3, 4, 7, 6]

precomputed_rmq = PrecomputedRMQ(a)
for i in precomputed_rmq.precomputed:
    print(i)
