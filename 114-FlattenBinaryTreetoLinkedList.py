# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:return root
        return self.flatten_(root)
        
        
    def flatten_(self,root):
        root_ = root
        root_temp = []
        while True:
            if root.right:
                root_temp.append(root.right)
            root.right = root.left
            root.left = None
            if root.right:
                root = root.right
            else:
                break
        while root_temp:
            root.right = self.flatten_(root_temp.pop())
            while root.right:
                root = root.right
        return root_

            