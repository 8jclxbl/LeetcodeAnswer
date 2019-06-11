class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        else:
            rootVal = preorder[0]
            idx = 0
            for i in preorder:
                if i > rootVal:break
                idx += 1

            root = TreeNode(rootVal)
            root.left = self.bstFromPreorder(preorder[1:idx])
            root.right = self.bstFromPreorder(preorder[idx:])
            return root