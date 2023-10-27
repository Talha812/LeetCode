class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        sett = set()
        ans = 0
        for ch in s:
            if ch not in sett:
                sett.add(ch)
            else:
                ans += 2
                sett.remove(ch)
        
        if len(sett) > 0:
            return ans + 1
        
        return ans