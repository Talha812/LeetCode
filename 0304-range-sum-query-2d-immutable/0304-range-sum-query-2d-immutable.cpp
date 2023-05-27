class NumMatrix {

    int rows, cols;
    vector<vector<int>> sums;

public:
    NumMatrix(vector<vector<int>>& matrix) {
        rows = matrix.size();

        cols = rows>0 ? matrix[0].size():0;

        sums.resize(rows+1, vector<int>(cols+1, 0));

        for(int i=1; i<=rows; i++){
            for(int j=1; j<=cols; j++){
                sums[i][j] = matrix[i-1][j-1] + sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1];
            }
        }
    }
    
    int sumRegion(int r1, int c1, int r2, int c2) {
        return sums[r2+1][c2+1] - sums[r1][c2+1] - sums[r2+1][c1] + sums[r1][c1];
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */