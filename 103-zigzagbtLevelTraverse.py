class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self,values):
        self.values = values
        self.length = len(values)
        self.root = TreeNode(self.values[0])
        self.gen_tree(self.root,0)

    def gen_node(self,val):
        if val is None:return None
        else:
            return TreeNode(val)

    def gen_tree(self,root,cur):
        if cur < self.length: 
            left = 2 * cur + 1
            right = 2 * cur + 2
            if left < self.length:
                root.left = self.gen_node(self.values[left])
                self.gen_tree(root.left,left)
            if right < self.length:
                root.right = self.gen_node(self.values[right])
                self.gen_tree(root.right,right)


class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return []
        queue = [root]
        res = [[root.val]]
        level = 1
        while queue:
            temp = []
            cur_res = []
            while queue:
                cur = queue.pop(0)

                if cur.left:
                    temp.append(cur.left)
                    cur_res.append(cur.left.val)

                if cur.right:
                    temp.append(cur.right)
                    cur_res.append(cur.right.val)
                
            queue = temp
            if temp:
                if level%2 == 1:cur_res = cur_res[::-1]
                res.append(cur_res)
            level += 1
        return res

if __name__ == "__main__":
    #test = Tree([1,2,3,4,None,None,5])
    test = Tree([3,9,20,None,None,15,7])
    s = Solution()
    print(s.zigzagLevelOrder(test.root))