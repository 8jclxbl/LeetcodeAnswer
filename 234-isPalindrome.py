class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
            
        if temp == temp[::-1]:return True
        else: return False
                