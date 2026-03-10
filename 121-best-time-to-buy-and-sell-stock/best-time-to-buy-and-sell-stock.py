class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyp = prices[0]
        profit = 0
        for p in prices[1:]:
            if buyp > p:
                buyp = p
            profit = max(profit, p - buyp)
        return profit