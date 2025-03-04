# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = Counter(s)
        return "1"*(c.get("1", 0)-1) + "0"*(c.get("0", 0))+"1"