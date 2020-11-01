class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for i in range(0, l - 1):
            for j in range(i + 1, l):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for j in range(0, l // 2):
            for i in range(l):
                cur = l - 1 - j
                matrix[i][j], matrix[i][cur] = matrix[i][cur], matrix[i][j]
