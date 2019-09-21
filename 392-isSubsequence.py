class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:return True
        if not t:return False
        sl = len(s)
        tl = len(t)
        i = 0
        j = 0
        while i < sl and j < tl:
            print()
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == sl and s[i-1] ==t[j-1]:return True
        else:return False

if __name__ == "__main__":
    case = dict(s = "abc", t = "ahbgdc")
    s = Solution()
    print(s.isSubsequence(**case))
            