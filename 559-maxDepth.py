class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return self.dfs(root,1)
    
    def dfs(self,root,depth):
        if not root: return 0
        if not root.children: return depth
        else:
            children = []
            for i in root.children:
                children.append(self.dfs(i,depth + 1))
            return max(children)

class Solution_b:
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root :
            return 0
        if not root.children :
            return 1
        length = 1+ max(self.maxDepth(node) for node in root.children)
        return length