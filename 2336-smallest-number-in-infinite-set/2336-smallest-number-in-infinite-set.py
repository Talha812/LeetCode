class SmallestInfiniteSet:

    def __init__(self):
        self.minVal = 1
        self.sett = set()

    def popSmallest(self) -> int:
        if len(self.sett) > 0:
            temp = min(self.sett)
            self.sett.remove(temp)
            return temp

        else:
            temp = self.minVal
            self.minVal += 1
            return temp
        
    def addBack(self, num: int) -> None:
        if num < self.minVal:
            self.sett.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)