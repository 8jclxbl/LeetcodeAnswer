class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B: return True
        l = len(A)
        i = 0
        while i < l:
            A = A[1:] + A[0]
            if A[0] == B[0]:
                if A == B:return True
            i += 1
        return False