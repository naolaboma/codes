# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        prsum = 0
        for i, num in enumerate(nums):
            if prsum == summ - prsum - num:
                return i
            prsum += num
        return -1