class Solution:
    def diagonalSum(self, mat):
        n = len(mat)
        temp = {}
        sum_ = 0
        for i in range(n):
            temp[(i, i)] = 1
            sum_ += mat[i][i]

        for i in range(n):
            if (n - 1 - i, i) not in temp:
                sum_ += mat[n - 1 - i][i]
        return sum_
