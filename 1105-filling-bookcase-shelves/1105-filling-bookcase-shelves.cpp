// class Solution {
// public:
//     int minHeightShelves(vector<vector<int>>& books, int shelfWidth) {
//         return helper(books, 0, shelfWidth);
//     }

//     int helper(vector<vector<int>>&books, int cur_i, int shelfWidth){
//         if(cur_i >= books.size())       return 0;

//         int i = cur_i, maxHeight = 0, usedWidth = 0;
//         int ret = INT_MAX;

//         while(i<books.size() && (usedWidth + books[i][0] <= shelfWidth)){
//             usedWidth += books[i][0];
//             maxHeight = max(maxHeight, books[i][1]);
//             ret = min(maxHeight + helper(books, i+1, shelfWidth), ret);
//             i++;
//         }
//         return ret;
//     }
// };


class Solution {
public:
    int minHeightShelves(vector<vector<int>>& books, int shelfWidth) {
        vector<int> dp(books.size()+1, -1);
        return helper(books, 0, shelfWidth, dp);
    }

    int helper(vector<vector<int>>&books, int cur_i, int shelfWidth, vector<int>&dp){
        if(cur_i >= books.size())       return 0;

        if(dp[cur_i] != -1) return dp[cur_i];

        int i = cur_i, maxHeight = 0, usedWidth = 0;
        int ret = INT_MAX;

        while(i<books.size() && (usedWidth + books[i][0] <= shelfWidth)){
            usedWidth += books[i][0];
            maxHeight = max(maxHeight, books[i][1]);
            ret = min(maxHeight + helper(books, i+1, shelfWidth, dp), ret);
            i++;
        }
        return dp[cur_i] = ret;
    }
};