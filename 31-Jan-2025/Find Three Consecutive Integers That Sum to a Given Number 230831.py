# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = (num-3)//3
        if ((3*x) +3)== num:
            return [x, x+1, x+2]

        else:
            return []
        