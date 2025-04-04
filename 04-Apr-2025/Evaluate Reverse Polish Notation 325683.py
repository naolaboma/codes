# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif t == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif t == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            elif t=="/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(t))
                
        return stack.pop()