class Solution:
    def generateParenthesis(self, n):
        if n == 0: return []
        if n == 1: return ['()']
        else:
            temp = []
            for i in self.generateParenthesis(n-1):
                for j in range(n):
                    temp.append(i[0:j] + '()' + i[j:])
            return list(set(temp))

class Solution_best:
    cache = {1: ['()'], 0: ['']}
    def generateParenthesis(self, n):
        ret = []
        if n in self.cache:
            return self.cache[n]
        for i in range(n):
            inners = self.generateParenthesis(i)
            outers = self.generateParenthesis(n-i-1)
            for inner in inners:
                for outer in outers:
                    ret.append('(' + inner + ')' + outer)
        return ret

if __name__ == "__main__":
    sb = Solution_best()
    print(sb.generateParenthesis(5))