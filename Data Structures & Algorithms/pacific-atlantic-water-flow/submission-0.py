class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        # Add Pacific border
        for row in range(len(heights)):
            pacific.add((row, 0))
        for col in range(len(heights[0])):
            pacific.add((0, col))
        
        # Add Atlantic border
        for row in range(len(heights)):
            atlantic.add((row, len(heights[0]) - 1))
        for col in range(len(heights[0])):
            atlantic.add((len(heights) - 1, col))

        stack = list(pacific)
        while stack:
            row, col = stack.pop()

            if row > 0 and (row - 1, col) not in pacific and heights[row - 1][col] >= heights[row][col]:
                pacific.add((row - 1, col))
                stack.append((row - 1, col))
            if row < len(heights) - 1 and (row + 1, col) not in pacific and heights[row + 1][col] >= heights[row][col]:
                pacific.add((row + 1, col))
                stack.append((row + 1, col))
            if col > 0 and (row, col - 1) not in pacific and heights[row][col - 1] >= heights[row][col]:
                pacific.add((row, col - 1))
                stack.append((row, col - 1))
            if col < len(heights[0]) - 1 and (row, col + 1) not in pacific and heights[row][col + 1] >= heights[row][col]:
                pacific.add((row, col + 1))
                stack.append((row, col + 1))
        
        stack = list(atlantic)
        while stack:
            row, col = stack.pop()

            if row > 0 and (row - 1, col) not in atlantic and heights[row - 1][col] >= heights[row][col]:
                atlantic.add((row - 1, col))
                stack.append((row - 1, col))
            if row < len(heights) - 1 and (row + 1, col) not in atlantic and heights[row + 1][col] >= heights[row][col]:
                atlantic.add((row + 1, col))
                stack.append((row + 1, col))
            if col > 0 and (row, col - 1) not in atlantic and heights[row][col - 1] >= heights[row][col]:
                atlantic.add((row, col - 1))
                stack.append((row, col - 1))
            if col < len(heights[0]) - 1 and (row, col + 1) not in atlantic and heights[row][col + 1] >= heights[row][col]:
                atlantic.add((row, col + 1))
                stack.append((row, col + 1))
        res = []
        for elm in pacific:
            if elm in atlantic:
                res.append(elm)
        return res






        