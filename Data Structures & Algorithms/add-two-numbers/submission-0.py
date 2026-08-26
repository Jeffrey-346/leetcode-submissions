# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # set curr1 to be the longer one
        curr1 = l1
        curr2 = l2
        length1 = 0
        length2 = 0
        while curr1:
            length1 += 1
            curr1 = curr1.next
        while curr2:
            length2 += 1
            curr2 = curr2.next

        if length2>length1:
            l1, l2 = l2, l1
        curr1 = l1
        curr2 = l2

        prev = None
        carry = 0
        while curr2:
            value = curr1.val + curr2.val + carry
            if value > 9:
                value = value - 10
                carry = 1
            else:
                carry = 0
            # set l1 node value to value
            curr1.val = value

            prev = curr1
            curr1 = curr1.next
            curr2 = curr2.next

        while carry and curr1:
            value = curr1.val + carry
            if value > 9:
                value = value - 10
                carry = 1
            else:
                carry = 0
            curr1.val = value
            prev = curr1
            curr1 = curr1.next
        if carry:
            prev.next = ListNode(1)
        
        return l1




        