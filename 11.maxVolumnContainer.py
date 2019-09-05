#求最大的题，想办法一开始就构造最大的解
#这里要大的话要么两边的值的最小高度最大（不好控制）
#要么最长，直接第一个和最后一个
class Solution:
    def maxArea(self, height):
        l = len(height)
        if l <= 1: return -1
        left = 0
        right = l-1
        maxV = 0
        while left < right:
            h = min(height[left], height[right])
            maxV = max(maxV, h * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxV

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))