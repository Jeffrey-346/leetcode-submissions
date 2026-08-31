class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-1 * num for num in nums]
        heapq.heapify(heap)
        curr = None
        for _ in range(k):
            curr = heapq.heappop(heap)
        return -1 * curr
        