#before opt 108ms
def isMonotonic(A):
        """
        :type A: List[int]
        :rtype: bool
        """
        l = len(A)
        count0 = 0
        count1 = 0
        for i in range(l-1):
            if A[i] >= A[i+1]:
                count0 += 1
            if A[i] <= A[i+1]:
                count1 += 1
            
        if count0 == l-1 or count1 == l-1:
            return True
        else:
            return False

#after opt 72ms
def isMonotonic(A):
        """
        :type A: List[int]
        :rtype: bool
        """
        l = len(A)
        if l <= 2:return True
        for k in range(l):
            if k == l-1:return True
            if A[k] == A[k+1]:
                continue
            else:
                idc = A[k] > A[k+1]
                break
        
        if idc:
            for i in range(k+1,l-1):
                if A[i] < A[i+1]:
                    return False
        else:
            for i in range(k+1,l-1):
                if A[i] > A[i+1]:
                    return False
        
        return True

