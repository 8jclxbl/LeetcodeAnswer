class Solution:
    def createTargetArray(self, nums, index):
        res = []
        for a, b in zip(index, nums):
            temp_l = res[:a]
            temp_r = res[a:]
            res = temp_l + [b] + temp_r

        return res
        