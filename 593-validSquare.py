class Solution:
    def validSquare(self, p1, p2, p3, p4) -> bool:
        dists = []
        dists.append(Solution.distanceSquare(p1,p2))
        dists.append(Solution.distanceSquare(p1,p3))
        dists.append(Solution.distanceSquare(p1,p4))
        dists.append(Solution.distanceSquare(p2,p3))
        dists.append(Solution.distanceSquare(p2,p4))
        dists.append(Solution.distanceSquare(p3,p4))
    
        count = {}
        for i in dists:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        if len(count) != 2:
            return False
        
        count1,count2 = count.items()
        if count1[0] * 2 == count2[0]:
            if count1[1] == 4 and count2[1] == 2:
                return True
        
        if count2[0] * 2 == count1[0]:
            if count2[1] == 4 and count1[1] == 2:
                return True

        return False
                
    @staticmethod
    def distanceSquare(a,b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

if __name__ == "__main__":
    s = Solution()
    test = dict(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1])
    print(s.validSquare(**test))