class Solution:
    def minOperations(self, n: int) -> int:
        tmp = n // 2
        if n % 2 == 1:
            return (tmp + 1) * tmp
        else:
            return tmp * tmp
