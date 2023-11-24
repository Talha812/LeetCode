class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        ans = ""
        
        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber%26
            char = chr(ord("A") + (rem))
            ans = char + ans
            columnNumber //= 26
        
        return ans