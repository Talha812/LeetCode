class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        
        power = 0
        
        ans = 0
        isNegative = False
        for d in range(len(s)-1, -1, -1):
            if d == 0:
                if s[d] == "-":
                    isNegative = True
                    break
                if s[d] == "+":
                    continue
                    
            if ans >= 0 and (s[d] == "." or s[d] == " " or s[d] == "+" or s[d] == "-" or (ord(s[d]) >= 65 and ord(s[d]) <= 90) or (ord(s[d]) >= 97 and ord(s[d]) <= 122)):
                ans = 0
                power = 0
                continue
                
                
            if int(s[d]) >= 0 and int(s[d]) <= 9:
                ans += (int(s[d])* (10**power))
                power += 1
        
        if ans > (2**31)-1 or ans < (-1*(2**31)):
            if isNegative:
                return (-1*(2**31))
            else:
                return (2**31)-1
        
        if isNegative:
            return -1*ans
        
        return ans