class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        
        if len(password) < 8:
            return False
        
        containLower, containUpper, containDigit, containSpecialCh, adjDifferent = False, False, False, False, True
        
        special_char = "!@#$%^&*()-+"
        
        for i in range(len(password)):
            if i != 0 and password[i] == password[i-1]: 
                adjDifferent = False
                break
            
            if not containLower: 
                containLower = password[i].islower()
                
            if not containUpper:
                containUpper = password[i].isupper()
                
            if not containDigit:
                containDigit = password[i].isdigit()
                
            if not containSpecialCh:
                containSpecialCh = password[i] in special_char
        return containLower and containUpper and containDigit and containSpecialCh and adjDifferent