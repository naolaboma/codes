# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = list(s)
        dictt = dict(zip(indices, res))
        so = dict(sorted(dictt.items()))
        return "".join(so.values())