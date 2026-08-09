# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy =  ListNode()

        tail = dummy
        carry = 0

        while l1 and l2:
            s = l1.val + l2.val + carry

            if s > 9:
                node = ListNode(s % 10)
                carry = 1
            else:
                node = ListNode(s)
                carry = 0

            l1 = l1.next
            l2 = l2.next

            tail.next = node
            tail = tail.next

        while l1:
            s = l1.val  + carry

            if s > 9:
                node = ListNode(s % 10)
                carry = 1
            else:
                node = ListNode(s)
                carry = 0

            l1 = l1.next 

            tail.next = node
            tail = tail.next

        while l2:
            s = l2.val + carry

            if s > 9:
                node = ListNode(s % 10)
                carry = 1
            else:
                node = ListNode(s)
                carry = 0

            l2 = l2.next 

            tail.next = node
            tail = tail.next

        if carry:
            node = ListNode(1)
            tail.next = node
            tail = tail.next
            
        return dummy.next
