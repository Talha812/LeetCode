class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        fresh_oranges = 0
        
        queue = collections.deque()
        
        m = len(grid)       # Rows
        n = len(grid[0])    # Columns
        
        # Record rotten and fresh orange (count)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif(grid[i][j] != 0):
                    fresh_oranges += 1
        
        queue.append((-1,-1))
        
        minute = -1
        
        while queue:
            
            curr_x, curr_y = queue.popleft()
            
            if curr_x == -1:
                minute += 1
                
                if queue:
                    queue.append((-1, -1))
            
            for direction in directions:
                new_x, new_y = curr_x+direction[0], curr_y+direction[1]
                
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                    continue
                
                if grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 2
                    fresh_oranges -= 1
                    queue.append((new_x, new_y))
                    
        if fresh_oranges == 0:
            return minute
        return -1