# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        st = list(map(str, nums))
        tr = []
        for c in st:
            for j in range(len(c)):
                tr.append(c[j])
        trs = list(map(int, tr))
        return trs