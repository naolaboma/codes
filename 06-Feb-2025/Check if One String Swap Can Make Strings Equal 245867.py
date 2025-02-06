# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2)
        if s1 == s2:
            return True
        elif c1 != c2:
            return False
        count = 0
        flag = True
        for i in range(len(s2)):
            if s1[i]!=s2[i]:
                count+=1
            if count > 2:
                flag = False
                break
        return flag
        
        