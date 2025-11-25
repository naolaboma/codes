# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        c = 0
        p = n-1
        while p >= 0:
            if digits[p]==9:
                digits[p] = 0
                c=1
                p-=1
            else:
                digits[p]+=1
                c-=1
                break
        print(c)
        if c > 0:
            digits.insert(0, c)
        return digits