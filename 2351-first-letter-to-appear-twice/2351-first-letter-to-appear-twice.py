class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        sett = set()
        
        for ch in s:
            if ch in sett:
                return ch
            
            sett.add(ch)
        
        