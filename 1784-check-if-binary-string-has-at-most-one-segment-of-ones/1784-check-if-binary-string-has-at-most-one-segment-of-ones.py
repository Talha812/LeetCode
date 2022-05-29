class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        seg = True
        
        for i in s:
            if(not seg and i == "1"):
                return False
            elif(i=="0" and seg):
                seg = False
        
        return True
        
        
        