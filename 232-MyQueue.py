class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.StackIn = []
        self.StackOut = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.StackIn.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.StackOut:
            return self.StackOut.pop()
        else:
            if not self.StackIn:
                raise IndexError
            else:
                while self.StackIn:
                    temp = self.StackIn.pop()
                    self.StackOut.append(temp)
            return self.StackOut.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.StackOut:
            if not self.StackIn:
                raise IndexError
            else:
                while self.StackIn:
                    temp = self.StackIn.pop()
                    self.StackOut.append(temp)
        return self.StackOut[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.StackIn and not self.StackOut:return True
        else:return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()