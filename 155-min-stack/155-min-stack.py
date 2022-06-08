class MinStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, val: int) -> None:
        self.stack1.append(val)
      
        if(len(self.stack2) == 0 or self.stack2[-1] >= val):
            self.stack2.append(val)

    def pop(self) -> None:
        if(len(self.stack1) <= 0):
            return
        t = self.stack1.pop()
        if(t == self.stack2[-1]):
            self.stack2.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        
        return self.stack2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()