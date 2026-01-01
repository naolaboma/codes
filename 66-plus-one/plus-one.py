class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += c
            c=0
            if digits[i] > 9:
                c = 1
                digits[i] = 0
        if c == 1:
            digits.insert(0, c)
        return digits