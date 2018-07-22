// 题目描述
// 请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
    bool isSymmetrical(TreeNode* pRoot)
    {
        return isSymmetrical(pRoot,pRoot);
    }

    bool isSymmetrical(TreeNode* p1, TreeNode* p2){
        if (p1 == nullptr && p2 == nullptr) {
            return true;
        }
        if (p1 == nullptr || p2 == nullptr) {
            return false;
        }
        if (p1->val != p2->val) {
            return false;
        }

        return isSymmetrical(p1->left,p2->right) && isSymmetrical(p1->right,p2->left);

    }



};
