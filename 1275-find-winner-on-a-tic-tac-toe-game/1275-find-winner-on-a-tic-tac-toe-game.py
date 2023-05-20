class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        grid = [["","",""],["","",""],["","",""]]
        
        def checkRow(grid, turn):
            if turn%2 == 0:
                player = "X"
            else:
                player = "O"
                
            if (grid[0][0] == player and grid[0][1] == player and grid[0][2] == player) or (grid[1][0] == player and grid[1][1] == player and grid[1][2] == player) or (grid[2][0] == player and grid[2][1] == player and grid[2][2] == player):
                if player == "X":
                    return "A"
                else:
                    return "B"
            
            return ""
        
        def checkColumn(grid, turn):
            if turn%2 == 0:
                player = "X"
            else:
                player = "O"
                
            if (grid[0][0] == player and grid[1][0] == player and grid[2][0] == player) or (grid[0][1] == player and grid[1][1] == player and grid[2][1] == player) or (grid[0][2] == player and grid[1][2] == player and grid[2][2] == player):
                if player == "X":
                    return "A"
                else:
                    return "B"
                
            return ""
        
        def checkDiagonal(grid, turn):                
            if (grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X") or (grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X"):
                return "A"
            
            if (grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O") or (grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O"):
                return "B"
        
            return ""
        
        def checkWinner(grid, turn):
            if checkRow(grid, turn) or checkColumn(grid, turn) or checkDiagonal(grid, turn):
                return (checkRow(grid, turn) + checkColumn(grid, turn) + checkDiagonal(grid, turn))[0]
        
            return "Pending"
        
        turn = 0
        for move in moves:
            if turn%2 == 0:
                grid[move[0]][move[1]] = "X"
            else:
                grid[move[0]][move[1]] = "O"
            output = checkWinner(grid, turn)
            if output != "Pending":
                return output
            
            turn += 1

            
        if len(moves) == 9:
            return "Draw"
        
        return "Pending"