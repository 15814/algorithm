
// 题目描述
// 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
        int presize = pre.size();
        int vinsize = vin.size();
        if (presize == 0 || vinsize == 0 || presize != vinsize) {
            return NULL;
        }
        if (presize == 1) {
            if (pre[0] != vin[0]) {
                return NULL;
            }else{
                TreeNode* node = new TreeNode(pre[0]);
                return node;
            }
        }

        TreeNode* root ;
        root = recurConstruct(pre,0,presize,vin,0,vinsize);
        return root;

    }

    TreeNode* recurConstruct(vector<int> pre,int counterstart,int counterend,vector<int> vin, int start, int end){

        if(end - start <= 0){
            return NULL;
        }
        if (end - start == 1) {
            TreeNode* node = new TreeNode(vin[start]);
            return node;
        }


        TreeNode* root = new TreeNode(pre[counterstart]);
        int sep = -1;
        for (int i = start; i < end; i++) {
            if (vin[i] == root->val) {
                sep = i ;
                break;
            }
        }
        if (sep < 0) {
            return NULL;
        }
        int presep = counterstart + (sep-start)+1;
        TreeNode* left = recurConstruct(pre,counterstart+1,presep,vin,start,sep);
        TreeNode* right = recurConstruct(pre,presep,counterend,vin,sep+1,end);

        root->left = left;
        root->right = right;

        return root;
    }
};






// AC 之后的心得
/*
区间划分的时候，你还是形成你自己的一种划分习惯。（不然，时而闭区间时而开区间，就会出错。像写这一题的时候一样。）
我自己的约定：所有的区间划分 一律用 左闭右开，即 [a,b)，与 Python 中的 range(a,b) 一致。





*/




//
