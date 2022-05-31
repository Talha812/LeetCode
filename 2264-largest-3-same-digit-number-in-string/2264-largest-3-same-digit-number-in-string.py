class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        
        maximum = "-1"
        for i in range(len(num)):
            if(i >= len(num)-2):
                if(maximum == "-1"):
                    return ""
                return maximum
                
            if(num[i] == num[i+1] == num[i+2]):
                maximum = max(maximum,(num[i]+num[i+1]+num[i+2]))
        
        