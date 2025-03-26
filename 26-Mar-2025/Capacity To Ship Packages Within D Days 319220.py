# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def validate(capacity):
            cur = 0
            daysc = 1
            for weight in weights:
                cur += weight
                if cur > capacity:
                    daysc += 1
                    cur = weight
                if daysc > days:
                    return False
            return True

        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            if validate(mid):
                r = mid
            else:
                l = mid+1
        return l