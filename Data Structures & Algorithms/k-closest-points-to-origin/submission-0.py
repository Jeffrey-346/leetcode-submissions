class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            distances.append((distance, point))
        heapq.heapify(distances)
        res = []
        for i in range(k):
            distance, point = heapq.heappop(distances)
            res.append(point)
        return res


        