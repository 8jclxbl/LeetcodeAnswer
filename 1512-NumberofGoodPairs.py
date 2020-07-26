class Solution:

    def numIdenticalPairs(self, nums):
        n = len(nums)
        mask = [0 for i in range(n)]
        
        cmpt = lambda x:x * (x - 1) / 2
        pairs = 0

        cur = 0
        while cur < n:
            if not mask[cur]:
                cnt = 0
                for idx in range(cur + 1, n):
                    if nums[idx] == nums[cur]:
                        cnt += 1
                        mask[idx] = 1
                if cnt: mask[cur] = 1
                
                pairs += cmpt(cnt + 1)
            cur += 1

        return int(pairs)

        
if __name__ == '__main__':
    s = Solution()
    print(s.numIdenticalPairs([1,1,1,1]))