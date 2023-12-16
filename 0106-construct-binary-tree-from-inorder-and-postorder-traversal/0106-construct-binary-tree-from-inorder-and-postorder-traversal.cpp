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
    int i;
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        i = postorder.size()-1;
        return helper(inorder, postorder, 0, inorder.size()-1);
    }

    TreeNode* helper(vector<int>& inorder, vector<int>& postorder, int start, int end){
        if(i<0 || (start > end))    return nullptr;

        int val = postorder[i];
        i--;

        TreeNode* node = new TreeNode(val);

        int idx;
        for(int j=0; j<inorder.size(); j++){
            if(inorder[j] == val){
                idx = j;
                break;
            }
        }
        node->right = helper(inorder, postorder, idx+1, end);
        node->left = helper(inorder, postorder, start, idx-1);
        
        return node;
    }
};