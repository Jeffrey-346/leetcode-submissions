class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we are looking for the one moment in the array where it goes from large to small. As long as the array is not in its original form, we can find this. i.e. if mid == last index, return zero index. If mid equals zero index, return it, 
        # but the question is... how do we know which direction to search?
        # well, if the middle index is greater than the far right, then 
        # there most be the downward jump in the right direction
        # otherwise there must be the jump in the left direction
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid - 1] >= nums[mid]:
                return nums[mid]
            else:
                r = mid - 1
                
        