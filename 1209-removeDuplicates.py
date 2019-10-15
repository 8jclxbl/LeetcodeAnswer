class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        changed = True
        while 1:
            changed = False
            length = len(s)
            i = 0
            delIdx = []
            while i < length:
                if i + k <= length and s[i:i + k] == s[i] * k:
                    delIdx.append(i)
                    delIdx.append(i+k)
                    i += k
                    changed = True
                else:
                    i += 1
            if not changed:break
            temp = []
            temp.append(s[0:delIdx[0]])
            delIdxLength = len(delIdx)
            i = 1
            while i < delIdxLength - 1:
                temp.append(s[delIdx[i]:delIdx[i+1]])
                i += 2
            temp.append(s[delIdx[-1]:])
            s = ''.join(temp)
        return s
9
if __name__ == "__main__":
    s = Solution()
    test = ("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy",4)
    print(s.removeDuplicates(*test))