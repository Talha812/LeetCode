class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        n = len(matrix)
        
        for i in range(n):
            s = set()
            count = 0
            for j in range(n):
                if(matrix[i][j] >= 1 and matrix[i][j] <= n):
                    s.add(matrix[i][j])
                    count += 1
            if(count != len(s)):
                return False
        
        for i in range(n):
            s = set()
            count = 0
            for j in range(n):
                if(matrix[j][i] >= 1 and matrix[j][i] <= n):
                    s.add(matrix[j][i])
                    count += 1
            if(count != len(s)):
                return False
            
        return True