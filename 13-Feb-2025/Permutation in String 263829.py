# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        window_count = Counter()
        window_size = len(s1)
        for i in range(len(s2)):
            window_count[s2[i]] += 1
            if i >= window_size:
                if window_count[s2[i - window_size]] == 1:
                    del window_count[s2[i - window_size]]
                else:
                    window_count[s2[i - window_size]] -= 1
            if window_count == s1_count:
                return True
        
        return False