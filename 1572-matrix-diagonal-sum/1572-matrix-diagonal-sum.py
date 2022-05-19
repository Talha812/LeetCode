class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

    
        Sum = 0
        
        col = len(mat)-1
        for i in range(len(mat)):
            Sum += mat[i][i]
            if(i != col):
                Sum += mat[i][col]
            col -= 1
        
        return Sum