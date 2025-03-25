# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        sqr = 0
        l, r = 0, x
        while l <= r:
            mid = (l+r) // 2
            if mid*mid <=x:
                sqr = mid
                l = mid +1
            else:
                r = mid-1
        return sqr