class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        table = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        state = [-1] * (2**5)
        state[0] = 0
        cur = 0
        cnt = 0
        res = 0

        for i in s:
            if i in table:
                cur ^= table[i]
            if state[cur] != -1:
                res = max(res, cnt + 1 - state[cur])
            else:
                state[cur] = cnt + 1
            cnt += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findTheLongestSubstring("eleetminicoworoep"))
