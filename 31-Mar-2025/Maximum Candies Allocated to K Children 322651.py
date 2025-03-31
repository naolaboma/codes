# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def ispossible(max_candies):
            res = 0
            for candy in  candies:
                res += candy//max_candies
            if res >= k:
                return True
            return False
        if sum(candies) < k:
            return 0
        left, right = 1, sum(candies)//k
        while left < right:
            mid = (left + right)//2 + 1
            if ispossible(mid):
                left = mid
            else:
                right = mid - 1
        return left