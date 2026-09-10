class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)] # list of lists
        # create the adjacency matrix:
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            adj[node1].append(node2)
            adj[node2].append(node1)

        components = 0
        visited = set()
        # find unvisited node to start the search
        for i in range(n):
            if i not in visited:
                queue = deque()
                queue.append(i)
                components += 1
                while queue:
                    node = queue.popleft()
                    visited.add(node)
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
        return components
            
        