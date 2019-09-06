class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = [root]
        res = [[root.val]]
        while queue:
            temp = []
            cur_res = []
            while queue:
                cur = queue.pop(0)

                if cur.left:
                    temp.append(cur.left)
                    cur_res.append(cur.left.val)

                if cur.right:
                    temp.append(cur.right)
                    cur_res.append(cur.right.val)
                
            queue = temp
            if temp:
                res.append(cur_res)
            
        return res