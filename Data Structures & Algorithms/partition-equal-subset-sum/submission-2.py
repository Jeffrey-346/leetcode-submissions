class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        sums = set()
        sums.add(nums[-1])
        sums.add(0)

        if target in sums:
            return True

        for i in range(len(nums) - 2, -1, -1):
            sums_copy = sums.copy()
            for elm in sums_copy:
                if elm + nums[i] == target:
                    return True
                sums.add(elm + nums[i])
        return False





        