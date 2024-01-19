class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        # Find R
        position = []
        for i in range(len(board)):
            flag = False
            for j in range(len(board)):
                if board[i][j] == "R":
                    position = [i, j]
                    flag = True
                    break
            
            if flag:
                break
                
        count = 0
        # Up 
        i = position[0]
        j = position[1]
        while i >= 0:
            if board[i][j] == "B":
                break
            elif board[i][j] == "p":
                count += 1
                break
            
            i -= 1
            
        # Down 
        i = position[0]
        j = position[1]
        while i < len(board):
            if board[i][j] == "B":
                break
            elif board[i][j] == "p":
                count += 1
                break
            
            i += 1
        
        # Right 
        i = position[0]
        j = position[1]
        while  j < len(board):
            if board[i][j] == "B":
                break
            elif board[i][j] == "p":
                count += 1
                break
            
            j += 1
        
        # Left
        i = position[0]
        j = position[1]
        while  j >= 0:
            if board[i][j] == "B":
                break
            elif board[i][j] == "p":
                count += 1
                break
            
            j -= 1
            
        return count
            