class Solution:
    def reformat(self, s: str) -> str:
        
        digits = 0
        str_digits = ""
        for i in s:
            if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
                digits += 1
                str_digits += i
       #print(str_digits)
        alphabets = 0
        str_alphabets = ""
        for i in s:
            if(ord(i) >= 97 and ord(i) <= 122):
                alphabets += 1
                str_alphabets += i
        
        #print(str_alphabets)
        
        possible = False
        
        if(digits-alphabets == 0 or digits-alphabets == -1 or digits-alphabets == 1):
            possible = True
        
        if possible:
            ans = ""
            if(digits-alphabets == 0 or digits-alphabets == 1):
                sInd = 0
                dInd = 0
                for i in range(len(s)):
                    if i%2 == 0:
                        ans += str_digits[dInd]
                        dInd += 1
                    else:
                        ans += str_alphabets[sInd]
                        sInd += 1
            
            else:
                sInd = 0
                dInd = 0
                for i in range(len(s)):
                    if i%2 == 0:
                        ans += str_alphabets[sInd]
                        sInd += 1
                    else:
                        ans += str_digits[dInd]
                        dInd += 1
                
            return ans
            
        return ""