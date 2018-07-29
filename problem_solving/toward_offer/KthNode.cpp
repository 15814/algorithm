//
// 给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

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
    TreeNode* KthNode(TreeNode* pRoot, int k)
    {
        if (k < 1 || pRoot == nullptr) {
            return nullptr;
        }
        vector<TreeNode*> vec;
        recur_travel(pRoot,k,vec);
        if (vec.size() >= k) {
            return vec[k-1];
        }else{
            return nullptr;
        }
    }

    TreeNode* recur_travel(TreeNode* pRoot, int k,vector<TreeNode*> &vec){
        if (pRoot == nullptr) {
            return nullptr;
        }
        recur_travel(pRoot->left,k,vec);
        vec.push_back(pRoot);
        if (vec.size() >= k) {
            return pRoot;
        }
        recur_travel(pRoot->right,k,vec);

        // when k > size(TreeNodes)
        return nullptr;
    }

};
