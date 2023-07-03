class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        vector<vector<int>> dir = {{1,0}, {-1,0}, {0,1}, {0, -1},{1, 1},{-1, -1}, {1, -1}, {-1, 1}};

        int m = board.size(), n = board[0].size();

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                int neigh = 0;
                for(auto d: dir){
                    int next_i = i + d[0], next_j = j + d[1];
                    if(next_i >= 0 && next_i < m && next_j >=0 && next_j < n && abs(board[next_i][next_j]) == 1)
                        neigh++;
                }
                if(abs(board[i][j]) == 1 && (neigh < 2 || neigh > 3))   board[i][j] = -1;
                if(board[i][j] == 0 && neigh == 3)  board[i][j] = 2;   
            }
        }

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(board[i][j] == -1)   board[i][j] = 0;
                if(board[i][j] == 2)    board[i][j] = 1; 
            }
        }
    }
};