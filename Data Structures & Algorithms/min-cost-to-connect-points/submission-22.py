class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()

        total = 0
        heap = [(0, 0)] # distance, point
        while len(visited) < n:
            distance, point = heapq.heappop(heap)

            if point in visited:
                continue

            total += distance
            visited.add(point)

            for i in range(n):
                if i not in visited:
                    distance = abs(points[point][0] - points[i][0]) + abs(points[point][1] - points[i][1])
                    heapq.heappush(heap, (distance, i))
        return total
                    
        