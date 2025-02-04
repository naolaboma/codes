# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c = Counter(s)
        ls = list(c.values())
        flag = True
        for i in range(1, len(ls)):
            if ls[i] != ls[i - 1]:
                flag = False
                break
        return flag