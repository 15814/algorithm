//
// 题目描述
// 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。


/*
struct TreeLinkNode {
    int val;
    struct TreeLinkNode *left;
    struct TreeLinkNode *right;
    struct TreeLinkNode *next;
    TreeLinkNode(int x) :val(x), left(NULL), right(NULL), next(NULL) {

    }
};
*/
class Solution {
public:
    TreeLinkNode* GetNext(TreeLinkNode* pNode)
    {
        if (pNode == nullptr) {
            return nullptr;
        }

        if (pNode->right != nullptr) {
            // get most left in right side
            TreeLinkNode* cur = pNode->right;
            while (cur->left != nullptr) {
                cur = cur->left;
            }
            return cur;
        }else{
            TreeLinkNode* parent = pNode->next;
            TreeLinkNode* cur = pNode;
            while (parent != nullptr) {
                if (parent->left == cur) {
                    break;
                }else{
                    cur = parent;
                    parent = parent->next;
                }
            }
            return parent;
        }

    }
};
