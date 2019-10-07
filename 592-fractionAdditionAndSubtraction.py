# 利用正则表达式进行划分
# temp_frac = re.split(r'[+-]', expression)
# temp_sign = list(re.sub('\d+/\d+', "", expression))

class Solution:
    @classmethod
    def gcd(cls,m,n):
        if n == 0:
            return m
        else:
            return cls.gcd(n,m%n)
    
    def fractionAddition(self, expression: str) -> str:
        nums = {}
        length = len(expression)
    
        if expression[0] == '-':
            sign = -1
            i = 1
        else:
            sign = 1
            i = 0
            
        hasSep = False
        while i < length:
            if not hasSep:
                j = 0
                while i + j < length:
                    if expression[i+j] == '/':
                        break
                    j += 1
                dividend = int(expression[i:i+j]) * sign
                hasSep = True
            else:
                j = 0
                while i + j < length:
                    if expression[i+j] == '+':
                        sign = 1
                        break
                    elif expression[i+j] == '-':
                        sign = -1
                        break
                    j += 1
                divisor = int(expression[i:i+j])
                if divisor in nums:
                    nums[divisor] += dividend
                else:
                    nums[divisor] = dividend
                hasSep = False
            i += j + 1
        
        resDivisor = 1
        resDividend = 0
        for k,v in nums.items():
            resDividend = resDividend * k + v * resDivisor
            resDivisor *= k
            
        common = self.gcd(resDividend,resDivisor)
        resDividend //= common
        resDivisor //= common

        if resDividend < 0:
            return '-{}/{}'.format(-1 * resDividend,resDivisor)
        else:
            return '{}/{}'.format(resDividend,resDivisor)
            
if __name__ == "__main__":
    s = Solution()
    test = "1/3-1/2"
    print(s.fractionAddition(test))    
                