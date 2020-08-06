class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)

        if l1 < l2:
            num1, num2 = num2, num1
            l1, l2 = l2, l1

        res = 0
        carry = 0
        base = 1
        for i in range(l2):
            n1 = ord(num1[l1 - 1 - i]) - 48
            n2 = ord(num2[l2 - 1 - i]) - 48

            s = n1 + n2 + carry
            if s > 10:
                carry = 1
                s -= 10
            else:
                carry = 0

            res += s * base
            base *= 10

        temp = l1 - l2
        while temp:
            n = ord(num1[temp - 1]) - 48
            s = n + carry

            if s > 10:
                carry = 1
                s -= 10
            else:
                carry = 0
            res += s * base
            base *= 10
            temp -= 1
        if carry:
            res += base
        return str(res)


class Solution_:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        if m - n > 0:
            num2 = '0' * (m - n) + num2
            l = m
        else:
            num1 = '0' * (n - m) + num1
            l = n
        r = ''
        i = 0
        carry = 0
        while i < l:
            s = ord(num1[l - 1 - i]) + ord(num2[l - 1 - i]) + carry - 96
            if s >= 10:
                carry = 1
                s -= 10
            else:
                carry = 0
            r = str(s) + r
            i += 1
        if carry:
            r = '1' + r
        return r


if __name__ == "__main__":
    s = Solution()
    print(s.addStrings('54', '641'))
