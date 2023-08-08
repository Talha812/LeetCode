class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        def calculate(n):
            if n == 1:
                return ["0", "1"]
            
            ans = []
            temp = calculate(n-1)
            
            for i in range(len(temp)):
                ans.append("0"+temp[i])
            
            for i in range(len(temp)-1, -1, -1):
                ans.append("1"+temp[i])
            
            return ans
        
        def convertDecimal(n):
            output = 0
            power = 0
            for i in range(len(n)-1, -1, -1):
                output += (int(n[i])*pow(2, power))
                power += 1
            
            return output
        
        grayStrings = calculate(n)
        ans = []
        
        for grayStr in grayStrings:
            ans.append(convertDecimal(grayStr))
        
        return ans