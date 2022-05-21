class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        peri = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == 1):
                    if(row == 0):   #check top
                        peri += 1
                    else:
                        if(grid[row-1][col] == 0):
                            peri += 1
                            
                    if(col == 0):   #check left
                        peri += 1
                    else:
                        if(grid[row][col-1] == 0):
                            peri += 1
                    
                    if(col == len(grid[0])-1):  #check Right
                        peri += 1
                    else:
                        if(grid[row][col+1] == 0):
                            peri += 1
                            
                    if(row == len(grid)-1):     #check Bottom
                        peri += 1
                    else:
                        if(grid[row+1][col] == 0):
                            peri += 1
                            
        return peri
                    