//
// 题目描述
// 输入一个链表，输出该链表中倒数第k个结点。

/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
        if (pListHead == nullptr) {
            return nullptr;
        }

        unsigned int length = 0;
        ListNode* cur = pListHead;
        while (cur != nullptr) {
            ++length;
            cur = cur->next;
        }

        if (k > length) {
            return nullptr;
        }

        // go k steps
        ListNode* faster = pListHead;
        unsigned int ct = k;
        while (ct--) {
            faster = faster->next;
        }

        ListNode* slower = pListHead;
        while (faster != nullptr) {
            faster = faster->next;
            slower = slower->next;
        }

        return slower;
    }
};














//
