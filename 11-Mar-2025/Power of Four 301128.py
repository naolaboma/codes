# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n <= 0:
            return False
            
        return (n & (n - 1)) == 0 and (n & 0x55555555) != 0
