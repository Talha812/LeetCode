// 2420. Find All Good Indices

class Solution {
public:
    vector<int> goodIndices(vector<int>& nums, int k) {
        vector<int> leftHist(nums.size(), 1);
        vector<int> rightHist(nums.size(), 1);

        int prev = 0, count = 1;

        for(int i=2; i<nums.size(); i++){
            count = nums[i-1] <= nums[i-2] ? count+1:1;
            leftHist[i] = count;
        }

        count = 1;
        for(int i = nums.size()-3; i>= 0; i--){
            count = nums[i+1] <= nums[i+2] ? count+1:1;
            rightHist[i] = count;
        }

        leftHist[0] = 0;
        rightHist[nums.size()-1] = 0;

        vector<int> res;
        for(int i= 0; i<nums.size(); i++){
            if(leftHist[i] >= k && rightHist[i] >= k)   res.push_back(i);
        }

        return res;
    }
};