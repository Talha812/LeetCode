class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        length = len(digits)
        if(length == 0):
            return []
        
        dic = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        ans = []
        
        if(length == 1):
            value = dic[digits[0]]
            for i in value:
                ans.append(i)
    
        elif(length == 2):
            for first in range(length-1):
                for sec in range(1,length):
                    for f_val in dic[digits[first]]:
                        for s_val in dic[digits[sec]]:
                            ans.append((f_val+s_val))
                            
        elif(length == 3):
            for first in range(length-2):
                for sec in range(1,length-1):
                    for third in range(2, length):
                        for f_val in dic[digits[first]]:
                            for s_val in dic[digits[sec]]:
                                for t_val in dic[digits[third]]:
                                    ans.append((f_val+s_val+t_val))
                            
        elif(length == 4):
            for first in range(length-3):
                for sec in range(1,length-2):
                    for third in range(2, length-1):
                        for fourth in range(3, length):
                            for f_val in dic[digits[first]]:
                                for s_val in dic[digits[sec]]:
                                    for t_val in dic[digits[third]]:
                                        for four_val in dic[digits[fourth]]:
                                            ans.append((f_val+s_val+t_val+four_val))
                            
                            
        return ans