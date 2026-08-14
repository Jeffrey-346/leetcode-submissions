class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = dict()
        for i in range(0, len(nums)):
            curr = nums[i]
            partner = target - curr
            if partner in my_dict.keys():
                return [my_dict[partner], i]
            my_dict[curr] = i
        