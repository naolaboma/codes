# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False 
        stack = []
        m = nums[0]
        for j in range(1, len(nums)):
            while stack and stack[-1][0] <= nums[j]:
                stack.pop()
            if stack and stack[-1][1] < nums[j]:
                return True
            stack.append((nums[j], m))
            m = min(m, nums[j])
        return False