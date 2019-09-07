class Solution:
    def search(self, nums, target):
        ed = len(nums) - 1
        st = 0
        while st < ed:
            mid = (ed + st) // 2
            if nums[mid] < target:
                st = mid + 1
            else:
                ed = mid
        if nums[st] == target:return st
        else:return -1
        
if __name__ == "__main__":
    s = Solution()
    # test1 = dict(nums = [-1,0,3,5,9,12], target = 9)
    # test2 = dict(nums = [-1,0,3,5,9,12], target = 0)
    # test3 = dict(nums = [-1,0,3,5,9,12], target = 3)
    # test4 = dict(nums = [-1,0,3,5,9,12], target = 12)
    # test5 = dict(nums = [-1,0,3,5,9,12], target = 2)

    # test = [test1,test2,test3,test4,test5]
    # for i in test:
    #     print(s.search(**i))

    test = dict(nums = [-1,0,3,5,9,12], target = 2)
    print(s.search(**test))