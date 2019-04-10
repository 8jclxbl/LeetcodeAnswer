class Solution:
    def levelOrder(self, root):
        if not root: return []
        res = [[root.val]]
        queue = [root]
        
        while queue:
            temp = []
            for i in queue:
                if i:
                    temp += i.children
            if temp:
                res.append([i.val for i in temp])
            else:break
            queue = temp
            
        return res