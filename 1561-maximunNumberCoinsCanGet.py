class Solution:
    def maxCoins(self, piles):
        piles.sort()
        lp = len(piles)
        sum_ = 0
        num = lp // 3
        for i in range(1, num + 1):
            sum_ += piles[lp - 2 * i]
        return sum_
