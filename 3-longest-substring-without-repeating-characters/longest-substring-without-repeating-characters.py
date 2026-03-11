class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        maxi = 0
        for p in range(len(s)):
            while s[p] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[p])
            maxi = max(maxi, p-l+1)
        return maxi