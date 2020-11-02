class Solution:
    def countCharacters(self, words, chars):
        table = Solution.count(chars)
        cnt = 0
        for i in words:
            cur = {k: v for k, v in table.items()}
            for j in i:
                if j in cur:
                    if cur[j] == 0:
                        break
                    else:
                        cur[j] -= 1
                else:
                    break
            else:
                cnt += len(i)
        return cnt

    @staticmethod
    def count(chars):
        base = {}
        for i in chars:
            if i in base:
                base[i] += 1
            else:
                base[i] = 1
        return base
