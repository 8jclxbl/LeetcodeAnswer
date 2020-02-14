#单链表，只能操作单个节点，所以考虑移动节点的值

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node:
            if not node.next.next:
                node.val = node.next.val
                node.next = None
                break
            if node.next:
                node.val = node.next.val
                node = node.next
