class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        length = len(A)
        p = 0
        o = 1
        
        oError = False
        pError = False
        while o <= length - 1 and p <= length - 2:
            if A[o] % 2 == 1:
                o += 2
            else:
                oError = True
            if A[p] % 2 == 0:
                p += 2
            else:
                pError = True
                
            if oError and pError:
                A[o],A[p] = A[p],A[o]
                oError = False
                pError = False
                o += 2
                p += 2
                
        return A