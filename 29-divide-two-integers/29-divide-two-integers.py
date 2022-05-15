class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        recordDividend = dividend
        recordDivisor = divisor
        
        quotient = abs(dividend)//abs(divisor)
        
        if((recordDividend<0 and recordDivisor<0) or (recordDividend>=0 and recordDivisor>0)):
            quotient = quotient
        
        elif(recordDividend<0 or recordDivisor<0):
            quotient = -1*quotient
        
        if(quotient>(pow(2,31)-1)):
            return pow(2,31)-1
        elif(quotient<(-1*pow(2,31))):
            return -1*pow(2,31)

        return quotient