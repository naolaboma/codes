# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = ""
        count = 0
        for i in range(len(s)):
            res+=s[i]
            c1 = Counter(res)
            if c1.get('R') == c1.get('L'):
                res = ""
                count+=1
        return count