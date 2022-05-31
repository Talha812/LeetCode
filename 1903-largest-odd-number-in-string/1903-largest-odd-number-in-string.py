class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        int_num = int(num)
        while(int_num > 0):
            if(int_num%2 != 0):
                return str(int_num)
            else:
                int_num //= 10
                #num = num[0:len(num)-1]
        
        return ""