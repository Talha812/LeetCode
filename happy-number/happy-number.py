class Solution:
    def isHappy(self, n: int) -> bool:
        
        ans = n
        stack = []
        while(ans > 1):
            summ = 0
            while(n>0):
                summ += pow(n%10, 2)
                n = n//10
            
            ans = summ
            n = summ
            if(summ in stack):
                return False
            else:
                stack.append(summ)
                
            if(ans == 1):
                return True
        
        return True