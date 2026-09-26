class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # real question: is there a subset that adds up to total / 2?
        total = 0
        for num in nums:
            total += num
        if total % 2 != 0:
            return False
        target = total // 2

        def dfs(i, curr):
            if i == len(nums) or curr > target:
                return False
            if curr == target:
                return True
            curr += nums[i]
            if dfs(i + 1, curr):
                return True
            curr -= nums[i]
            if dfs(i + 1, curr):
                return True
            return False
        return dfs(0, 0)
            
        




        