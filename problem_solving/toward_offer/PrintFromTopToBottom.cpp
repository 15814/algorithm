
// 题目描述
// 从上往下打印出二叉树的每个节点，同层节点从左至右打印。

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
    vector<int> PrintFromTopToBottom(TreeNode* root) {
        deque<TreeNode*> deq;
        vector<int> result;
        if (root == nullptr) {
            return result;
        }
        deq.push_back(root);
        while (!deq.empty()) {
            TreeNode* cur = deq.front();
            deq.pop_front();
            result.push_back(cur->val);
            if (cur->left != nullptr) {
                deq.push_back(cur->left);
            }
            if (cur->right != nullptr) {
                deq.push_back(cur->right);
            }
        }
        return result;
    }
};











// note
