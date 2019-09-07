#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        before = ListNode('head')
        cur = before
        cnt = 0
        while l1 and l2:
            temp = l1.val + l2.val + cnt
            cnt = temp//10
            val = temp%10
            cur.next = ListNode(val)
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
            
        res = l1 if l1 else l2
        while cnt:
            if not res:
                res = ListNode(0)
            temp = res.val + cnt
            cnt = temp//10
            val = temp%10
            cur.next = ListNode(val)
            res = res.next
            cur = cur.next
        if res:
            cur.next = res
            
        
        return before.next