class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:return []
        temp = [root.val]
        for i in root.children:
            temp += self.preorder(i)
        return temp