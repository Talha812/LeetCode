class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        data = []
        dp = [[[ -1 for k in range(n + 1)] for j in range(m + 1)] for i in range(len(strs) + 1)]

        for string in strs:
            cnt_0 = string.count("0")
            cnt_1 = string.count("1")
            
            data.append((cnt_0, cnt_1))
            
        def helper(data, m, n , ind, dp):
            if ind >= len(data) or m < 0 or n < 0:
                return 0
            
            if dp[ind][m][n] != -1:
                return dp[ind][m][n]
            
            consider = 0
            if (m-data[ind][0] >= 0 and n-data[ind][1] >= 0):
                consider = 1 + helper(data, m-data[ind][0], n-data[ind][1], ind+1, dp)
            
            notConsider = helper(data, m , n, ind+1, dp)
            
            dp[ind][m][n] = max(consider, notConsider)
            
            return dp[ind][m][n]
        
        return helper(data, m, n, 0, dp)