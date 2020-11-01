class Solution:
    def singleNumbers(self, nums):
        tmp = 0
        for i in nums:
            tmp ^= i

        diff = Solution.find_one(tmp)
        tmp1 = 0
        tmp2 = 0

        a = []
        b = []
        print(tmp, diff)
        for i in nums:
            if i | diff == i:
                tmp1 ^= i
                a.append(i)
            else:
                tmp2 ^= i
                b.append(i)
        print(a, b)
        return [tmp1, tmp2]

    @staticmethod
    def find_one(n):
        cur = 1
        while n:
            if n & 1 == 1:
                return cur
            else:
                n >>= 1
            cur *= 2


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumbers([1, 2, 5, 2]))
