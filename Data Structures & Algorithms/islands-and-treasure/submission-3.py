class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        lands = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    lands.append((row, col, 0))
        
        while lands:
            row, col, distance = lands.popleft()
            if distance == 0:
                lands.append((row + 1, col, distance + 1))
                lands.append((row - 1, col, distance + 1))
                lands.append((row, col + 1, distance + 1))
                lands.append((row, col - 1, distance + 1))

            if (row < 0 or row >= len(grid) or
                col < 0 or col >= len(grid[0]) or 
                grid[row][col] != 2147483647):
                continue
            grid[row][col] = distance
            lands.append((row + 1, col, distance + 1))
            lands.append((row - 1, col, distance + 1))
            lands.append((row, col + 1, distance + 1))
            lands.append((row, col - 1, distance + 1))
            

        