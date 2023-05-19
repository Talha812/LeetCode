class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 0
        for i in range(len(digits)-1,-1,-1):
            if i == len(digits)-1:
                digits[i] = digits[i] + carry + 1
            else:
                digits[i] = digits[i] + carry
                
            if digits[i] >= 10:
                carry = digits[i]//10
                digits[i] = digits[i]%10
            else:
                carry = 0
        
        if carry > 0:
            digits.insert(0, carry)
        
        return digits
            