# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        return self.flatten_(root)

    def flatten_(self, root):
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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution_recusive:
    def __init__(self):
        self.stack = []

    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        self.flatten_(cur)
        return root

    def flatten_(self, root):
        if not root:
            return
        else:
            if root.right:
                self.stack.append(root.right)
            if root.left:
                root.right = root.left
                root.left = None
            else:
                if not self.stack:
                    return
                root.right = self.stack.pop()
            self.flatten_(root.right)
