def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=fast=head
        while slow and fast:
            try:
                slow=slow.next
                fast=fast.next.next
            except:
                return False
            if slow==fast:
                return True
        return False


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes = []
        while head != None:
            if head in nodes:
                return True
            nodes.append(head)
            head = head.next
        return False
            