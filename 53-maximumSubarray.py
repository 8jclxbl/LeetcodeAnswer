class Solution:
    def maxSubArray(self, nums):
        #初始化应为第一个值，一开始直接写0会出现对于第一个值小于0时直接返回0
        max_val = nums[0]
        tmp_val = 0
        for i in nums:
            if tmp_val >= 0:
                tmp_val += i
            else:
                tmp_val = i
            max_val = max(tmp_val,max_val)
        return max_val

if __name__ == "__main__":
    test  = [-2,1,-3,4,-1,2,1,-5,4]
    test1 = [1]
    s = Solution()
    print(s.maxSubArray(test1))