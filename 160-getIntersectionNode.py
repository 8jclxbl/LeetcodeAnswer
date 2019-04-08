class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tA = headA
        tB = headB
        
        over = False
        
        while tA != tB:
            if not tA:
                if not over:over = True
                else:return None
                tA = headB
            else:
                tA = tA.next
            if not tB:
                tB = headA
            else:
                tB = tB.next
                
        return tA