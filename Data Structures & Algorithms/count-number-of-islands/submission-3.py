class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    stack = []
                    stack.append((i, j))
                    grid[i][j] = "0"
                    while stack:
                        r, c = stack.pop()
                        if r > 0 and grid[r - 1][c] == "1":
                            grid[r - 1][c] = "0"
                            stack.append((r- 1, c))
                        if r < len(grid) - 1 and grid[r + 1][c] == "1":
                            grid[r + 1][c] = "0"
                            stack.append((r + 1, c))
                        if c > 0 and grid[r][c - 1] == "1":
                            grid[r][c - 1] = "0"
                            stack.append((r, c - 1))
                        if c < len(grid[0]) - 1 and grid[r][c + 1] == "1":
                            grid[r][c + 1] = "0"
                            stack.append((r, c + 1))
        return islands

                        



        