class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        grid = [["","",""],["","",""],["","",""]]
        
        def checkWinner(grid):
            if (grid[0][0] == "X" and grid[0][1] == "X" and grid[0][2] == "X") or (grid[1][0] == "X" and grid[1][1] == "X" and grid[1][2] == "X") or (grid[2][0] == "X" and grid[2][1] == "X" and grid[2][2] == "X") or (grid[0][0] == "X" and grid[1][0] == "X" and grid[2][0] == "X") or (grid[0][1] == "X" and grid[1][1] == "X" and grid[2][1] == "X") or (grid[0][2] == "X" and grid[1][2] == "X" and grid[2][2] == "X") or (grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X") or (grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X"):
                return "A"
            
            if (grid[0][0] == "O" and grid[0][1] == "O" and grid[0][2] == "O") or (grid[1][0] == "O" and grid[1][1] == "O" and grid[1][2] == "O") or (grid[2][0] == "O" and grid[2][1] == "O" and grid[2][2] == "O") or (grid[0][0] == "O" and grid[1][0] == "O" and grid[2][0] == "O") or (grid[0][1] == "O" and grid[1][1] == "O" and grid[2][1] == "O") or (grid[0][2] == "O" and grid[1][2] == "O" and grid[2][2] == "O") or (grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O") or (grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O"):
                return "B"
        
            return "Pending"
        
        turn = 0
        for move in moves:
            if turn%2 == 0:
                grid[move[0]][move[1]] = "X"
            
            else:
                grid[move[0]][move[1]] = "O"            
            
            output = checkWinner(grid)
            if output != "Pending":
                return output
                    
            turn += 1
        
        if len(moves) == 9:
            return "Draw"
        
        return "Pending"