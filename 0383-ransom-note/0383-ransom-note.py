class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        dic1 = {}
        dic2 = {}
        
        for i in ransomNote:
            if i not in dic1:
                dic1[i] = 1
            else:
                dic1[i] += 1
        
        for i in magazine:
            if i not in dic2:
                dic2[i] = 1
            else:
                dic2[i] += 1
        
        
        for k in dic1:
            if k not in dic2 or dic1[k] > dic2[k]:
                return False
        
        return True