class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # naive solution, go through each combination of indicies and 
        # choose the greatest amount <- O(n^2)

        # we want better, we want O(n)
        # track the current max amount, intialized to far left and right
        # What can we definitively say? 
        # Whichever pointer is the limiting one, that is the best the
        # pointer will ever do, because it is the most height it can       
        # achieve and the furthest distance (<- a little sus)

        l, r = 0, len(heights) - 1
        max_volume = 0
        while l < r:
            limit = min(heights[l], heights[r])
            max_volume = max(max_volume, limit * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_volume
        