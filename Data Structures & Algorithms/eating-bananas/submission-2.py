class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float('inf')
        l, r = 1, max(piles)
        while l <= r:
            rate = (l + r) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / rate)
            if time <= h:
                res = min(rate, res)
                r = rate - 1
            if time > h:
                l = rate + 1
        return res