# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxSub = nums[0]
        minSub = nums[0]
        cursum = 0
        cursumm = 0

        for n in nums:
            if cursum < 0:
                cursum = 0
            if cursumm > 0:
                cursumm = 0 
            cursum +=n
            cursumm+=n
            maxSub = max(maxSub, cursum)
            minSub = min(minSub, cursumm)
        return max(abs(maxSub), abs(minSub))