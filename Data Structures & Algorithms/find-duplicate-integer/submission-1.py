class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # naively we just use a set
        # key is that nums is in range [1, n] where there are n + 1 elms

        # here's the idea, may be way too big, but
        # digit determines place (ones, tens, etc.)
        # add each digit. Check if the place has already been filled first

        n = 0
        for num in nums:
            if (1 << num & n):
                return num
            else: n += 1 << num


        