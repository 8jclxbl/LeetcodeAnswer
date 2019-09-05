class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        l = m + n
        mid = l // 2
        
        if l == 0:return 0
        if l == m:
            master = nums1
        elif l == n:
            master = nums2
        else:
            if nums1[0] < nums2[0]:
                master = nums1
                slave = nums2
            else:
                master = nums2
                slave = nums1
                
            count = 1
            while count <= mid:
                if count >= len(master):
                    master = master + slave
                    break
                if master[count] <= slave[0]:
                    count += 1
                else:
                    master,slave = master[:count] + slave,master[count:]
            
        if l % 2 == 0:return (master[mid]+master[mid-1]) / 2
        else:return master[mid]

class Solution_a:
    def findMedianSortedArrays(self,nums1,nums2):
        m = len(nums1)
        n = len(nums2)

        if m > n:
            nums1,nums2 = nums2,nums1
            m,n = n,m
        start = 0
        end = m
        mid = (m + n + 1) // 2

        while start <= end:
            i = (start + end) // 2
            j = mid - 1
            if i < end and nums2[j-1] > nums1[i]:
                start = i + 1
            elif i > start and nums1[i-1] > nums2[j]:
                end = i - 1
            else:
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i-1],nums2[j-1])
                if (m + n) % 2 == 1:
                    return max_left
                
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i],nums2[j])
                return (max_left + min_right) / 2
        return 0

if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1,2],[3,4]))
    print(s.findMedianSortedArrays([0,0],[0,0]))
    print(s.findMedianSortedArrays([],[1]))
    print(s.findMedianSortedArrays([2,2,2,2],[2,2,2]))
