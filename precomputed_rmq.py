"""
Implementing the PrecomputedRMQ type using the ⟨O(n^2), O(1)⟩ RMQ data structure that
precomputes the answers to all possible range minimum queries.
"""


class PrecomputedRMQ:
    def __init__(self, arr):
        self.precomputed = [[0 for i in range(len(arr))] for j in range(len(arr))]

        for j in range(len(arr)):
            self.precomputed[j][j] = arr[j]

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                self.precomputed[j - 1 - i][j] = min(
                    self.precomputed[j - 1 - i][j - 1], self.precomputed[j - i][j]
                )


a = [39, 91, 62, 31, 80]
rmq = PrecomputedRMQ(a)

for i in rmq.precomputed:
    print(i)

print(rmq.precomputed[0][2])
