class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        length = len(arr)
        i = 0
        table = {}
        min_ = 1 << 31
        while i < length - 1:
            tmp = arr[i+1] - arr[i]
            if tmp in table:
                table[tmp].append([arr[i],arr[i+1]])
            else:
                table[tmp] = [[arr[i],arr[i+1]]]
            if tmp < min_:
                min_ = tmp
            i += 1
        return table[min_]