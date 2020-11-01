class Solution:
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        #print(input)
        for i, c in enumerate(input):
            if c in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        print(l,r,c)
                        res.append(eval(f'{l}{c}{r}'))
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.diffWaysToCompute("2-1-1"))