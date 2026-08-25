# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the end
        # get index of n
        # delete it
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        index = count - n
        count = 0
        curr = head
        prev = None
        while True:
            if count == index:
                if not prev:
                    return head.next
                prev.next = curr.next
                return head
            prev = curr
            curr = curr.next
            count += 1


        