class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_ = candies[0]
        for i in candies:
            if i > max_:
                max_ = i
        res = []
        for i in candies:
            if extraCandies >= max_ - i:
                res.append(True)
            else:
                res.append(False)
        return res
