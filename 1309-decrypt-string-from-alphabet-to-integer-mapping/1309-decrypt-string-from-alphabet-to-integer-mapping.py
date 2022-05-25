class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        dic = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j", 11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s", 20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}
        
        if(len(s) == 1):
            return dic[s[0]]
        if(len(s) == 2):
            return (dic[s[0]]+dic[s[1]])
        
        ans = ""
        
        i = 0
        while(i < (len(s)-2)):
            if(s[i+2] != "#"):
                ans = ans + dic[int(s[i])]
                i += 1
            
            else:
                ans = ans + dic[int(s[i:i+2])] #dic[int(s[i]+s[i+1])]
                i += 3
    
        for r in range(i, len(s)):
            ans = ans + dic[int(s[r])]
            
            
        return ans
        
        
        
#         ans = ""
#         ind = len(s)-1
#         for i in range(len(s)-1, -1, -1):
#             if(s[ind] == "#"):
#                 num = s[ind-2] + s[ind-1]
#                 ans = dic[int(num)] + ans
#                 #print(ans)
#                 ind = ind - 3
#             else:
#                 ans = dic[int(s[ind])] + ans
#                 ind -= 1
#                # print(ans)
                
#             if(ind < 0):
#                 break
        
#         return ans
                