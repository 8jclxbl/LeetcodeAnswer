class Solution:
    def swapNumbers(self, numbers):
        numbers[1] += numbers[0]
        numbers[0] = numbers[1] - numbers[0]
        numbers[1] -= numbers[0]
        return numbers

# 还可以使用异或，相对于加法，当数字特别大的时候异或更快一些
