class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        for i in range(len(edges) + 1):
            parent[i] = i
        def find(x):
            if parent[x] == x:
                return x
            else:
                return find(parent[x])

        def union(a, b):
            root1 = find(a)
            root2 = find(b)
            
            # if they are already connected
            if root1 == root2:
                return False
            
            parent[root2] = root1
            return True
        
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
        

            
        