class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return self.travers(root)[1]
            
        
    def travers(self,root):
        if not root:
            return 0,0
        else:
            #sum,tilt
            [ls,lt] = self.travers(root.left)
            [rs,rt] = self.travers(root.right)
            
            return root.val + ls + rs, abs(ls - rs) + lt + rt