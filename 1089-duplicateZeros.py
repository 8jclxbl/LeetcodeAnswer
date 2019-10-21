class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        temp = [0 for i in range(length)]
        idx = 0
        for i in arr:
            if i == 0:
                idx += 2
            else:
                temp[idx] = i
                idx += 1
            if idx >= length:
                break
            print(i,idx)
        for idx,val in enumerate(temp):
            arr[idx] = val
        return arr

if __name__ == "__main__":
    test = [1,0,2,3,0,4,5,0]
    s = Solution()
    print(s.duplicateZeros(test))