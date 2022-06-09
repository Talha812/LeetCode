class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0]*maxSize
        self.index = -1       #index where to place element
        self.size = 0       #current size (how many elements are filled)

    def push(self, x: int) -> None:
        if(self.index < len(self.stack)-1):
            self.index += 1
            self.stack[self.index] = x
            self.size += 1
        else:
            return

    def pop(self) -> int:
        if(self.index == -1):
            return -1
        else:
            data = self.stack[self.index]
            self.index -= 1
            self.size -= 1
            return data

    def increment(self, k: int, val: int) -> None:
        if(self.size < k):
            for i in range(self.size):
                self.stack[i] = (self.stack[i]+val)
        else:
            for i in range(k):
                self.stack[i] = (self.stack[i]+val)


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


