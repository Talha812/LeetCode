class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        cost_consume = 0
        max_length = 0
        
        left = 0
        right = 0
        
        while (right < len(s)):
            
            diff = abs(ord(s[right]) - ord(t[right]))
            cost_consume += diff
            
            while cost_consume > maxCost:
                cost_consume -= abs(ord(s[left])- ord(t[left]))
                left += 1
                
            
            max_length = max(max_length, right-left+1)
            
            right += 1
        
        return max_length