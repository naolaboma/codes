# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        se = set(nums)
        res = []
        for i in range(1, n+1):
            if i not in se:
                res.append(i)
        return res