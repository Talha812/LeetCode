class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        res = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                res += grid[i][j] * 6 - 2 * (grid[i][j] - 1)

                if i < n - 1:
                    res -= 2 * min(grid[i][j], grid[i + 1][j])

                if j < n - 1:
                    res -= 2 * min(grid[i][j], grid[i][j + 1])

        return res