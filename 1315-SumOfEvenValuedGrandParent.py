# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumEvenGrandparent(self, root):
        if not root:
            return 0
        temp = 0
        if root.val % 2 == 0:
            temp = self.getGrandChildSum(root)
        return temp + self.sumEvenGrandparent(
            root.left) + self.sumEvenGrandparent(root.right)

    def getGrandChildSum(self, root):
        gSum = 0
        if root.left:
            gSum += root.left.left.val if root.left.left else 0
            gSum += root.left.right.val if root.left.right else 0

        if root.right:
            gSum += root.right.left.val if root.right.left else 0
            gSum += root.right.right.val if root.right.right else 0

        return gSum
