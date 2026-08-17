class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # super naive is for each iterate just iterate through all element
        # multiply if it is not the same index

        # O(n) with division would be to multiply all nums together and
        # then at each index divide by the current index num

        # O(n) without division by:
        # -maintain two lists : pre and post
        # -fill pre the result of multiplying all elements before i
            #-this is O(n) bc you just need the previous index
        # -fill post with the res of mult all elements after i
        # -return the multiplaction of pre and post

        # [1, 1, 2, 8]
        # - for curr i of input: multiply previous i of input * prev i of
        # pre list. Start with one

        # work backwards/flip the list [48, 24, 6, 1]

        # pre:  [1, -1, 0, 0, 0]
        # post: [0, 6, 6, 3, 1]

        pre = [1] * len(nums)
        post = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                pre[i] = 1
            else:
                pre[i] = pre[i - 1] * nums[i - 1]
        
        for i in range(len(nums) -1, -1, -1):
            if i == (len(nums) - 1):
                post[i] = 1
            else:
                post[i] = post[i + 1] * nums[i + 1]
        
        res = [pre[i] * post[i] for i in range(len(nums))]

        return res
            



        