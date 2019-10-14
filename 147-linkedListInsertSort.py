# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    @staticmethod
    def show(node):
        temp = []
        while node:
            temp.append(str(node.val))
            node = node.next
        print('->'.join(temp))

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        ordered = head
        ordered_length = 1
        while ordered.next:
            nxt = ordered.next
            cur = head
            last = None
            count = 0
            while count < ordered_length:
                if cur.val < nxt.val:
                    last = cur
                    cur = cur.next
                else:
                    ordered.next = nxt.next
                    if not last:
                        nxt.next = head
                        head = nxt
                    else:
                        last.next = nxt
                        nxt.next = cur
                    break
                count += 1
            if nxt.val > ordered.val:
                ordered = nxt
            ordered_length += 1
            ListNode.show(head)
        return head

def list2Linkedlist(l):
    nodes = [ListNode(i) for i in l]
    root = nodes[0]
    cur = root
    for i in nodes[1:]:
        cur.next = i
        cur = cur.next
    return root

if __name__ == "__main__":
    s = Solution()
    test = [4,2,1,3]
    root = list2Linkedlist(test)

    ListNode.show(root)
    res = s.insertionSortList(root)
    ListNode.show(res)
    
                        
            