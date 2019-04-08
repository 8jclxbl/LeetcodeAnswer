#注意最大直径可能会出现在子树中

#暴力憨憨式
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:return 0
        dRoot = self.dfs(root.left,0) + self.dfs(root.right,0)
        return max(dRoot,self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
    
        
    def dfs(self,root,depth):
        if not root: return depth
        return max(self.dfs(root.left,depth + 1), self.dfs(root.right, depth + 1))

#优化版本，增加输出参数数目来减少重复长度递归的次数
class Solution1:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:return 0
        return self.dfs(root)[0]
    
        
    def dfs(self,root):
        if not root: return 0,0,0
        ld,llm,lrm = self.dfs(root.left)
        rd,rlm,rrm = self.dfs(root.right)
        ml = max(llm,lrm)
        mr = max(rlm,rrm)
        d = max(ld,rd,ml+mr)
        return d,ml+1,mr+1