


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
    ListNode* FindFirstCommonNode( ListNode* pHead1, ListNode* pHead2) {
        if (pHead1 == nullptr || pHead2 == nullptr) {
            return nullptr;
        }

        ListNode* p1 = pHead1;
        ListNode* p2 = pHead2;
        int len1 = 0;
        while (p1 != nullptr) {
            ++len1;
            p1 = p1->next;
        }
        int len2 = 0;
        while (p2 != nullptr) {
            ++len2;
            p2 = p2->next;
        }

        p1 = pHead1;
        p2 = pHead2;
        if (len1 < len2) {
            swap(p1,p2);
            swap(len1,len2);
        }

        unsigned int steps = len1 - len2;
        while (steps--) {
            p1 = p1->next;
        }

        while (p1 != p2) {
            p1 = p1->next;
            p2 = p2->next;
        }

        return p1;









    }
};


















//
