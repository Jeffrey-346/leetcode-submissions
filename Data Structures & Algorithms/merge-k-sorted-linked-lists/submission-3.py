# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # apparently we need faster so let's use a min heap
        # put each first node into the heap
        # pop the min and add the next node
        # repeat until heap is empty

        head = ListNode()
        tail = head
        heap = []

        # initialize heap by adding first node
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        count = 0
        while heap:
            _, _, lst = heapq.heappop(heap)
            # remove node from list and add new node to list
            min_node = lst
            lst = lst.next
            if lst:
                heapq.heappush(heap, (lst.val, count, lst))

            # append min node to res
            min_node.next = None
            tail.next = min_node
            tail = tail.next
            count += 1
        return head.next



        