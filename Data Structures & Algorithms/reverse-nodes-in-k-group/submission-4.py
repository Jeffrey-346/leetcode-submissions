# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # track previous node
        # have a loop
        # check length if there are enough (k) remaining nodes
        # if length is < k return
        # else:
        # - preserve the next start node
        # - reverse k nodes (set would be end's next to the next start)
        # continue until there are no longer k nodes

        curr = head
        next_first = curr
        prev_end = None
        while True:
            # make sure we at least k nodes left
            prev = None
            length = 0
            while next_first and length < k:
                length += 1
                next_first = next_first.next
            if length < k and not next_first:
                return head

            # reverse k nodes
            curr_end = curr
            count = 0
            while count < k:
                next_node = curr.next
                curr.next = prev

                prev = curr
                curr = next_node
                count += 1
            # hook up previoous end to now reversed start
            if prev_end:
                prev_end.next = prev
            else:
                head = prev
            # hook up end to the rest of the list (not yet reversed)
            curr_end.next = next_first
            # but we also need to track the prev
            prev_end = curr_end
        return head

            
            

        