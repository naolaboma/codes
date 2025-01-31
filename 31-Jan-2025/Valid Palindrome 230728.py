# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_arr =[]

        for ch in s:
            if(ch.isalnum()):
                new_arr.append(ch.lower())
        return new_arr == new_arr[::-1]