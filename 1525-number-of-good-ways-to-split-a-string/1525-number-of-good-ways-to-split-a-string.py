class Solution:
    def numSplits(self, s: str) -> int:
        
        dic1 = {}
        
        for ch in s:
            if ch in dic1:
                dic1[ch] += 1
            else:
                dic1[ch] = 1
        
        count = 0
        dic2 = {}
        for ch in s:
            if ch not in dic2:
                dic2[ch] = 1
            else:
                dic2[ch] += 1

            dic1[ch] -= 1
            
            if dic1[ch] == 0:
                dic1.pop(ch)
            
            if len(dic1) == len(dic2):
                count += 1
        
        return count