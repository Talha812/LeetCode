class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        
        UD = []
        LR = []
        
        for i in moves:
            if i=='U' or i == 'D':
                if UD == []:
                    UD.append(i)
                else:
                    if UD[-1] == i:
                        UD.append(i)
                    else:
                        UD.pop()
                        
            elif i=='L' or i == 'R':
                if LR == []:
                    LR.append(i)
                else:
                    if LR[-1] == i:
                        LR.append(i)
                    else:
                        LR.pop()
                        
        return UD == LR