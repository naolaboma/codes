# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return n
        a,b = 0 , 1
        for i in range(2, n+1):
            tmp = b
            b = a+b
            a = tmp
        return b