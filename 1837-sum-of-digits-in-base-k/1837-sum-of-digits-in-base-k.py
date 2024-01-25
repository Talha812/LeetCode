class Solution:
    def sumBase(self, n: int, k: int) -> int:
        
        # base_output = ""
        ans = 0
        while n > 0:
            rem = n%k
            # base_output = str(rem) + base_output
            ans += rem
            n = n//k
        
        return ans
    
#         ans = 0
#         for digit in base_output:
#             ans += int(digit)
            
#         return ans