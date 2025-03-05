# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for fol in logs:
            if fol == "../":
                if stack:
                    stack.pop()
            elif fol == "./":
                continue
            else:
                stack.append(fol)
        return len(stack)