class Solution:
    def numDecodings(self, s: str) -> int:    
        
        memo = {}
        
        def decodeWays(index, s, memo):
            if index == len(s):
                return 1
            
            if index in memo:
                return memo[index]
            
            if s[index] == "0":
                return 0
            
            count = decodeWays(index+1, s, memo)
            
            if index < len(s)-1 and (s[index] == "1" or (s[index] == "2" and s[index+1] <= "6")):
                count += decodeWays(index+2, s, memo)
            
            memo[index] = count
            
            return memo[index]
        
        return decodeWays(0, s, memo)