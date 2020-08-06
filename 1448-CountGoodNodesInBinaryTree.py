# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root):
        self.good = 0
        self.goodNodes_(root, root.val)
        return self.good

    def goodNodes_(self, root, max_):
        if not root:
            return
        else:
            if root.val >= max_:
                max_ = root.val
                self.good += 1
            self.goodNodes_(root.left, max_)
            self.goodNodes_(root.right, max_)
