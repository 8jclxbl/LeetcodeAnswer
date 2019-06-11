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

class Solution(object):
    def minDepth(self, root):
        if not root:return 0
        if not root.left and not root.right: return 1
        if not root.left: return 1 + self.minDepth(root.right)
        if not root.right: return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.right), self.minDepth(root.left))


if __name__ == "__main__":
    s = Solution()
    t = Tree([1,2])
    print(s.minDepth(t.root))