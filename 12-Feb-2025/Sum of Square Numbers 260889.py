# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c<0:
            return False
        a,b = 0,int(sqrt(c))
        while a <= b:
            cursu = a**2 + b**2
            if cursu == c:
                return True
            elif cursu < c:
                a+=1
            else:
                b-=1
        return False