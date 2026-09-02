class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # let's see if we can do it without the seen dict
        # seems like if it is the same as the previous number, we
        # can skip the whole branch
        nums = sorted(nums)
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                if len(nums) == 0:
                    res.append(subset.copy())
                    return 
                else:
                    res.append(subset.copy())
                    return
    
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            # if nums[i + 1] 
            i += 1 
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            dfs(i)
        dfs(0)
        return res
        