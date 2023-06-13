class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        ans = [-1]*len(grid[0])
        
        col = len(grid[0])
        row = len(grid)
        
        q = collections.deque([])
        for j in range(col):
            ball = j
            q.append((ball,0,j))

        while q:
            ball, r, c = q.popleft()
            if r == len(grid):
                ans[ball] = c            
                                
            elif c+1 < len(grid[0]) and grid[r][c] == 1 and grid[r][c+1] == 1:
                q.append((ball, r+1,c+1))
                    
            elif c-1 >= 0 and grid[r][c] == -1 and grid[r][c-1] == -1:
                q.append((ball, r+1, c-1))
        
            
                
        return ans
            
            
                    
                    
            
            