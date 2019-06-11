class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self,values):
        self.genFromList(values)
        
    def genFromList(self,values):
        length = len(values)
        nodes = [TreeNode(i) for i in values]
        self.root = nodes[0]
        i = 0
        while i < length:
            cur = nodes[i]
            if i * 2 + 1 < length: cur.left = nodes[i * 2 + 1]
            if i * 2 + 2 < length: cur.right = nodes[i * 2 + 2]
            i += 1

def GenNodes(values):
    temp = []
    for i in values:
        if i:
            temp.append(TreeNode(i))
    return temp

def Traverse(root):
    if root:
        print(root.val)
        Traverse(root.left)
        Traverse(root.right)

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        else:
            if root.left:
                if not root.left.left and not root.left.right:
                    if root.left.val != 1:root.left = None
                else:
                    root.left = self.pruneTree(root.left)
                    
            if root.right:
                if not root.right.left and not root.right.right:
                    if root.right.val != 1: root.right = None
                else:
                    root.right = self.pruneTree(root.right)

            if not root.left and not root.right and root.val != 1:return None
            return root

class Solution1:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        else:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            if not root.left and not root.right and root.val != 1:return None
            return root

if __name__ == "__main__":
    test = Tree([1,0,1,0,0,0,1])
    s = Solution()
    Traverse(test.root)
    print('-' * 10)
    root = s.pruneTree(test.root)
    print('-' * 10)
    Traverse(root)
