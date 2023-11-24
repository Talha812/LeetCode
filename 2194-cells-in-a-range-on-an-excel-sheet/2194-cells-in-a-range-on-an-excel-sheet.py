class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        c1 = ord(s[0])
        r1 = int(s[1])
        
        c2 = ord(s[3])
        r2 = int(s[4])
        
        ans = []
        for y in range(c1, c2+1):
            
            for x in range(r1, r2+1):
                
                ans.append(chr(y) + str(x))
        
        return ans
                
        
        