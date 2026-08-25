# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        tail = res
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                # add to output and cut off tail
                tail.next = curr1
                tail = tail.next

                next_node = curr1.next
                curr1.next = None
                curr1 = next_node
            else:
                tail.next = curr2
                tail = tail.next

                next_node = curr2.next
                curr2.next = None
                curr2 = next_node
        if not curr1:
            tail.next = curr2
        if not curr2:
            tail.next = curr1
        return res.next



        