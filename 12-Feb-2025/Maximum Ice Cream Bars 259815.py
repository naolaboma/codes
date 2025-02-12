# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        summ = 0
        for i in range(len(costs)):
            summ+=costs[i]
            if summ>coins:
                break
            count+=1
        return count