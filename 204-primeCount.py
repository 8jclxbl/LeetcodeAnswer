class Solution:
    table = {2:0,3:1,5:2,7:3}
    def countPrimes(self, n: int) -> int:
        if n <= 2:return 0
        else:
            if n-1 in self.table:
                return self.isPrime(n) + self.isPrime(n-1) + self.table[n-1]
            else:
                temp = self.countPrimes(n - 1)
                self.table[n-1] = temp
                return self.isPrime(n) + self.isPrime(n-1) + temp 
    
    def isPrime(self,n):
        if n%2 == 0:
            if n == 2:return 1
            else:return 0
        else:
            i = 3
            while i < n**(1/2) + 1:
                if n%i == 0:return 0
                i += 2
            return 1
class Solution_a:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        temp = [0,0,1] + [1] * (n-2) 
        i = 2
        while i < n ** (1/2) + 1:
            cur = i + i
            while cur < n:
                temp[cur] = 0
                cur += i
            k = 1
            while i + k -1 < n and not temp[i + k]:
                k += 1
            i += k
        print(temp)
        return sum(temp[:-1])
    
   

if __name__ == "__main__":
    s = Solution_a()
    print(s.countPrimes(10))