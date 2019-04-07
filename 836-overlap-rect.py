def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        acrossh = min(rec1[3],rec2[3])
        acrossl = max(rec1[1],rec2[1])
        verticalr = min(rec1[2],rec2[2])
        verticall = max(rec1[0],rec2[0])
        return acrossh > acrossl and verticalr > verticall

def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        
        x1,y1,x2,y2=rec1
        x3,y3,x4,y4=rec2
        return (x3-x2)*(x4-x1)<0 and (y3-y2)*(y4-y1)<0

def isRectangleOverlap(rec1, rec2):
    [xa0,ya0,xa1,ya1] = rec1
    [xb0,yb0,xb1,yb1] = rec2

    if (ya0 < yb1 and xa0 < xb1) and (yb0 < ya1 and xb0 < xb1):
        return True

    return False


rec1 = [0,0,2,2]
rec2 = [1,1,3,3]

#rec1 = [0,0,1,1]
#rec2 = [1,0,2,1]

rec1 = [2,17,6,20]
rec2 = [3,8,6,20]
print(isRectangleOverlap(rec1, rec2))