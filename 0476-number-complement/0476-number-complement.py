class Solution:
    def findComplement(self, num: int) -> int:
        
        binn = ""
            
        while(num>0):
            rem = num%2
            binn = str(rem) + binn
            num = num//2
        
        inv = ""
        for d in binn:
            if(d == "0"):                
                inv += "1"
            else:
                inv += "0"
        
        ans = 0
        power = 0
        
        for i in range(len(inv)-1,-1,-1):
            ans += int(inv[i]) * (2**power)
            power += 1
            
        return ans