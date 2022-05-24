class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        
        return -1
        
        
#         dic = {}
        
#         for i in range(len(s)):
#             if(s[i] in dic):
#                 dic[s[i]] += 1
#             else:
#                 dic[s[i]] = 1
        
#         for i in range(len(s)):
#             if(dic[s[i]] == 1):
#                 return i
        
#         return -1