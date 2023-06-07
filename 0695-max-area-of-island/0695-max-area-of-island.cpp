class Solution {
public:
    int maxArea = 0;
    vector<vector<int>> directions = {{-1,0}, {0,1}, {1,0}, {0,-1}};
    
    void helper(vector<vector<int>> &grid, int i, int j, int &area){
        if(i<0 || i >= grid.size() || j < 0 || j >= grid[0].size() || grid[i][j] == 0){
            return;
        }
        
        grid[i][j] = 0;
        area += 1;
        maxArea = max(maxArea, area);
        
        for(auto direction : directions){
            int newRow = i + direction[0];
            int newCol = j + direction[1];
            helper(grid, newRow, newCol, area);
        }
        
    }
    
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        for(int i=0; i<grid.size(); i++){
            for(int j=0; j< grid[0].size(); j++){
                if(grid[i][j] == 1){
                    int area = 0;
                    helper(grid, i, j, area);
                }
            }
        }
        
        return maxArea;
    }
};