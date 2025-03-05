# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for car in s:
            if car == "*":
                stack.pop()
            else:
                stack.append(car)
        return "".join(stack)