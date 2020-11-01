class Solution:
    table = {
        '2': "abc",
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        res = []
        for i in words:
            if self.match(num, i):
                res.append(i)
        return res

    def match(self, code, word):
        if len(code) != len(word):
            return False
        for c, w in zip(code, word):
            if w not in self.table[c]:
                return False
        return True