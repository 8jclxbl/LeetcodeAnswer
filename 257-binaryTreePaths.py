#有时候直接输出解反而比获取中间值再输出解简单
class Solution:
    def binaryTreePaths(self, root):
        if not root: return []
        else:
            temp = []
            left =  self.binaryTreePaths(root.left)
            right = self.binaryTreePaths(root.right)
            if left: 
                for i in left:
                    temp.append(str(root.val) + '->' + i)
            if right:
                for i in right:
                    temp.append(str(root.val) + '->' + i)
            if not temp:temp = [str(root.val)]
            return temp