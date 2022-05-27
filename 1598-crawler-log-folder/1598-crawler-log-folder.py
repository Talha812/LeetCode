class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        ans = 0
        
        for i in logs:
            if i == "../" and ans != 0:
                ans -= 1
                
            elif i == "./" or i == "../":
                continue
                
            else:
                ans += 1
        
        return ans