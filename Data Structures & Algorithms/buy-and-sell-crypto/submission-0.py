class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # track lowest possible buy. And then if the profit difference is
        # greater than profit, update profit. If lower possible buy,      
        # update buy
        buy = None
        for i in range(len(prices)):
            if i == 0:
                buy = prices[i]
            elif prices[i] < buy:
                buy = prices[i]
            else:
                profit = max(profit, prices[i] - buy)
        return profit

            

        