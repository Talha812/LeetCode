class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        p = 1
        dirc_forward = True
        
        while time > 0:
            if dirc_forward:
                p += 1
                if p == n:
                    dirc_forward = False
            else:
                p -= 1
                if p == 1:
                    dirc_forward = True
                    
            time -= 1
        
        return p
            