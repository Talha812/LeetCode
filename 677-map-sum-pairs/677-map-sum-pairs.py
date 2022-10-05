class MapSum:

    def __init__(self):
        self.dic = {}
        

    def insert(self, key: str, val: int) -> None:
        self.dic[key] = val

    def sum(self, prefix: str) -> int:
        sum = 0
        for i in self.dic.keys():
            if(prefix[0:] == i[0:len(prefix)]):
                sum += self.dic[i]
        
        return sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)