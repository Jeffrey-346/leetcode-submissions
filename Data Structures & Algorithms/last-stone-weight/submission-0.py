class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -1 * stone)
        while heap:
            if len(heap) == 1:
                return -1 * heap[0]
            stone1 = -1 * heapq.heappop(heap)
            stone2 = -1 * heapq.heappop(heap)
            if stone1 == stone2:
                continue
            new_stone = stone1 - stone2
            heapq.heappush(heap, -1 * new_stone)
        return 0
        