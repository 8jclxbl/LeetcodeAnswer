# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:return []
        values = {}
        def travel(root):
            nonlocal values
            if root:
                if root.val in values:
                    values[root.val] += 1
                else:
                    values[root.val] = 1
                travel(root.left)
                travel(root.right)
        travel(root)
        temp = sorted(values.items(),key = lambda x:x[1],reverse = True)
        res = [temp[0][0]]
        for i in temp[1:]:
            if i[1] == temp[0][1]:
                res.append(i[0])
            else:
                break
        return res
        