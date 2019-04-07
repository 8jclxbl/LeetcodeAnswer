class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
BETTER
    def middleNode(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
"""

class Solution:
    def middleNode(self,head):
        fast = head
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if not fast:break
            else:fast = fast.next
            if not fast:break
        return slow
            