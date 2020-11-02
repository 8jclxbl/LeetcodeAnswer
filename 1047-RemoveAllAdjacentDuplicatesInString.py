from typing import ChainMap


class Solution:
    def removeDuplicates(self, S: str) -> str:
        changed = True
        while changed:
            changed = False
            ls = len(S)
            cur = 0
            tmp = []
            while cur < ls:
                if cur < ls - 1 and S[cur] == S[cur + 1]:
                    cur += 2
                    changed = True
                else:
                    tmp.append(S[cur])
                    cur += 1
            S = ''.join(tmp)
        return S


class Solution_base:
    def removeDuplicates(self, S):
        dup = {chr(i) * 2 for i in range(97, 97 + 26)}
        ll = len(S)
        while True:
            for i in dup:
                S = S.replace(i, "")
            if len(S) == ll:
                break
            else:
                ll = len(S)
        return S
