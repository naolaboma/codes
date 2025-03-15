# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7        
        def expo(x: int, num: int) -> int:
            if num == 0:
                return 1  
            elif num & 1 == 0:
                return expo(x ** 2 % MOD, num // 2)
            return x * expo(x, num - 1) % MOD
        return 5 ** (n % 2) * expo(20, n // 2) % MOD