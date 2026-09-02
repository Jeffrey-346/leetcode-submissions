class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # one solution is to build up the subsets (add new element each    
        # iteration to all lists) 
        nums = sorted(nums)
        res = []
        seen = set()
        subset = []

        def dfs(i):
            if i == len(nums):
                if tuple(subset) not in seen:
                    res.append(subset.copy())
                    seen.add(tuple(subset))
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res

        

        


