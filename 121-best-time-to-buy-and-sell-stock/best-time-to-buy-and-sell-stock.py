class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyp = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            currentP = prices[i]
            buyp = min(buyp, currentP)
            profit = max(profit, currentP - buyp)
        return profit