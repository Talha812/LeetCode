class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        count = 0
        move = 0
        
        for i in s:
            if i == "(":
                count += 1
            else:
                count -= 1
            
            if count < 0:
                move += 1
                count = 0

        return (move + count)