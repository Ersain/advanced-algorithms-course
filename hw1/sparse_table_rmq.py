from math import log2


class SparseTableRMQ:
    def __init__(self, arr):
        n = len(arr)
        self.precomputed = [[0 for i in range(n)] for j in range(int(log2(n)) + 1)]

        for i in range(n):
            self.precomputed[0][i] = arr[i]

        for j in range(1, int(log2(n)) + 1):
            i = 0
            while (i + 2 ** (j - 1)) < n:
                self.precomputed[j][i] = min(
                    self.precomputed[j - 1][i], self.precomputed[j - 1][i + 2 ** (j - 1)]
                )
                i += 1

    def query(self, i, j):
        n = j - i
        k = int(log2(n))
        return min(
            self.precomputed[k][i], self.precomputed[k][j - 2 ** k]
        )
