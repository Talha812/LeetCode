class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        res = ""
        
        dic = {}
        for i in range(numRows):
            dic[i] = ""
            
        flag = False
        ind = 0
        for i in range(len(s)):
            dic[ind] += s[i]
            if i%(numRows-1) == 0:
                flag = not flag
            
            if not flag:
                ind -= 1
            else:
                ind += 1
        
        for i in dic:
            res += dic[i]
            
        return res