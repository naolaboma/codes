# Problem: Palindrome Number  - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        orig = x
        reversee = 0
        while x>0:
            digit = x % 10
            reversee = reversee*10 + digit
            x = x//10
        return orig == reversee
