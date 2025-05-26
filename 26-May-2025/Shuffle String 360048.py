# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s = list(s)
        n = len(s)
        res = [" "]*n
        for i in range(n):
            res[indices[i]] = s[i]
        return "".join(res)