class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        dic1 = {}
        dic2 = {}
        
        for i in range(len(ransomNote)):
            if(ransomNote[i] in dic1):
                dic1[ransomNote[i]] += 1
            else:
                dic1[ransomNote[i]] = 1
        
        for i in range(len(magazine)):
            if(magazine[i] in dic2):
                dic2[magazine[i]] += 1
            else:
                dic2[magazine[i]] = 1
        
        for i in dic1.keys():
            if(dic2.get(i) != None and dic2.get(i) >= dic1.get(i)):
                continue
            elif(dic2.get(i) == None or dic2.get(i) != dic1.get(i)):
                return False
            
        return True
                