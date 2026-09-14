class Solution:
    def rob(self, nums: List[int]) -> int:
        # Question: at house i, what is the most amount of money
        # I can get?
        # options: either however much there was at house i - 2 + nums[i]
        #          or however much there is at house i - 1
        # only need to keep track of i - 2 and i - 1

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        profit = [0] * 2
        profit[0] = nums[0]
        profit[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr = nums[i]
            if curr + profit[0] > profit[1]:
                temp = profit[0]
                profit[0] =  profit[1]
                profit[1] = temp + curr
            else:
                profit[0] = profit[1]
        return profit[1]
        