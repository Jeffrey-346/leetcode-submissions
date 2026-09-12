class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        totals = [-1] * n
        totals[0] = cost[0]
        totals[1] = cost[1]
        for i in range(2, n):
            totals[i] = cost[i] + min(totals[i - 1], totals[i - 2])
        return min(totals[n -1], totals[n - 2])
        
        