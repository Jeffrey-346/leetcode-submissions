class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # let's have a dp array where index i represents the longest increasing subsequence
        # up to the ith element. we will actually have the list within the array
        # choice: if nums[i] is smaller than the last element and gives a subs of the same size
        # or larger, set that length to the index and then make nums[i] the tail.
        # otherwise carry over the value form nums[i - 1]
        res = 1
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        if dp[j] + 1 > res:
                            res = dp[j] + 1
        print(dp)
        return res






        