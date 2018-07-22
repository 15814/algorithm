// 题目描述
// 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。



/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
*/
class Solution {
public:
    ListNode* EntryNodeOfLoop(ListNode* pHead)
    {
        ListNode* faster = pHead;
        ListNode* slower = pHead;

        while (faster != nullptr && faster->next != nullptr) {
            faster = faster->next->next;
            slower = slower->next;
            if (faster == slower) {
                slower = pHead;
                while (slower != faster) {
                    slower = slower->next;
                    faster = faster->next;
                }
                return slower;
            }
        }
        return nullptr;
    }
};
