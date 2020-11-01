class Solution:
    def combinationSum(self, candidates, target):
        self.candidates = candidates
        self.lc = len(self.candidates)
        self.res = []
        self.back_trace(target, [], 0)
        return self.res

    def back_trace(self, target, path, start):
        if target < 0:
            return
        elif target == 0:
            self.res.append(path)
            return
        else:
            for i in range(start, self.lc):
                self.back_trace(target - self.candidates[i], path + [self.candidates[i]], i)


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2, 3, 5], 8))