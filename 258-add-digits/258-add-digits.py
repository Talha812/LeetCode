class Solution:
    def addDigits(self, num: int) -> int:
        ans = num
        while(ans>=10):
            summ = 0
            while(num>0):
                summ += num%10
                num = num//10
                
            ans = summ
            num = summ
        
        return ans