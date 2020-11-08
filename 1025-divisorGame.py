# 归纳法
# 2人均是取自身的最优决策

class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0

class Solution1:
    def divisorGame(self, N):
        if N <= 1:return False
        else:
            table = [0 for i in range(N + 1)]
            table[2] = 1
            for i in range(3, N+1):
                for j in range(i//2, 0, -1):
                    if i%j == 0 and table[i - j] == 0:
                        table[i] = 1
            
            return table[N] == 1
        