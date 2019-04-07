def sortedSquares(A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([i ** 2 for i in A])

print(sortedSquares([-4,-1,0,3,10]))