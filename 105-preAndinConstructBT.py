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
    @classmethod
    def inorder(cls,root):
        if root:
            print(root.val)
            cls.inorder(root.left)
            cls.inorder(root.right)

class Solution:
    def buildTree(self, preorder, inorder):
        length = len(preorder)
        if length == 0:return None
        if length == 1:
            return TreeNode(preorder[0])
        else:
            root_val = preorder[0]
            root = TreeNode(root_val)
            piv = inorder.index(root_val)

            left_inorder = inorder[0:piv]
            right_inorder = inorder[piv+1:]

            left_length = len(left_inorder)
            left_preorder = preorder[1:1 + left_length]
            right_preorder = preorder[left_length + 1:]

            root.left = self.buildTree(left_preorder,left_inorder)
            root.right = self.buildTree(right_preorder,right_inorder)
            return root

if __name__ == "__main__":
    s = Solution()

    # test = Tree([3,9,20,None,None,15,7])
    # preorder = [3,9,20,15,7]
    # inorder = [9,3,15,20,7]

    # test = Tree([1,2])
    # preorder = [1,2]
    # inorder = [1,2]

    test = Tree([3,2,4,1,None])
    preorder = [3,2,1,4]
    inorder = [1,2,3,4]

    root = s.buildTree(preorder,inorder)
    Tree.inorder(root)