#best answer
def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        first = ListNode(-1)
        first.next = head
        p, q = first, head
        while q:
            if q.val == val:
                p.next = q.next
                q = p.next
            else:
                p = p.next
                q = q.next
        return first.next

def removeElements(head, val):
    pre = None
    start = head
    while head:
        if head.val == val:
            if pre:
                pre.next = head.next
                
            else:
                start = head.next
        else:
            pre = head
        head = head.next
    return start

                
    