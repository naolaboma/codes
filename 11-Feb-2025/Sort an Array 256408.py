# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mi = min(nums)
        ma = max(nums)
        count = [0] * (ma - mi + 1)
        for num in nums:
            count[num - mi] += 1
        s_a = []
        for i in range(len(count)):
            s_a.extend([i + mi] * count[i])
        return s_a