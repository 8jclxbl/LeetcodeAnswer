# 注意题目中已经给出数字的范围，由于并不多，所以可以直接对区间进行判断

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            temp = Solution.order(i)
            if temp % 2 == 0:
                count += 1
        return count

    @staticmethod
    def order(num):
        count = 1
        while True:
            num = num // 10
            if not num:
                return count
            else:
                count += 1