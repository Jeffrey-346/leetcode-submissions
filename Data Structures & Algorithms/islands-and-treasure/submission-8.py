class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(r, c):
            queue = deque()
            queue.append((r, c, 0))
            while queue:
                row, col, dist = queue.popleft()
                if row > 0 and dist + 1 < grid[row - 1][col]:
                    grid[row - 1][col] = dist + 1
                    queue.append((row - 1, col, dist + 1))
                if row < len(grid) - 1 and dist + 1 < grid[row + 1][col]:
                    grid[row + 1][col] = dist + 1
                    queue.append((row + 1, col, dist + 1))
                if col > 0 and dist + 1 < grid[row][col - 1]:
                    grid[row][col - 1] = dist + 1
                    queue.append((row, col - 1, dist + 1))
                if col < len(grid[0]) - 1 and dist + 1 < grid[row][col + 1]:
                    grid[row][col + 1] = dist + 1
                    queue.append((row, col + 1, dist + 1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfs(i, j)
        return

