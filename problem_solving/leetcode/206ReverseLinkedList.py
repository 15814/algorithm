# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head:
            prev = head
            cur = head.next
            if cur:
                mark = cur.next
            while cur:
                cur.next = prev
                prev = cur
                cur = mark
                if mark:
                    mark = mark.next
            head.next = None

            return prev
            
