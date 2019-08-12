class heap:
    def __init__(self,values):
        self.heap_ = values
        self.length = len(self.heap_ )
        self.heap_init()
        
        
    def heap_init(self):
        tail = 1
        while tail < self.length:
            cur = tail
            while cur > 0:
                cur = self.up_(cur)
            tail += 1
            
    def out_(self):
        top = self.heap_[0]
        self.heap_[0] = self.heap_[self.length-1]
        self.length -= 1
        cur = 0
        while cur != -1:
            cur = self.down_(cur)
        return top
        
    def in_(self,val):
        self.heap_[self.length] = val
        cur = self.length
        self.length += 1
        while cur != -1:
            cur = self.up_(cur)
            
            
    @staticmethod
    def find_par(cur):
        return (cur - 1)//2
        
    def up_(self,cur):
        par = self.find_par(cur)
        if par == -1:return par
        if self.heap_[cur] > self.heap_[par]:
            self.heap_[cur], self.heap_[par] = self.heap_[par], self.heap_[cur]
            return par
        else:
            return -1
    
    def down_(self,cur):
        ls = 2 * cur + 1
        rs = 2 * cur + 2
        if  ls < self.length and rs < self.length:
            if self.heap_[ls] > self.heap_[rs]: 
                if self.heap_[ls] > self.heap_[cur]:
                    self.heap_[cur], self.heap_[ls] = self.heap_[ls], self.heap_[cur]
                    return ls
                else:
                    return -1
            else:
                if self.heap_[cur] < self.heap_[rs]:
                    self.heap_[cur], self.heap_[rs] = self.heap_[rs], self.heap_[cur]
                    return rs
                else:
                    return -1
        elif ls < self.length:
            if self.heap_[ls] > self.heap_[cur]:
                self.heap_[cur], self.heap_[ls] = self.heap_[ls], self.heap_[cur]
                return ls
            else:
                return -1
        else:
            return -1


class Solution:
    def lastStoneWeight(self, stones):
        h = heap(stones)
        while h.length > 1:
            x = h.out_()
            y = h.out_()
            if x - y == 0:
                continue
            else:
                h.in_(abs(x-y))
        if h.length == 0:return 0
        else:return h.out_()
        

if __name__ == "__main__":
    s = Solution()
    res = s.lastStoneWeight([2,7,4,1,8,1])
    print(res)
        