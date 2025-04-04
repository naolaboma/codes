# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        coun = Counter(nums)
        output = []
        for k, v in coun.items():
            if v ==2:
                output.append(k)
        return output