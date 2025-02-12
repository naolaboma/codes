# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        r1 = sorted(costs)
        if r1[0]>coins:
            return 0
        count=0
        summ = 0
        for i in range(n):
            summ+=r1[i]
            if summ>coins:
                break
            count+=1
        return count