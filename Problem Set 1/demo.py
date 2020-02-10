from precomputed_rmq import PrecomputedRMQ
from sparse_table_rmq import SparseTableRMQ

a = [3, 1, 5, 3, 4, 7, 6]

precomputed_rmq = PrecomputedRMQ(a)

print(precomputed_rmq.query(0, len(a) - 1))

a = [3, 1, 5, 3, 4, 7, 6]
rmq = SparseTableRMQ(a)
for i in rmq.preprocessed:
    print(i)

print(rmq.query(2, len(a)))
