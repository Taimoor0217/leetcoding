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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p and !q){
            return true;
        }
        if (!p || !q){
            return false;
        }
        if (p->val != q->val){
            return false ;
        }else{
            return isSameTree(p->left , q->left) && isSameTree(p->right , q->right);
        }
        
    }
};

// Runtime: 4 ms, faster than 59.81% of C++ online submissions for Same Tree.
// Memory Usage: 9.7 MB, less than 100.00% of C++ online submissions for Same Tree.