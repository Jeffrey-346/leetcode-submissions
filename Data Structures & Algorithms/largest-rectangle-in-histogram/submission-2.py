class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        # need this so that the loop does a final run
        heights.append(0)
        # counting area forwards
        for i in range(len(heights)):
            start_index = i
            while stack and heights[i] < stack[-1][1]:
                start_index, height = stack.pop()
                width = i - start_index
                max_area = max(max_area, width * height)
            stack.append((start_index, heights[i]))
        return max_area
        