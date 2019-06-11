class Solution:
    def permute(self, nums):
        self.res = []
        self.permute_([],nums)
        return self.res
        
    def permute_(self,lastRes,residual):
        length = len(residual)
        if not length: return self.res.append(lastRes)
        else:
            for i in range(length):
                result = [j for j in lastRes]
                temp = residual[i]
                curRes = residual[0:i] + residual[i+1:]
                result.append(temp)
                self.permute_(result,curRes)


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1,2,3]))