class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        vector<vector<int>> dp(grid.size(), vector<int>(grid[0].size(), 0));

        if(grid.size()==1 && grid[0].size() == 1)   return grid[0][0];

        int sum = 0;
        for(int i=0; i<grid[0].size(); i++){
            sum += grid[0][i];
            dp[0][i] = sum;
        }

        sum = 0;
        for(int i=0; i<grid.size(); i++){
            sum += grid[i][0];
            dp[i][0] = sum;
        }

        for(int i=1; i<grid.size(); i++){
            for(int j=1; j<grid[0].size(); j++){
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[grid.size()-1][grid[0].size()-1];
    }
};