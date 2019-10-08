# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum_ = 0
        self.func(root)
        return root
        
    def func(self,root):
        if not root:
            return 
        else:
            self.func(root.right)
            root.val += self.sum_
            self.sum_ = root.val
            self.func(root.left)
        
        
        
    
            
            