class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        digonals = defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                digonals[i-j].append(mat[i][j])
        
        for k in digonals.keys():
            digonals[k].sort()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = digonals[i-j].pop(0)
                
        return mat