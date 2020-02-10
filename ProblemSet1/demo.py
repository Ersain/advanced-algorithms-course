from ProblemSet1.precomputed_rmq import PrecomputedRMQ
from ProblemSet1.skylines import skylines
from ProblemSet1.sparse_table_rmq import SparseTableRMQ

a = [3, 1, 5, 3, 4, 7, 6]

precomputed_rmq = PrecomputedRMQ(a)
sparse_table_rmq = SparseTableRMQ(a)

print(
    precomputed_rmq.query(i=0, j=4) == 1
)
print(
    sparse_table_rmq.query(i=2, j=6) == 3
)

print(skylines([4, 2, 3, 1]) == 6)
print(skylines([1, 3, 7, 4, 2]) == 9)
print(skylines([2, 7, 1, 8, 3, 0, 5, 4]) == 8)
