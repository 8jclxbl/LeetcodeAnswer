class KthLargest:
    def __init__(self, k: int, nums):
        self.heap = MinHeap(k,nums)

    def add(self, val: int) -> int:
        cur_ = self.heap.top()
        if self.heap.isFull() and val < cur_:
            return cur_
        else:
            temp = self.heap.add(val)
            if temp is None:
                return
            else:
                return temp

class MinHeap:
    def __init__(self, k, list_):
        self.values = [None for i in range(k + 1)]
        self.length = k
        self.tail = -1
        self.initByList(list_)
    
    def isFull(self):
        return self.tail == self.length - 1

    def initByList(self, list_):
        if not list_:
            return None
        cur = 0
        length = len(list_)
        while cur < length and cur < self.length:
            self.add(list_[cur])
            cur += 1
        if cur == self.length:
            while cur < length:
                if list_[cur] > self.top():
                    self.add(list_[cur])
                cur += 1
            
    def add(self,val):
        self.tail += 1
        self.values[self.tail] = val

        if self.tail != 0:
            self.up(self.tail)
        if self.tail == self.length:
            self.out()
        return self.top() 

    def up(self,pos):
        parent = (pos - 1) // 2
        if parent < 0:
            return None
        if self.values[parent] > self.values[pos]:
            self.values[parent],self.values[pos] = self.values[pos],self.values[parent]
            self.up(parent)

    def down(self, pos):
        left = pos * 2 + 1
        right = pos * 2 + 2
        if left <= self.tail:
            if right > self.tail:
                if self.values[pos] > self.values[left]:
                    self.values[left],self.values[pos] = self.values[pos],self.values[left]
            else:
                if self.values[left] > self.values[right]:
                    if self.values[pos] > self.values[right]:
                        self.values[right],self.values[pos] = self.values[pos],self.values[right]
                        self.down(right)
                else:
                    if self.values[pos] > self.values[left]:
                        self.values[left],self.values[pos] = self.values[pos],self.values[left]
                        self.down(left)

    def out(self):
        min_ = self.values[0]
        self.values[0] = self.values[self.tail]

        self.down(0)
        self.tail -= 1
        return min_

    def top(self):
        return self.values[0]

                            

if __name__ == "__main__":
    # k = KthLargest(2,[0])
    # print(k.add(-1))
    # print(k.add(1))
    # print(k.add(-2))
    # print(k.add(-4))
    # print(k.add(3))
    k = KthLargest(1,[])
    print(k.add(-3))
    print(k.add(-2))
    print(k.add(-4))
    print(k.add(0))
    print(k.add(4))