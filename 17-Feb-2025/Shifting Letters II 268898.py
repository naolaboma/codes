# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        n = len(s)
        opera = [0] * (n + 1)
        for start, end, direction in shifts:
            if direction == 1:
                opera[start] += 1
                opera[end + 1] -= 1
            elif direction == 0:
                opera[start] -= 1
                opera[end + 1] += 1
        for i in range(1, n):
            opera[i] += opera[i - 1]
        for j in range(n):
            s[j] = chr((ord(s[j]) - 97 + opera[j]) % 26 + 97)
        return "".join(s)