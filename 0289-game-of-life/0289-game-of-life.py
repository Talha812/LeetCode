class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                neigh_cnt = 0
                for dirs in directions:
                    next_i = i + dirs[0] 
                    next_j = j + dirs[1]
                    if next_i >= 0 and next_i < m and next_j >= 0 and next_j < n:
                        if abs(board[next_i][next_j]) == 1:
                            neigh_cnt += 1
                
                if (neigh_cnt < 2 or neigh_cnt > 3) and abs(board[i][j]) == 1:
                    board[i][j] = -1
                
                if neigh_cnt == 3 and board[i][j] == 0:
                    board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1