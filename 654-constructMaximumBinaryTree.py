class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        else:
            
            maxVal = max(nums)
            idx = nums.index(maxVal)
            
            root = TreeNode(maxVal)
            root.left = self.constructMaximumBinaryTree(nums[:idx])
            root.right = self.constructMaximumBinaryTree(nums[idx+1:])
            
            return root