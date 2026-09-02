class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # seems like we want backtracing
        # explore each combination of numbers
        res = []
        used = set() # this set affects the next level
        def dfs(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in used:
                    perm.append(nums[i])
                    used.add(nums[i])
                    dfs(perm)
                    perm.pop()
                    used.remove(nums[i])
        dfs([])
        return res


            
            
        