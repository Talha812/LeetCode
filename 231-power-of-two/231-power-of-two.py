class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        num = 1
        power = 0
        while(num <= n):
            num = 2**power
            power += 1
            if(num == n):
                return True
        
        return False