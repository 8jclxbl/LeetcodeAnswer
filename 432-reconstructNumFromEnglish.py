class Solution:
    table = {
            0: {'z': 1, 'e': 1, 'r': 1, 'o': 1}, 
            1: {'o': 1, 'n': 1, 'e': 1}, 
            2: {'t': 1, 'w': 1, 'o': 1}, 
            3: {'t': 1, 'h': 1, 'r': 1, 'e': 2}, 
            4: {'f': 1, 'o': 1, 'u': 1, 'r': 1}, 
            5: {'f': 1, 'i': 1, 'v': 1, 'e': 1}, 
            6: {'s': 1, 'i': 1, 'x': 1}, 
            7: {'s': 1, 'e': 2, 'v': 1, 'n': 1}, 
            8: {'e': 1, 'i': 1, 'g': 1, 'h': 1, 't': 1}, 
            9: {'n': 2, 'i': 1, 'e': 1}
    }
    fstCharIden = {0:'z',2:'w',4:'u',6:'x',8:'g'}
    scdCharIden = {1:'o',3:'h',5:'f',7:'s'}
    def originalDigits(self, s: str) -> str:
        self.count = {}
        for i in s:
            if i in self.count:
                self.count[i] += 1
            else:
                self.count[i] = 1

        res = []
        for k,v in self.fstCharIden.items():
            wordCount = self.remove(k,v)
            if wordCount != 0:
                res.append((k,wordCount))
                
        for k,v in self.scdCharIden.items():
            wordCount = self.remove(k,v)
            if wordCount != 0:
                res.append((k,wordCount))
        if 'n' in self.count:
            res.append((9,self.count['n']//2))

        return self.resProcess(res)

    def resProcess(self,res):
        temp = ['' for i in range(10)]
        for i in res:
            temp[i[0]] = str(i[0]) * i[1]
        return ''.join(temp)
        
    def remove(self,num,char):
        if char in self.count:
            factor = self.count[char]
            for k,v in self.table[num].items():
                self.count[k] -= factor * v
                if self.count[k] == 0:
                    self.count.pop(k)
            return factor
        else:
            return 0

class Solution_best:
    def originalDigits(self, s: str) -> str:
        count = {}
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        zero = count.get('z',0)
        six = count.get('x',0)
        eight = count.get('g',0)
        two = count.get('w',0)
        four = count.get('u',0)
        seven = count.get('s',0) - six
        three = count.get('h',0) - eight
        five = count.get('f',0) - four
        one = count.get('o',0) - zero - two - four
        nine = count.get('i',0) - six - eight - five
        return "0"*zero+"1"*one+"2"*two+"3"*three+"4"*four+"5"*five+"6"*six+"7"*seven+"8"*eight+"9"*nine
        
if __name__ == "__main__":
    s = Solution()
    print(s.originalDigits("owoztneoer"))