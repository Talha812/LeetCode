class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            min_val = float('inf')
            j = 1
            while j * j <= i:
                min_val = min(min_val, dp[i - j * j] + 1)
                j += 1
            dp[i] = min_val
        return dp[n]

    
#         if n <= 3:
#             return n
        
#         rec = [float("inf")] * (n + 1)
#         rec[0] = 0
#         for i in range(1, n+1):
            
#             smaller = float("inf")
#             for num in range(1, n//2):
#                 if num * num <= i:
#                     smaller = min(smaller, rec[i-num*num]+1)
#                 else:
#                     break
            
#             rec[i] = smaller
            
#         return rec[n]
    
