# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:return None
        cur = head.next
        oddLast = head
        last = head
        count = 2
        while cur:
            if count % 2 == 1:
                curNxt = cur.next
                tmp = oddLast.next
                oddLast.next = cur
                oddLast = oddLast.next
                cur.next = tmp
                last.next = curNxt
                last = last.next
                cur = curNxt
            else:
                last = cur
                cur = cur.next
            count += 1
        return head