/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int findMax(vector<int> &nums, int l, int r){
        int maxVal = -1, maxInd = l;
        int i = l;
        while(i<=r){
            if(maxVal < nums[i]){
                maxVal = nums[i];
                maxInd = i;
            }
            i++;
        }
        return maxInd;
    }
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        return helper(nums, 0, nums.size()-1);
    }
    TreeNode * helper(vector<int> &nums, int l, int r){
        if(l>r) return nullptr;
        
        int maxInd = findMax(nums, l, r);

        TreeNode * root = new TreeNode(nums[maxInd]);
        root->left = helper(nums, l, maxInd - 1);
        root->right = helper(nums, maxInd + 1, r);
        return root;
    }
};