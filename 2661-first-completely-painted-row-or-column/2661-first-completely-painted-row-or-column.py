class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        summary = {}
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                summary[mat[i][j]] = (i, j)
        
        
        rowFilled = [0] * len(mat)
        colFilled = [0] * len(mat[0])
        
        for i in range(len(arr)):
            
            r, c = summary[arr[i]]
            
            rowFilled[r] += 1
            colFilled[c] += 1
            
            if rowFilled[r] == len(mat[0]) or colFilled[c] == len(mat):
                return i
