# Problem: Find the Middle Index in Array - https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        prsum = 0
        for i, num in enumerate(nums):
            if prsum == summ - prsum - num:
                return i
            prsum += num
        return -1