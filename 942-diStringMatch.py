class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        out = []
        max = len(S)
        min = 0
        for item in S:
            if item == "D":
                out.append(max)
                max -=1
            else:
                out.append(min)
                min +=1
        out.append(min)
        return out

class Solution_me:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l = len(S) 
        temp = [i for i in range(l+1)]
        for i in range(l):
            if S[i] == 'D':
                temp[i],temp[i+1] = temp[i+1],temp[i]
                
        changed = True
        while changed:
            changed = False
            for i in range(l):
                if S[i] == 'D' and temp[i] < temp[i+1]:
                    changed = True
                    temp[i],temp[i+1] = temp[i+1],temp[i]
                if S[i] == 'I' and temp[i] > temp[i+1]:
                    changed = True
                    temp[i],temp[i+1] = temp[i+1],temp[i]
        return temp

if __name__ == "__main__":
    sm = Solution_me()
    s = Solution()
    print(sm.diStringMatch('DIDIDI'))
    print(sm.diStringMatch('IDIDID'))