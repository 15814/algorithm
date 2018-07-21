// 题目描述
// 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）



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
    bool HasSubtree(TreeNode* pRoot1, TreeNode* pRoot2)
    {
        if (pRoot1 == nullptr || pRoot2 == nullptr) {
            return false;
        }

        if (travel_judge(pRoot1,pRoot2) > 0) return true;
        else return false;
    }

    int travel_judge(TreeNode* p1, TreeNode* p2){
        if (p1 == nullptr) {
            return 0;
        }
        if (p1->val == p2->val){
            if (is_included(p1,p2)) {
                return 1;
            }
        }

        return travel_judge(p1->left,p2) + travel_judge(p1->right,p2);

    }

    bool is_included(TreeNode* p1, TreeNode* p2){
        if (p2 == nullptr) {
            return true;
        }

        if (p1 == nullptr || p2->val != p1->val) {
            return false;
        }
        return is_included(p1->left,p2->left) && is_included(p1->right,p2->right);

    }
};






















//
