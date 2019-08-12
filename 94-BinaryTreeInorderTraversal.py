# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
class Solution:
    def __init__(self):
        self.res = []
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.traverse(root)
        return self.res
        
        
    def traverse(self,node):
        if node:
            self.traverse(node.left)
            self.res.append(node.val)
            self.traverse(node.right)
"""
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        temp = [root]
        travered = {}
        res = []
        while temp:
            cur = temp.pop()
            if cur.left and cur.left not in travered:
                temp.append(cur)
                cur = cur.left
                temp.append(cur)
            else:
                res.append(cur.val)
                travered[cur] = True
                if cur.right:
                    cur = cur.right
                    temp.append(cur)
        return res
                    
