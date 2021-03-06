class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:return 0
        else:
            if root.val < L or root.val > R: 
                return self.rangeSumBST(root.left, L,R) + self.rangeSumBST(root.right, L,R)
            else:
                return root.val + self.rangeSumBST(root.left, L,R) + self.rangeSumBST(root.right, L,R)