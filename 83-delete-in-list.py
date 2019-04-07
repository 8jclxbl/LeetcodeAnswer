class ListNode:
    def __init__(self,val):
        self.next = None
        self.val = val

a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
e = ListNode(3)

a.next = b
b.next = c
c.next = d
d.next = e

#注意给定的输入中，由于已经是链表，
#所以最后加入的节点如果不是原链表的最后一个节点的时候
#结果会返回后面不应该出现的节点
def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    temp = head
    if head.next == None:
        return head
    current = head.next
    res = pre_node = ListNode(0)
    
    res.next = head
    res = res.next

    while current != None:
        print(current.val, temp.val)
        if current.val != temp.val:
            res.next = current
            res = res.next
            print('res ',res.val)
            temp = current
        current = current.next
    res.next = None
    return pre_node.next

if __name__ == '__main__':
    result = deleteDuplicates(a)
    while result != None:
        print(result.val)
        result = result.next