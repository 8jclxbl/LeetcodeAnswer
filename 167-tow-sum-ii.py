#best answer
def twoSum(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            x = numbers[i]
            y = target - x
            while numbers[j] > y:
                j -= 1
            if numbers[j] == y:
                return  [i + 1, j + 1]
            i += 1
        
        raise IndexError


def twoSum1(numbers, target):
    i = 0
    length = len(numbers)
    while i < length:
        res = target - numbers[i]
        lo = i + 1
        hi = length - 1

        while lo <= hi:
            mi = (lo + hi) // 2
            if numbers[mi] == res:
                if i == mi:continue        
                else:return [i+1,mi+1]
            elif res < numbers[mi]:
                hi = mi -1
            else:
                lo = mi + 1
    
        i += 1
    return []

numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers,target))