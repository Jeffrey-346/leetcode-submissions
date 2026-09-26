class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                queue = deque()
                queue.append((i, j))
                grid[i][j] = 0
                area = 1
                while queue:
                    row, col = queue.popleft()
                    if row > 0 and grid[row - 1][col] == 1:
                        grid[row - 1][col] = 0
                        area += 1
                        queue.append((row - 1, col))
                    if row < len(grid) - 1 and grid[row + 1][col] == 1:
                        grid[row + 1][col] = 0
                        area += 1
                        queue.append((row + 1, col))
                    if col > 0 and grid[row][col - 1] == 1:
                        grid[row][col - 1] = 0
                        area += 1
                        queue.append((row, col - 1))
                    if col < len(grid[0]) - 1 and grid[row][col + 1] == 1:
                        grid[row][col + 1] = 0
                        area += 1
                        queue.append((row, col + 1))
                max_area = max(area, max_area)
        return max_area
        