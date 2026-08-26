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
        # the fear is what if the list has cycles right?
        # we can just have a visited
        # loop through and create normal list
        # and what if we have 2 hashmaps
        # org list: map node objects to indicies (used only to make map 2)
        # org list: map node index to its random index using 1st map
        # copied list: map indices to node objects
        # use map 2 to map from current index to random index
        # use map 3 to map from index to actual node object
        # connect up
        res = Node(0)
        tail = res
        prev = None

        node_to_index = {}
        index_to_random = {}
        random_to_node = {}

        curr = head
        index = 0
        while curr:
            # creat normal map (no random)
            tail.next = Node(curr.val)
            tail = tail.next

            # create org node to index map and index to copy node map
            node_to_index[curr] = index
            random_to_node[index] = tail
            
            curr = curr.next
            index += 1
        
        # create index to random index map
        for node in node_to_index.keys():
            index = node_to_index[node]
            random_node = node.random
            if random_node:
                random_index = node_to_index[random_node]
                index_to_random[index] = random_index
            else:
                index_to_random[index] = -1
        
        # set random
        index = 0
        curr = res.next
        while curr:
            random_index = index_to_random[index]
            if random_index == -1:
                curr.random = None
            else:
                curr.random = random_to_node[random_index]
            curr = curr.next
            index += 1
        return res.next




        