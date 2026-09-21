class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
                return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        def rob_helper(nums):
            profit = [nums[0], max(nums[0], nums[1])]
            for i in range(2, len(nums)):
                temp = profit[1]
                profit[1] = max(profit[0] + nums[i], profit[1])
                profit[0] = temp
            return profit[1]
        return max(rob_helper(nums[1:]), rob_helper(nums[:len(nums) - 1]))


        

        