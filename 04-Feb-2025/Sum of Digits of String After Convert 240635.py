# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ss = ""
        for i in range(len(s)):
            ss += str(ord(s[i])-96)
        ml = list(map(int, ss))
        for j in range(k):
            res = ""
            res+=str(sum(ml))
            ml=list(map(int, res))
        return int(res)

