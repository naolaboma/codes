# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            s = list(map(str, s.split("@")))
            coded = s[0].lower()
            exten = s[1].lower()
            s1 = coded[0]+ "*****"+ coded[len(coded)-1] + "@" + exten
            return s1
        else:
            res = "***-***-"
            sett = {'+', '-', '(', ')', ' '}
            s = list(s)
            s= [k for k in s if k not in sett]
            if len(s) ==10:
                return res + ''.join(s[-4:])
            elif len(s) ==11:
                return "+*-"+ res + ''.join(s[-4:])
            elif len(s) ==12:
                return "+**-"+ res + ''.join(s[-4:])
            elif len(s) == 13:
                return "+***-"+ res + ''.join(s[-4:])