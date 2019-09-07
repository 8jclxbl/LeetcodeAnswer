class Solution:
    table = {0:1,1:1,2:2}
    def numTrees(self, n: int) -> int:
        if n in self.table:
            return self.table[n]
        else:
            cur = 0
            res = 0
            while cur < n:
                left = cur
                right = n - cur - 1
                res += self.numTrees(left) * self.numTrees(right)
                cur += 1
            self.table[n] = res 
            return res
            
if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(5))
    