class Solution:
    def maxDepth(self, s: str) -> int:
        
        ans = 0
        counter = 0
        
        for ch in s:
            if ch == "(":
                counter += 1
                ans = max(ans, counter)
            elif ch == ")":
                counter -= 1
            
        return ans