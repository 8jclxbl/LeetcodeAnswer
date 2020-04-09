class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ = 0
        last = len(nums) - 1
        if last == 0:
            return True
        for i, j in enumerate(nums):
            if max_ >= i and i+j > max_:
                max_ = i + j
                if max_ >= last:
                    return True
        
        return False
    

if __name__ == "__main__":
    case = [3,2,1,0,4]
    s = Solution()
    print(s.canJump(case))