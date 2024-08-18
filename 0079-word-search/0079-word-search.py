class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(board, word, i, j):
            if len(word) == 0: 
                return True
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0] or board[i][j]==-1: 
                return False
            
            rec_char = board[i][j]
            board[i][j] = -1
            word = word[1:]
            
            left = dfs(board, word, i, j-1)
            right = dfs(board, word, i, j+1)
            up = dfs(board, word, i-1, j)
            down = dfs(board, word, i+1, j)
            
            board[i][j] = rec_char
            return up or down or left or right
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (board[r][c] == word[0]) and dfs(board, word, r,c):
                    return True
                
        return False