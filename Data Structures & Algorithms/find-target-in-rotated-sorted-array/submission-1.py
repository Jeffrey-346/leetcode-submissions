class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use last solution to find the minimum in O(log(n)) time
        # then just use modular arithmetic to search the array
        m = self.mindex(nums)
        # [4, 5, 6, 1, 2, 3]
        # [0, 1, 2, 3, 4, 5]
        # [3, 4, 5, 0, 1, 2]
        # left and right operate as if unrotated
        # find mid
        # add min_index to mid to get adjusted mid (mod len(nums))
        # check if mid is our target
        # when adjusting l and r, make sure to use unrotated mid
        l, r = 0 , len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            rotated_mid = (mid + m) % len(nums)
            if nums[rotated_mid] == target:
                return rotated_mid
            elif nums[rotated_mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
            


    def mindex(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return l

        