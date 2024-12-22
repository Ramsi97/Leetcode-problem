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
    void inorderTraversal(TreeNode* root, vector<int>& result)
    {
        if(!root)
        {
            return;
        }
        inorderTraversal(root->left, result);

        result.push_back(root->val);

        inorderTraversal(root->right, result);      
    }
    bool isValidBST(TreeNode* root) {
        vector<int> result;
        inorderTraversal(root, result);

        vector<int> check = result;
        sort(result.begin(), result.end());
        unordered_set<int> ss(result.begin(), result.end());
        if(ss.size() != result.size()) return false;
        return result == check;
        
    }
};