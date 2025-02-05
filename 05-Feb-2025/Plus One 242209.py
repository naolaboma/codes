# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carrier = 0
        i = n-1
        while i >=0:
            if digits[i] < 9:
                digits[i] +=1
                carrier=0
                break
            elif digits[i]==9:
                digits[i]=0
                carrier=1
            i-=1
        if carrier >0:
            digits.insert(0, carrier)
        return digits