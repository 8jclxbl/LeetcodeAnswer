from math import sqrt


class Solution:
    def findContinuousSequence(self, target):
        tail = 1 + 8 * target
        total_res = []
        for i in range(1, (target // 2) + 1):
            tmp = 4 * i * (i - 1) + tail
            base = sqrt(tmp)
            if int(base) == base:
                res = []
                cur = i
                ct = target
                while ct > 0:
                    res.append(cur)
                    ct -= cur
                    cur += 1
                total_res.append(res)
        return total_res
