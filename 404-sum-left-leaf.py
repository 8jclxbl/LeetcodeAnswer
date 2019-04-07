class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sumOfLeftLeaves(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        def recur(root):
            if not root:
                return 0
            if root.left and root.left.left == None and root.left.right == None and root.right == None:
                return result + root.left.val
            else:
                return result + recur(root.left) + recur(root.right)
        return recur(root)