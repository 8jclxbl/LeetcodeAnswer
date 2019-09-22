class Solution:
    def myAtoi(self, str: str) -> int:
        l = len(str)
        i = 0
        #受限处理掉前面空的部分
        while i < l and str[i] == ' ':
            i += 1
        #如果全空，返回0
        if i == l:
            return 0

        #如果带符号，需要进行处理
        sign = 1
        if str[i] == '-':
            i += 1
            sign = -1
        elif str[i] == '+':
            i += 1

        #截取数字部分，如果有小数，直接转化为整数 
        j = 0
        while i+j < l and ord(str[i + j])> 47 and ord(str[i + j]) < 58:
            j += 1
        if j == 0:return 0
        base = str[i:i + j]
        big = 1 << 31
        res = int(base) * sign
        if res < (big * -1):
            return big * -1
        if res > big - 1:
            return big -1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi(" -43"))


