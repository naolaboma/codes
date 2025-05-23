# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        tsum = n*(n + 1)//2
        csum = sum(nums)
        return tsum - csum
