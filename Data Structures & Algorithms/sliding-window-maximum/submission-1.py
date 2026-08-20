class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # let's trying the deque solution
        q = deque()
        l, r = 0, 0
        res = []
        
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # if we are out of range, remove the index from q
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res
