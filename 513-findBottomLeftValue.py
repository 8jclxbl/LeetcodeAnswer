# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = []
        queue.append(root)
        while queue:
            queue_ = []
            after_row = True
            while queue:
                cur = queue.pop(0)
                if after_row:
                    first = cur
                    after_row = False
                if cur.left:
                    queue_.append(cur.left)
                if cur.right:
                    queue_.append(cur.right)
            queue = queue_
        return first.val