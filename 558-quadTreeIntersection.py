# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            if quadTree1.val:
                return quadTree1
            else:
                return quadTree2
        if quadTree2.isLeaf:
            if quadTree2.val:
                return quadTree2
            else:
                return quadTree1
        topleft = self.intersect(quadTree1.topLeft,quadTree2.topLeft)
        topright = self.intersect(quadTree1.topRight,quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft,quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight,quadTree2.bottomRight)
        if topleft.isLeaf and topright.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topleft.val and topright.val and bottomLeft.val and bottomRight.val:
            return Node(True,True,None,None,None,None)
        else:
            return Node(False,False,topleft,topright,bottomLeft,bottomRight)