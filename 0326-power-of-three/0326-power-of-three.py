class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
                
        p = 0
        num = 1
        while num <= n:
            num = (3**p)
            if num == n:
                return True
        
            p += 1
        
        return False