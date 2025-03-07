# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for p in s:
            if p == "(":
                stack.append(0)
            elif p == ")":
                r = stack.pop()
                stack[-1]+=max(2*r, 1)
        return stack[0]