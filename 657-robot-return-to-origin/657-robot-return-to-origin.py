class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        left = 0
        right = 0
        up = 0
        down = 0
        
        i = 0
        while(i<len(moves)):
            if(moves[i] == "U"):
                up += 1
            
            elif(moves[i] == "D"):
                down += 1
            
            elif(moves[i] == "L"):
                left += 1
            
            else:
                right += 1
            
            i += 1
        
        if(left == right and up == down):
            return True
        
        return False
        
#         UD = []
#         LR = []
        
#         for i in moves:
#             if i=='U' or i == 'D':
#                 if UD == []:
#                     UD.append(i)
#                 else:
#                     if UD[-1] == i:
#                         UD.append(i)
#                     else:
#                         UD.pop()
                        
#             elif i=='L' or i == 'R':
#                 if LR == []:
#                     LR.append(i)
#                 else:
#                     if LR[-1] == i:
#                         LR.append(i)
#                     else:
#                         LR.pop()
                        
#         return UD == LR