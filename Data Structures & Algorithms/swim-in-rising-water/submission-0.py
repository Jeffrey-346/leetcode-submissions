class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dijkstra's application
        # build adjacency matrix
        # maintain a list (distance from (0, 0) initialized to inf for each point
        n = len(grid)

        settled = set()
        heap = [(grid[0][0], (0, 0))] # time to swim, cell

        final_times = [float("inf")] * n * n

        while final_times[(n - 1)*n + n - 1] == float("inf"):
            time, cell = heapq.heappop(heap)
            if cell in settled:
                continue
            final_times[cell[0]*n + cell[1]] = time
            settled.add(cell)
            # relax the adjacent cells if they haven't already been settled
            if cell[0] > 0 and (cell[0] - 1, cell[1]) not in settled:
                next_time = max(time, grid[cell[0] - 1][cell[1]])
                heapq.heappush(heap, (next_time, (cell[0] - 1, cell[1])))
            if cell[0] < n - 1 and (cell[0] + 1, cell[1]) not in settled:
                next_time = max(time, grid[cell[0] + 1][cell[1]])
                heapq.heappush(heap, (next_time, (cell[0] + 1, cell[1])))
            if cell[1] > 0 and (cell[0], cell[1] - 1) not in settled:
                next_time = max(time, grid[cell[0]][cell[1] - 1])
                heapq.heappush(heap, (next_time, (cell[0], cell[1] - 1)))
            if cell[1] < n - 1 and (cell[0], cell[1] + 1) not in settled:
                next_time = max(time, grid[cell[0]][cell[1] + 1])
                heapq.heappush(heap, (next_time, (cell[0], cell[1] + 1)))
        return final_times[(n - 1)*n + n - 1]
        