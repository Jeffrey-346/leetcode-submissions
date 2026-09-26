"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        org_to_copy = {}
        new_node = Node()
        new_node.val = node.val
        org_to_copy[node] = new_node
        stack = []
        stack.append(node)
        while stack:
            org = stack.pop()
            for neighbor in org.neighbors:
                if neighbor not in org_to_copy:
                    copy = Node()
                    copy.val = neighbor.val
                    org_to_copy[neighbor] = copy
                    stack.append(neighbor)
        for key in org_to_copy:
            copy = org_to_copy[key]
            for neighbor in key.neighbors:
                copy.neighbors.append(org_to_copy[neighbor])
        return new_node

        

        