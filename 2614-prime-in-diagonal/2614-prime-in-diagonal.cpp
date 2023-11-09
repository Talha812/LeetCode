class Solution {
public:
    bool check(int a){
        if(a<=1)return false;
        for(int i = 2; i <= sqrt(a); i++){
            if(a%i==0)return false;
        }
        return true;
    }
    int diagonalPrime(vector<vector<int>>& nums) {
        int ans = 0,i,n=nums.size();
        for(i = 0; i < n; i++){
            if(check(nums[i][i])){//CHECK NUMS[I][I] IS PRIME OR NOT
                ans = max(ans,nums[i][i]);
            }
            if(check(nums[i][n-1-i])){//CHECK NUMS[I][N-1-I] IS PRIME OR NOT
                ans = max(ans,nums[i][n-1-i]);
            }
        }
        return ans;
    }
};
