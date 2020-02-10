from math import log2


class SparseTableRMQ:
    def __init__(self, arr):
        n = len(arr)
        self.preprocessed = [[0 for i in range(n)] for j in range(int(log2(n)) + 1)]

        for i in range(n):
            self.preprocessed[0][i] = arr[i]

        for j in range(1, int(log2(n)) + 1):
            i = 0
            while (i + 2 ** (j - 1)) < n:
                self.preprocessed[j][i] = min(
                    self.preprocessed[j - 1][i], self.preprocessed[j - 1][i + 2 ** (j - 1)]
                )
                i += 1

    def query(self, i, j):
        n = j - i
        k = int(log2(n))
        return min(
            self.preprocessed[k][i], self.preprocessed[k][j - 2 ** k]
        )


a = [3, 1, 5, 3, 4, 7, 6]
rmq = SparseTableRMQ(a)
for i in rmq.preprocessed:
    print(i)

print(rmq.query(2, len(a)))
