class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for l in range(len(prices)):
            for r in range(l+1, len(prices)):
                profit = prices[r] - prices[l]
                if profit > max:
                    max = profit
        return max
            