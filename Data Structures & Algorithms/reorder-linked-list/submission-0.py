# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. first we split the lists into two (first half second half)
        # - get the length
        # - iterate for half the length
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        curr = head
        half = math.ceil(length/2) 
        for _ in range(half - 1):
            curr = curr.next

        head1 = head
        head2 = curr.next
        curr.next = None
        # 2. then we reverse second half
        curr = head2
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node
        head2 = prev
        # 3. then we interweave them
        res = ListNode()
        tail = res
        coin = 1
        while head1 or head2:
            if coin == 1:
                next1 = head1.next
                tail.next = head1
                tail = tail.next
                tail.next = None
                head1 = next1
                coin = 2
            elif coin == 2:
                next2 = head2.next
                tail.next = head2
                tail = tail.next
                tail.next = None
                head2 = next2
                coin = 1
        head = res.next





        