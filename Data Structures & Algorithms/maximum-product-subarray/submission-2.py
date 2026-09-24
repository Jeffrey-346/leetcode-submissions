class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = []
        res.append([nums[0], nums[0]])
        for i in range(1, len(nums)):
            max_sub = max(res[i - 1][0] * nums[i], res[i - 1][1] * nums[i], nums[i])
            min_sub = min(res[i - 1][0] * nums[i], res[i - 1][1] * nums[i], nums[i])
            res.append([max_sub, min_sub])
        return max(res[i][0] for i in range(len(res)))
        

        