
/*
struct RandomListNode {
    int label;
    struct RandomListNode *next, *random;
    RandomListNode(int x) :
            label(x), next(NULL), random(NULL) {
    }
};
*/
class Solution {
public:
    RandomListNode* Clone(RandomListNode* pHead)
    {
        if (pHead == nullptr) {
            return nullptr;
        }

        RandomListNode* cur = pHead;
        RandomListNode* nhead = new RandomListNode(pHead->label);
        RandomListNode* ncur = nhead;
        std::map<RandomListNode*, RandomListNode*> m;
        m[pHead] = nhead;
        while (cur->next != nullptr) {
            cur = cur->next;
            RandomListNode* node = new RandomListNode(cur->label);
            m[cur] = node;
            ncur->next = node;
            ncur = ncur->next;
        }

        cur = pHead;
        ncur = nhead;
        while (cur != nullptr) {
            RandomListNode* node = m[cur->random];
            ncur->random = node;
            cur = cur->next;
            ncur = ncur->next;
        }

        return nhead;

    }
};




















//
