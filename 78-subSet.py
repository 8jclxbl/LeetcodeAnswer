class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res = []
        for i in range(2 ** length):
            idx = bin(i)[2:]
            if length - len(idx) > 0:
                idx = '0' * (length - len(idx)) + idx
            temp = []
            cur = 0
            for j in idx:
                if j == '1':
                    temp.append(nums[cur])
                cur += 1
            res.append(temp)
        return res