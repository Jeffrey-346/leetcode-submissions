class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        totals = [-1] * 2
        totals[0] = cost[0]
        totals[1] = cost[1]
        for i in range(2, n):
            save = totals[1]
            totals[1] = cost[i] + min(totals[1], totals[0])
            totals[0] = save
        return min(totals[0], totals[1])
        