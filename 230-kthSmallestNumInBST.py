# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return None
        
        stack = []
        curr = root
        count = 0
        while curr or stack:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                count += 1
                if count == k:
                    return node.val
                curr = node.right