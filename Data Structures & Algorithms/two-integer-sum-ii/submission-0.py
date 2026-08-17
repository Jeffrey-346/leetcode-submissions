class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # another two pointer problem
        # move l and r depending on if the current sum is too large or too
        # small

        l, r = 0, len(numbers) - 1

        while 1:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
        