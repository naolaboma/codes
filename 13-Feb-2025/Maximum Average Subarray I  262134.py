# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        mavg = summ/k
        for i in range(len(nums)-k):
            summ = summ - nums[i] + nums[i+k]
            mavg = max(mavg, summ/k)
        return mavg