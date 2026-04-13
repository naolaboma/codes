class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = prices[0]
        profit = 0
        for p in prices:
            if p>=b:
                profit = max(profit, p - b)
            else:
                b = p
        return profit