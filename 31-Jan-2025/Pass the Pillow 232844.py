# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = 2 * (n - 1)    
        reduced_time = time % cycle_length
        if reduced_time <= n - 1:
            return reduced_time + 1
        else:
            return n - (reduced_time - (n - 1))