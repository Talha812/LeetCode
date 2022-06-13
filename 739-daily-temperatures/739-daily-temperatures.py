class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = []
        
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackt, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
                
            stack.append([t, i])
            
        return res
#         ans = []
        
#         for i in range(len(temperatures)):
#             count = 0
#             found = False
#             for j in range(i+1, len(temperatures)):
#                 if(temperatures[j] > temperatures[i]):
#                     found = True
#                     count += 1
#                     break
#                 if(found == False):
#                     count += 1
#             if(found):        
#                 ans.append(count)
#             else:
#                 ans.append(0)
        
#         return ans