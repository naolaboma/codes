# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        c1 = Counter(s)
        sc = dict(sorted(c1.items(), key=lambda item: item[1], reverse = True))
        res=""
        for k, v in sc.items():
            res+=v*k
        return res