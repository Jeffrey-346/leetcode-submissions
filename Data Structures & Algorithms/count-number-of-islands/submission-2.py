class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                res += 1
                stack = []
                stack.append((i, j))
                while stack:
                    row, col = stack.pop()
                    grid[row][col] = '0'
                    if row > 0 and grid[row - 1][col] == '1':
                        stack.append((row - 1, col))
                    if row < len(grid) - 1 and grid[row + 1][col] == '1':
                        stack.append((row + 1, col))
                    if col > 0 and grid[row][col - 1] == '1':
                        stack.append((row, col - 1))
                    if col < len(grid[0]) - 1 and grid[row][col + 1] == '1':
                        stack.append((row, col + 1))
        return res
        