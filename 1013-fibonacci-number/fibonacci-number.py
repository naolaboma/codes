class Solution:
    def fib(self, n: int) -> int:
        # Base case for 0
        if n == 0:
            return 0
        
        # Initialize memo with None
        memo = [None] * (n + 1)
        
        def sol(n):
            # Check if value is already computed
            if memo[n] is not None:
                return memo[n]
            
            # Base cases for 1 and 2
            if n == 1 or n == 2:
                result = 1
            else:
                result = sol(n - 1) + sol(n - 2)

            # Store and return result
            memo[n] = result
            return result
            
        return sol(n)
