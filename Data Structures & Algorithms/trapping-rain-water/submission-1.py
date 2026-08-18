class Solution:
    def trap(self, height: List[int]) -> int:
        # solution:
        # initalize l, r pointers to first negative drop
        # scan foward smaller one until hit something equal or bigger
        # fill with appropriate water at each step. Repeat 

        l, r = 0, len(height) - 1
        volume = 0
        while l < r:
            # skip past any upward/flat elevation change
            while height[l] <= height[l + 1] and l < r:
                l += 1
            while height[r] <= height[r - 1] and l < r:
                r -= 1
            if l == r:
                return volume
            # take the smaller height and scan forward
            if height[l] < height[r]:
                curr = l + 1
                while height[curr] < height[l]:
                    volume += height[l] - height[curr]
                    curr += 1
                l = curr
            else:
                curr = r - 1
                while height[curr] < height[r]:
                    volume += height[r] - height[curr]
                    curr -= 1
                r = curr
        return volume


        