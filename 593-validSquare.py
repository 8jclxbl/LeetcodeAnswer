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
        
        c1,c2 = count.values()
        if (c1 == 4 and c2 == 2) or (c1 == 2 and c2 == 4):
            return True
        else:
            return False
                
    @staticmethod
    def distanceSquare(a,b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

if __name__ == "__main__":
    s = Solution()
    test = dict(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1])
    print(s.validSquare(**test))