class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        wordsFrequent = []
        for i in words:
            wordsFrequent.append(Solution.getF(i))
        self.wordsFrequent = sorted(wordsFrequent)
        res = []
        for i in queries:
            frequent = Solution.getF(i)
            res.append(self.countRes(frequent))
        return res        
        
    @staticmethod
    def getF(word):
        temp = [0 for i in range(26)]
        for i in word:
            temp[ord(i) - 97] += 1
            
        return Solution.findMin(temp)
        
    @staticmethod
    def findMin(temp):
        for i in temp:
            if i != 0:
                return i
            
    def countRes(self,frequent):
        count = 0
        for i in self.wordsFrequent:
            if frequent < i:
                count += 1
        return count