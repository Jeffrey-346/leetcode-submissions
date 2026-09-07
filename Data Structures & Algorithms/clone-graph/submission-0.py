"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        def dfs(node):
            if not node:
                return
            new_node = Node(node.val)
            old_to_new[node] = new_node

            for neighbor in node.neighbors:
                if neighbor in old_to_new:
                    new_node.neighbors.append(old_to_new[neighbor])
                else:
                    new_node.neighbors.append(dfs(neighbor))
            return new_node
        return dfs(node)




        