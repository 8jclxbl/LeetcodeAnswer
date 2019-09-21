class Solution:
    table = {1:1,2:2}
    def climbStairs(self, n: int) -> int:
        if n in self.table:
            return self.table[n]
        else:
            self.table[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.table[n]

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(35))