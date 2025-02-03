# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevaMaps = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevaMaps:
                return [prevaMaps[diff], i]
            prevaMaps[n] = i
        return