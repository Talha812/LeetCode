class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def checkValid(row, col, board):
            # Primary Diagonal
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                
                i -= 1
                j -= 1
                
            # Sec Diagonal
            i, j = row, col
            while i < len(board) and j >= 0:
                if board[i][j] == "Q":
                    return False
                
                i += 1
                j -= 1
                
            # Col Check
            i = row
            j = col
            while j >= 0:
                if board[i][j] == "Q":
                    return False
                
                j -= 1
                
            return True
            
            
        grid = ["."*n for i in range(n)]
        ans = []
        def backtrack(col, grid):
            
            if col == n:
                ans.append(grid[:])
                return
            
            for i in range(n):
                if checkValid(i, col, grid):
                    grid[i] = grid[i][0:col] + "Q" + grid[i][col+1:]
                    backtrack(col+1, grid)
                    grid[i] = grid[i][0:col] + "." + grid[i][col+1:]
        
        backtrack(0, grid)
        return ans