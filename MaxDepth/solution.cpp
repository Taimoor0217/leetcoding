/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root){
            return 0;
        }else{
            int l = maxDepth(root->left);
            int r = maxDepth(root->right);
            if (l > r)
                return l+1;
            return r+1;
        }
    }
};


// Runtime: 12 ms, faster than 57.93% of C++ online submissions for Maximum Depth of Binary Tree.
// Memory Usage: 19.1 MB, less than 98.90% of C++ online submissions for Maximum Depth of Binary Tree.