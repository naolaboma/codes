# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        i = 0
        while i < n:
            if i<n-1 and (not nums[i] ^ nums[i+1]):
                i +=2
                continue
            else:
                return nums[i]