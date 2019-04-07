class Solution:
    
    """
    此版本只考虑了父子结点间的差
    def getMinimumDifference(self, root: TreeNode) -> int:
        if root.left:
            leftTreeVal = self.getMinimumDifference(root.left)
            left = abs(root.val - root.left.val)
            if leftTreeVal < left:
                left =  leftTreeVal
        if root.right:
            rightTreeVal = self.getMinimumDifference(root.right)
            right = abs(root.val - root.right.val)
            if rightTreeVal < right:
                right = rightTreeVal

        if root.left and root.right:
            if left < right:
                return left
            else:
                return right
        elif root.left and not root.right:
            return left
        elif root.right and not root.left:
            return right
        else:return 65535
    """
    def getMinimumDifference(self, root):
        bstList = self.bst2List(root)
        length = len(bstList)
        i = 1
        minD = abs(bstList[0] - bstList[1])
        while i < length - 1:
            temp = abs(bstList[i] - bstList[i + 1])
            if temp < minD:
                minD = temp
            i += 1
        return minD

    def bst2List(self, root):
        if root.left:
            left = self.bst2List(root.left)
        else:
            left = []
        
        if root.right:
            right = self.bst2List(root.right)
        else:
            right = []

        return left + [root.val] + right

    