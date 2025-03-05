# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pref  = path.split("/")
        for car in pref:
            if car == "." or car== "":
                continue
            elif car == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(car)
        return "/" + "/".join(stack)