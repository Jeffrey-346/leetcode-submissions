class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # initialize with empty list
        # loop through each num
        # for each list in res, make a new list copy and append num 

        res = [[]]
        for num in nums:
            new_sets = []
            for s in res:
                new_set = s.copy()
                new_set.append(num)
                new_sets.append(new_set)
            res.extend(new_sets)
        return res

        