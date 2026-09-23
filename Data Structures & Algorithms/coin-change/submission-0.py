class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # array of size amount
        res = [float('inf')] * (amount + 1)
        res[0] = 0
        for i in range(1, len(res)):
            for coin in coins:
                previous_amount_index = i - coin
                if previous_amount_index >= 0 and res[previous_amount_index] != float("inf"):
                    res[i] = min(res[previous_amount_index] + 1, res[i])
        return res[-1] if res[-1] != float('inf') else -1

                
        