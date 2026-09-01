class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # let's try to do "backtracking"
        res = []
        def dfs(start, path, total):
            if total > target:
                return
            if total == target:
                res.append(path.copy())
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i, path, total + nums[i])
                path.pop()
        dfs(0, [], 0)
        return res





        