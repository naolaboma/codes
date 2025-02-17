# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        cursum = 0
        for n in nums:
            if cursum < 0:
                cursum = 0
            cursum +=n
            maxSub = max(maxSub, cursum)
        return maxSub