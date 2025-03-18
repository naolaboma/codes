# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        cur = ""
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
                
            elif char == "[":
                stack.append((cur, num))
                cur, num = "", 0
            elif char == "]":
                prev, repeat = stack.pop()
                cur = prev + repeat * cur
            else:
                cur += char
        return cur
            