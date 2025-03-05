# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        for char in s:
            if char!="#":
                s1.append(char)
            else:
                if s1:
                    s1.pop()
        for char in t:
            if char=="#":
                if s2:
                    s2.pop()
            else:
                s2.append(char)
        return s1 == s2