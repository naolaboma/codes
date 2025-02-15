# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for start, end in ranges:
            if end < left: continue 
            if start > left: return False
            if end >= right: return True 
            left = end + 1
        return False