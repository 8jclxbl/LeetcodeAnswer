# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:return None
        if not head.next:
            return head
        root = head.next
        cur = head.next.next
        head.next.next = head
        head.next = cur
        
        left = head
        swap = 0
        while cur:
            if not swap:
                last = cur
            else:
                temp = cur.next
                left.next = cur
                cur.next = last
                last.next = temp
                left = last
                cur = left
            
            cur = cur.next
            swap ^= 1
        return root
            
                
        
        