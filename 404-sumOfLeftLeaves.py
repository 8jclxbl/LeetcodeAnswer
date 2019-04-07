class Solution:
#既然时左叶子就定义为左叶子，不要偷懒按叶子处理
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        if root.left and root.left.left==None and root.left.right==None:
            return root.left.val+self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)