class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length1 = len(str1)
        length2 = len(str2)
        
        if length1 < length2:
            length1,length2 = length2,length1
            str1,str2 = str2,str1

        step = length2
        while step > 0:
            if length1 % step != 0:
                step -= 1
                continue
            else:
                factor = str2[0:step]
                j = 0
                while j != length1:
                    if str1[j:j + step] != factor:
                        break
                    j += step
                else:
                    k = 0 
                    while k != length2:
                        if str2[k:k+step] != factor:
                            break
                        k += step
                    else:
                        return factor
                step -= 1
        return ""

class Solution_best:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:return ""
        length1 = len(str1)
        length2 = len(str2)
        gcdLength = Solution_best.gcd(length1,length2)
        return str1[0:gcdLength]

    @staticmethod
    def gcd(a,b):
        if b == 0:
            return a
        return Solution_best.gcd(b,a%b)

if __name__ == "__main__":
    test = dict(str1 = "ABCABC", str2 = "ABC")
    test1 = dict(str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX", str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")
    
    s = Solution()
    print(s.gcdOfStrings(**test1))

    sb = Solution_best()
    print(sb.gcdOfStrings(**test1))