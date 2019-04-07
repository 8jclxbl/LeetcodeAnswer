class Solution:
    def tree2str(self, t):
        if not t:
            return ''
        if not t.left and not t.right: return str(t.val)
        else:
            left = self.tree2str(t.left)
            right = self.tree2str(t.right)
            if right != '':
                right ='({0})'.format(right)
            return "{0}({1}){2}".format(t.val,left,right)