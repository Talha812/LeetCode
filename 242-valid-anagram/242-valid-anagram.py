class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False
        
        dic1 = {}
        for i in range(len(s)):
            if s[i] in dic1:
                dic1[s[i]] += 1
            else:
                dic1[s[i]] = 1
        
        dic2 = {}
        for i in range(len(t)):
            if t[i] in dic2:
                dic2[t[i]] += 1
            else:
                dic2[t[i]] = 1
        
        
        for i in dic2.keys():
            if(dic2.get(i) != None and dic1.get(i)!=None and dic2[i] != dic1[i]):
                return False
            elif(dic2.get(i) != None and dic1.get(i) == None):
                return False
            elif(dic2.get(i) == None and dic1.get(i) != None):
                return False
        
        return True
            