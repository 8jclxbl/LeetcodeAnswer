# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 or l2
        return head.next


if __name__ == "__main__":
    a = [ListNode(i) for i in (1, 2, 4)]
    b = [ListNode(i) for i in (1, 3, 4)]

    l1 = a[0]
    a[0].next = a[1]
    a[1].next = a[2]

    l2 = b[0]
    b[0].next = b[1]
    b[1].next = b[2]

    s = Solution()
    root = s.mergeTwoLists(l1, l2)

    while root:
        print(root.val)
        root = root.next
