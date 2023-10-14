class Solution:
    def countTime(self, time: str) -> int:
                
        splitted = time.split(":")
        
        hours = splitted[0]
        minutes = splitted[1]
        
        ans = 1
        if hours == "??":
            ans *= (24)
        
        elif hours[1] == "?":
            if hours[0] == "1" or hours[0] == "0":
                ans *= (10)
            elif hours[0] == "2":
                ans *= (4)
        
        elif hours[0] == "?":
            if int(hours[1]) > 3:
                ans *= (2)
            else:
                ans *= (3)
        
        if minutes == "??":
            if ans == 0:
                ans *= (60)
            else:
                ans *= (60)
        
        elif minutes[1] == "?":
            if ans == 0:
                ans *= (10)
            else:
                ans *= (10)
        
        elif minutes[0] == "?":
            if ans == 0:
                ans *= (6)
            else:
                ans *= (6)
                    
        return ans
                