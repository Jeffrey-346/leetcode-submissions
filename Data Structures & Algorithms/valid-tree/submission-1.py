class GraphNode:
    def __init__(self):
        self.neighbors = set() # set of other Nodes
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # construct the tree
        # traverse it bfs.
        # each time we add a new node to the frontier, remove its edge
        # If we try to visit a node in more once, return false
        # if visited < n after traversal, return false
        nodes = []
        for i in range(n):
            nodes.append(GraphNode())
        
        for edge in edges:
            node1 = nodes[edge[0]]
            node2 = nodes[edge[1]]
            node1.neighbors.add(node2)
            node2.neighbors.add(node1)
        
        # traversal (we can start at any node)
        visited = set()
        queue = deque()
        queue.append(nodes[0])
        while queue:
            node = queue.popleft()
            if node in visited:
                return False
            visited.add(node)
            for neighbor in node.neighbors:
                neighbor.neighbors.remove(node)
                queue.append(neighbor)
        if len(visited) < n:
            return False
        return True



        