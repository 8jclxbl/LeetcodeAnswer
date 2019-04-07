"""给定一个二叉搜索树的根结点 root, 返回树中任意两节点的差的最小值。"""

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        bstList = self.bst2List(root)
        length = len(bstList)
        i = 1
        minD = abs(bstList[0] - bstList[1])
        while i < length - 1:
            if minD == 1:return 1
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