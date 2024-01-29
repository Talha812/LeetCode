class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        pos = []
        for i in range(len(number)):
            if number[i] == digit:
                pos.append(i)
        
        temp = float("-inf")
        ans = ""
        for p in pos:
            s1 = number[ : p]
            s2 = number[p+1 : ]
            
            num = s1 + s2
            
            if int(num) > temp:
                ans = num
                temp = int(num)
        
        return ans