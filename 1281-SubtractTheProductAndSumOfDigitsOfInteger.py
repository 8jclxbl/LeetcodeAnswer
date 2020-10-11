class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = []
        while n:
            temp.append(n % 10)
            n //= 10
        sum_ = 0
        res_ = 1
        for i in temp:
            sum_ += i
            res_ *= i

        return res_ - sum_
