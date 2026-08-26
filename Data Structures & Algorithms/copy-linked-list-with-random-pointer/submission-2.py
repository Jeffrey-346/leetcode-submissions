"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = Node(0)
        tail = res

        nodes = {}

        curr = head
        index = 0
        while curr:
            # creat normal map (no random)
            tail.next = Node(curr.val)
            tail = tail.next

            # create org node to index map and index to copy node map
            nodes[curr] = tail
            
            curr = curr.next
            index += 1
        
        curr = head
        while curr:
            random = curr.random
            if random:
                random_copy = nodes[curr.random]
            else:
                random_copy = None
            nodes[curr].random = random_copy

            curr = curr.next
        return res.next
        