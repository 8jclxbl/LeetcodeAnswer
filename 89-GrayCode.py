# 格雷码，递归算法
# n 位格雷码，先算出n-1位格雷码
# 前一半为n-1位格雷码加上前导0，后一半逆序加上前导1
class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        else:
            base = self.grayCode(n - 1)
            add = 1 << (n - 1)
            b_half = [i + add for i in base[::-1]]
            return base + b_half
