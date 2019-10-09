from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = 1
        stack = deque()
        stack.append(root)
        while stack:
            count = 0
            stack_ = deque()
            while stack:
                cur = stack.popleft()
                if not cur.left:
                    return 2 ** level - 1 + count
                stack_.append(cur.left)
                count += 1
                if not cur.right:
                    return 2 ** level - 1 + count
                stack_.append(cur.right)
                count += 1
            level += 1
            stack = stack_

if __name__ == "__main__":
    s = Solution()
    Nodes = [TreeNode(i) for i in [1,2,3,4,5,6,7,8]]
    root = Nodes[0]
    Nodes[0].left = Nodes[1]
    Nodes[0].right = Nodes[2]
    Nodes[1].left = Nodes[3]
    Nodes[1].right = Nodes[4]
    Nodes[2].left = Nodes[5]
    Nodes[2].right = Nodes[6]
    Nodes[3].left = Nodes[7]
    print(s.countNodes(root))