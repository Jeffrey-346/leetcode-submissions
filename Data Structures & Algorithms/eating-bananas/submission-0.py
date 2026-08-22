class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # naive solution:
        # start with eating 1 banana per hour
        # check if that let's us finish within h
        # if not increment
        # return when successful
        # O(n * m)

        # better solution:
        # (1, m)
        # perform binary search
        # start at middle value
        # if we succeed: Then search lower half
        # if we fail: Then search the upper half

        m = 0
        for pile in piles:
            m = max(m, pile)
        l, r = 1, m
        while l < r:
            time = 0
            k = (l + r) // 2
            for pile in piles:
                time += math.ceil(pile / k)
            if time <= h:
                r = k
            else:
                l = k + 1
        return l

        