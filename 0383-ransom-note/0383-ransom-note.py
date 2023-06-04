class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False
        
        dic1 = {}
                
        for ch in magazine:
            if ch in dic1:
                dic1[ch] += 1
            else:
                dic1[ch] = 1
            
        for ch in ransomNote:
            if ch in dic1 and dic1[ch] > 0:
                dic1[ch] -= 1
            
            else:
                return False
        
        return True