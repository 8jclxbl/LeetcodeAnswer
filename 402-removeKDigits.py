class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        length = len(num)
        if num[0] == '0':
            i = 0
            j = 1
            while i + j < length:
                if num[i+j] == '0':
                    j += 1
                else:
                    break   
            if i + j == length:
                return '0'
            num = num[i+j:]

        if k == 0:
            return num
        elif length == k:
            return '0'
        else:
            for i in range(length - 1):
                if num[i] > num[i+1]:
                    return self.removeKdigits(num[0:i] + num[i+1:], k - 1)
            return self.removeKdigits(num[0:length - 1], k - 1)
if __name__ == "__main__":
    case = dict(num = "10200", k = 1)
    s = Solution()
    print(s.removeKdigits(**case))
        

        


        