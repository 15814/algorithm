
// from nowcoder oj

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
    ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
    {
        ListNode* p1 = pHead1;
        ListNode* p2 = pHead2;
        if (p1 == nullptr || p2 == nullptr){
            if (p1 == nullptr)
                return p2;
            else
                return p1;
        }
        ListNode* head = NULL;
        ListNode* cur;
        while(p1 != NULL && p2 != NULL){
            if (p1->val <= p2->val) {
                if (head == NULL) {
                    head = p1;
                    cur = head;
                    p1 = p1->next;
                }else{
                    cur->next = p1;
                    p1 = p1->next;
                    cur = cur->next;
                }
            }else{
                if (head == NULL) {
                    head = p2;
                    cur = head;
                    p2 = p2->next;
                }else{
                    cur->next = p2;
                    p2 = p2->next;
                    cur = cur->next;
                }
            }

        }

        while (p1 != nullptr) {
            cur->next = p1;
            p1 = p1->next;
        }

        while (p2 != nullptr) {
            cur->next = p2;
            p2 = p2->next;
        }

        return head;
    }
};
