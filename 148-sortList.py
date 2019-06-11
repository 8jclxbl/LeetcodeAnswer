class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class List:
    def __init__(self,values):
        self.generate(values)

    @classmethod
    def generate(self,values):
        self.head = ListNode(values[0])
        cur = self.head
        for i in values[1:]:
            cur.next = ListNode(i)
            cur = cur.next

def traverse(head):
    while head:
        print(head.val)
        head = head.next

#归并排序法
#一般而言用到了递归应该不是常数空间复杂度

#最简单，遍历一遍，记录数组，排序后重新赋值
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return None
        if not head.next:
            return head
        else:
            mid = self.middleNode(head)
            l1 = self.sortList(head)
            l2 = self.sortList(mid)
            return self.mergeTwoLists(l1,l2)

    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast.next:
            last = slow
            slow = slow.next
            fast = fast.next
            if not fast:break
            else:fast = fast.next
            if not fast:break
        last.next = None
        return slow
    
    def mergeTwoLists(self, l1, l2):
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
    t = List([-1,5,3,4,0])
    test = t.head

    s = Solution()
    r = s.sortList(test)
    traverse(r)