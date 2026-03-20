class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        memo = [None]*(n + 1)
        
        def sol(n):
            if memo[n] != None:
                return memo[n]
            if n == 1 or n == 2:
                result = 1
            else:
                result = sol(n-1) + sol(n-2)

            memo[n] = result
            return result
        return sol(n)
            