class Solution:
    def searchRange(self, nums, target):
        if not nums: return [-1,-1]
        self.length = len(nums)
        self.target = target
        left = self.search_start(nums)
        if left == -1:
            return [-1,-1]
        right = self.search_end(nums,left)
        return [left,right]
        
    def search_start(self, nums):
        ed = self.length - 1
        st = 0
        while st < ed:
            mid = (ed + st) // 2
            if nums[mid] < self.target:
                st = mid + 1
            else:
                ed = mid
        if nums[st] == self.target:return st
        return -1

    def search_end(self, nums, left):
        ed = self.length - 1
        st = left
        target = self.target + 1
        if st == ed:
            return st 
        while st < ed:
            mid = (ed + st) // 2
            if nums[mid] < target:
                st = mid + 1
            else:
                ed = mid
        if nums[st] == self.target:
            return st
        return st-1

if __name__ == "__main__":
    s = Solution()
    test1 = dict(nums = [5,7,7,8,8,10], target = 8)
    test2 = dict(nums = [5,7,7,8,8,10], target = 6)
    test3 = dict(nums = [1], target = 1)
    test4 = dict(nums = [2,2], target = 2)
    print(s.searchRange(**test1))