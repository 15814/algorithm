// 题目描述
// 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5


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
    ListNode* deleteDuplication(ListNode* pHead)
    {
        if (pHead == nullptr) {
            return nullptr;
        }

        ListNode* nhead = new ListNode(-1);
        ListNode* cur = pHead;
        nhead->next = pHead;
        ListNode* pre = nhead;
        while (cur != nullptr && cur->next != nullptr) {

            if (cur->val == cur->next->val) {
                ListNode* keep = cur;
                cur = cur->next;
                while (cur != nullptr && cur->next != nullptr && cur->val == cur->next->val) {
                    cur = cur->next;
                }
                if (cur->next != nullptr) {
                    pre->next = cur->next;
                    cur = cur->next;
                }else{
                    pre->next = nullptr;
                    break;
                }

            }else{
                pre = cur;
                cur = cur->next;
            }
        }
        if(nhead->next != nullptr) return nhead->next;
        else return nullptr;
    }
};
