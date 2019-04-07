class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        res = []
        last_queue = [root]
        
        while last_queue:
            res.insert(0, [i.val for i in last_queue])
            temp_queue = []
            for i in last_queue:
                if i.left:
                    temp_queue.append(i.left)
                if i.right:
                    temp_queue.append(i.right)
            last_queue = temp_queue

        return res
             