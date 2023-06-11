class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        ind = 0
        
        ans = ""
        for i in range(len(s)):
            if ind < len(spaces) and i == spaces[ind]:
                ans += " "
                ind += 1
                ans += s[i]
            else:
                ans += s[i]
        
        return ans
                