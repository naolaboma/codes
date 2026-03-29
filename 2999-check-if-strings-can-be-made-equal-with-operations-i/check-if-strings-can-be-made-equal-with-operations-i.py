class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        li = [s1, str(s1[2] + s1[1] + s1[0] + s1[3]), str(s1[0] + s1[3] + s1[2] + s1[1])]
        li2 = [s2, str(s2[2] + s2[1] + s2[0] + s2[3]), str(s2[0] + s2[3] + s2[2] + s2[1])]
        for x in li2:
            if x in li:
                return True
        return False