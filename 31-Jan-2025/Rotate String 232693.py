# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        flagg = False
        for i in range(len(s)):
            s = s[1:n] + s[0]
            if s == goal:
                flagg = True
                break
        return flagg