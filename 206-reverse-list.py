class ListNode(object):
    def __init__(self, x):
        self.val = x 
        self.next = None

#best answer
def reverseList1(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

def reverseList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = head
        temp = []
        size = 0
        while head != None:
            temp.append(head.val)
            size += 1
            head = head.next
        head = pre
        while size > 0:
            head.next = ListNode(temp[size-1])
            size -= 1
            head = head.next
        return pre.next
        

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d

result = reverseList(a)
while result != None:
    print(result.val)
    result = result.next