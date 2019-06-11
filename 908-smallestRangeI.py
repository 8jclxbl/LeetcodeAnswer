class Solution:
    def smallestRangeI(self, A, K):
        if len(A) == 1:return 0
        low = []
        high = []
        for i in A:
            low.append(i-K)
            high.append(i+K)
            
        l = max(low)
        h = min(high)
        print(l,h)
        if h >= l: return 0
        else: return l - h
        
    
if __name__ == "__main__":
    s= Solution()
    print(s.smallestRangeI([0,10],2))