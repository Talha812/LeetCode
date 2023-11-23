class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
        queue<pair<int, int>> q;
        vector<int> res;

        q.push({0, 0});

        while(!q.empty()){
            int size = q.size();

            for(int i=0; i<size; i++){
                auto cur = q.front();
                q.pop();
                res.push_back(nums[cur.first][cur.second]);

                if(cur.first+1 < nums.size() && cur.second < nums[cur.first+1].size() && cur.second == 0){
                    q.push({cur.first+1, cur.second});
                }
                if(cur.second+1 < nums[cur.first].size()){
                    q.push({cur.first, cur.second+1});
                }
            }
        }
        return res;
    }
};