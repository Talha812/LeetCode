class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if(r*c != len(mat[0])*len(mat)):
            return mat
        
        ans = []
        matCol = 0
        matRow = 0
        for row in range(r):
            temp = []
            for col in range(c):
                if(matCol < len(mat[0])):
                    temp.append(mat[matRow][matCol])
                    matCol += 1
                    
                else:
                    matCol = 0
                    matRow += 1
                    temp.append(mat[matRow][matCol])
                    matCol += 1
                    
                    
            
            ans.append(temp)
            
        return ans