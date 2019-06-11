class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sumP = 0
        res = []
        for i in A:
            if i % 2 == 0: sumP += i
        for i in queries:
            temp = A[i[1]]
            if (temp + i[0]) % 2 != 0 and temp % 2 == 0:
                sumP -= temp
            if (temp + i[0]) % 2 == 0 and temp % 2 != 0:
                sumP += temp + i[0]
            if (temp + i[0]) % 2 == 0 and temp % 2 == 0:
                sumP += i[0]
                
            A[i[1]] += i[0]
            res.append(sumP)
        return res