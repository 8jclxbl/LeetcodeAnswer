class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        else:
            if abs(self.height(root.left) - self.height(root.right)) > 1:return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
 
    
    def height(self,root):
        if not root: return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right)) 

class Solution1:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def balanced(root):
            if not root:
                return 0
            left = balanced(root.left)
            right = balanced(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return balanced(root) != -1