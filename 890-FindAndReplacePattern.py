class Solution:
    def findAndReplacePattern(self, words, pattern):
        len_p = len(pattern)
        res = []

        for word in words:
            flag = True
            temp = {}
            temp_re = {}
            for j in range(len_p):
                la = word[j]
                lp = pattern[j]
                if lp not in temp:
                    temp[lp] = la
                else:
                    if temp[lp] != la:
                        flag = False
                        continue

                if la not in temp_re:
                    temp_re[la] = lp
                else:
                    if temp_re[la] != lp:
                        flag = False
                        continue

            if flag:
                res.append(word)
        return res


if __name__ == "__main__":
    s = Solution()
    print(
        s.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"],
                                'abb'))
