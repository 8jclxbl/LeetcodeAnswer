class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self,values):
        if not values:
            self.root = None
        else:
            self.genFromList(values)

    def genFromList(self,List):
        self.root = TreeNode(List[0])
        cur = self.root
        curIdx = 0

        length = len(List)
        while curIdx < length:
            if curIdx * 2 + 1 < length:
                cur.left = TreeNode(List[curIdx * 2 + 1])
            if curIdx * 2 + 2 < length:
                cur.right = TreeNode(List[curIdx * 2 + 2])
            curIdx += 1

#96ms
class Solution1:
    def isSubtree(self, s, t):
        # 另一种思路，分别将两棵树序列化
        # 然后根据序列化的结果判断是否存在子树
        s_serialize = self.serialize(s)
        t_serialize = self.serialize(t)
        
        if t_serialize in s_serialize:
            return True
        else:
            return False
    
    def serialize(self, root):
        if root is None:
            return []
        
        def pre_order(root):
            if root:
                result.append('^' + str(root.val))
                pre_order(root.left)
                pre_order(root.right)
            else:
                result.append('^#')
                
        result = []
        pre_order(root)
        
        return ','.join(result)

#296ms
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s: return False
        else:
            if s.val == t.val:
                return self.isSame(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
            else:
                return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        
        
    def isSame(self,s,t):
        if (not s and not t) :return True
        if s and t:
            if (s.val == t.val):
                return self.isSame(s.left,t.left) and self.isSame(s.right,t.right)
            return False
        return False

if __name__ == "__main__":
    s = Tree([1,2,3])
    t = Tree([1,2])
    solution = Solution()
    print(solution.isSubtree(s.root,t.root))    
