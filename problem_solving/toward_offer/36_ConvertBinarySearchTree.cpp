/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {
public:
    TreeNode* Convert(TreeNode* pRootOfTree)
    {
        return unrecur_inorder(pRootOfTree);
    }

    TreeNode* unrecur_inorder(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }
        stack<TreeNode*> st;
        TreeNode* head = nullptr;
        TreeNode* pre = nullptr;
        //st.push(root);
        while (!st.empty() or root != nullptr) {
            if (root != nullptr) {
                st.push(root);
                root = root->left;
            }else{
                TreeNode* top = st.top();
                st.pop();
                if (head == nullptr) {
                    head = top;
                    pre = top;
                }else{
                    pre->right = top;
                    top->left = pre;
                    pre = top;
                }

                // std::cout << top->val << '\n';
                root = top->right;
            }
        }
        return head;

    }
};
