# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strr = ""
        for d in digits:
            strr+=str(d)
        res = str(int(strr) +1)
        return list(map(int, res))