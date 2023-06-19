class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1]==1:
            return -1
        
        
        directions = [(0,1), (-1,0), (1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
        
        visited = set()
        
        queue = collections.deque([(0,0,0)])
        
        while queue:
            x, y, dist = queue.popleft()
            
            if x == n-1 and y == n-1:
                return dist+1
            
            for direction in directions:
                next_x, next_y, new_dist = direction[0] + x, direction[1] + y, dist+1
                
                if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n and grid[next_x][next_y] != 1 and (next_x,next_y) not in visited:
                    queue.append((next_x, next_y, new_dist))
                    visited.add((next_x, next_y))
        
        return -1
            