class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.tr_(root)
        return self.res
        
    def tr_(self,root):
        if root:
            self.res.append(root.val)
            self.tr_(root.left)
            self.tr_(root.right)

class Solution_Iter:
    def preorderTraversal(self,root):
        if not root:return None
        stack = [root]
        values = []
        while stack:
            cur = stack.pop()
            values.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return values
        
    