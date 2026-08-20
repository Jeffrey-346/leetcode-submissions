class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # idea: maintain a max heap of size window and a frequency dict
        # check heap max against freq. 
        # if the frequency of the max is zero, remove it from heap. 
        heap = []
        freq = defaultdict(int)
        # intialize window
        l, r = 0, k - 1
        res = []
        # set up the first window
        for i in range(l, r + 1):
            heapq.heappush(heap, -nums[i])
            freq[nums[i]] += 1

        # now begin the actual sliding part...
        while r < len(nums):
            # find the max of the window
            while freq[-heap[0]] == 0:
                heapq.heappop(heap)
            curr_max = heap[0]
            res.append(-curr_max)

            # shift right
            freq[nums[l]] -= 1
            l += 1
            r += 1
            if r == len(nums):
                break
            freq[nums[r]] += 1
            heapq.heappush(heap, -nums[r])
        return res


        