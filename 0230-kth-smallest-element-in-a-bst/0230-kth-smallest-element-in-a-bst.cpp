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
    vector<int> result;
    void inordertraversal(TreeNode* root, vector<int>& result)
    {
        if(!root)
        {
            return;
        }
        inordertraversal(root->left, result);

        result.push_back(root->val);

        inordertraversal(root->right, result);

    }
    int kthSmallest(TreeNode* root, int k) {
        inordertraversal(root, result);
        return result[k-1];
    }
};