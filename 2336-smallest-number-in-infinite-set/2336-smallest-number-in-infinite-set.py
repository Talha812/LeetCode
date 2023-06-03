class SmallestInfiniteSet:

    def __init__(self):
        self.min_val = 1
        self.rec = set()

    def popSmallest(self) -> int:
        if len(self.rec) != 0:
            temp = min(self.rec)
            self.rec.remove(temp)
            return temp
        else:
            temp = self.min_val
            self.min_val += 1
            return temp

    def addBack(self, num: int) -> None:
        if num < self.min_val:
            self.rec.add(num)


            
            
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)