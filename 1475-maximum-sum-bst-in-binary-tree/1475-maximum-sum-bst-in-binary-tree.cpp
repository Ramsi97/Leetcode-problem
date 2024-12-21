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
    int sum_ = 0;
    long long Lmax = INT_MIN;
    long long Rmin = INT_MAX;

    vector<int> postorder(TreeNode* root)
    {
        if(!root)
        {
            return {0, INT_MAX, INT_MIN};
        }

        vector<int> leftResult = postorder(root->left);
        vector<int> rightResult = postorder(root->right);

        if (leftResult[2] < root->val && root->val < rightResult[1]){
            int cur = leftResult[0] + rightResult[0] +root->val;
            sum_ = max(sum_,cur);
            return {cur ,min(root->val,leftResult[1]),max(root->val,rightResult[2])};

        }
        else{
            return {0, INT_MIN, INT_MAX};
        }
     return {0,0,0};
        
        
    }
    int maxSumBST(TreeNode* root) {
        vector<int> res = postorder(root);
        return sum_;
    }
};