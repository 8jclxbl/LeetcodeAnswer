class Solution1:
    def combine(self, n, k):
        base = [i for i in range(1,n+1)]
        self.res = []
        self.maxL = k
        self.combine_(0,[],base)
        return self.res[0:len(self.res)//2]

    
    def combine_(self,curL,curRes,reisidual):
        if curL == self.maxL:
            self.res.append(curRes)
        else:
            
            length = len(reisidual)
            for i in range(length):
                newRes = [i for i in curRes]
                curResid = reisidual[0:i] + reisidual[i+1:]
                newRes.append(reisidual[i])
                self.combine_(curL + 1,newRes,curResid)


class Solution:
    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':
        self.results = []
        self.combine_(0, 0, k, n, [])
        return self.results
    def combine_(self,curL, i, k, n, result):
        print(curL,i,n-(k-curL)+1)
        if curL == k:
            self.results.append(result)
            return 
        for t in range(i, n-(k-curL)+1):
            self.combine_(curL+1, t + 1, k, n, result+[t+1])
        


if __name__ == "__main__":
    s = Solution()
    print(s.combine(4,2))