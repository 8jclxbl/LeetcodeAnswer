class Solution:
    def lowestCommonAncestor(self, root, p, q):
        pPath = self.search(root,p)
        qPath = self.search(root,q)
        i = 0
        upBound = min(len(pPath),len(qPath))
        while i < upBound:
            if pPath[i].val != qPath[i].val:
                return pPath[i-1]
            i += 1

        return pPath[i-1]
        
    def search(self,root,node):
        if not root:return []
        else:
            if node.val == root.val:
                return [root]
            elif node.val > root.val: 
                return [root] + self.search(root.right, node)
            elif node.val < root.val:
                return [root] + self.search(root.left, node)