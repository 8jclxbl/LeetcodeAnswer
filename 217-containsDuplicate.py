class Solution:
    def containsDuplicate(self, nums):
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                return True
        return False