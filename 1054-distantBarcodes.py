class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        l = len(barcodes)
        if l == 1:return barcodes
        count = {}
        for i in barcodes:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        
        temp = sorted(count.items(),key = lambda x:x[1],reverse = True)
        m = len(temp)
        i = 0
        j = 0
        while i < l:
            cur = temp[j]
            cur_code = cur[0]
            cur_num = cur[1]
            while cur_num and i < l:
                barcodes[i] = cur_code
                i += 2
                cur_num -= 1
            if cur_num == 0:
                j += 1
        i = 1
        if cur_num == 0:
            cur = temp[j]
            cur_code = cur[0]
            cur_num = cur[1]
        while i < l:
            while cur_num and i < l:
                barcodes[i] = cur_code
                i += 2
                cur_num -= 1
            if cur_num == 0:
                j += 1
                if j == m:break
            cur = temp[j]
            cur_code = cur[0]
            cur_num = cur[1]
        
        return barcodes
                
                
            