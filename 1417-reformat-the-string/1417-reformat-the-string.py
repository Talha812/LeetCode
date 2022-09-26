class Solution:
    def reformat(self, s: str) -> str:
        
        characters = ""
        digits = ""
        
        for i in s:
            if i.isdigit():
                digits += i
            else:
                characters += i
        
        digits_count = len(digits)
        char_count = len(characters)
        
        if((char_count-digits_count > 1) or (char_count-digits_count < -1)):
            return ""
        
        ans = ""
        sInd = 0
        dInd = 0
        if(digits_count-char_count == 0 or digits_count-char_count == 1):
            for i in range(len(s)):
                if i%2 == 0:
                    ans += digits[dInd]
                    dInd += 1
                else:
                    ans += characters[sInd]
                    sInd += 1
            
        else:
            for i in range(len(s)):
                if i%2 == 0:
                    ans += characters[sInd]
                    sInd += 1
                else:
                    ans += digits[dInd]
                    dInd += 1
                
        return ans