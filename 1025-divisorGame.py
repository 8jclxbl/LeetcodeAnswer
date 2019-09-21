#抢到2的必胜，反推所有的偶数有必胜的方法
class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0

class Solution_dp:
    table = {1:False,2:True}
    def divisorGame(self, N: int):
        print(self.table)
        if N in self.table:
            return self.table[N]
        else:
            for i in range(1,N//2 + 1):
                if N % i == 0:
                    print(i)
                    if self.divisorGame(N-i):
                        self.table[N] = False
                    else:
                        self.table[N] = True
                        return True
            return False
            
if __name__ == "__main__":
    s = Solution()
    sdp = Solution_dp()
    print(sdp.divisorGame(10))
            
            
        