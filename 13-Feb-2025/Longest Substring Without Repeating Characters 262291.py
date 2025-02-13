# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ind = {}
        mlen = 0
        start = 0
        for i, char in enumerate(s):
            if char in ind and ind[char] >= start:
                start = ind[char] + 1
            ind[char] = i
            mlen = max(mlen, i - start + 1)
        return mlen
            