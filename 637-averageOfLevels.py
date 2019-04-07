class Solution:
    def averageOfLevels(self,root):
        if not root:return []
        res = []
        last_queue = [root]
        mean = lambda x:sum(x)/float(len(x))

        while last_queue:
            res.append(mean([i.val for i in last_queue]))
            temp_queue = []
            for i in last_queue:
                if i.left:
                    temp_queue.append(i.left)
                if i.right:
                    temp_queue.append(i.right)
            last_queue = temp_queue
            
        return res