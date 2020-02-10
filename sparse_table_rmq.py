from math import log2


class SparseTableRMQ:
    def __init__(self, arr):
        n = len(arr)
        self.precomputed = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            self.precomputed[0][i] = arr[i]

        for j in range(1, log2(n)):
            pass
