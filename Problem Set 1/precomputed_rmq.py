"""
Implementing the PrecomputedRMQ type using the ⟨O(n^2), O(1)⟩ RMQ data structure that
precomputes the answers to all possible range minimum queries.
"""


class PrecomputedRMQ:
    def __init__(self, arr):
        n = len(arr)
        self.precomputed = [[0 for i in range(n)] for j in range(n)]

        for j in range(n):
            self.precomputed[j][j] = arr[j]

        for i in range(n):
            for j in range(i + 1, n):
                self.precomputed[j - 1 - i][j] = min(
                    self.precomputed[j - 1 - i][j - 1], self.precomputed[j - i][j]
                )

    def query(self, i, j):
        return self.precomputed[i][j]
