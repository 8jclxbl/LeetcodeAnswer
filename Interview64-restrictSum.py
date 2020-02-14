#无法使用分支，循环，乘除
#短路原理，与时只要有一个False就判断False

class Solution:
    def sumNums(self, n: int) -> int:
        return n and n + self.sumNums(n-1)