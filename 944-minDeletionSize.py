class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        r = len(A)
        c = len(A[0])
        count = 0

        for i in range(c):
            temp = []
            for j in range(r):
                temp.append(A[j][i])
            if not self.isNotDecOrder(temp):count += 1
        return count
            
    def isNotDecOrder(self,l):
        for i in range(len(l)-1):
            if l[i] > l[i + 1]:return False
        else:return True