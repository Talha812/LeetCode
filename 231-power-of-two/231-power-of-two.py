class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if(n==0):
            return False
        
        while(n!=1):
            if(n%2 != 0):
                return False
            n = n//2
        
        return True
    
    
#         num = 1
#         power = 0
#         while(num <= n):
#             num = 2**power
#             power += 1
#             if(num == n):
#                 return True
        
#         return False