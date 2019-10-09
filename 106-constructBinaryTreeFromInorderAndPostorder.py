class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        inorder_length = len(inorder)
        cur_val = postorder[-1]
        root = TreeNode(cur_val)
        if inorder_length == 1:return root
        root_idx = inorder.index(cur_val)
        
        left_inorder = inorder[0:root_idx]
        if root_idx == inorder_length - 1:
            right_inorder = []
        else:
            right_inorder = inorder[root_idx+1:]
            
        left_length = len(left_inorder)
        left_postorder = postorder[0:left_length]
        right_postorder = postorder[left_length:-1]
        root.left = self.buildTree(left_inorder,left_postorder)
        root.right = self.buildTree(right_inorder,right_postorder)
        return root
        
class Solution_best:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        d={j:i for i,j in enumerate(inorder)}
        k=len(postorder)-1
        def f(i,j):
            if i<j:
                nonlocal k
                t=TreeNode(postorder[k])
                k-=1
                t.right=f(d[t.val]+1,j)
                t.left=f(i,d[t.val])
                return t
        return f(0,len(inorder))