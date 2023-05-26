class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        rowMax = []
        colMax = []
        
        for row in grid:
            rowMax.append(max(row))
        
        for i in range(len(grid)):
            max_n = -1
            for j in range(len(grid)):
                max_n = max(grid[j][i], max_n)
            colMax.append(max_n)
            
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                ans += min(rowMax[i], colMax[j]) - grid[i][j]
        
        return ans