class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1 = sorted(s1)
        k = len(s1)
        for i in range(len(s2) - k + 1):
            win_substr = s2[i : i+k]
            if sorted(win_substr) == s1:
                return True
        
        return False