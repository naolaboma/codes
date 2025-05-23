# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x^y
        y = str(bin(res))
        x = y.count("1")
        return x