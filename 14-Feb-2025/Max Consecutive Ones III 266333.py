# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0  
        res = 0  
        count = 0  
        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1  
            while count > k:
                if nums[l] == 0:
                    count -= 1
                l += 1
            res = max(res, r - l + 1)
        return res