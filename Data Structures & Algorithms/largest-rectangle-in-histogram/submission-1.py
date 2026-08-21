class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # insight, 
        # when height decreases, taller heights are done growing rightward
        # check if it is less than heights[stack[-1]]
        # if it is, then we are done with this height for now
        # we need to retrieve its start index and its end index
        # its start index is in the stack, its end index is curr index 
        # add curr index to stack
        stack = []
        right_area = [0] * (len(heights))
        left_area = [0] * (len(heights))
        # need this so that the loop does a final run
        heights.append(0)
        # counting area forwards
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                start_index = stack.pop()
                height = heights[start_index]
                width = i - start_index
                right_area[start_index] = width * height
            stack.append(i)
        stack = []
        heights.pop()
        heights.reverse()
        heights.append(0)
        # counting backwards
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                start_index = stack.pop()
                height = heights[start_index]
                width = i - start_index
                # subtract one heigth so we don't double count
                left_area[start_index] = width * height - height
            stack.append(i)

        max_area = 0
        for i in range(len(right_area)):
            max_area = max(right_area[i] + left_area[len(right_area) - 1 -i], max_area)
        return max_area


        