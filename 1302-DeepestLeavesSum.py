# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def deepestLeavesSum(self, root):
        queue = [root]
        sums = []
        while queue:
            temp = []
            sum_ = 0
            for node in queue:
                if node.left:
                    temp.append(node.left)
                    sum_ += node.left.val
                if node.right:
                    temp.append(node.right)
                    sum_ += node.right.val
            sums.append(sum_)
            queue = temp
        return sums[-2]
