class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        length = len(digits)
        if(length == 0):
            return []
        
        dic = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        """       
        ans = []
        
        if(length == 1):
            value = dic[digits[0]]
            for i in value:
                ans.append(i)
    
        elif(length == 2):
            for f_val in dic[digits[0]]:
                for s_val in dic[digits[1]]:
                    ans.append((f_val+s_val))
                            
        elif(length == 3):
            for f_val in dic[digits[0]]:
                for s_val in dic[digits[1]]:
                    for t_val in dic[digits[2]]:
                        ans.append((f_val+s_val+t_val))
                            
        elif(length == 4):
            for f_val in dic[digits[0]]:
                for s_val in dic[digits[1]]:
                    for t_val in dic[digits[2]]:
                        for four_val in dic[digits[3]]:
                            ans.append((f_val+s_val+t_val+four_val))
                            
                            
        return ans
        """   
        ans = [""]
        for digit in digits:
            tmp = []
            for i in dic[digit]:
                for j in ans:
                    tmp.append(j+i)
            ans = tmp
        
        return ans