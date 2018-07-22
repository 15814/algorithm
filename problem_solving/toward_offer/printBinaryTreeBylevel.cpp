// 题目描述
// 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。


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
        vector<vector<int> > Print(TreeNode* pRoot) {

            vector<vector<int> > result;
            if (pRoot == nullptr) {
                return result;
            }

            deque<TreeNode*> deq;
            std::vector<int> level;
            int nextlevelnumber = 0;
            int curlevelnumber = 1;

            deq.push_back(pRoot);

            while (!deq.empty()) {
                TreeNode* cur = deq.front();
                deq.pop_front();
                curlevelnumber--;
                level.push_back(cur->val);
                if (cur->left != nullptr) {
                    deq.push_back(cur->left);
                    nextlevelnumber++;
                }
                if (cur->right != nullptr) {
                    deq.push_back(cur->right);
                    nextlevelnumber++;
                }

                if (curlevelnumber <= 0) {
                    result.push_back(level);
                    level.clear();
                    curlevelnumber = nextlevelnumber;
                    nextlevelnumber = 0;
                }
            }

            return result;

        }
















};
