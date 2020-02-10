from .precomputed_rmq import PrecomputedRMQ
from .sparse_table_rmq import SparseTableRMQ

a = [3, 1, 5, 3, 4, 7, 6]

precomputed_rmq = PrecomputedRMQ(a)
sparse_table_rmq = SparseTableRMQ(a)

print(precomputed_rmq.query(0, len(a) - 1))
print(sparse_table_rmq.query(2, len(a)))
