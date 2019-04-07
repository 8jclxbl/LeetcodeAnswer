# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:return None
        length = len(nums)
        if length == 1:
            return TreeNode(nums[0])
        else:
            mid = length//2
            print(nums[mid])
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[0:mid])
            root.right = self.sortedArrayToBST(nums[mid + 1:])
            return root

def traverse(root):
    if root:
        print(root.val)
        traverse(root.left)
        traverse(root.right)

s = Solution()
root = s.sortedArrayToBST([-10,-3,0,5,9])
#traverse(root)