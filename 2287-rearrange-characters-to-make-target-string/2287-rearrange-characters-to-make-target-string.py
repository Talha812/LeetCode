class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        
        dic = {}
        passed_chars = []
        for char in target:
            for ch in s:
                if char == ch and ch not in passed_chars:
                    if ch in dic:
                        dic[ch] += 1
                    else:
                        dic[ch] = 1
            passed_chars.append(char)        
                
        
        copy = 0
        firstTime = 1
        for i in target:
            if(dic.get(i) == None):
                return 0
            
            elif (dic.get(i) != None and floor(dic[i]/target.count(i)) < copy) or firstTime == 1:
                copy = floor(dic[i]/target.count(i))
                firstTime += 1
            
        
        return copy