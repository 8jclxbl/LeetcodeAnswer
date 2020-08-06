class Solution:
    def minCostToMoveChips(self, chips):
        paul = 0
        odd = 0

        for i in chips:
            if i % 2 == 0:
                paul += 1
            else:
                odd += 1

        return min(paul, odd)
