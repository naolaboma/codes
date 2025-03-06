# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        track = {}
        for num in nums2:
            while stack and stack[-1]< num:
                val = stack.pop()
                track[val] = num
            stack.append(num)
        ans = []
        for num in nums1:
            if num in track:
                ans.append(track[num])
            else:
                ans.append(-1)
        return ans