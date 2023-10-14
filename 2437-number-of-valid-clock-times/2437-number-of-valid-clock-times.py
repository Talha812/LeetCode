class Solution:
    def countTime(self, time: str) -> int:
                
        splitted = time.split(":")
        
        hours = splitted[0]
        minutes = splitted[1]
        
        ans = 0
        if hours == "??":
            ans += (1*24)
        
        elif hours[1] == "?":
            if hours[0] == "1" or hours[0] == "0":
                ans += (1*10)
            elif hours[0] == "2":
                ans += (1*4)
        
        elif hours[0] == "?":
            if int(hours[1]) > 3:
                ans += (1*2)
            else:
                ans += (1*3)
        
        if minutes == "??":
            if ans == 0:
                ans += (1*60)
            else:
                ans *= (1*60)
        
        elif minutes[1] == "?":
            if ans == 0:
                ans += (1*10)
            else:
                ans *= (1*10)
        
        elif minutes[0] == "?":
            if ans == 0:
                ans += (1*6)
            else:
                ans *= (1*6)
        
        if ans == 0:
            ans = 1
            
        return ans
                