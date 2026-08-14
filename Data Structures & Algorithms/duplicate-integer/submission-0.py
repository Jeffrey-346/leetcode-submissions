class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for elm in nums:
            if elm in my_set:
                return True
            my_set.add(elm)
        return False
        