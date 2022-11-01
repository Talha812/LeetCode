class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xffffffff
        while(b & mask):
            c = a&b
            a = a^b
            b = c<<1
    
        if (b > 0):
            return a & mask
        
        return a
    
        #return (a & mask) if b > 0 else a