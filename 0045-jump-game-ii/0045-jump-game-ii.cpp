class Solution {
public:
    int jump(vector<int>& nums) {
        queue<int> q;
        int steps = 0;

        vector<bool> visited(nums.size(), false);

        q.push(0);
        visited[0] = true;

        while(!q.empty()){
            int size = q.size();

            for(int i=0; i<size; i++){
                int cur = q.front();
                q.pop();

                if(cur == nums.size()-1)    return steps;

                int maxJump = nums[cur];
                for(int j=1; j<=maxJump; j++){
                    if(cur+j <nums.size()){
                     if(visited[cur+j] == false) 
                        q.push(cur+j);
                        visited[cur+j] = true;
                    }
                    else break;
                }
            }
            steps++;
        }
        return 0;
    }
};