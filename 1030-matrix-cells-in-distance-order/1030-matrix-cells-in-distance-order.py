class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        
        ans = []
        for i in range(rows):
            for j in range(cols):
                ans.append([i, j])
                
        ans.sort(key = lambda c : abs(c[0]-rCenter) + abs(c[1]-cCenter))
        
        return ans