class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # breadth first search from each rotten fruit
        # Concretely: we would have a queue of rotten fruits
        # loop:
        # for each adjacent cell of fresh fruit
        # - mark it rotten, add its position to new queue (which will
        #   replace current queue once we've gone through the whole 
        #   level)
        # If new queue is empty do not incremment minutes
        # Replace curr queue with new queue
        minutes = 0
        queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))

        while queue:
            new_queue = deque()
            while queue:
                row, col = queue.popleft()

                if row > 0 and grid[row - 1][col] == 1:
                    grid[row - 1][col] = 2
                    new_queue.append((row - 1, col))
                if row < len(grid) - 1 and grid[row + 1][col] == 1:
                    grid[row + 1][col] = 2
                    new_queue.append((row + 1, col))
                if col > 0 and grid[row][col - 1] == 1:
                    grid[row][col - 1] = 2
                    new_queue.append((row, col - 1))
                if col < len(grid[0]) - 1 and grid[row][col + 1] == 1:
                    grid[row][col + 1] = 2
                    new_queue.append((row, col + 1))
            queue = new_queue
            if queue:
                minutes += 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
        
        return minutes
            
            


        

        