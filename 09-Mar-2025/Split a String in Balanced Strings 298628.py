# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        balance = 0
        for char in s:
            if char == 'R':
                balance += 1
            elif char == 'L':
                
                balance -= 1
            if balance == 0:
                count += 1    
        return count