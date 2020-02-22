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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ret;
        if(root == NULL){
            return ret;
        }
        TreeNode* prev = NULL;
        TreeNode* p = root;
        stack<TreeNode*> st;
        st.push(root);
        while(!st.empty()){
            p = st.top();
            if((p->left == NULL && p->right == NULL) || (prev != NULL && (p->left == prev || p->right == prev))){
                prev = p;
                st.pop();
                ret.push_back(prev->val);
            }
            else{
                if(p->right != NULL){
                    st.push(p->right);
                }
                if(p->left != NULL){
                    st.push(p->left);
                }
            }
        }
        return ret; 
    }
};